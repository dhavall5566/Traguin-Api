"""Builder functions for ID-001 through ID-020 Bali/Indonesia international packages."""

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

BALI_SLUG = "bali"


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


def build_id_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-001'
    tour_code = 'TRAGUIN-BALI-001'
    title = 'Premium Bali Honeymoon'
    duration = '05 Nights / 06 Days'
    slug = 'id-001-premium-bali-honeymoon'
    itin_slug = 'id-001-premium-bali-honeymoon-itinerary'
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
            _ph('Serial code ID-001 | TRAGUIN tour code TRAGUIN-BALI-001', 1),
            _ph('Country: Bali, Indonesia | Category: Honeymoon', 2),
            _ph('Destinations: Bali | Duration: 5N/6D', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Honeymoon'],
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
        tagline='Premium Bali Honeymoon',
        overview='nchanting journey with a TRAGUIN curated experience. This luxury Bali holiday is designed to provide intimate moments, breathtaking landscapes, and premium stays. From the lush jungles of Ubud to the romantic sunsets of Uluwatu, every detail is crafted for an unforgettable romantic escape. DESTINATION HIGHLIGHTS Experience the best Bali honeymoon with its scenic beauty and iconic attractions. Bali is renowned for its vibrant culture, top tourist places like the Sacred Monkey Forest and Uluwatu Temple, and exclusive experiences like private villa dining. It is undoubtedly a premium Bali experience that offers the perfect blend of relaxation and adventure. DAY WISE ITINERARY\n\nTOUR OVERVIEW\nEmbark on an enchanting journey with a TRAGUIN curated experience. This luxury Bali holiday is designed to provide intimate moments, breathtaking landscapes, and premium stays. From the lush jungles of Ubud to the romantic sunsets of Uluwatu, every detail is crafted for an unforgettable romantic escape. DESTINATION HIGHLIGHTS Experience the best Bali honeymoon with its scenic beauty and iconic attractions. Bali is renowned for its vibrant culture, top tourist places like the Sacred Monkey Forest and Uluwatu Temple, and exclusive experiences like private villa dining. It is undoubtedly a premium Bali experience that offers the perfect blend of relaxation and adventure. DAY WISE ITINERARY',
        seo_title='ID-001 | Premium Bali Honeymoon | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Bali package (ID-001 / TRAGUIN-BALI-001): Bali | Duration: 5N/6D with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI - THE ROMANTIC BEGINNING', 1),
            _ih('Day 02: UBUD - CULTURAL IMMERSION', 2),
            _ih('Day 03: UBUD TO SEMINYAK - SCENIC TRANSFER', 3),
            _ih('Day 04: SEMINYAK - BEACH BLISS', 4),
            _ih('Day 05: ULUWATU - SUNSET ROMANCE', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI - THE ROMANTIC BEGINNING',
                (
                    'Arrive at Denpasar Airport and receive a warm TRAGUIN welcome. Transfer to your handpicked hotel in Ubud. Enjoy a candlelit dinner to start your romantic journey. Overnight: Ubud | Meals: Dinner'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'UBUD - CULTURAL IMMERSION',
                (
                    'Visit the Tegalalang Rice Terraces and the Sacred Monkey Forest. Immerse yourselves in the culture of Bali with curated experiences in local markets. Overnight: Ubud | Meals: Breakfast, Dinner'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'UBUD TO SEMINYAK - SCENIC TRANSFER',
                (
                    'Travel to Seminyak, exploring waterfalls along the way. Enjoy the scenic beauty of Bali’s coast. Overnight: Seminyak | Meals: Breakfast, Dinner'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'SEMINYAK - BEACH BLISS',
                (
                    "Relax at premium beach clubs or indulge in a couple's spa treatment. Enjoy the vibrant Overnight: Seminyak | Meals: Breakfast, Dinner"
                ),
                [
                    'shopping: and cafe culture.',
                ],
            ),
            _day(
                5,
                'ULUWATU - SUNSET ROMANCE',
                (
                    'Visit the iconic Uluwatu Temple. Witness the mesmerizing Kecak Fire Dance at sunset, one of the top tourist places in Bali. Overnight: Uluwatu/Seminyak | Meals: Breakfast, Dinner'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Enjoy breakfast before your transfer to the airport. TRAGUIN ensures a seamless departure after your unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Bali | Duration: 5N/6D',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Bali | Duration: 5N/6D',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Bali | Duration: 5N/6D',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Bali | Duration: 5N/6D',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('5 Nights premium accommodation', 1),
            _inc_included('Daily breakfast and romantic dinners', 2),
            _inc_included('Private luxury airport transfers', 3),
            _inc_excluded('International airfare and Indonesia visa on arrival fees', 4),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 5),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 6),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 7),
        ],
    )
    return package, itinerary

def build_id_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-002'
    tour_code = 'TRAGUIN-BALI-002'
    title = 'Bali Ubud Love Escape'
    duration = '05 Nights / 06 Days'
    slug = 'id-002-bali-ubud-love-escape'
    itin_slug = 'id-002-bali-ubud-love-escape-itinerary'
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
            _ph('Serial code ID-002 | TRAGUIN tour code TRAGUIN-BALI-002', 1),
            _ph('Country: Bali, Indonesia | Category: Honeymoon', 2),
            _ph('Destinations: Ubud, Bali | Duration: 5N/6D', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
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
        tagline='Bali Ubud Love Escape',
        overview='Ubud – The Heart of Romantic Bali 05 Nights / 06 Days ITINERARY SUMMARY Serial Code: ID-002 | Category: Honeymoon Destinations Covered: Ubud, Bali | Duration: 5N/6D\n\nTOUR OVERVIEW\nEscape to the serene landscapes of Ubud with this TRAGUIN curated honeymoon experience. Our Ubud Love Escape package offers luxury stays nestled in lush tropical jungles, providing a tranquil and romantic setting for your premium Bali holiday. From private villa experiences to intimate cultural tours, TRAGUIN ensures your time in Ubud is filled with unforgettable memories. DAY WISE ITINERARY',
        seo_title='ID-002 | Bali Ubud Love Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Bali package (ID-002 / TRAGUIN-BALI-002): Ubud, Bali | Duration: 5N/6D with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN UBUD - A DREAMY WELCOME', 1),
            _ih('Day 02: UBUD - NATURE’S EMBRACE', 2),
            _ih('Day 03: UBUD - WELLNESS & RELAXATION', 3),
            _ih('Day 04: UBUD - CULTURAL EXPLORATION', 4),
            _ih('Day 05: UBUD - WATERFALL ADVENTURE', 5),
            _ih('Day 06: FAREWELL BALI', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN UBUD - A DREAMY WELCOME',
                (
                    'Arrive in Bali and take a private transfer to your handpicked hotel in the lush heart of Ubud. Enjoy a relaxing evening with a floral bath and a romantic dinner setup by TRAGUIN experts. Overnight: Luxury Villa, Ubud | Meals: Dinner'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'UBUD - NATURE’S EMBRACE',
                (
                    'Explore the iconic Tegalalang Rice Terraces and the Sacred Monkey Forest. Experience scenic beauty and take photos at the most popular Instagram spots in Ubud. Overnight: Ubud | Meals: Breakfast, Dinner'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'UBUD - WELLNESS & RELAXATION',
                (
                    'Indulge in a couple’s spa retreat. TRAGUIN recommends a traditional Balinese massage in a jungle-view setting. Spend the evening at a boutique cafe in downtown Ubud. Overnight: Ubud | Meals: Breakfast, Dinner'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'UBUD - CULTURAL EXPLORATION',
                (
                    'Visit the Ubud Art Market for local souvenirs. Participate in a private cooking class to learn the flavors of Bali—another exclusive experience curated by TRAGUIN. Overnight: Ubud | Meals: Breakfast, Dinner'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'UBUD - WATERFALL ADVENTURE',
                (
                    'Discover the hidden gems of Ubud, including the stunning Tegenungan Waterfall. Enjoy a final romantic evening with a private dinner under the stars. Overnight: Ubud | Meals: Breakfast, Dinner'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'FAREWELL BALI',
                (
                    'Enjoy a leisurely breakfast before your private transfer to the airport. TRAGUIN ensures a seamless end to your perfect Ubud Love Escape.'
                ),
                [
                    'Meals: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Ubud, Bali | Duration: 5N/6D',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Ubud, Bali | Duration: 5N/6D',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Ubud, Bali | Duration: 5N/6D',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Ubud, Bali | Duration: 5N/6D',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('5 Nights luxury villa accommodation in Ubud', 1),
            _inc_included('Daily breakfast and romantic dinners', 2),
            _inc_included('Private luxury transfers', 3),
            _inc_excluded('International airfare and Indonesia visa on arrival fees', 4),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 5),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 6),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 7),
        ],
    )
    return package, itinerary

def build_id_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-005'
    tour_code = 'TRAGUIN-BALI-PREMIUM-005'
    title = 'Premium Bali Family Tour'
    duration = '07 Nights / 08 Days'
    slug = 'id-005-premium-bali-family-tour'
    itin_slug = 'id-005-premium-bali-itinerary'
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
            _ph('Serial code ID-005 | TRAGUIN tour code TRAGUIN-BALI-PREMIUM-005', 1),
            _ph('Country: Bali, Indonesia | Category: Family Luxury DURATION: 07 Nights / 08 Days', 2),
            _ph('Destinations: Ubud • Kuta • Seminyak •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
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
        tagline='Premium Bali Family Tour',
        overview="Ubud (3N) • Kuta/Seminyak (4N) with Nusa Penida Day Cruise 07 Nights / 08 Days Immersive Tropical Luxury Welcome to the Ultimate Bali Family Tour, a majestic journey meticulously woven by TRAGUIN to transport your loved ones into a realm of transcendent tropical beauty. Bali, affectionately known as the Island of the Gods, seamlessly blends pristine coastal luxury with rich cultural heritage. This Luxury Bali Holiday is engineered to provide premium stays, breathtaking landscapes, and curated experiences that transform moments into unforgettable memories. Let us guide you through mystical emerald rice terraces, iconic sea temples, and exclusive experiences designed for multi-generational families looking for the finest Bali Sightseeing.\n\nTOUR OVERVIEW\nThis customized Best Bali Tour Package is curated exclusively for discerning families who refuse to compromise on comfort, privacy, and authentic cultural immersion. Travel Framework: Fully Independent Travel (FIT) with private logistics. Vehicle Deployment: Premium Air-Conditioned Private MPV (Toyota Alphard or Innova Premium) with professional English-speaking guide-cum-driver throughout the itinerary. Meal Blueprint: Daily buffet breakfast at your handpicked hotels, authentic local organic lunches during tours, and premium curated dinners. Route Mapping: Denpasar Airport → Ubud (Cultural Heart) → Nusa Penida (Iconic Islet) → Seminyak/Kuta (Coastal Luxury) → Denpasar Airport. TRAGUIN Curated Experience Note: Your family's satisfaction is backed by our 24/7 Premium Concierge Helpdesk. From fast-tracked airport immigration clearances to premium front-row access at major attractions, every element is overseen by TRAGUIN experts to guarantee absolute relaxation.\n\nWHY CHOOSE TRAGUIN BALI PACKAGES?\nBali remains the ultimate benchmark for a premium global vacation. Our Bali Family Tour packages carefully balanced high-octane adventure with restorative wellness, making it perfect for children, parents, and grandparents alike. From the world-famous cultural canvas of Ubud to the vibrant sunset lounges of Seminyak, this destination boasts the Top Tourist Places in Bali that consistently dominate global tourism charts. Most Searched Experiences & Instagram Locations: This itinerary grants you direct access to the most popular Instagram locations including the legendary Bali Swing, Kelingking T-Rex Cliff, and Tanah Lot at sunset. Immerse your family in authentic Balinese culture with private cooking classes, sacred purification rituals, and premium shopping excursions at local markets famed for exquisite silver jewelry, handcrafted woodcrafts, and organic silks. The Best Time to Visit Bali: While Bali is a beautiful year-round paradise, the dry season between April and October provides brilliant azure skies and cool ocean breezes, ideal for exploring the island’s scenic beauty, marine life sanctuaries, and breathtaking landscapes. DAY-BY-DAY CURATED ITINERARY",
        seo_title='ID-005 | Premium Bali Family Tour | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Bali package (ID-005 / TRAGUIN-BALI-PREMIUM-005): Ubud • Kuta • Seminyak • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI & TRANSFER TO CULTURAL HEART OF UBUD', 1),
            _ih('Day 02: UBUD CULTURAL IMMERSION: REVEALING THE MYSTICAL EMERALD', 2),
            _ih('Day 03: KINTAMANI VOLCANO MAJESTY & SACRED PURIFICATION RITUALS', 3),
            _ih('Day 04: THE ICONIC TANAH LOT TRANSITION TO REFINED COASTAL LUXURY', 4),
            _ih('Day 05: NUSA PENIDA EXCLUSIVE CRUISE: DISCOVERING UNTOUCHED', 5),
            _ih('Day 06: SOUTHERN BALI MAJESTY: ULUWATU CLIFF TEMPLE & FIRE DANCE', 6),
            _ih('Day 07: LEISURE RESORT SPA IMMERSION & HIGH-END SHOPPING', 7),
            _ih('Day 08: FAREWELL BALI: MEMORIES BEYOND DESTINATIONS', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI & TRANSFER TO CULTURAL HEART OF UBUD',
                (
                    'Arrive at Ngurah Rai International Airport (DPS) where your family will be greeted with a warm Balinese welcome by your private TRAGUIN representative. Enjoy a refreshing traditional cold towel and fresh flower garlands before being escorted to your premium private vehicle. As you embark on your scenic drive toward Ubud, the cultural epicentre of Bali, marvel at how the bustling coastline shifts into tranquil countryside punctuated by historic stone temples and artistic enclaves. Upon reaching your premium handpicked luxury resort in Ubud, complete your seamless private check-in and relax in your villa overlooking lush valleys. Sightseeing Included: Airport Meet & Greet, Ubud Scenic Transfer, Private Resort Orientation. Evening Experience: Relax at leisure within the resort premises or enjoy a stroll through the artsy lanes of Ubud town.'
                ),
                [
                    'Overnight Stay: Premium Handpicked Resort Villa in Ubud.',
                    'Meals Included: Welcome Drink & Premium Curated Dinner.',
                ],
            ),
            _day(
                2,
                'UBUD CULTURAL IMMERSION: REVEALING THE MYSTICAL EMERALD',
                (
                    "RICE TERRACES Awaken to the soothing sounds of the Ayung River valley. Today's immersive experience explores the heart of Balinese heritage. Our first stop is the breathtaking Tegalalang Rice Terraces, a UNESCO World Heritage site showcasing the traditional 'Subak' cooperative irrigation system. Here, your family can participate in an exclusive private flight on the famous Bali Swing, capturing unforgettable memories against a backdrop of deep green glasses. Next, walk through the sacred Ubud Monkey Forest, a natural sanctuary where towering banyan trees shade historic temple ruins and playful long-tailed macaques roam. Indulge in an organic farm- to-table lunch overlooking the vibrant landscape. Sightseeing Included: Tegalalang Rice Terraces, Private Bali Swing Experience, Sacred Monkey Forest, Ubud Royal Palace. Optional Activities: Private white-water rafting on the pristine Ayung River with gourmet lunch. Evening Experience: Gourmet dining at an award-winning fine dining restaurant in Ubud serving Balinese fusion cuisine."
                ),
                [
                    'Overnight Stay: Premium Handpicked Resort Villa in Ubud.',
                    'Meals Included: Breakfast & Gourmet Lunch.',
                ],
            ),
            _day(
                3,
                'KINTAMANI VOLCANO MAJESTY & SACRED PURIFICATION RITUALS',
                (
                    "Embark on an extraordinary journey to the highlands of Kintamani. As you ascend, the air becomes crisp and reveals the magnificent panoramic views of Mount Batur, an active volcano, and its tranquil crescent lake. Enjoy a premium lunch at a private viewing deck, appreciating the scenic beauty that defines northeastern Bali. In the afternoon, descend to the holy spring water temple of Pura Tirta Empul. Participate in an optional, deeply moving traditional purification ritual where your family can step into the crystal-clear pools fed by mountain springs—a cornerstone of Balinese spiritual culture. Conclude the day with a visit to local coffee and spice plantations to savor premium Luwak coffee. Sightseeing Included: Kintamani Volcano Viewpoint, Tirta Empul Holy Water Temple, Local Spice & Premium Coffee Plantations. Optional Activities: Traditional Balinese family woodcarving or batik painting workshop. Evening Experience: Relaxing evening at Ubud's artisan cafes or custom spa therapies within your private luxury resort."
                ),
                [
                    'Overnight Stay: Premium Handpicked Resort Villa in Ubud.',
                    'Meals Included: Breakfast & Lunch at Volcano-View Restaurant.',
                ],
            ),
            _day(
                4,
                'THE ICONIC TANAH LOT TRANSITION TO REFINED COASTAL LUXURY',
                (
                    'Check out from your serene Ubud villa as we smoothly transition your family to the vibrant southern coast of Bali. En route, experience one of the most celebrated highlights of any Bali Sightseeing tour: the mystical Tanah Lot Temple. Perched on a craggy wave-swept offshore rock, this iconic ancient sea shrine is a masterpiece of natural architecture. Watch the Indian Ocean waves dramatically crash against its base. After capturing pristine family photos at this legendary Instagram location, arrive at your ultra-luxury beachfront resort in Seminyak/Kuta. Transition seamlessly to a world of coastal indulgence, soft sandy beaches, and premium oceanfront hospitality. Sightseeing Included: Tanah Lot Sea Temple, Southern Coastal Highlights, Premium Seminyak Orientation. Optional Activities: Surfing lessons for kids and teenagers at Kuta Beach under professional, licensed instruction. Evening Experience: Vibrant sunset watching from an exclusive, pre-booked cabana at a premium Seminyak beach club.'
                ),
                [
                    'Overnight Stay: Luxury Beachfront Resort in Seminyak / Kuta.',
                    'Meals Included: Breakfast & Premium Seafood Dinner.',
                ],
            ),
            _day(
                5,
                'NUSA PENIDA EXCLUSIVE CRUISE: DISCOVERING UNTOUCHED',
                (
                    "PARADISE Prepare for an exhilarating highlight of your Luxury Bali Holiday. Board a premium high-speed catamaran for a private day cruise to the pristine island of Nusa Penida. As you cross the sparkling Badung Strait, the dramatic limestone cliffs of the island emerge from the azure water. Upon arrival, step directly into a postcard view as you visit Kelingking Beach, world-famed for its T-Rex shaped cliffside rock formation. Walk along the ridge to behold the breathtaking landscapes below. Continue your adventure to the natural rock lagoon of Angel's Billabong and the collapsed sea cave known as Broken Beach, treating your family to some of the rarest geological wonders in Southeast Asia. Sightseeing Included: Nusa Penida Catamaran Cruise, Kelingking Beach, Angel's Billabong, Broken Beach. Optional Activities: Snorkeling with giant manta rays at Manta Point, featuring pristine coral gardens. Evening Experience: Return cruise to the main island followed by an elegant, relaxing multi-course dinner at the resort."
                ),
                [
                    'Overnight Stay: Luxury Beachfront Resort in Seminyak / Kuta.',
                    'Meals Included: Breakfast & International Buffet Lunch on the Cruise Catamaran.',
                ],
            ),
            _day(
                6,
                'SOUTHERN BALI MAJESTY: ULUWATU CLIFF TEMPLE & FIRE DANCE',
                (
                    'Enjoy a slow, late breakfast and spend your morning relaxing poolside or walking along the soft sandy beaches. In the afternoon, your private guide will escort you to the southernmost tip of the island to explore the majestic Uluwatu Temple. Perched precariously on a sheer cliff dropping 70 meters into the roaring Indian Ocean, this temple offers unmatched scenic beauty. As the sun begins to melt into the horizon, take your reserved premium seats for the spellbinding Kecak Fire Dance performance. This dramatic sunset showcase tells the ancient Ramayana epic through hypnotic vocal chanting, blazing fires, and intricate choreography against an open-ocean backdrop. Sightseeing Included: Uluwatu Cliff Temple, Premium Kecak Fire Dance Show, Jimbaran Bay Coastal Tour. Optional Activities: Pre-sunset professional family photoshoot on the secluded cliffs of Uluwatu. Evening Experience: An unforgettable candlelit private family dinner directly on the sand at Jimbaran Bay, savoring grilled lobster and fresh catches.'
                ),
                [
                    'Overnight Stay: Luxury Beachfront Resort in Seminyak / Kuta.',
                    'Meals Included: Breakfast & Exclusive Jimbaran Beach Seafood Feast.',
                ],
            ),
            _day(
                7,
                'LEISURE RESORT SPA IMMERSION & HIGH-END SHOPPING',
                (
                    "EXCURSION Dedicated entirely to family leisure and sophisticated retail indulgence, today allows you to pace your day exactly as you please. Spend your morning pampering your senses with a complimentary traditional Balinese deep-tissue massage at your resort's world-class spa. In the afternoon, your private vehicle is at your disposal for a curated shopping tour of Seminyak's luxury boutiques, high-end art galleries, and upscale lifestyle centers. Hunt for high-quality souvenirs, elegant designer resort wear, and rare antique treasures. Gather tonight for a celebratory farewell dinner organized by TRAGUIN to commemorate your tropical journey. Sightseeing Included: Seminyak Luxury Retail Tour, Beachfront Leisure Walk. Optional Activities: Private Balinese culinary masterclass hosted by a celebrity chef at an organic estate. Evening Experience: Grand Farewell Dinner at a fine-dining Indonesian heritage estate with traditional music."
                ),
                [
                    'Overnight Stay: Luxury Beachfront Resort in Seminyak / Kuta.',
                    'Meals Included: Breakfast & Grand Farewell Dinner.',
                ],
            ),
            _day(
                8,
                'FAREWELL BALI: MEMORIES BEYOND DESTINATIONS',
                (
                    'Savor your final gourmet breakfast at your luxurious resort while looking out at the turquoise ocean waves. Enjoy a relaxed morning completing your packing and gathering your premium souvenirs. Your private chauffeur will arrive at the scheduled time to transfer your family seamlessly back to Ngurah Rai International Airport. As you check in for your return flight home, carry with you the radiant warmth of the Balinese sun, the laughter of shared family adventures, and a treasury of unforgettable memories beautifully crafted by the destination experts at TRAGUIN. Sightseeing Included: Airport Departure Private Transfer. Optional Activities: Airport VIP Executive Lounge Access booking for stress-free flight preparation. Evening Experience: Transatlantic/International homeward bound flight.'
                ),
                [
                    'Overnight Stay: In-Flight / Home.',
                    'Meals Included: Gourmet Buffet Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Alaya Resort Ubud',
                'Bali',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Alaya Resort Ubud',
            ),
            _hotel(
                'Maya Ubud Resort & Spa',
                'Bali',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Maya Ubud Resort & Spa',
            ),
            _hotel(
                'The Kayon Resort by Pramana',
                'Bali',
                '7N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Kayon Resort by Pramana',
            ),
            _hotel(
                'Mandapa, a Ritz-Carlton Reserve',
                'Bali',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandapa, a Ritz-Carlton Reserve',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Bali', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven MPV', 2),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 3),
            _inc_excluded('TRAGUIN Package Inclusions', 4),
        ],
    )
    return package, itinerary

def build_id_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-006'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Bali Girls Escape'
    duration = '05 Nights / 06 Days'
    slug = 'id-006-bali-girls-escape'
    itin_slug = 'id-006-bali-girls-escape-itinerary'
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
            _ph('Serial code ID-006 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Female Only / Bali Girls Escape DURATION: 05 Nights / 06 Days KEY', 2),
            _ph("Destinations: Seminyak • Ubud • Canggu • Uluwatu RECOMMENDED FOR: Bachelorette • Friends' Getaway IDEAL SEASON: April to October (Dry & Sunny) VIP CONCIERGE: 24/7 Dedicated Support Included BALI GIRLS ESCAPE Seminyak Trendy Coasts (3N) & Ubud Rainforest Sanctuary (2N) A CURATED LUXURY HOLIDAY EXPERIENCE BY TRAGUIN Welcome to your bespoke Bali Girls Escape • an ultra-luxury journey exclusively arranged by TRAGUIN for discerning all-female travel collectives. This 5-Night • 6-Day tropical retreat beautifully balances chic lifestyle beach clubs • premium boutique shopping • dramatic cliffside sunsets • and soulful rainforest wellness. Travel in flawless style with private luxury vehicles • curated culinary stops • and handpicked hotel sanctuaries tailored precisely to your preferences. Relax • laugh • and celebrate your bond while our dedicated concierge helpdesk takes care of every detail behind the scenes. TOUR OVERVIEW This premium Best Bali Tour Package is tailored exclusively as a private • female-only retreat that brings together elite island logistics with Bali's trendiest social and relaxation spots. Travel Type: Private Boutique Group / Fully Independent Travel (FIT).", 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury'],
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
        tagline='Bali Girls Escape',
        overview="TOUR OVERVIEW\nThis premium Best Bali Tour Package is tailored exclusively as a private, female-only retreat that brings together elite island logistics with Bali's trendiest social and relaxation spots. Travel Type: Private Boutique Group / Fully Independent Travel (FIT). • Bali Girls Escape (ID-006) 1 Vehicle Deployment: Dedicated Premium Private Luxury MPV with a professional, English-speaking tourist chauffeur. Meal Blueprint: Sumptuous daily breakfasts (including a signature floating villa pool experience), custom culinary stops, and oceanfront dinners. Route Sequence: Denpasar Airport → Seminyak Coastal Hub → Canggu Lifestyle Escapes → Uluwatu Cliffs → Ubud Rainforest & Cultural Oasis → Denpasar Airport. TRAGUIN Lifestyle Assurance: Skip-the-line entries, pre-arranged VIP daybeds at iconic beach clubs, and tailored spa times are seamlessly secured in advance for your ultimate peace of mind.\n\nWHY BOOK THIS LUXURY BALI HOLIDAY?\nA sophisticated women's getaway requires perfect execution, premium comfort, and gorgeous visual elements. Our Bali Girls Escape package showcases the absolute Top Tourist Places in Bali, curated alongside highly sought-after Instagram locations to ensure premium comfort, complete safety, and continuous lifestyle inspiration. From the magnificent seaside scenery of Tanah Lot and Uluwatu to the high-energy beach clubs of Canggu, you will experience the best time to visit Bali in unparalleled style. Indulge in elite retail therapy across Seminyak's luxury designer rows, design your own souvenirs during private artisan workshops, and experience timeless wellness treatments inside rainforest valleys. DAY-BY-DAY CURATED ITINERARY",
        seo_title='ID-006 | Bali Girls Escape | TRAGUIN',
        seo_description="Premium 05 Nights / 06 Days Bali package (ID-006 / TRAGUIN-BALI-000): Seminyak • Ubud • Canggu • Uluwatu RECOMMENDED FOR: Bachelorette •  Friends' Getaway IDEAL SEASON: A with 4-tier handpicked accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • ELITE WELCOME TO SEMINYAK COASTAL LUXURY', 1),
            _ih('Day 02: CANGGU LIFESTYLE: BOUTIQUE SHOPPING & VIP BEACH CLUB', 2),
            _ih('Day 03: ULUWATU CLIFFSIDE MAJESTY & DRAMATIC SUNSET PANORAMIC DINING', 3),
            _ih('Day 04: TANAH LOT SEA SHRINE • JOURNEY TO THE JUNGLE SANCTUARY OF UBUD', 4),
            _ih('Day 05: INSTAGRAM GLAMOUR: TEGALALANG RICE TERRACES & PRIVATE BALI', 5),
            _ih('Day 06: SOULFUL FAREWELL • UNFORGETTABLE MEMORIES BEYOND', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • ELITE WELCOME TO SEMINYAK COASTAL LUXURY',
                (
                    'Begin your luxurious escape the moment you step off your plane at Ngurah Rai International Airport (DPS). Your private TRAGUIN luxury chauffeur awaits in the arrivals terminal with beautiful fresh flower garlands and cold mineral waters. Relax inside your premium private vehicle as you glide smoothly to your handpicked hotel suite or private pool villa in Seminyak—the culinary and chic fashion epicenter of Bali. After checking in, spend a relaxed afternoon unpacking and exploring. In the evening, regroup for a wonderful welcome sunset cocktail at a premier beachfront lounge, toasting to an incredible getaway ahead. Sightseeing & Logistics: VIP Airport Meet & Greet, Private Luxury Transfer, Accommodation Orientation. Evening Highlight:Sunset drinks and tapas at an upscale oceanfront lounge in Seminyak. • Bali Girls Escape (ID-006) 2'
                ),
                [
                    'Overnight Stay: Premium Handpicked Luxury Resort / Private Pool Villa in Seminyak.',
                    'Meals Included: Welcome Refreshments & Curated Welcome Dinner.',
                ],
            ),
            _day(
                2,
                'CANGGU LIFESTYLE: BOUTIQUE SHOPPING & VIP BEACH CLUB',
                (
                    'EXPERIENCE Enjoy a delicious gourmet breakfast before your private chauffeur transfers your group to the neighboring trendy coastal town of Canggu. Known globally for its vibrant energy, aesthetic cafes, and independent fashion boutiques, Canggu is a haven for high-end retail therapy. Your guide will escort you through premium custom swimwear studios, luxury organic linen brands, and local designer shops. At noon, step into an ultra-exclusive, pre- booked VIP oceanfront cabana at one of Bali’s world-famous beach clubs. Spend the afternoon lounging poolside, drinking artisan mocktails, and enjoying beautiful ocean breezes. Sightseeing & Logistics: Canggu Guided Shopping Tour, Premium Lifestyle Exploration, Pre-booked Daybed Access. Optional Add-ons:Private cocktail masterclass hosted by an award-winning resort mixologist. Evening Highlight:Dinner at a highly-vetted botanical glasshouse restaurant, celebrated for its gourmet cuisine and stunning decor.'
                ),
                [
                    'Overnight Stay: Premium Handpicked Luxury Resort / Private Pool Villa in Seminyak.',
                    'Meals Included: Breakfast & VIP Beach Club Lunch Platter.',
                ],
            ),
            _day(
                3,
                'ULUWATU CLIFFSIDE MAJESTY & DRAMATIC SUNSET PANORAMIC DINING',
                (
                    'Savor a relaxing morning swimming or visiting the spa at your resort. In the afternoon, journey south along the coast to the dramatic sea cliffs of Uluwatu, a key highlight of Bali Sightseeing. Perched 70 meters above the Indian Ocean, the historical Uluwatu Temple offers jaw-dropping panoramic views and deep cultural heritage. Stroll the scenic cliffside walkways for incredible group photographs. Afterward, escape to an elite cliff-hanging restaurant to watch a pristine Bali sunset over the water while enjoying fresh, expertly prepared seafood dishes. Sightseeing & Logistics: Uluwatu Cliff Temple Entry, Guided Coastal Panoramic Tour, Sunset Viewing. Optional Add-ons:Premium seating for the traditional cliffside Kecak Fire Dance performance. Evening Highlight:Candlelit fine dining at an exclusive cliff-edge restaurant with live acoustic music. • Bali Girls Escape (ID-006) 3'
                ),
                [
                    'Overnight Stay: Premium Handpicked Luxury Resort / Private Pool Villa in Seminyak.',
                    'Meals Included: Breakfast & Luxury Seafood Sunset Dinner.',
                ],
            ),
            _day(
                4,
                'TANAH LOT SEA SHRINE • JOURNEY TO THE JUNGLE SANCTUARY OF UBUD',
                (
                    'Check out from your coastal resort and begin your journey into the lush emerald interior of Ubud. En route, experience Tanah Lot Temple, an iconic offshore wave-swept rock shrine that stands as one of the most famous sights in Bali. After capturing magnificent photos, watch the landscape change into rolling hills, deep river valleys, and pristine forests as you enter Ubud. Check into your ultra-luxury rainforest resort. In the afternoon, indulge in an incredible immersive experience: a lavish, pre-arranged Balinese flower-petal bath prepared inside your villa for total physical and mental relaxation. Sightseeing & Logistics: Tanah Lot Temple Visit, Scenic Ubud Interior Transfer, Luxury Villa Check-In. Optional Add-ons:A private sound healing or meditation session at an elite wellness pavilion. Evening Highlight:An organic farm-to-table dinner served by the valley rim under a canopy of stars.'
                ),
                [
                    'Overnight Stay: Ultra-Luxury Rainforest Resort Villa in Ubud.',
                    'Meals Included: Breakfast & Balinese Luxury Fusion Dinner.',
                ],
            ),
            _day(
                5,
                'INSTAGRAM GLAMOUR: TEGALALANG RICE TERRACES & PRIVATE BALI',
                (
                    "SWING Dress in your finest flowing resort wear for a morning dedicated to iconic island visuals. Visit the breathtaking Tegalalang Rice Terraces early to catch the morning sunbeams filtering through the palms. Enjoy private VIP access to the premier Bali Swing, gliding out over the emerald agricultural valleys for breathtaking, professional photographs. Afterward, visit a hidden, pristine jungle waterfall for a refreshing break, followed by a stroll through Ubud's traditional artisan markets. Celebrate your final evening with a grand TRAGUIN Signature Celebration Dinner, raising a glass to lifelong friendships and unforgettable memories. Sightseeing & Logistics: Tegalalang Terraces, Private Premium Bali Swing, Hidden Waterfall, Ubud Artisan Market. Optional Add-ons:A private silver jewelry-making class to design matching custom keepsake rings. Evening Highlight:Grand Farewell Celebration Feast featuring fine gastronomy and artisanal custom cocktails. • Bali Girls Escape (ID-006) 4"
                ),
                [
                    'Overnight Stay: Ultra-Luxury Rainforest Resort Villa in Ubud.',
                    'Meals Included: Signature Floating Villa Breakfast & Premium Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'SOULFUL FAREWELL • UNFORGETTABLE MEMORIES BEYOND',
                (
                    'DESTINATIONS Wake up to the sounds of the jungle and enjoy a luxurious floating breakfast served right in your private villa infinity pool. Take this morning for last-minute relaxation, meditation, or a peaceful walk through the resort’s lush grounds. At the designated time, your private luxury vehicle and chauffeur will arrive to transfer your group seamlessly back to Ngurah Rai International Airport for your departure flight. Leave the Island of the Gods with radiant smiles, relaxed minds, and a collection of unforgettable memories meticulously brought to life by TRAGUIN. Sightseeing & Logistics: Private Airport Departure Logistics, Airport Transfer. Optional Add-ons:VIP Airport Lounge access pre-booking for an entirely stress-free departure experience. Evening Highlight:International flight homeward.'
                ),
                [
                    'Overnight Stay: In-Flight / Home.',
                    'Meals Included: Premium Floating or Buffet Resort Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'LUXURY Wina Holiday Villa Kuta / Seminyak',
                'Multi-city Bali',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — LUXURY Wina Holiday Villa Kuta / Seminyak',
            ),
            _hotel(
                'LUXURY Hotel Indigo Bali Seminyak Beach',
                'Multi-city Bali',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — LUXURY Hotel Indigo Bali Seminyak Beach',
            ),
            _hotel(
                'The Legian Seminyak, Bali',
                'Bali',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The Legian Seminyak, Bali',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Bali', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven MPV', 2),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 3),
            _inc_excluded('TRAGUIN Inclusions', 4),
        ],
    )
    return package, itinerary

def build_id_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-007'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Luxury Bali Retreat'
    duration = '06 Nights / 07 Days'
    slug = 'id-007-luxury-bali-retreat'
    itin_slug = 'id-007-luxury-bali-retreat-itinerary'
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
            _ph('Serial code ID-007 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Luxury / Ultra-Luxury Signature DURATION: 06 Nights / 07 Days KEY', 2),
            _ph("Destinations: Nusa Dua • Uluwatu • Ubud • Mount Batur RECOMMENDED FOR: Connoisseurs • Couples • Families IDEAL SEASON: April to October (Dry & Sunny) VIP CONCIERGE: 24/7 Dedicated Support Included LUXURY BALI RETREAT Exclusive Coastal Havens (3N) & Majestic Cultural Valleys (3N) A SIGNATURE HIGH-END HOLIDAY EXPERIENCE BY TRAGUIN Welcome to your bespoke Luxury Bali Retreat • an ultra-luxury journey exclusively crafted by TRAGUIN for discerning world travelers. This comprehensive 6-Night • 7-Day signature itinerary offers an extraordinary immersion into the Island of the Gods. Experience white-glove logistics • private helicopter transfers or luxury MPV transit • elite culinary journeys • and stays within the world's most acclaimed resort estates. From the tranquil exclusive beaches of Nusa Dua and majestic cliffs of Uluwatu to the spiritual heartbeat and emerald mist of Ubud • every single element is curated to transcend standard luxury. TOUR OVERVIEW This premium Best Bali Tour Package represents the peak of bespoke holiday planning • matching seamless private aviation and ground transit with unique cultural and culinary discoveries. Travel Type: Ultra-Luxury Private Guided FIT Experience.", 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Nature', 'Leisure'],
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
        tagline='Luxury Bali Retreat',
        overview="rivate luxury catamaran charter for a serene three-hour cruise along the pristine reef lagoons of Nusa Dua, offering snorkeling opportunities in crystal-clear waters. Return for an artisanal beachfront lunch. In the afternoon, your private guide will escort you to the dramatic Water Blow site, where powerful Indian Ocean waves crash spectacularly through narrow limestone crags. Spend the remaining afternoon relaxing inside a reserved premium private beach cabana with complimentary butler services at your disposal. Sightseeing & Logistics: Private Lagoon Cruise, Water Blow Guided Walk, Premium Beachfront Cabana Placement. Optional Add-ons:A 90-minute signature hot stone massage treatment inside the resort’s elite spa center. Evening Highlight:Intimate beachside dining featuring premium grilled lobsters and international wine pairing. Overnight Stay: Elite Handpicked Luxury Oceanfront Resort in Nusa Dua. Meals Included: Breakfast, Oceanfront Lunch, & Premium Beachside Dinner.\n\nTOUR OVERVIEW\nThis premium Best Bali Tour Package represents the peak of bespoke holiday planning, matching seamless private aviation and ground transit with unique cultural and culinary discoveries. Travel Type: Ultra-Luxury Private Guided FIT Experience. • Luxury Bali Retreat (ID-007) 1 Vehicle Deployment: Premium private luxury alphard or matching multi-purpose luxury vehicle with an expert, English-fluent tour ambassador. Meal Blueprint: Complete premium breakfast curation, fine gastronomy multi-course lunches, and iconic candlelit dinners. Route Sequence: Denpasar VIP Terminal → Nusa Dua Elite Enclave → Uluwatu Sea Cliffs → Ubud Cultural Hinterlands → Kintamani Volcanic Vistas → Denpasar Airport. TRAGUIN Privilege Access: Private temple viewings, skip-the-line VIP entry clearance, reservation access at world-ranked top restaurants, and bespoke spa therapies are pre-secured. DISCOVER THE TOP TOURIST PLACES IN BALI IN FLAWLESS COMFORT True luxury lies in the flawless integration of time, privacy, and exceptional comfort. Our Luxury Bali Retreat has been structured to introduce you to the absolute Top Tourist Places in Bali without the rush of commercial tourism. You will explore historic coastal sea temples, expansive terraced valleys, and serene highland volcanoes at the absolute best time to visit Bali. By blending the deep tranquility of Nusa Dua's turquoise lagoons with the vibrant artistry and mist-laden river valleys of Ubud, TRAGUIN invites you to rediscover island indulgence. Delight in immersive culinary classes inside heritage royal gardens, witness dramatic traditional arts with reserved VIP front-row seating, and find peace with curated holistic therapies overlooking pristine rainforest valleys. DAY-BY-DAY CURATED ITINERARY",
        seo_title='ID-007 | Luxury Bali Retreat | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Bali package (ID-007 / TRAGUIN-BALI-000): Nusa Dua • Uluwatu • Ubud • Mount Batur RECOMMENDED FOR: Connoisseurs •  Couples •  Families IDEAL S with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • ELITE VIP FAST-TRACK • NUSA DUA LUXURY REPOSE', 1),
            _ih('Day 02: EXCLUSIVE LAGOON CRUISE • PRIVATE WATER BLOW TOUR & BEACH', 2),
            _ih('Day 03: ULUWATU SEA SHRINE • MAJESTIC CLIFFS & THE VIP KECAK FIRE DANCE', 3),
            _ih("Day 04: HISTORIC TANAH LOT • TRANSFER INTO UBUD'S EMERALD VALLEY WALLED", 4),
            _ih('Day 05: KINTAMANI HIGHLANDS • MOUNT BATUR VISTAS & PRIVATE COFFEE ESTATE', 5),
            _ih('Day 06: TEGALALANG RICE COATINGS • PRIVATE SWING • HOLY WATER', 6),
            _ih('Day 07: FLOATING RESORT POOL BREAKFAST • SOULFUL BALI DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • ELITE VIP FAST-TRACK • NUSA DUA LUXURY REPOSE',
                (
                    'Your grand journey begins the moment your flight touches down at Ngurah Rai International Airport (DPS). Step directly into a luxury airport escort service with our fast-track VIP customs agent handling all immigration clearances seamlessly. Collect your luggage and meet your private TRAGUIN luxury chauffeur, stepping into an air-conditioned premium vehicle stocked with chilled towels, organic snacks, and vintage mineral waters. Drive to the exclusive luxury peninsula of Nusa Dua, entering your world-class beachfront resort estate. Spend a relaxed afternoon settling into your oceanfront suite, followed by an elegant multi-course coastal dinner overlooking the quiet, candlelit tides. Sightseeing & Logistics: VIP Fast-Track Airport Arrival, Private Luxury Chauffeur Transfer, Accommodation Orientation. Evening Highlight:Welcome dinner introducing fine contemporary Indonesian gastronomy at a beachfront pavilion. • Luxury Bali Retreat (ID-007) 2'
                ),
                [
                    'Overnight Stay: Elite Handpicked Luxury Oceanfront Resort in Nusa Dua.',
                    'Meals Included: Welcome Refreshments & Curated Welcome Dinner.',
                ],
            ),
            _day(
                2,
                'EXCLUSIVE LAGOON CRUISE • PRIVATE WATER BLOW TOUR & BEACH',
                (
                    'CABANA Awake to the sunrise over the ocean and enjoy a delightful gourmet breakfast. In the morning, embark on a private luxury catamaran charter for a serene three-hour cruise along the pristine reef lagoons of Nusa Dua, offering snorkeling opportunities in crystal-clear waters. Return for an artisanal beachfront lunch. In the afternoon, your private guide will escort you to the dramatic Water Blow site, where powerful Indian Ocean waves crash spectacularly through narrow limestone crags. Spend the remaining afternoon relaxing inside a reserved premium private beach cabana with complimentary butler services at your disposal. Sightseeing & Logistics: Private Lagoon Cruise, Water Blow Guided Walk, Premium Beachfront Cabana Placement. Optional Add-ons:A 90-minute signature hot stone massage treatment inside the resort’s elite spa center. Evening Highlight:Intimate beachside dining featuring premium grilled lobsters and international wine pairing.'
                ),
                [
                    'Overnight Stay: Elite Handpicked Luxury Oceanfront Resort in Nusa Dua.',
                    'Meals Included: Breakfast, Oceanfront Lunch, & Premium Beachside Dinner.',
                ],
            ),
            _day(
                3,
                'ULUWATU SEA SHRINE • MAJESTIC CLIFFS & THE VIP KECAK FIRE DANCE',
                (
                    'Enjoy a leisurely morning of relaxation by the pool or individual wellness activities. In the afternoon, journey south to the grand limestone cliffs of Uluwatu, a foundational pillar of any elite Bali Sightseeing tour. Perched dramatically 70 meters above crashing surf, the ancient Uluwatu Temple offers unforgettable expansive ocean views. Stroll along the historical pathways accompanied by your expert guide. As dusk settles, take your pre- reserved, front-row VIP seats at the cliffside amphitheater to witness the spellbinding Kecak Fire Dance performance set against a glorious, golden tropical sunset. Sightseeing & Logistics: Uluwatu Cliff Temple Entry, Private Expert-Guided Walk, VIP Amphitheater Seating. Optional Add-ons:A private sunset helicopter flight over the Uluwatu Peninsula before the cultural dance show. Evening Highlight:A magnificent multi-course dinner at an award-winning cliff-edge fine dining culinary venue. • Luxury Bali Retreat (ID-007) 3'
                ),
                [
                    'Overnight Stay: Elite Handpicked Luxury Oceanfront Resort in Nusa Dua.',
                    'Meals Included: Breakfast & Luxury Fine Dining Cliff Dinner.',
                ],
            ),
            _day(
                4,
                "HISTORIC TANAH LOT • TRANSFER INTO UBUD'S EMERALD VALLEY WALLED",
                (
                    'SANCTUARY Check out from your coastal paradise and travel toward the cultural heartlands of Bali. Your route stops at the world-renowned Tanah Lot Temple, a majestic, ancient offshore sea shrine wave-swept by tides and filled with spiritual history. Take incredible photographs from the private viewing terraces. Continue inland as the landscape transitions into endless emerald hills and deep, jungle river valleys. Arrive in Ubud and check into an ultra-luxury valley estate villa featuring an infinity pool suspended over the jungle canopy. Spend the evening enjoying the natural tranquility and sounds of the rainforest. Sightseeing & Logistics: Tanah Lot Temple Exclusive Access, Scenic Inland Luxury Drive, Valley Estate Villa Check-In. Optional Add-ons:Private sound bath relaxation therapy at an elite bamboo wellness pavilion in Ubud. Evening Highlight:A curated farm-to-table culinary degustation menu overlooking a misty valley canyon.'
                ),
                [
                    'Overnight Stay: Ultra-Luxury Rainforest Valley Private Pool Villa in Ubud.',
                    'Meals Included: Breakfast & Gourmet Valley Degustation Dinner.',
                ],
            ),
            _day(
                5,
                'KINTAMANI HIGHLANDS • MOUNT BATUR VISTAS & PRIVATE COFFEE ESTATE',
                (
                    'TOUR Set off today for the spectacular northern highlands of Kintamani. Witness the breathtaking, vast panorama of Mount Batur, an active volcano, and its shimmering caldera lake below. Enjoy an exceptional lunch at a luxury lookout establishment with pristine alpine breezes. Afterward, enjoy an exclusive private tour through an artisanal organic coffee estate hidden inside the volcanic hills, tasting rare varieties and learning traditional roasting methods. Return to Ubud for an evening of relaxation or custom boutique exploration across the central artisan lanes. Sightseeing & Logistics: Kintamani Volcano Panoramic Tour, Mount Batur Caldera Viewing, Private Coffee Estate Access. Optional Add-ons:A morning luxury 4x4 Jeep safari across the historic black lava fields of Mount Batur. Evening Highlight:An evening culinary experience at a highly acclaimed, top-ranked gastronomy destination in Ubud. • Luxury Bali Retreat (ID-007) 4'
                ),
                [
                    'Overnight Stay: Ultra-Luxury Rainforest Valley Private Pool Villa in Ubud.',
                    'Meals Included: Breakfast, Luxury Highland Lunch, & Fine Dining Dinner.',
                ],
            ),
            _day(
                6,
                'TEGALALANG RICE COATINGS • PRIVATE SWING • HOLY WATER',
                (
                    'PURIFICATION Experience the scenic majesty of the rolling Tegalalang Rice Terraces in the gentle morning light. Enjoy exclusive, private VIP access to a premier Bali Swing, gliding out safely over the dramatic valley terraces for extraordinary lifestyle photographs. Continue to the historical Tirta Empul Holy Water Temple for a private, deeply moving cultural purification ritual inside the crystal-clear volcanic springs, guided by a senior temple priest. Celebrate your final evening on the island with a custom TRAGUIN Signature Celebration Dinner prepared directly inside your villa grounds. Sightseeing & Logistics: Tegalalang Terraces, Private Premium Bali Swing, Tirta Empul Priest-Guided Purification. Optional Add-ons:A private masterclass with a master artisan to fashion a commemorative silver keepsake ring. Evening Highlight:A grand candlelight farewell dinner feast featuring individual butler service and live acoustic entertainment.'
                ),
                [
                    'Overnight Stay: Ultra-Luxury Rainforest Valley Private Pool Villa in Ubud.',
                    'Meals Included: Signature Floating Villa Breakfast & Private Gala Farewell Dinner.',
                ],
            ),
            _day(
                7,
                'FLOATING RESORT POOL BREAKFAST • SOULFUL BALI DEPARTURE',
                (
                    'Awake to the peaceful singing of jungle birds and savor an iconic floating breakfast served beautifully on water inside your private villa infinity pool. Take a quiet morning for last-minute photography, relaxation, or packing. At your designated departure time, your private luxury multi-purpose vehicle and chauffeur arrive to transfer you smoothly back to Ngurah Rai International Airport. Your guide will escort you directly to the premium lounge check- in, ensuring a completely stress-free departure. Leave the Island of the Gods with a collection of unforgettable memories masterfully crafted by TRAGUIN. Sightseeing & Logistics: Private Luxury Chauffeur Airport Transfer, Departure Concierge Assistance. Optional Add-ons:VIP Departure Lounge access confirmation for premium relaxation prior to your flight. Evening Highlight:International flight connection homeward. • Luxury Bali Retreat (ID-007) 5'
                ),
                [
                    'Overnight Stay: In-Flight / Home.',
                    'Meals Included: Premium Floating Infinity Pool Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'LUXURY The Westin Resort Nusa Dua, Bali',
                'Multi-city Bali',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — LUXURY The Westin Resort Nusa Dua, Bali',
            ),
            _hotel(
                'LUXURY The St. Regis Bali Resort',
                'Multi-city Bali',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — LUXURY The St. Regis Bali Resort',
            ),
            _hotel(
                'Amanusa (Aman Villas Nusa Dua)',
                'Bali',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Amanusa (Aman Villas Nusa Dua)',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Bali', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven MPV', 2),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 3),
            _inc_excluded('TRAGUIN Inclusions', 4),
        ],
    )
    return package, itinerary

def build_id_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-008'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Luxury Bali Villa Retreat'
    duration = '06 Nights / 07 Days'
    slug = 'id-008-luxury-bali-villa-retreat'
    itin_slug = 'id-008-luxury-bali-villa-retreat-itinerary'
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
            _ph('Serial code ID-008 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Luxury / Premium Ubud Villas DURATION: 06 Nights / 07 Days KEY', 2),
            _ph('Destinations: Ubud Central • Ayung River Valley • Kintamani RECOMMENDED FOR: Couples • Wellness Seekers • Families IDEAL SEASON: April to October (Dry & Clear) VIP CONCIERGE: 24/7 Dedicated Support Included PREMIUM UBUD VILLAS RETREAT Deep Rainforest Immersions & Private Valley Sanctuaries (6N) A CURATED HIGH-END HIDDEN PARADISE EXPERIENCE BY TRAGUIN Welcome to your bespoke Premium Ubud Villas Retreat • an ultra-luxury journey exclusively arranged by TRAGUIN. This comprehensive 6-Night • 7-Day luxury escape is dedicated entirely to the spiritual and cultural heart of Bali—Ubud. Escape from typical rushed sightseeing and instead immerse your senses inside an expansive rainforest estate • private infinity pool villas hanging over mist-laden canyons • and elite culinary concepts. Revel in flawless daily logistics • elite private wellness therapies • and hidden artisan trail operations curated precisely to your tastes. TOUR OVERVIEW This premium Best Bali Tour Package is intentionally slow-paced yet deeply detailed • matching ultra- exclusive villa living with iconic rainforest explorations. Travel Type: Ultra-Luxury Private Villa Experiential FIT Travel.', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
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
        tagline='Luxury Bali Villa Retreat',
        overview='TOUR OVERVIEW\nThis premium Best Bali Tour Package is intentionally slow-paced yet deeply detailed, matching ultra- exclusive villa living with iconic rainforest explorations. Travel Type: Ultra-Luxury Private Villa Experiential FIT Travel. • Premium Ubud Villas (ID-008) 1 Vehicle Deployment: Premium private luxury MPV or high-end SUV with a dedicated English-fluent chauffeur-guide. Meal Blueprint: Gourmet floating pool breakfasts, estate multi-course organic lunches, and fine gastronomy valley rim dinners. Route Sequence: Denpasar Airport VIP Arrival → Ubud Central Rainforest → Tegallalang Valley → Ayung River Rim → Kintamani Highlands → Denpasar Airport. TRAGUIN Lifestyle Perks: Skip-the-line temple access, direct private villa check-ins, pre-booked top-tier canyon spa pavilions, and elite culinary seating. EXPERIENCE THE ABSOLUTE TOP TOURIST PLACES IN BALI FROM YOUR PRIVATE SANCTUARY A true luxury vacation relies on unparalleled privacy and deep connection to the local surroundings. Our Premium Ubud Villas holiday package showcases the ultimate Top Tourist Places in Bali from a peaceful, crowd-free viewpoint, making it the best time to visit Bali to refresh your mind and spirit. From the magnificent stepped agricultural rows of Tegalalang to the dramatic ridge lines of Kintamani volcano, you will enjoy premium Bali Sightseeing without compromising on comfort. Take part in private water temple blessings, wander through vibrant artisan design markets, and enjoy holistic body spa rituals over rushing river rapids. DAY-BY-DAY CURATED ITINERARY',
        seo_title='ID-008 | Luxury Bali Villa Retreat | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Bali package (ID-008 / TRAGUIN-BALI-000): Ubud Central • Ayung River Valley • Kintamani RECOMMENDED FOR: Couples •  Wellness Seekers •  Famili with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • VIP FAST-TRACK ENTRY • RETREAT TO YOUR UBUD', 1),
            _ih('Day 02: UBUD ARTISAN PATHWAYS • MONKEY FOREST SANCTUARY & ROYAL', 2),
            _ih('Day 03: MAGNIFICENT TEGALALANG TERRACES • VIP BALI SWING EXPERIENCE', 3),
            _ih('Day 04: SPIRITUAL TIRTA EMPUL PURIFICATION • HIDDEN CANYON WATERFALL', 4),
            _ih('Day 05: MOUNT BATUR VOLCANIC PANORAMA • PRIVATE COFFEE ESTATE VIEWING', 5),
            _ih('Day 06: BALINESE ROYAL CULINARY MASTERCLASS • IMMERSIVE VALE', 6),
            _ih('Day 07: PREMIUM FLOATING POOL BREAKFAST • SOULFUL BALI DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • VIP FAST-TRACK ENTRY • RETREAT TO YOUR UBUD',
                (
                    'FOREST ESTATE Your luxury escape begins seamlessly as you touch down at Ngurah Rai International Airport (DPS). Walk straight past lines into the care of our private VIP fast-track customs representative, who handles all immigration clearances smoothly. Meet your dedicated TRAGUIN luxury chauffeur at the arrivals lounge and step into your premium multi-purpose vehicle, fully stocked with fresh mineral waters and cold essential-oil towels. Enjoy a picturesque drive inland as coastal views melt into lush rolling hills and emerald valleys. Arrive at your world-class Ubud private villa sanctuary and settle into your luxury pavilion, finishing the night with a fine candlelight welcome dinner over the valley rim. Sightseeing & Logistics: VIP Airport Fast-Track Handling, Private Luxury MPV Transfer, Estate In-Villa Check-In. Evening Highlight:Welcome tasting dinner showcasing modern contemporary Indonesian gastronomy inside your estate. • Premium Ubud Villas (ID-008) 2'
                ),
                [
                    'Overnight Stay: Premium Handpicked Luxury Rainforest Pool Villa in Ubud.',
                    'Meals Included: Welcome Drinks & Curated Estate Dinner.',
                ],
            ),
            _day(
                2,
                'UBUD ARTISAN PATHWAYS • MONKEY FOREST SANCTUARY & ROYAL',
                (
                    'PALACE TOUR Awake to the peaceful calls of the jungle and enjoy a magnificent gourmet breakfast. Your private guide will escort you on an exclusive discovery tour of central Ubud. Stroll down the sacred pathways of the ancient Ubud Monkey Forest Sanctuary, observing exotic long-tailed macaques beneath a canopy of towering banyan trees. Continue to the historic Ubud Royal Palace to admire beautiful classical stone architecture. Afterward, enjoy premium retail therapy across Ubud’s design markets, featuring luxury linen, fine woven art, and boutique home goods, before returning to your villa for a relaxed afternoon. Sightseeing & Logistics: Monkey Forest VIP Access, Royal Palace Guided Tour, Central Ubud Artisan Shopping. Optional Add-ons:A private, hands-on silver jewelry design workshop with an expert local artisan. Evening Highlight:Fine dining at an award-winning botanical restaurant celebrated for its innovative garden gastronomy.'
                ),
                [
                    'Overnight Stay: Premium Handpicked Luxury Rainforest Pool Villa in Ubud.',
                    'Meals Included: Breakfast & Gourmet Organic Lunch.',
                ],
            ),
            _day(
                3,
                'MAGNIFICENT TEGALALANG TERRACES • VIP BALI SWING EXPERIENCE',
                (
                    "Dress in elegant resort wear for a morning focused on Bali's most iconic agricultural vistas. Journey a short distance north to the stunning Tegalalang Rice Terraces, walking the emerald slopes as morning sunbeams cut through the palms. Skip the commercial crowds with private VIP access to a premier Bali Swing pavilion, soaring high over the canyon for spectacular lifestyle photography. Spend your afternoon at leisure back at your private estate pool, enjoying a complimentary 90-minute holistic Balinese deep-tissue massage in an open-air riverfront spa terrace. Sightseeing & Logistics: Tegalalang Terraces Walk, Premium Private Bali Swing Access, Luxury Spa Allocation. Optional Add-ons:A professional dress-rental service for high-end lifestyle photography at the valley swings. Evening Highlight:A customized romantic private candlelit dinner set up inside your villa's private infinity pool deck. • Premium Ubud Villas (ID-008) 3"
                ),
                [
                    'Overnight Stay: Premium Handpicked Luxury Rainforest Pool Villa in Ubud.',
                    'Meals Included: Breakfast & Romantic In-Villa Dinner.',
                ],
            ),
            _day(
                4,
                'SPIRITUAL TIRTA EMPUL PURIFICATION • HIDDEN CANYON WATERFALL',
                (
                    'TRAIL Immerse your group into the profound spiritual heritage of the island today. Travel with your guide to the sacred Tirta Empul Holy Water Temple. Change into formal ceremonial sarongs and enter the crystal-clear volcanic springs for a private, priest-guided spiritual purification ritual. Afterward, take a scenic drive to a hidden, low-traffic jungle waterfall canyon for a private gourmet picnic lunch set against the elements. Spend a peaceful afternoon returning to your estate to enjoy refreshing botanical drinks and personal relaxation time. Sightseeing & Logistics: Tirta Empul Priest-Guided Ritual, Private Waterfall Trail, Luxury Picnic Logistics. Optional Add-ons:A private evening sound healing session inside an exclusive architectural bamboo dome. Evening Highlight:Dinner at an elegant cliff-edge fine dining venue known for its global-fusion degustation menus.'
                ),
                [
                    'Overnight Stay: Premium Handpicked Luxury Rainforest Pool Villa in Ubud.',
                    'Meals Included: Breakfast & Private Luxury Picnic Lunch.',
                ],
            ),
            _day(
                5,
                'MOUNT BATUR VOLCANIC PANORAMA • PRIVATE COFFEE ESTATE VIEWING',
                (
                    'Journey up into the refreshing northern alpine climate of Kintamani. Behold the vast, breathtaking panorama of the active Mount Batur Volcano and its shimmering crater lake down below. Enjoy a premium lunch at a luxury overlook restaurant with floor-to-ceiling glass windows. In the afternoon, explore an exclusive, artisanal organic coffee estate tucked inside the fertile highlands. Discover the meticulous processing of world-class coffee beans and indulge in a private tasting flight before your luxury vehicle drives you smoothly back down to Ubud. Sightseeing & Logistics: Kintamani Volcanic Overlook Tour, Private Coffee Estate Access & Tasting Flight. Optional Add-ons:An early-morning premium 4x4 Jeep safari to watch the sunrise from Mount Batur’s black lava fields. Evening Highlight:A fine multi-course culinary experience at a world-ranked fine dining restaurant in central Ubud. • Premium Ubud Villas (ID-008) 4'
                ),
                [
                    'Overnight Stay: Premium Handpicked Luxury Rainforest Pool Villa in Ubud.',
                    'Meals Included: Breakfast, Highland Luxury Lunch, & Gastronomy Dinner.',
                ],
            ),
            _day(
                6,
                'BALINESE ROYAL CULINARY MASTERCLASS • IMMERSIVE VALE',
                (
                    "CELEBRATION Spend your final full day engaging deeply with local culinary traditions. Participate in an exclusive culinary masterclass hosted inside a private heritage garden estate by an acclaimed Balinese chef. Hand-harvest fresh organic herbs and spices from the estate gardens before preparing a marvelous, authentic royal feast for lunch. Spend your last afternoon enjoying your estate's premium facilities. In the evening, gather for your grand TRAGUIN Signature Farewell Dinner, complete with live acoustic entertainment and premium personalized service. Sightseeing & Logistics: Private Culinary Masterclass, Organic Garden Sourcing, Farewell Festivities. Optional Add-ons:A customized premium flower-petal arrangement hand-drawn inside your private pool. Evening Highlight:A grand final celebration dinner with custom mocktails and beautiful river valley views."
                ),
                [
                    'Overnight Stay: Premium Handpicked Luxury Rainforest Pool Villa in Ubud.',
                    'Meals Included: Breakfast, Royal Masterclass Lunch, & Gala Farewell Dinner.',
                ],
            ),
            _day(
                7,
                'PREMIUM FLOATING POOL BREAKFAST • SOULFUL BALI DEPARTURE',
                (
                    "Celebrate your final morning on the island with an iconic TRAGUIN Floating Breakfast beautifully served right in your villa's private infinity pool. Enjoy a final swim or some quiet meditation amidst the peaceful morning mist. At your designated departure time, your private luxury vehicle and chauffeur will arrive to transfer your group smoothly back to Ngurah Rai International Airport. Your guide will escort you directly to the premium airline lounge check-in, ensuring a stress-free departure. Leave the Island of the Gods carrying unforgettable memories masterfully delivered by TRAGUIN. Sightseeing & Logistics: Private Luxury Chauffeur Airport Transfer, Departure Concierge Support. Optional Add-ons:VIP Airport Lounge access confirmation for premium relaxation prior to your flight. Evening Highlight:International flight connection homeward. • Premium Ubud Villas (ID-008) 5"
                ),
                [
                    'Overnight Stay: In-Flight / Home.',
                    'Meals Included: Premium Floating Infinity Pool Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'LUXURY Maya Ubud Resort & Spa Villa Type: Heavenly Pool Villa Daily Luxury Breakfast + Complimentary Afternoon High Tea',
                'Multi-city Bali',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — LUXURY Maya Ubud Resort & Spa Villa Type: Heavenly Pool Villa Daily Luxury Breakfast + Complimentary Afternoon High Tea',
            ),
            _hotel(
                'LUXURY Komaneka at Bisma, Ubud Villa Type: One-Bedroom Pool Villa Daily Gourmet Breakfast + 24-Hour Dedicated Villa Concierge',
                'Multi-city Bali',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — LUXURY Komaneka at Bisma, Ubud Villa Type: One-Bedroom Pool Villa Daily Gourmet Breakfast + 24-Hour Dedicated Villa Conc',
            ),
            _hotel(
                'Mandapa, a Ritz-Carlton Reserve, Ubud Villa Type: One-Bedroom Rainforest Pool Villa Bespoke 24-Hour Patih (Butler) Service + Tailored All-Inclusive Dining • Premium Ubud Villas (ID-008) 6',
                'Multi-city Bali',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandapa, a Ritz-Carlton Reserve, Ubud Villa Type: One-Bedroom Rainforest Pool Villa Bespoke 24-Hour Patih (Butler) Servi',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Bali', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven MPV', 2),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 3),
            _inc_excluded('TRAGUIN Inclusions', 4),
        ],
    )
    return package, itinerary

def build_id_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-009'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Senior Citizen Relax Bali Escape'
    duration = '05 Nights / 06 Days'
    slug = 'id-009-senior-citizen-relax-bali-escape'
    itin_slug = 'id-009-senior-citizen-relax-bali-escape-itinerary'
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
            _ph('Serial code ID-009 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Senior Citizen / Relax BaliDURATION: 05 Nights / 06 Days KEY', 2),
            _ph('Destinations: Sanur Beachfront • Ubud Suburbs • Tanah Lot Rim RECOMMENDED FOR: Seniors • Multi-gen Families • Slow Travelers IDEAL SEASON: Year-Round Luxury Execution VIP CONCIERGE: Wheelchair-Accessible / Easy Pace Assurance SENIOR CITIZEN RELAX BALI ESCAPE Tranquil Boardwalks • Gentle Heritage Trails & Luxury Coastlines (5N) A THOUGHTFULLY PACED • ACCESSIBLE MASTERPIECE BY TRAGUIN Welcome to your bespoke Relax Bali Tour Package • an ultra-comfortable luxury journey designed by TRAGUIN with senior travelers in mind. This comprehensive 5-Night • 6-Day itinerary balances scenic Balinese beauty with a gentle • slow-paced flow. Forget about steep climbs • long walking paths • and rushed transfers. Instead • enjoy luxurious beachfront properties • private ground-floor access suites • customized smooth chauffeured transport • and highly accessible cultural highlights. Every meal • transfer • and excursion is optimized for maximum physical comfort and complete peace of mind. TOUR OVERVIEW This tailored Bali Tour Package for Seniors focuses entirely on relaxation • cultural preservation • and minimal physical strain. Travel Type: Ultra-Relaxed • Accessible Luxury FIT Travel.', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Leisure'],
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
        tagline='Senior Citizen Relax Bali Escape',
        overview='mooth drive to the iconic Tanah Lot Temple. Rather than navigating the crowded steps down to the rocky shore, your driver will escort you straight to a reserved terrace table at a premium cliffside cafe. Here, you can sit comfortably and enjoy unhindered, panoramic views of the sea temple as the sun sets brilliantly over the waves, all while sipping fresh coconut water. Sightseeing & Logistics: Tanah Lot Accessible Viewpoint, Reserved Premium Cliffside Seating. Optional Add-ons:A professional portrait photography session capturing your sunset moments against the temple backdrop. Evening Highlight:A relaxed dinner right on the terrace featuring freshly prepared, non-spicy local seafood and grilled specialties. Overnight Stay: Premium Handpicked Accessible Luxury Beachfront Resort in Sanur. Meals Included: Breakfast & Reserved Sunset View Terrace Dinner. • Senior Citizen Relax Bali (ID-009) 3\n\nTOUR OVERVIEW\nThis tailored Bali Tour Package for Seniors focuses entirely on relaxation, cultural preservation, and minimal physical strain. Travel Type: Ultra-Relaxed, Accessible Luxury FIT Travel. • Senior Citizen Relax Bali (ID-009) 1 Vehicle Deployment: Premium private full-sized luxury MPV with extra-low step entry, climate control, and a patient, English-fluent chauffeur-guide. Meal Blueprint: Inclusive daily wellness buffet breakfasts, soft local organic lunches, and sunset oceanfront dining with clear access paths. Route Sequence: Denpasar Airport VIP Arrival → Sanur Beachfront (3 Nights) → Accessible Ubud Heritage (2 Nights) → Denpasar Airport. TRAGUIN Lifestyle Perks: Airport curb-to-car luggage management, pre-arranged ground-floor or elevator-adjacent premium suites, and wheelchair-friendly paths pre-vetted by our local ground agents. EXPERIENCE THE BEST SIGHTSEEING IN BALI AT A GENTLE, EASY PACE A true vacation should never feel exhausting. Our Relax Bali package opens up the Top Tourist Places in Bali through a stress-free framework. We select places like Sanur’s paved, flat beach boardwalks and the majestic ocean views of Tanah Lot Temple—viewed from a comfortable cliffside cafe terrace without requiring long walks or steps. Whether you choose to travel during the dry months or prefer a quiet mid-season getaway, this itinerary provides the best time to visit Bali for a refreshing holiday. Enjoy soothing wellness spa therapies, gentle cultural evening shows, and delicious fine dining tailored to your specific dietary needs. DAY-BY-DAY CURATED ITINERARY',
        seo_title='ID-009 | Senior Citizen Relax Bali Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Bali package (ID-009 / TRAGUIN-BALI-000): Sanur Beachfront • Ubud Suburbs • Tanah Lot Rim RECOMMENDED FOR: Seniors •  Multi-gen Families •  Sl with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • VIP ARRIVALS LOUNGE ESCORT • SANUR BEACHFRONT', 1),
            _ih('Day 02: SANUR SUNRISE BOARDWALK STROLL • REFRESHING HYDRO-SPA', 2),
            _ih('Day 03: COMFORTABLE TANAH LOT SUNSET VIEWING • ACCESSIBLE TERRACE', 3),
            _ih('Day 04: SCENIC DRIVE INLAND • UBUD PALACE ECO-TRAIL • LUXURY RESORT', 4),
            _ih('Day 05: GENTLE TEGALALANG OVERLOOK LUNCH • TRADITIONAL LEGONG', 5),
            _ih('Day 06: SOOTHING MORNING GARDEN LEISURE • SEAMLESS AIRPORT TRANSFER', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • VIP ARRIVALS LOUNGE ESCORT • SANUR BEACHFRONT',
                (
                    'WELCOME Your relaxing escape begins smoothly at Ngurah Rai International Airport (DPS). Step off your plane and right into the care of our private VIP fast-track representative. Relax inside the air-conditioned immigration lounge with fresh refreshments while we process your passports and collect your luggage. Meet your patient TRAGUIN chauffeur right at the vehicle entrance and step into your spacious luxury MPV. Enjoy a smooth 25-minute drive via the scenic sea toll road to your tranquil beachfront resort in Sanur—a destination famous for its calm waters and flat coastal paths. Complete an easy, seated in-room check-in and relax for the evening. Sightseeing & Logistics: VIP Fast-Track Porter Support, Low-Step Luxury MPV Transfer, Beachfront Resort Arrival. Evening Highlight:A relaxed, three-course welcome dinner served on an open-air seaside deck with a smooth boardwalk path. • Senior Citizen Relax Bali (ID-009) 2'
                ),
                [
                    'Overnight Stay: Premium Handpicked Accessible Luxury Beachfront Resort in Sanur.',
                    'Meals Included: Welcome Drinks & Curated Oceanside Dinner.',
                ],
            ),
            _day(
                2,
                'SANUR SUNRISE BOARDWALK STROLL • REFRESHING HYDRO-SPA',
                (
                    "WELLNESS Wake up to a beautiful, calm sunrise over the ocean. If you feel up to it, enjoy a gentle stroll along Sanur's completely flat, paved coastal path, or simply enjoy the morning view from your private balcony. Savor a slow, multi- dish breakfast featuring local and international options. In the afternoon, visit a premium luxury wellness center for an accessible, age-friendly spa treatment. Unwind with a soothing 60-minute warm herbal compress therapy and a gentle foot massage designed to boost circulation and melt away travel fatigue. Sightseeing & Logistics: Sanur Boardwalk Leisure, Private Door-to-Door Spa Transfers with Driver Assistance. Optional Add-ons:A gentle, private morning chair-yoga session with a certified wellness specialist. Evening Highlight:An early dinner at a quiet beachfront garden pavilion specializing in healthy, organic cuisine."
                ),
                [
                    'Overnight Stay: Premium Handpicked Accessible Luxury Beachfront Resort in Sanur.',
                    'Meals Included: Breakfast & Soothing Coastal Dinner.',
                ],
            ),
            _day(
                3,
                'COMFORTABLE TANAH LOT SUNSET VIEWING • ACCESSIBLE TERRACE',
                (
                    'DINING Enjoy a slow, restful morning at your resort, taking advantage of the oceanfront amenities or reading by the pool. At mid-afternoon, embark on a smooth drive to the iconic Tanah Lot Temple. Rather than navigating the crowded steps down to the rocky shore, your driver will escort you straight to a reserved terrace table at a premium cliffside cafe. Here, you can sit comfortably and enjoy unhindered, panoramic views of the sea temple as the sun sets brilliantly over the waves, all while sipping fresh coconut water. Sightseeing & Logistics: Tanah Lot Accessible Viewpoint, Reserved Premium Cliffside Seating. Optional Add-ons:A professional portrait photography session capturing your sunset moments against the temple backdrop. Evening Highlight:A relaxed dinner right on the terrace featuring freshly prepared, non-spicy local seafood and grilled specialties. • Senior Citizen Relax Bali (ID-009) 3'
                ),
                [
                    'Overnight Stay: Premium Handpicked Accessible Luxury Beachfront Resort in Sanur.',
                    'Meals Included: Breakfast & Reserved Sunset View Terrace Dinner.',
                ],
            ),
            _day(
                4,
                'SCENIC DRIVE INLAND • UBUD PALACE ECO-TRAIL • LUXURY RESORT',
                (
                    'RECONSTRUCTION After a leisurely breakfast, check out of Sanur and enjoy a comfortable drive inland towards the lush hills of Ubud. Stop at the historic Ubud Royal Palace, entering through a side entrance specifically selected to avoid steps. Admire the beautiful courtyard stonework before checking into your premium valley-view resort. Your accommodation is pre-arranged on the ground level or close to central elevators, letting you relax deeply as afternoon mist rolls over the forest canopy. Sightseeing & Logistics: Ubud Side-Entrance Palace Access, Smooth Inland Transfer, Ground-Floor Villa Orientation. Optional Add-ons:A private, traditional Balinese wooden batik painting demonstration held right in your villa courtyard. Evening Highlight:Dinner at an elegant resort restaurant known for its farm-to-table organic menus and gentle acoustic background music.'
                ),
                [
                    'Overnight Stay: Premium Handpicked Low-Walking Luxury Resort in Ubud.',
                    'Meals Included: Breakfast & Fine Resort Dinner.',
                ],
            ),
            _day(
                5,
                'GENTLE TEGALALANG OVERLOOK LUNCH • TRADITIONAL LEGONG',
                (
                    'EVENING PERFORMANCE Your luxury exploration continues with a short, scenic morning drive to the famous Tegalalang Rice Terraces. Skip any steep trekking paths entirely; TRAGUIN will seat your group at a premier, level-access valley viewpoint restaurant. Enjoy a delicious lunch while looking out over the emerald green terraces. Return to the resort for an afternoon rest. In the evening, attend an exclusive, seated cultural performance of the beautiful Legong Dance, highlighting classical Balinese storytelling with vibrant costumes and mesmerizing gamelan music. Sightseeing & Logistics: Level-Access Rice Terrace Overlook, Seated VIP Tickets for Legong Dance Show. Optional Add-ons:A private meet-and-greet with the lead cultural dancers for a memorable group photo after the performance. Evening Highlight:A special TRAGUIN Signature Farewell Dinner showcasing mild, authentic Balinese recipes and delicate desserts. • Senior Citizen Relax Bali (ID-009) 4'
                ),
                [
                    'Overnight Stay: Premium Handpicked Low-Walking Luxury Resort in Ubud.',
                    'Meals Included: Breakfast, Overlook Lunch, & Farewell Gala Dinner.',
                ],
            ),
            _day(
                6,
                'SOOTHING MORNING GARDEN LEISURE • SEAMLESS AIRPORT TRANSFER',
                (
                    'DEPARTURE Enjoy a final morning waking up to the peaceful jungle surroundings. Relish a leisurely breakfast served directly to your terrace garden table. Spend your last hours enjoying the quiet resort grounds, capturing beautiful photos among the tropical flora. At the designated check-out time, your private luxury MPV will arrive to take you comfortably back to Ngurah Rai International Airport. Your chauffeur will coordinate directly with airport porters to handle all your luggage at the curb, ensuring a smooth, stress-free departure home. Sightseeing & Logistics: Curbside Luggage Porter Integration, Luxury Airport MPV Transfer, Departure Guidance. Optional Add-ons:VIP Departure Lounge access voucher for comfortable seating prior to your boarding call. Evening Highlight:International flight connection homeward. HANDPICKED SENIOR-FRIENDLY LUXURY RESORT TIERS TRAGUIN selects only premier properties that offer excellent level-access routes, elevators, large walk-in showers, and minimal steps: TIER CLASSIFICATION SANUR BEACHFRONT STAY (3 NIGHTS) UBUD RAINFOREST VALLEY STAY (2 NIGHTS) OPTION 01 DELUXE LUXURY InterContinental Bali Sanur Resort Room: Ground-Floor Garden Suite Alaya Resort Ubud Room: Deluxe Room (Elevator Access) OPTION 02 PREMIUM LUXURY Andaz Bali - a Concept by Hyatt Room: Premium Ground-Floor King Maya Ubud Resort & Spa Room: Heavenly Forest Pool Villa (Flat Entry) OPTION 03 ELITE LUXURY The Samata Sanur by LifestyleRetreats Room: Pool Villa with Ramped Access The Kayon Resort by Pramana Room: Valley Luxury Suite (Priority Elevator) • Senior Citizen Relax Bali (ID-009) 5 TIER CLASSIFICATION SANUR BEACHFRONT STAY (3 NIGHTS) UBUD RAINFOREST VALLEY STAY (2 NIGHTS) OPTION 04 ULTRA LUXURY The Fairmont Sanur Beach Bali Room: Oceanview Suite (Full Accessibility) Mandapa, a Ritz-Carlton Reserve Room: Dedicated Reserve Suite with Private Buggy'
                ),
                [
                    'Overnight Stay: In-Flight / Home.',
                    'Meals Included: Gourmet Garden Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'LUXURY InterContinental Bali Sanur Resort',
                'Bali',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — LUXURY InterContinental Bali Sanur Resort',
            ),
            _hotel(
                'LUXURY Andaz Bali - a Concept by Hyatt',
                'Multi-city Bali',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — LUXURY Andaz Bali - a Concept by Hyatt',
            ),
            _hotel(
                'The Fairmont Sanur Beach Bali',
                'Bali',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The Fairmont Sanur Beach Bali',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Bali', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven MPV', 2),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 3),
            _inc_excluded('TRAGUIN Inclusions', 4),
        ],
    )
    return package, itinerary

def build_id_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-010'
    tour_code = 'TRAGUIN-BALI-ADV-010'
    title = 'Premium Bali Adventure Tour'
    duration = '05 Nights / 06 Days'
    slug = 'id-010-premium-bali-adventure-tour'
    itin_slug = 'id-010-premium-bali-adventure-tour-itinerary'
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
            _ph('Serial code ID-010 | TRAGUIN tour code TRAGUIN-BALI-ADV-010', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Ubud (3N) • Seminyak (2N)IDEAL FOR Families, Couples, Adventure', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Daily Buffet Breakfast & Curated Gourmet Lunches Route Silhouette: Denpasar Arrival → Ubud Eco-Adventure → Kintamani Volcano Active Exploration → Nusa Penida Coastal Thrills → Seminyak Sunset & Beach', 7),
            _ph('TRAGUIN Signature Experience: Private sunrise breakfast setup overlooking the black lava fields of', 8),
            _ph('Curated by TRAGUIN Experts: Handpicked routing that reduces standard highway transit times by up to', 9),
            _ph('Personalized Assistance: Directly contact our on-ground destination head via a dedicated WhatsApp', 10),
            _ph('Premium Handpicked Hotels: Every selected resort undergoes strict quality audits for premium hygiene,', 11)
        ],
        moods=['Luxury', 'Adventure'],
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
        tagline='Premium Bali Adventure Tour',
        overview="TOUR OVERVIEW\nThis bespoke Bali Family Tour is crafted as a Private FIT (Free Independent Traveler) itinerary, ensuring complete flexibility and personalized care. Travel in style across the island in a private, fully air-conditioned luxury vehicle under the guidance of a dedicated English-speaking concierge driver. Your accommodation features premium stays at handpicked hotels known for world-class hospitality and stunning views. Travel Format: Private Luxury FIT Tour• ARRIVAL & LUXURY TRANSFER Vehicle: Premium Private Toyota Alphard / Innova Reborn Meal Plan: Daily Buffet Breakfast & Curated Gourmet Lunches Route Silhouette: Denpasar Arrival → Ubud Eco-Adventure → Kintamani Volcano Active Exploration → Nusa Penida Coastal Thrills → Seminyak Sunset & Beach Luxury → Departure TRAGUIN Curated Experience Note: Enjoy priority VIP access at all iconic attractions, avoiding general queues for the famous Bali swing and major marine transfers, a hallmark of TRAGUIN Packages.\n\nWHY CHOOSE THE PREMIUM BALI ADVENTURE EXPERIENCE?\nBali remains one of the world's most sought-after destinations because of its unique ability to fuse soft adventure with ultra-luxury comfort. This curated itinerary addresses the most searched experiences globally, providing the absolute Best Time to Visit Bali highlights. Whether you are looking for the ultimate Bali Honeymoon Package or an action-packed Bali Family Tour, the island caters to all ages with flawless elegance. Our itinerary highlights the Top Tourist Places in Bali, including the cultural heart of Ubud, the iconic Mount Batur viewpoint, and the breathtaking cliffs of Nusa Penida. Capture stunning visuals at popular Instagram locations like the Tegalalang Rice Terraces and Kelingking Beach. Beyond the visual splendors, immerse yourself in deep spiritual culture, high-end boutique shopping in Seminyak, and adrenaline-fueled white-water rafting, delivering a truly Premium Bali Experience.",
        seo_title='ID-010 | Premium Bali Adventure Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Bali package (ID-010 / TRAGUIN-BALI-ADV-010): Ubud (3N) • Seminyak (2N)IDEAL FOR Families, Couples, Adventure with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • TRANSITION TO THE CULTURAL HEART OF UBUD', 1),
            _ih('Day 02: UBUD JUNGLE SWING, TEGALALANG RICE TERRACES & WHITE WATER', 2),
            _ih('Day 03: KINTAMANI VOLCANO TREK OR JEEP TOUR & COFFEE PLANTATION', 3),
            _ih('Day 04: NUSA PENIDA EXCLUSION • CELTIC CLIFFS & THE ICONIC KELINGKING', 4),
            _ih('Day 05: TANAH LOT TEMPLE SUNSET & SEMINYAK BOUTIQUE DISCOVERY', 5),
            _ih('Day 06: FINAL SHOPPING & DEPARTURE FROM THE ISLAND OF THE GODS', 6),
            _ih('TRAGUIN Signature Experience: Private sunrise breakfast setup overlooking the black lava fields of', 7),
            _ih('Curated by TRAGUIN Experts: Handpicked routing that reduces standard highway transit times by up to', 8),
            _ih('Personalized Assistance: Directly contact our on-ground destination head via a dedicated WhatsApp', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • TRANSITION TO THE CULTURAL HEART OF UBUD',
                (
                    'Your extraordinary Luxury Bali Holiday begins the moment you touch down at Ngurah Rai International Airport (DPS). As you step into the arrival hall, you will be warmly greeted by your private TRAGUIN tour concierge holding a personalized placard. Receive a traditional Balinese welcome complete with fresh, fragrant frangipani garlands and chilled premium mineral water. Board your luxury private transport and relax as you leave the coastal bustle behind, driving inland toward the lush, emerald hills of Ubud—the cultural and spiritual core of the island. The scenic route takes you past traditional artisan villages, towering banyan trees, and misty river valleys. Upon arrival at your luxury jungle resort, complete a seamless, private check-in process. Spend your evening unwinding in your private pool villa, breathing in the crisp jungle air and listening to the soothing sounds of the Ayung River. ADRENALINE & ICONIC LANDSCAPES VOLCANIC WONDERS & SUNRISE MAGIC'
                ),
                [
                    'Sightseeing Included: Traditional Balinese Welcome, Scenic Drive through Ubud Foothills.',
                    "Evening Experience: Gourmet Welcome Dinner at the resort's award-winning fine dining restaurant.",
                    'Overnight Stay: Premium Jungle Resort & Spa, Ubud.',
                    'Meals Included: Dinner.',
                ],
            ),
            _day(
                2,
                'UBUD JUNGLE SWING, TEGALALANG RICE TERRACES & WHITE WATER',
                (
                    'RAFTING Savor a premium floating breakfast in your private pool before launching into a high-energy day of Bali Sightseeing. Your first destination is the famous Tegalalang Rice Terraces, a UNESCO World Heritage site displaying ancient subak irrigation. Here, engage in an immersive experience on the legendary Bali Swing. Experience the thrill of soaring high above the deep jungle canopy, capturing that quintessential, breathtaking Instagram photo with cascading rice paddies stretching out beneath you. Next, trade serene landscapes for pure adrenaline with an exclusive white-water rafting expedition down the sacred Ayung River. Under the supervision of expert guides, navigate class II and III rapids carved into deep volcanic rock. Paddle past spectacular hidden waterfalls, towering stone cliffs, and dense tropical rainforests. Conclude your river adventure with a gourmet hot-buffet lunch overlooking the pristine river canyon. In the late afternoon, explore the sacred Ubud Monkey Forest for a playful encounter with indigenous macaques amid ancient temple ruins. Mandif.'
                ),
                [
                    'Sightseeing Included: Tegalalang Rice Terraces, Ubud Monkey Forest, Ubud Traditional Art Market.',
                    'Optional Activities: ATV Quad Biking through local mud tracks and gorilla-face caves.',
                    'Evening Experience: Stroll through Ubud Center; optional dinner at the world-renowned Locavore or Blanco Par',
                    'Overnight Stay: Premium Jungle Resort & Spa, Ubud.',
                    'Meals Included: Breakfast & Lunch.',
                ],
            ),
            _day(
                3,
                'KINTAMANI VOLCANO TREK OR JEEP TOUR & COFFEE PLANTATION',
                (
                    'An early morning awakening brings you one of the most highly sought-after experiences in our Best Bali Tour Package collections. Choose between an adventurous sunrise trek up the sacred slopes of Mount Batur or a premium 4x4 custom Jeep tour across the surreal, black lava fields of Kintamani. As dawn breaks, watch the sky shift into vibrant hues of crimson and gold over Mount Abang and Lake Batur—a truly emotional and spiritual sight. Following sunrise, indulge in a hearty breakfast at a cliffside restaurant with sweeping panoramic views of the active volcano. On your return journey to Ubud, stop at an exclusive, sustainable Balinese plantation. Here, learn the intricate art of making traditional Luwak coffee. Sample an array of locally infused teas and herbal brews while overlooking lush herbal gardens, wrapping up a day defined by natural wonders and cultural immersion. ISLAND EXPEDITION & COASTAL LUXURY CULTURAL ICONS & MODERN ELEGANCE'
                ),
                [
                    'Sightseeing Included: Kintamani Volcano Viewpoint, Black Lava Fields, Mount Batur Caldera.',
                    'Optional Activities: Soaking in the Toya Devasya Natural Volcanic Hot Springs at the base of the mountain.',
                    'Evening Experience: Traditional Balinese Legong Dance performance at the historic Ubud Royal Palace.',
                    'Overnight Stay: Premium Jungle Resort & Spa, Ubud.',
                    'Meals Included: Breakfast & Lunch.',
                ],
            ),
            _day(
                4,
                'NUSA PENIDA EXCLUSION • CELTIC CLIFFS & THE ICONIC KELINGKING',
                (
                    'BEACH Bid a temporary farewell to Ubud as your private chauffeur transfers you to Sanur Harbor. Board a luxury high-speed catamaran for an exhilarating cruise across the Badung Strait to Nusa Penida, an island globally celebrated for its dramatic, untamed limestone cliffs and pristine coastal ecosystems. This day-trip is a premier highlight of our TRAGUIN Bali Packages. Upon arrival, your private island vehicle will escort you to Kelingking Beach, affectionately known as the "T- Rex Cliff" due to its unique rock formation jutting out into the crystal-clear turquoise ocean. Take in the awe- inspiring panoramic vistas from premium, uncrowded vantage points. Next, visit the natural infinity pool of Angel’s Billabong and the majestic collapsed sea cliff at Broken Beach. Enjoy a freshly caught seafood lunch at an exclusive beachfront club before returning to the mainland via fast boat, transitioning seamlessly to your ultra-luxury resort in Seminyak.'
                ),
                [
                    'Sightseeing Included: Kelingking Beach, Angel’s Billabong, Broken Beach, Crystal Bay.',
                    'Optional Activities: Manta Ray snorkeling safari at Marine Park.',
                    'Evening Experience: Elite beachside cocktails at Potato Head or Ku De Ta in chic Seminyak.',
                    'Overnight Stay: Luxury Beachfront Resort, Seminyak.',
                    'Meals Included: Breakfast & Beachside Lunch.',
                ],
            ),
            _day(
                5,
                'TANAH LOT TEMPLE SUNSET & SEMINYAK BOUTIQUE DISCOVERY',
                (
                    'Enjoy a leisurely morning in chic Seminyak, the capital of style and luxury in Bali. After breakfast, enjoy a free afternoon to discover upscale fashion boutiques, contemporary art galleries, and artisanal lifestyle stores. Seminyak is highly praised as one of the best family and luxury holiday hubs for shopping and high-end cafes. In the late afternoon, your private driver will escort you to the legendary Tanah Lot Temple. Perched dramatically on a wave-swept rock formation just offshore, this ancient sea temple is one of Bali’s most iconic attractions. Watch in awe as the sun sets behind the temple towers, casting a brilliant golden glow over the crashing waves of the Indian Ocean. It is an emotional, unforgettable scene, perfect for timeless family photography. END OF A MAGICAL JOURNEY'
                ),
                [
                    'Sightseeing Included: Tanah Lot Sea Temple, Seminyak Beach Boulevard.',
                    'Optional Activities: A 120-minute authentic luxury Balinese Spa Massage treatment.',
                    'Evening Experience: Grand Farewell Dinner at an upscale Indonesian heritage restaurant.',
                    'Overnight Stay: Luxury Beachfront Resort, Seminyak.',
                    'Meals Included: Breakfast & Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'FINAL SHOPPING & DEPARTURE FROM THE ISLAND OF THE GODS',
                (
                    'Awake to your final Balinese sunrise and indulge in an expansive buffet breakfast at your resort. Depending on your flight departure schedule, utilize your private luxury vehicle for last-minute souvenir shopping or a relaxing coffee stop at an Instagram-famous cafe. Your private concierge driver will ensure a timely transfer to Ngurah Rai International Airport, assisting you completely with your luggage up to the departure gates. Board your flight home with a heart full of joy, a renewed spirit of adventure, and unforgettable memories curated exclusively by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Airport Departure Escort.',
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Alaya Resort Ubud / Sthala Ubud The Haven Seminyak / Amadea Resort Deluxe Pool View Room Buffet Breakfast (BB)',
                'Multi-city Bali',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Alaya Resort Ubud / Sthala Ubud The Haven Seminyak / Amadea Resort Deluxe Pool View Room Buffet Breakfast (BB)',
            ),
            _hotel(
                'The Kayon Resort / Maya Ubud The Seminyak Beach Resort & Spa Premium Valley View Suite Buffet Breakfast (BB)',
                'Multi-city Bali',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Kayon Resort / Maya Ubud The Seminyak Beach Resort & Spa Premium Valley View Suite Buffet Breakfast (BB)',
            ),
            _hotel(
                'Viceroy Bali / Mandapa, a Ritz-Carlton The Legian Bali / W Bali - Seminyak Private Luxury Pool Villa Breakfast & High Tea',
                'Multi-city Bali',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Viceroy Bali / Mandapa, a Ritz-Carlton The Legian Bali / W Bali - Seminyak Private Luxury Pool Villa Breakfast & High Te',
            ),
            _hotel(
                'Amandari / COMO Shambhala Estate The Samaya Seminyak / Bulgari Resort Signature Ultra-Luxury Sanctuary Villa Bespoke All-Inclusive Plan',
                'Multi-city Bali',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Amandari / COMO Shambhala Estate The Samaya Seminyak / Bulgari Resort Signature Ultra-Luxury Sanctuary Villa Bespoke All',
            )
        ],
        inclusions=[
            _inc_included('Mount Batur, avoiding tourist crowds. Curated by TRAGUIN Experts: Handpicked routing that reduces standard highway transit times by up to 20%, saving valuable leisure hours. Personalized Assistance: Directly contact our on-ground destination head via a dedicated WhatsApp hotline for rapid dynamically updated restaurant reservations or spa bookings. Premium Handpicked Hotels: Every selected resort undergoes strict quality audits for premium hygiene, security, and world-class hospitality standards. Luxury Accommodation: 05 Nights stay at your chosen premium handpicked hotels tier.✔ Gourmet Meal Plan: Daily international breakfasts, 3 premium lunches during excursions, and 2 curated fine dining dinners.', 1),
            _inc_included('Private Transfers: All transfers via a private, air-conditioned premium vehicle (Toyota Alphard/Innova Reborn) with dedicated English-speaking tour concierge driver.', 2),
            _inc_included('Exclusive Sightseeing: All entry tickets, parking fees, and VIP skip-the-line privileges at listed iconic attractions.', 3),
            _inc_included('Adventure Gear: Professional safety gear, premium life jackets, and certified local guides for White Water Rafting and Volcano expeditions.', 4),
            _inc_included('Nusa Penida Cruise: Round-trip luxury fast catamaran tickets from Sanur to Nusa Penida with VIP lounge access.', 5),
            _inc_included('24/7 TRAGUIN Support: Dedicated executive assistance monitoring your journey round-the-clock for effortless execution.', 6),
            _inc_excluded('International Flights and associated airport terminal departure taxes', 7),
            _inc_excluded('Indonesia Visa on Arrival (VoA) fees (payable directly at the border counter)', 8),
            _inc_excluded('Personal incidentals, laundry, telephone services, and alcoholic beverages during meals', 9),
            _inc_excluded('Tips and gratuities for your private drivers, local adventure guides, and hotel staff', 10),
            _inc_excluded('Any optional or unlisted sightseeing excursions and leisure sports activities', 11),
            _inc_excluded('Comprehensive International Travel & Medical Insurance (highly recommended)', 12),
        ],
    )
    return package, itinerary

def build_id_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-011'
    tour_code = 'TRAGUIN-BALI-BCH-011'
    title = 'Best Bali Beaches & Coastal Escape'
    duration = '05 Nights / 06 Days'
    slug = 'id-011-best-bali-beaches-coastal-escape'
    itin_slug = 'id-011-best-bali-beaches-coastal-escape-itinerary'
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
            _ph('Serial code ID-011 | TRAGUIN tour code TRAGUIN-BALI-BCH-011', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Nusa Dua (2N) • Seminyak', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Daily International Buffet Breakfast, Beachside Seafood Dining, and Sunset Platters Route Silhouette: Denpasar Airport Arrival → Nusa Dua White Sands → Uluwatu Cliffside Sunset & Kecak → Seminyak Chic', 7),
            _ph('TRAGUIN Signature Experience: Private, beachside sunset table setup at Jimbaran Bay, avoiding', 8),
            _ph('Curated by TRAGUIN Experts: A balanced pace combining culture, sights, and relaxing resort time,', 9),
            _ph('Personalized Assistance: Directly contact our local on-ground representative for restaurant', 10),
            _ph('Premium Handpicked Hotels: Resorts are regularly audited to ensure excellent beachfront locations and', 11)
        ],
        moods=['Luxury', 'Beach'],
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
        tagline='Best Bali Beaches & Coastal Escape',
        overview="TOUR OVERVIEW\nThis Bali Family Tour is organized as a private, personalized FIT itinerary designed around maximum comfort and unhurried coastal discovery. Avoid the stress of coordinates as a private luxury vehicle and dedicated English-speaking tour concierge driver handle your daily itinerary with seamless precision. Travel Format: Private Premium Family FIT Tour Vehicle: Private Premium Multi-Purpose Vehicle (Innova Reborn / Alphard) ARRIVAL & WELCOME AMENITY Meal Plan: Daily International Buffet Breakfast, Beachside Seafood Dining, and Sunset Platters Route Silhouette: Denpasar Airport Arrival → Nusa Dua White Sands → Uluwatu Cliffside Sunset & Kecak → Seminyak Chic Beachfront → Jimbaran Seafood Dinner → Departure TRAGUIN Curated Experience Note: This beach package includes VIP reserve seating at the cliffside Uluwatu Kecak dance and custom front-row daybed options at Bali's premium beach clubs, provided exclusively as part of your TRAGUIN Bali Packages. THE ULTIMATE LUXURY BALI BEACH EXPERIENCE When searching for a Luxury Bali Holiday or an iconic Bali Honeymoon Package, the island's southern beaches stand out as premier global choices. This itinerary maximizes time around the Top Tourist Places in Bali for sun-seekers, ensuring you visit during the absolute Best Time to Visit Bali for crystal clear waters and cool ocean breezes. Our itinerary highlights key coastal landmarks, including the calm water enclaves of Nusa Dua, the dramatic drop-offs of Uluwatu, and the stylish social energy of Seminyak. Take advantage of popular Instagram locations such as the sea-cliffs overlooking Padang Padang, the iconic Tanah Lot backdrop, and trendy beachfront swings. Whether your family seeks calm beach walks, water sports at Tanjung Benoa, or gourmet beachfront seafood dining, this curated itinerary delivers a complete Premium Bali Experience.",
        seo_title='ID-011 | Best Bali Beaches & Coastal Escape | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Bali package (ID-011 / TRAGUIN-BALI-BCH-011): Nusa Dua (2N) • Seminyak with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • TRANSITION TO THE LUXURY RESORT HAVEN OF NUSA', 1),
            _ih('Day 02: TANJUNG BENOA WATERSYSTEM, THE MAJESTIC WATER BLOW & ULUWATU', 2),
            _ih('Day 03: TRANSITION TO SEMINYAK • EN ROUTE DISCOVERY OF GWK CULTURAL', 3),
            _ih('Day 04: THE MAJESTIC SEA TEMPLE OF TANAH LOT & SEMINYAK BEACH CLUB', 4),
            _ih('Day 05: LEISURE RESORT MORNING • ROMANTIC JIMBARAN BAY CANDLELIT', 5),
            _ih('Day 06: CHIC SOUVENIR SHOPPING • AIRPORT DEPARTURE WITH MEMORIES BY', 6),
            _ih('TRAGUIN Signature Experience: Private, beachside sunset table setup at Jimbaran Bay, avoiding', 7),
            _ih('Curated by TRAGUIN Experts: A balanced pace combining culture, sights, and relaxing resort time,', 8),
            _ih('Personalized Assistance: Directly contact our local on-ground representative for restaurant', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • TRANSITION TO THE LUXURY RESORT HAVEN OF NUSA',
                (
                    "DUA Your family's dream coastal getaway begins the moment your flight lands at Ngurah Rai International Airport. Your dedicated private TRAGUIN tour concierge will await your family at the arrival pavilion with a custom sign board. Savor your first taste of traditional Balinese warmth as you are presented with refreshing tropical leis and chilled botanical water. Step into your private, air-conditioned vehicle and enjoy a smooth transfer over the scenic Bali Mandara Toll Road, which curves gracefully over the ocean. Check into your premium resort in Nusa Dua—an exclusive, gated beachfront enclave celebrated for its manicured tropical gardens and calm lagoon beaches. Spend your afternoon unpacking and relaxing by your resort's multi-tiered infinity pool or strolling along the white sands. COASTAL WONDERS & CULTURAL PERFORMANCE ICONIC MONUMENTS & TRENDY COASTLINES"
                ),
                [
                    'Sightseeing Included: Luxury Airport Welcome, Panoramic Ocean Toll Route.',
                    'Evening Experience: Leisurely family walk along the paved Nusa Dua beachfront promenade.',
                    'Overnight Stay: Premium Beachfront Resort, Nusa Dua.',
                    'Meals Included: Welcome Amenities.',
                ],
            ),
            _day(
                2,
                'TANJUNG BENOA WATERSYSTEM, THE MAJESTIC WATER BLOW & ULUWATU',
                (
                    "CLIFF SUNSET Savor a world-class buffet breakfast before heading to Tanjung Benoa, the center of beach activities in Bali. Your family will enjoy an included private glass-bottom boat ride to Turtle Island, a great educational experience for children. Feel the ocean breeze as you look through the viewing panel at tropical marine life. In the afternoon, view the spectacular natural 'Water Blow' rock formation in Nusa Dua, where ocean waves crash into limestone cliffs, creating massive, photogenic plumes of spray. Later, drive along the Bukit Peninsula to the dramatic Uluwatu Temple, perched 70 meters high on a sheer sea cliff. As the sun sets over the Indian Ocean, watch the traditional Kecak & Fire Dance in a cliffside amphitheater—a memorable combination of rhythmic chanting, fire performance, and natural ocean views. Water Blow, Uluwatu Temple."
                ),
                [
                    'Sightseeing Included: Tanjung Benoa Peninsula, Glass-Bottom Boat Ride, Turtle Island Conservation, Nusa Dua',
                    'Optional Activities: Adrenaline-pumping banana boat, parasailing, or jet skiing at Tanjung Benoa.',
                    'Evening Experience: Premium seats for the Uluwatu Kecak Dance during sunset.',
                    'Overnight Stay: Premium Beachfront Resort, Nusa Dua.',
                    'Meals Included: Breakfast.',
                ],
            ),
            _day(
                3,
                'TRANSITION TO SEMINYAK • EN ROUTE DISCOVERY OF GWK CULTURAL',
                (
                    'PARK Following breakfast, check out from Nusa Dua and drive toward the legendary Garuda Wisnu Kencana (GWK) Cultural Park. Marvel at the colossal 122-meter-tall bronze statue of Lord Vishnu riding the mythical bird Garuda—one of the tallest monumental statues in the world. Enjoy a guided buggy tour through the massive limestone pillars of the park, taking in this blend of modern engineering and traditional Balinese art. Continue onward to Seminyak, the vibrant capital of luxury, fashion, and beach culture in Bali. Check into your stylish luxury resort located along the beachfront. The afternoon is yours to relax—enjoy the trendy boutique shopping lanes or watch the waves from a comfortable resort daybed. TIMELESS TEMPLES & VIBRANT BEACH CLUBS GOURMET DINING & FAMILY CELEBRATIONS FAREWELL BALI'
                ),
                [
                    'Sightseeing Included: GWK Cultural Park Monument, Seminyak Beach Front Plaza.',
                    'Optional Activities: Traditional Balinese costume family photoshoot at the cultural park.',
                    "Evening Experience: Relaxed dining at an upscale cafe along Seminyak's famous dining streets.",
                    'Overnight Stay: Luxury Beachfront Resort, Seminyak.',
                    'Meals Included: Breakfast.',
                ],
            ),
            _day(
                4,
                'THE MAJESTIC SEA TEMPLE OF TANAH LOT & SEMINYAK BEACH CLUB',
                (
                    'SUNSET Enjoy a peaceful morning swimming or indulging in a spa treatment. In the afternoon, your driver will take you to Tanah Lot Temple, an iconic Balinese sea temple built on a wave-swept offshore rock formation. Learn about its spiritual history and watch the waves break against its foundations during low tide. Return to Seminyak for a premium sunset experience at an upscale beach club, such as Potato Head or Tropicola. Relax on your reserved daybed, listen to chill tracks from world-class DJs, and watch the sun dip below the horizon, painting the sky in deep purples and warm oranges.'
                ),
                [
                    'Sightseeing Included: Tanah Lot Sea Temple, Seminyak Beach Front View.',
                    'Optional Activities: Surfing lessons for the family at Double Six Beach.',
                    'Evening Experience: VIP lounge access and sunset views at a premier Seminyak beach club.',
                    'Overnight Stay: Luxury Beachfront Resort, Seminyak.',
                    'Meals Included: Breakfast.',
                ],
            ),
            _day(
                5,
                'LEISURE RESORT MORNING • ROMANTIC JIMBARAN BAY CANDLELIT',
                (
                    "SEAFOOD DINNER Your final full day in Bali is designed around relaxation and memory-making. Enjoy your resort's luxury facilities, take a swim in the ocean, or visit local boutiques for high-quality linen resort wear and artisanal home decor. As twilight approaches, travel to the golden sands of Jimbaran Bay for your grand farewell dinner. TRAGUIN has arranged a private, candlelit table right on the beach, steps away from the surf. Indulge in a premium, freshly caught Balinese seafood platter cooked over traditional coconut husks, making for an emotional and unforgettable final evening with your family."
                ),
                [
                    'Sightseeing Included: Jimbaran Bay Coastline.',
                    'Optional Activities: A 90-minute aromatherapy massage at a luxury wellness spa.',
                    'Evening Experience: Candlelit Seafood Farewell Dinner on the beach.',
                    'Overnight Stay: Luxury Beachfront Resort, Seminyak.',
                    'Meals Included: Breakfast & Farewell Seafood Dinner.',
                ],
            ),
            _day(
                6,
                'CHIC SOUVENIR SHOPPING • AIRPORT DEPARTURE WITH MEMORIES BY',
                (
                    'TRAGUIN Enjoy your breakfast overlooking the Indian Ocean one last time. Depending on your flight time, your private vehicle is available for a final stop at premium souvenir centers like Krisna Oleh Oleh or a trendy local cafe. Your private concierge driver will ensure a smooth transfer to the airport, assisting with luggage check-in. Board your flight home with beautiful photos, wonderful family stories, and unforgettable memories crafted seamlessly by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Airport Departure Escort Service.',
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Merusaka Nusa Dua / Grand Hyatt Amadea Resort / The Haven Seminyak Deluxe Ocean/Garden Room Buffet Breakfast (BB)',
                'Multi-city Bali',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Merusaka Nusa Dua / Grand Hyatt Amadea Resort / The Haven Seminyak Deluxe Ocean/Garden Room Buffet Breakfast (BB)',
            ),
            _hotel(
                'The Westin Resort / Sofitel Bali Nusa Dua The Seminyak Beach Resort & Spa Premium Ocean View Suite Buffet Breakfast (BB)',
                'Multi-city Bali',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Westin Resort / Sofitel Bali Nusa Dua The Seminyak Beach Resort & Spa Premium Ocean View Suite Buffet Breakfast (BB)',
            ),
            _hotel(
                'The St. Regis Bali / The Ritz-Carlton W Bali - Seminyak / The Legian Bali Luxury Private Pool Villa Breakfast & High Tea Perks',
                'Multi-city Bali',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The St. Regis Bali / The Ritz-Carlton W Bali - Seminyak / The Legian Bali Luxury Private Pool Villa Breakfast & High Tea',
            ),
            _hotel(
                'The Mulia Mansion / The Apurva Kempinski The Samaya Seminyak / Alila Seminyak Signature Ultra-Luxury Beachfront Villa Bespoke Elite Service Plan',
                'Multi-city Bali',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — The Mulia Mansion / The Apurva Kempinski The Samaya Seminyak / Alila Seminyak Signature Ultra-Luxury Beachfront Villa Be',
            )
        ],
        inclusions=[
            _inc_included('Luxury Accommodation: 05 Nights stay across selected premium handpicked beach resorts', 1),
            _inc_included('TRAGUIN Signature Perks: Traditional lei welcomes, cool mineral water, and onboard high-speed Wi-Fi', 2),
            _inc_included('Marine Activity: Private glass-bottom boat charter to Turtle Island with local guide', 3),
            _inc_included('24/7 TRAGUIN Support: Ongoing support from our on-ground customer experience team', 4),
            _inc_included('Luxury Accommodation: 05 Nights stay across selected premium handpicked beach resorts', 5),
            _inc_excluded('International Flights and associated airport security/terminal fees', 6),
            _inc_excluded('Indonesia Visa on Arrival fees (payable directly at immigration)', 7),
            _inc_excluded('Personal incidentals, room service, laundry, and alcoholic beverages', 8),
            _inc_excluded('Tips and gratuities for your private drivers, local guides, and resort staff', 9),
            _inc_excluded('Optional water sports activities at Tanjung Benoa (jet ski, parasailing, etc.)', 10),
            _inc_excluded('Comprehensive International Travel & Medical Insurance', 11),
        ],
    )
    return package, itinerary

def build_id_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-012'
    tour_code = 'TRAGUIN-BALI-ID-012'
    title = 'Bali Romantic Tour Package'
    duration = '05 Nights / 06 Days'
    slug = 'id-012-bali-romantic-tour-package'
    itin_slug = 'id-012-bali-romantic-tour-package-itinerary'
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
            _ph('Serial code ID-012 | TRAGUIN tour code TRAGUIN-BALI-ID-012', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Romantic Uluwatu • Artistic Ubud • Nusa Dua Coastal Paradise', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Royal Breakfast (CP+) & Specialty Curated Dining Experiences Primary Route: Denpasar Airport → Romantic Uluwatu Cliffs → Ubud Cultural Heart → Nusa Dua Coast → Departure', 7)
        ],
        moods=['Luxury', 'Honeymoon'],
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
        tagline='Bali Romantic Tour Package',
        overview="Uluwatu • Ubud • Nusa Dua | 05 Nights & 06 Days Indulge in an extraordinary romantic escapade crafted exclusively for discerning souls. This Luxury Bali Holiday promises an immersive, deeply emotional journey across Indonesia's most captivating island paradise. Designed carefully by TRAGUIN, your premium travel companion, this customized itinerary balances the cinematic, cliff-hanging drama of Uluwatu with the emerald, mystical soul of Ubud's rain forests. From your private pool villa overlooking pristine turquoise waters to intimate candlelit dining beneath starlit skies, every touchpoint has been curated to transform moments into unforgettable memories. Experience the true definition of a Premium Bali Experience, where your personal desires dictate the pace of the day and world-class Balinese hospitality cocoons you in comfort. TRAGUIN Premium Luxury Holidays Page 1\n\nTOUR OVERVIEW\nTravel Pattern: Flexible Private FIT (Fully Independent Tour) Vehicle Fleet: Private Premium Luxury Alphard / SUV with English-speaking Guide-Driver Meal Plan: Royal Breakfast (CP+) & Specialty Curated Dining Experiences Primary Route: Denpasar Airport → Romantic Uluwatu Cliffs → Ubud Cultural Heart → Nusa Dua Coast → Departure TRAGUIN Curated Note: Includes fast-track airport assistance, pre-vetted premium romantic pool villas, and VIP entry at prime attractions. THE ULTIMATE BALI HONEYMOON PACKAGE EXPERIENCE\n\nWhy choose our signature  Bali Honeymoon Package? Bali remains the ultimate luxury destination for\ncouples, weaving breathtaking landscapes with deep spiritual heritage. It is globally searched for its dramatic coastlines, sweeping cliffside sunsets, and lush tiered rice terraces. By choosing a Luxury Bali Holiday via TRAGUIN, you unlock access to handpicked premium properties and private, uncrowded natural spectacles. Our TRAGUIN Bali Packages highlight the absolute Top Tourist Places in Bali, focusing heavily on highly sought-after Instagram locations like the iconic Uluwatu Temple, the magical Tegenungan Waterfall, and the romantic Tegalalang Rice Terraces. Whether you seek thrilling jungle swings over deep valleys, exclusive high-fashion couples photography sessions, private sunset catamarans, or traditional holistic couple spa treatments, this itinerary serves as the definitive reference for the Best Bali Tour Package online. TRAGUIN Premium Luxury Holidays Page 2",
        seo_title='ID-012 | Bali Romantic Tour Package | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Bali package (ID-012 / TRAGUIN-BALI-ID-012): Romantic Uluwatu • Artistic Ubud • Nusa Dua Coastal Paradise with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI', 1),
            _ih('Day 02: ULUWATU SIGHTSEEING', 2),
            _ih('Day 03: JOURNEY TO UBUD', 3),
            _ih('Day 04: IMMERSIVE UBUD CULTURE', 4),
            _ih('Day 05: NUSA DUA TRANSITION', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI | THE ROMANTIC CLIFFS OF ULUWATU WELCOME',
                (
                    'Step into paradise as you land at Denpasar International Airport. After seamlessly clearing immigration via our VIP fast-track assistance, your dedicated private luxury vehicle and personal tour concierge from TRAGUIN will greet you with fresh orchid garlands and chilled refreshments. Sit back and take in the beautiful island vistas as you ascend toward the dramatic limestone cliffs of southern Bali. Arrive at your ultra-luxury cliffside resort in Uluwatu. Check into your private pool villa designed with traditional accents and high-end modern amenities. Spend your afternoon unwinding in your private infinity pool that blends seamlessly into the ocean skyline. As twilight approaches, embark on your first of this island paradise. Indian Ocean. TRAGUIN Premium Luxury Holidays Page 3'
                ),
                [
                    'evening experience: toward the cliff edges, absorbing the immense scenic beauty and spiritual energy',
                    'Sightseeing Included: VIP Airport Assistance, Scenic Uluwatu Coastal Drive, Private Villa Check-In.',
                    'Evening Experience: Intimate sunset cocktails at an exclusive cliff-hanging lounge overlooking the',
                    'Overnight Stay: Premium Handpicked Luxury Cliff Villa, Uluwatu',
                    'Meals Included: Welcome Drinks & Refreshments',
                ],
            ),
            _day(
                2,
                'ULUWATU SIGHTSEEING | SPIRITUAL TEMPLES & FIRE DANCE APEX',
                (
                    'Wake up to the sounds of crashing waves and enjoy a floating breakfast served directly in your private pool. Today is dedicated to exploring the finest Bali Sightseeing highlights in the southern peninsula. Your private guide will escort you to the magnificent Uluwatu Temple, perched precisely 70 meters atop a sheer cliff face. This is universally recognized as one of the top tourist places in Bali for majestic photography and breathtaking landscapes. Stroll hand-in-hand along the ancient stone pathways while learning about Balinese mythology. As the sun dips below the horizon, painting the sky in deep shades of gold and amber, witness the dramatic, world-famous Kecak Fire Dance performance. The rhythmic chanting against the backdrop of the blazing sunset creates an absolute sensory highlight. Conclude your day with an elite seafood dinner right on the sands of Jimbaran Bay. Dinner. TRAGUIN Premium Luxury Holidays Page 4'
                ),
                [
                    'Sightseeing Included: Uluwatu Cliff Temple, Melasti Beach Coastal Walk, Panoramic Viewpoints.',
                    'Optional Activities: Couples Professional Cinematic Sunset Drone Shoot.',
                    'Evening Experience: VIP seating at the Kecak Fire Dance followed by a Candlelit Jimbaran Seafood',
                    'Overnight Stay: Premium Handpicked Luxury Cliff Villa, Uluwatu',
                    'Meals Included: Floating Breakfast & Private Seafood Dinner',
                ],
            ),
            _day(
                3,
                'JOURNEY TO UBUD | WATERFALLS, TROPICAL VALLEYS & EMERALD RICE',
                (
                    "TERRACES After a luxurious breakfast, bid adieu to the coast as your TRAGUIN Family Tour / Couple vehicle drives you inland toward Ubud, the beating cultural heart of Bali. The route transitions beautifully from oceanic blue to vibrant shades of deep forest emerald. En route, make a private stop at the majestic Tegenungan Waterfall, nestled inside a lush tropical valley—perfect for immersive nature walks and photography. Arrive in Ubud and witness the breathtaking Tegalalang Rice Terraces. Walk through the ancient, valley-carved subak irrigation systems that look like cascading green steps. For those seeking mild adventure, step onto the famous Bali Jungle Swing, soaring over the canopy for an iconic couple's photograph. Check into your ultra-private rainforest sanctuary resort later in the afternoon for some serene relaxation. TRAGUIN Premium Luxury Holidays Page 5"
                ),
                [
                    'Sightseeing Included: Tegenungan Waterfall, Tegalalang Rice Terraces, Ubud Art Market.',
                    'Optional Activities: High-fly Jungle Swing Experience & Traditional Luwak Coffee Tasting.',
                    'Evening Experience: Leisurely walks through Ubud’s fine-dining culinary streets or artisan boutiques.',
                    'Overnight Stay: Luxury Rainforest Private Pool Villa, Ubud',
                    'Meals Included: Gourmet Breakfast',
                ],
            ),
            _day(
                4,
                'IMMERSIVE UBUD CULTURE | ARTISAN VILLAGES & HOLY WATER',
                (
                    'CLEANSING Embrace a spiritual morning with an optional, beautifully peaceful sunrise yoga session overlooking the mist-shrouded jungle valleys. Following breakfast, your guide will lead you into the authentic cultural side of Ubud. Visit Tirta Empul Holy Water Temple, where you can choose to participate in an immersive, traditional Balinese purification ritual, cleansing your mind and body in crystal-clear mountain spring water. Spend your afternoon browsing through Celuk and Mas villages, world-famous for their high-end handmade silver jewelry and intricate wood carvings. Meet local master artisans and witness centuries- old crafting techniques passed down through generations. This is a brilliant opportunity to acquire highly authentic souvenirs and meaningful keepsakes from your magical TRAGUIN Bali Packages journey. Forest. winning spa. TRAGUIN Premium Luxury Holidays Page 6'
                ),
                [
                    'Sightseeing Included: Tirta Empul Holy Springs, Artisan Village Tours (Celuk/Mas), Ubud Monkey',
                    'Optional Activities: Private Silver-Making Couples Workshop.',
                    'Evening Experience: 120-minute Royal Balinese Deep Tissue Couple Spa Treatment at an award-',
                    'Overnight Stay: Luxury Rainforest Private Pool Villa, Ubud',
                    'Meals Included: Gourmet Breakfast',
                ],
            ),
            _day(
                5,
                'NUSA DUA TRANSITION | PRISTINE WHITE BEACHES & PRIVATE SUNSET',
                (
                    "CRUISE Enjoy your final breakfast overlooking the calm river valleys of Ubud before driving down to the pristine, white-sand enclave of Nusa Dua—Bali’s premier resort zone. Nusa Dua is globally highly-rated for its calm, azure waters and meticulously manicured beachfront properties, making it an essential inclusion in our Best Bali Tour Package structures. Check into your ultra-luxury beachfront resort. In the late afternoon, your driver will transfer you to the private marina where you will step onto a private luxury catamaran cruise. Sail along the beautiful coastlines as the sun goes down, drinking premium vintage wine and enjoying gourmet hors d'oeuvres. This elegant, private ocean experience offers the perfect romantic culmination to your magnificent holiday."
                ),
                [
                    'Sightseeing Included: Nusa Dua Beach Promenade, Water Blow Landmark Attraction.',
                    'Optional Activities: Jet Skiing, Parasailing, or Sea Walking at nearby Tanjung Benoa.',
                    'Evening Experience: Private Sunset Catamaran Cruise followed by an elegant multi-course dinner.',
                    'Overnight Stay: Ultra-Luxury Oceanfront Resort, Nusa Dua',
                    'Meals Included: Gourmet Breakfast & Farewell Dinner Cruise',
                ],
            ),
            _day(
                6,
                'DEPARTURE | CHERISHING UNFORGETTABLE MEMORIES BEYOND',
                (
                    'DESTINATIONS Greet your final Balinese morning with a peaceful beach stroll or a final swim in the azure waters. Indulge in an expansive international buffet breakfast at the resort restaurant. Depending on your flight schedule, enjoy some last-minute luxury shopping at The Bali Collection mall or simply relax in the sun- drenched gardens of your resort property. Your private luxury vehicle will arrive precisely on time to smoothly transfer you to Denpasar International Airport for your homeward journey. As you board your flight, look back at a perfectly organized luxury vacation filled with deep laughter, culture, romance, and beautiful milestones, expertly delivered by the destination professionals at TRAGUIN. TRAGUIN Premium Luxury Holidays Page 7'
                ),
                [
                    'Sightseeing Included: Leisure Beach Time, Private Airport Outbound Transfer.',
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Renaissance Bali Uluwatu Alaya Resort Ubud Merusaka Nusa DuaBB (Breakfast Plan)',
                'Multi-city Bali',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Renaissance Bali Uluwatu Alaya Resort Ubud Merusaka Nusa DuaBB (Breakfast Plan)',
            ),
            _hotel(
                'Anantara Uluwatu Resort The Kayon Resort Ubud The Westin Resort Bali BB + Special Dinner',
                'Multi-city Bali',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Anantara Uluwatu Resort The Kayon Resort Ubud The Westin Resort Bali BB + Special Dinner',
            ),
            _hotel(
                'Six Senses UluwatuThe Kayon Jungle Resort The St. Regis Bali Resort BB + Floating BF',
                'Multi-city Bali',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Six Senses UluwatuThe Kayon Jungle Resort The St. Regis Bali Resort BB + Floating BF',
            ),
            _hotel(
                'Bvlgari Resort Bali Mandapa, a Ritz- Carlton The Mulia Villas BaliUltra-VIP Club Plan',
                'Multi-city Bali',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Bvlgari Resort Bali Mandapa, a Ritz- Carlton The Mulia Villas BaliUltra-VIP Club Plan',
            )
        ],
        inclusions=[
            _inc_included('Royal Meals: 5 Gourmet Breakfasts, 1 Jimbaran Candlelit Dinner, 1 Luxury Sunset Cruise Dinner', 1),
            _inc_included('Luxury Transfers: All transfers in an exclusive, private air-conditioned vehicle with dedicated driver-guide', 2),
            _inc_included('VIP Assistance: Personalized meet-and-greet on arrival plus fast-track airport customs assistance', 3),
            _inc_included('Curated Sightseeing: All entrance fees, parking, and toll expenses for itineraries listed above', 4),
            _inc_included('Complimentary Experiences: 120-Minute Couple Spa session and access to top-tier beach clubs', 5),
            _inc_included('24/7 TRAGUIN Support: Dedicated digital concierge service throughout your entire trip', 6),
            _inc_included('Royal Meals: 5 Gourmet Breakfasts, 1 Jimbaran Candlelit Dinner, 1 Luxury Sunset Cruise Dinner', 7),
            _inc_included('Luxury Transfers: All transfers in an exclusive, private air-conditioned vehicle with dedicated driver-guide', 8),
            _inc_included('VIP Assistance: Personalized meet-and-greet on arrival plus fast-track airport customs assistance', 9),
            _inc_included('Curated Sightseeing: All entrance fees, parking, and toll expenses for itineraries listed above', 10),
            _inc_included('Complimentary Experiences: 120-Minute Couple Spa session and access to top-tier beach clubs', 11),
            _inc_included('24/7 TRAGUIN Support: Dedicated digital concierge service throughout your entire trip', 12),
            _inc_excluded('International Flights: Round-trip airfares from your originating city to Denpasar, Bali', 13),
            _inc_excluded('Visa Formalities: Visa on Arrival (VoA) fees and Tourism Levy taxes payable directly at the border', 14),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium alcoholic beverages, and tipping tips', 15),
            _inc_excluded('Optional Activities: Water sports at Tanjung Benoa, specific jungle swings, or extra meals not mentioned', 16),
            _inc_excluded('Travel Insurance: Comprehensive international travel and medical health insurance policies', 17),
            _inc_excluded('International Flights: Round-trip airfares from your originating city to Denpasar, Bali', 18),
            _inc_excluded('Visa Formalities: Visa on Arrival (VoA) fees and Tourism Levy taxes payable directly at the border', 19),
            _inc_excluded('Personal Expenses: Laundry, telephone calls, premium alcoholic beverages, and tipping tips', 20),
        ],
    )
    return package, itinerary

def build_id_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-013'
    tour_code = 'TRAGUIN-BALI-ID-013'
    title = 'Bali Family Tour Package'
    duration = '06 Nights / 07 Days'
    slug = 'id-013-bali-family-tour-package'
    itin_slug = 'id-013-bali-family-tour-package-itinerary'
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
            _ph('Serial code ID-013 | TRAGUIN tour code TRAGUIN-BALI-ID-013', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Kuta Gateway • Ubud Rainforest • Kintamani Volcano • Seminyak Coast', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Daily Extensive International Buffets (Bed & Breakfast) + Curated Family Lunches Primary Route: Denpasar Airport → Vibrant Kuta Coastal Base → Ubud Rainforest Sanctuary → Kintamani Highlands → Chic Se', 7)
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
        tagline='Bali Family Tour Package',
        overview='The Ultimate Bali Explorer | 06 Nights & 07 Days Welcome to an immersive family odyssey crafted by TRAGUIN, where pristine natural beauty, majestic spiritual heritage, and joyful multi-generational adventures come together perfectly. This bespoke Best Bali Tour Package is intelligently designed to delight travelers of all age groups—combining the high- energy beachfront fun of Kuta and Seminyak with the tranquil, cultural charm of Ubud and the panoramic volcano vistas of Kintamani. From private luxury transport ensuring absolute comfort for senior citizens to engaging, safe animal encounters for children, every single element of this Luxury Bali Holiday has been hand-selected. Trust TRAGUIN to present your family with an unparalleled, stress-free, and emotionally enriching Premium Bali Experience that will be cherished in your hearts forever. TRAGUIN Premium Travel & Luxury Holidays Page 1\n\nTOUR OVERVIEW\nTravel Pattern: Private Family FIT (Fully Independent Tour) Vehicle Fleet: Dedicated Luxury Private Microbus (e.g., Toyota HiAce Luxury) with English-fluent Guide-Driver Meal Plan: Daily Extensive International Buffets (Bed & Breakfast) + Curated Family Lunches Primary Route: Denpasar Airport → Vibrant Kuta Coastal Base → Ubud Rainforest Sanctuary → Kintamani Highlands → Chic Seminyak → Departure TRAGUIN Curated Note: Includes all mandatory child-safe standard checks, premium spacious seating arrangements, flexible timelines, and VIP skipped lines at top tourist spots.\n\nWHY CHOOSE OUR SIGNATURE BALI FAMILY TOUR PACKAGE?\nBali stands as a world-class destination for a fulfilling, safe, and exciting Bali Family Tour. Highly searched across Google for its rare combination of interactive wildlife safaris, magical cultural dances, and gorgeous beach resorts, it offers a multi-layered vacation canvas. Booking your TRAGUIN Bali Packages guarantees that you experience the absolute Top Tourist Places in Bali without any typical tour coordination hassle. Our bespoke itinerary balances popular Instagram locations with calm, interactive cultural tours. Children will be fascinated by the playful inhabitants of the Sacred Monkey Forest and the massive exotic species at the Safari Park, while adults soak in the peaceful scenic beauty of ancient water temples and volcanic calderas. This meticulously organized route outlines the definitive blueprint for an incredible, luxury Bali Sightseeing trip during the Best Time to Visit Bali. TRAGUIN Premium Travel & Luxury Holidays Page 2',
        seo_title='ID-013 | Bali Family Tour Package | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Bali package (ID-013 / TRAGUIN-BALI-ID-013): Kuta Gateway • Ubud Rainforest • Kintamani Volcano • Seminyak Coast with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: WELCOME TO PARADISE', 1),
            _ih('Day 02: FAMILY ADVENTURE', 2),
            _ih('Day 03: JOURNEY TO UBUD', 3),
            _ih('Day 04: HIGHLAND EXPLORER', 4),
            _ih('Day 05: WATERFALLS & SUNSETS', 5),
            _ih('Day 06: CHIC SEMINYAK LEISURE', 6),
            _ih('Day 07: CHERISHED MEMORIES', 7)
        ],
        days=[
            _day(
                1,
                'WELCOME TO PARADISE | ARRIVAL & PRIVATE KUTA COASTAL',
                (
                    "SETTLEMENT Your unforgettable family holiday begins as your flight descends into Denpasar International Airport. Step through our VIP Arrival Fast-Track lane to completely avoid tiresome airport queues. Outside the terminal, your dedicated private luxury vehicle from TRAGUIN will be waiting with refreshing cold towels, chilled tropical juices, and beautiful welcome flower garlands for the whole family. Enjoy a smooth transfer to your premium beachfront resort in Kuta. Spend your afternoon unpacking at leisure and exploring the resort's premium amenities, including safe kids' play pools and elegant adult lounges. In the evening, step onto the soft golden sands of Kuta Beach to witness an incredible crimson sunset—a perfect introduction to the mesmerizing breathtaking landscapes of Bali. Walk. restaurant. TRAGUIN Premium Travel & Luxury Holidays Page 3"
                ),
                [
                    'Sightseeing Included: VIP Fast-Track Airport Welcoming, Private Microbus Transfer, Kuta Beach Sunset',
                    'Evening Experience: Relaxed beachfront family dinner at a highly rated traditional Indonesian',
                    'Overnight Stay: Premium Handpicked Beachfront Resort, Kuta / Legian',
                    'Meals Included: Welcome Drink & Specialty Family Welcome Dinner',
                ],
            ),
            _day(
                2,
                'FAMILY ADVENTURE | BALI SAFARI & MARINE PARK IMMERSIVE',
                (
                    'EXPEDITION Indulge in a rich international buffet breakfast at your resort before setting off for an exhilarating day at the world-renowned Bali Safari & Marine Park. This is one of the highest-ranked family attractions in Indonesia, offering a premium immersive experience where children and adults can see over a hundred species of exotic animals roaming freely in beautifully replicated natural habitats. Board a private, secure tram vehicle to journey through regions mimicking India, Africa, and Indonesia. Witness thrilling live animal educational shows, including the majestic elephant presentation and the grand Bali Agung cultural performance. Conclude the safari experience with an optional unique lunch inside a glass-walled restaurant, looking directly into a live lion habitat. Educational Shows. cafes. TRAGUIN Premium Travel & Luxury Holidays Page 4'
                ),
                [
                    'Sightseeing Included: Full-Day Pass to Bali Safari & Marine Park, Safari Journey Tram, Live',
                    'Optional Activities: Water Play Zone access within the park or Elephant Feeding Interaction.',
                    "Evening Experience: Leisurely stroll through Kuta's vibrant modern shopping squares and seaside",
                    'Overnight Stay: Premium Handpicked Beachfront Resort, Kuta / Legian',
                    'Meals Included: International Breakfast',
                ],
            ),
            _day(
                3,
                'JOURNEY TO UBUD | SACRED MONKEY FOREST & TEGALALANG RICE',
                (
                    'TERRACES After checking out from your coastal resort, your private family coach drives you inland toward Ubud, the peaceful cultural capital of Bali. Watch the scenery shift dramatically into dense tropical jungles, river gorges, and terraced agricultural valleys. Your first stop is the famous Sacred Monkey Forest Sanctuary, a beautiful ecological reserve holding ancient moss-covered temples and hundreds of playful long-tailed macaques. Next, visit the spectacular Tegalalang Rice Terraces, universally searched as one of the ultimate iconic attractions in Bali. Marvel at the stunning green vistas shaped by centuries-old traditional Balinese community irrigation. Your family can take stunning group photos here, and the brave hearts can ride the safe family-friendly giant valley swings over the canopy. Check into your luxury Ubud forest villa later in the afternoon. Market. TRAGUIN Premium Travel & Luxury Holidays Page 5'
                ),
                [
                    'Sightseeing Included: Sacred Ubud Monkey Forest, Tegalalang Rice Terraces, Ubud Traditional Art',
                    'Optional Activities: Luwak Coffee Plantation Interactive Guided Walk & Tea Tasting.',
                    'Evening Experience: Fine dining at a gorgeous riverside restaurant surrounded by glowing fireflies.',
                    'Overnight Stay: Luxury Rainforest Family Suite / Private Pool Villa, Ubud',
                    'Meals Included: Gourmet Breakfast',
                ],
            ),
            _day(
                4,
                'HIGHLAND EXPLORER | KINTAMANI VOLCANO PANORAMA & HOLY',
                (
                    'SPRINGS Wake up to the fresh, crisp air of the Ubud hills. Today, your TRAGUIN Bali Packages journey scales the scenic highlands to Kintamani. As you reach the ridge viewpoint, a stunning panorama reveals itself: the active Mount Batur Volcano standing dramatically beside the expansive, mirror-like waters of Lake Batur. This majestic landscape offers an incredible backdrop for a premium family photograph. Enjoy a delicious buffet lunch at a premium restaurant on the cliff edge, letting you savor authentic cuisine while soaking in the cool mountain breeze. In the afternoon, descend back down to visit the sacred Tirta Empul Holy Water Temple. Observe the beautiful spiritual heritage of Balinese families participating in traditional ritual purification across ancient, spring-fed stone pools. Temple. boutiques. TRAGUIN Premium Travel & Luxury Holidays Page 6'
                ),
                [
                    'Sightseeing Included: Kintamani Volcano Overlook, Mount Batur Caldera Viewpoint, Tirta Empul',
                    'Optional Activities: Natural Volcanic Hot Springs relaxing bath at the foot of Mount Batur.',
                    "Evening Experience: Restful evening exploring Ubud's local organic cafes and artisan chocolate",
                    'Overnight Stay: Luxury Rainforest Family Suite / Private Pool Villa, Ubud',
                    'Meals Included: Gourmet Breakfast & Panoramic Buffet Lunch at Kintamani',
                ],
            ),
            _day(
                5,
                'WATERFALLS & SUNSETS | TEGENUNGAN & THE ICONIC TANAH LOT',
                (
                    'CLIFF TEMPLE Check out from Ubud after a relaxing morning breakfast. Your private tour heading back to the coast stops first at the impressive Tegenungan Waterfall. Nestled deep within a green tropical valley, this massive waterfall features a wide, safe viewing deck—ideal for senior citizens to comfortably enjoy the view while the younger family members walk down to feel the cool river mist. In the afternoon, proceed toward the west coast to witness the ultimate crown jewel of Bali sightseeing: the iconic Tanah Lot Temple. This legendary offshore temple sits majestically on a wave-swept black rock formation in the ocean. As the sun sets behind the temple towers, the entire horizon glows in stunning orange hues. Check into your ultra-luxury Seminyak resort following this magical experience. TRAGUIN Premium Travel & Luxury Holidays Page 7'
                ),
                [
                    'Sightseeing Included: Tegenungan Waterfall Exploration, Tanah Lot Sea Temple Sunset Excursion.',
                    'Optional Activities: Traditional Balinese attire group family studio photo shoot.',
                    'Evening Experience: Al-fresco seaside dining along the upscale culinary streets of Seminyak.',
                    'Overnight Stay: Premium Luxury Beach Resort, Seminyak',
                    'Meals Included: Gourmet Breakfast',
                ],
            ),
            _day(
                6,
                'CHIC SEMINYAK LEISURE | BEACH CLUBS & GOURMET FAREWELL',
                (
                    "DINNER This day is deliberately kept open and completely flexible, allowing your family to enjoy the upscale beachfront lifestyle of Seminyak at your own desired pace. Relax on the comfortable daybeds of a premium, family-friendly beach club, where kids can play safely in shallow pools while parents enjoy world-class tropical mixology and chilled music overlooking the Indian Ocean. Alternatively, walk through the trendy streets of Seminyak, famous for holding the island's best designer boutiques, elegant art galleries, and upscale lifestyle centers. In the evening, gather together as TRAGUIN hosts an exquisite multi-course family farewell dinner at a private beachside pavilion, celebrating the bond of family amidst premium luxury."
                ),
                [
                    'Sightseeing Included: Seminyak Beach Promenade, Flexible Lifestyle Exploration.',
                    'Optional Activities: Full-Body Therapeutic Family Spa Treatment package.',
                    'Evening Experience: Exclusive TRAGUIN curated Private Beachside Farewell Barbecue Feast.',
                    'Overnight Stay: Premium Luxury Beach Resort, Seminyak',
                    'Meals Included: Gourmet Breakfast & Private Farewell Dinner',
                ],
            ),
            _day(
                7,
                'CHERISHED MEMORIES | LAST-MINUTE SHOPPING & DEPARTURE',
                (
                    "Savor your final lavish morning buffet breakfast at the resort's open-air terrace. Spend your remaining hours indulging in a refreshing morning dip in the pool or grabbing last-minute premium souvenirs at the nearby luxury malls. Pack your bags filled with incredible stories and joyful family moments. Your private luxury microbus will arrive precisely on time to provide a comfortable transfer back to Denpasar International Airport. Your dedicated TRAGUIN concierge will assist with your luggage and guide you smoothly to the departure gates, marking the perfect end to a flawlessly organized elite family holiday. TRAGUIN Premium Travel & Luxury Holidays Page 8"
                ),
                [
                    'Sightseeing Included: Resort Leisure, Private Airport Outbound Escort.',
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Kuta Gateway',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Kuta Gateway',
                '6N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Kuta Gateway',
                '6N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Kuta Gateway',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Curated Meals: 6 Lavish International Breakfasts, 1 Panoramic Highland Lunch, 1 Grand Farewell Beachfront Barbecue.', 1),
            _inc_included('Private Transportation: Dedicated, spacious air-conditioned luxury microbus (Toyota HiAce style) for all transfers and tours.', 2),
            _inc_included('VIP Meet & Greet: Fast-track customs entry line on arrival with personalized baggage handling assistance.', 3),
            _inc_included('All Entrance Fees: Complete entry tickets to Bali Safari & Marine Park, Monkey Forest, Tanah Lot, and Kintamani points.', 4),
            _inc_included('Welcome Amenities: Cold face towels, tropical welcome juices, and fresh orchid garlands for the entire family.', 5),
            _inc_included('24/7 TRAGUIN Support: Real-time digital travel concierge support directly operational from Denpasar. Local Taxes: All local government taxes, driver allowances, toll-gate charges, and resort service fees included.', 6),
            _inc_included('TRAGUIN Premium Travel & Luxury Holidays Page 9', 7),
            _inc_excluded('International Flight Tickets: Round-trip airfare from your home city to Bali', 8),
            _inc_excluded('Personal Incidentals: Resort laundry services, telephone calls, mini-bar spending, and tipping tips', 9),
            _inc_excluded('Optional Detours: Water sports at Tanjung Benoa or activities not clearly mentioned in the day plans', 10),
            _inc_excluded('Travel Insurance: Comprehensive global travel and medical emergency health insurance policies', 11),
        ],
    )
    return package, itinerary

def build_id_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-014'
    tour_code = 'TRG-BALI-WELLNESS-014'
    title = 'Luxury Yoga & Wellness Bali Retreat'
    duration = '06 Nights / 07 Days'
    slug = 'id-014-luxury-yoga-wellness-bali-retreat'
    itin_slug = 'id-014-luxury-yoga-wellness-bali-retreat-itinerary'
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
            _ph('Serial code ID-014 | TRAGUIN tour code TRG-BALI-WELLNESS-014', 1),
            _ph('Country: Bali, Indonesia | Category: Wellness & Yoga Retreat DURATION: 06 Nights / 07 Days', 2),
            _ph('Destinations: Ubud (4N) • Seminyak (2N)IDEAL FOR: Wellness Seekers, Families &', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Leisure'],
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
        tagline='Luxury Yoga & Wellness Bali Retreat',
        overview='An Immersive Journey of Mindfulness, Rejuvenation, and Breathtaking Landscapes Welcome Note from TRAGUIN: Embark on an extraordinary, soulful escape with the Best Bali Tour Package curated meticulously by TRAGUIN experts. Known as the Island of the Gods, Bali represents a sanctuary where spirituality meets raw natural beauty. This exclusive Bali Wellness Yoga Retreat is tailored to harmonize your mind, body, and spirit while enveloping you in ultra-luxury. Experience signature holistic therapy, sacred rituals, and the breathtaking landscapes of Ubud and Seminyak in this ultimate Luxury Bali Holiday.\n\nTOUR OVERVIEW\nThis premium Bali Family Tour and Wellness Retreat is designed as a fully customizable FIT (Flexible Independent Travel) experience. It features high-end private transfers in an executive luxury vehicle, premium handpicked hotels, and a carefully curated daily meal plan emphasizing organic, farm-to-table culinary experiences. Your route seamlessly bridges the tranquil, emerald-green cultural heart of Ubud with the sophisticated, beachside opulence of Seminyak. Every detail reflects the distinct TRAGUIN Curated Experience hallmark, ensuring unforgettable memories. TRAGUIN Luxury Travel WHY CHOOSE THE TRAGUIN PREMIUM BALI EXPERIENCE? Bali remains the world’s most searched destination for holistic wellness, spiritual healing, and high-fashion leisure. Travelers look for the ultimate Bali Honeymoon Package and immersive Bali Sightseeing opportunities to reconnect and capture moments. Ubud, famed for its sweeping rice terraces and artistic heritage, provides the ideal ecosystem for a transformative Yoga Bali Retreat. Meanwhile, Seminyak delivers the premium lifestyle elements—from iconic Instagram locations to legendary golden sunsets. Our itinerary unlocks the Top Tourist Places in Bali, including the iconic sacred monkey forest, Tirta Empul holy spring water temple, breathtaking Tegenungan waterfall, and exclusive beach clubs. Whether it’s participating in a traditional Balinese Melukat purification ritual, shopping for unique handcrafted silver jewelry in local markets, or practicing sunrise yoga overlooking mist-shrouded jungle valleys, this package serves as your definitive guide to the ultimate island escape.\n\nWHY CHOOSE THE TRAGUIN PREMIUM BALI EXPERIENCE?\nBali remains the world’s most searched destination for holistic wellness, spiritual healing, and high-fashion leisure. Travelers look for the ultimate Bali Honeymoon Package and immersive Bali Sightseeing opportunities to reconnect and capture moments. Ubud, famed for its sweeping rice terraces and artistic heritage, provides the ideal ecosystem for a transformative Yoga Bali Retreat. Meanwhile, Seminyak delivers the premium lifestyle elements—from iconic Instagram locations to legendary golden sunsets. Our itinerary unlocks the Top Tourist Places in Bali, including the iconic sacred monkey forest, Tirta Empul holy spring water temple, breathtaking Tegenungan waterfall, and exclusive beach clubs. Whether it’s participating in a traditional Balinese Melukat purification ritual, shopping for unique handcrafted silver jewelry in local markets, or practicing sunrise yoga overlooking mist-shrouded jungle valleys, this package serves as your definitive guide to the ultimate island escape.',
        seo_title='ID-014 | Luxury Yoga & Wellness Bali Retreat | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Bali package (ID-014 / TRG-BALI-WELLNESS-014): Ubud (4N) • Seminyak (2N)IDEAL FOR: Wellness Seekers, Families & with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • THE JOURNEY INTO TRANQUILITY BEGINS', 1),
            _ih('Day 02: MORNING VINYASA YOGA & SACRED BALINESE PURIFICATION RITUAL', 2),
            _ih('Day 03: SPIRITUAL HEALING, SPA THERAPY & GASTRONOMIC EXPLORATION', 3),
            _ih('Day 04: MT. BATUR SUNRISE TREK OR SCENIC WATERFALL SAFARI', 4),
            _ih('Day 05: TRANSITION TO SEMINYAK • ICONIC TANAH LOT SUNSET', 5),
            _ih('Day 06: COASTAL YOGA, BEACHFRONT LEISURE & SUNSET CATAMARAN', 6),
            _ih('Day 07: FAREWELL BALI • DEPARTURE WITH UNFORGETTABLE MEMORIES', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • THE JOURNEY INTO TRANQUILITY BEGINS',
                (
                    'Arrive at Ngurah Rai International Airport in Denpasar, where you will experience a seamless VIP welcome. Your dedicated TRAGUIN luxury consultant and private chauffeur will greet you at the arrival terminal with customized welcome amenities. Settle into your premium executive vehicle and enjoy a scenic, comfortable drive to Ubud, the spiritual and cultural heart of Bali. As the urban landscape transitions into emerald-green vistas, feel the tranquil energy of the island instantly put your mind at ease. Arrive at your ultra-luxury resort, complete an exclusive in-villa check-in, and spend the afternoon unwinding in your private infinity pool overlooking the lush river valley. venue.'
                ),
                [
                    'Sightseeing Included: VIP Airport Meet & Greet, Scenic Private Transfer to Ubud.',
                    "Evening Experience: An intimate, candlelit organic welcome dinner at the resort's signature fine-dining",
                    'Overnight Stay: Premium Handpicked Luxury Resort in Ubud (e.g., Maya Ubud Resort / Viceroy Bali).',
                    'Meals Included: Dinner.',
                ],
            ),
            _day(
                2,
                'MORNING VINYASA YOGA & SACRED BALINESE PURIFICATION RITUAL',
                (
                    'Awaken your senses with an invigorating sunrise Vinyasa yoga session inside a breathtaking open-air bamboo shala, guided by a master yogi. Following a nutritious, farm-fresh breakfast, journey to the historic Tirta Empul Holy Water Temple. Here, participate in a deeply moving, traditional Melukat purification ceremony, bathing in crystalline spring waters to cleanse your aura. In the afternoon, explore the iconic Tegalalang Rice Terraces—a world-famous Instagram location—where you can capture striking photographs TRAGUIN Luxury Travel on a private valley swing. Conclude the afternoon with an immersive stroll through the Sacred Monkey Forest Sanctuary.'
                ),
                [
                    'Sightseeing Included: Tirta Empul Holy Temple, Tegalalang Rice Terraces, Sacred Monkey Forest.',
                    'Optional Activities: Private sound healing session at the Pyramids of Chi.',
                    'Evening Experience: Leisurely walk through Ubud Art Market followed by a gourmet vegan-fusion dinner.',
                    'Overnight Stay: Premium Handpicked Luxury Resort in Ubud.',
                    'Meals Included: Breakfast & Lunch.',
                ],
            ),
            _day(
                3,
                'SPIRITUAL HEALING, SPA THERAPY & GASTRONOMIC EXPLORATION',
                (
                    "Dedicate your morning to holistic restoration. Partake in a personalized Hatha yoga and meditation session aimed at calming the nervous system. Afterward, surrender to a blissful, 120-minute signature Balinese massage and organic body scrub at an award-winning luxury spa. In the afternoon, delve into Bali's culinary heritage with an exclusive farm-to-table cooking masterclass. Handpick fresh herbs and spices from an organic garden and learn the traditional methods of preparing authentic, nutrient-rich Balinese delicacies. Mozaic restaurant."
                ),
                [
                    'Sightseeing Included: Ubud Traditional Arts, Luxury Wellness Spa Experience.',
                    'Optional Activities: Private consultation with a traditional Balinese healer (Balian).',
                    'Evening Experience: Fine-dining multi-course culinary experience at the world-renowned Locavore or',
                    'Overnight Stay: Premium Handpicked Luxury Resort in Ubud.',
                    'Meals Included: Breakfast & Lunch (Self-Prepared).',
                ],
            ),
            _day(
                4,
                'MT. BATUR SUNRISE TREK OR SCENIC WATERFALL SAFARI',
                (
                    'An exhilarating day of adventure awaits. Opt for an early morning, premium guided trek up Mount Batur to witness a dramatic sunrise over the volcanic caldera and Lake Batur, complete with a gourmet breakfast served at the summit. Alternatively, choose a relaxed, premium waterfall safari to the majestic Hidden Canyons and Tukad Cepung Waterfall, where morning sunbeams dance magically through a cave opening. Spend your afternoon at leisure, shopping for premium linen apparel, handmade boutique goods, and exquisite ceramics along Ubud’s chic avenues. TRAGUIN Luxury Travel Evening Experience: Relaxed acoustic evening at a boutique lounge in Ubud center.'
                ),
                [
                    'Sightseeing Included: Choice of Mt. Batur Sunrise Trek OR Tukad Cepung & Tegenungan Waterfalls.',
                    'Optional Activities: White-water rafting along the pristine Ayung River with a luxury picnic setup.',
                    'Overnight Stay: Premium Handpicked Luxury Resort in Ubud.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'TRANSITION TO SEMINYAK • ICONIC TANAH LOT SUNSET',
                (
                    "Bid farewell to the serene jungle as you check out from Ubud. Travel via your luxury private vehicle toward the sophisticated coastal paradise of Seminyak. En route, stop at the magnificent Royal Temple of Mengwi (Taman Ayun), a stunning architectural marvel surrounded by wide moats. Arrive in Seminyak, check into your ultra-luxury beachfront resort, and feel the vibrant, cosmopolitan seaside energy. In the late afternoon, proceed to the iconic Tanah Lot Temple, perched dramatically on a wave-swept rock formation in the ocean, to witness one of the world's most spectacular and legendary sunsets. cocktails. Bali)."
                ),
                [
                    'Sightseeing Included: Taman Ayun Temple, Tanah Lot Temple Sunset Expedition.',
                    'Optional Activities: Surfing lessons with a certified private instructor on Seminyak Beach.',
                    'Evening Experience: VIP access to an elite beachfront lounge like Potato Head or Ku De Ta for dinner and',
                    'Overnight Stay: Ultra-Luxury Beachfront Resort in Seminyak (e.g., The Seminyak Beach Resort / W',
                    'Meals Included: Breakfast & Lunch.',
                ],
            ),
            _day(
                6,
                'COASTAL YOGA, BEACHFRONT LEISURE & SUNSET CATAMARAN',
                (
                    "CRUISE Greet your final full day on the island with a rejuvenating beachside Yin Yoga session, listening to the rhythmic soothing crash of the Indian Ocean waves. Spend your morning shopping at Seminyak’s upscale fashion boutiques, designer flagships, and artisanal art galleries. In the afternoon, embark on an exclusive, private luxury catamaran cruise. Sail along Bali's dramatic southern coastline, enjoy snorkeling in turquoise waters, and toast to an unforgettable trip with a premium gourmet seafood barbecue dinner served on board as the sun dips below the horizon. TRAGUIN Luxury Travel Meals Included: Breakfast & Dinner Cruise."
                ),
                [
                    'Sightseeing Included: Coastal Yoga, Seminyak Premium Shopping Streets, Private Sunset Cruise.',
                    'Optional Activities: Pre-dinner modern Balinese spa ritual.',
                    'Evening Experience: Farewell premium beach party celebrations or fine dining.',
                    'Overnight Stay: Ultra-Luxury Beachfront Resort in Seminyak.',
                ],
            ),
            _day(
                7,
                'FAREWELL BALI • DEPARTURE WITH UNFORGETTABLE MEMORIES',
                (
                    'Savor a decadent, final floating breakfast in your private pool or a relaxed breakfast at the ocean-facing restaurant. Enjoy a morning at leisure for last-minute souvenir shopping or a final walk along the golden sand beach. At the designated time, your TRAGUIN private chauffeur will arrive to provide a comfortable transfer back to Ngurah Rai International Airport for your departure flight, carrying with you refreshed energy, peace of mind, and beautiful memories.'
                ),
                [
                    'Sightseeing Included: Private Departure Transfer.',
                    'Optional Activities: Airport VIP Premium Lounge access booking via TRAGUIN.',
                    'Evening Experience: Onward Journey.',
                    'Overnight Stay: N/A.',
                    'Meals Included: Breakfast.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Alaya Resort Ubud Deluxe Room The Haven Seminyak Suite Room CP (Breakfast Only)',
                'Multi-city Bali',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Alaya Resort Ubud Deluxe Room The Haven Seminyak Suite Room CP (Breakfast Only)',
            ),
            _hotel(
                'Maya Ubud Resort & Spa Impression Forest Valley Suite The Seminyak Beach Resort The Garden Suite MAP (Breakfast & Dinner)',
                'Multi-city Bali',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Maya Ubud Resort & Spa Impression Forest Valley Suite The Seminyak Beach Resort The Garden Suite MAP (Breakfast & Dinner',
            ),
            _hotel(
                'Viceroy Bali Ubud Pool Villa W Bali - Seminyak Wonderful Garden Escape Villa MAP (Breakfast & Curated Dining)',
                'Multi-city Bali',
                '6N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Viceroy Bali Ubud Pool Villa W Bali - Seminyak Wonderful Garden Escape Villa MAP (Breakfast & Curated Dining)',
            ),
            _hotel(
                'Mandapa, a Ritz-Carlton Reserve One Bedroom Pool Villa The Legian Bali Beachfront Studio Suite As Per Curated Gourmet Menu',
                'Multi-city Bali',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandapa, a Ritz-Carlton Reserve One Bedroom Pool Villa The Legian Bali Beachfront Studio Suite As Per Curated Gourmet Me',
            )
        ],
        inclusions=[
            _inc_included('Luxury Accommodation at handpicked hotels', 1),
            _inc_included('All VIP entry tickets, parking fees, and fuel taxes', 2),
            _inc_included('Luxury Accommodation at handpicked hotels', 3),
            _inc_excluded('International or domestic flight tickets', 4),
            _inc_excluded('Indonesian Visa on Arrival (VoA) fees', 5),
            _inc_excluded('Optional tours and non-itinerary activities', 6),
            _inc_excluded('Travel and health insurance coverage', 7),
            _inc_excluded('Tipping/Gratuites for drivers and local guides', 8),
            _inc_excluded('Any meals or beverages not explicitly detailed', 9),
            _inc_excluded('International or domestic flight tickets', 10),
        ],
    )
    return package, itinerary

def build_id_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-015'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Ultimate Bali Luxury Escapes'
    duration = '08 NIGHTS / 09 DAYS'
    slug = 'id-015-ultimate-bali-luxury-escapes'
    itin_slug = 'id-015-ultimate-bali-luxury-escapes-itinerary'
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
            _ph('Serial code ID-015 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: ULTIMATE BALI LUXURY ESCAPES • 08 NIGHTS / 09', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7),
            _ph('TRAGUIN Signature Experiences: Enjoy pre-arranged VIP front-row seating allocations at the Uluwatu', 8)
        ],
        moods=['Luxury'],
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
        tagline='Ultimate Bali Luxury Escapes',
        overview="ULTIMATE BALI LUXURY ESCAPES • 08 NIGHTS / 09 DAYS Welcome to an extraordinary journey beautifully orchestrated by TRAGUIN. Immerse yourself in the timeless elegance of paradise with our bespoke Bali Honeymoon Package and elite Bali Family Tour options. From the mystical, mist-veiled rainforests of Ubud to the sun-kissed, ultra-exclusive clifftops of Uluwatu, this meticulously Luxury Bali Holiday layout promises seamless execution, private curated experiences, and moments that transform into unforgettable memories. SERIAL CODE ID-015 TOUR CODE TRAGUIN- BALI-015 STATE / COUNTRY Bali / Indonesia CATEGORY Luxury / Ultra Premium DURATION 08 Nights / 09 Days DESTINATIONS Ubud (4N) • Seminyak / TRAGUIN Premium Luxury Holidays 1\n\nTOUR OVERVIEW\nDesigned exclusively for discerning travelers, the Best Bali Tour Package by TRAGUIN synthesizes cultural immersion with undisturbed seaside relaxation. Your journey begins in the artistic and spiritual beating heart of Ubud, surrounded by terraced emerald valleys and traditional architectural marvels. Transition effortlessly to South Bali's ultra-luxury beach enclaves, where premium stays, trendy beach clubs, and iconic sunset horizons await. This Premium Bali Experience includes high-end private transport, expert local English- speaking hosts, and personalized access keys to highly restricted signature events.\n\nWHY CHOOSE TRAGUIN LUXURY BALI HOLIDAY?\nBali, widely praised as the Island of the Gods, remains a leading global destination for luxury lifestyle seekers. When booking your TRAGUIN Bali Packages, you gain immediate entry to high-value, highly searched tourism activities across the mainland. Famous Attractions & Experiences: Discover the timeless aesthetics of the iconic Tegalalang Rice Terraces, the majestic sea temple of Tanah Lot, and the soaring clifftops of Uluwatu. Experience the thrill of the Bali Swing over pristine jungle canopies, submerge in spiritual purification rituals at Pura Tirta Empul, or explore the underwater ecosystems of Nusa Penida. Instagram Locations & Shopping: Capture breathtaking visuals at the Lempuyang Heaven’s Gate or the neon-infused infinity pools of world-renowned beach clubs like Atlas Beach Fest and Potato Head. For shopping connoisseurs, the high-fashion boutiques of Seminyak and artisanal woodworking markets of Ubud offer unparalleled souvenir choices. Whether it's a dedicated Bali Honeymoon Package or an expansive Bali Family Tour, the island guarantees a multifaceted tapestry of adventure, wellness, and culinary perfection. Nusa Dua (4N) IDEAL FOR Connoisseurs, Couples, Families BEST SEASON April to October (Dry Season) VEHICLE TYPE Private Luxury Alphard / Toyota Innova Reborn MEAL PLAN Breakfast Included (BB) + Special Dynamic Dining TRAGUIN Premium Luxury Holidays 2",
        seo_title='ID-015 | Ultimate Bali Luxury Escapes | TRAGUIN',
        seo_description='Premium 08 NIGHTS / 09 DAYS Bali package (ID-015 / TRAGUIN-BALI-000): ULTIMATE BALI LUXURY ESCAPES • 08 NIGHTS / 09 with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • WELCOME TO PARADISE (UBUD)', 1),
            _ih('Day 02: UBUD CULTURAL HEARTLAND & ICONIC BALI SWING', 2),
            _ih('Day 03: MYSTICAL TEMPLES & SPIRITUAL PURIFICATION EXPERIENCE', 3),
            _ih('Day 04: VOLCANO VIEWING AT KINTAMANI & COFFEE PLANTATION TOUR', 4),
            _ih('Day 05: UBUD TO SEMINYAK • TANAH LOT SEA TEMPLE SUNSET', 5),
            _ih('Day 06: EXCLUSIVE NUSA PENIDA ISLAND PRIVATE SPEEDBOAT EXCURSION', 6),
            _ih('Day 07: SUNNY BEACH DAY • PREMIUM BEACH CLUBBED LUXURY', 7),
            _ih('Day 08: ULUWATU CLIFF TEMPLE, KECAK DANCE & JIMBARAN BAY DINNER', 8),
            _ih('TRAGUIN Signature Experiences: Enjoy pre-arranged VIP front-row seating allocations at the Uluwatu', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • WELCOME TO PARADISE (UBUD)',
                (
                    'Step off your flight into the warm, tropical embrace of Denpasar International Airport. Your dedicated TRAGUIN Luxury Concierge awaits you at the arrival terminal with custom name signage, refreshing cold towels, and traditional Balinese frangipani garlands. Board your private luxury vehicle and enjoy a smooth transfer up the scenic foothills to your handpicked resort in Ubud. As you check into your private pool villa, enjoy premium welcome amenities while looking out over breathtaking landscapes of undisturbed rainforest canopies.'
                ),
                [
                    'Sightseeing Included: Smooth Airport VIP Meet & Greet, Scenic Foothill Transfer.',
                    'Evening Experience: Leisure unpacking, intimate candlelit welcome dinner inside the resort villa.',
                    'Overnight Stay: Ubud (Premium Luxury Pool Villa) | Meals Included: Welcome Drink & Dinner',
                ],
            ),
            _day(
                2,
                'UBUD CULTURAL HEARTLAND & ICONIC BALI SWING',
                (
                    'Savor a delightful organic breakfast with views of the mist-covered valleys. Today, dive into the core of Balinese spirituality and adventure. Your private tour guide takes you directly to the legendary Tegalalang Rice Terraces to witness ancient Subak irrigation design up close. Elevate your adrenaline on the high-flying Bali Swing, soaring out over deep emerald gorges for quintessential Instagram photographs. Follow this with a refreshing stop at the crisp Tegenungan Waterfall, and conclude with an afternoon stroll through the Sacred Monkey Forest Sanctuary. Forest.'
                ),
                [
                    'Sightseeing Included: Tegalalang Rice Terraces, Famous Bali Swing, Tegenungan Waterfall, Ubud Monkey',
                    'Optional Activities: White Water Rafting on the Ayung River with a gourmet riverside picnic.',
                    'Overnight Stay: Ubud | Meals Included: Breakfast',
                ],
            ),
            _day(
                3,
                'MYSTICAL TEMPLES & SPIRITUAL PURIFICATION EXPERIENCE',
                (
                    'Today features profound cultural engagement. Travel along scenic, winding country roads to Pura Tirta Empul, a sacred water temple where you can experience a traditional Melukat purification ritual guided by a resident priest. Next, visit Kanto Lampo Waterfall, a spectacular tiered cascade perfect for dramatic photography. Spend your late afternoon discovering the bustling Ubud Traditional Art Market, picking out fine hand-woven silk scarves, organic essential oils, and intricate wood carvings. TRAGUIN Premium Luxury Holidays 3'
                ),
                [
                    'Sightseeing Included: Tirta Empul Holy Water Temple, Kanto Lampo Tiered Waterfall, Ubud Art Market.',
                    'Evening Experience: Traditional Royal Legong Dance Performance at Ubud Palace.',
                    'Overnight Stay: Ubud | Meals Included: Breakfast',
                ],
            ),
            _day(
                4,
                'VOLCANO VIEWING AT KINTAMANI & COFFEE PLANTATION TOUR',
                (
                    "Embark on a spectacular drive north to Kintamani, a majestic mountain village overlooking the active volcano of Mount Batur and its expansive, glassy crater lake. Enjoy a premium lunch at a panoramic viewing venue, feeling the cool mountain breeze. On your return route, visit an exclusive agro-tourism estate to discover the traditional artisanal creation of Bali's famous Luwak coffee, complemented by a curated tasting flight of exotic organic teas."
                ),
                [
                    'Sightseeing Included: Mount Batur Viewpoint, Kintamani Highlands, Premium Coffee Estate Tour.',
                    'Optional Activities: Sunrise Mount Batur 4x4 Jeep Adventure (requires early morning departure).',
                    'Overnight Stay: Ubud | Meals Included: Breakfast & Premium Lunch',
                ],
            ),
            _day(
                5,
                'UBUD TO SEMINYAK • TANAH LOT SEA TEMPLE SUNSET',
                (
                    'Bid farewell to the serene valleys of Ubud as your TRAGUIN Premium Bali Tour Package shifts down to the vibrant beach lifestyle of South Bali. Check into your ultra-luxury beachfront resort in Seminyak or Nusa Dua. In the late afternoon, journey out to the iconic Tanah Lot Temple, a striking offshore rock formation housing an ancient Hindu shrine. Stand on the coast and watch the sun melt beneath the Indian Ocean horizon, illuminating the breaking waves in a deep golden amber hue.'
                ),
                [
                    'Sightseeing Included: Southern Coastline Transfer, Iconic Tanah Lot Sea Temple.',
                    "Evening Experience: Explore Seminyak's world-class culinary strip, dining at acclaimed fine restaurants.",
                    'Overnight Stay: Seminyak / Nusa Dua Beach Resort | Meals Included: Breakfast',
                ],
            ),
            _day(
                6,
                'EXCLUSIVE NUSA PENIDA ISLAND PRIVATE SPEEDBOAT EXCURSION',
                (
                    "Board a fast, private speedboat over to the legendary island of Nusa Penida. Today is dedicated to capturing Bali's most dramatic coastal geology. Walk the spectacular ridge line at Kelingking Beach, famous worldwide for its T-Rex shaped rock formation. Dip your toes into the crystal-clear waters of Broken Beach and swim in Angel’s Billabong, a breathtaking natural infinity pool carved seamlessly into the coastal rock. Return to mainland Bali by late afternoon to relax. TRAGUIN Premium Luxury Holidays 4"
                ),
                [
                    "Sightseeing Included: Kelingking Beach, Broken Beach, Angel's Billabong, Private Speedboat Transfers.",
                    'Optional Activities: Snorkeling with Majestic Manta Rays at Crystal Bay.',
                    'Overnight Stay: Seminyak / Nusa Dua | Meals Included: Breakfast & Packed Beachside Lunch',
                ],
            ),
            _day(
                7,
                'SUNNY BEACH DAY • PREMIUM BEACH CLUBBED LUXURY',
                (
                    'Enjoy a completely unscheduled, blissful day to embrace the true spirit of a Luxury Bali Holiday. Wake up late, order a floating breakfast to your private pool, or treat yourself to a world-class holistic multi-hour Balinese massage treatment. In the afternoon, take advantage of VIP access reservations secured by TRAGUIN Experts at an elite beach club like Atlas Beach Fest or Potato Head. Sip premium cocktails on a private daybed while listening to chilled house music against a backdrop of breaking surf.'
                ),
                [
                    'Sightseeing Included: Premium Beachfront Daybed Access.',
                    "Optional Activities: Professional couples' spa therapy, private surfing coaching session.",
                    'Overnight Stay: Seminyak / Nusa Dua | Meals Included: Breakfast',
                ],
            ),
            _day(
                8,
                'ULUWATU CLIFF TEMPLE, KECAK DANCE & JIMBARAN BAY DINNER',
                (
                    'Your penultimate day on the island delivers unforgettable dramatic highlights. Travel to the southernmost tip of Bali to explore Uluwatu Temple, perched precariously on a sheer cliff face 70 meters above the roaring Indian Ocean. At sunset, watch an immersive, emotionally captivating performance of the traditional Kecak Fire Dance inside an open-air cliffside amphitheater. Conclude this beautiful evening with a candlelit, toes-in-the- sand seafood dinner along the iconic arc of Jimbaran Bay.'
                ),
                [
                    'Sightseeing Included: Uluwatu Cliff Temple, Sunset Kecak Fire Dance, Jimbaran Bay Beachfront Dining.',
                    'Evening Experience: Toast to your journey with fine wines directly on the beach.',
                    'Overnight Stay: Seminyak / Nusa Dua | Meals Included: Breakfast & Premium Seafood Dinner',
                ],
            ),
            _day(
                9,
                'LASTRADITIONAL SOUVENIRS & FOND FAREWELLS',
                (
                    'Indulge in your final gourmet breakfast overlooking the ocean. Spend your last morning gathering exquisite souvenirs from the trendy boutiques of Seminyak or a final stop at a premium handicraft emporium. At the designated hour, your private luxury transport arrives to escort you in absolute comfort to Denpasar International Airport for your homeward journey, carrying a treasure trove of unforgettable memories curated meticulously by TRAGUIN. TRAGUIN Premium Luxury Holidays 5 Best Time to Visit Note: April through October provides glorious, uninterrupted daily sunshine.'
                ),
                [
                    'Sightseeing Included: Private Departure Airport Transfer.',
                    'Overnight Stay: Departure Flight | Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Alaya Resort Ubud / Sthala Ubud The Haven Seminyak / Merusaka Nusa Dua Deluxe Pool View Room (BB)',
                'Multi-city Bali',
                '8N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Alaya Resort Ubud / Sthala Ubud The Haven Seminyak / Merusaka Nusa Dua Deluxe Pool View Room (BB)',
            ),
            _hotel(
                'The Kayon Resort / Maya Ubud The Seminyak Beach Resort / Courtyard Marriott Premium Garden Villa (BB)',
                'Multi-city Bali',
                '8N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Kayon Resort / Maya Ubud The Seminyak Beach Resort / Courtyard Marriott Premium Garden Villa (BB)',
            ),
            _hotel(
                'Viceroy Bali / Mandapa, a Ritz-Carlton The Legian Seminyak / Mulia Villas Private Luxury Pool Villa (BB)',
                'Multi-city Bali',
                '8N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Viceroy Bali / Mandapa, a Ritz-Carlton The Legian Seminyak / Mulia Villas Private Luxury Pool Villa (BB)',
            ),
            _hotel(
                'Amandari / Hanging Gardens of Bali The Bulgari Resort Bali / Six Senses Uluwatu Signature Panoramic Pool Villa (BB)',
                'Multi-city Bali',
                '8N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Amandari / Hanging Gardens of Bali The Bulgari Resort Bali / Six Senses Uluwatu Signature Panoramic Pool Villa (BB)',
            )
        ],
        inclusions=[
            _inc_included('Private Transportation: Chauffeur-driven luxury AC vehicles.', 1),
            _inc_included('Daily Meals: Gourmet breakfasts plus specialized dinings.', 2),
            _inc_included('VIP Sightseeing: Entry tickets to all mentioned attractions.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest experience helpline.', 4),
            _inc_included('Welcome Amenities: Cold towels, garlands, and complimentary fruit platters.', 5),
            _inc_excluded('PACKAGE INCLUSIONS', 6),
            _inc_excluded('Airfare: International round-trip flights', 7),
            _inc_excluded('Tipping: Gratuities for guides and drivers', 8),
            _inc_excluded('Airfare: International round-trip flights', 9),
            _inc_excluded('Tipping: Gratuities for guides and drivers', 10),
        ],
    )
    return package, itinerary

def build_id_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-016'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Bali Lombok Ultimate Family Vacation'
    duration = '07 NIGHTS / 08 DAYS'
    slug = 'id-016-bali-lombok-ultimate-family-vacation'
    itin_slug = 'id-016-bali-lombok-ultimate-family-vacation-itinerary'
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
            _ph('Serial code ID-016 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Ubud (3N) • Gili', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7),
            _ph('TRAGUIN Signature Experience: Travel with absolute peace of mind. Every family excursion includes', 8)
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
        tagline='Bali Lombok Ultimate Family Vacation',
        overview='ULTIMATE FAMILY VACATION • 07 NIGHTS / 08 DAYS Welcome to an unforgettable exotic escape curated by TRAGUIN Experts. Discover the ultimate balance of culture, dramatic islands, and pristine white-sand shores with our specialized Bali Family Tour and Lombok Tour Package combo. From the vibrant temples and lush jungles of mainland Bali to the untouched tropical paradise of Lombok and the Gili Islands, this bespoke itinerary ensures complete safety, premium stays, and immersive experiences tailored beautifully for multi-generational families. SERIAL CODE ID-016 TRAGUIN TOUR CODETRAGUIN-BAL- LOM-016 STATE / COUNTRY Bali & Lombok / Indonesia CATEGORY Luxury Family Holiday DURATION 07 Nights / 08 Days DESTINATIONS COVERED: Ubud (3N) • Gili Trawangan / Lombok (4N) IDEAL FOR Families, Couples & Multi- generational Groups BEST TIME TO VISIT BALI April to October (Dry and pleasant season) TRAGUIN Premium Family Vacations 1 STARTING PRICE On Request (Premium Customized) VEHICLE Private Luxury AC Innova / Alphard\n\nTOUR OVERVIEW\nThe Best Bali Tour Package combined with Lombok presents a perfect synthesis of island exploration. Your family will enjoy seamless, door-to-door private transitions starting in Bali’s cultural capital, Ubud, where cascading valleys and breathtaking landscapes set a calm pace. From there, cross the sparkling Lombok Strait by private speed vessel to arrive in the Gili Islands and Lombok, known globally for their turquoise waters, missing motorized traffic, and spectacular coral reefs. Enjoy handpicked luxury family resorts, dedicated private guides, and exclusive itineraries prepared meticulously by TRAGUIN.\n\nWHY VISIT BALI & LOMBOK ON A FAMILY TOUR?\nChoosing the right destination for a premium family vacation requires experiences that delight all ages. Our tailored TRAGUIN Bali Packages highlight the top tourist places in Bali and Lombok while avoiding overwhelming crowds. Famous Attractions & Immersive Experiences: In Bali, your family will explore the iconic Tegalalang Rice Terraces, the magical sea temple of Tanah Lot, and participate in spiritual purification rituals. In Lombok, discover the legendary Gili Islands (Gili Trawangan, Meno, and Air), dive into pristine marine sanctuaries with sea turtles, and explore Sasak cultural heritage villages. Most Searched & Instagram Locations: Capture unforgettable family memories at the famous Bali Swing over Ubud’s deep jungles, the white sands of Senggigi beach, and the pink hues of Lombok’s coastlines. With premium child-friendly amenities, curated menus, and safe beachfront relaxation, this is recognized as the ultimate Luxury Bali Holiday layout for modern families.',
        seo_title='ID-016 | Bali Lombok Ultimate Family Vacation | TRAGUIN',
        seo_description='Premium 07 NIGHTS / 08 DAYS Bali package (ID-016 / TRAGUIN-BALI-000): Ubud (3N) • Gili with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • WELCOME TO UBUD RAINFOREST', 1),
            _ih('Day 02: ICONIC UBUD SIGHTSEEING, BALI SWING & MONKEY FOREST', 2),
            _ih('Day 03: HOLY TEMPLES & TANAH LOT SEA TEMPLE SUNSET', 3),
            _ih('Day 04: PREMIUM SPEEDBOAT TO THE GILI ISLANDS (GILI TRAWANGAN)', 4),
            _ih('Day 05: PRIVATE GLASS-BOTTOM BOAT SNORKELING WITH SEA TURTLES', 5),
            _ih('Day 06: MAINLAND LOMBOK • SASAK CULTURAL HERITAGE TOUR', 6),
            _ih('Day 07: SENGGIGI COASTAL ESCAPE & SUNSET DINING', 7),
            _ih('Day 08: DEPARTURE FROM LOMBOK • FOND MEMORIES', 8),
            _ih('TRAGUIN  Signature  Experience: Travel  with  absolute  peace  of  mind.  Every  family  excursion  includes', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • WELCOME TO UBUD RAINFOREST',
                (
                    'Touch down at Denpasar International Airport where your professional TRAGUIN representative greets your family with cold refreshments and local floral leis. Relax inside your private luxury transport as you pass scenic rural roads up into the highlands of Ubud. Check into your premium handpicked resort, offering breathtaking landscapes of untouched valleys. Spend the evening resting and adjusting to the beautiful tropical air. TRAGUIN Premium Family Vacations 2'
                ),
                [
                    'Sightseeing Included: VIP Airport Meet & Private Transfer.',
                    'Evening Experience: Relaxed unpacking followed by an authentic Balinese family dinner.',
                    'Overnight Stay: Ubud | Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'ICONIC UBUD SIGHTSEEING, BALI SWING & MONKEY FOREST',
                (
                    'Enjoy an early breakfast overlooking the valley mist. Your private guide takes you to the historic Tegalalang Rice Terraces to witness ancient farming systems. Experience the thrill of the iconic Bali Swing over deep forest canopies (highly safe and secured for families). Later, walk together through the shaded canopies of the Sacred Monkey Forest Sanctuary, capturing wonderful photography points with the playful macaques.'
                ),
                [
                    'Sightseeing Included: Tegalalang Rice Terraces, Bali Swing, Ubud Monkey Forest, Ubud Art Market.',
                    'Optional Activities: Family cooking masterclass using organic local herbs.',
                    'Overnight Stay: Ubud | Meals Included: Breakfast',
                ],
            ),
            _day(
                3,
                'HOLY TEMPLES & TANAH LOT SEA TEMPLE SUNSET',
                (
                    'Dive into the rich culture of mainland Bali. Today your family visits Pura Tirta Empul for an immersive experience observing traditional holy spring water cleansing rituals. In the afternoon, head toward the southwest coast to witness the dramatic Tanah Lot Temple, resting on an offshore volcanic rock. Watch a breathtaking sunset over the Indian Ocean as waves gently crash against the ancient temple walls.'
                ),
                [
                    'Sightseeing Included: Tirta Empul Holy Water Temple, Tegenungan Waterfall, Tanah Lot Sea Temple.',
                    'Evening Experience: Authentic seafood dining at a premium beachfront cafe.',
                    'Overnight Stay: Ubud | Meals Included: Breakfast',
                ],
            ),
            _day(
                4,
                'PREMIUM SPEEDBOAT TO THE GILI ISLANDS (GILI TRAWANGAN)',
                (
                    'Bid farewell to Bali as you board a high-speed premium vessel from Padang Bai harbor across to Gili Trawangan. Since motorized vehicles are restricted on the Gilis, your family will travel to the resort by a charming traditional horse-drawn cart (Cidomo). Check into your premium luxury beach villa. Spend the afternoon cycling along the sandy paths or relaxing on the white shoreline. TRAGUIN Premium Family Vacations 3'
                ),
                [
                    'Sightseeing Included: Inter-island Speedboat Transfer, Cidomo Village Ride.',
                    'Evening Experience: Unwind at a beachfront bonfire lounge under a starlit island sky.',
                    'Overnight Stay: Gili Trawangan | Meals Included: Breakfast',
                ],
            ),
            _day(
                5,
                'PRIVATE GLASS-BOTTOM BOAT SNORKELING WITH SEA TURTLES',
                (
                    'Board a private glass-bottom boat chartered exclusively by TRAGUIN for a magnificent three-island snorkeling tour around Gili Trawangan, Gili Meno, and Gili Air. Explore world-famous underwater coral sculptures and swim alongside gentle wild sea turtles in crystal-clear waters. Stop at a quiet beach on Gili Air for a fresh grilled fish lunch before returning to your resort.'
                ),
                [
                    'Sightseeing Included: Three Gili Islands Snorkeling, Underwater Statue Coral Reefs.',
                    'Food Suggestions: Freshly caught lime-marinated snapper at an open-air oceanfront bistro.',
                    'Overnight Stay: Gili Trawangan | Meals Included: Breakfast & Beachside Lunch',
                ],
            ),
            _day(
                6,
                'MAINLAND LOMBOK • SASAK CULTURAL HERITAGE TOUR',
                (
                    'Take a short boat ride to mainland Lombok. Today is dedicated to discovering the rich culture of the Sasak people. Visit a traditional Sasak tribal village to view unique thatched architecture and watch local women weave fine Ikat textiles by hand. Continue to the stunning Kuta Beach Lombok to admire its expansive coastal vistas and unique pepper-like white sand grains.'
                ),
                [
                    'Sightseeing Included: Lombok Mainland Transition, Sasak Cultural Village, Kuta Lombok Beach.',
                    'Photography Points: Merese Hill, looking out over matching turquoise bays.',
                    'Overnight Stay: Senggigi / South Lombok Beach | Meals Included: Breakfast',
                ],
            ),
            _day(
                7,
                'SENGGIGI COASTAL ESCAPE & SUNSET DINING',
                (
                    'Enjoy a completely free, leisurely day at your luxury beachfront resort in Senggigi. This day is designed for your family to fully enjoy premium stays, infinity pools, and top-tier spa facilities. Walk along the tranquil sands of Senggigi Beach, far away from commercial tourist rush, allowing your children to swim safely in the calm coastal waters.'
                ),
                [
                    'Sightseeing Included: Relaxed Resort Beach Access.',
                    "Optional Activities: Surfing lessons for beginners on Lombok's gentle reef breaks.",
                    'Overnight Stay: Senggigi / Lombok Beach | Meals Included: Breakfast',
                ],
            ),
            _day(
                8,
                'DEPARTURE FROM LOMBOK • FOND MEMORIES',
                (
                    'Savor your final gourmet tropical breakfast. Pack your hand-woven souvenirs and premium artisanal gifts. At the designated time, your private luxury transport transfers your family safely to Lombok International Airport TRAGUIN Premium Family Vacations 4 (LOP) for your flight back home, carrying unforgettable memories of an extraordinary holiday curated flawlessly by TRAGUIN. Best Time to Visit Note: The dry season ensures glorious blue skies and excellent sea visibility.'
                ),
                [
                    'Sightseeing Included: Private Departure Airport Transfer.',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Alaya Resort UbudPearl of Trawangan Katamaran Resort (Ocean View)',
                'Multi-city Bali',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Alaya Resort UbudPearl of Trawangan Katamaran Resort (Ocean View)',
            ),
            _hotel(
                'The Kayon Resort Ponte Villas Gili The Jayakarta Lombok',
                'Multi-city Bali',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Kayon Resort Ponte Villas Gili The Jayakarta Lombok',
            ),
            _hotel(
                'Maya Ubud Resort & Spa Villa Ombak (Luxury Pool)Sheraton Senggigi Beach Resort',
                'Multi-city Bali',
                '7N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Maya Ubud Resort & Spa Villa Ombak (Luxury Pool)Sheraton Senggigi Beach Resort',
            ),
            _hotel(
                'Viceroy Bali / Mandapa The Oberoi Beach Resort Lombok The Lombok Lodge / Sudamala Resort',
                'Multi-city Bali',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Viceroy Bali / Mandapa The Oberoi Beach Resort Lombok The Lombok Lodge / Sudamala Resort',
            )
        ],
        inclusions=[
            _inc_included('07 Nights Stay: Selected luxury family properties', 1),
            _inc_included('Snorkeling Trip: Private glass-bottom boat charter', 2),
            _inc_included('07 Nights Stay: Selected luxury family properties', 3),
            _inc_included('Snorkeling Trip: Private glass-bottom boat charter', 4),
            _inc_excluded('PACKAGE INCLUSIONS', 5),
            _inc_excluded('Flights: International/domestic flights', 6),
            _inc_excluded('Visa Costs: Visa on Arrival fees', 7),
            _inc_excluded('Insurance: Comprehensive medical travel cover', 8),
            _inc_excluded('Tipping: Gratuities for local drivers and boatmen', 9),
            _inc_excluded('Flights: International/domestic flights', 10),
            _inc_excluded('Visa Costs: Visa on Arrival fees', 11),
            _inc_excluded('Insurance: Comprehensive medical travel cover', 12),
            _inc_excluded('Tipping: Gratuities for local drivers and boatmen', 13),
        ],
    )
    return package, itinerary

def build_id_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-017'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Luxury Couple Bali Package'
    duration = '06 NIGHTS / 07 DAYS'
    slug = 'id-017-luxury-couple-bali-package'
    itin_slug = 'id-017-luxury-couple-bali-package-itinerary'
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
            _ph('Serial code ID-017 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Ubud (3', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7),
            _ph("TRAGUIN Signature Couples' Experiences: Enjoy pre-arranged VIP entry keys that bypass all public", 8),
            _ph('TRAGUIN Support: 24/7 dedicated on-ground', 9),
            _ph('TRAGUIN Premium Travel | Luxury Honeymoon Experts 5', 10)
        ],
        moods=['Luxury', 'Honeymoon'],
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
        tagline='Luxury Couple Bali Package',
        overview="BESPOKE ROMANTIC ESCAPES • 06 NIGHTS / 07 DAYS Welcome to an exceptionally romantic journey orchestrated by TRAGUIN Experts. Immerse yourselves in the absolute epitome of tropical intimacy with our signature Bali Honeymoon Package layout. From the misty, lush green ravines of Ubud where infinity pools merge seamlessly into jungle canopies, to the dramatic clifftops and golden sandy beaches of Uluwatu and Seminyak, this tailored Luxury Bali Holiday ensures curated experiences, complete couples' privacy, and unforgettable memories that linger forever. SERIAL CODE ID-017 TRAGUIN TOUR CODETRAGUIN- BALI-CP-017 STATE / COUNTRY Bali / Indonesia CATEGORY Premium Romantic Luxury / Honeymoon DURATION 06 Nights / 07 Days DESTINATIONS COVERED: Ubud (3 Nights) • Seminyak / Jimbaran (3 Nights) TRAGUIN Premium Travel | Luxury Honeymoon Experts 1 IDEAL FOR Couples, Honeymooners, Anniversary Celebrations BEST TIME TO VISIT BALI April to October (Dry and sun-kissed season) STARTING PRICE On Request (Exclusive Premium Curation) VEHICLE Private Luxury Chauffeur Alphard / Innova Reborn\n\nTOUR OVERVIEW\nThe Best Bali Tour Package for couples is meticulously curated to blend unhurried personal relaxation with immersive, romantic cultural discovery. Your journey begins with a 3-night stay in the artistic soul of the island —Ubud—residing in handpicked luxury pool villas that offer unparalleled romantic privacy. Transition down south to the vibrant upscale coastlines of Seminyak or Jimbaran for another 3 nights of breathtaking landscapes, elite beach clubs, and iconic temple sunsets. Experience personalized daily luxury transportation, candlelit fine-dining encounters, and seamless execution with TRAGUIN support. THE MAGIC OF A LUXURY BALI HOLIDAY FOR COUPLES Bali is universally recognized as one of the world's most romantic islands. By choosing our dedicated TRAGUIN Bali Packages, couples unlock access to unforgettable locations and high-end aesthetic experiences designed to strengthen connections. Famous Attractions & Intimate Experiences: Walk hand-in-hand through the iconic Tegalalang Rice Terraces, capture dramatic photographs on the high-soaring Bali Swing, and find tranquility at the sacred water temple of Tirta Empul. Witness the breathtaking offshore Tanah Lot Temple at dusk, and see the ancient clifftop Uluwatu Temple overlooking a roaring ocean horizon. Top Tourist Places & Instagram Spots: From floating villa breakfasts in your private pool to spectacular seaside dining at Jimbaran Bay, every moment creates a sensory story. Take romantic sunset strolls through Seminyak's boutique streets, capture stunning photos at Kanto Lampo Waterfall, or indulge in side-by-side Balinese spa treatments. This is the ultimate Premium Bali Experience tailored for couples seeking elegance, sophistication, and pure magic.",
        seo_title='ID-017 | Luxury Couple Bali Package | TRAGUIN',
        seo_description='Premium 06 NIGHTS / 07 DAYS Bali package (ID-017 / TRAGUIN-BALI-000): Ubud (3 with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • ROMANTIC PRIVATE VILLA WELCOME', 1),
            _ih('Day 02: UBUD HIGHLANDS, BALI SWING & EMERALD RICE TERRACES', 2),
            _ih('Day 03: MYSTICAL WATERFALLS & HOLY WATER PURIFICATION COUPLING', 3),
            _ih('Day 04: UBUD TO SEMINYAK COASTLINE • TANAH LOT SEA TEMPLE SUNSET', 4),
            _ih('Day 05: EXCLUSIVE SUN-KISSED DAY AT AN ELITE BEACH CLUB', 5),
            _ih('Day 06: ULUWATU CLIFF TEMPLE, KECAK FIRE DANCE & JIMBARAN SEAFOOD DINNER', 6),
            _ih('Day 07: SOUVENIRS SHOPPING & FOND FAREWELL TO PARADISE', 7),
            _ih("TRAGUIN  Signature  Couples'  Experiences: Enjoy  pre-arranged  VIP  entry  keys  that  bypass  all  public", 8),
            _ih('TRAGUIN Support: 24/7 dedicated on-ground', 9),
            _ih('TRAGUIN Premium Travel | Luxury Honeymoon Experts 5', 10)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • ROMANTIC PRIVATE VILLA WELCOME',
                (
                    'TRAGUIN Premium Travel | Luxury Honeymoon Experts 2 Arrive together at Denpasar International Airport where your private TRAGUIN Luxury Concierge awaits at the VIP exit. Receive traditional Balinese frangipani garlands, cold towels, and a refreshing tropical beverage before boarding your private luxury car. Ascend through emerald countryside roads to your handpicked rainforest resort in Ubud. Check into your ultra-private luxury pool villa, beautifully decorated with complimentary honeymoon floral art. oasis.'
                ),
                [
                    'Sightseeing Included: Airport VIP Welcome, Private Luxury Transfer.',
                    'Evening Experience: Leisure unpacking followed by a romantic candlelit dinner served inside your private villa',
                    'Overnight Stay: Ubud (Private Pool Villa Tier) | Meals Included: Welcome Drink & Dinner',
                ],
            ),
            _day(
                2,
                'UBUD HIGHLANDS, BALI SWING & EMERALD RICE TERRACES',
                (
                    "Awake to the soothing sounds of the jungle and savor your first iconic floating breakfast in your private pool. Today, discover the breathtaking landscapes of Ubud. Walk through the ancient multi-tiered Tegalalang Rice Terraces, capturing gorgeous couples' photos. Next, feel the thrill of the famous Bali Swing, soaring over deep rainforest valleys. Conclude the afternoon with a peaceful stroll through the Sacred Monkey Forest Sanctuary."
                ),
                [
                    'Sightseeing Included: Tegalalang Rice Terraces, Bali Swing Adventure, Ubud Monkey Forest, Art Market.',
                    'Photography Points: Mid-air on the Bali Swing with panoramic valley backdrops.',
                    'Overnight Stay: Ubud | Meals Included: Floating Breakfast',
                ],
            ),
            _day(
                3,
                'MYSTICAL WATERFALLS & HOLY WATER PURIFICATION COUPLING',
                (
                    "Immerse yourselves in Bali's rich cultural heritage. Travel along beautiful country roads to the sacred water temple of Pura Tirta Empul. Participate together in a traditional Melukat water purification ritual led by a local priest. Later, visit Kanto Lampo Waterfall, a spectacular cascading waterfall perfect for stunning artistic photography. Spend your evening exploring Ubud's intimate candlelit cafes and artisanal markets."
                ),
                [
                    'Sightseeing Included: Tirta Empul Temple Ritual, Kanto Lampo Waterfall, Ubud Palace.',
                    "Optional Activities: A private couple's holistic wellness and sound healing session in Ubud.",
                    'Overnight Stay: Ubud | Meals Included: Breakfast',
                ],
            ),
            _day(
                4,
                'UBUD TO SEMINYAK COASTLINE • TANAH LOT SEA TEMPLE SUNSET',
                (
                    "Bid farewell to the serene valleys of Ubud as your TRAGUIN Premium Bali Tour Package moves to the stylish southwest coast. Check into an ultra-luxury beach resort in Seminyak or Jimbaran. In the late afternoon, your chauffeur takes you to the iconic Tanah Lot Temple, built on a jagged offshore rock formation. Watch a glorious golden sunset over the Indian Ocean as waves crash gently against the temple's base. TRAGUIN Premium Travel | Luxury Honeymoon Experts 3 beachfront lounge."
                ),
                [
                    'Sightseeing Included: South Bali Transfer, Iconic Tanah Lot Sea Temple.',
                    "Evening Experience: Stroll through Seminyak's high-end boutique streets and enjoy premium cocktails at a stylish",
                    'Overnight Stay: Seminyak / Jimbaran Beach Resort | Meals Included: Breakfast',
                ],
            ),
            _day(
                5,
                'EXCLUSIVE SUN-KISSED DAY AT AN ELITE BEACH CLUB',
                (
                    "Enjoy a blissfully free day dedicated entirely to unhurried relaxation, a true hallmark of a Luxury Bali Holiday. Lounge together under a private cabana at one of Bali's most famous beach clubs, such as Atlas Beach Fest or Potato Head. Listen to chilled house music, dip into oceanfront infinity pools, and sip curated tropical cocktails as you watch the surf roll onto the shore."
                ),
                [
                    'Sightseeing Included: Premium Beach Club Access & Reserved Daybed Day.',
                    "Optional Activities: A multi-hour luxurious couples' floral bath spa treatment at a world-class wellness center.",
                    'Overnight Stay: Seminyak / Jimbaran | Meals Included: Breakfast',
                ],
            ),
            _day(
                6,
                'ULUWATU CLIFF TEMPLE, KECAK FIRE DANCE & JIMBARAN SEAFOOD DINNER',
                (
                    'Your final full day features unforgettable sights. Travel to the southern tip of the Bukit Peninsula to explore Uluwatu Temple, perched dramatically on a sheer cliff 70 meters above the ocean. At sunset, enjoy front-row seats at the captivating Kecak Fire Dance performance in an open-air amphitheater. Afterward, enjoy a romantic, candlelit seafood dinner right on the soft sands of Jimbaran Bay.'
                ),
                [
                    'Sightseeing Included: Uluwatu Cliff Temple, Sunset Kecak Dance, Jimbaran Bay Seafood Dinner.',
                    'Evening Experience: Toast to your love with fine wine as the tide gently comes in.',
                    'Overnight Stay: Seminyak / Jimbaran | Meals Included: Breakfast & Premium Dinner',
                ],
            ),
            _day(
                7,
                'SOUVENIRS SHOPPING & FOND FAREWELL TO PARADISE',
                (
                    'Savor a final gourmet breakfast overlooking the ocean. Spend your morning picking up unique local souvenirs, from fine hand-woven silk textiles to premium Kintamani single-origin coffee beans. At the designated hour, your private luxury transport arrives to take you to Denpasar International Airport for your flight home, carrying a treasure trove of unforgettable memories curated flawlessly by TRAGUIN. Best Time to Visit Note: Booking 45-60 days ahead secures the best luxury pool villas during peak dry months. TRAGUIN Premium Travel | Luxury Honeymoon Experts 4'
                ),
                [
                    'Sightseeing Included: Private Departure Airport Transfer.',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Ubud (3',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Ubud (3',
                '6N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Ubud (3',
                '6N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Ubud (3',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included("06 Nights Stay: Selected luxury couples' properties", 1),
            _inc_excluded('PACKAGE INCLUSIONS', 2),
            _inc_excluded('Airfare: International roundtrip flights', 3),
            _inc_excluded('Visa Cost: Visa on Arrival fees', 4),
            _inc_excluded('Extra Tours: Optional experiences not explicitly listed', 5),
            _inc_excluded('Insurance: Comprehensive medical travel cover', 6),
        ],
    )
    return package, itinerary

def build_id_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-018'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Bali Fixed Departure Group Package'
    duration = '05 NIGHTS / 06 DAYS'
    slug = 'id-018-bali-fixed-departure-group-package'
    itin_slug = 'id-018-bali-fixed-departure-group-package-itinerary'
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
            _ph('Serial code ID-018 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Ubud Highlands', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7),
            _ph('TRAGUIN Signature Group Experiences: Enjoy pre-arranged priority entry lines at the Uluwatu Kecak', 8),
            _ph('TRAGUIN Support: 24/7 dedicated on-ground group', 9),
            _ph('TRAGUIN Corporate MICE & Premium Group Vacations 5', 10)
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
        tagline='Bali Fixed Departure Group Package',
        overview='EXCLUSIVE MANAGED GROUP ESCAPES • 05 NIGHTS / 06 DAYS Welcome to a beautifully managed group vacation journey structured by TRAGUIN Experts. Experience the incredible energy of companionship, premium execution, and deep corporate/social networking with our top-selling Bali Fixed Departure program. Built as an ultimate Bali Family Tour framework that serves seamlessly as a Luxury Bali Holiday for individual groups, this meticulously assembled blueprint integrates world-class coordination, upscale coaches, and immersive activities to create unforgettable memories. SERIAL CODE ID-018 TRAGUIN TOUR CODETRAGUIN-BALI- FD-018 STATE / COUNTRY Bali / Indonesia CATEGORY Premium Fixed Departure / Managed Group DURATION 05 Nights / 06 Days DESTINATIONS COVERED: Ubud Highlands (2 Nights) • Kuta / Kuta Beach (3 Nights) TRAGUIN Corporate MICE & Premium Group Vacations 1 IDEAL FOR Corporate Groups, Families, Like- Minded Travelers BEST TIME TO VISIT BALI April to October (Dry, pleasant weather window) STARTING PRICE Premium Competitive Group Rates (On Request) VEHICLE TYPE Private Premium Luxury AC Coach / Tour Bus\n\nTOUR OVERVIEW\nThe Best Bali Tour Package for fixed departures offers a premium social atmosphere without compromising individual luxury or personal comfort. Your journey is planned comprehensively to maximize your time, beginning in the central cultural highlands of Ubud before shifting directly down to the legendary beaches, nightlife zones, and iconic beach clubs of South Bali. Travel in style inside our premium air-conditioned luxury transportation coaches accompanied by an energetic native team, specialized local tour guides, and constant TRAGUIN support at every point.\n\nWHY CHOOSE TRAGUIN BALI FIXED DEPARTURE PACKAGES?\nOrganizing a premium group journey requires local insight and robust logistical capabilities. Our exclusive TRAGUIN Bali Packages strike a beautiful balance between high-demand tourist hubs and private, exclusive group encounters. Famous Attractions & Immersive Experiences: Walk through the iconic Tegalalang Rice Terraces, feel the wind on the legendary Bali Swing, and capture spectacular views of the active volcano at Mount Batur in Kintamani. Witness the spiritual heritage at Pura Tirta Empul and watch waves gently break around the majestic offshore Tanah Lot Temple. Most Searched Group Options & Instagram Locations: Capture stunning group memories at the Kanto Lampo waterfall cascades or during an intimate beachside seafood dinner at Jimbaran Bay. From exploring the bustling artistic streets of Ubud Market to enjoying VIP entry slots at top coastal beach clubs, this comprehensive Premium Bali Experience delivers seamless coordination, safety, and excellent group engagement.',
        seo_title='ID-018 | Bali Fixed Departure Group Package | TRAGUIN',
        seo_description='Premium 05 NIGHTS / 06 DAYS Bali package (ID-018 / TRAGUIN-BALI-000): Ubud Highlands with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • GROUP GATHERING & UBUD HIGHLANDS', 1),
            _ih('Day 02: UBUD CULTURE, BALI SWING & TEGALALANG RICE TERRACES', 2),
            _ih('Day 03: KINTAMANI VOLCANO VIEW, LUWAK COFFEE TASTING & TRANSITION SOUTH', 3),
            _ih('Day 04: TANAH LOT SEA TEMPLE EXPLORATION & BEACH CLUB LIFESTYLE', 4),
            _ih('Day 05: ULUWATU CLIFF TEMPLE, KECAK FIRE DANCE & JIMBARAN BAY DINNER', 5),
            _ih('Day 06: LOCAL SOUVENIR SHOPPING & DEPARTURE FROM BALI', 6),
            _ih('TRAGUIN Signature Group Experiences: Enjoy pre-arranged priority entry lines at the Uluwatu Kecak', 7),
            _ih('TRAGUIN Support: 24/7 dedicated on-ground group', 8),
            _ih('TRAGUIN Corporate MICE & Premium Group Vacations 5', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • GROUP GATHERING & UBUD HIGHLANDS',
                (
                    'TRAGUIN Corporate MICE & Premium Group Vacations 2 Arrive at Denpasar International Airport where the dedicated TRAGUIN Group Coordination team meets you at our private welcome lounge. Receive fresh frangipani leis, cold bottled water, and helpful itinerary binders before boarding your luxury air-conditioned coach. Enjoy a scenic journey up into the lush hills of Ubud. Check into your selected premium resort, unpack comfortably, and join your fellow travelers for a refreshing evening orientation cocktail.'
                ),
                [
                    'Sightseeing Included: Smooth Airport Welcome, Private Group Coach Transfer.',
                    "Evening Experience: Interactive group ice-breaker dinner inside the resort's premium dining room.",
                    'Overnight Stay: Ubud Highlands | Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'UBUD CULTURE, BALI SWING & TEGALALANG RICE TERRACES',
                (
                    'Savor a fresh tropical breakfast looking out over mist-covered valley canopies. Today features immersive group adventures across the core tourist places in Bali. Visit the stunning, multi-tiered Tegalalang Rice Terraces to witness ancient irrigation design. Next, experience the famous Bali Swing over deep emerald gorges for high-quality photos. Walk through the cool, shaded paths of the Sacred Monkey Forest Sanctuary before enjoying free time to shop around the Ubud Traditional Art Market.'
                ),
                [
                    'Sightseeing Included: Tegalalang Rice Terraces, Bali Swing Adventure, Ubud Monkey Forest, Art Markets.',
                    'Photography Points: Group portrait spots right over the emerald rice terrace amphitheater.',
                    'Overnight Stay: Ubud Highlands | Meals Included: Breakfast',
                ],
            ),
            _day(
                3,
                'KINTAMANI VOLCANO VIEW, LUWAK COFFEE TASTING & TRANSITION SOUTH',
                (
                    'Check out of Ubud and travel north along spectacular mountain ridges to Kintamani, a highland village overlooking the grand active volcano of Mount Batur and its deep crater lake. Enjoy a premium buffet lunch at a panoramic viewing pavilion. On the return loop, visit an exclusive agro-tourism estate to see how traditional Balinese Luwak coffee is made. In the afternoon, descend to South Bali to check into your premium beach resort in Kuta or Seminyak. Group Highlights: Coffee flight tasting of 12 exotic herbal teas and authentic local roasts.'
                ),
                [
                    'Sightseeing Included: Mount Batur Viewpoint, Kintamani Highlands, Luwak Coffee Estate, South Bali Transfer.',
                    'Overnight Stay: Kuta / Seminyak Beach Area | Meals Included: Breakfast & Buffet Lunch',
                ],
            ),
            _day(
                4,
                'TANAH LOT SEA TEMPLE EXPLORATION & BEACH CLUB LIFESTYLE',
                (
                    "Spend a completely relaxed morning enjoying your resort's facilities or swimming along the lively golden shores of Kuta Beach. In the afternoon, board your group coach for a short trip to the iconic Tanah Lot Sea Temple, perched dramatically on a black volcanic wave-swept rock formation. Watch the sun dip beneath the TRAGUIN Corporate MICE & Premium Group Vacations 3 horizon before heading to a premier beachfront club to experience Bali's world-famous music and lifestyle scene."
                ),
                [
                    'Sightseeing Included: Tanah Lot Sea Temple, Kuta Beach walk area.',
                    'Evening Experience: Reserved group seating area at a premium coastal beach club for sunset drinks.',
                    'Overnight Stay: Kuta / Seminyak Beach Area | Meals Included: Breakfast',
                ],
            ),
            _day(
                5,
                'ULUWATU CLIFF TEMPLE, KECAK FIRE DANCE & JIMBARAN BAY DINNER',
                (
                    'Your final full day on the island features iconic coastal highlights. Travel to the southernmost tip of Bali to explore Uluwatu Temple, resting precariously on a 70-meter cliff edge above the Indian Ocean. At sunset, enjoy pre-arranged VIP entry seats at the open-air cliff amphitheater to watch the moving Kecak Fire Dance performance. Celebrate the final night of your journey with a grand, candlelit seafood barbecue dinner right on the soft sands of Jimbaran Bay. Group Highlights: Final celebration toast with fresh coconut water and local wines on the beach.'
                ),
                [
                    'Sightseeing Included: Uluwatu Cliff Temple, Sunset Kecak Dance, Jimbaran Bay Seafood Dinner.',
                    'Overnight Stay: Kuta / Seminyak Beach Area | Meals Included: Breakfast & Premium Dinner',
                ],
            ),
            _day(
                6,
                'LOCAL SOUVENIR SHOPPING & DEPARTURE FROM BALI',
                (
                    'Enjoy your final breakfast at the resort. Take advantage of your last morning to browse local markets for fine handmade batik shirts, aromatic spices, and traditional souvenirs. At the scheduled time, your premium luxury transportation coach arrives to transfer the entire group safely to Denpasar International Airport for your return flights, wrapping up an extraordinary group vacation curated expertly by TRAGUIN. Best Time to Visit Note: The dry season ensures clear skies and seamless coach transfers.'
                ),
                [
                    'Sightseeing Included: Scheduled Private Group Airport Departure Transfer.',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Corporate MICE & Premium Group Vacations 4 TIER CATEGORYUBUD HIGHLANDS (2 NIGHTS) KUTA / SEMINYAK BEACH (3 NIGHTS) ROOM TYPE & MEAL PLAN Sthala Ubud / Element by Westin The Haven Seminyak / Aston Kuta Deluxe Supe',
                'Multi-city Bali',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — TRAGUIN Corporate MICE & Premium Group Vacations 4 TIER CATEGORYUBUD HIGHLANDS (2 NIGHTS) KUTA / SEMINYAK BEACH (3 NIGHT',
            ),
            _hotel(
                'Alaya Resort Ubud / Arkamara Merusaka Nusa Dua / Hard Rock Hotel Premium Grand Deluxe (BB)',
                'Multi-city Bali',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Alaya Resort Ubud / Arkamara Merusaka Nusa Dua / Hard Rock Hotel Premium Grand Deluxe (BB)',
            ),
            _hotel(
                'The Kayon Resort / Maya Ubud The Seminyak Beach Resort / Discovery Kartika Luxury Garden Suite (BB)',
                'Multi-city Bali',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Kayon Resort / Maya Ubud The Seminyak Beach Resort / Discovery Kartika Luxury Garden Suite (BB)',
            ),
            _hotel(
                'Viceroy Bali / Mandapa Ritz-Carlton The Mulia / W Bali Seminyak Resort Signature Private Pool Villa (BB)',
                'Multi-city Bali',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Viceroy Bali / Mandapa Ritz-Carlton The Mulia / W Bali Seminyak Resort Signature Private Pool Villa (BB)',
            )
        ],
        inclusions=[
            _inc_included('05 Nights Stay: Selected high-end group properties', 1),
            _inc_excluded('PACKAGE INCLUSIONS', 2),
            _inc_excluded('Airfare: International roundtrip flights', 3),
            _inc_excluded('Visa Costs: Visa on Arrival (VoA) fees', 4),
        ],
    )
    return package, itinerary

def build_id_019(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-019'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Ladies Bali Retreat'
    duration = '05 NIGHTS / 06 DAYS'
    slug = 'id-019-ladies-bali-retreat'
    itin_slug = 'id-019-ladies-bali-retreat-itinerary'
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
            _ph('Serial code ID-019 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Ubud Spiritual', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Leisure'],
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
        tagline='Ladies Bali Retreat',
        overview="EXCLUSIVE FEMALE-ONLY LUXURY ESCAPE • 05 NIGHTS / 06 DAYS Welcome to a beautifully curated wellness and lifestyle experience organized exclusively by TRAGUIN Experts. Reconnect, rejuvenate, and share unparalleled laughter on this specialized Ladies Bali Retreat. Thoughtfully designed as a sophisticated twist to the classic Bali Family Tour framework, this absolute Luxury Bali Holiday integrates therapeutic holistic wellness, beautiful photography points, private high-tea encounters, and elite beach club reservations to generate unforgettable memories. SERIAL CODE ID-019 TRAGUIN TOUR CODETRAGUIN-BALI- WM-019 STATE / COUNTRY Bali / Indonesia CATEGORY Female-Only Luxury Retreat / Lifestyle & Wellness DURATION 05 Nights / 06 Days DESTINATIONS COVERED: Ubud Spiritual Center (2 Nights) • Seminyak Beachfront (3 Nights) TRAGUIN Ladies Special Vacations | Exclusive Getaways 1 IDEAL FOR Solo Female Travelers, Girlfriends' Getaways, Mother-Daughter Retreats BEST TIME TO VISIT BALI April to October (Sunny, optimal coastal season) STARTING PRICE Premium Curated Rates (On Request) VEHICLE TYPE Private Luxury AC Multi-Van with dedicated female chauffeur assistance\n\nTOUR OVERVIEW\nThe Best Bali Tour Package for an all-women group provides a beautiful blend of peaceful sanctuary and vibrant tropical chic. Your journey flows seamlessly through the central mountain arts hub of Ubud—where breathtaking landscapes and holistic yoga sanctuaries center the spirit—before heading to the glamorous boutique streets, upscale shopping avenues, and legendary coastal sunset spots of Seminyak. Travel comfortably with our premium luxury transportation options, accompanied by dedicated local guides and continuous 24/7 TRAGUIN support.\n\nWHY CHOOSE TRAGUIN LADIES BALI RETREAT PACKAGES?\nAn exceptional all-female getaway requires absolute comfort, premium stays, top-tier safety, and highly curated social settings. Our exclusive TRAGUIN Bali Packages are created explicitly to blend popular iconic locations with private, relaxing spaces. Famous Attractions & Immersive Experiences: Walk through the terraced hills of the Tegalalang Rice Terraces, capture stunning photos on the iconic Bali Swing, and visit the serene water temple Pura Tirta Empul. Savor artisanal chocolates, discover fine silver-making skills, and marvel at the offshore sunset views of Tanah Lot Temple. Top Tourist Places & Instagram Locations: Capture incredible group memories at the tiered Kanto Lampo waterfalls, enjoy floating villa breakfasts in private infinity pools, or take part in professional sunset beach photography sessions. From high-fashion shopping in Seminyak to VIP daybed bookings at famous beach clubs, this true Premium Bali Experience ensures smooth travel and an incredible lifestyle escape. TRAGUIN Ladies Special Vacations | Exclusive Getaways 2",
        seo_title='ID-019 | Ladies Bali Retreat | TRAGUIN',
        seo_description='Premium 05 NIGHTS / 06 DAYS Bali package (ID-019 / TRAGUIN-BALI-000): Ubud Spiritual with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • RETREAT GATHERING IN UBUD', 1),
            _ih('Day 02: UBUD WELLNESS SWING, TEGALALANG & SOUND HEALING', 2),
            _ih('Day 03: TIRTA EMPUL PURIFICATION, WATERFALL & TRANSITION SOUTH', 3),
            _ih('Day 04: TANAH LOT TEMPLE SUNSET & PREMIUM COUTURE SHOPPING', 4),
            _ih('Day 05: ULTIMATE BEACH CLUB LIFESTYLE & JIMBARAN DINNER CELEBRATION', 5),
            _ih('Day 06: SPA REJUVENATION & DEPARTURE FROM BALI', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • RETREAT GATHERING IN UBUD',
                (
                    'Touch down at Denpasar International Airport where your professional TRAGUIN coordination team welcomes you warmly with fresh frangipani garlands and cold organic refreshments. Board your private luxury transport to travel comfortably into the peaceful forest hills of Ubud. Check into your selected luxury resort, unpack, and gather with your fellow retreat guests for an elegant sunset welcome circle.'
                ),
                [
                    'Sightseeing Included: VIP Airport Welcome, Private Luxury Transfer to Ubud.',
                    'Evening Experience: A welcome gathering and introduction dinner featuring fresh, organic Balinese cuisine.',
                    'Overnight Stay: Ubud Sanctuary | Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'UBUD WELLNESS SWING, TEGALALANG & SOUND HEALING',
                (
                    'Start your morning with a peaceful guided yoga and meditation session. Today, explore the top tourist places in Bali. Walk through the scenic, multi-tiered Tegalalang Rice Terraces to witness ancient irrigation design. Next, head to the iconic Bali Swing, soaring over deep forest valleys for beautiful photos. In the afternoon, experience a transformative sound healing journey at the Pyramids of Chi wellness sanctuary. Exclusive Highlights: Curated sound healing or multi-hour holistic group meditation session.'
                ),
                [
                    'Sightseeing Included: Tegalalang Rice Terraces, Bali Swing, Ubud Traditional Art Market.',
                    'Overnight Stay: Ubud Sanctuary | Meals Included: Breakfast',
                ],
            ),
            _day(
                3,
                'TIRTA EMPUL PURIFICATION, WATERFALL & TRANSITION SOUTH',
                (
                    'Check out of Ubud and head to the sacred water temple Pura Tirta Empul. Participate in a traditional Melukat water purification ritual led by a local priest. Next, visit Kanto Lampo Waterfall to capture gorgeous photos by the tiered cascades. In the afternoon, head down to South Bali to check into your premium beachfront resort in Seminyak.'
                ),
                [
                    'Sightseeing Included: Tirta Empul Temple, Kanto Lampo Waterfall, Seminyak Coastline.',
                    'Evening Experience: Unwind at an upscale beachfront lounge with curated cocktails and sea views.',
                    'Overnight Stay: Seminyak Beachfront | Meals Included: Breakfast & Lunch',
                ],
            ),
            _day(
                4,
                'TANAH LOT TEMPLE SUNSET & PREMIUM COUTURE SHOPPING',
                (
                    'TRAGUIN Ladies Special Vacations | Exclusive Getaways 3 Enjoy a leisurely morning, sleep in late, or treat yourself to an iconic floating breakfast in your private pool. The afternoon is dedicated to exploring Seminyak’s famous fashion streets, home to upscale local designer boutiques and unique home decor. Later, head to the iconic Tanah Lot Sea Temple, built on an offshore volcanic rock, to watch a spectacular sunset over the ocean. Food Recommendations: Tapas and organic smoothies at a trendy, beautifully designed cafe.'
                ),
                [
                    'Sightseeing Included: Seminyak Boutique Boulevard, Tanah Lot Sea Temple.',
                    'Overnight Stay: Seminyak Beachfront | Meals Included: Breakfast',
                ],
            ),
            _day(
                5,
                'ULTIMATE BEACH CLUB LIFESTYLE & JIMBARAN DINNER CELEBRATION',
                (
                    'Spend a fabulous day relaxing at an elite beach club like Atlas Beach Fest or Potato Head. Lounge on reserved private daybeds, swim in infinity pools, and listen to chilled house music against the backdrop of the ocean. In the evening, celebrate the final night of your retreat with a grand, candlelit seafood dinner right on the soft sands of Jimbaran Bay. Group Highlights: Final celebration toast with fine wine and fresh seafood on the beach.'
                ),
                [
                    'Sightseeing Included: Premium Beach Club Daybed Access, Jimbaran Bay Coastline.',
                    'Overnight Stay: Seminyak Beachfront | Meals Included: Breakfast & Premium Dinner',
                ],
            ),
            _day(
                6,
                'SPA REJUVENATION & DEPARTURE FROM BALI',
                (
                    'Savor your final gourmet breakfast at the resort. Before departing, indulge in a luxurious multi-hour traditional Balinese spa and massage treatment. Afterwards, your private luxury transport transfers you safely to Denpasar International Airport for your return flight, wrapping up an extraordinary retreat curated expertly by TRAGUIN. Best Time to Visit Note: Booking 45-60 days ahead ensures the best villa availability.'
                ),
                [
                    'Sightseeing Included: Scheduled Private Airport Departure Transfer.',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Alaya Resort Ubud / Sthala Ubud The Haven Seminyak / Merusaka Deluxe Premium Room (BB)',
                'Multi-city Bali',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Alaya Resort Ubud / Sthala Ubud The Haven Seminyak / Merusaka Deluxe Premium Room (BB)',
            ),
            _hotel(
                'The Kayon Resort / Maya Ubud The Seminyak Beach ResortPremium Garden Suite (BB)',
                'Multi-city Bali',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — The Kayon Resort / Maya Ubud The Seminyak Beach ResortPremium Garden Suite (BB)',
            ),
            _hotel(
                'Como Shambhala Estate / Viceroy Bali The Legian Seminyak / Mulia Villas Luxury Private Pool Villa (BB)',
                'Multi-city Bali',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Como Shambhala Estate / Viceroy Bali The Legian Seminyak / Mulia Villas Luxury Private Pool Villa (BB)',
            ),
            _hotel(
                'Mandapa, a Ritz-Carlton / Amandari The Bulgari Resort / W Bali Seminyak Signature Ocean View Pool Villa (BB)',
                'Multi-city Bali',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Mandapa, a Ritz-Carlton / Amandari The Bulgari Resort / W Bali Seminyak Signature Ocean View Pool Villa (BB)',
            )
        ],
        inclusions=[
            _inc_included('05 Nights Stay: Selected high-end luxury properties', 1),
            _inc_excluded('PACKAGE INCLUSIONS', 2),
            _inc_excluded('Airfare: International roundtrip flight bookings', 3),
            _inc_excluded('Visa Costs: Visa on Arrival (VoA) fees', 4),
        ],
    )
    return package, itinerary

def build_id_020(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'ID-020'
    tour_code = 'TRAGUIN-BALI-000'
    title = 'Grand Bali Premium Tour'
    duration = '08 NIGHTS / 09 DAYS'
    slug = 'id-020-grand-bali-premium-tour'
    itin_slug = 'id-020-grand-bali-premium-tour-itinerary'
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
            _ph('Serial code ID-020 | TRAGUIN tour code TRAGUIN-BALI-000', 1),
            _ph('Country: Bali, Indonesia | Category: Premium Haryana Tour', 2),
            _ph('Destinations: Ubud Art Hub', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury MPV / Buffet Breakfast & Curated Dinners', 7),
            _ph('TRAGUIN Signature Experiences: Enjoy pre-arranged priority entry lines at the Uluwatu Kecak Dance', 8)
        ],
        moods=['Luxury'],
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
        tagline='Grand Bali Premium Tour',
        overview='Couples STARTING PRICE Custom Luxury Level (On Request) VEHICLE Private Luxury AC Car / MPV with Dedicated Chauffeur\n\nTOUR OVERVIEW\nThe Best Bali Tour Package by TRAGUIN provides a detailed, comprehensive 9-day route that hits the absolute top tourist places in Bali. This premium stay format is built around unhurried discovery, moving you comfortably from the terraced green mountains of Ubud through the golden sandy beaches of Nusa Dua, and finishing inside the high-end boutique neighborhoods of Seminyak. Travel effortlessly under the protection of 24/7 on-ground TRAGUIN support, with fine dining, private speedboats, and dedicated guides included.\n\nWHY CHOOSE THE TRAGUIN GRAND BALI PREMIUM EXPERIENCE?\nExploring Bali in true luxury requires smart planning to avoid heavy public traffic. Our premium TRAGUIN Bali Packages combine high-value iconic landmarks with curated hidden locations. Famous Attractions & Immersive Experiences: Walk through the historic Tegalalang Rice Terraces, fly above the valley on the iconic Bali Swing, and witness spiritual purification water rituals at Pura Tirta Empul. Travel down to the dramatic cliffside Uluwatu Temple to hear traditional sunset Kecak chanting, and visit the legendary offshore Tanah Lot Temple. Top Tourist Places & Instagram Locations: Capture amazing memories at the tiered Kanto Lampo and Tegenungan waterfalls, or during an unforgettable day trip across the turquoise marine sanctuaries of Nusa Penida. From world-class dining over Jimbaran Bay to relaxing on reserved daybeds at elite beach clubs, this package offers premium comfort and total safety.',
        seo_title='ID-020 | Grand Bali Premium Tour | TRAGUIN',
        seo_description='Premium 08 NIGHTS / 09 DAYS Bali package (ID-020 / TRAGUIN-BALI-000): Ubud Art Hub with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN BALI • ESCAPE TO THE UBUD HIGHLANDS', 1),
            _ih('Day 02: UBUD HIGHLANDS, TEGALALANG & HIGH-SOARING BALI SWING', 2),
            _ih('Day 03: KINTAMANI VOLCANO VIEW & HOLY PURIFICATION EXPERIENCE', 3),
            _ih('Day 04: UBUD TO NUSA DUA • TANAH LOT TEMPLE SUNSET', 4),
            _ih('Day 05: EXCLUSIVE NUSA PENIDA PRIVATE SPEEDBOAT EXCURSION', 5),
            _ih('Day 06: BLISSFUL BEACH RESORT DAY & REJUVENATING SPA', 6),
            _ih('Day 07: TRANSITION TO SEMINYAK • ULUWATU CLIFFS & KECAK FIRE DANCE', 7),
            _ih('Day 08: ELITE BEACH CLUB INFUSED LIFESTYLE DAY', 8),
            _ih('TRAGUIN Signature Experiences: Enjoy pre-arranged priority entry lines at the Uluwatu Kecak Dance', 9)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN BALI • ESCAPE TO THE UBUD HIGHLANDS',
                (
                    'Land at Denpasar International Airport where your private TRAGUIN concierge greets you at the arrival terminal. Enjoy cold towels and a traditional Balinese frangipani flower greeting as you are escorted to your luxury vehicle. Take a relaxing drive up into the foothills to check into your premium resort in Ubud, enjoying beautiful views of the jungle valleys. TRAGUIN Premium Travel | Luxury Holiday Experts 2'
                ),
                [
                    'Sightseeing Included: VIP Airport Pick-up & Private Luxury Car Transfer.',
                    "Evening Experience: A relaxing welcome dinner inside the resort's premium restaurant.",
                    'Overnight Stay: Ubud | Meals Included: Welcome Dinner',
                ],
            ),
            _day(
                2,
                'UBUD HIGHLANDS, TEGALALANG & HIGH-SOARING BALI SWING',
                (
                    'Savor a fresh organic breakfast overlooking the valley mist. Today, dive into the cultural heart of the island. Walk through the scenic, multi-tiered Tegalalang Rice Terraces, and then experience the thrill of the famous Bali Swing over the deep green forest. In the afternoon, explore the Sacred Monkey Forest Sanctuary and pick up handcrafted treasures at the Ubud Art Market.'
                ),
                [
                    'Sightseeing Included: Tegalalang Rice Terraces, Bali Swing, Ubud Monkey Forest, Art Market.',
                    'Photography Points: Mid-air on the swing with perfect panoramic valley backdrops.',
                    'Overnight Stay: Ubud | Meals Included: Breakfast',
                ],
            ),
            _day(
                3,
                'KINTAMANI VOLCANO VIEW & HOLY PURIFICATION EXPERIENCE',
                (
                    'Travel along scenic ridge roads to Kintamani to admire the active volcano of Mount Batur and its deep crater lake during a premium lunch. On your way back, stop at Pura Tirta Empul to witness or participate in a traditional holy spring water cleansing ritual led by a resident priest. Conclude your evening at the beautiful cascading Kanto Lampo Waterfall.'
                ),
                [
                    'Sightseeing Included: Mount Batur Viewpoint, Tirta Empul Holy Temple, Kanto Lampo Waterfall.',
                    'Optional Activities: An early morning sunrise 4x4 Jeep safari tour up Mount Batur.',
                    'Overnight Stay: Ubud | Meals Included: Breakfast & Premium Lunch',
                ],
            ),
            _day(
                4,
                'UBUD TO NUSA DUA • TANAH LOT TEMPLE SUNSET',
                (
                    "Check out of Ubud and head toward South Bali's elite beachfront resort area, Nusa Dua. On the way, visit the iconic Tanah Lot Temple, built on a volcanic rock just off the coast. Watch a spectacular sunset over the Indian Ocean as waves crash gently around the ancient temple walls. TRAGUIN Premium Travel | Luxury Holiday Experts 3"
                ),
                [
                    'Sightseeing Included: Southward Coastal Transfer, Tanah Lot Sea Temple.',
                    'Evening Experience: Check into your premium five-star beachfront resort in Nusa Dua.',
                    'Overnight Stay: Nusa Dua | Meals Included: Breakfast',
                ],
            ),
            _day(
                5,
                'EXCLUSIVE NUSA PENIDA PRIVATE SPEEDBOAT EXCURSION',
                (
                    'Board a high-speed private boat over to the famous island of Nusa Penida. Walk along the dramatic cliffs of Kelingking Beach, renowned worldwide for its T-Rex shaped rock formation. Swim in the clear waters of Angel’s Billabong, a natural infinity pool, and stroll across the white sands of Broken Beach.'
                ),
                [
                    "Sightseeing Included: Kelingking Beach, Angel's Billabong, Broken Beach, Speedboat Crossings.",
                    'Optional Activities: Snorkeling with wild Manta Rays at Crystal Bay.',
                    'Overnight Stay: Nusa Dua | Meals Included: Breakfast & Picnic Lunch',
                ],
            ),
            _day(
                6,
                'BLISSFUL BEACH RESORT DAY & REJUVENATING SPA',
                (
                    "Enjoy a completely free, relaxing day at your luxury resort in Nusa Dua. Swim in the calm coastal waters or enjoy a traditional, multi-hour Balinese floral oil massage at the resort's premium spa center, leaving you feeling completely refreshed."
                ),
                [
                    'Sightseeing Included: Relaxed Resort Beach Access.',
                    'Evening Experience: A modern theatrical performance of the Devdan Show, celebrating Indonesian culture.',
                    'Overnight Stay: Nusa Dua | Meals Included: Breakfast',
                ],
            ),
            _day(
                7,
                'TRANSITION TO SEMINYAK • ULUWATU CLIFFS & KECAK FIRE DANCE',
                (
                    'Check out of Nusa Dua and check into your next premium hotel in Seminyak. In the afternoon, travel to the southern tip of the island to explore Uluwatu Temple, perched on a 70-meter cliff above the ocean. Watch the moving Kecak Fire Dance performance at sunset, followed by a romantic seafood dinner on the beach at Jimbaran Bay.'
                ),
                [
                    'Sightseeing Included: Uluwatu Cliff Temple, Sunset Kecak Dance, Jimbaran Bay Seafood Dinner.',
                    'Overnight Stay: Seminyak | Meals Included: Breakfast & Seafood Dinner',
                ],
            ),
            _day(
                8,
                'ELITE BEACH CLUB INFUSED LIFESTYLE DAY',
                (
                    "Spend a fabulous day relaxing at an elite beach club like Atlas Beach Fest or Potato Head. Lounge on reserved private daybeds, swim in infinity pools, and listen to chilled music against the backdrop of the ocean. In the evening, explore Seminyak's famous fashion streets, home to high-end boutiques and local designer shops. TRAGUIN Premium Travel | Luxury Holiday Experts 4 Food Recommendations: Fine dining at a premier restaurant along Seminyak's famous culinary street."
                ),
                [
                    'Sightseeing Included: Reserved Beach Club Daybed Access.',
                    'Overnight Stay: Seminyak | Meals Included: Breakfast',
                ],
            ),
            _day(
                9,
                'FINE SOUVENIRS & FOND FAREWELLS FROM BALI',
                (
                    'Enjoy a final gourmet breakfast at your resort. Spend your last morning picking up beautiful souvenirs like fine wood carvings, organic oils, and Kintamani coffee beans. At the scheduled time, your private luxury transport transfers you safely to Denpasar International Airport for your return flight, wrapping up an extraordinary journey curated expertly by TRAGUIN.'
                ),
                [
                    'Sightseeing Included: Private Departure Airport Transfer.',
                    'Meals Included: Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Ubud Art Hub',
                '8N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Ubud Art Hub',
                '8N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Luxury Property',
                'Ubud Art Hub',
                '8N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Ubud Art Hub',
                '8N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Bali', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven MPV', 2),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 3),
            _inc_excluded('PACKAGE INCLUSIONS', 4),
            _inc_excluded('Airfare: International roundtrip flight bookings', 5),
            _inc_excluded('Visa Costs: Visa on Arrival (VoA) fees', 6),
            _inc_excluded('Airfare: International roundtrip flight bookings', 7),
            _inc_excluded('Visa Costs: Visa on Arrival (VoA) fees', 8),
        ],
    )
    return package, itinerary

INDONESIA_ID_001_020_BUILDERS = [
    build_id_001,
    build_id_002,
    build_id_005,
    build_id_006,
    build_id_007,
    build_id_008,
    build_id_009,
    build_id_010,
    build_id_011,
    build_id_012,
    build_id_013,
    build_id_014,
    build_id_015,
    build_id_016,
    build_id_017,
    build_id_018,
    build_id_019,
    build_id_020,
]
