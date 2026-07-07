"""Builder functions for HR-001 through HR-010 Haryana packages."""

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

HARYANA_SLUG = "haryana"


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


def build_hr_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-001'
    tour_code = 'TRAGUIN-HAR-KUR-001'
    title = 'Dharmakshetra Kurukshetra Heritage Trail'
    duration = '03 Nights / 04 Days'
    slug = 'hr-001-kurukshetra-heritage-trail'
    itin_slug = 'hr-001-kurukshetra-heritage-trail-itinerary'
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
            _ph('Serial code HR-001 | TRAGUIN tour code TRAGUIN-HAR-KUR-001', 1),
            _ph('State / Country: Haryana / India | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Haryana', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI', 7),
            _ph('TRAGUIN Signature Experience: Enjoy a private, expert-led heritage walk through the ancient relics of', 8),
            _ph('Curated by TRAGUIN Experts: Every detail, from driving times to sunset views over Brahma Sarovar, has', 9),
            _ph('Premium Handpicked Hotels: We choose only properties that maintain exceptional service, high hygiene', 10),
            _ph('Luxury Transportation: Travel safely with our fully verified, polite chauffeurs who know the local heritage', 11),
            _ph('Standard hotel check-in time is 14:00 hrs and check-out is 11:00 hrs. Early access depends on availability.', 12),
            _ph('To maintain the sanctity of religious locations, visitors are advised to wear modest clothing during temple', 13)
        ],
        moods=['Heritage', 'Family', 'Spiritual'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dharmakshetra Kurukshetra Heritage Trail',
        overview='Dharmakshetra Kurukshetra Heritage Trail • 3 Nights / 4 Days Embark on an extraordinary journey through time with the Best Kurukshetra Tour Package, meticulously crafted for selective travelers by TRAGUIN. Known as the cradle of Vedic civilization and the sacred land where the celestial song of the Bhagavad Gita was delivered, Kurukshetra is a canvas of deep spirituality, profound heritage, and timeless epic lore. This premium Kurukshetra Family Tour offers a beautiful harmony of luxury hospitality, historical exploration, and seamless arrangements, TRAGUIN Premium Kurukshetra Heritage Tour 1 ensuring your family uncovers the top tourist places in Kurukshetra while creating unforgettable memories.\n\nTOUR OVERVIEW\nDesigned specifically as a premium family heritage gateway, this Luxury Kurukshetra Holiday by TRAGUIN promises an immaculate, high-end travel experience. Travel back into India’s glorious past while relaxing in absolute modern comfort. From private luxury transfers to premium stays and expert-guided storytelling sessions at iconic attractions, every detail is engineered to perfection. Travel Dates Flexible / Customized Independent FIT Leaves Group / FIT Customized Private Family Tour (FIT) Vehicle Assigned Chauffeur-Driven Premium Air-Conditioned Luxury Sedan / Innova Crysta Meal Plan CPAI (Premium Breakfast Included) / MAPAI (Breakfast & Dinner Included) Route Outline Delhi / Chandigarh → Kurukshetra Sightseeing → Jyotisar → Thanesar → Delhi / Chandigarh TRAGUIN Curated Note Includes exclusive VIP darshan arrangements, a private local expert historian guide, a specialized traditional Haryanvi high-tea experience, and customized premium travel kits for children.\n\nWHY VISIT KURUKSHETRA? EXCLUSIVE DESTINATION HIGHLIGHTS\nOpting for a Premium Kurukshetra Experience means standing precisely where history changed forever. Kurukshetra is not merely a spiritual destination; it is an epic open-air living museum. Recognized globally as one of the most searches experiences for spiritual tourism, it attracts thousands looking for historical depth, architectural wonders, and deep-seated Indian heritage. The Best Time to Visit Kurukshetra is from October to March when the weather turns pleasantly cool, ideal for outdoor exploring and photographing the beautiful reflection of historical shrines. Families choose our Kurukshetra Heritage Packages to introduce their children to the lessons of the Mahabharata, explore popular Instagram locations like the massive multi-tiered Brahma Sarovar, and experience the cultural highlights of Thanesar. Whether you are seeking adventure at science museums, looking for handloom shopping, or wanting to sit peacefully under ancient holy trees, TRAGUIN Kurukshetra Packages cater perfectly to every generation of your family. TRAGUIN Premium Kurukshetra Heritage Tour 2 DAY WISE ITINERARY',
        seo_title='HR-001 | Dharmakshetra Kurukshetra Heritage Trail | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Haryana package (HR-001 / TRAGUIN-HAR-KUR-001): Haryana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: WELCOME TO THE SACRED LAND OF MAHABHARATA', 1),
            _ih('Day 02: THE ETERNAL WISDOM & SCIENTIFIC WONDERS', 2),
            _ih('Day 03: ARCHITECTURAL WONDERS & SPIRITUAL FORTRESSES', 3),
            _ih('Day 04: FAREWELL TO THE LAND OF LEGENDS', 4),
            _ih('TRAGUIN Signature Experience: Enjoy a private, expert-led heritage walk through the ancient relics of', 5),
            _ih('Curated by TRAGUIN Experts: Every detail, from driving times to sunset views over Brahma Sarovar, has', 6),
            _ih('Premium Handpicked Hotels: We choose only properties that maintain exceptional service, high hygiene', 7)
        ],
        days=[
            _day(
                1,
                'WELCOME TO THE SACRED LAND OF MAHABHARATA',
                (
                    'ARRIVE IN KURUKSHETRA – THE HOLY COMMENCEMENT Your luxury escape begins as you arrive in Delhi or Chandigarh, where a premium, chauffeur-driven vehicle arranged by TRAGUIN awaits your family. Enjoy a smooth and comfortable highway drive toward the historic town of Kurukshetra. Upon arrival, check into your handpicked premium hotel and experience a warm traditional welcome. In the afternoon, proceed for your first immersive experience at the spectacular Brahma Sarovar, one of the most majestic and largest man-made water bodies in Asia. According to legends, Lord Brahma created the universe from this very spot. Walk along the wide red-sandstone banks, feel the calm spiritual atmosphere, and capture beautiful landscape photos as the sun goes down. Stay back for the spectacular evening Maha Aarti, where hundreds of floating oil lamps illuminate the sacred waters. lakeside.'
                ),
                [
                    'Sightseeing Included: Brahma Sarovar, Sacred Sarovar Complex, Evening Maha Aarti.',
                    'Optional Activities: Guided photography walk around the ancient shrines bordering the sarovar.',
                    'Evening Experience: Experiencing the beautiful and spiritually uplifting sound-and-light presentation at the',
                    'Overnight Stay: Handpicked Premium Hotel in Kurukshetra.',
                    'Meals Included: Welcome Drinks & Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'THE ETERNAL WISDOM & SCIENTIFIC WONDERS',
                (
                    'JYOTISAR BIRTHPLACE OF GITA & MODERN KNOWLEDGE HUBS Start your morning with a premium curated breakfast at the hotel. Today, TRAGUIN takes your family to Jyotisar, arguably the most iconic attraction in Kurukshetra. Here, beneath the shade of an immortal Banyan Tree (Akshay Vat) that has survived for over 5,000 years, Lord Krishna delivered the eternal message of the Bhagavad Gita to Arjun before the great war. Stand on this hallowed ground and feel the incredible emotional storytelling brought to life by our private historian guide. Enjoy a newly launched world-class multimedia laser and light show that depicts the cosmic form (Vishwaroopam) of Krishna. Transition from ancient history to modern ingenuity in the afternoon by visiting the Kurukshetra Panorama and Science Centre. This unique museum houses a breathtaking 34-foot-high cylindrical panorama painting that brings the 18-day battle of Mahabharata to life with realistic sound and light effects, making it a favorite for children and a highlight of any Kurukshetra Family Tour. Next, visit the nearby Sri Krishna Museum to view rare sculptures, antiquities, and beautiful artwork depicting the life of Krishna. TRAGUIN Premium Kurukshetra Heritage Tour 3 Krishna Museum.'
                ),
                [
                    'Sightseeing Included: Jyotisar Holy Tree, Multimedia Light Show, Kurukshetra Panorama & Science Centre, Sri',
                    "Optional Activities: Interactive learning sessions for kids inside the science center's gallery.",
                    'Evening Experience: A relaxing stroll in the beautifully manicured gardens surrounding the museum complex.',
                    'Overnight Stay: Handpicked Premium Hotel in Kurukshetra.',
                    'Meals Included: Premium Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'ARCHITECTURAL WONDERS & SPIRITUAL FORTRESSES',
                (
                    "EXPLORING THANESAR, SHEIKH CHILLI TOMB & BHADRAKALI SHAKTIPEETH After a delicious breakfast, dedicate your day to discovering the architectural marvels and deep spiritual hubs of Thanesar. Your first stop is the elegant Sheikh Chilli's Tomb, a stunning Mughal-era monument made of striking white marble and red sandstone. Often called the 'Taj of Haryana,' this architectural gem provides magnificent backdrops for family photography and serves as a popular Instagram location. Learn about the rich Sufi culture and explore the archeological museum located within the compound. Next, visit the highly revered Maa Bhadrakali Temple, one of the 51 sacred Shaktipeeths in India. It is believed that the right ankle of Goddess Sati fell here. Devotees traditionally offer beautiful clay horses to the temple upon the fulfillment of their wishes. Afterward, visit the historical Harsh Ka Tila, which holds structural remains dating from the 7th-century reign of King Harshavardhana. End your sightseeing day at the modern and grand Birla Gita Mandir, famous for its walls entirely carved with the verses of the Bhagavad Gita. luxury farm."
                ),
                [
                    'Sightseeing Included: Sheikh Chilli Tomb, Maa Bhadrakali Shaktipeeth, Harsh Ka Tila, Birla Mandir.',
                    'Optional Activities: Private Vedic chanting and blessings ritual arranged at the Bhadrakali Temple.',
                    'Evening Experience: Authentic Haryanvi High-Tea experience featuring local delicacies at a curated rustic',
                    'Overnight Stay: Handpicked Premium Hotel in Kurukshetra.',
                    'Meals Included: Premium Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'FAREWELL TO THE LAND OF LEGENDS',
                (
                    'Enjoy your final gourmet breakfast at the resort before checking out. Spend your morning checking out local handloom markets to pick up unique souvenirs, premium Phulkari embroideries, and traditional wooden handicrafts. Take a final look at the beautiful town and reflect on the breathtaking landscapes and profound heritage you have witnessed over the last few days. TRAGUIN Premium Kurukshetra Heritage Tour 4 Your premium chauffeur will then drive you back to Delhi or Chandigarh airport/railway station for your journey home. Your luxury Kurukshetra Sightseeing adventure concludes with beautiful, long-lasting memories of a perfectly managed holiday, curated by TRAGUIN.'
                ),
                [
                    'SHOPPING: , MEMORIES & DEPARTURE',
                    'Sightseeing Included: Local Artisan Markets, Souvenir Shopping Tour.',
                    'Optional Activities: Quick en-route stop at a premium highway lounge for lunch.',
                    'Evening Experience: Dropping off safely at the airport or station.',
                    'Overnight Stay: None.',
                    'Meals Included: Premium Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Kimaya / Equivalent Premium',
                'Kurukshetra',
                '03 Nights',
                'Deluxe',
                'Property',
                'Executive Room',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Kimaya / Equivalent Premium | Property | Executive Room',
            ),
            _hotel(
                'Hotel Red Castle / Divine Clerks',
                'Kurukshetra',
                '03 Nights',
                'Premium',
                'Super Deluxe',
                'Room',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Red Castle / Divine Clerks | Super Deluxe | Room',
            ),
            _hotel(
                'The Pearl Resort & Spa / Similar',
                'Kurukshetra',
                '03 Nights',
                'Luxury',
                'Elite Stay',
                'Luxury Suite',
                4,
                3,
                description='OPTION 03 – LUXURY: The Pearl Resort & Spa / Similar | Elite Stay | Luxury Suite',
            ),
            _hotel(
                'Curated Heritage Boutique Farm &',
                'Kurukshetra',
                '03 Nights',
                'Ultra Luxury',
                'Wellness Villa',
                'Royal Club Villa',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Curated Heritage Boutique Farm & | Wellness Villa | Royal Club Villa',
            )
        ],
        inclusions=[
            _inc_included("Thanesar, unearthing untold secrets of the Harsha Empire. been personally reviewed for maximum family comfort. ratings, and top-tier hospitality. routes inside out. Bring a piece of your Luxury Kurukshetra Holiday back home with you. Kurukshetra is famous for its handloom products, durable brass utensils from neighboring hubs, and beautiful earthenware. Our expert guides will take you to the best local markets where you can find authentic souvenirs. Don't leave without tasting genuine Haryanvi food: enjoy fresh bajra khichri, hot choorma, homemade white butter, and refreshing glasses of sweet lassi at our handpicked premium local dining spots. 03 Nights premium accommodation in handpicked top-rated hotels.", 1),
            _inc_included('Daily multi-cuisine buffet breakfasts and curated gourmet dinners.', 2),
            _inc_included('Private air-conditioned luxury sedan / SUV vehicle for all transfers and sightseeing.', 3),
            _inc_included('Dedicated local historian guide for deep emotional storytelling.', 4),
            _inc_included('VIP Darshan assistance at Maa Bhadrakali Shaktipeeth.', 5),
            _inc_included('Complimentary tickets to the Jyotisar Multimedia Light Show.', 6),
            _inc_included('Welcome drinks, arrival amenities, and refreshing travel kits.', 7),
            _inc_included('24/7 dedicated TRAGUIN guest relationship support.', 8),
            _inc_included('All applicable fuel, parking, toll charges, and state taxes.', 9),
            _inc_included('Airfare, train tickets, or interstate flight connectivity costs.', 10),
            _inc_excluded('Camera fees, video recording charges, or specific monument entry fees.', 11),
            _inc_excluded('Personal expenses such as laundry, phone calls, tips, and mini-bar usage.', 12),
            _inc_excluded('Any extra meal or beverage items ordered outside the pre-fixed menu.', 13),
            _inc_excluded('Optional adventure sports, boat rides, or activities not listed.', 14),
            _inc_excluded('Travel insurance and medical emergency protection.', 15),
            _inc_excluded('GST and statutory luxury cess if applicable at payment.', 16),
        ],
    )
    return package, itinerary

def build_hr_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-002'
    tour_code = 'TRAGUIN-HR-002'
    title = 'Kurukshetra Spiritual Tour'
    duration = '03 Nights / 04 Days'
    slug = 'hr-002-kurukshetra-spiritual-tour'
    itin_slug = 'hr-002-kurukshetra-spiritual-tour-itinerary'
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
            _ph('Serial code HR-002 | TRAGUIN tour code TRAGUIN-HR-002', 1),
            _ph('State / Country: Haryana / India | Category: Pilgrimage / Luxury', 2),
            _ph('Destinations: Kurukshetra & Jyotisar', 3),
            _ph('Ideal for: Families, Spiritual Seekers, Elders', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Scale)', 6),
            _ph('Vehicle / Meals: Chauffeur-Driven Luxury SUV', 7),
            _ph('Route: Delhi / Chandigarh → Kurukshetra → Jyotisar → Thanesar → Delhi / Chandigarh', 8),
            _ph('Signature Experience: An exclusive scriptural storytelling session led by a local scholar, bringing the', 9),
            _ph('Premium Handpicked Hotels: Properties are selected based on strict standards of luxury, hygiene, and', 10),
            _ph('Personalized Assistance: Enjoy 24/7 dedicated support from our travel team to handle any on-the-', 11),
            _ph("& INSIDER RECOMMENDATIONS Shopping Treasures: Take home authentic souvenirs from the local markets, such as beautiful brass artifacts, handcrafted icons of the Geeta Upadesh, and fine devotional scriptures printed in Thanesar. Top Instagram Spots: Capture the giant bronze chariot at Brahma Sarovar, the scenic hanging pathways at Jyotisar, and the beautiful symmetry of Sheikh Chilli's Tomb.", 12),
            _ph('Dress Code Guidelines: Guests are kindly requested to dress modestly when visiting active places of worship. Shoes must', 13)
        ],
        moods=['Spiritual', 'Heritage', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Scale)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kurukshetra Spiritual Tour',
        overview='THE DIVINE LAND OF BHAGAVAD GITA • JYOTISAR • BRAHMA SAROVAR • THANESAR Welcome to the holy land where history, mythology, and eternity converge. The Best Kurukshetra Tour Package designed by TRAGUIN invites you on a profound inner journey to the land of Mahabharata. Experience a uniquely customized Kurukshetra Family Tour rich with sacred rituals, premium handpicked accommodations, and expert storytelling that unlocks ancient epics. Let the timeless verses of the Bhagavad Gita elevate your consciousness on this definitive Luxury Kurukshetra Holiday.\n\nTOUR OVERVIEW\nThis meticulously planned itinerary offers a deep dive into the cultural and spiritual core of ancient India. Seamlessly managed from your arrival to your departure, this Premium Kurukshetra Experience guarantees TRA GUIN TRAGUIN Premium Itinerary - HR-002 a hassle-free exploration of the legendary battlefield, holy water tanks, and historic monuments. Enjoy absolute comfort with a dedicated private luxury transport infrastructure, tailored gourmet meal plans, and highly knowledgeable local guides curated specially for our discerning guests. ROUTE: Delhi / Chandigarh → Kurukshetra → Jyotisar → Thanesar → Delhi / Chandigarh VEHICLE ASSET: Chauffeur-driven Premium Toyota Innova Crysta / Luxury Sedan MEAL ARCHITECTURE: Modified American Plan (MAP) – Daily Premium Breakfast & Imperial Vegetarian Dinners TRAGUIN NOTE: Every element of this spiritual retreat includes a signature touch, featuring exclusive VIP access at major temples, priority seating for the divine sound & light shows, and specialized expert narration.\n\nWHY CHOOSE A PREMIUM KURUKSHETRA SPIRITUAL TOUR?\nKurukshetra is recognized globally as the cradle of Vedic civilization and the sacred site where Lord Krishna delivered the timeless message of the Bhagavad Gita to Arjuna. Booking a high-end Kurukshetra Sightseeing package ensures you witness the transition from grand mythical legends to modern historical discoveries. Explore the Top Tourist Places in Kurukshetra, including the massive Brahma Sarovar—believed to be created by Lord Brahma himself—and the legendary Jyotisar, the literal birthplace of the Gita. This tour balances deep cultural insights with peaceful moments, perfect for a deeply meaningful Kurukshetra Family Tour or a quiet, personalized spiritual retreat. Captured through your camera lens, the vibrant evening arti rituals and centuries-old banyan trees provide exceptional Instagram backdrops while fostering unforgettable personal moments.',
        seo_title='HR-002 | Kurukshetra Spiritual Tour | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Haryana package (HR-002 / TRAGUIN-HR-002): Kurukshetra & Jyotisar with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN THE SACRED REALM & THE GRAND BRAHMA SAROVAR EXPERIENCE', 1),
            _ih('Day 02: JYOTISAR SPIRITUAL CRADLE & EPIC SOUND & LIGHT MASTERPIECE', 2),
            _ih('Day 03: ANTIQUITY OF THANESAR, MYSTICAL SHRINES & ARCHAEOLOGICAL MARVELS', 3),
            _ih('Day 04: SACRED WATER TANKS & HOMEWARD BOUND DEPARTURE', 4),
            _ih('Signature Experience: An exclusive scriptural storytelling session led by a local scholar, bringing the', 5),
            _ih('Premium Handpicked Hotels: Properties are selected based on strict standards of luxury, hygiene, and', 6),
            _ih('Personalized Assistance: Enjoy 24/7 dedicated support from our travel team to handle any on-the-', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN THE SACRED REALM & THE GRAND BRAHMA SAROVAR EXPERIENCE',
                (
                    'Your divine journey begins as our professional chauffeur welcomes you at Delhi or Chandigarh airport/railway station. Travel in style in a luxury private vehicle toward the land of the Mahabharata. Arrive and check into your handpicked premium hotel, where a warm traditional welcome awaits you. In the afternoon, begin your exploration with the magnificent Brahma Sarovar, one of the most iconic Top Tourist Places in Kurukshetra. Walk along its majestic ghats and take in the spiritual energy of this massive solar eclipse bathing destination. As dusk approaches, enjoy an exclusive, front-row view of the evening Maha Arti, followed by a peaceful visit to the nearby historical scriptural exhibits. sculpture. TRAGUIN Premium Itinerary - HR-002'
                ),
                [
                    'SIGHTSEEING INCLUDED: Brahma Sarovar, Birla Gita Mandir, Sri Hanuman Temple.',
                    'EVENING EXPERIENCE: Immersive grand evening oil-lamp Arti at the Brahma Sarovar banks with private seating.',
                    'PHOTOGRAPHY POINTS: Sunset reflection over the grand waters of Brahma Sarovar, the gigantic bronze chariot',
                    'OVERNIGHT STAY: Handpicked Luxury/Premium Hotel in Kurukshetra.',
                    'MEALS INCLUDED: Welcome Drink & Gourmet Vegetarian Dinner.',
                ],
            ),
            _day(
                2,
                'JYOTISAR SPIRITUAL CRADLE & EPIC SOUND & LIGHT MASTERPIECE',
                (
                    'Start your morning with a rejuvenating meditation session. Today we visit Jyotisar, the most revered site on our Kurukshetra Spiritual Tour. Stand beneath the immortal holy Banyan Tree, a living witness to Lord Krishna delivering the sacred dialogue of the Bhagavad Gita to Arjuna. A specialized Vedic scholar will guide you through the history of this holy site. In the afternoon, explore the state-of-the-art Multimedia Mahabharata Gallery. Return to Jyotisar in the evening for an incredible, high-tech Sound and Light Show that brings the timeless ancient epic to life. TRAGUIN Premium Itinerary - HR-002'
                ),
                [
                    'SIGHTSEEING INCLUDED: Jyotisar Holy Birthplace, Krishna Museum, Kurukshetra Panorama & Science Centre.',
                    'OPTIONAL ACTIVITIES: Personalised Sankalpa Puja under the ancient holy Banyan tree.',
                    'EVENING EXPERIENCE: Premium tickets to the Light & Sound spectacular narration at Jyotisar.',
                    'OVERNIGHT STAY: Premium Heritage Hotel setup in Kurukshetra.',
                    'MEALS INCLUDED: Organic Breakfast & Royal Indian Dinner.',
                ],
            ),
            _day(
                3,
                'ANTIQUITY OF THANESAR, MYSTICAL SHRINES & ARCHAEOLOGICAL MARVELS',
                (
                    "Following a premium breakfast, discover the fascinating layers of history at Thanesar. Visit the elegant Sheikh Chilli's Tomb, a architectural masterpiece that highlights the region's diverse past. Next, explore the ancient mounds of Harsh ka Tila, which reveal artifacts from the glorious reign of King Harshavardhana. In the afternoon, visit the sacred Sthaneshwar Mahadev Temple, where the Pandavas prayed to Lord Shiva for victory before the great war. Conclude your daytime sightseeing at the peaceful Bhadrakali Temple, one of the revered 51 Shakti Peethas, offering a quiet space for personal reflection and spiritual connection. Peetha. dining spots."
                ),
                [
                    'SIGHTSEEING INCLUDED: Sheikh Chilli Tomb, Harsh ka Tila, Sthaneshwar Mahadev Shrine, Maa Bhadrakali Shakti',
                    'FOOD SUGGESTIONS: Savor premium authentic North Indian delicacies and traditional local lassi at selected clean',
                    'EVENING EXPERIENCE: A peaceful walk through the local brass craft markets and historical lanes of Thanesar.',
                    'OVERNIGHT STAY: Selected Premium Luxury Resort in Kurukshetra.',
                    'MEALS INCLUDED: Superb Breakfast Buffet & Curated Multi-cuisine Dinner.',
                ],
            ),
            _day(
                4,
                'SACRED WATER TANKS & HOMEWARD BOUND DEPARTURE',
                (
                    'On the final day of your Best Kurukshetra Tour Package, enjoy a relaxed breakfast at the resort. Visit the peaceful Sannihit Sarovar, believed to be the holy confluence of seven sacred Saraswati rivers. This quiet sanctuary offers the perfect place to gather your thoughts before your journey home. After checking out of your hotel, enjoy a comfortable drive back to Delhi or Chandigarh. Your premium luxury tour concludes as you are transferred to the airport or railway station, taking home a renewed sense of peace and unforgettable memories from this special spiritual journey.'
                ),
                [
                    'SIGHTSEEING INCLUDED: Sannihit Sarovar, Kalpana Chawla Memorial Planetarium (Time Permitting).',
                    'MEALS INCLUDED: Extravagant Breakfast Buffet.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Divine Castle / Noormahal Palace Heritage variant',
                'Kurukshetra',
                '03 Nights',
                'Luxury',
                'Executive Suite / Club Room',
                'Breakfast & Dinner (MAP)',
                5,
                1,
                description='OPTION 01 – LUXURY: The Divine Castle / Noormahal Palace Heritage variant | Executive Suite / Club Room | Breakfast & Dinner (MAP)',
            ),
            _hotel(
                'Hotel Kimaya / Golden Tulip Essence',
                'Kurukshetra',
                '03 Nights',
                'Deluxe',
                'Super Deluxe King Room',
                'Breakfast & Dinner (MAP)',
                4,
                2,
                description='OPTION 02 – DELUXE: Hotel Kimaya / Golden Tulip Essence | Super Deluxe King Room | Breakfast & Dinner (MAP)',
            ),
            _hotel(
                'Hotel Red Castle / Divine Clerks',
                'Kurukshetra',
                '03 Nights',
                'Premium',
                'Super Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – PREMIUM: Hotel Red Castle / Divine Clerks | Super Deluxe Room | MAPAI',
            ),
            _hotel(
                'Curated Heritage Boutique Farm & Wellness Villa',
                'Kurukshetra',
                '03 Nights',
                'Ultra Luxury',
                'Royal Club Villa',
                'All Inclusive Premium Meals',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Curated Heritage Boutique Farm & Wellness Villa | Royal Club Villa | All Inclusive Premium Meals',
            )
        ],
        inclusions=[
            _inc_included('Luxury stays at premium, handpicked hotels.', 1),
            _inc_included('All transfers via private, chauffeur-driven luxury SUV.', 2),
            _inc_included('Daily premium buffet breakfast and multi-cuisine dinners.', 3),
            _inc_included('VIP priority access pass for the Jyotisar Light & Sound Show.', 4),
            _inc_included('Dedicated spiritual tour guide for select major sites.', 5),
            _inc_included('All toll taxes, parking fees, fuel surcharges, and driver allowances.', 6),
            _inc_included('24/7 remote guest assistance and trip tracking.', 7),
            _inc_excluded('Airfare, train tickets, or interstate border permits.', 8),
            _inc_excluded('Camera charges, special personal puja fees, or dakshina.', 9),
            _inc_excluded('Laundry, telephone calls, and room service orders.', 10),
            _inc_excluded('Any meals or snacks not listed in the itinerary.', 11),
            _inc_excluded('Travel insurance protections and medical coverages.', 12),
            _inc_excluded('Optional activities or extended destination detours.', 13),
        ],
    )
    return package, itinerary

def build_hr_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-003'
    tour_code = 'TRAGUIN-HR-003-2026'
    title = 'Sultanpur Birding Tour • Gurugram Premium Escapes'
    duration = '03 Nights / 04 Days'
    slug = 'hr-003-sultanpur-birding-gurugram-eco'
    itin_slug = 'hr-003-sultanpur-birding-gurugram-eco-itinerary'
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
            _ph('Serial code HR-003 | TRAGUIN tour code TRAGUIN-HR-003-2026', 1),
            _ph('State / Country: Haryana / India | Category: Premium Family Vacation & Birding', 2),
            _ph('Destinations: Haryana', 3),
            _ph('Ideal for: Family, Nature Enthusiasts, Wildlife Photographers', 4),
            _ph('Best season: October to March (Migratory Bird Season)', 5),
            _ph('Starting price: On Request (Premium Luxury Pricing)', 6),
            _ph('Vehicle / Meals: Private Premium Luxury SUV (Innova Crysta / Luxury Coach) throughout the entire journey. Meal Plan: Comprehensive American Plan (Breakfast, Gourmet Lunch, and Specialized Curated Dinners). Guest Type & Group: Private FIT (Family Tour / Executive Corporate Wellness Holiday).', 7),
            _ph('Route: Delhi/Gurugram Arrival • Sultanpur Bird Sanctuary Eco-Corridor • Heritage Farm Explorations • Premium Retreats', 8),
            _ph('TRAGUIN Signature Experience: Private entry alignment avoiding long general public queues,', 9),
            _ph('Curated by TRAGUIN Experts: Handpicked safety-verified elite travel pathways suited ideally for', 10),
            _ph('Luxury Transportation: Sanizited premium fleet with professional multilingual drivers knowledgeable', 11),
            _ph('Wildlife Protocol: Dull, earthy, or camouflaged clothing (greens, browns, khakis) is highly', 12),
            _ph('recommended for birding tours to blend in with nature.', 13)
        ],
        moods=['Family', 'Luxury', 'Heritage'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Luxury Pricing)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Sultanpur Birding Tour',
        overview='Sultanpur National Park • Gurugram Premium Escapes • Heritage Eco-Resorts Welcome to an unforgettable escape into the heart of wilderness and sheer sophistication. The Best Sultanpur Birding Tour Package curated by TRAGUIN promises an immersive journey tailored exclusively for families who appreciate the finer aspects of nature, luxury, and leisure. Nestled within Haryana, Sultanpur National Park stands out as one of the top tourist places in Haryana, serving as a pristine winter sanctuary for thousands of migratory birds flying across continents. This carefully crafted Sultanpur Family Tour beautifully seamlessly balances high-end comfort with premium wildlife sightings, giving you a refreshing break right on the outskirts of India’s millennium city. Indulge in breathtaking landscapes, immersive experiences, and handpicked hotels that turn a brief holiday into a lifetime memoir. TRAGUIN Premium Holiday Proposals\n\nTOUR OVERVIEW\nRoute: Delhi/Gurugram Arrival • Sultanpur Bird Sanctuary Eco-Corridor • Heritage Farm Explorations • Premium Retreats Vehicle: Private Premium Luxury SUV (Innova Crysta / Luxury Coach) throughout the entire journey. Meal Plan: Comprehensive American Plan (Breakfast, Gourmet Lunch, and Specialized Curated Dinners). Guest Type & Group: Private FIT (Family Tour / Executive Corporate Wellness Holiday). TRAGUIN Curated Experience Note: This bespoke itinerary includes private naturalists, early-access entry permissions to Sultanpur National Park, gourmet lakeside picnics, and customized high-tea arrangements designed exclusively by TRAGUIN destination specialists.\n\nWHY CHOOSE A LUXURY SULTANPUR HOLIDAY?\nSultanpur National Park is widely recognized as a premier destination for birding in North India. If you are seeking the absolute Best Time to Visit Sultanpur Bird Sanctuary, the vibrant winter months from October to March bring alive a visual spectacle featuring over 250 species of resident and migratory avifauna. From the Siberian Crane, Greater Flamingo, and Northern Pintail to majestic birds of prey, this eco-haven offers unparalleled Sultanpur Sightseeing opportunities. Perfect for a refined Sultanpur Honeymoon Package or a relaxing Sultanpur Family Tour, the region offers top Instagram locations ranging from quiet panoramic lakeside trails to luxurious rustic farmhouses. Beyond birding, families can enjoy organic farm-to-table dining, premium spa therapies, cultural village walks, and high-end shopping in nearby Gurugram, ensuring an ultra-luxury experience for every generation.',
        seo_title='HR-003 | Sultanpur Birding Tour | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Haryana package (HR-003 / TRAGUIN-HR-003-2026): Haryana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GURUGRAM', 1),
            _ih('Day 02: SULTANPUR NATIONAL PARK', 2),
            _ih('Day 03: HERITAGE FARM EXPERIENCES & LUXURY LEISURE', 3),
            _ih('Day 04: GURUGRAM SIGHTSEEING & DEPARTURE WITH UNFORGETTABLE MEMORIES', 4),
            _ih('TRAGUIN Signature Experience: Private entry alignment avoiding long general public queues,', 5),
            _ih('Curated by TRAGUIN Experts: Handpicked safety-verified elite travel pathways suited ideally for', 6),
            _ih('Luxury Transportation: Sanizited premium fleet with professional multilingual drivers knowledgeable', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GURUGRAM | WELCOME TO THE PREMIUM ECO-CORRIDOR',
                (
                    'Arrive at New Delhi Airport or your preferred location, where a premium luxury chauffeured vehicle arranged by TRAGUIN awaits you. Experience a seamless check-in at your handpicked ultra-luxury resort near the Sultanpur eco-corridor. After checking in, enjoy a customized welcome drink and a personalized briefing by your tour coordinator. Spend the afternoon relaxing amid the breathtaking landscapes of your property. In the evening, head out for a gentle introductory walk along the countryside roads near Sultanpur, capturing the beautiful sunset over the mustard fields—a perfect photography point. Conclude your evening with a curated multi-course dinner at the resort. TRAGUIN Premium Holiday Proposals'
                ),
                [
                    'Sightseeing Included: Countryside scenic drives, sunset photography over rural Haryana landscapes.',
                    'Evening Experience: Welcome high-tea followed by a premium private sit-down welcome dinner.',
                    'Overnight Stay: Handpicked Luxury Eco-Resort / Premium Retreat near Sultanpur.',
                    'Meals Included: Lunch & Dinner.',
                ],
            ),
            _day(
                2,
                'SULTANPUR NATIONAL PARK | THE ULTIMATE BIRDING EXPERIENCE',
                (
                    'Wake up to a crisp winter morning for your highly anticipated Sultanpur Sightseeing. Embark on an early morning excursion to Sultanpur National Park, armed with high-end binoculars and accompanied by a top-tier private naturalist certified by TRAGUIN. Walk along the well-shaded circular trail surrounding the lake to spot iconic attractions like the Black-necked Stork, Bar-headed Geese, and Dalmatian Pelicans. Your naturalist will guide you through immersive experiences, explaining bird behaviors and nesting patterns. After a rewarding morning of photography, enjoy a premium packed gourmet picnic breakfast under the canopy of ancient trees. Return to the resort for lunch and a relaxing afternoon. Before dusk, take a curated village walk to experience local Haryanvi culture and crafts up close.'
                ),
                [
                    'Sightseeing Included: Full Sultanpur National Park birding loop, watchtowers, and educational interpretation center.',
                    'Optional Activities: Advanced wildlife photography masterclass with a professional mentor.',
                    'Evening Experience: Bonfire night with live traditional music and a premium regional barbecue dinner.',
                    'Overnight Stay: Handpicked Luxury Eco-Resort / Premium Retreat near Sultanpur.',
                    'Meals Included: Breakfast, Lunch & Dinner.',
                ],
            ),
            _day(
                3,
                'HERITAGE FARM EXPERIENCES & LUXURY LEISURE',
                (
                    'Savor a lazy breakfast before heading out for an exclusive, curated farm-to-table experience at a premium heritage estate nearby. Participate in organic farming activities, pick fresh seasonal produce, and enjoy a traditional yet refined lunch in an open-air pavilion. In the afternoon, return to your premium resort to indulge in wellness therapies, a dip in the temperature-controlled pool, or a game of golf. This day is specially tailored to offer an elegant blend of rural charm and urban luxury, ensuring unforgettable memories for the entire family.'
                ),
                [
                    'Sightseeing Included: Heritage farm tours, local agricultural estates, and curated rural life exhibits.',
                    'Evening Experience: Exclusive dynamic high-tea followed by a premium multi-cuisine farewell dinner.',
                    'Overnight Stay: Handpicked Luxury Eco-Resort / Premium Retreat near Sultanpur.',
                    'Meals Included: Breakfast, Lunch & Dinner.',
                ],
            ),
            _day(
                4,
                'GURUGRAM SIGHTSEEING & DEPARTURE WITH UNFORGETTABLE MEMORIES',
                (
                    'TRAGUIN Premium Holiday Proposals After an elegant breakfast, check out from your resort. Your private premium luxury SUV will take you toward Gurugram for premium shopping at high-end plazas or a stroll through CyberHub, a popular Instagram location for lifestyle photography. Pick up exclusive local souvenirs and traditional handicrafts. After a delightful lunch, your driver will drop you at the airport or railway station, concluding your magnificent Premium Sultanpur Experience designed by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Gurugram modern architectural landmarks, shopping emporiums.',
                    'Meals Included: Breakfast & Lunch.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Hotel, Tarudhan Valley /',
                'Kurukshetra',
                '03 Nights',
                'Deluxe',
                'Similar',
                'Executive Room',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Hotel, Tarudhan Valley / | Similar | Executive Room',
            ),
            _hotel(
                'Heritage Village Resort & Spa,',
                'Kurukshetra',
                '03 Nights',
                'Premium',
                'Manesar / Similar',
                'Heritage Superior',
                4,
                2,
                description='OPTION 02 – PREMIUM: Heritage Village Resort & Spa, | Manesar / Similar | Heritage Superior',
            ),
            _hotel(
                'The Grand Orchard Retreat /',
                'Kurukshetra',
                '03 Nights',
                'Luxury',
                'Sultanpur Eco Lodges',
                'Luxury Lake-View',
                4,
                3,
                description='OPTION 03 – LUXURY: The Grand Orchard Retreat / | Sultanpur Eco Lodges | Luxury Lake-View',
            ),
            _hotel(
                'The Oberoi, Gurugram / ITC Grand',
                'Kurukshetra',
                '03 Nights',
                'Ultra Luxury',
                'Bharat (Extended)',
                'Deluxe Suite / Luxury',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi, Gurugram / ITC Grand | Bharat (Extended) | Deluxe Suite / Luxury',
            )
        ],
        inclusions=[
            _inc_included("Premium accommodation at handpicked Haryana properties.", 1),
            _inc_included("Private luxury vehicle for all transfers and sightseeing.", 2),
            _inc_excluded("Airfare and personal expenses.", 3),
        ],
    )
    return package, itinerary

def build_hr_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-004'
    tour_code = 'TRAGUIN-LUX-HR-004'
    title = 'Luxury Haryana Retreat'
    duration = '04 Nights / 05 Days'
    slug = 'hr-004-luxury-haryana-retreat'
    itin_slug = 'hr-004-luxury-haryana-retreat-itinerary'
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
            _ph('Serial code HR-004 | TRAGUIN tour code TRAGUIN-LUX-HR-004', 1),
            _ph('State / Country: Haryana / India | Category: Luxury Holidays', 2),
            _ph('Destinations: Haryana', 3),
            _ph('Ideal for: Couples, Families, Corporate Retreats', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: INR 85,000/- Per Person', 6),
            _ph('Vehicle / Meals: Private Luxury SUV (Toyota Alphard / Mercedes-Benz V-Class) Meal Plan: Fully Modified American Plan (Breakfast & Dinner Included at Premium Venues)', 7),
            _ph('Route: Gurugram ➔ Manesar Heritage Village ➔ Pinjore Mughal Gardens ➔ Panchkula Morni Hills', 8),
            _ph('TRAGUIN Signature Experience: Private access to premium polo lounges and custom rural', 9),
            _ph('Curated by TRAGUIN Experts: Itinerary designed by seasoned travel designers specializing in', 10),
            _ph('Personalized Assistance: A dedicated hospitality concierge connected with you throughout the', 11),
            _ph('Premium Handpicked Hotels: Regular quality audits ensure your properties remain top-tier', 12),
            _ph('Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Early access or late', 13),
            _ph('departures remain strictly subject to room availability.', 14)
        ],
        moods=['Luxury', 'Family', 'Heritage'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='INR 85,000/- Per Person',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Haryana Retreat',
        overview='ighly scenic drive northward toward the historic valleys of Panchkula. Your Premium Haryana Experience transitions seamlessly into historical luxury as you stop at the legendary Yadavindra Gardens in Pinjore. Spanning over 100 acres, these stunning 17th-century terraced Mughal gardens are among the most popular Instagram locations in North India. Walk hand-in-hand through the majestic symmetry of descending water channels, sparkling fountains, and historic palaces like the Shish Mahal and Hawa Mahal. Your TRAGUIN guide will reveal the captivating history of the rulers who conceptualized this oasis. By late afternoon, ascend into the tranquil, lush surroundings of Panchkula, nestled right under the Shivalik hills. Check into your premium hilltop resort and enjoy a private sunset high-tea looking out over the endless green valleys. Sightseeing Included: Pinjore Mughal Gardens, Bhima Devi Temple Complex, Panchkula Valley Drive. Optional Activities: Private photography session inside Pinjore Gardens with a professional photographer. Evening Experience: Luxury High-Tea on a private terrace overlooking the Shivalik foothills. Overnight Stay: The Oberoi Sukhvilas Spa Resort / Welcomhotel by ITC Hotels, Bella Vista, Panchkula. Meals Included: Rich Breakfast & Exquisite Fine-Dining Dinner.\n\nTOUR OVERVIEW\nThis elite, handpicked itinerary offers an unparalleled window into the cultural depth and contemporary luxury of Haryana. Traveling in an ultra-premium, climate-controlled luxury SUV with your dedicated personal concierge, your route connects the opulent urban retreats of Gurugram and Manesar to the scenic foothills of Panchkula and the historic Mughal architecture of Pinjore. Every property on this journey has been hand-selected to fulfill the highest benchmarks of premium hospitality. Travel Dates: Flexible / Customizable Upon Request Group / FIT: Bespoke Private Tour (FIT) Vehicle: Private Luxury SUV (Toyota Alphard / Mercedes-Benz V-Class) Meal Plan: Fully Modified American Plan (Breakfast & Dinner Included at Premium Venues) Route: Gurugram ➔ Manesar Heritage Village ➔ Pinjore Mughal Gardens ➔ Panchkula Morni Hills TRAGUIN Curated Experience Note: Includes private royal polo lounge access, curated heritage culinary walks, automated VIP entry passes, and a spectacular luxury high-tea session overlooking the Shivalik foothills.\n\nDESTINATION SEO CONTENT\nWhen considering the Best Time to Visit Haryana, the crisp autumn and winter months from October to March provide an idyllic backdrop for a Premium Haryana Experience. Long overlooked by mainstream leisure travel, high-end voyagers are discovering that the state hosts some of the most exclusive royal wellness retreats and ultra-modern lifestyle attractions in the region. The Top Tourist Places in Haryana cater effortlessly to diverse preferences. For those embarking on a romantic escapade, a curated Haryana Honeymoon Package delivers secluded luxury villas, private spa therapies, and candle-lit lakeside dinners. Families seeking a meaningful break can opt for a tailored Haryana Family Tour, which seamlessly introduces children to the legacy of India’s epic histories alongside high-tech entertainment parks and organic farming encounters. Most Searched Experiences & Instagram Locations: Capture striking lifestyle imagery at the architectural masterpiece CyberHub Gurugram, freeze time amidst the symmetric fountains of the 17th-century Pinjore Gardens, or take panoramic sunset shots from the heights of Morni Hills. From high-octane adventure sports like paramotoring in Sohna to traditional cultural showcases at heritage villages and luxury shopping at global designer boutiques, TRAGUIN Haryana Packages open doors to experiences completely unavailable to the ordinary traveler.',
        seo_title='HR-004 | Luxury Haryana Retreat | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Haryana package (HR-004 / TRAGUIN-LUX-HR-004): Haryana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: GURUGRAM & MANESAR', 1),
            _ih('Day 02: MANESAR HERITAGE VILLAGE', 2),
            _ih('Day 03: MANESAR TO PANCHKULA & PINJORE', 3),
            _ih('Day 04: MORNI HILLS & TIKKAR TAAL', 4),
            _ih('Day 05: PANCHKULA TO DELHI / DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private access to premium polo lounges and custom rural', 6),
            _ih('Curated by TRAGUIN Experts: Itinerary designed by seasoned travel designers specializing in', 7),
            _ih('Personalized Assistance: A dedicated hospitality concierge connected with you throughout the', 8)
        ],
        days=[
            _day(
                1,
                'GURUGRAM & MANESAR',
                (
                    "ARRIVAL IN THE MILLENNIUM CITY & ROYAL WELCOME AT MANESAR Your signature Luxury Haryana Holiday begins with a warm, VIP personalized greeting as you step out of Delhi airport or your preferred pickup point. Your dedicated TRAGUIN tour concierge will escort you to an elite luxury vehicle, equipped with premium refreshments and high-speed connectivity. Arrive at your ultra-luxury heritage resort in Manesar, where a traditional royal welcome with flower garlands, live folk music, and artisanal welcome mocktails awaits. Spend the afternoon settling into your palatial private suite. In the evening, your personal chauffeur will drive you through the spectacular, neon-lit skyline of Gurugram for a glamorous Haryana Sightseeing preview. Walk the vibrant corridors of CyberHub, a globally renowned culinary and lifestyle avenue. Indulge in an exclusive multi-course dinner reservation at an award-winning chef's table, soaking in the energy of India's premier corporate oasis."
                ),
                [
                    'Sightseeing Included: Private Transfer, CyberHub Boulevard Walk, Gurugram Horizon View.',
                    'Optional Activities: High-end designer boutique shopping at Horizon Center, Luxury Spa therapy.',
                    'Evening Experience: Fine-dining gastronomy experience with live contemporary music.',
                    'Overnight Stay: ITC Grand Bharat, A Luxury Collection Resort / Heritage Village Resort & Spa, Manesar.',
                    'Meals Included: Welcome Amenities & Premium Dinner.',
                ],
            ),
            _day(
                2,
                'MANESAR HERITAGE VILLAGE',
                (
                    'IMMERSIVE CULTURAL EXPERIENCES & WELLNESS RETREAT Wake up to the pristine, manicured landscapes of your resort. Day two of your Best Haryana Tour Package is dedicated to an immersive, soulful engagement with local heritage. Following an organic breakfast, enjoy a privately guided heritage tour of an authentic model village. Witness the timeless artistry of local potters, experience luxury camel-cart safaris through the mustard fields, and discover traditional stepwell architecture that has endured for centuries. In the afternoon, retreat into the world-class wellness center of your resort. Treat yourself to a revitalizing Ayurvedic massage or a signature holistic therapy session. As the sun begins to set, capture beautiful photographs against the backdrop of Rajasthani-Mughal inspired architectures. Conclude the day with a spectacular private cultural evening featuring traditional Haryana folk dancers, followed by a royal feast prepared by master chefs utilizing locally harvested organic produce. course.'
                ),
                [
                    'Sightseeing Included: Manesar Heritage Exploration, Organic Farm Walk, Traditional Stepwell Visit.',
                    'Optional Activities: Hot air balloon ride (seasonal), Professional Golfing Session at a championship',
                    'Evening Experience: Royal Folk Dance performance followed by an exclusive poolside dinner.',
                    'Overnight Stay: Luxury Resort, Manesar.',
                    'Meals Included: Gourmet Breakfast & Royal Buffet Dinner.',
                ],
            ),
            _day(
                3,
                'MANESAR TO PANCHKULA & PINJORE',
                (
                    'ROYAL MUGHAL SPLENDOR & THE SHIVALIK FOOTHILLS Bid farewell to the modern energy of Gurugram as you embark on a highly scenic drive northward toward the historic valleys of Panchkula. Your Premium Haryana Experience transitions seamlessly into historical luxury as you stop at the legendary Yadavindra Gardens in Pinjore. Spanning over 100 acres, these stunning 17th-century terraced Mughal gardens are among the most popular Instagram locations in North India. Walk hand-in-hand through the majestic symmetry of descending water channels, sparkling fountains, and historic palaces like the Shish Mahal and Hawa Mahal. Your TRAGUIN guide will reveal the captivating history of the rulers who conceptualized this oasis. By late afternoon, ascend into the tranquil, lush surroundings of Panchkula, nestled right under the Shivalik hills. Check into your premium hilltop resort and enjoy a private sunset high-tea looking out over the endless green valleys. photographer.'
                ),
                [
                    'Sightseeing Included: Pinjore Mughal Gardens, Bhima Devi Temple Complex, Panchkula Valley Drive.',
                    'Optional Activities: Private photography session inside Pinjore Gardens with a professional',
                    'Evening Experience: Luxury High-Tea on a private terrace overlooking the Shivalik foothills.',
                    'Overnight Stay: The Oberoi Sukhvilas Spa Resort / Welcomhotel by ITC Hotels, Bella Vista, Panchkula.',
                    'Meals Included: Rich Breakfast & Exquisite Fine-Dining Dinner.',
                ],
            ),
            _day(
                4,
                'MORNI HILLS & TIKKAR TAAL',
                (
                    'BREATHTAKING LANDSCAPES & EXCLUSIVE LAKESIDE LUXURY The fourth day of your Haryana Family Tour or Haryana Honeymoon Package centers around pristine nature and tranquil landscapes. Embark on an early morning excursion to Morni Hills, the only hill station in the state. Wind through dense pine forests, taking in the crisp mountain air and panoramic viewpoints that are ideal for photography. Arrive at the beautiful twin lakes of Tikkar Taal. Here, TRAGUIN arranges a private lakeside luxury setup where you can relax in total isolation. Enjoy a quiet boat cruise across the calm waters, or simply unwind with a premium book and specialized refreshments. On your way back to Panchkula, explore the ancient ruins of the Bhima Devi Temple, often called the Khajuraho of North India for its exquisite stone carvings. Return to the resort for your grand final-night celebratory dinner. journey.'
                ),
                [
                    'Sightseeing Included: Morni Hills Viewpoint, Tikkar Taal Lakes, Ancient Bhima Devi Temple Ruins.',
                    'Optional Activities: Adventure activities at Morni Adventure Park (Ziplining, Rock Climbing).',
                    'Evening Experience: Special candle-lit farewell dinner with a customized menu celebrating your',
                    'Overnight Stay: Luxury Hillside Resort, Panchkula.',
                    'Meals Included: Breakfast & Grand Farewell Dinner.',
                ],
            ),
            _day(
                5,
                'PANCHKULA TO DELHI / DEPARTURE',
                (
                    'MEMORIES BEYOND DESTINATIONS & FAREWELL Savor a leisurely breakfast on your final morning, taking in the soothing mountain air of Panchkula one last time. Spend a few hours relaxing by the infinity pool or utilizing the premium amenities of your luxury resort. At your scheduled checkout time, your personal luxury vehicle will be waiting to transport you back to Delhi. As you reflect on the incredible heritage, vibrant cityscapes, and tranquil hill stations experienced on this journey, you will realize why this is considered the definitive Premium Haryana Experience. Your chauffeur will smoothly drop you at the airport, railway station, or your home, concluding your phenomenal holiday with TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Scenic Return Drive, Airport/Station Private Drop-off.',
                    'Meals Included: Gourmet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Hotel, Tarudhan Valley | Golden Tulip Panchkula Resort',
                'Manesar | Panchkula',
                '02 Nights Manesar + 02 Nights Panchkula',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner Included)',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Hotel, Tarudhan Valley (Executive Room) | Golden Tulip Panchkula Resort (Deluxe Valley View Room) | MAPAI (Breakfast & Dinner Included)',
            ),
            _hotel(
                'Heritage Village Resort & Spa, Manesar | Welcomhotel by ITC Hotels, Bella Vista',
                'Manesar | Panchkula',
                '02 Nights Manesar + 02 Nights Panchkula',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner Included)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Heritage Village Resort & Spa, Manesar (Heritage Superior Room) | Welcomhotel by ITC Hotels, Bella Vista (Premium Room) | MAPAI (Breakfast & Dinner Included)',
            ),
            _hotel(
                'ITC Grand Bharat, A Luxury Collection Resort | The Oberoi Sukhvilas Spa Resort',
                'Manesar | Panchkula',
                '02 Nights Manesar + 02 Nights Panchkula',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Gourmet Breakfast & Multi-cuisine Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: ITC Grand Bharat, A Luxury Collection Resort (Deluxe Suite) | The Oberoi Sukhvilas Spa Resort (Premier Room) | MAPAI (Gourmet Breakfast & Multi-cuisine Dinner)',
            ),
            _hotel(
                'ITC Grand Bharat, A Luxury Collection Resort | The Oberoi Sukhvilas Spa Resort',
                'Manesar | Panchkula',
                '02 Nights Manesar + 02 Nights Panchkula',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Bespoke Curated Fine-Dining Plan)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: ITC Grand Bharat, A Luxury Collection Resort (Luxury Suite with Private Pool) | The Oberoi Sukhvilas Spa Resort (Luxury Villa with Private Pool) | MAPAI (Bespoke Curated Fine-Dining Plan)',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: 04 Nights stay in handpicked premier luxury properties.', 1),
            _inc_included('Welcome Amenities: Royal traditional welcome with exotic juices and floral arrangements.', 2),
            _inc_included('Meals: Daily multi-cuisine buffet breakfasts and premium dinners.', 3),
            _inc_excluded('Flights: Domestic or International airfare and airport taxes.', 4),
            _inc_excluded('Entry Tickets: Camera fees, monument entry tickets, or local guide hiring charges.', 5),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, alcoholic beverages, and mini-bar usage.', 6),
            _inc_excluded('TRAGUIN Premium Luxury Holidays • HR-004 6 Transfers & Sightseeing: All transfers and sightseeing via dedicated private luxury SUV.', 7),
            _inc_excluded('TRAGUIN Support: 24/7 dedicated guest relations officer and professional concierge assistance.', 8),
            _inc_excluded('Complimentary Experiences: Private sunset high-tea at Panchkula and luxury farm-walk tickets.', 9),
            _inc_excluded('Taxes: All current applicable hotel taxes, fuel charges, toll fees, and driver allowances.', 10),
            _inc_excluded('Activities: Cost of optional adventures like paramotoring, golfing, or hot air ballooning.', 11),
            _inc_excluded('Insurance: Comprehensive travel, medical, or baggage insurance coverage.', 12),
            _inc_excluded('Taxes: Any newly mandated government service tax or TCS adjustments.', 13),
        ],
    )
    return package, itinerary

def build_hr_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-005'
    tour_code = 'TG-HAR-SR-005'
    title = 'Royal Heritage & Wellness Leisure Circuit'
    duration = '04 Nights / 05 Days'
    slug = 'hr-005-royal-heritage-wellness-circuit'
    itin_slug = 'hr-005-royal-heritage-wellness-circuit-itinerary'
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
            _ph('Serial code HR-005 | TRAGUIN tour code TG-HAR-SR-005', 1),
            _ph('State / Country: Haryana / India | Category: Senior Citizen', 2),
            _ph('Destinations: Haryana', 3),
            _ph('Ideal for: Senior Citizens, Multi- generational Families, Leisure Seekers', 4),
            _ph('Best season: October to March (Pleasant Winters)', 5),
            _ph('Starting price: INR 34,500/- Per Person (Premium Luxury All-Inclusive)', 6),
            _ph('Vehicle / Meals: Luxury Innova Crysta (Completely Private)', 7),
            _ph('Route: Delhi/Gurugram ➔ Sultanpur ➔ Kurukshetra ➔ Pinjore ➔ Panchkula Foothills', 8),
            _ph('TRAGUIN Signature Experience: Hand-vetted properties ensuring absolute accessibility, premium', 9),
            _ph('Curated by TRAGUIN Experts: A thoroughly slow-paced itinerary focused on premium leisure, avoiding', 10),
            _ph('Personalized Assistance: Daily wellness check-ins from our operations head to ensure your complete', 11),
            _ph('Premium Handpicked Hotels: Properties holding exceptional reputations for exquisite cuisine, pristine', 12),
            _ph('Hotel Policies: Standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Early check-in is subject to', 13),
            _ph('availability.', 14)
        ],
        moods=['Heritage', 'Family', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='INR 34,500/- Per Person (Premium Luxury All-Inclusive)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Royal Heritage & Wellness Leisure Circuit',
        overview='The Royal Heritage & Wellness Leisure Circuit Gurugram • Sultanpur • Kurukshetra • Pinjore • Panchkula Embark on a soul-stirring, slow-paced luxury journey through the historic heartland of India with the Best Haryana Tour Package curated exclusively by TRAGUIN. Designed meticulously for senior citizens, this Haryana Family Tour combines ultra-comfortable luxury transit, handpicked premium stays, and deeply immersive cultural experiences. From the tranquil wetlands of Sultanpur to the spiritual aura of holy Kurukshetra and the breathtaking Mughal splendor of Pinjore Gardens, witness timeless heritage blended seamlessly with unparalleled modern comforts. Let TRAGUIN redefine your travel experience with personalized care, gentle pacing, and memories to cherish forever. TRAGUIN TRAGUIN Premium Holidays • HR-005\n\nTOUR OVERVIEW\nOur signature Premium Haryana Experience is curated specifically for discerning senior travelers who value comfort, safety, and deep exploration over rushed itineraries. This bespoke Luxury Haryana Holiday minimizes long driving fatigue by scheduling optimal breaks and utilizing a premium, smooth-riding luxury vehicle with an experienced professional driver-guide. Enjoy rich local cuisine, beautiful luxury boutique stays, and dedicated on- ground TRAGUIN support throughout your journey. Travel Dates: Flexible / Custom FIT (Fully Individual Traveler) Group / FIT: Customized Private Premium Leisure FIT Vehicle: Private Chauffeur-Driven Luxury Innova Crysta (Air-conditioned, ergonomically optimized) Meal Plan: Premium MAPAI Plan (Daily Buffet Breakfast, Choice of Gourmet Lunch or Dinner) Route: Delhi/Gurugram ➔ Sultanpur ➔ Kurukshetra ➔ Pinjore ➔ Panchkula Foothills TRAGUIN Curated Note: Includes wheelchair assistance at key monuments upon request, pre-vetted accessible entry points, gentle walking tracks, and daily complementary wellness immunity-boosting tea breaks.\n\nWHY CHOOSE A LUXURY HARYANA HOLIDAY?\nOften overlooked, Haryana holds some of the finest hidden treasures of North India, making it an exceptional destination for a relaxed Haryana Family Tour. It boasts magnificent historic landmarks, tranquil eco-tourism spots, and world-renowned spiritual centers. Seeking the perfect Haryana Honeymoon Package or a refreshing senior retreat? The lush organic farmlands, heritage stepwells, and royal fountains offer magnificent, popular Instagram locations without the overwhelming tourist crowds. Our curated Haryana Sightseeing circuit includes iconic attractions such as the sacred Brahma Sarovar, the architectural marvel of Yadavindra Mughal Gardens, and the avian paradise at Sultanpur. Experience authentic Haryanvi hospitality, savor rich ghee-laden delicacies, and purchase fine local handicrafts like handwoven Dari rugs and exquisite pottery. With the Best Time to Visit Haryana being the cool, crisp winter months, TRAGUIN Haryana Packages guarantee a thoroughly comfortable, enriching, and unforgettable vacation.',
        seo_title='HR-005 | Royal Heritage & Wellness Leisure Circuit | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Haryana package (HR-005 / TG-HAR-SR-005): Haryana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GURUGRAM', 1),
            _ih('Day 02: SULTANPUR BIRD SANCTUARY & HERITAGE FARM LUNCH', 2),
            _ih('Day 03: GURUGRAM TO KURUKSHETRA', 3),
            _ih('Day 04: KURUKSHETRA TO PINJORE & PANCHKULAFOOTHILLS', 4),
            _ih('Day 05: PANCHKULA TO DELHI / CHANDIGARH DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Hand-vetted properties ensuring absolute accessibility, premium', 6),
            _ih('Curated by TRAGUIN Experts: A thoroughly slow-paced itinerary focused on premium leisure, avoiding', 7),
            _ih('Personalized Assistance: Daily wellness check-ins from our operations head to ensure your complete', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GURUGRAM',
                (
                    "WELCOME TO THE MILLENNIUM CITY & LUXURY CHECK-IN Arrive at New Delhi Airport/Railway Station where your dedicated private TRAGUIN luxury chauffeur welcomes you with customized amenities. Enjoy a smooth, short drive to your ultra-premium hotel in Gurugram. Our representative will seamlessly manage your VIP check-in, allowing you to relax without any hassle. Spend your afternoon unwinding in your plush room or enjoying the premium wellness amenities of the property. TRAGUIN Premium Holidays • HR-005 In the evening, enjoy a gentle, curated walk around the premium CyberHub or experience a peaceful cultural evening at the Kingdom of Dreams precinct (subject to operational schedules), showcasing India's diverse heritage. Savor a premium welcome dinner filled with local and global delicacies, curated exclusively for your dietary preferences."
                ),
                [
                    'Sightseeing Included: Smooth airport pick-up, CyberHub premium evening lounge access.',
                    'Optional Activities: Therapeutic light spa session at the hotel to alleviate travel fatigue.',
                    'Evening Experience: Private TRAGUIN welcome mocktail session with your travel consultant overview.',
                    'Overnight Stay: Gurugram (Premium 5-Star Luxury Hotel)',
                    'Meals Included: Welcome Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'SULTANPUR BIRD SANCTUARY & HERITAGE FARM LUNCH',
                (
                    'BREATHTAKING LANDSCAPES & AVIAN WONDERS Begin your day with an early, refreshing morning breakfast before heading out for a premium Haryana Sightseeing excursion to the famous Sultanpur Bird Sanctuary. A absolute paradise for nature enthusiasts, this sanctuary transforms into a vibrant canvas of migratory birds during the winter season. Enjoy a relaxed, golf-cart assisted tour around the peaceful lake, capturing stunning views of flamingos, Siberian cranes, and painted storks. Following your serene morning, we drive to a nearby luxury eco-heritage farmstead. Here, you will enjoy an authentic, organic Haryanvi lunch prepared with fresh, farm-to-table ingredients and pure white butter. Spend your afternoon relaxing under shaded canopies, observing traditional pottery making, and experiencing true rural luxury. Return to the hotel for a quiet, relaxing evening.'
                ),
                [
                    'Sightseeing Included: Guided Sultanpur Bird Sanctuary Tour, Eco-Heritage Farmstead Visit.',
                    'Optional Activities: Photography workshop focusing on local bird species with our expert guide.',
                    'Evening Experience: Relaxed tea-tasting lounge session at the premium hotel cafe.',
                    'Overnight Stay: Gurugram (Premium 5-Star Luxury Hotel)',
                    'Meals Included: Buffet Breakfast & Authentic Organic Farm Lunch',
                ],
            ),
            _day(
                3,
                'GURUGRAM TO KURUKSHETRA',
                (
                    'THE SPIRITUAL HEART OF HOLY KURUKSHETRA TRAGUIN Premium Holidays • HR-005 Following a delicious breakfast, check out and embark on a smooth, scenic drive along the national highway toward the legendary holy city of Kurukshetra. This spiritual hub stands as one of the Top Tourist Places in Haryana. Upon arrival, check into your handpicked premium heritage hotel. After a short rest, begin your serene spiritual tour starting with the breathtaking Brahma Sarovar—a massive, sacred water tank reflecting beautiful blue skies. Stroll gently along the highly accessible walkways to Jyotisar, the revered birth site of the Holy Bhagavad Gita, where you will witness the ancient, sacred Banyan tree. TRAGUIN ensures premium seating for you to enjoy the spectacular, state-of-the-art Multimedia Laser Light Show in the evening, bringing the epic history to life with emotional storytelling.'
                ),
                [
                    'Sightseeing Included: Brahma Sarovar, Jyotisar Holy Site, Multimedia Laser Show.',
                    'Optional Activities: Private interaction with a renowned Vedic scholar for spiritual insights.',
                    'Evening Experience: Divine Maha Aarti experience at the banks of Brahma Sarovar with reserved seating.',
                    'Overnight Stay: Kurukshetra (Premium Selected Boutique Heritage Hotel)',
                    'Meals Included: Buffet Breakfast & Gourmet Dinner',
                ],
            ),
            _day(
                4,
                'KURUKSHETRA TO PINJORE & PANCHKULAFOOTHILLS',
                (
                    'MUGHAL GRANDEUR, TERRACED FOUNTAINS & SHIVALIK VISTAS Savor an early breakfast before driving north toward the beautiful Shivalik foothills. Your destination is the magnificent Pinjore Gardens, also widely celebrated as the Yadavindra Mughal Gardens. This architectural masterpiece features cascading terraced lawns, monumental fountains, and serene reflecting pools built in the classic 17th-century style. It stands as a top-ranked popular Instagram location and a highlight of our Premium Haryana Experience. Enjoy a leisurely stroll through the shaded orchards and beautiful pavilions. Afterward, check into your ultra-luxury resort nestled in the tranquil green foothills of Panchkula. This handpicked premium resort offers breathtaking panoramic views of the hills, perfect for a peaceful evening. Celebrate your final tour night with a candlelit farewell dinner arranged specially by TRAGUIN. TRAGUIN Premium Holidays • HR-005'
                ),
                [
                    'Sightseeing Included: Yadavindra Pinjore Mughal Gardens, Panchkula scenic overlook.',
                    'Optional Activities: Gentle cable car ride at nearby Timber Trail for panoramic mountain views.',
                    'Evening Experience: Premium farewell multi-course dinner with live soft instrumental music.',
                    'Overnight Stay: Panchkula Foothills (Luxury 5-Star Wellness Resort)',
                    'Meals Included: Buffet Breakfast & Special Farewell Dinner',
                ],
            ),
            _day(
                5,
                'PANCHKULA TO DELHI / CHANDIGARH DEPARTURE',
                (
                    "CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Wake up to a crisp, misty morning overlooking the beautiful Shivalik hills. Enjoy a relaxed, extensive breakfast spread at the resort's premium terrace restaurant. Spend your morning at leisure, capturing final photographs of the breathtaking landscapes or indulging in a final wellness therapy session at the resort. At the designated hour, check out comfortably. Your private luxury TRAGUIN vehicle will drive you smoothly to either Chandigarh Airport (just 30 minutes away) or back to New Delhi International Airport/Railway Station for your onward journey home. Return with an abundance of relaxed, beautiful memories and rejuvenated spirits from this masterfully crafted senior holiday."
                ),
                [
                    'Sightseeing Included: Comfortable return transfers, souvenir assistance.',
                    'Optional Activities: Short stopover for handicraft shopping at the Chandigarh Sector 17 emporium.',
                    'Meals Included: Extravagant Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                '(NIGHTS 1 & 2)',
                'Kurukshetra',
                '04 Nights',
                'Gurugram',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – GURUGRAM: (NIGHTS 1 & 2) | Deluxe Room | MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                '/ Similar',
                'Kurukshetra',
                '04 Nights',
                'Deluxe',
                'Deluxe Room',
                'Breakfast, Base',
                4,
                2,
                description='OPTION 02 – DELUXE: / Similar | Deluxe Room | Breakfast, Base',
            ),
            _hotel(
                'Taj City Centre',
                'Kurukshetra',
                '04 Nights',
                'Premium',
                'Deluxe Room',
                'MAPAI, Club',
                4,
                3,
                description='OPTION 03 – PREMIUM: Taj City Centre | Deluxe Room | MAPAI, Club',
            ),
            _hotel(
                'Spa Resort',
                'Kurukshetra',
                '04 Nights',
                'Luxury',
                'Selected Suite',
                'MAPAI, Premium',
                5,
                4,
                description='OPTION 04 – LUXURY: Spa Resort | Selected Suite | MAPAI, Premium',
            )
        ],
        inclusions=[
            _inc_included('TRAGUIN Premium Holidays • HR-005 Page 5 of 7', 1),
            _inc_excluded('Personal Expenses: Laundry service, telephone calls, premium alcoholic beverages, mini-bar usage, or tipping fees.', 2),
            _inc_excluded('Optional Activities: Adventure rides, cable car tours, or spa therapies explicitly marked as optional.', 3),
            _inc_excluded('Insurance: Travel or medical insurance policies (Highly recommended for senior citizens).', 4),
            _inc_excluded('• • • • TRAGUIN Premium Holidays • HR-005 Page 6 of 7 Our Premium Haryana Experience introduces you to magnificent local traditions: Panipat Handlooms & Phulkari: Pick up exquisite traditional handwoven shawls, stunning Phulkari embroidery, and top-quality linens. Terracotta Pottery: Visit a local artisan village near Sultanpur to acquire beautifully handcrafted clay artifacts and souvenirs. Authentic Sweetmeats: Taste the famous, melt-in-the-mouth Kurukshetra Pedas and rich, clarifying traditional desi ghee jalebis. Instagram Spots: Pose gracefully against the majestic multi-tiered fountains of Pinjore and the tranquil reflecting pools of Brahma Sarovar.', 5),
        ],
    )
    return package, itinerary

def build_hr_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-006'
    tour_code = 'TG-HR-EDU-006'
    title = 'Educational Tour Kurukshetra & Pinjore'
    duration = '03 Nights / 04 Days'
    slug = 'hr-006-educational-kurukshetra-pinjore'
    itin_slug = 'hr-006-educational-kurukshetra-pinjore-itinerary'
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
            _ph('Serial code HR-006 | TRAGUIN tour code TG-HR-EDU-006', 1),
            _ph('State / Country: Haryana / India | Category: School Educational Tour', 2),
            _ph('Destinations: Haryana', 3),
            _ph('Ideal for: Students, Educators & Academic Institutions', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Group Pricing Available)', 6),
            _ph('Vehicle / Meals: Premium Luxury Coach / All Meals Included', 7),
            _ph('Route: Delhi / NCR Origin → Kurukshetra (1N) → Pinjore & Panchkula (2N) → Return.', 8),
            _ph('TRAGUIN Signature Experience: Special academic interactions, analytical worksheets, and quiz platforms', 9),
            _ph('Curated by TRAGUIN Experts: Safety audits completed prior to student arrival at all properties, restaurants,', 10),
            _ph('Premium Handpicked Hotels: Properties featuring modern security protocols, functional CCTV systems, and', 11),
            _ph('Exclusive Recommendations: Access to expert local guides specializing in Vedic history, modern industrial', 12),
            _ph('Institutional Guidelines: Students must carry valid institutional ID cards at all times during sightseeing tours.', 13),
            _ph('Weather & Clothing: Autumn and winter months (October to March) require comfortable woolen layers;', 14)
        ],
        moods=['Heritage', 'Family', 'Spiritual'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Group Pricing Available)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Educational Tour Kurukshetra & Pinjore',
        overview="03 Nights / 04 Days Premium Educational Odyssey Welcome to an expertly curated academic exploration across the historic landscapes of Haryana, thoughtfully conceptualized by TRAGUIN. This premium tour package seamlessly blends India's deep Vedic roots with modern scientific achievements and environmental sciences, offering an immersive learning experience for students. From the ancient battlefield of Mahabharata in Kurukshetra to the architectural and ecological wonders of northern Haryana, our premium travel consultants ensure an enriching, safe, and entirely unforgettable educational journey. TRAGUIN Premium Travel & Luxury Holidays\n\nTOUR OVERVIEW\nThe TRAGUIN Haryana Educational Tour is a signature bespoke program tailored to foster experiential learning outside the traditional classroom. This comprehensive itinerary covers key heritage, scientific, and ecological hubs in Haryana, presenting students with handpicked academic engagements under the constant supervision of expert guides. Travel Dates: Flexible / Customizable as per institutional requirements. Group / FIT: School Educational Delegation (FIT / Large Group formats). Vehicle: Premium high-deck luxury air-conditioned touring coaches equipped with emergency first-aid systems. Meal Plan: Multi-cuisine, highly hygienic buffer meals (Breakfast, Lunch, and Dinner) prepared to suit student health standards. Route: Delhi / NCR Origin → Kurukshetra (1N) → Pinjore & Panchkula (2N) → Return. TRAGUIN Curated Experience Note: Includes designated student interaction sessions, custom educational worksheets, priority entry passes to scientific research centers, and round-the-clock premium care coordination.\n\nWHY CHOOSE THE BEST HARYANA TOUR PACKAGE FOR STUDENTS?\nWhen considering the Best Haryana Tour Package for academic groups, the state stands out as a living textbook. A Haryana Family Tour or educational program brings alive centuries of history, scientific breakthroughs, and botanical diversity. Choosing a customized Haryana Honeymoon Package or an educational itinerary ensures that travelers witness the breathtaking landscapes and rich cultural identity of this robust state. Famous Attractions & Most Searched Experiences: This region is globally renowned for Kurukshetra Sightseeing, which spans the sacred Brahma Sarovar, the high-tech Kalpana Chawla Planetarium, and the interactive Kurukshetra Panorama and Science Centre. Students explore the roots of Indian philosophy alongside modern astronomy, making it a highly requested Premium Haryana Experience. Culture, Adventure & Instagram Locations: Beyond historical depth, Northern Haryana introduces students to Yadavindra Gardens at Pinjore—a magnificent operational Mughal terrace garden—and the pristine ecosystem of Morni Hills in Panchkula, which offers excellent popular Instagram locations for young travelers alongside lessons in biodiversity, geography, and terraced agricultural models.",
        seo_title='HR-006 | Educational Tour Kurukshetra & Pinjore | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Haryana package (HR-006 / TG-HR-EDU-006): Haryana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: COCHIN / DELHI TO KURUKSHETRA – SACRED HERITAGE &', 1),
            _ih('Day 02: KURUKSHETRA TO PINJORE & PANCHKULA – STEPPING INTO LIVING', 2),
            _ih('Day 03: MORNI HILLS ECO-TREK & SCIENCE INTERACTION AT PANCHKULA', 3),
            _ih('Day 04: CHANDIGARH REGIONAL URBAN EXPLORATION TO HOME DESTINATION', 4),
            _ih('TRAGUIN Signature Experience: Special academic interactions, analytical worksheets, and quiz platforms', 5),
            _ih('Curated by TRAGUIN Experts: Safety audits completed prior to student arrival at all properties, restaurants,', 6),
            _ih('Premium Handpicked Hotels: Properties featuring modern security protocols, functional CCTV systems, and', 7)
        ],
        days=[
            _day(
                1,
                'COCHIN / DELHI TO KURUKSHETRA – SACRED HERITAGE &',
                (
                    "ASTROBIOLOGY EXPLORATION The educational adventure begins with a warm welcome from your dedicated TRAGUIN representative at the pre-designated school assembly point or transit hub. Board your premium luxury coach and embark on a scenic drive along the national highway toward the historic city of Kurukshetra. As part of our signature TRAGUIN Haryana Packages, an expert tour director will engage students with brief introductory storytelling about the epic history of the region. TRAGUIN Premium Travel & Luxury Holidays Upon arrival, enjoy a seamless check-in at your handpicked, premium student-friendly hotel. After a fresh lunch, proceed for a comprehensive Kurukshetra Sightseeing session. The first stop is the breathtaking Brahma Sarovar, one of Asia's largest man-made water tanks, where students learn about ancient hydraulic engineering and spiritual customs. Next, explore the Kurukshetra Panorama and Science Centre, an exceptional interactive facility where scientific principles are explained alongside a massive 3D panorama of the Mahabharata war. Conclude the afternoon at the Kalpana Chawla Memorial Planetarium, built to honor India's iconic daughter and astronaut, fostering interest in astronomy and space sciences. Sightseeing Included: Brahma Sarovar, Kurukshetra Panorama & Science Centre, Kalpana Chawla Memorial Planetarium. architecture. Evening Experience: A beautiful, serene walk along the lit promenade of Brahma Sarovar, followed by an educational debriefing."
                ),
                [
                    'Optional Activities: Interactive Physics Quiz at the Science Park; Photography contest centered on ancient',
                    'Overnight Stay: Premium Handpicked Hotel in Kurukshetra.',
                    'Meals Included: Hygienic Lunch & Premium Buffet Dinner (Vegetarian).',
                ],
            ),
            _day(
                2,
                'KURUKSHETRA TO PINJORE & PANCHKULA – STEPPING INTO LIVING',
                (
                    'HISTORY Greet the morning with a healthy breakfast before completing check-out protocols. Your Luxury Haryana Holiday path now heads northward toward Panchkula and the historical town of Pinjore, nestled in the picturesque foothills of the Shivalik range. This scenic route offers breathtaking landscapes of pastoral Haryana transitioning into undulating green hills. Arrive in Pinjore and check into your premium accommodation. Post lunch, visit the iconic 17th-century Yadavindra Gardens (Pinjore Gardens), a masterpiece of Mughal architecture planned on a terraced layout. Here, students delve into subjects such as historical landscape architecture, Persian-style water channels, and botany as they wander through fruit orchards and manicured lawns. In the late afternoon, proceed to the nearby historic Bhima Devi Temple Complex, often referred to as the Khajuraho of North India, offering a fascinating archaeology lesson focused on 8th-11th century temple sculptures and historical preservation. Sightseeing Included: Yadavindra Mughal Gardens, Bhima Devi Temple Archaeological Museum, Pinjore Heritage Complex. gardens. Evening Experience: Illuminated musical fountains show at Pinjore Gardens, offering pristine cultural and sensory immersion. TRAGUIN Premium Travel & Luxury Holidays'
                ),
                [
                    'Optional Activities: Botanical identification trail; Sketching and architectural modeling workshops within the',
                    'Overnight Stay: Premium Resort / Luxury Hotel in Panchkula / Pinjore Suburbs.',
                    'Meals Included: Nutritious Breakfast, Hot Executive Lunch & Premium Buffet Dinner.',
                ],
            ),
            _day(
                3,
                'MORNI HILLS ECO-TREK & SCIENCE INTERACTION AT PANCHKULA',
                (
                    'Dedicate this day to environmental sciences and geography. After an early breakfast, board the coach for a premium excursion into Morni Hills, Haryana’s only hill station. This region presents stunning scenic beauty and dense flora, serving as an exceptional site for learning about ecological conservation, soil erosion, and Shivalik wildlife habitats. Students visit the pristine Tikkar Taal twin lakes, studying their unique geological formation. Return to Panchkula for lunch. In the afternoon, visit the regional scientific centers or organize a curated interactive academic session at the hotel conference hall led by TRAGUIN tour directors. Students participate in team-building exercises, presentation sessions regarding their discoveries over the past two days, and structural academic quizzes, culminating in recognition certificates. Sightseeing Included: Morni Hills Eco-system, Tikkar Taal Lakes, Panchkula Nature Trails & Local Heritage Hubs. Evening Experience: TRAGUIN Special Gala Evening with an educational quiz finale, student performances, and prize distribution.'
                ),
                [
                    'Optional Activities: Guided light nature trek; Water harvesting and ecological field note workshop.',
                    'Overnight Stay: Premium Resort / Luxury Hotel in Panchkula / Pinjore Suburbs.',
                    'Meals Included: Full Breakfast, Packed or Resort Lunch & Premium Gala Dinner.',
                ],
            ),
            _day(
                4,
                'CHANDIGARH REGIONAL URBAN EXPLORATION TO HOME DESTINATION',
                (
                    'On the final day of your Haryana Family Tour and educational track, check out after a hearty breakfast. Before concluding the journey, your luxury coach takes you on a brief educational orientation tour of the adjoining capital grid. Visit the world-famous Rock Garden of Chandigarh, an unparalleled monument of sustainability created entirely out of industrial and domestic waste by Nek Chand. This visit provides an invaluable lesson in environmental recycling and creative urban arts. Following a comfortable lunch, begin the return journey back to your origin point. Students spend the transit time completing their educational worksheets and sharing unforgettable memories. Arrive back at the institutional campus by evening, where the TRAGUIN travel consultants formally conclude this premium educational journey. Sightseeing Included: Nek Chand Rock Garden, Sukhna Lake Ecological Precinct (Drive-by / Brief Stopover). Evening Experience: Arrival at school campus with systematic dispersal coordination. TRAGUIN Premium Travel & Luxury Holidays'
                ),
                [
                    'Optional Activities: Waste-to-wealth project presentation during travel transit.',
                    'Overnight Stay: None (Transit Day).',
                    'Meals Included: Buffet Breakfast & Delicious Mid-route Lunch.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Kimaya / Similar',
                'Kurukshetra',
                '03 Nights',
                'Deluxe',
                'Executive Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Kimaya / Similar | Executive Room | MAPAI',
            ),
            _hotel(
                'Hotel Red Castle / Divine Clerks',
                'Kurukshetra',
                '03 Nights',
                'Premium',
                'Super Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Red Castle / Divine Clerks | Super Deluxe Room | MAPAI',
            ),
            _hotel(
                'The Pearl Resort & Spa / Similar',
                'Kurukshetra',
                '03 Nights',
                'Luxury',
                'Luxury Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Pearl Resort & Spa / Similar | Luxury Suite | MAPAI',
            ),
            _hotel(
                'Curated Heritage Boutique Farm & Wellness Villa',
                'Kurukshetra',
                '03 Nights',
                'Ultra Luxury',
                'Royal Club Villa',
                'All Inclusive Premium Meals',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Curated Heritage Boutique Farm & Wellness Villa | Royal Club Villa | All Inclusive',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Selected handpicked hotels with multi-sharing configurations for students and single/twin for faculty.', 1),
            _inc_included('All Meals Included: Hygienic buffet breakfast, lunch, and dinner curated by institutional chefs.', 2),
            _inc_included('Luxury Transportation: Dedicated air-conditioned high-deck coaches throughout the tour track.', 3),
            _inc_included('Immersive Experiences: Entry tickets to all listed planetariums, science hubs, and heritage gardens.', 4),
            _inc_included('Personalized Assistance: Dedicated TRAGUIN tour directors and institutional safety marshals on-site.', 5),
            _inc_included('Complimentary Perks: Professional group photography, customized educational kits, and daily mineral water bottles.', 6),
            _inc_included('TRAGUIN Support: 24/7 centralized corporate helpline and emergency back-up medical coordination.', 7),
            _inc_excluded('Travel Tickets: Institutional flights or rail tickets from outstation cities to Delhi/NCR.', 8),
            _inc_excluded('Personal Expenses: Laundry services, telephone bills, souvenirs, or individual snacks.', 9),
            _inc_excluded('Optional Tours: Any amusement park entry fees or joyrides not defined in the core itinerary.', 10),
            _inc_excluded('Camera Fees: Commercial movie camera or high- end DSLR permissions at specific monuments.', 11),
            _inc_excluded('Insurance: Extended comprehensive personal medical insurance policies (can be supplemented by TRAGUIN).', 12),
        ],
    )
    return package, itinerary

def build_hr_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-007'
    tour_code = 'TRG-HAR-007'
    title = 'Haryana Explorer'
    duration = '05 Nights / 06 Days'
    slug = 'hr-007-haryana-explorer'
    itin_slug = 'hr-007-haryana-explorer-itinerary'
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
            _ph('Serial code HR-007 | TRAGUIN tour code TRG-HAR-007', 1),
            _ph('State / Country: Haryana / India | Category: Premium Family', 2),
            _ph('Destinations: Gurugram • Sultanpur • Kurukshetra • Pinjore • Chandigarh', 3),
            _ph('Ideal for: Family Vacations, Luxury Explorers & Heritage Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Customised)', 6),
            _ph('Vehicle / Meals: Luxury Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked routing to avoid highway traffic, maximizing your leisure and', 9),
            _ph('Exclusive Recommendations: VIP access parameters to select evening ceremonies and fine-dining', 10),
            _ph('Traditional Souvenirs: Bring home beautiful, authentic Phulkari embroidery jackets, dupattas, and suits from local markets. Haryana is also famous for exquisite hand-woven Punjabi Juttis, clay pottery artifacts, and magnificent brassware from Rewari. Gourmet & Cafes: Indulge your palate in rich local dairy delicacies, authentic hot tandoori paranthas with fresh white butter at premium Murthal en-route stops, and global artisan coffees across Gurugram’s high-end cafes.', 11),
            _ph('& TRAVEL INFORMATION', 12)
        ],
        moods=['Family', 'Heritage', 'Luxury'],
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
        tagline='Haryana Explorer',
        overview='HARYANA EXPLORER • LEGACY, LUXURY & LANDSCAPES Welcome to an unforgettable journey curated exclusively by TRAGUIN. Embark on the finest Haryana Family Tour designed to reveal the breathtaking landscapes, ancient epics, and modern sophisticated wonders of this historic region. As your premier travel consultants, TRAGUIN transforms your vacation into a seamless luxury holiday filled with handpicked hotels, immersive experiences, and deeply moving stories. From the high-paced cosmopolitan luxury of Gurugram to the sacred, timeless fields of Kurukshetra and the royal steps of Pinjore Gardens, every detail is engineered to create unforgettable memories.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between urban opulence, natural wildlife sanctuaries, sacred historical architecture, and manicured royal gardens. Travelling in a dedicated premium AC vehicle with professional chauffeur-driven assistance, your family will enjoy absolute comfort and privacy. With a carefully curated meal plan featuring lavish breakfasts and specialized dinners, this route represents the definitive premium Haryana experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, ensuring VIP entry privileges, local storytelling insight, and around- the-clock bespoke support.\n\nWHY CHOOSE THE BEST HARYANA TOUR PACKAGE?\nWhen considering a Luxury Haryana Holiday, discerning travellers seek more than just standard sightseeing; they seek a deeply immersive dive into culture, heritage, and contemporary comfort. Haryana boasts some of the most iconic attractions in Northern India. From the internationally acclaimed Sultanpur National Park—a top tourist place in Haryana for birdwatching and wildlife photography—to the legendary battlegrounds and spiritual heritage sites of Kurukshetra, the region offers unparalleled depth. For families and couples booking a bespoke Haryana Honeymoon Package or Haryana Family Tour, the state reveals highly popular Instagram locations like the majestic heritage stepwells, the CyberHub lifestyle zone, and the historic Mughal-style Pinjore Gardens. Whether you are looking for local handicraft shopping, indulging in traditional culinary delights, or seeking historical enlightenment where the holy Bhagavad Gita was spoken, our TRAGUIN Haryana Packages guarantee premium comfort, handpicked luxury stays, and curated exclusive experiences that make it the best time to visit Haryana.',
        seo_title='HR-007 | Haryana Explorer | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Haryana package (HR-007 / TRG-HAR-007): Gurugram • Sultanpur • Kurukshetra • Pinjore • Chandigarh with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GURUGRAM', 1),
            _ih('Day 02: GURUGRAM TO SULTANPUR NATIONAL PARK', 2),
            _ih('Day 03: GURUGRAM TO KURUKSHETRA', 3),
            _ih('Day 04: KURUKSHETRA TO PINJORE & CHANDIGARH', 4),
            _ih('Day 05: CHANDIGARH SIGHTSEEING', 5),
            _ih('Day 06: CHANDIGARH TO DELHI / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private family interaction and historical storytelling briefing before', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked routing to avoid highway traffic, maximizing your leisure and', 8),
            _ih('Exclusive Recommendations: VIP access parameters to select evening ceremonies and fine-dining', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GURUGRAM',
                (
                    "WELCOME TO THE CYBER CITY – URBAN LUXURY & OPULENCE Your premium Haryana experience begins as you arrive at New Delhi Airport/Railway Station, where a dedicated private luxury transport vehicle waits to escort you. Enter Gurugram, India's glittering corporate capital, and check into your handpicked premium luxury hotel. After a refreshing afternoon, step out for an exclusive evening experience at CyberHub, a globally recognized lifestyle epicenter. Enjoy an evening of fine dining, premium shopping, and vibrant urban photography."
                ),
                [
                    'Sightseeing Included: CyberHub, Kingdom of Dreams plaza ambiance, Heritage Transport Museum (optional).',
                    'Evening Experience: Gourmet dinner at an award-winning restaurant curated by TRAGUIN experts.',
                    'Overnight Stay: Gurugram (Premium / Luxury Hotel)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'GURUGRAM TO SULTANPUR NATIONAL PARK',
                (
                    'BREATHTAKING LANDSCAPES & MIGRATORY AVIAN MAJESTY Awake early for a refreshing, crisp morning drive to Sultanpur National Park, one of the top tourist places in Haryana for eco-tourism. This pristine bird sanctuary offers breathtaking landscapes and serves as a haven for hundreds of migratory bird species. Accompanied by a professional naturalist, enjoy private bird-spotting paths, serene lake views, and superb photography points. Spend your afternoon exploring local eco-resorts or visiting the ancient sheetla mata shrine before winding down with a luxury spa session back at your property.'
                ),
                [
                    'Sightseeing Included: Sultanpur Bird Sanctuary, Guided Nature Trails, Lake Observation Towers.',
                    'Optional Activities: Professional wildlife photography session with high-end camera gear hire.',
                    'Overnight Stay: Gurugram / Sultanpur Eco-Resort',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'GURUGRAM TO KURUKSHETRA',
                (
                    'THE CRADLE OF VEDIC CIVILIZATION & EPIC HERITAGE Depart after a sumptuous breakfast towards the land of the Mahabharata—Kurukshetra. This is an essential stop on any premium Haryana family tour. Visit Brahma Sarovar, a breathtakingly massive sacred water tank where the sky reflects elegantly on the holy waters. Explore Jyotisar, the iconic, emotionally moving site where Lord Krishna delivered the eternal message of the Bhagavad Gita under an ancient banyan tree. Witness an immersive multimedia light and sound show depicting the legendary epic.'
                ),
                [
                    'Sightseeing Included: Brahma Sarovar, Jyotisar Birthplace of Gita, Sri Krishna Museum, Sannihit Sarovar.',
                    'Evening Experience: Maha Aarti experience at Brahma Sarovar with reserved private seating.',
                    'Overnight Stay: Kurukshetra (Premium Selected Heritage Stay)',
                    'Meals Included: Breakfast & Traditional Elite Thali Dinner',
                ],
            ),
            _day(
                4,
                'KURUKSHETRA TO PINJORE & CHANDIGARH',
                (
                    'MUGHAL SPLENDOUR & ROYAL TERRACED GARDENS Drive north towards the beautiful Shivalik foothills to explore the iconic Pinjore Gardens (Yadavindra Gardens). Built in the 17th century, these majestic multi-level terraced gardens showcase spectacular fountains, Mughal- style architecture, and beautiful Japanese canopies. It is a highly popular Instagram location perfect for your family portraiture. In the evening, check into your ultra-luxury hotel in Chandigarh and relax in style.'
                ),
                [
                    'Sightseeing Included: Pinjore Gardens, Bhima Devi Temple Complex (Khajuraho of North India).',
                    'Evening Experience: Illuminated night walk through the grand fountains of Pinjore with refreshments.',
                    'Overnight Stay: Chandigarh / Panchkula Luxury Hotel',
                    'Meals Included: Breakfast & Exquisite Buffet Dinner',
                ],
            ),
            _day(
                5,
                'CHANDIGARH SIGHTSEEING',
                (
                    'THE TRI-CITY LUXURY EXPERIENCE & SCENIC BEAUTY Spend a magnificent day exploring the ultra-modern planning and scenic beauty of Chandigarh. Enjoy an immersive private tour of the world-famous Rock Garden, sculpted completely from recycled urban materials by Nek Chand. Next, visit the exquisite Rose Garden before concluding your afternoon at Sukhna Lake, where a private sunset boat cruise has been arranged exclusively for your family.'
                ),
                [
                    "Sightseeing Included: Nek Chand's Rock Garden, Zakir Hussain Rose Garden, Sukhna Lake Promenade.",
                    'Optional Activities: Shopping for authentic Phulkari textiles and local high-end souvenirs.',
                    'Overnight Stay: Chandigarh (Premium / Luxury Stay)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),
            _day(
                6,
                'CHANDIGARH TO DELHI / DEPARTURE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Indulge in a final lavish breakfast at your premium hotel. Your private luxury transport will safely drive you back along the smooth national highway to New Delhi Airport or Railway Station for your onward journey. Return home carrying a heart filled with sweet family bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Premier /',
                'Kurukshetra',
                '05 Nights',
                'Deluxe',
                'similar',
                'Hotel Divine Clerks /',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Premier / | similar | Hotel Divine Clerks /',
            ),
            _hotel(
                'Crowne Plaza / Hyatt',
                'Kurukshetra',
                '05 Nights',
                'Premium',
                'Regency',
                "The King's Sukham /",
                4,
                2,
                description="OPTION 02 – PREMIUM: Crowne Plaza / Hyatt | Regency | The King's Sukham /",
            ),
            _hotel(
                'The Leela Ambience /',
                'Kurukshetra',
                '05 Nights',
                'Luxury',
                'Trident',
                'Premium Heritage',
                4,
                3,
                description='OPTION 03 – LUXURY: The Leela Ambience / | Trident | Premium Heritage',
            ),
            _hotel(
                'The Oberoi Gurugram',
                'Kurukshetra',
                '05 Nights',
                'Ultra Luxury',
                '(Luxury Suite)',
                'VVIP Custom Private',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi Gurugram | (Luxury Suite) | VVIP Custom Private',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Handpicked hotels as per chosen category.', 1),
            _inc_included('Luxury Transportation: Private AC Innova Crysta for all transfers & sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfast and gourmet dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Customized family travel kit and refreshments upon arrival.', 5),
            _inc_included('Complimentary Experience: Private sunset boat ride ticket at Sukhna Lake.', 6),
            _inc_excluded('Airfare / Train tickets to and from New Delhi.', 7),
            _inc_excluded('Monument entry tickets, camera fees, and local guide charges.', 8),
            _inc_excluded('Personal expenses such as laundry, liquor, telephone calls, and tips.', 9),
            _inc_excluded('Any optional activities, adventure sports, or extended tours not specified.', 10),
        ],
    )
    return package, itinerary

def build_hr_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-008'
    tour_code = 'TRG-GURG-MICE-008'
    title = 'Gurgaon MICE Excellence'
    duration = '03 Nights / 04 Days'
    slug = 'hr-008-gurgaon-mice-excellence'
    itin_slug = 'hr-008-gurgaon-mice-excellence-itinerary'
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
            _ph('Serial code HR-008 | TRAGUIN tour code TRG-GURG-MICE-008', 1),
            _ph('State / Country: Haryana / India | Category: Corporate MICE &', 2),
            _ph('Destinations: Haryana', 3),
            _ph('Ideal for: Corporate Retreats, Team Building, Strategy Sessions, Executive MICE', 4),
            _ph('Best season: Year-Round (Best from October to March)', 5),
            _ph('Starting price: On Request (Bespoke Group Quotation)', 6),
            _ph('Vehicle / Meals: Premium Luxury Coaches & Luxury Innova / All Inclusive Boarding', 7),
            _ph('TRAGUIN Signature Experience: Customized team-building modules developed by corporate coaches to', 8),
            _ph('Curated by TRAGUIN Experts: Seamless coordination between the conference program and leisure', 9),
            _ph('Luxury Transportation Layout: High-end executive coaches fitted with onboard Wi-Fi connectivity and', 10),
            _ph('Exclusive Recommendations: Priority reservations at CyberHub’s premier restaurants and private', 11),
            _ph('& CORPORATE TERMS', 12),
            _ph('Advance Booking Guidelines: MICE retreat confirmations require a minimum 30-day notice period to', 13)
        ],
        moods=['Luxury', 'Family', 'Heritage'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Bespoke Group Quotation)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Gurgaon MICE Excellence',
        overview="GURGAON MICE EXCELLENCE • INNOVATION, COLLABORATION & TEAM ALIGNMENT Welcome to an ultra-premium executive experience conceptualized and managed by TRAGUIN. This exclusive Gurgaon Corporate Retreat is meticulously structured for high-performance leadership team alignment, high-impact strategic conferences, and sophisticated corporate team-building events. Elevate your corporate culture against the backdrop of Gurgaon's soaring skyscrapers, world-class business ecosystems, and luxurious secluded resorts. TRAGUIN transforms conventional corporate itineraries into deeply immersive experiences, seamlessly combining state-of-the-art conference infrastructure with handpicked hotels, breathtaking landscapes, and unforgettable memories.\n\nTOUR OVERVIEW\nThis elite 4-Day Corporate MICE itinerary is designed to maximize executive networking, team motivation, and leadership collaboration. Your team will experience the absolute pinnacle of luxury business travel, supported by premium transportation layouts including high-end executive coaches and private luxury sedans. Accommodating all elements of custom business retreats, our program integrates state-of-the-art boardrooms, premium catering menus, dedicated AV coordinators, and custom corporate team building games. From initial airport transfers to the final gala banquet night, every touchpoint reflects the signature TRAGUIN curated experience guarantee—ensuring seamless execution, flawless prestige, and zero-downtime productivity.\n\nWHY CHOOSE GURGAON FOR YOUR PREMIUM CORPORATE MICE\nRETREAT? When organizations research the Best Gurgaon Tour Package for corporate engagements, they discover a cosmopolitan epicenter that blends dynamic business venues with elite leisure facilities. Gurgaon stands out as the ultimate destination for a Luxury Gurgaon Holiday built around professional corporate development. Hosting an expansive grid of global corporations, Gurgaon offers iconic attractions ranging from the magnificent CyberHub lifestyle precinct to the tranquil, scenic beauty of eco-friendly resorts in Manesar and the therapeutic hot springs of Sohna. Whether planning a focused Gurgaon Family Tour for employee engagement rewards, a grand corporate milestone gala, or looking for premium handpicked properties for an executive summit, our highly sought-after TRAGUIN Gurgaon Packages deliver impeccable premium stays and customized exclusive experiences. From premium brand retail shopping at upscale luxury malls to high-octane team adventure challenges, selecting the Best Time to Visit Gurgaon ensures your executive team experiences the finest conference facilities, top tourist places in Gurgaon, and unmatched luxury transport configurations in Northern India.",
        seo_title='HR-008 | Gurgaon MICE Excellence | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Haryana package (HR-008 / TRG-GURG-MICE-008): Haryana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GURGAON & HIGH-IMPACT NETWORKING', 1),
            _ih('Day 02: STRATEGY SYMPOSIUM & COLLABORATIVE TEAM-BUILDING', 2),
            _ih('Day 03: HERITAGE EXPLORATION & GRAND GALA AWARDS NIGHT', 3),
            _ih('Day 04: WELLNESS IN SOHNA & CORPORATE DEPARTURE', 4),
            _ih('TRAGUIN Signature Experience: Customized team-building modules developed by corporate coaches to', 5),
            _ih('Curated by TRAGUIN Experts: Seamless coordination between the conference program and leisure', 6),
            _ih('Luxury Transportation Layout: High-end executive coaches fitted with onboard Wi-Fi connectivity and', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GURGAON & HIGH-IMPACT NETWORKING',
                (
                    'WELCOME CONCIERGE, CHECK-IN & CYBER CITY EXCURSION Arrive at New Delhi International Airport, where a private executive concierge from TRAGUIN welcomes your corporate delegation with VIP arrival amenities. Board your premium luxury transportation coach and transfer directly to your handpicked ultra-luxury hotel in Gurgaon. After checking into your premium stays, assemble in the main executive boardroom for an analytical pre-retreat briefing and a networking luncheon. In the evening, visit CyberHub—the crown jewel of Gurgaon sightseeing—for a curated corporate dine-around experience, perfectly blending upscale social dynamics with unforgettable memories.'
                ),
                [
                    'Sightseeing Included: CyberHub Promenade, Galleria Luxury High-street, Sector 29 Entertainment Hub.',
                    'Evening Experience: Exclusive ice-breaking cocktail reception and gourmet dinner at a premium restaurant.',
                    'Overnight Stay: Gurgaon (Five-Star Luxury Hotel)',
                    'Meals Included: Welcome Drink, Business Lunch & Gourmet Networking Dinner',
                ],
            ),
            _day(
                2,
                'STRATEGY SYMPOSIUM & COLLABORATIVE TEAM-BUILDING',
                (
                    'CONFERENCE WORKSHOPS & HIGH-OCTANE ADVENTURE EXCURSIONS Commence the day with a gourmet breakfast before gathering in the grand ballroom for your annual corporate strategy conference, equipped with premium AV systems and high-speed enterprise connectivity. Following a business networking lunch, transition to an intensive, immersive team-building experiential session curated by TRAGUIN experts at a premium adventure resort. Participate in structured team-building games, leadership problem-solving scenarios, and high-energy trust activities designed to enhance organizational communication and foster unforgettable team synergy.'
                ),
                [
                    'Sightseeing Included: Premium Adventure Outpost, Leisure Valley Botanical Park, Instagram lifestyle hot-spots.',
                    'Optional Activities: Professional corporate portraiture and dynamic team highlight video drone capture.',
                    'Overnight Stay: Gurgaon (Five-Star Luxury Hotel)',
                    'Meals Included: Gourmet Breakfast, Mid-session High Tea, and Executive Buffet Dinner',
                ],
            ),
            _day(
                3,
                'HERITAGE EXPLORATION & GRAND GALA AWARDS NIGHT',
                (
                    "TRANSPORT MUSEUM TO ROYAL GALA EXTRAVAGANZA Enjoy a premium breakfast before heading out on a scenic drive to the Heritage Transport Museum, celebrated as one of the top tourist places in Gurgaon and a popular Instagram location for high-profile executive groups. Explore India's rich transport legacy through beautifully restored vintage cars and historic aviation exhibits. Return to the resort for an afternoon of leisure, spa therapies, or golf matches. As twilight falls, gather for the highlight of the retreat—the Grand Gala Awards Night, featuring live entertainment, executive award presentations, and custom dining arrangements. perimeter)."
                ),
                [
                    'Sightseeing Included: Heritage Transport Museum private guided tour, Sultanpur Bird Sanctuary (scenic',
                    'Evening Experience: Red-carpet corporate awards presentation ceremony with a premium live band.',
                    'Overnight Stay: Gurgaon Luxury Golf & Spa Resort Hub',
                    'Meals Included: Lavish Breakfast, Curated Mid-day Lunch, and Gala Celebratory Dinner',
                ],
            ),
            _day(
                4,
                'WELLNESS IN SOHNA & CORPORATE DEPARTURE',
                (
                    'MINDFULNESS REFLECTION & TRANSFERS TO NEW DELHI Begin your final morning with an optional wellness and mindfulness meditation session overlooking the tranquil, scenic beauty of the Shivalik foothills near Sohna. Gather for a final executive farewell brunch to recap key strategic takeaways from the retreat. Pack your luggage and board your premium transport coaches as TRAGUIN ensures a seamless transfer back to New Delhi International Airport or Railway Station, concluding a world-class corporate experience filled with strategy, success, and unforgettable memories.'
                ),
                [
                    'Transfers Included: Synchronized group coach drops to Airport/Railway hubs.',
                    'Meals Included: International Farewell Brunch Arrangement',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Kimaya / Similar',
                'Kurukshetra',
                '03 Nights',
                'Deluxe',
                'Executive Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Kimaya / Similar | Executive Room | MAPAI',
            ),
            _hotel(
                'Hotel Red Castle / Divine Clerks',
                'Kurukshetra',
                '03 Nights',
                'Premium',
                'Super Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hotel Red Castle / Divine Clerks | Super Deluxe Room | MAPAI',
            ),
            _hotel(
                'The Pearl Resort & Spa / Similar',
                'Kurukshetra',
                '03 Nights',
                'Luxury',
                'Luxury Suite',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: The Pearl Resort & Spa / Similar | Luxury Suite | MAPAI',
            ),
            _hotel(
                'Curated Heritage Boutique Farm & Wellness Villa',
                'Kurukshetra',
                '03 Nights',
                'Ultra Luxury',
                'Royal Club Villa',
                'All Inclusive Premium Meals',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Curated Heritage Boutique Farm & Wellness Villa | Royal Club Villa | All Inclusive',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Chosen luxury rooms with twin/single configurations.', 1),
            _inc_included('Luxury Transportation: Private luxury coaches for transfers, airport runs, & excursions.', 2),
            _inc_included('MICE Infrastructure: 1 Full-day conference hall use with projectors, audio, and pads.', 3),
            _inc_included('Full Board Catering: Multi-cuisine breakfast, premium lunches, and themed dinners.', 4),
            _inc_included('Welcome & Branding: Specialized group registration, welcome drinks, and check-in help.', 5),
            _inc_included('TRAGUIN Support: On-site MICE operations manager overseeing all event timelines.', 6),
            _inc_excluded('Airfares, flight adjustments, or interstate railway booking tickets.', 7),
            _inc_excluded('Liquor packages, bar tabs, and custom entertainment items during gala dinner.', 8),
            _inc_excluded('Personal expenditures: long-distance phone lines, laundry facilities, in-room mini-bars.', 9),
            _inc_excluded('Extended touring routes, vehicle use after business hours, or individual travel extensions.', 10),
        ],
    )
    return package, itinerary

def build_hr_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-009'
    tour_code = 'TRG-HAR-009'
    title = 'Heritage Haryana'
    duration = '04 Nights / 05 Days'
    slug = 'hr-009-heritage-haryana'
    itin_slug = 'hr-009-heritage-haryana-itinerary'
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
            _ph('Serial code HR-009 | TRAGUIN tour code TRG-HAR-009', 1),
            _ph('State / Country: Haryana / India | Category: Heritage Family', 2),
            _ph('Destinations: Delhi • Kurukshetra • Jyotisar • Narnaul • Heritage Haveli Stay', 3),
            _ph('Ideal for: Families, History Enthusiasts & Heritage Explorers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium Customised)', 6),
            _ph('Vehicle / Meals: Luxury Tourer / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private archeological brief and architectural walk around Narnaul', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked scheduling ensuring perfect timing for sunset photography at', 9),
            _ph('Personalized Assistance: Elite verified chauffeurs who double as expert local route navigators for', 10),
            _ph('Exclusive Recommendations: Access points to authentic heritage eateries and verified handloom', 11),
            _ph('Local Handlooms: Explore local markets to find exquisite traditional Dari rugs, ethnic leather footwear, handwoven phulkari patterns, and fine brassware souvenirs directly from regional artisans. Traditional Delicacies: Taste authentic rich milk sweets, freshly prepared organic ghee delicacies, and traditional tandoori dishes served at high-end highway pitstops.', 12),
            _ph('& TRAVEL INFORMATION', 13)
        ],
        moods=['Heritage', 'Family', 'Spiritual'],
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
        tagline='Heritage Haryana',
        overview="HERITAGE HARYANA • EPIC LEGENDS & ROYAL FORTRESSES Welcome to a timeless journey back into antiquity, seamlessly curated by TRAGUIN. Embark on the finest Heritage Haryana Family Tour, a luxury holiday specifically sculpted to uncover royal stepwells, legendary battlefields, and architectural landmarks. As your expert travel consultants, TRAGUIN presents a premium guest-facing itinerary packed with handpicked hotels, breathtaking landscapes, and immersive experiences. Walk the holy grounds where empires rose and fell, returning home with unforgettable memories etched deep into your family heritage.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite perspective on India's deep-rooted past. Travel in absolute comfort in a premium private AC vehicle with custom amenities and an expert chauffeur. Enjoy a sophisticated meal plan comprising lavish morning breakfast buffets and signature local dinners across prestigious properties. Featuring an exclusive TRAGUIN curated experience note, your loved ones will benefit from prioritized monument access, verified heritage guides, and dedicated support parameters.\n\nWHY CHOOSE THE BEST HERITAGE HARYANA TOUR PACKAGE?\nTo truly appreciate a Luxury Haryana Holiday, one must traverse beyond standard modern highways into its hidden legacy towns. This region hosts the top tourist places in Haryana, presenting an unparalleled collection of archaeological marvels and ancient sites. From the iconic water bodies of Kurukshetra to the royal tombs, palatial mansions, and grand stepwells of Narnaul, history buffs will enjoy unmatched cultural wealth. For family getaways or a unique Haryana Honeymoon Package, this route provides highly popular Instagram locations like Jal Mahal, Chini Koti, and the expansive Brahma Sarovar. Immerse yourselves in boutique artisan shopping, traditional organic cuisines, and majestic folklore storytelling. Our specialized TRAGUIN Haryana Packages guarantee premium stays, expert coordination, and an unforgettable premium Haryana experience during the absolute best time to visit Haryana.",
        seo_title='HR-009 | Heritage Haryana | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Haryana package (HR-009 / TRG-HAR-009): Delhi • Kurukshetra • Jyotisar • Narnaul • Heritage Haveli Stay with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DELHI – DRIVE TO KURUKSHETRA', 1),
            _ih('Day 02: KURUKSHETRA SIGHTSEEING TO JYOTISAR', 2),
            _ih('Day 03: KURUKSHETRA TO NARNAUL HERITAGE HUB', 3),
            _ih('Day 04: NARNAUL EXPLORATION & JAL MAHAL PRIVÉ', 4),
            _ih('Day 05: NARNAUL TO DELHI / DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private archeological brief and architectural walk around Narnaul', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked scheduling ensuring perfect timing for sunset photography at', 7),
            _ih('Personalized Assistance: Elite verified chauffeurs who double as expert local route navigators for', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DELHI – DRIVE TO KURUKSHETRA',
                (
                    'GATEWAY TO THE LAND OF SPIRITUALITY & LEGENDS Your premium Haryana experience starts with a warm welcome at New Delhi Airport/Railway Station by our representative. Board your premium luxury transport vehicle and enjoy a smooth scenic drive to the legendary town of Kurukshetra. Upon arrival, check into your chosen handpicked hotel. After freshening up, spend a serene afternoon by the grand Sannihit Sarovar, believed to be the meeting point of seven sacred rivers.'
                ),
                [
                    "Sightseeing Included: Sannihit Sarovar, Sheikh Chilli's Tomb (The Taj of Haryana), local museum galleries.",
                    'Evening Experience: Illuminated walk through the grand brick arches of historic monuments.',
                    'Overnight Stay: Kurukshetra (Premium / Luxury Selected Stay)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'KURUKSHETRA SIGHTSEEING TO JYOTISAR',
                (
                    "THE IMMERSIVE SAGAS OF BRONZE STATUES & HOLY WATERWAYS Dedicate your morning to Kurukshetra Sightseeing, exploring the legendary Brahma Sarovar—one of Asia's largest man-made water tanks. Proceed next to Jyotisar, a deeply moving site where Lord Krishna delivered the holy sermon of the Bhagavad Gita under an ancient banyan tree. Witness the breathtaking landscapes of the heritage park and explore the Sri Krishna Museum housing millennia-old sculptures."
                ),
                [
                    'Sightseeing Included: Brahma Sarovar, Jyotisar Birthplace, Sri Krishna Museum, Panorama & Science Centre.',
                    'Evening Experience: Exclusive multimedia light & sound show at Jyotisar curated by TRAGUIN experts.',
                    'Overnight Stay: Kurukshetra (Premium Selected Resort)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'KURUKSHETRA TO NARNAUL HERITAGE HUB',
                (
                    'ROYAL ARCHITECTURE & HIDDEN STEPWELL MAJESTY After a hearty breakfast, check out and proceed on a scenic route toward Narnaul, a town dating back to the Mahabharata and Mughal era. Check into a meticulously restored premium heritage stay. Spend your afternoon discovering the magnificent Chor Gumbad and the breathtaking multi-story stepwells (Baolis) that make Narnaul a highly popular Instagram location for architectural lovers.'
                ),
                [
                    "Sightseeing Included: Chor Gumbad, Mirza Raja Ali Jan's Baoli, Shah Wilayat Tomb Complex.",
                    'Optional Activities: Traditional interactive pottery workshop with local village artisans.',
                    'Overnight Stay: Narnaul / Heritage Palace Vicinity Stay',
                    'Meals Included: Breakfast & Authentic Regional Heritage Dinner',
                ],
            ),
            _day(
                4,
                'NARNAUL EXPLORATION & JAL MAHAL PRIVÉ',
                (
                    'PALACES ON WATER & MAJESTIC FORTIFIED HILLS Discover the ultimate architectural gem today: the Jal Mahal of Narnaul, an exquisite pleasure palace standing perfectly in the center of a water tank, showcasing a fusion of Persian and Indian styles. Follow this with a trip to Dhosi Hill, a volcanic site steeped in Vedic history where ancient hermits performed penance. Capture high- contrast photography at these iconic attractions.'
                ),
                [
                    'Sightseeing Included: Jal Mahal, Dhosi Hill Heritage Fortified Outposts, Ibrahim Khan Suri Tomb.',
                    'Evening Experience: Private family sundowner overlook from the royal balconies of Jal Mahal.',
                    'Overnight Stay: Narnaul / Heritage Boutique Resort',
                    'Meals Included: Breakfast & Premium Continental Fusion Dinner',
                ],
            ),
            _day(
                5,
                'NARNAUL TO DELHI / DEPARTURE',
                (
                    'RETURNING HOME WITH CHERISHED UNFORGETTABLE MEMORIES Relish a relaxed morning breakfast buffet at your royal accommodation. Conclude your shopping for fine local traditional items and handicrafts before boarding your private luxury transport vehicle. Enjoy a comfortable highway journey back to New Delhi Airport or Railway Station for your return trip. Your royal tour concludes here, leaving you with unforgettable memories crafted seamlessly by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door highway drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Divine Clerks / similar',
                'Kurukshetra | Narnaul',
                '02 Nights Kurukshetra + 02 Nights Narnaul',
                'Deluxe',
                'Deluxe Room | Heritage Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Divine Clerks / similar | Shree Hari Heritage Hotel / similar | MAPAI',
            ),
            _hotel(
                "The King's Sukham / similar",
                'Kurukshetra | Narnaul',
                '02 Nights Kurukshetra + 02 Nights Narnaul',
                'Premium',
                'Premium Suite | Heritage Plaza Luxury Rooms',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description="OPTION 02 – PREMIUM: The King's Sukham / similar | Hotel Heritage Plaza Luxury Rooms | MAPAI",
            ),
            _hotel(
                'Premium Heritage Haveli Suite',
                'Kurukshetra | Narnaul',
                '02 Nights Kurukshetra + 02 Nights Narnaul',
                'Luxury',
                'Heritage Haveli Suite | Restored Boutique Fort Mansion',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: Premium Heritage Haveli Suite | Restored Boutique Fort Mansion / Haveli Stay | MAPAI',
            ),
            _hotel(
                'VVIP Custom Private Villa Stay',
                'Kurukshetra | Narnaul',
                '02 Nights Kurukshetra + 02 Nights Narnaul',
                'Ultra Luxury',
                'Private Villa | The Neemrana Fort Palace Elite Wing',
                'Bespoke Heritage Dining Plan',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: VVIP Custom Private Villa Stay | The Neemrana Fort Palace Elite Wing (Nearby) | Bespoke Plan',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodation: Stays in handpicked boutique heritage properties.', 1),
            _inc_included('Luxury Transportation: Private Chauffeur- driven AC transport for all transits.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfast and gourmet thematic dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated travel concierge assistant on call.', 4),
            _inc_included('Welcome Amenities: Personalized welcome kit, wet tissues, and premium mineral water.', 5),
            _inc_included('Complimentary Experience: Prioritized sound and light multimedia show passes.', 6),
            _inc_included('TRAGUIN Premium Luxury Itinerary — HR-009 4', 7),
            _inc_excluded('Airfare, flight insurance, or train transit tickers to Delhi.', 8),
            _inc_excluded('Monument entry fees, camera permits, and local tip allocations.', 9),
            _inc_excluded('Personal items such as laundry services, luxury room service, or bar orders.', 10),
            _inc_excluded('Any private optional tours or additional mileage routing.', 11),
        ],
    )
    return package, itinerary

def build_hr_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'HR-010'
    tour_code = 'TRG-HAR-010'
    title = 'Complete Haryana Premium Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'hr-010-complete-haryana-premium-family-tour'
    itin_slug = 'hr-010-complete-haryana-premium-family-tour-itinerary'
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
            _ph('Serial code HR-010 | TRAGUIN tour code TRG-HAR-010', 1),
            _ph('State / Country: Haryana / India | Category: Complete', 2),
            _ph('Destinations: Gurugram • Sultanpur • Kurukshetra • Pinjore • Chandigarh • Hisar', 3),
            _ph('Ideal for: Multi-Generation Families, Culture Buffs & Luxury Seekers', 4),
            _ph('Best season: October to March (Pleasant and Cool Winter Months)', 5),
            _ph('Starting price: On Request (Premium Bespoke Customization)', 6),
            _ph('Vehicle / Meals: Luxury Chauffeur- driven Innova Crysta / MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private, reserved seating at the grand Brahma Sarovar Maha Aarti with', 8),
            _ph('Curated by TRAGUIN Experts: Smooth highway routing with optimized break stops, ensuring a', 9),
            _ph('Premium Handpicked Hotels: Elite properties selected for their exceptional hospitality, cleanliness,', 10),
            _ph('Luxury Transportation: Uniformed, background-verified professional chauffeurs with extensive route', 11),
            _ph("Local Markets & Souvenirs: Shop for beautiful Phulkari embroidered textiles, hand-loomed fabrics, traditional brassware handicrafts from Rewari, and authentic handcrafted footwear (jutti) at popular local market bazaars. Food & Cafes: Enjoy rich milk-based traditional sweets, authentic paranthas with fresh butter at landmark highway stops, and global artisan coffee and multi-cuisine delicacies across Gurugram and Chandigarh's high-end dining districts.", 12),
            _ph('& BOOKING INFORMATION', 13)
        ],
        moods=['Family', 'Heritage', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Bespoke Customization)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Complete Haryana Premium Family Tour',
        overview="COMPLETE HARYANA • GRAND HERITAGE, ECO-LUXURY & URBAN SPLENDOUR Welcome to an extraordinary exploration of legacy, culture, and absolute comfort meticulously designed by TRAGUIN. This exclusive Complete Haryana Family Tour is a masterfully balanced luxury travel experience curated for multi-generational families. Our premium travel itinerary spans across the state's historical epics, modern cosmopolitan landmarks, and breathtaking landscapes. As your dedicated travel consultants, TRAGUIN transforms each day into an immersive luxury holiday featuring handpicked hotels, executive logistics, and highly engaging local narratives. From the dazzling cityscape of Gurugram to the sacred waters of Kurukshetra, the royal gardens of Pinjore, and the historical forts of Hisar, prepare to build unforgettable memories with your loved ones.\n\nTOUR OVERVIEW\nThis elite 5 Nights / 6 Days fully-guided route offers a comprehensive panoramic overview of Haryana’s finest treasures. Travelling in an executive-class, fully sanitized, premium air-conditioned vehicle with highly experienced uniformed chauffeurs, your family will enjoy absolute safety, privacy, and curated priority access. Our high-end meal plan encompasses generous daily buffet breakfasts alongside themed gourmet dinners featuring regional and global cuisines. Every detail of this premium travel proposal carries the distinct hallmark of TRAGUIN curated experiences—guaranteeing premium handpicked accommodations, VIP entrances, and 24/7 dedicated travel support.\n\nWHY CHOOSE THE BEST COMPLETE HARYANA TOUR PACKAGE?\nA true Luxury Haryana Holiday reveals the diverse soul of Northern India. Travelers who book the definitive Best Haryana Tour Package get to experience a spectacular combination of highly historic battlegrounds, royal architecture, world-class wildlife reserves, and luxurious contemporary lifestyle centers. From the internationally celebrated Sultanpur National Park—a top tourist place in Haryana for bird watching—to the profound spiritual heritage sites of Kurukshetra, the destination delivers endless deep experiences. For couples and families organizing a memorable Haryana Honeymoon Package or Haryana Family Tour, the state offers beautiful contrast and popular Instagram locations such as the multi-tiered Pinjore Gardens, the chic CyberHub complex, and the heritage stepwells. Travelers can indulge in authentic handicraft shopping, discover the historical remains of ancient forts, and enjoy the true culinary excellence of fine-dining venues. Choosing our signature TRAGUIN Haryana Packages promises a beautifully structured, elegant, and highly polished itinerary during the absolute best time to visit Haryana.",
        seo_title='HR-010 | Complete Haryana Premium Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Haryana package (HR-010 / TRG-HAR-010): Gurugram • Sultanpur • Kurukshetra • Pinjore • Chandigarh • Hisar with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN GURUGRAM', 1),
            _ih('Day 02: SULTANPUR NATIONAL PARK & HISAR HERITAGE', 2),
            _ih('Day 03: HISAR TO SACRED KURUKSHETRA', 3),
            _ih('Day 04: KURUKSHETRA TO PINJORE & CHANDIGARH', 4),
            _ih('Day 05: CHANDIGARH FULL-DAY SIGHTSEEING', 5),
            _ih('Day 06: CHANDIGARH TO DELHI / DEPARTURE', 6),
            _ih('TRAGUIN Signature Experience: Private, reserved seating at the grand Brahma Sarovar Maha Aarti with', 7),
            _ih('Curated by TRAGUIN Experts: Smooth highway routing with optimized break stops, ensuring a', 8),
            _ih('Premium Handpicked Hotels: Elite properties selected for their exceptional hospitality, cleanliness,', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN GURUGRAM',
                (
                    'WELCOME TO THE COSMOPOLITAN HEARTLAND & ELITE URBAN LIVING Your premium Complete Haryana experience begins with a warm VIP greeting as you arrive at New Delhi Airport or Railway Station. Your private luxury vehicle will seamlessly transfer your family to an elite handpicked hotel in Gurugram. After checking in and enjoying a smooth afternoon of relaxation, step out to experience the vibrant energy of CyberHub—the crown jewel of urban entertainment in the National Capital Region. This premium boulevard offers phenomenal fine dining, luxury boutique retail shopping, and fantastic lifestyle photography points.'
                ),
                [
                    'Sightseeing Included: CyberHub Promenade, Luxury Galleria retail exploration, High-street culinary districts.',
                    'Evening Experience: A curated multi-course gourmet dinner at an award-winning premium restaurant.',
                    'Overnight Stay: Gurugram (Premium / Luxury 5-Star Hotel)',
                    'Meals Included: Welcome Amenities & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'SULTANPUR NATIONAL PARK & HISAR HERITAGE',
                (
                    'NATURAL AVIAN SANCTUARIES & STEPPING INTO THE ANCIENT KINGDOMS Embrace the day with a crisp, refreshing morning excursion to Sultanpur National Park, universally rated among the top tourist places in Haryana. Marvel at the breathtaking landscapes as thousands of rare migratory and resident birds gather across the natural wetland lakes. Following an expert naturalist-led bird watching tour, enjoy a scenic drive towards the historic city of Hisar. In the afternoon, explore the magnificent Asigarh Fort (Hansi) and the iconic Firoz Shah Palace complex, featuring ancient underground structures and superb architectural photography opportunities.'
                ),
                [
                    'Sightseeing Included: Sultanpur Bird Sanctuary Trails, Firoz Shah Palace, Lat ki Masjid, Hansi Fort Ruins.',
                    'Evening Experience: Private heritage presentation over traditional high-tea at your premium hotel.',
                    'Overnight Stay: Hisar (Premium Selected Executive Luxury Property)',
                    'Meals Included: Premium Breakfast & Elaborate Buffet Dinner',
                ],
            ),
            _day(
                3,
                'HISAR TO SACRED KURUKSHETRA',
                (
                    'THE EPIC BATTLEFIELDS OF MAHABHARATA & SACRED REFLECTIONS Following a premium breakfast, your luxury tour advances to the historic and spiritually significant city of Kurukshetra. Arrive and explore the breathtaking Brahma Sarovar, an architectural marvel and one of Asia’s largest man-made sacred water tanks. Walk the hallowed grounds of Jyotisar, the emotionally moving birthplace of the holy Bhagavad Gita, where Lord Krishna delivered his timeless spiritual discourse under a legendary 5,000-year-old banyan tree. Conclude your evening by witnessing a spectacular multimedia light and sound show. Science Center.'
                ),
                [
                    'Sightseeing Included: Brahma Sarovar, Jyotisar Gita Birthplace, Sri Krishna Heritage Museum, Panorama',
                    'Evening Experience: Reserved front-row private seating for the magnificent Brahma Sarovar Evening Aarti.',
                    'Overnight Stay: Kurukshetra (Premium Selected Heritage Boutique Hotel)',
                    'Meals Included: Breakfast & Special Traditional Royal Vegetarian Dinner',
                ],
            ),
            _day(
                4,
                'KURUKSHETRA TO PINJORE & CHANDIGARH',
                (
                    "ROYAL MUGHAL SYMMETRY & SECLUDED FOOTHILL ESCAPES Bid farewell to Kurukshetra and travel north towards the scenic Shivalik foothills to explore Pinjore Gardens, also known as Yadavindra Gardens. This historic 17th-century estate features grand terraced levels, active fountains, pristine channels, and classical Mughal architecture, making it an incredibly popular Instagram location. Next, explore the adjacent Bhima Devi Temple complex, celebrated as the 'Khajuraho of North India' due to its detailed historical stone carvings. Afterward, take a smooth drive to check into your ultra-luxury hotel in Chandigarh."
                ),
                [
                    'Sightseeing Included: Pinjore Terraced Gardens, Shivalik Foothill Views, Bhima Devi Archaeological Site.',
                    'Optional Activities: Private heritage walk guided by an expert art historian.',
                    'Overnight Stay: Chandigarh / Panchkula (Luxury 5-Star Hotel)',
                    'Meals Included: Breakfast & Exquisite Continental-Indian Fusion Dinner',
                ],
            ),
            _day(
                5,
                'CHANDIGARH FULL-DAY SIGHTSEEING',
                (
                    'MODERN URBAN DESIGN, URBAN ARTISTRY & SCENIC LAKE CRUISING Dedicate a glorious day to experiencing the beautiful planning, clean infrastructure, and scenic beauty of Chandigarh. Begin with an exclusive private tour of the world-renowned Rock Garden, a spectacular maze of outdoor art created entirely from recycled industrial and domestic materials by Nek Chand. Visit the fragrant Rose Garden before enjoying a relaxing afternoon along the banks of Sukhna Lake. To top off the experience, a private sunset boat cruise has been arranged exclusively for your family to enjoy the serene lake views. (Outer view).'
                ),
                [
                    "Sightseeing Included: Nek Chand's Rock Garden, Rose Garden, Sukhna Lake Promenade, Capitol Complex",
                    'Evening Experience: Private sunset boat cruise followed by an elite family farewell dinner curated by TRAGUIN.',
                    'Overnight Stay: Chandigarh (Luxury 5-Star Hotel)',
                    'Meals Included: Breakfast & Premium Farewell Dinner',
                ],
            ),
            _day(
                6,
                'CHANDIGARH TO DELHI / DEPARTURE',
                (
                    "FORWARDING JOURNEYS WITH CHERISHED FAMILY MEMORIES Indulge in a final lavish breakfast at your premium hotel's cafe. Your dedicated private vehicle will then pick you up for a smooth highway drive back to New Delhi. Your driver will safely drop you off at New Delhi Airport or the Railway Station for your onward journey. Return home carrying a heart filled with beautiful family moments and unforgettable memories, knowing your holiday was impeccably managed by TRAGUIN."
                ),
                [
                    'Transfers Included: Private chauffeur-driven door-to-door highway drop-off at Delhi.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree',
                'Kurukshetra',
                '05 Nights',
                'Deluxe',
                'Premier / similar',
                'Hotel Midtown',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree | Premier / similar | Hotel Midtown',
            ),
            _hotel(
                'Crowne Plaza /',
                'Kurukshetra',
                '05 Nights',
                'Premium',
                'Hyatt Regency',
                'Besta Fiesta',
                4,
                2,
                description='OPTION 02 – PREMIUM: Crowne Plaza / | Hyatt Regency | Besta Fiesta',
            ),
            _hotel(
                'The Leela',
                'Kurukshetra',
                '05 Nights',
                'Luxury',
                'Ambience / Trident',
                'Suncity Hotel',
                4,
                3,
                description='OPTION 03 – LUXURY: The Leela | Ambience / Trident | Suncity Hotel',
            ),
            _hotel(
                'The Oberoi',
                'Kurukshetra',
                '05 Nights',
                'Ultra Luxury',
                'Gurugram (Suite)',
                'Elite Private',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: The Oberoi | Gurugram (Suite) | Elite Private',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations across handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Private Innova Crysta for all transfers and sightseeing routes.', 2),
            _inc_included('Curated Meals: Daily five-star buffet breakfasts and specialty dinners (MAPAI).', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated elite guest relations manager on active standby.', 4),
            _inc_included('Welcome Amenities: Customized family welcome kit, snacks, and mineral water.', 5),
            _inc_included('Exclusive Experiences: Private sunset boat cruise charter tickets at Sukhna Lake.', 6),
            _inc_included('TRAGUIN Premium Luxury Itinerary — HR-010 5', 7),
            _inc_excluded('Airfare or interstate train ticketing expenses to reach New Delhi.', 8),
            _inc_excluded('Individual monument entry tickets, specialized camera permissions, and local guides.', 9),
            _inc_excluded('Personal incidentals such as room service, laundry, premium beverages, and tips.', 10),
        ],
    )
    return package, itinerary

HARYANA_DOMESTIC_BUILDERS = [
    build_hr_001,
    build_hr_002,
    build_hr_003,
    build_hr_004,
    build_hr_005,
    build_hr_006,
    build_hr_007,
    build_hr_008,
    build_hr_009,
    build_hr_010,
]
