"""Builder functions for TG-001 through TG-010 Telangana domestic packages."""

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

TELANGANA_SLUG = "telangana"


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


def build_tg_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-001'
    tour_code = 'TRG-TEL-001'
    title = 'HYDERABAD HIGHLIGHTS • A ROYAL FAMILY ESCAPE'
    duration = '03 Nights / 04 Days'
    slug = 'tg-001-hyderabad-highlights-a-royal-family-escape'
    itin_slug = 'tg-001-hyderabad-highlights-a-royal-family-escape-itinerary'
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
            _ph('Serial code TG-001 | TRAGUIN tour code TRG-TEL-001', 1),
            _ph('State / Country: Telangana / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Hyderabad •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Innova Crysta / MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Private, reserved seating coordination for the iconic Sound & Light', 8),
            _ph('Curated by TRAGUIN Experts: Smart, route-optimized itinerary designed to skip city congestion and', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen strictly based on high safety ratings, elite', 10),
            _ph('Luxury Transportation: Highly trained, polite, and background-verified chauffeurs with excellent local', 11)
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
        tagline='HYDERABAD HIGHLIGHTS',
        overview="HYDERABAD HIGHLIGHTS • A ROYAL FAMILY ESCAPE TRAGUIN Premium Luxury Itinerary — TG-001 1 Welcome to an unforgettable luxury vacation curated exclusively by TRAGUIN. Embark on the finest Hyderabad Family Tour, custom-tailored to immerse your loved ones in the iconic attractions, breathtaking landscapes, and timeless heritage of the Nizams. As your trusted premium travel consultants, TRAGUIN turns your itinerary into a seamless masterpiece featuring handpicked hotels, immersive experiences, and magical cultural insights. From the majestic echoes of Golconda to the cinematic wonders of Ramoji, cherish unforgettable memories with your family.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package provides an elite balance of heritage storytelling, cinematic entertainment, and contemporary relaxation. Travel in utmost safety and private comfort aboard a chauffeured luxury air-conditioned vehicle. With curated premium stays and an upscale meal plan featuring gourmet daily breakfast and exquisite dinner settings, this route ensures a flawless execution of the premium Telangana experience. Your entire family journey is augmented by the special TRAGUIN curated experience note, giving you access to elite guides, priority transfers, and around-the-clock specialized customer care.\n\nWHY BOOK THE BEST TELANGANA TOUR PACKAGE?\nChoosing a Luxury Telangana Holiday or a tailored Hyderabad Honeymoon Package means opening the doors to a world where ancient stone fortresses stand adjacent to cutting-edge metropolitan life. Hyderabad, famously known as the City of Pearls, features some of the top tourist places in Telangana. From the architectural wonder of the Charminar to the royal corridors of Chowmahalla Palace, Hyderabad sightseeing offers timeless historic marvels. Families choosing our Telangana Family Tour will discover popular Instagram locations like the serene Hussain Sagar Lake at twilight and the massive, record-breaking sets of Ramoji Film City. Delight your senses with local handicraft and pearl shopping at Laad Bazaar, sample authentic Hyderabadi Biryani at premium restaurants, and marvel at the world's largest one-man antique compilation inside the Salar Jung Museum. Our signature TRAGUIN Telangana Packages ensure magnificent stays and elite exclusive experiences during the best time to visit Telangana.",
        seo_title='TG-001 | HYDERABAD HIGHLIGHTS | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Telangana package (TG-001 / TRG-TEL-001): Hyderabad • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD & HUSSAIN SAGAR CRUISE', 1),
            _ih('Day 02: HISTORIC OLD CITY TOUR & GOLCONDA SOUND & LIGHT SHOW', 2),
            _ih('Day 03: FULL DAY EXCURSION TO RAMOJI FILM CITY', 3),
            _ih('Day 04: PALACE HERITAGE WALK & DEPARTURE', 4),
            _ih('TRAGUIN Signature Experience: Private, reserved seating coordination for the iconic Sound & Light', 5),
            _ih('Curated by TRAGUIN Experts: Smart, route-optimized itinerary designed to skip city congestion and', 6),
            _ih('Premium Handpicked Hotels: Accommodations chosen strictly based on high safety ratings, elite', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD & HUSSAIN SAGAR CRUISE',
                (
                    'WELCOME TO THE CITY OF NIZAMS – ROYAL RECEPTION & TWILIGHT CRUISE Your premium Telangana experience starts the moment you step off your plane or train. Your private chauffeur-driven luxury vehicle will receive your family and transition you smoothly to your handpicked'
                ),
                [
                    'Sightseeing Included: Birla Temple, Hussain Sagar Lake, Buddha Monolith Statue, NTR Gardens.',
                    'Evening Experience: Laser light fountain show followed by an elite dinner curated by TRAGUIN experts.',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel / Palace Resort)',
                    'Meals Included: Welcome Refreshment & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'HISTORIC OLD CITY TOUR & GOLCONDA SOUND & LIGHT SHOW',
                (
                    'LEGENDARY FORTS, RARE PEARLS & CHRONICLES OF TIME Indulge in a magnificent breakfast before diving deep into timeless history. Arrive at the majestic Charminar, the global icon of Hyderabad sightseeing. Walk through the grand four-tiered courtyards of the Chowmahalla Palace, getting a close view of the opulent lifestyle of the Nizams. After an afternoon exploring the ancient treasures of the Salar Jung Museum, journey to the magnificent Golconda Fort. Climb its historic stone paths to experience its miraculous acoustic engineering, followed by a VIP reserved seating experience for the legendary Sound and Light Show. bangles.'
                ),
                [
                    'Sightseeing Included: Charminar, Chowmahalla Palace, Salar Jung Museum, Laad Bazaar, Golconda Fort.',
                    'Optional Activities: Bespoke luxury shopping tour for genuine certified culture pearls and authentic lacquer',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel / Palace Resort)',
                    'Meals Included: Premium Breakfast & Traditional Nizami Specialty Dinner',
                ],
            ),
            _day(
                3,
                'FULL DAY EXCURSION TO RAMOJI FILM CITY',
                (
                    "THE MAGIC OF CINEMA – AN UNFORGETTABLE CELLULOID FANTASY An exciting morning awaits your family as you head out to the world's largest integrated film studio complex— Ramoji Film City. Travel past scenic outer ring highways to reach this immense wonderland. Enjoy a curated VIP entry that bypasses all standard queues. Travel across massive film sets, beautiful Japanese gardens, live action stunt shows, and grand thematic avenues. It's a marvelous day of family bonding and cinematic interactive experiences."
                ),
                [
                    'Sightseeing Included: Ramoji Studio Sets, Eureka Theme Plaza, Bird Park, Live Cinematic Shows.',
                    'Evening Experience: Carnival parade walk and an international buffet dining setup inside the studio park.',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel / Palace Resort)',
                    'Meals Included: Premium Breakfast & Multi-cuisine Buffet Dinner',
                ],
            ),
            _day(
                4,
                'PALACE HERITAGE WALK & DEPARTURE',
                (
                    'CHERISHING ROYAL EXPERIENCES BEYOND DESTINATIONS Savor a lazy, luxurious breakfast layout at your premium stay. Spend your final morning exploring the peaceful, architectural marvel of the Qutb Shahi Tombs, surrounded by green landscapes. Do any final souvenir shopping before your private chauffeur drives your family comfortably back to Hyderabad Airport or Secunderabad Station. Return home carrying beautiful family bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury point-to-point departure drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Park Hyderabad / Vivanta',
                'Hyderabad',
                '3N',
                'Deluxe',
                'Begumpet / similar',
                'Deluxe City View',
                4,
                1,
                description='OPTION 01 – DELUXE: The Park Hyderabad / Vivanta | Begumpet / similar | Deluxe City View',
            ),
            _hotel(
                'ITC Kakatiya / Hyatt Regency /',
                'Hyderabad',
                '3N',
                'Premium',
                'similar',
                'Premium',
                4,
                2,
                description='OPTION 02 – PREMIUM: ITC Kakatiya / Hyatt Regency / | similar | Premium',
            ),
            _hotel(
                'Taj Krishna / Park Hyatt',
                'Hyderabad',
                '3N',
                'Luxury',
                'Hyderabad',
                'Luxury Lake View',
                4,
                3,
                description='OPTION 03 – LUXURY: Taj Krishna / Park Hyatt | Hyderabad | Luxury Lake View',
            ),
            _hotel(
                'Taj Falaknuma Palace (The',
                'Hyderabad',
                '3N',
                'Ultra Luxury',
                'Ultimate Nizam Royalty)',
                'VVIP Royal Palace',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace (The | Ultimate Nizam Royalty) | VVIP Royal Palace',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights in high-end properties as selected.', 1),
            _inc_included('Luxury Transportation: Private Innova Crysta for all point-to-point transfers.', 2),
            _inc_included("Curated Meals: Lavish breakfast spreads and premium table d'hôte dinners.", 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local customer care executive presence.', 4),
            _inc_included('Welcome Amenities: Cold towels, luxury family travel kits, and mineral water.', 5),
            _inc_included('Complimentary Experience: Private twilight boat ride tickets at Hussain Sagar Lake.', 6),
            _inc_excluded('Airfare, domestic flights, or long-distance train tickets.', 7),
            _inc_excluded('Ramoji Film City entry tickets and inner park activity charges.', 8),
            _inc_excluded('Monument entry fees, camera fees, and local expert historical guide tips.', 9),
            _inc_excluded('Personal items such as laundry, long-distance phone calls, or mini-bar usage.', 10),
        ],
    )
    return package, itinerary

def build_tg_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-002'
    tour_code = 'TRG-TEL-002'
    title = 'HYDERABAD & RAMOJI MAGIC • HERITAGE & GRANDEUR EXPLORER'
    duration = '04 Nights / 05 Days'
    slug = 'tg-002-hyderabad-ramoji-magic-heritage-grandeur-explorer'
    itin_slug = 'tg-002-hyderabad-ramoji-magic-heritage-grandeur-explorer-itinerary'
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
            _ph('Serial code TG-002 | TRAGUIN tour code TRG-TEL-002', 1),
            _ph('State / Country: Telangana / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Hyderabad • Telangana', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury SUV / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family interaction and history briefing prior to your old city', 8),
            _ph('Curated by TRAGUIN Experts: Custom-tailored routes designed to bypass traffic hot spots, giving your', 9),
            _ph('Premium Handpicked Hotels: Properties meticulously chosen based on stringent elite comfort scores,', 10),
            _ph('Luxury Transportation: Courteous, well-uniformed, background-verified chauffeurs with superior local', 11)
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
        tagline='HYDERABAD & RAMOJI MAGIC',
        overview='HYDERABAD & RAMOJI MAGIC • HERITAGE & GRANDEUR EXPLORER TRAGUIN Premium Luxury Itinerary — TG-002 1 Welcome to a grand royal exploration meticulously crafted by TRAGUIN. Immerse your loved ones in the absolute Best Telangana Tour Package, designed to seamlessly unveil the legendary Nawabi culture, magnificent fortresses, and world-class cinematic marvels of Hyderabad. As your premier travel consultants, TRAGUIN elevates your journey into a true Luxury Telangana Holiday. From the historic minarets of Charminar to the enchanting silver screens of Ramoji Film City, enjoy premium stays, handpicked hotels, and immersive experiences that promise to create unforgettable memories for your entire family.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance of legendary Deccan history and spectacular modern amusement. Traveling in an exclusive premium AC vehicle with a professional chauffeur, your family will experience flawless door-to-door comfort. Featuring a rich daily meal plan filled with authentic Nizam culinary spreads and global breakfast buffets, this curated route is the definitive Premium Telangana Experience. Every step of your holiday includes the distinct TRAGUIN curated experience note, ensuring priority VVIP access tickets, expert storytelling, and around-the-clock specialized assistance.\n\nWHY CHOOSE THE BEST TELANGANA TOUR PACKAGE?\nWhen planning a Luxury Telangana Holiday, discerning family travelers look for a smooth combination of historical wisdom, recreational fun, and world-class hospitality. The capital city of Hyderabad stands out as an iconic attraction, rendering a Telangana Family Tour an absolute must-experience journey. From exploring iconic attractions like the acoustics-rich Golconda Fort to admiring the glittering collection inside Salar Jung Museum, Hyderabad sightseeing satisfies every generation. For couples and families seeking a magical getaway, a custom Telangana Honeymoon Package or family vacation opens doors to incredibly popular Instagram locations like the serene stepwells, the spectacular laser fountains at Hussain Sagar, and the sprawling movie sets of Ramoji. Indulge in exquisite pearl shopping at Laad Bazaar, sample world-renowned Hyderabadi Biryani, and explore vibrant street life. Our signature TRAGUIN Telangana Packages ensure your family relaxes in handpicked hotels with exclusive experiences during the best time to visit Telangana. TRAGUIN Premium Luxury Itinerary — TG-002 2',
        seo_title='TG-002 | HYDERABAD & RAMOJI MAGIC | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Telangana package (TG-002 / TRG-TEL-002): Hyderabad • Telangana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD & HUSSAIN SAGAR CRUISE', 1),
            _ih('Day 02: RAMOJI FILM CITY FULL-DAY EXCURSION', 2),
            _ih('Day 03: HERITAGE TOUR: GOLCONDA FORT & QUTUB SHAHI TOMBS', 3),
            _ih('Day 04: THE HEART OF OLD HYDERABAD & PALACE GLORY', 4),
            _ih('Day 05: BIRLA MANDIR VISTAS & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private family interaction and history briefing prior to your old city', 6),
            _ih('Curated by TRAGUIN Experts: Custom-tailored routes designed to bypass traffic hot spots, giving your', 7),
            _ih('Premium Handpicked Hotels: Properties meticulously chosen based on stringent elite comfort scores,', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD & HUSSAIN SAGAR CRUISE',
                (
                    'WELCOME TO THE CITY OF PEARLS – GLITTERING WATERS & NAWABI LIFESTYLE Your premium Telangana experience begins the moment you touch down at Rajiv Gandhi International Airport or arrive at Hyderabad Station. Your private luxury transport chauffeur welcomes you warmly and transfers your family to your handpicked premium hotel. After a smooth check-in and short rest, embark on a scenic evening drive to the gorgeous Hussain Sagar Lake. Step onto a private ferry to witness the monolithic Buddha Statue closely before watching the vibrant, musical laser show at NTR Gardens. appetizers.'
                ),
                [
                    'Sightseeing Included: Hussain Sagar Lake, Monolithic Buddha Statue, NTR Gardens Laser Show.',
                    'Evening Experience: Bespoke luxury lake-view dinner curated by TRAGUIN experts featuring traditional',
                    'Overnight Stay: Hyderabad (Premium / Luxury Hotel)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'RAMOJI FILM CITY FULL-DAY EXCURSION',
                (
                    "A MAGICAL JOURNEY THROUGH THE WORLD'S LARGEST CINEMATIC PARADISE Indulge in an early premium breakfast as we head out for a full-day magical experience at the world- famous Ramoji Film City. Spanning over 2,000 acres, this spectacular wonderland offers breathtaking landscapes, custom movie sets, live stunt shows, and magnificent Japanese gardens. Travel inside the park with a specialized vintage tour bus under our premium privileges, exploring the iconic Bahubali set and grand mythological palaces. It is an unmatched destination to capture unforgettable memories and iconic family photographs."
                ),
                [
                    'Sightseeing Included: Full Guided Tour of Ramoji Film City, Studio Sets, Eureka Stunt Shows, Bahubali Set.',
                    'Optional Activities: Premium upgrades to Ramoji Star Experience featuring buffet lunch and express',
                    'Overnight Stay: Hyderabad (Premium / Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Luxury Dinner',
                ],
            ),
            _day(
                3,
                'HERITAGE TOUR: GOLCONDA FORT & QUTUB SHAHI TOMBS',
                (
                    'ECHOING ACOUSTICS, MAJESTIC FORTRESSES & ROYAL LEGENDS Today, travel back in time as your luxury transport heads toward the grand Golconda Fort. Marvel at the world-renowned acoustic engineering where a single clap at the entrance gate echoes explicitly up to the mountain citadel. Your expert guide will share emotional stories of hidden diamond vaults and royal court intrigues. Conclude your afternoon by visiting the highly regal Qutub Shahi Tombs, a magnificent architectural blend of Persian and Hindu styles. stars.'
                ),
                [
                    'Sightseeing Included: Golconda Fort, Sound & Light Show, Qutub Shahi Tombs, Ibrahim Bagh.',
                    'Evening Experience: VIP seating at the spectacular Golconda Sound & Light Show narrated by Bollywood',
                    'Overnight Stay: Hyderabad (Premium / Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Royal Deccani Dinner',
                ],
            ),
            _day(
                4,
                'THE HEART OF OLD HYDERABAD & PALACE GLORY',
                (
                    'THE CHARMINAR MAJESTY, SALAR JUNG MUSEUM & CHOWMAHALLA PALACE Awake for a delightful morning breakfast and drive to the world-famous symbol of Hyderabad—the iconic Charminar. Walk past the busy, historical lanes of Laad Bazaar, renowned globally for shimmering lacquer pearls and bridal bangles. Next, step into the spectacular Chowmahalla Palace, the official seat of the Nizams, featuring grand durbar halls and vintage Rolls Royce collections. Spend your late afternoon browsing through the incredible single-man antiquities collection at the Salar Jung Museum.'
                ),
                [
                    'Sightseeing Included: Charminar, Chowmahalla Palace, Salar Jung Museum, Mecca Masjid, Laad Bazaar.',
                    'Shopping: Point: Guided heritage pearl shopping experience with certified elite vendors.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Authentic Hyderabadi Biryani Farewell Dinner',
                ],
            ),
            _day(
                5,
                'BIRLA MANDIR VISTAS & DEPARTURE',
                (
                    'SPIRITUAL CALM, PANORAMIC CITYVIEWS & FAREWELL On the final morning of your premium Telangana experience, ascend the high hill of Naubath Pahad to visit the serene Birla Mandir. Built entirely out of 2,000 tons of pure white Rajasthani marble, this architectural marvel offers breathtaking panoramic landscapes of the entire twin cities. Return to your hotel for a final lavish meal. Your private vehicle will transfer you safely to Hyderabad Airport or Railway Station, returning you home with beautiful family bonds and unforgettable memories designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door airport or railway station drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Premier /',
                'Hyderabad',
                '4N',
                'Deluxe',
                'Mercure KCP / similar',
                'Executive Deluxe',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Premier / | Mercure KCP / similar | Executive Deluxe',
            ),
            _hotel(
                'Radisson Blu Plaza / Novotel',
                'Hyderabad',
                '4N',
                'Premium',
                'Hitec City',
                'Premium Club RoomMAPAI (Breakfast &',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Blu Plaza / Novotel | Hitec City | Premium Club RoomMAPAI (Breakfast &',
            ),
            _hotel(
                'ITC Kohenur / Taj Krishna /',
                'Hyderabad',
                '4N',
                'Luxury',
                'Park Hyatt',
                'Luxury Skyline View',
                4,
                3,
                description='OPTION 03 – LUXURY: ITC Kohenur / Taj Krishna / | Park Hyatt | Luxury Skyline View',
            ),
            _hotel(
                'Taj Falaknuma Palace (The',
                'Hyderabad',
                '4N',
                'Ultra Luxury',
                'Mirror of Sky)',
                'VVIP Royal Nizam',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace (The | Mirror of Sky) | VVIP Royal Nizam',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights accommodation in handpicked top-rated hotels.', 1),
            _inc_included('Luxury Transportation: Private dedicated AC SUV for all transfers and sightseeing.', 2),
            _inc_included('Curated Meal Plan: Lavish daily breakfast and customized family dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Personalized arrival welcome drink kit and Deccani sweets.', 5),
            _inc_included('Complimentary Experience: Private family boat ride tickets at Hussain Sagar Lake.', 6),
            _inc_excluded('Airfare, flight tickets, or long-distance interstate train travel.', 7),
            _inc_excluded('Ramoji Film City entry tickets (available as a premium add-on).', 8),
            _inc_excluded('Monument entrance fees, local guide fees, and camera permits.', 9),
            _inc_excluded('Personal expenses such as laundry, phone bills, or tips.', 10),
        ],
    )
    return package, itinerary

def build_tg_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-003'
    tour_code = 'TRG-TEL-003'
    title = 'NIZAM HERITAGE TOUR • ECHOES OF ROYALTY & OPULENCE'
    duration = '03 Nights / 04 Days'
    slug = 'tg-003-nizam-heritage-tour-echoes-of-royalty-opulence'
    itin_slug = 'tg-003-nizam-heritage-tour-echoes-of-royalty-opulence-itinerary'
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
            _ph('Serial code TG-003 | TRAGUIN tour code TRG-TEL-003', 1),
            _ph('State / Country: Telangana / India | Category: Nizam Heritage Tour', 2),
            _ph('Destinations: Hyderabad •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Private Sedan / MAPAI (Breakfast & Gourmet Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private family heritage storyteller walkthrough inside Chowmahalla', 8),
            _ph('Curated by TRAGUIN Experts: Custom routing tailored specifically to bypass urban metropolitan traffic.', 9),
            _ph('Premium Handpicked Hotels: Properties chosen specifically for historical character, modern luxury, and', 10),
            _ph('Luxury Transportation: Safe, uniformly dressed, background-verified elite local chauffeurs.', 11)
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
        tagline='NIZAM HERITAGE TOUR',
        overview="NIZAM HERITAGE TOUR • ECHOES OF ROYALTY & OPULENCE Welcome to an unforgettable journey back in time, curated exclusively by TRAGUIN. Step into a world of pure royalty, timeless elegance, and legendary hospitality with our ultimate Telangana Heritage Tour. Crafted as the definitive Best Telangana Tour Package, this itinerary unfolds the magical chapter of the TRAGUIN Premium Luxury Itinerary — TG-003 1 Nizams of Hyderabad. As your premier luxury travel consultants, TRAGUIN transforms your stay into an imperial escape, combining breathtaking landscapes of old fortifications with premium stays in handpicked hotels. Let the poetic charm, grand structures, and culinary legacies of Telangana form unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday package offers an exquisite balance between legendary ancient architecture, world-renowned cinematic attractions, and modern sophisticated comforts. Traveling in a fully dedicated premium AC vehicle with professional chauffeur assistance, your family or group will enjoy absolute privacy and elite care. With a meticulously planned route and an exceptional meal plan offering rich breakfasts and specialized royal dinners, this package promises a flawless Premium Telangana Experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, ensuring fast-track entry privileges, local historical insight, and 24/7 personalized concierge support.\n\nWHY CHOOSE THE BEST TELANGANA TOUR PACKAGE?\nWhen considering a Luxury Telangana Holiday, discerning global travelers seek an elite immersion into royal culture, artisanal shopping, and unparalleled architectural grandeur. Telangana's capital city, Hyderabad, is a treasure trove of iconic attractions. From the staggering heights of the historic Golconda Fort to the majestic frames of Charminar, Telangana sightseeing offers an unmatched visual storytelling experience. For couples planning a romantic Telangana Honeymoon Package or families booking a Telangana Family Tour, the region offers incredibly popular Instagram locations such as the mirror rooms of Chowmahalla Palace, the scenic beauty of Hussain Sagar Lake at twilight, and the massive fantasy sets of Ramoji Film City. Whether you are exploring top tourist places in Telangana, indulging in authentic world-famous Hyderabadi Biryani, or shopping for precious Nizami pearls, our signature TRAGUIN Telangana Packages ensure your journey aligns perfectly with the best time to visit Telangana.",
        seo_title='TG-003 | NIZAM HERITAGE TOUR | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Telangana package (TG-003 / TRG-TEL-003): Hyderabad • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD', 1),
            _ih('Day 02: EPIC NIZAM HERITAGE SIGHTSEEING', 2),
            _ih('Day 03: GOLCONDA FORT CHRONICLES & QUTB SHAHI TOMBS', 3),
            _ih('Day 04: DEPARTURE VIA CHOWMAHALLA REVERIE', 4),
            _ih('TRAGUIN Signature Experience: Private family heritage storyteller walkthrough inside Chowmahalla', 5),
            _ih('Curated by TRAGUIN Experts: Custom routing tailored specifically to bypass urban metropolitan traffic.', 6),
            _ih('Premium Handpicked Hotels: Properties chosen specifically for historical character, modern luxury, and', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD',
                (
                    'WELCOME TO THE CITY OF PEARLS – LAND OF THE NIZAMS Your premium Telangana experience begins the moment you touch down at Rajiv Gandhi International Airport or arrive at the station. A private luxury chauffeur-driven vehicle welcomes and escorts you to your handpicked premium luxury hotel. After a smooth check-in and refreshing break, step out in the late afternoon to experience the serene scenic beauty of Hussain Sagar Lake. Indulge in an exclusive private boat cruise to the monolithic Buddha Statue followed by a leisurely stroll through the beautifully illuminated NTR Gardens.'
                ),
                [
                    'Sightseeing Included: Hussain Sagar Lake, Monolithic Buddha Statue, NTR Gardens.',
                    'Evening Experience: Welcome high-tea session followed by a curated elite briefing from TRAGUIN experts.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Selected Property)',
                    'Meals Included: Welcome Mocktail & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'EPIC NIZAM HERITAGE SIGHTSEEING',
                (
                    'ROYAL PALACES, REPLENDENT ARCHITECTURE & OLD CITY SECRETS Awake to a lavish breakfast before diving deep into timeless imperial legends. First, visit the magnificent Chowmahalla Palace, the official seat of the Asaf Jahi dynasty, to marvel at grand crystal chandeliers and vintage royal car collections. Next, stand before the iconic Charminar, an architectural masterpiece of the Qutb Shahi era. Explore the bustling markets of Laad Bazar, famous for its glittering lacquer bangles, before heading to the massive Salar Jung Museum to witness one of the largest private art collections in the world.'
                ),
                [
                    'Sightseeing Included: Chowmahalla Palace, Charminar, Mecca Masjid, Laad Bazar, Salar Jung Museum.',
                    'Optional Activities: Private guided pearl valuation tour with a master jeweler in Pathergatti.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Selected Property)',
                    'Meals Included: Premium Breakfast & Traditional Royal Nizami Dinner',
                ],
            ),
            _day(
                3,
                'GOLCONDA FORT CHRONICLES & QUTB SHAHI TOMBS',
                (
                    'DIAMOND LEGENDS & A MAGICAL EVENING OF LIGHTS Following a rich morning breakfast, drive to the world-famous Golconda Fort, an architectural marvel known for its acoustic diamond-trading chambers and robust engineering. Walk through the historic gates where the Koh-i-Noor diamond was once stored. Nearby, explore the grand, serene domes of the Qutb Shahi Tombs, surrounded by landscaped gardens. In the evening, witness the breathtaking Sound and Light Show inside Golconda Fort, narrated by cinematic legends.'
                ),
                [
                    'Sightseeing Included: Golconda Fort acoustic tour, Qutb Shahi Heritage Park Tombs.',
                    'Evening Experience: VIP reserved seating at the Golconda Sound & Light Multimedia Show.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Selected Property)',
                    'Meals Included: Premium Breakfast & Multi-Cuisine Luxury Dinner',
                ],
            ),
            _day(
                4,
                'DEPARTURE VIA CHOWMAHALLA REVERIE',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Savor your final luxury breakfast at the hotel restaurant. If your flight timings permit, enjoy a relaxed morning visit to the peaceful Birla Mandir, built of pure white Rajasthani marble on an elevated hillock overlooking the cityscape. Your private luxury transport will then guide you seamlessly back to Rajiv Gandhi International Airport or the rail terminal for your onward flight. Return home carrying unforgettable memories and royal stories beautifully tailored by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door departure drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Golkonda Hotel / Mercure KCP',
                'Telangana',
                '3N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: The Golkonda Hotel / Mercure KCP',
            ),
            _hotel(
                'Vivanta Hyderabad Begumpet / Hyatt Regency Premium Club Balcony Room MAPAI (Breakfast & Dinner)',
                'Telangana',
                '3N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Vivanta Hyderabad Begumpet / Hyatt Regency Premium Club Balcony Room MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'ITC Kakatiya / Taj Krishna / Park Hyatt Luxury Heritage View Suite Elite MAPAI Plan',
                'Telangana',
                '3N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: ITC Kakatiya / Taj Krishna / Park Hyatt Luxury Heritage View Suite Elite MAPAI Plan',
            ),
            _hotel(
                'Taj Falaknuma Palace (The Palace in the Sky) Royal Nizam Presidential Suite Bespoke Royal Dining Plan',
                'Telangana',
                '3N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace (The Palace in the Sky) Royal Nizam Presidential Suite Bespoke Royal Dining Pla',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights in top luxury handpicked hotels.', 1),
            _inc_included('Luxury Transportation: Private dedicated AC Sedan for transfers & sightseeing.', 2),
            _inc_included('Curated Meals: Daily extensive buffet breakfasts and royal dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-ground guest experience manager.', 4),
            _inc_included('Welcome Amenities: Royal custom travel kit, traditional sweets & refreshments.', 5),
            _inc_included('Complimentary Experience: Reserved tickets to Hussain Sagar boat cruise.', 6),
            _inc_excluded('Airfare, domestic flights, or inter-state train booking.', 7),
            _inc_excluded('Monument entry tickets, camera permissions, or local guiding fees.', 8),
            _inc_excluded('Personal items such as laundry, phone calls, drinks, or tips.', 9),
            _inc_excluded('Optional culinary walks, shopping excursions or extended tours.', 10),
        ],
    )
    return package, itinerary

def build_tg_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-004'
    tour_code = 'TRG-TEL-004'
    title = 'HYDERABAD WEEKEND • THE ROYAL LEGACY OF NIZAMS'
    duration = '02 Nights / 03 Days'
    slug = 'tg-004-hyderabad-weekend-the-royal-legacy-of-nizams'
    itin_slug = 'tg-004-hyderabad-weekend-the-royal-legacy-of-nizams-itinerary'
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
            _ph('Serial code TG-004 | TRAGUIN tour code TRG-TEL-004', 1),
            _ph('State / Country: Telangana / India | Category: Premium Family Weekend Escape', 2),
            _ph('Destinations: Hyderabad •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury AC Innova Crysta / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private architectural walk and acoustic demonstration booking at', 8),
            _ph('Curated by TRAGUIN Experts: Perfect layout mapping maximizing weekend times to completely avoid', 9),
            _ph('Premium Handpicked Hotels: Elite properties selected for their unparalleled hospitality ratings, safety', 10),
            _ph('Luxury Transportation: Travel via immaculate, professional, and chauffeur-driven premium multi-purpose', 11)
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
        tagline='HYDERABAD WEEKEND',
        overview="HYDERABAD WEEKEND • THE ROYAL LEGACY OF NIZAMS TRAGUIN Premium Luxury Itinerary — TG-004 1 Welcome to an extraordinary escape through the land of royal heritage and modern marvels, meticulously structured by TRAGUIN. Embark on the finest Hyderabad Family Tour, custom-tailored to reveal the breathtaking landscapes, ancient fortifications, and mouth-watering culinary treasures of Telangana. As your expert travel consultants, TRAGUIN transforms this weekend getaway into a lavish luxury holiday featuring premium stays, immersive experiences, and seamlessly managed transportation. From the historic whispering walls of Golconda to the magical sets of Ramoji Film City, every detail is refined to create unforgettable memories for you and your loved ones.\n\nTOUR OVERVIEW\nThis bespoke weekend getaway is specifically crafted for families looking to discover the cultural grandiosity and modern entertainment wonders of Telangana over a premium weekend layout. Traveling in absolute comfort within a dedicated private luxury AC vehicle accompanied by a top-tier tourist chauffeur, your family will explore effortlessly. With a detailed meal plan offering opulent morning spreads and personalized evening culinary feasts, this route defines the ultimate premium Hyderabad experience. Every phase of your trip carries the signature touch of TRAGUIN curated experiences, including reserved VIP entries, guided historical narratives, and specialized concierge oversight.\n\nWHY CHOOSE THE BEST HYDERABAD TOUR PACKAGE?\nWhen exploring options for a Luxury Hyderabad Holiday, travelers demand a perfect synthesis of timeless history and elite contemporary conveniences. Hyderabad delivers exactly that. Home to iconic attractions such as the centuries-old Charminar, the breathtaking Chowmahalla Palace, and the spectacular acoustics of Golconda Fort, Hyderabad sightseeing presents an unforgettable journey through time. For couples arranging an elegant Hyderabad Honeymoon Package or families looking for a comprehensive Hyderabad Family Tour, the city offers some of India's most popular Instagram locations—including the tranquil waters of Hussain Sagar Lake featuring its colossal Buddha statue and the vibrant bazaar energy of Laad Bazar. From handicraft pearl shopping to relishing the world-famous Hyderabadi Biryani at elite establishments, our custom-crafted TRAGUIN Telangana Packages bring together handpicked hotels and exclusive experiences to match the best time to visit Hyderabad seamlessly.",
        seo_title='TG-004 | HYDERABAD WEEKEND | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Telangana package (TG-004 / TRG-TEL-004): Hyderabad • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD & HERITAGE EXPLORATION', 1),
            _ih('Day 02: RAMOJI FILM CITY FULL-DAY EXCURSION', 2),
            _ih('Day 03: GOLCONDA ACOUSTICS & DEPARTURE', 3),
            _ih('TRAGUIN Signature Experience: Private architectural walk and acoustic demonstration booking at', 4),
            _ih('Curated by TRAGUIN Experts: Perfect layout mapping maximizing weekend times to completely avoid', 5),
            _ih('Premium Handpicked Hotels: Elite properties selected for their unparalleled hospitality ratings, safety', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD & HERITAGE EXPLORATION',
                (
                    'WELCOME TO THE CITY OF PEARLS – CHRONICLES OF THE NIZAMS Your premium Telangana experience commences the moment you arrive at Rajiv Gandhi International Airport or Hyderabad Station. Your dedicated chauffeur greeted private luxury transport vehicle stands ready to'
                ),
                [
                    'Sightseeing Included: Charminar, Chowmahalla Palace, Hussain Sagar Lake Private Cruise, NTR Gardens.',
                    'Evening Experience: Laser light show at Lumbini Park followed by a royal Nizami dinner curated by TRAGUIN',
                    'Overnight Stay: Hyderabad (Premium / Luxury Selected Hotel)',
                    'Meals Included: Welcome Drink & Fine-dining Nizami Dinner',
                ],
            ),
            _day(
                2,
                'RAMOJI FILM CITY FULL-DAY EXCURSION',
                (
                    "AN IMMERSIVE CINEMATIC JOURNEY & SPECTACULAR ENTERTAINMENT Indulge in a glorious lavish breakfast before departing for a full-day excursion to the legendary Ramoji Film City—certified as the world's largest integrated film studio complex. Travelling in your premium private vehicle, you will receive VIP entry into this massive world of cinematic illusions. Explore iconic movie sets (including the grand Baahubali set), stroll through beautifully manicured Japanese gardens, enjoy live stunt shows, and snap photos across high-profile Instagram locations scattered throughout the park."
                ),
                [
                    'Sightseeing Included: Full Guided Studio Tour, Baahubali Set Entry, Live Eco-Zone Walks, Cinematic Shows.',
                    'Optional Activities: Upgrade to a customized Ramoji Star Experience with private AC coach transits inside.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Selected Hotel)',
                    'Meals Included: Premium Breakfast & Luxury Resort Dinner',
                ],
            ),
            _day(
                3,
                'GOLCONDA ACOUSTICS & DEPARTURE',
                (
                    'LEGENDARY FORTRESS WHISPERS & ELITE PEARL SHOPPING Savor a delightful morning breakfast and check out from your premium stay. Head over to the historic Golconda Fort, an architectural marvel renowned for its brilliant diamond heritage and unmatched acoustic system. Clapping at the entry dome can be clearly heard at the highest hilltop pavilion. Walk through the beautifully preserved Qutb Shahi Tombs situated nearby. Conclude your weekend tour with exclusive drops you off at the airport or railway station. Permitting).'
                ),
                [
                    'shopping: for authentic Hyderabadi pearls and hand-woven traditional textiles before your private vehicle safely',
                    'Sightseeing Included: Golconda Fort (Acoustic Tour), Qutb Shahi Tombs Complex, Salar Jung Museum (Time',
                    'Transfers Included: Private door-to-door luxury transit drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'The Golkonda Hotel / Lemon Tree',
                'Hyderabad',
                '2N',
                'Deluxe',
                'Premier / similar',
                'Executive Deluxe',
                4,
                1,
                description='OPTION 01 – DELUXE: The Golkonda Hotel / Lemon Tree | Premier / similar | Executive Deluxe',
            ),
            _hotel(
                'Vivanta Hyderabad Begumpet /',
                'Hyderabad',
                '2N',
                'Premium',
                'ITC Kohenur / similar',
                'Premium Club',
                4,
                2,
                description='OPTION 02 – PREMIUM: Vivanta Hyderabad Begumpet / | ITC Kohenur / similar | Premium Club',
            ),
            _hotel(
                'The Westin Mindspace / Taj',
                'Hyderabad',
                '2N',
                'Luxury',
                'Krishna / Park Hyatt',
                'Luxury City View',
                4,
                3,
                description='OPTION 03 – LUXURY: The Westin Mindspace / Taj | Krishna / Park Hyatt | Luxury City View',
            ),
            _hotel(
                'Taj Falaknuma Palace (The',
                'Hyderabad',
                '2N',
                'Ultra Luxury',
                'Ultimate Nizam Living)',
                'VVIP Palace Royal',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace (The | Ultimate Nizam Living) | VVIP Palace Royal',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 02 Nights accommodation in handpicked, top-rated hotels.', 1),
            _inc_included('Luxury Transportation: All sightseeing & transfers via private Innova Crysta.', 2),
            _inc_included('Curated Meals: Daily extensive buffet breakfasts and custom dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local guest experience manager assistance.', 4),
            _inc_included('Welcome Amenities: Customized luxury welcome drinks and refreshing travel kit.', 5),
            _inc_included('Complimentary Experience: Private family sunset boat tickets at Hussain Sagar.', 6),
            _inc_excluded('Airfare, domestic flight charges, or inbound train ticketing.', 7),
            _inc_excluded('Ramoji Film City entry tickets (can be pre- booked via TRAGUIN).', 8),
            _inc_excluded('Monument entry fees, specialized guide hiring charges, camera permits.', 9),
            _inc_excluded('Personal items, laundry expenses, alcoholic drinks, and gratuities.', 10),
        ],
    )
    return package, itinerary

def build_tg_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-005'
    tour_code = 'TRG-TEL-005'
    title = 'HYDERABAD ROMANCE • TIMELESS HERITAGE & MODERN OPULENCE'
    duration = '03 Nights / 04 Days'
    slug = 'tg-005-hyderabad-romance-timeless-heritage-modern-opulence'
    itin_slug = 'tg-005-hyderabad-romance-timeless-heritage-modern-opulence-itinerary'
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
            _ph('Serial code TG-005 | TRAGUIN tour code TRG-TEL-005', 1),
            _ph('State / Country: Telangana / India | Category: Honeymoon Package', 2),
            _ph('Destinations: Hyderabad • Telangana', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Sedan / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private palace-vibe photographic mapping briefing before exploring', 8),
            _ph('Curated by TRAGUIN Experts: Smooth scheduling that balances busy cultural walks with relaxing couple', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen strictly based on world-class safety, stellar', 10),
            _ph('Luxury Transportation: Background-verified, professional chauffeurs intimately familiar with optimal city', 11)
        ],
        moods=['Luxury', 'Honeymoon', 'Culture'],
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
        tagline='HYDERABAD ROMANCE',
        overview='HYDERABAD ROMANCE • TIMELESS HERITAGE & MODERN OPULENCE TRAGUIN Premium Luxury Itinerary — TG-005 1 Welcome to an ethereal romantic escape woven by TRAGUIN. Embark on the ultimate Hyderabad Honeymoon Package, meticulously crafted to immerse you and your partner in the spectacular legacy and royal grandeur of the City of Nizams. As your trusted premium travel consultants, TRAGUIN transforms your romantic getaway into a seamless luxury holiday filled with handpicked hotels, breathtaking landscapes, and exclusive culinary journeys. From the majestic heights of ancient forts to the modern marvels of entertainment, every element is designed to curate unforgettable memories for a lifetime.\n\nTOUR OVERVIEW\nThis premium travel itinerary offers an unmatched romantic narrative across Telangana, showcasing its rich cultural tapestry and modern luxury. Travelling in a dedicated private luxury transport vehicle driven by an elite chauffeur, you will move seamlessly between historic royal palaces, peaceful lakes, and sprawling film studios. Enjoy a tailored meal plan featuring lavish daily breakfasts and specialized candle-lit culinary spreads. With our signature TRAGUIN curated experience note, enjoy VIP check-ins, skip-the-line privileges, and around- the-clock bespoke support designed for the ultimate honeymoon journey.\n\nWHY CHOOSE THE BEST HYDERABAD TOUR PACKAGE?\nWhen considering a Luxury Telangana Holiday, discerning couples seek a perfect blend of old-world charm, imperial luxury, and vibrant urban culture. Hyderabad stands out as an iconic hub of romance, rendering a Hyderabad Honeymoon Package the ultimate choice for newlyweds. From the internationally celebrated Charminar to the acoustic brilliance of Golconda Fort—top tourist places in Telangana—the city offers fascinating storytelling at every turn. For couples looking to create an elegant travel diary, this Telangana Family Tour and couple layout incorporates highly popular Instagram locations like the majestic Falaknuma Palace step-vistas, the glittering Hussain Sagar Lake during golden hour, and the breathtaking sets of Ramoji Film City. Indulge in premium pearl shopping at Laad Bazaar, sample authentic world-famous Hyderabadi Biryani, and witness magnificent laser showcases. Our bespoke TRAGUIN Telangana Packages seamlessly blend romantic comfort with premium stays, guaranteeing the absolute best time to visit Telangana.',
        seo_title='TG-005 | HYDERABAD ROMANCE | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Telangana package (TG-005 / TRG-TEL-005): Hyderabad • Telangana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD & HUSSAIN SAGAR CRUISE', 1),
            _ih('Day 02: HISTORIC CHARMINAR & FORTRESS ACOUSTICS', 2),
            _ih('Day 03: RAMOJI FILM CITY FULL-DAY EXCURSION', 3),
            _ih('Day 04: SALAR JUNG MUSEUM & DEPARTURE', 4),
            _ih('TRAGUIN Signature Experience: Private palace-vibe photographic mapping briefing before exploring', 5),
            _ih('Curated by TRAGUIN Experts: Smooth scheduling that balances busy cultural walks with relaxing couple', 6),
            _ih('Premium Handpicked Hotels: Accommodations chosen strictly based on world-class safety, stellar', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD & HUSSAIN SAGAR CRUISE',
                (
                    'WELCOME TO THE CITY OF NIZAMS – ROYAL RECEPTION & LAKESIDE GLOW Your premium Telangana experience begins as you land at Rajiv Gandhi International Airport or arrive at Hyderabad station. A dedicated private luxury transport vehicle greets you for a seamless transfer to your handpicked premium luxury hotel. After a refreshing afternoon, step out for an exclusive evening experience at'
                ),
                [
                    'Sightseeing Included: Hussain Sagar Lake, Buddha Statue Promenade, Necklace Road.',
                    'Evening Experience: Romantic sunset speedboat ride with personal refreshments, followed by an intimate',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel / Palace Option)',
                    'Meals Included: Welcome Drink & Gourmet Dinner',
                ],
            ),
            _day(
                2,
                'HISTORIC CHARMINAR & FORTRESS ACOUSTICS',
                (
                    'ECHOES OF THE PAST – CHARMINAR, LAAD BAZAAR & GOLCONDA SOUND SHOW Awake to a lavish buffet breakfast and begin your guided Hyderabad sightseeing journey. Explore the legendary Charminar, an architectural masterpiece standing tall as the symbol of the city. Walk through the bustling lanes of Laad Bazaar, world-renowned for its brilliant, shimmering lacquer bangles and pearls. In the afternoon, visit the grand Qutb Shahi Tombs before heading to the mighty Golconda Fort. Walk hand-in-hand through its monumental gates and experience its fascinating acoustic engineering before sitting down for the glorious illuminated Sound & Light show.'
                ),
                [
                    'Sightseeing Included: Charminar, Mecca Masjid, Laad Bazaar, Qutb Shahi Tombs, Golconda Fort.',
                    'Optional Activities: Bespoke luxury pearl shopping tour guided by a local gem expert.',
                    'Evening Experience: VIP entry seating at the Golconda Fort Sound & Light historical presentation.',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Authentic Nizam Thali Dinner',
                ],
            ),
            _day(
                3,
                'RAMOJI FILM CITY FULL-DAY EXCURSION',
                (
                    "A CINEMATIC ROMANCE – MAGICAL SETS & LIVE SHOWS Indulge in an early gourmet breakfast before driving to the world's largest integrated film studio complex— Ramoji Film City. This spectacular entertainment oasis provides a thrilling backdrop for couples, filled with manicured gardens, replicas of global wonders, and grand cinematic streets. Journey through the majestic movie sets of blockbusters, enjoy high-energy live stunt performances, and find stunning photography points across its wide fountains and themed avenues."
                ),
                [
                    'Sightseeing Included: Ramoji Film City Studio Tour, Bahubali Set, Mughal Gardens, Askari Garden, Movie Magic.',
                    'Evening Experience: Honeymoon Special: A private, curated candle-lit dinner with a custom celebratory cake',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Romantic Candle-lit Dinner',
                ],
            ),
            _day(
                4,
                'SALAR JUNG MUSEUM & DEPARTURE',
                (
                    'ROYAL TREASURES & UNFORGETTABLE FAREWELL Conclude your premium Telangana experience with a grand final breakfast. Check out and visit the legendary Salar Jung Museum, housing one of the largest private antique collections in the world, including the famous Veiled Rebecca statue. After a quick stop for souvenirs and premium local bakeries, your private luxury transport transfers you safely to Hyderabad Airport or Railway Station. Return home carrying beautiful bonds and unforgettable memories meticulously designed by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private luxury door-to-door station or airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Lemon Tree Premier / Mercure KCP',
                'Hyderabad',
                '3N',
                'Deluxe',
                '/ similar',
                'Deluxe King RoomMAPAI (Breakfast &',
                4,
                1,
                description='OPTION 01 – DELUXE: Lemon Tree Premier / Mercure KCP | / similar | Deluxe King RoomMAPAI (Breakfast &',
            ),
            _hotel(
                'Radisson Blu Plaza / Novotel',
                'Hyderabad',
                '3N',
                'Premium',
                'Airport / Hyatt Regency',
                'Premium Executive',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Blu Plaza / Novotel | Airport / Hyatt Regency | Premium Executive',
            ),
            _hotel(
                'ITC Kohenur / Taj Krishna / Park',
                'Hyderabad',
                '3N',
                'Luxury',
                'Hyatt',
                'Luxury Lake View',
                4,
                3,
                description='OPTION 03 – LUXURY: ITC Kohenur / Taj Krishna / Park | Hyatt | Luxury Lake View',
            ),
            _hotel(
                'Taj Falaknuma Palace (The Grand',
                'Hyderabad',
                '3N',
                'Ultra Luxury',
                'Royal Residence)',
                'VVIP Royal Palace',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace (The Grand | Royal Residence) | VVIP Royal Palace',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights accommodation in handpicked, top-rated romantic luxury properties.', 1),
            _inc_included('Luxury Transportation: Private dedicated AC Sedan for all airport runs and sightseeing.', 2),
            _inc_included('Curated Meal Plan: Daily premium breakfast spreads and gourmet dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated travel concierge and guest relations manager.', 4),
            _inc_included('Welcome Amenities: Personalized honeymoon travel welcome pack and refreshing beverages.', 5),
            _inc_included('Complimentary Experience: Reserved private speedboat tour tickets at Hussain Sagar Lake.', 6),
            _inc_excluded('Airfare, domestic flight charges, or long-distance train tickets.', 7),
            _inc_excluded('Entry tickets to monuments, Ramoji Film City passes, and camera fees.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, alcoholic drinks, or tips.', 9),
            _inc_excluded('Any optional excursions, activities, or extensions not explicitly outlined.', 10),
        ],
    )
    return package, itinerary

def build_tg_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-006'
    tour_code = 'TRG-TEL-006'
    title = 'LUXURY HYDERABAD ESCAPE • THE NIZAMI HERITAGE OPULENCE'
    duration = '04 Nights / 05 Days'
    slug = 'tg-006-luxury-hyderabad-escape-the-nizami-heritage-opulence'
    itin_slug = 'tg-006-luxury-hyderabad-escape-the-nizami-heritage-opulence-itinerary'
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
            _ph('Serial code TG-006 | TRAGUIN tour code TRG-TEL-006', 1),
            _ph('State / Country: Telangana / India | Category: Luxury Holiday Escape', 2),
            _ph('Destinations: Hyderabad •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Chauffeur-Driven Luxury SUV / MAPAI Plan', 7),
            _ph('TRAGUIN Signature Experience: Elite, skip-the-line access to Chowmahalla Palace with a specialized', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked scheduling to tour the Old City during optimal morning', 9),
            _ph('Premium Handpicked Hotels: Accommodations evaluated meticulously based on luxury parameters,', 10),
            _ph('Luxury Transportation: Private executive vehicle fleets ensuring immaculate cleaning and professional', 11)
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
        tagline='LUXURY HYDERABAD ESCAPE',
        overview='LUXURY HYDERABAD ESCAPE • THE NIZAMI HERITAGE OPULENCE Welcome to an extraordinary immersion into royal history, timeless heritage, and modern sophistication curated exclusively by TRAGUIN. Embark on the definitive Telangana Family Tour and romantic escape, TRAGUIN Premium Luxury Itinerary — TG-006 1 engineered to reveal the breathtaking landscapes, ancient fortifications, and legendary culinary arts of Hyderabad. As your premier travel consultants, TRAGUIN transforms your vacation into a seamless luxury holiday filled with handpicked hotels, palatial hospitality, and curated exclusive experiences. Let the scenic beauty of historical lakes and majestic monuments forge unforgettable memories for your family.\n\nTOUR OVERVIEW\nThis custom-tailored luxury holiday itinerary provides a pristine balance between iconic attractions, ancient dynastic heritage, and contemporary lifestyle spaces in Telangana. Traveling in a dedicated premium air- conditioned vehicle with highly trained chauffeur assistance, your party will enjoy absolute privacy and comfort. With a carefully structured meal plan highlighting exquisite breakfasts and high-end specialized dinners, this curated route represents the finest premium Telangana experience. Every step of your journey includes the signature touch of TRAGUIN curated experiences, providing skip-the-line privileges, local storytelling insight, and around-the-clock elite support.\n\nWHY CHOOSE THE BEST TELANGANA TOUR PACKAGE?\nWhen planning a Luxury Telangana Holiday, discerning globetrotters seek more than just basic sightseeing; they pursue an immersive dive into royal traditions and culinary perfection. Hyderabad stands out as an incomparable destination, making a Telangana Honeymoon Package or Telangana Family Tour the ideal choice for travelers. From exploring iconic attractions like the timeless Charminar and Chowmahalla Palace to uncovering the grand stone ramparts of Golconda Fort, Telangana sightseeing is a revelation. For families and couples looking for a bespoke vacation, the state offers top tourist places in Telangana and highly popular Instagram locations like the majestic Falaknuma Palace step-gardens, the sparkling Hussain Sagar Lake at twilight, and the massive fantasy sets of Ramoji Film City. Whether you are looking for authentic pearl shopping at Laad Bazaar, tasting authentic world-famous Hyderabadi Biryani, or experiencing cultural highlights, our TRAGUIN Telangana Packages ensure premium stays and curated experiences during the absolute best time to visit Telangana.',
        seo_title='TG-006 | LUXURY HYDERABAD ESCAPE | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Telangana package (TG-006 / TRG-TEL-006): Hyderabad • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD', 1),
            _ih('Day 02: HISTORIC MONUMENTS & PALACES TOUR', 2),
            _ih('Day 03: GOLCONDA FORT & QUTB SHAHI TOMBS', 3),
            _ih('Day 04: FULL DAY RAMOJI FILM CITY EXCURSION', 4),
            _ih('Day 05: SALAR JUNG MUSEUM & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Elite, skip-the-line access to Chowmahalla Palace with a specialized', 6),
            _ih('Curated by TRAGUIN Experts: Handpicked scheduling to tour the Old City during optimal morning', 7),
            _ih('Premium Handpicked Hotels: Accommodations evaluated meticulously based on luxury parameters,', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD',
                (
                    'WELCOME TO THE CITY OF PEARLS – ELITE ARRIVAL & TWILIGHT CRUISE Your premium Telangana experience begins as you touch down at Rajiv Gandhi International Airport or Hyderabad Station, where your dedicated private luxury transport vehicle waits. Transfer to your handpicked premium luxury hotel and experience a royal Nizami welcome. After a refreshing afternoon, proceed for an exclusive evening experience at Hussain Sagar Lake. Board a private luxury boat to cruise past the monolithic Buddha Statue as the city lights shimmer across the water, creating an ideal canvas for photography points.'
                ),
                [
                    'Sightseeing Included: Hussain Sagar Lake, Birla Mandir architectural view, Necklace Road promenade.',
                    'Evening Experience: Private sunset boat cruise with high-tea refreshments curated by TRAGUIN experts.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Selected Hotel)',
                    'Meals Included: Welcome Drink & Fine-Dining Luxury Dinner',
                ],
            ),
            _day(
                2,
                'HISTORIC MONUMENTS & PALACES TOUR',
                (
                    'ECHOES OF THE NIZAMS – ARCHITECTURAL MARVELS & LUXURY SHOPPING Awake to a lavish breakfast before setting out for an immersive journey through old-world Hyderabad sightseeing. Stand beneath the monumental arches of Charminar, an iconic attraction of India. Walk through the opulent courtyards of Chowmahalla Palace, mirroring the grand lifestyle of the Asaf Jahi dynasty with its vintage car collections and crystal chandeliers. In the late afternoon, enjoy an exclusive shopping excursion through Laad Bazaar, renowned globally for its hand-crafted lacquer and pearl jewelry.'
                ),
                [
                    'Sightseeing Included: Charminar, Chowmahalla Palace, Mecca Masjid, Laad Bazaar.',
                    'Optional Activities: Private guided pearl valuation session with a master heritage jeweler.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Selected Hotel)',
                    'Meals Included: Premium Breakfast & Authentic Nizam Thali Dinner',
                ],
            ),
            _day(
                3,
                'GOLCONDA FORT & QUTB SHAHI TOMBS',
                (
                    'FORTRESS OF DIAMONDS – ACOUSTIC WONDERS & LIGHT SHOW Indulge in a fine morning breakfast and proceed to the grand Golconda Fort, one of the top tourist places in Telangana. Marvel at the magical acoustic system where a clap at the entry gates echoes up to the highest pavilion. Wander through the majestic, landscaped Qutb Shahi Tombs, which stand as breathtaking landscapes of medieval architecture. Conclude your evening with VIP seats at the brilliant sound and light show narrating the history of the Diamond Kingdom.'
                ),
                [
                    'Sightseeing Included: Golconda Fort complex, Qutb Shahi Heritage Park Tombs.',
                    'Evening Experience: VIP entry to the Golconda Sound & Light Show with private guide accompaniment.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Selected Hotel)',
                    'Meals Included: Premium Breakfast & Specialty Gourmet Dinner',
                ],
            ),
            _day(
                4,
                'FULL DAY RAMOJI FILM CITY EXCURSION',
                (
                    'THE MAGIC OF CINEMA – CELEBRITY RED-CARPET EXPERIENCE Following an early breakfast, take a scenic drive to the world’s largest integrated film studio complex—Ramoji Film City. Enjoy an exclusive experience with a private tour guide and air-conditioned luxury transportation moving through massive cinematic sets, grand Mughal gardens, and international stunt shows. It is a highly popular Instagram location and a delightful highlight for a luxury Telangana holiday.'
                ),
                [
                    'Sightseeing Included: Ramoji Studio Tour, Bahubali Film Sets, Action Studio, Eco Zone & Bird Park.',
                    'Optional Activities: Bespoke thematic photo session inside famous cinematic sets.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Selected Hotel)',
                    'Meals Included: Premium Breakfast & Farewell Buffet Dinner',
                ],
            ),
            _day(
                5,
                'SALAR JUNG MUSEUM & DEPARTURE',
                (
                    'PRESERVING UNFORGETTABLE MEMORIES – ROYAL DEPARTURE Savor your final luxury breakfast at the property before exploring the world-famous Salar Jung Museum, housing one of the largest single-man collections of antiques in the world. Admire the iconic Veiled Rebecca marble statue before checking out. Your private luxury transport will safely drive you to Hyderabad Airport or Railway Station for your onward destination. Return home carrying unforgettable memories curated seamlessly by TRAGUIN.'
                ),
                [
                    "Sightseeing Included: Salar Jung Museum art walk, Nizam's Jubilee Pavilion (if time permits).",
                    'Transfers Included: Private door-to-door luxury airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Vivanta Hyderabad, Begumpet /',
                'Hyderabad',
                '4N',
                'Deluxe',
                'similar',
                'Superior Courtyard',
                4,
                1,
                description='OPTION 01 – DELUXE: Vivanta Hyderabad, Begumpet / | similar | Superior Courtyard',
            ),
            _hotel(
                'Hyatt Regency / ITC Kakatiya /',
                'Hyderabad',
                '4N',
                'Premium',
                'similar',
                'Premium Executive',
                4,
                2,
                description='OPTION 02 – PREMIUM: Hyatt Regency / ITC Kakatiya / | similar | Premium Executive',
            ),
            _hotel(
                'The Park Hyatt / Taj Krishna /',
                'Hyderabad',
                '4N',
                'Luxury',
                'Park Hyderabad',
                'Luxury Club Valley',
                4,
                3,
                description='OPTION 03 – LUXURY: The Park Hyatt / Taj Krishna / | Park Hyderabad | Luxury Club Valley',
            ),
            _hotel(
                'Taj Falaknuma Palace (The',
                'Hyderabad',
                '4N',
                'Ultra Luxury',
                'Mirror of Sky)',
                'VVIP Royal Palace',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace (The | Mirror of Sky) | VVIP Royal Palace',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 04 Nights in handpicked premier accommodation.', 1),
            _inc_included('Luxury Transportation: Private dedicated AC vehicle for all transfers.', 2),
            _inc_included('Curated Meal Plan: Daily luxury breakfast and gourmet specialized dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations manager on active call.', 4),
            _inc_included('Welcome Amenities: Personalized travel documentation, sanitization, and snack kits.', 5),
            _inc_included('Complimentary Experience: Reserved tickets for the private Hussain Sagar Lake Cruise.', 6),
            _inc_excluded('Airfare, domestic flight costs, or cross-state train tickets.', 7),
            _inc_excluded('Monument entrance tickets, guide services, or camera fees.', 8),
            _inc_excluded('Personal expenses including laundry, telephone services, and alcoholic drinks.', 9),
            _inc_excluded('Any optional excursions or individual lifestyle activities.', 10),
        ],
    )
    return package, itinerary

def build_tg_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-007'
    tour_code = 'TRG-TEL-007'
    title = 'LEISURE HYDERABAD • THE ROYAL NIZAMI LEGACY EXPERIENCE'
    duration = '04 Nights / 05 Days'
    slug = 'tg-007-leisure-hyderabad-the-royal-nizami-legacy-experience'
    itin_slug = 'tg-007-leisure-hyderabad-the-royal-nizami-legacy-experience-itinerary'
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
            _ph('Serial code TG-007 | TRAGUIN tour code TRG-TEL-007', 1),
            _ph('State / Country: Telangana / India | Category: Senior Citizen Custom Tour', 2),
            _ph('Destinations: Hyderabad • Telangana', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Private AC Traveller / MAPAI (Bespoke Menu)', 7),
            _ph('TRAGUIN Signature Experience: Private, exclusive palace tour arrangements with priority seating for', 8),
            _ph('Curated by TRAGUIN Experts: Custom slow-paced daily routing that guarantees ample relaxation hours', 9),
            _ph('Personalized Assistance: Constant, direct coordinate management for baggage handling at all hotel', 10),
            _ph('Luxury Transportation: Low step-height entry vehicles perfect for senior commuters.', 11)
        ],
        moods=['Luxury', 'Culture', 'Leisure'],
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
        tagline='LEISURE HYDERABAD',
        overview='LEISURE HYDERABAD • THE ROYAL NIZAMI LEGACY EXPERIENCE Welcome to a majestic exploration of history, culture, and timeless luxury crafted with utmost sensitivity by TRAGUIN. This exclusive Telangana Family Tour and dedicated senior citizen escape is planned TRAGUIN Elite Luxury Travel Proposal • TG-007 1 specifically to offer a relaxed pace, eliminating strenuous walks while preserving the absolute magic of the City of Pearls. As your premium travel consultants, TRAGUIN ensures that your luxury holiday unfolds smoothly, pairing the monumental grandeur of the Nizams with unmatched personal comfort, handpicked hotels, and curated experiences that leave our esteemed guests with unforgettable memories.\n\nTOUR OVERVIEW\nThoughtfully designed as a premium FIT itinerary for senior citizens, this holiday bypasses rapid schedules in favor of deep immersion and easy transfers. Traveling in an ultra-spacious, customized luxury vehicle with professional chauffeur-driven assistance and dedicated local handlers, you are assured wheelchair assistance parameters where required. With an optimized meal plan featuring gentle yet luxurious dining variants, your path covers the finest cultural treasures of Telangana. Every element incorporates the elite TRAGUIN curated experience hallmark—guaranteeing prioritized monument entries, verified smooth floor accesses, and unparalleled hospitality.\n\nWHY BOOK THE BEST TELANGANA TOUR PACKAGE?\nWhen considering a Luxury Telangana Holiday, mature travelers search for an itinerary that offers comfort without compromising on cultural enrichment. Hyderabad, the historic capital, boasts a spectacular array of iconic attractions. From the architectural marvel of the Charminar to the acoustic brilliance of the Golconda Fort, Telangana Sightseeing provides an inspiring window into medieval India. For newlyweds booking a romantic Telangana Honeymoon Package or seniors enjoying a peaceful reunion, the city offers popular Instagram locations such as the stunning white marble structures of the Birla Temple and the sunset vistas over Hussain Sagar Lake. Our specialized TRAGUIN Telangana Packages ensure that guests enjoy exclusive experiences, exquisite local shopping for world-renowned pearls, and mild variants of the iconic Hyderabadi Biryani. Traveling during the best time to visit Telangana allows you to appreciate these top tourist places in Telangana wrapped in absolute premium comfort. DAY WISE ITINERARY',
        seo_title='TG-007 | LEISURE HYDERABAD | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Telangana package (TG-007 / TRG-TEL-007): Hyderabad • Telangana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD', 1),
            _ih('Day 02: HISTORIC HYDERABAD EXPLORATION', 2),
            _ih('Day 03: GOLCONDA SOUND & LIGHT SPECTACLE', 3),
            _ih('Day 04: RAMOJI FILM CITY LEISURE EXCURSION', 4),
            _ih('Day 05: SOUVENIR COLLECTING & DEPARTURE', 5),
            _ih('TRAGUIN Signature Experience: Private, exclusive palace tour arrangements with priority seating for', 6),
            _ih('Curated by TRAGUIN Experts: Custom slow-paced daily routing that guarantees ample relaxation hours', 7),
            _ih('Personalized Assistance: Constant, direct coordinate management for baggage handling at all hotel', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD',
                (
                    'ROYAL RECEPTION & LEISURELY CRUISE ON HUSSAIN SAGAR Your premium Telangana experience begins as you step out of Hyderabad Airport. Your private TRAGUIN tour representative greets you warmly and guides you to your luxury vehicle. After checking into one of our handpicked hotels with hassle-free room keys, enjoy a relaxed afternoon. In the late evening, proceed for a tranquil experience at Hussain Sagar Lake. A private motorized boat ferries you smoothly to the monolithic statue of Lord Buddha, followed by a gentle musical fountain show at NTR Gardens. TRAGUIN Elite Luxury Travel Proposal • TG-007 2 restaurant.'
                ),
                [
                    'Sightseeing Included: Hussain Sagar Lake, Monolithic Buddha Statue, NTR Gardens area ambiance.',
                    'Evening Experience: Bespoke welcome dinner featuring mild, authentic Nizami flavors at your hotel',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel Property)',
                    'Meals Included: Welcome Special Drink & Gourmet Buffet Dinner',
                ],
            ),
            _day(
                2,
                'HISTORIC HYDERABAD EXPLORATION',
                (
                    "THE ICONIC CHARMINAR & CHOWMAHALLA PALACE SPLENDOUR Savor a premium healthy breakfast before venturing out for a cultural dip into history. Arrive at Chowmahalla Palace, the grand seat of the Asaf Jahi dynasty, where wide corridors and pristine vintage car collections offer a comfortable, accessible walking experience. View the iconic Charminar from a designated comfort seating point, allowing for beautiful photography without navigating crowded bazaars. Finish your afternoon at the Salar Jung Museum, admiring one of the world's largest private art collections with optional wheelchair assistance."
                ),
                [
                    'Sightseeing Included: Chowmahalla Palace, Charminar photo stop, Salar Jung Museum (with lift access).',
                    'Optional Activities: Private luxury showroom shopping session for authentic Hyderabadi Cultured Pearls.',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel Property)',
                    'Meals Included: Healthy Premium Breakfast & Luxury Dinner',
                ],
            ),
            _day(
                3,
                'GOLCONDA SOUND & LIGHT SPECTACLE',
                (
                    'ACOUSTIC MARVELS & THE MAJESTIC BIRLA TEMPLE Dedicate your morning to spirituality at the stunning Birla Temple, carved beautifully from pure white Rajasthani marble, offering serene views of the city skyline. In the afternoon, rest comfortably at your luxury resort. As evening falls, your vehicle smoothly transitions to the Golconda Fort. Here, skip the strenuous uphill climb; instead, settle into VIP reserved seating to enjoy the dramatic Sound & Light Show, narrated by iconic voices illuminating centuries of history. TRAGUIN Elite Luxury Travel Proposal • TG-007 3'
                ),
                [
                    'Sightseeing Included: Birla Venkateswara Temple, Golconda Fort lower courts, Evening Sound & Light Show.',
                    'Evening Experience: A private traditional high-tea session with views of the illuminated battlements.',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel Property)',
                    'Meals Included: Premium Breakfast & Royal Multi-Cuisine Dinner',
                ],
            ),
            _day(
                4,
                'RAMOJI FILM CITY LEISURE EXCURSION',
                (
                    'A DAY OF CINEMATIC MAGIC & MANICURED LANDSCAPES Embark on a delightful day trip to the world-renowned Ramoji Film City. To maximize comfort for our senior travelers, we arrange for an exclusive premium air-conditioned coach experience inside the complex. Marvel at the sprawling gardens, cinematic sets, and live entertainment spectaculars without feeling fatigued. Witness beautiful fountains, mock palaces, and professional dance shows before returning to your hotel in absolute comfort.'
                ),
                [
                    'Sightseeing Included: Ramoji Film City Studio Tour, Eco Zone, Bird Park, Cinematic Live Shows.',
                    'Optional Activities: Photography tour across legendary film-set replicas.',
                    'Overnight Stay: Hyderabad (Premium Luxury Hotel Property)',
                    'Meals Included: Premium Breakfast & Farewell Celebration Dinner',
                ],
            ),
            _day(
                5,
                'SOUVENIR COLLECTING & DEPARTURE',
                (
                    'CHERISHING MEMORIES BEYOND DESTINATIONS Enjoy a relaxed morning breakfast followed by a smooth check-out. If flight timings permit, take a brief scenic drive through the ultra-modern HITEC City corridor, showcasing the contemporary face of Telangana. Drop off at a premium handicraft emporium to collect authentic local souvenirs and beautiful fabrics. Later, your private chauffeur ensures a seamless drop-off directly to the airport terminal, concluding an exceptional holiday built on care and luxury. TRAGUIN Elite Luxury Travel Proposal • TG-007 4 PREMIUM HANDPICKED'
                ),
                [
                    'Transfers Included: Private chauffeured airport drop-off service.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                    'SHOPPING: & LOCAL EXPERIENCES',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Mercure Hyderabad KCP',
                'Telangana',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Mercure Hyderabad KCP',
            ),
            _hotel(
                'The Dasapalla / Vivanta Hyderabad Premium Executive Room Excellent elevator placement, quiet wings',
                'Telangana',
                '4N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Dasapalla / Vivanta Hyderabad Premium Executive Room Excellent elevator placement, quiet wings',
            ),
            _hotel(
                'ITC Kakatiya / Taj KrishnaLuxury Club Room Bespoke customized bedding, personalized service',
                'Telangana',
                '4N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: ITC Kakatiya / Taj KrishnaLuxury Club Room Bespoke customized bedding, personalized service',
            ),
            _hotel(
                'Taj Falaknuma Palace Royal Palace Palace Suite Nizami horse-carriage reception, VIP palace care',
                'Telangana',
                '4N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace Royal Palace Palace Suite Nizami horse-carriage reception, VIP palace care',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 4 Nights in luxury properties featuring flat floor entries.', 1),
            _inc_included('Luxury Transportation: Private luxury vehicle for all point-to-point sightseeing.', 2),
            _inc_included('Custom Meal Plan: Daily mild gourmet breakfasts and detailed dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 priority senior-citizen care phone line.', 4),
            _inc_included('VIP Entrances: Pre-booked entry tickets to eliminate standing queues.', 5),
            _inc_included('Complimentary Experience: Private boat ride tickets on Hussain Sagar Lake.', 6),
            _inc_excluded('Domestic or International airfares and train bookings.', 7),
            _inc_excluded('Personal expenses like telephone charges, laundry, and minibar usage.', 8),
            _inc_excluded('Camera licenses or video equipment fees at historical spots.', 9),
            _inc_excluded('Any supplementary medical care or travel insurance plans. TRAGUIN Elite Luxury Travel Proposal • TG-007 5', 10),
        ],
    )
    return package, itinerary

def build_tg_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-008'
    tour_code = 'TRG-TEL-008'
    title = 'HYDERABAD EDUCATIONAL TOUR • ENVISIONING KNOWLEDGE, SCIENCE & HERITAGE'
    duration = '03 Nights / 04 Days'
    slug = 'tg-008-hyderabad-educational-tour-envisioning-knowledge-science-heritage'
    itin_slug = 'tg-008-hyderabad-educational-tour-envisioning-knowledge-science-heritage-itinerary'
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
            _ph('Serial code TG-008 | TRAGUIN tour code TRG-TEL-008', 1),
            _ph('State / Country: Telangana / India | Category: School Educational Tour', 2),
            _ph('Destinations: Hyderabad • Ramoji', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Multi-Axle Volvo Coach / APAC (All Meals)', 7),
            _ph('TRAGUIN Signature Experience: Private acoustic clapping test workshop at the majestic arches of', 8),
            _ph('Curated by TRAGUIN Experts: Structuring traffic routes to maximize field study duration while keeping', 9),
            _ph('Personalized Assistance: Pre-departure academic orientations hosted at institutions by expert travel', 10),
            _ph('Exclusive Recommendations: Specially monitored and certified student menus focusing strictly on', 11)
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
        tagline='HYDERABAD EDUCATIONAL TOUR',
        overview='HYDERABAD EDUCATIONAL TOUR • ENVISIONING KNOWLEDGE, SCIENCE & HERITAGE Welcome to an academically enriching and highly engaging student expedition proudly curated by TRAGUIN. Embark on the finest Telangana Family Tour and Student Immersion Program, intricately engineered to seamlessly combine learning with premium luxury. As your professional travel consultants, TRAGUIN Premium Luxury Itinerary — TG-008 1 TRAGUIN transforms an ordinary field trip into a premium Telangana experience, featuring meticulously curated experiences, handpicked hotels, and comprehensive structural planning. From the historical marvels of the Nizams to state-of-the-art space exploration hubs, this program guarantees unforgettable memories and deep academic value for young minds.\n\nTOUR OVERVIEW\nThis custom architecture student program offers a highly premium luxury holiday approach to institutional travel. Operating with premium stays, large multi-axle luxury coach transportation, and an inclusive meal plan (all buffet breakfasts, student lunches, and nutritious dinners), the route covers the absolute top tourist places in Telangana. Backed by the signature TRAGUIN curated experience note, every group receives dedicated tour managers, strict security protocols, premium guide assistance, and experiential learning workshops across iconic attractions.\n\nWHY CHOOSE THE BEST TELANGANA TOUR PACKAGE?\nWhen shortlisting the premier Telangana Family Tour or Student Group Expedition, selecting a highly comprehensive and safe operational itinerary is paramount. Hyderabad is renowned for hosting the most sought-after interactive educational zones in India. From the legendary battlefields of Golconda Fort to the universe-simulating dome of Birla Planetarium, Telangana sightseeing offers an unparalleled blend of ancient history, deep culture, and advanced modern technology. For educational bodies seeking a premium Luxury Telangana Holiday or custom Telangana Honeymoon Package setups, the city offers popular Instagram locations like the majestic Charminar, the breathtaking landscapes of Hussain Sagar Lake, and the sprawling entertainment sets of Ramoji Film City. Our custom TRAGUIN Telangana Packages ensure handpicked hotels, seamless travel schedules, and deep immersive experiences, identifying the absolute best time to visit Telangana for complete academic and structural satisfaction.',
        seo_title='TG-008 | HYDERABAD EDUCATIONAL TOUR | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Telangana package (TG-008 / TRG-TEL-008): Hyderabad • Ramoji with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD & HERITAGE EXPLORATION', 1),
            _ih('Day 02: RAMOJI FILM CITY EXCURSION', 2),
            _ih('Day 03: SCIENCE, SPACE & FORTRESS STRATEGY', 3),
            _ih('Day 04: SALAR JUNG MUSEUM & HOMEWARD BOUND', 4),
            _ih('TRAGUIN Signature Experience: Private acoustic clapping test workshop at the majestic arches of', 5),
            _ih('Curated by TRAGUIN Experts: Structuring traffic routes to maximize field study duration while keeping', 6),
            _ih('Personalized Assistance: Pre-departure academic orientations hosted at institutions by expert travel', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD & HERITAGE EXPLORATION',
                (
                    'WELCOME TO THE CITY OF NIZAMS – HISTORIC ROOTS & MONUMENTAL STORIES Your premium Telangana experience springs to life upon arrival at Hyderabad Rajiv Gandhi International Airport or Secunderabad Station. Meet your dedicated luxury transportation coaches and transfer to your handpicked premium stays. Following a specialized introductory student brief, start your tour at the majestic Charminar and the historic Mecca Masjid. Dive into rich historic storytelling, explaining the Nizam architecture, before gathering on the banks of Hussain Sagar Lake to admire the giant monolithic Buddha Statue during sunset.'
                ),
                [
                    'Sightseeing Included: Charminar, Mecca Masjid, Hussain Sagar Lake, Monolithic Buddha Statue.',
                    'Evening Experience: Laser light and sound fountain show at Lumbini Park with private student gallery seating.',
                    'Overnight Stay: Hyderabad (Premium Student-Friendly Luxury Hotel)',
                    'Meals Included: Buffet Student Lunch & Luxury Institutional Dinner',
                ],
            ),
            _day(
                2,
                'RAMOJI FILM CITY EXCURSION',
                (
                    "A JOURNEY INTO THE WORLD OF CINEMA, MEDIA & CREATIVE ARCHITECTURE Indulge in a crisp morning buffet breakfast before departing for the world's largest integrated film studio complex—Ramoji Film City. This immersive experience offers students direct insight into cinematic arts, visual mechanics, live theatrical performance, sound design, and stage production. Walk through royal palace sets, scenic beauty locations, western cowboy setups, and eco-parks, capturing amazing photos at multiple popular Instagram locations."
                ),
                [
                    'Sightseeing Included: Ramoji Studio Tours, Action Studio, Filmi Duniya, Extravaganza Live Shows, Bird Park.',
                    'Optional Activities: Interactive student workshop with production crew directors on movie-making.',
                    'Overnight Stay: Hyderabad (Premium Student-Friendly Luxury Hotel)',
                    'Meals Included: Full Buffet Breakfast, Studio Buffet Lunch & Special Dinner',
                ],
            ),
            _day(
                3,
                'SCIENCE, SPACE & FORTRESS STRATEGY',
                (
                    'INTERACTIVE LEARNING HUB & MAGNIFICENT ACOUSTIC ENGINEERING Dedicate this day to high-value educational core targets. Begin your day exploring the Birla Science Museum and Planetarium, ranked among the top tourist places in Telangana for science interactions. Students can interact directly with physics projects, celestial stargazing displays, and ancient dinosaur fossils. In the afternoon, shift to the towering Golconda Fort to learn about ancient mediaeval acoustic engineering, defensive fortress design, and historical water management systems.'
                ),
                [
                    'Sightseeing Included: B.M. Birla Science Museum, Space Planetarium, Golconda Fort Heritage Walk.',
                    'Evening Experience: Historical Sound & Light Show at Golconda Fort narrated by legendary cinematic voices.',
                    'Overnight Stay: Hyderabad (Premium Student-Friendly Luxury Hotel)',
                    'Meals Included: Premium Breakfast, Organized Hot Lunch & Grand Farewell Dinner',
                ],
            ),
            _day(
                4,
                'SALAR JUNG MUSEUM & HOMEWARD BOUND',
                (
                    'GLOBAL ARTIFACTS COLLECTION & CHERISHING KNOWLEDGE JOURNEYS Following breakfast, explore the iconic Salar Jung Museum, housing one of the largest one-man collections of antiques, royal weaponry, and fine art masterpieces on Earth. Witness the famous 19th-century musical clock mechanism before taking time for souvenir handicraft shopping. In the afternoon, your private luxury transportation coach handles airport or railway transfers safely. Return home filled with deep intellectual insights and unforgettable memories crafted by TRAGUIN.'
                ),
                [
                    'Transfers Included: Private terminal or platform luxury coach drop-offs.',
                    'Meals Included: Sumptuous Buffet Breakfast & Packed Departure Lunch',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Hotel Ibis Hyderabad / Lemon Tree',
                'Telangana',
                '3N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Hotel Ibis Hyderabad / Lemon Tree',
            ),
            _hotel(
                'Novotel Hyderabad Airport / Courtyard by Marriott Twin Sharing PremiumFull APAC Institutional Matrix',
                'Telangana',
                '3N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Novotel Hyderabad Airport / Courtyard by Marriott Twin Sharing PremiumFull APAC Institutional Matrix',
            ),
            _hotel(
                'ITC Kohenur / The Park Hyderabad Luxury Twin Room Accommodation Premium Handpicked Fine Dining',
                'Telangana',
                '3N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: ITC Kohenur / The Park Hyderabad Luxury Twin Room Accommodation Premium Handpicked Fine Dining',
            ),
            _hotel(
                'Taj Falaknuma Palace (Exclusive Group Block) VVIP Royal Heritage Suite Setup Bespoke Royal Custom Catering',
                'Telangana',
                '3N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace (Exclusive Group Block) VVIP Royal Heritage Suite Setup Bespoke Royal Custom Ca',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: 03 Nights in student-safe, secure premium hotels.', 1),
            _inc_included('Luxury Transportation: High-end, sanitized AC coaches for all transfers.', 2),
            _inc_included('Full Board Meals: All institutional breakfasts, lunches, and mineral water.', 3),
            _inc_included('TRAGUIN Support: Dedicated student travel marshall and 24/7 concierge.', 4),
            _inc_included('Complimentary Experience: Entry fees to Ramoji Film City and both Sound Shows.', 5),
            _inc_included('Safety Parameters: Group first-aid assistance kits and dedicated female marshalls.', 6),
            _inc_excluded('Domestic or international flight tickets to and from Hyderabad.', 7),
            _inc_excluded('Personal electronics hire, camera fees, video camera permits.', 8),
            _inc_excluded('Personal purchase expenses, laundry, tips, shopping, or specialized food orders.', 9),
            _inc_excluded('Medical insurance or any emergency hospitalization costs.', 10),
        ],
    )
    return package, itinerary

def build_tg_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-009'
    tour_code = 'TRG-TEL-009'
    title = 'HYDERABAD CORPORATE MICE ELITE RETREAT'
    duration = '03 Nights / 04 Days'
    slug = 'tg-009-hyderabad-corporate-mice-elite-retreat'
    itin_slug = 'tg-009-hyderabad-corporate-mice-elite-retreat-itinerary'
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
            _ph('Serial code TG-009 | TRAGUIN tour code TRG-TEL-009', 1),
            _ph('State / Country: Telangana / India | Category: MICE Corporate Presentation', 2),
            _ph('Destinations: Hyderabad • Telangana', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Luxury Multi-Axle Coaches / All- Inclusive Corporate Meal Plan', 7)
        ],
        moods=['Luxury', 'Corporate'],
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
        tagline='HYDERABAD CORPORATE MICE ELITE RETREAT',
        overview='HYDERABAD CORPORATE MICE ELITE RETREAT TRAGUIN Corporate Luxury Proposal — TG-009 1 Welcome Note: Welcome to a meticulously designed business retreat presented by TRAGUIN. This exclusive corporate itinerary has been engineered specifically for premium business delegates to experience the perfect synergy between state-of-the-art infrastructure and the royal timeless heritage of Telangana. As your specialist corporate travel consultants, TRAGUIN transforms business travel into an unforgettable luxury holiday experience, combining elite conference venues with immersive experiences and handpicked hotels. Prepare for a seamless, executive-class journey where corporate goals align beautifully with curated premium leisure.\n\nTOUR OVERVIEW\nThe TRAGUIN Hyderabad Corporate Tour is a custom-curated business proposal designed for highly professional Corporate MICE groups. This strategic itinerary features executive transfers via premium luxury multi-axle air-conditioned coaches, a comprehensive institutional meal plan with world-class catering, and a perfectly balanced route map covering Hyderabad’s central business hubs and legendary landmarks. From technical modern marvels to grand gala dinners amidst Nizami grandeur, every single touchpoint incorporates the exclusive TRAGUIN curated experience note, promising flawless on-site coordination, dedicated concierge support, and premium team alignment.\n\nWHY CHOOSE THE BEST TELANGANA TOUR PACKAGE FOR\nCORPORATE MICE? When organizing high-stakes business events, selecting a premier hub with state-of-the-art facilities and a rich cultural fabric is essential. Hyderabad stands out as one of the ultimate locations for a Luxury Telangana Holiday or a high-impact corporate retreat. Offering the perfect blend of historic architecture and massive conventions facilities, it is widely recognized as a top tourist place in Telangana for both local sightseeing and modern technical summits. Whether planning an expansive Telangana Family Tour, a reward-based incentive getaway, or a Telangana Honeymoon Package for top performers, the city provides spectacular iconic attractions and sought-after experiences. From the corporate corridors of Hi-Tech City and Gachibowli to popular Instagram locations like the majestic Charminar and the breathtaking landscapes of Golconda Fort, the options are boundless. Delegates can immerse themselves in traditional Nizami culture, enjoy authentic luxury shopping for premium pearls, and savor the world-famous Hyderabadi Biryani. Booking our specialized TRAGUIN Telangana Packages ensures access to premium stays, seamless transportation, and handpicked local experiences during the absolute best time to visit Telangana. TRAGUIN Corporate Luxury Proposal — TG-009 2',
        seo_title='TG-009 | HYDERABAD CORPORATE MICE ELITE RETREAT | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Telangana package (TG-009 / TRG-TEL-009): Hyderabad • Telangana with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD – HI-TECH RETREAT', 1),
            _ih('Day 02: HIGH-IMPACT CONFERENCE & ROYAL GALA EVENING', 2),
            _ih('Day 03: FULL-DAY TEAM SYNERGY AT RAMOJI FILM CITY', 3),
            _ih('Day 04: ICONIC HERITAGE SIGHTSEEING – DEPARTURE', 4)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD – HI-TECH RETREAT',
                (
                    'WELCOME BRIEFING, EXECUTIVE CHECKS & NIZAMI COCKTAIL CRUISE Your premium Telangana experience officially starts as delegates touch down at Rajiv Gandhi International Airport. Enjoy a seamless welcome experience organized by our dedicated on-ground team. Private premium luxury coaches escort the group along the smooth outer ring road to a handpicked ultra-luxury hotel in the heart of Gachibowli or Hi-Tech City. Following an efficient private group check-in and an executive networking lunch, enjoy a relaxed afternoon briefing. As dusk falls, head out for an exclusive evening experience: a private chartered sunset cruise on the serene waters of Hussain Sagar Lake, offering spectacular waterfront.'
                ),
                [
                    'photography points: with the illuminated standing Buddha statue in the background.',
                    'Sightseeing Included: Necklace Road drive, Hussain Sagar Lake panoramic views, Cyber City landmarks.',
                    "Optional Activities: Pre-conference executive dry-run session at the hotel's boardroom facility.",
                    'Evening Experience: A Nizami-themed welcome cocktail reception with live classical music on the',
                    'Overnight Stay: Hyderabad (Premium 5-Star Business Luxury Hotel)',
                    'Meals Included: Executive Networking Lunch & Gala Welcome Dinner',
                ],
            ),
            _day(
                2,
                'HIGH-IMPACT CONFERENCE & ROYAL GALA EVENING',
                (
                    "STRATEGIC SESSIONS AND PALATIAL NIZAMI OPULENCE Dedicate your morning to your strategic business goals with a premium conference experience inside the hotel’s grand ballroom. Enjoy high-speed connectivity, state-of-the-art audiovisual setups, and custom-tailored corporate breaks. In the afternoon, transition from business to heritage with a private guided tour of the historic Golconda Fort, showcasing marvelous acoustic engineering that echoes the region's rich past. As night falls, indulge in an unforgettable evening at a royal palace venue. This immersive experience features a curated royal culinary feast, transporting delegates back to the golden era of the Nawabs. TRAGUIN Corporate Luxury Proposal — TG-009 3 fortifications. Pukht cuisine."
                ),
                [
                    'Sightseeing Included: Golconda Fort acoustic walk, Qutb Shahi Tombs heritage reservation area.',
                    'Optional Activities: Professional corporate drone videography and group portraiture at the historic',
                    'Evening Experience: A royal gala banquet complete with Sufi musical performances and authentic Dum',
                    'Overnight Stay: Hyderabad (Premium 5-Star Business Luxury Hotel)',
                    'Meals Included: Breakfast, Mid-Session Breaks, & Royal Imperial Dinner',
                ],
            ),
            _day(
                3,
                'FULL-DAY TEAM SYNERGY AT RAMOJI FILM CITY',
                (
                    'IMMERSIVE KINETIC EXPERIENCES & LARGE-SCALE TEAM BUILDING Embark on an early morning drive to the world-renowned Ramoji Film City, the largest integrated film studio complex on earth and a premier destination for corporate engagement. This expansive venue features breathtaking landscapes, massive thematic sets, and manicured lawns perfect for custom team-building activities. TRAGUIN experts have arranged VIP access passes for the group, ensuring premium entry into studio stages, stunt workshops, and cinematic simulators. It is an amazing location filled with popular Instagram locations and interactive team challenges designed to inspire collaboration and leave lasting corporate memories. and cocktail arrays.'
                ),
                [
                    'Sightseeing Included: Bahubali Set, Eureka Extravaganza, Mughal Gardens, Askari Aviary Aviations.',
                    'Optional Activities: Custom corporate team-building games led by a professional behavioral facilitator.',
                    'Evening Experience: An interactive corporate rewards ceremony accompanied by high-energy DJ music',
                    'Overnight Stay: Hyderabad (Premium 5-Star Business Luxury Hotel)',
                    'Meals Included: Buffet Breakfast, Special Studio Lunch, & Festive Corporate Dinner',
                ],
            ),
            _day(
                4,
                'ICONIC HERITAGE SIGHTSEEING – DEPARTURE',
                (
                    "OLD CITY EXPLORATION, LUXURY PEARL SHOPPING & FAREWELL Indulge in a final lavish breakfast at the hotel before checking out. Conclude your tour with an immersive exploration of Hyderabad's iconic Old City. Walk around the monumental Charminar and visit the grand Chowmahalla Palace, the historical seat of the Asaf Jahi dynasty. Enjoy an exclusive shopping excursion at Laad Bazaar, renowned worldwide for premium culture pearls, bangles, and authentic traditional souvenirs. Later in the afternoon, your private luxury coaches will drive you back to Rajiv Gandhi International Airport for TRAGUIN Corporate Luxury Proposal — TG-009 4 your return flights. Return home with strengthened team bonds and unforgettable corporate memories designed flawlessly by TRAGUIN."
                ),
                [
                    'Sightseeing Included: Charminar structural plaza, Chowmahalla Palace interiors, Laad Bazaar.',
                    'Transfers Included: Private door-to-door luxury airport drop-off for all corporate delegates.',
                    'Meals Included: Sumptuous Buffet Breakfast & Traditional Hyderabadi Farewell Lunch',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Novotel Hyderabad Convention Centre / Radisson Blu Hi-Tech City Superior Corporate Room',
                'Telangana',
                '3N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Novotel Hyderabad Convention Centre / Radisson Blu Hi-Tech City Superior Corporate Room',
            ),
            _hotel(
                'The Westin Hyderabad Mindspace / Hyatt Regency Gachibowli Premium Executive Balcony Room',
                'Telangana',
                '3N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: The Westin Hyderabad Mindspace / Hyatt Regency Gachibowli Premium Executive Balcony Room',
            ),
            _hotel(
                'ITC Kohenur / Trident Hyderabad / Sheraton Hyderabad Hotel Luxury Club Valley Suite',
                'Telangana',
                '3N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: ITC Kohenur / Trident Hyderabad / Sheraton Hyderabad Hotel Luxury Club Valley Suite',
            ),
            _hotel(
                'Taj Falaknuma Palace (The Ultimate Royal Experience) Royal Palace Suite VVIP Tier',
                'Telangana',
                '3N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace (The Ultimate Royal Experience) Royal Palace Suite VVIP Tier',
            )
        ],
        inclusions=[
            _inc_included('Premium Accommodations: Chosen luxury stay with twin/single configurations.', 1),
            _inc_included('Conference Arrangements: 1 Full-day ballroom usage with professional tech assistance.', 2),
            _inc_included('Luxury Transportation: Private dedicated multi-axle coaches for all transfers & sightseeing.', 3),
            _inc_included('All-Inclusive Meal Plan: Lavish institutional breakfasts, custom breaks, and gala dinners.', 4),
            _inc_included('TRAGUIN Support: Dedicated 24/7 on-site event managers and expert local guides.', 5),
            _inc_included('INCLUDED SERVICES & GUEST AMENITIESCORPORATE EVENT FACILITIES Complimentary Experiences: Private chartered boat tickets and VIP access passes at Ramoji.', 6),
            _inc_included('Taxes & Hospitality: All applicable local institutional service taxes and welcome amenities.', 7),
            _inc_included('Welcome Amenities: Customized delegate gift packs, corporate badges, and city map kits.', 8),
            _inc_excluded('Domestic or International airfares and long- distance train ticketing.', 9),
            _inc_excluded('Personal service items such as laundry, liquor orders, and telephone bills.', 10),
            _inc_excluded('Individual camera permits, drone licensing fees, or separate local guide hires.', 11),
            _inc_excluded('Any optional adventure park entries, premium team building props, or external artists.', 12),
        ],
    )
    return package, itinerary

def build_tg_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TG-010'
    tour_code = 'TRG-TEL-010'
    title = 'COMPLETE TELANGANA • LEGENDS OF THE NIZAMS & KAKATIYAS'
    duration = '05 Nights / 06 Days'
    slug = 'tg-010-complete-telangana-legends-of-the-nizams-kakatiyas'
    itin_slug = 'tg-010-complete-telangana-legends-of-the-nizams-kakatiyas-itinerary'
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
            _ph('Serial code TG-010 | TRAGUIN tour code TRG-TEL-010', 1),
            _ph('State / Country: Telangana / India | Category: Premium Family Tour', 2),
            _ph('Destinations: Hyderabad •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Transport / MAPAI (Breakfast & Dinner)', 7),
            _ph('TRAGUIN Signature Experience: Private scholar-guided heritage walk through the historic quarters of', 8),
            _ph('Curated by TRAGUIN Experts: Custom routing designed to bypass heavy city traffic, ensuring maximum', 9),
            _ph('Premium Handpicked Hotels: Accommodations chosen based on excellent safety reviews, luxury', 10),
            _ph('Exclusive Recommendations: Curated list of elite tables for enjoying authentic, world-famous', 11)
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
        tagline='COMPLETE TELANGANA',
        overview='COMPLETE TELANGANA • LEGENDS OF THE NIZAMS & KAKATIYAS TRAGUIN Premium Luxury Itinerary — TG-010 1 Welcome to an unforgettable luxury exploration curated exclusively by TRAGUIN. Discover the rich tapestry of heritage, modern marvels, and spiritual grace with our signature Telangana Family Tour. As your professional travel consultants, TRAGUIN brings you a premium Telangana experience where imperial histories seamlessly blend with breathtaking landscapes and timeless architecture. From the majestic monuments of the Nizams in Hyderabad to the intricately carved stone architectures of Warangal, this itinerary offers premium stays, handpicked hotels, and exclusive experiences designed to create unforgettable memories for your entire family.\n\nTOUR OVERVIEW\nThis custom-designed holiday features a flawless route through the absolute finest cultural and recreational hubs of Telangana. Travelling in a chauffeured premium luxury vehicle, your family will experience unmatched convenience and safety. Indulge in an exquisite meal plan providing daily multi-cuisine breakfasts and customized fine-dining dinners. Every segment of this itinerary integrates a TRAGUIN curated experience note, guaranteeing priority monument passes, private guided narration from seasoned scholars, and round- the-clock tailored concierge support.\n\nWHY CHOOSE THE BEST TELANGANA TOUR PACKAGE?\nWhen planning a Luxury Telangana Holiday, modern families seek a balanced mix of grand architectural heritage, high-tech amusement, and peaceful spiritual getaways. Telangana boasts several iconic attractions, making it a highly requested travel option. From the globally revered Charminar and Golconda Fort to the UNESCO World Heritage Ramappa Temple in Warangal, Telangana sightseeing offers endless awe. For couples and large multi-generational groups planning a Telangana Honeymoon Package or Telangana Family Tour, the state offers top tourist places in Telangana that serve as popular Instagram locations—such as the scenic beauty of Hussain Sagar Lake at sunset, the royal pathways of Chowmahalla Palace, and the cinematic worlds of Ramoji Film City. Complete with exquisite local shopping for pearls, beautiful handloom sarees, and traditional Nizami food suggestions, our TRAGUIN Telangana Packages ensure you travel during the best time to visit Telangana with absolute peace of mind.',
        seo_title='TG-010 | COMPLETE TELANGANA | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Telangana package (TG-010 / TRG-TEL-010): Hyderabad • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN HYDERABAD', 1),
            _ih('Day 02: GOLCONDA FORT & HUSSAIN SAGAR CRUISE', 2),
            _ih('Day 03: FULL DAY AT RAMOJI FILM CITY', 3),
            _ih('Day 04: EXCURSION TO HISTORIC WARANGAL', 4),
            _ih('Day 05: SALAR JUNG MUSEUM & YADADRI EXCURSION', 5),
            _ih('Day 06: DEPARTURE FROM HYDERABAD', 6),
            _ih('TRAGUIN Signature Experience: Private scholar-guided heritage walk through the historic quarters of', 7),
            _ih('Curated by TRAGUIN Experts: Custom routing designed to bypass heavy city traffic, ensuring maximum', 8),
            _ih('Premium Handpicked Hotels: Accommodations chosen based on excellent safety reviews, luxury', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN HYDERABAD',
                (
                    'WELCOME TO THE CITY OF PEARLS – MAJESTIC NIZAMI HERITAGE Your premium Telangana experience begins as you touch down at Hyderabad International Airport. You will be warmly received by your dedicated private luxury transport driver and escorted to your premium handpicked'
                ),
                [
                    'Sightseeing Included: Charminar, Mecca Masjid, Chowmahalla Palace, Laad Bazaar.',
                    'Evening Experience: A slow walk through the pearl markets followed by an authentic royal Nizami dinner curated',
                    'Overnight Stay: Hyderabad (Premium / Luxury Hotel)',
                    'Meals Included: Welcome Drink & Luxury Dinner',
                ],
            ),
            _day(
                2,
                'GOLCONDA FORT & HUSSAIN SAGAR CRUISE',
                (
                    'ECHOES OF THE PAST & SCENIC LAKESIDE SPLENDOUR Enjoy a lavish breakfast before heading to the architectural masterpiece of Golconda Fort. Witness the acoustic wonders and historic bastions with a private historian. Afterwards, visit the nearby Qutb Shahi Tombs, which showcase a beautiful blend of Persian and Indian design. In the evening, head to the scenic Hussain Sagar Lake for an exclusive experience—a private boat cruise to the massive monolithic Buddha Statue, perfect for capturing family photographs at sunset.'
                ),
                [
                    'Sightseeing Included: Golconda Fort, Qutb Shahi Tombs, Hussain Sagar Lake, NTR Gardens.',
                    'Evening Experience: An immersive Laser Light and Sound Show at Golconda Fort with VIP seating.',
                    'Overnight Stay: Hyderabad (Premium / Luxury Hotel)',
                    'Meals Included: Premium Breakfast & Dinner',
                ],
            ),
            _day(
                3,
                'FULL DAY AT RAMOJI FILM CITY',
                (
                    "THE MAGIC OF CINEMA – AN UNPARALLELED FAMILY ADVENTURE Dedicate an exhilarating day to Ramoji Film City, the world's largest integrated film studio complex and a premier attraction on our Telangana family tour. Travel inside the studio in an exclusive premium vehicle. Explore grand cinematic sets, beautiful thematic gardens, live stunt shows, and interactive space simulations that appeal beautifully to both adults and children."
                ),
                [
                    'Sightseeing Included: Ramoji Studio Tour, Movie Magic Parks, Filmi Duniya, Live Entertainment Shows.',
                    'Optional Activities: Adventure challenges at the Sahas Theme Park.',
                    'Overnight Stay: Hyderabad or Luxury Ramoji Studio Resort',
                    'Meals Included: Premium Breakfast & Festive Buffet Dinner',
                ],
            ),
            _day(
                4,
                'EXCURSION TO HISTORIC WARANGAL',
                (
                    'THE KAKATIYA LEGACY – STONE MARVELS & UNESCO HERITAGE Set out on a morning drive through beautiful rural landscapes to the historic city of Warangal. Visit the breathtaking Thousand Pillar Temple, a masterpiece of Kakatiya sculpture. Continue to the Ramappa Temple, a UNESCO World Heritage site celebrated for its floating bricks and exquisite bracket figures. End your day at the majestic Warangal Fort to view the iconic stone gateways (Kakatiya Kala Thoranam).'
                ),
                [
                    'Sightseeing Included: Thousand Pillar Temple, Ramappa Temple, Warangal Fort, Bhadrakali Temple.',
                    'Evening Experience: A quiet sunset walk along the peaceful shores of Laknavaram Lake (if time permits).',
                    'Overnight Stay: Warangal / Hyderabad (Premium Selection)',
                    'Meals Included: Breakfast & Authentic Regional Deccan Dinner',
                ],
            ),
            _day(
                5,
                'SALAR JUNG MUSEUM & YADADRI EXCURSION',
                (
                    'TREASURES OF ART & SACRED ARCHITECTURAL GRACE Spend your morning browsing the incredible private collections at the Salar Jung Museum, including the famous Veiled Rebecca statue. In the afternoon, head to Yadadri to tour the magnificent, newly reconstructed Sri Lakshmi Narasimha Swamy Temple. Carved entirely from black stone, this architectural wonder offers a peaceful spiritual experience for the family.'
                ),
                [
                    'Sightseeing Included: Salar Jung Museum, Birla Mandir, Yadadri Temple Complex.',
                    'Optional Activities: Exclusive high-end shopping for Pochampally Ikat silk sarees.',
                    'Overnight Stay: Hyderabad (Premium Luxury Stay)',
                    'Meals Included: Breakfast & Farewell Premium Dinner',
                ],
            ),
            _day(
                6,
                'DEPARTURE FROM HYDERABAD',
                (
                    'CHERISHING UNFORGETTABLE MEMORIES BEYOND DESTINATIONS Enjoy a final leisurely breakfast at your luxury hotel. Depending on your flight schedule, fit in some last-minute comfortably to Hyderabad International Airport for your journey home, carrying sweet family bonds and unforgettable memories designed by TRAGUIN.'
                ),
                [
                    'shopping: for local souvenirs or famous Hyderabadi biscuits. Your private luxury transport will then drive you',
                    'Transfers Included: Private luxury airport drop-off.',
                    'Meals Included: Sumptuous Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Mercure KCP / Lemon Tree Premier Hotel City Grand',
                'Telangana',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: Mercure KCP / Lemon Tree Premier Hotel City Grand',
            ),
            _hotel(
                'Radisson Blu Plaza / Novotel Airport Sitara Luxury Hotel (Ramoji) MAPAI (Breakfast & Dinner)',
                'Telangana',
                '5N',
                'Premium',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: Radisson Blu Plaza / Novotel Airport Sitara Luxury Hotel (Ramoji) MAPAI (Breakfast & Dinner)',
            ),
            _hotel(
                'ITC Kakatiya / Park Hyatt Hyderabad Tara Hotel / Custom Premium Suite MAPAI + Elevated Amenities',
                'Telangana',
                '5N',
                'Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                3,
                description='OPTION 03 – LUXURY: ITC Kakatiya / Park Hyatt Hyderabad Tara Hotel / Custom Premium Suite MAPAI + Elevated Amenities',
            ),
            _hotel(
                'Taj Falaknuma Palace (Royal Suite) VVIP Private Luxury Villa Stay Bespoke Royal Signature Dinner',
                'Telangana',
                '5N',
                'Ultra Luxury',
                'Premium Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: Taj Falaknuma Palace (Royal Suite) VVIP Private Luxury Villa Stay Bespoke Royal Signature Dinner',
            )
        ],
        inclusions=[
            _inc_included('Premium Stays: Luxury accommodations as per selected tier category.', 1),
            _inc_included('Luxury Transportation: All transfers & sightseeing in a private AC vehicle.', 2),
            _inc_included('Curated Meal Plan: Daily lavish breakfasts and gourmet buffet dinners.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience manager on call.', 4),
            _inc_included('Welcome Amenities: Personalized family travel kit and refreshments on arrival.', 5),
            _inc_included('Complimentary Experience: Private sunset boat cruise tickets at Hussain Sagar.', 6),
            _inc_excluded('Airfare, domestic flights, or interstate train tickets.', 7),
            _inc_excluded('Sahas adventure sport fees or special camera permits.', 8),
            _inc_excluded('Monument entry tickets, local guides, and audio gear.', 9),
            _inc_excluded('Personal expenses such as laundry, liquor, and tips.', 10),
        ],
    )
    return package, itinerary

TELANGANA_DOMESTIC_BUILDERS = [
    build_tg_001,
    build_tg_002,
    build_tg_003,
    build_tg_004,
    build_tg_005,
    build_tg_006,
    build_tg_007,
    build_tg_008,
    build_tg_009,
    build_tg_010,
]
