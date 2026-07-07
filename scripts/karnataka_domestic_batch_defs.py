"""Builder functions for KA-001 through KA-017 Karnataka domestic packages."""

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

KARNATAKA_SLUG = "karnataka"


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


def build_ka_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-001'
    tour_code = 'TRAGUIN-MYS-CRG-001'
    title = 'Mysore Coorg Luxury Escape'
    duration = '04 Nights / 05 Days'
    slug = 'ka-001-mysore-coorg-luxury-escape'
    itin_slug = 'ka-001-mysore-coorg-luxury-escape-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Premium Family Vacation', 2),
            _ph('Destinations: Mysore • Coorg', 3),
            _ph('Ideal for: Families, Couples, Nature & Heritage Lovers', 4),
            _ph('Best season: October to March (Plus Lush Monsoons)', 5),
            _ph('Starting price: On Request (Premium Scale)', 6),
            _ph('Vehicle: Private Premium SUV (Innova Crysta / Luxury Sedan)', 7),
            _ph('Meal Plan: Breakfast & Handpicked Curated Dinners (MAPAI)', 8),
            _ph('Route Plan: Bangalore → Mysore (1N) → Coorg (3N) → Bangalore Departure', 9),
            _ph('TRAGUIN Signature Amenities & 24/7 Dedicated Concierge Support', 10),
            _ph('TRAGUIN Signature Experience: Private family bean-to-cup coffee brewing masterclass with an estate connoisseur', 11),
            _ph('Shopping: Mysore Silk saris, sandalwood oils, Mysore Pak; Coorg coffee, cardamom, pepper, organic honey', 12),
            _ph("Instagram Spots: Mysore Palace illumination, Abbey Falls, Raja's Seat sunset, Tibetan Golden Temple at Bylakuppe", 13),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; book ultra-luxury rooms 45 days ahead during peak season', 14),
        ],
        moods=['Nature', 'Family', 'Luxury', 'Heritage'],
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
        tagline='Mysore • Coorg Luxury Escape • 04 Nights / 05 Days',
        overview=(
            "Welcome to an extraordinary journey meticulously crafted by TRAGUIN. This exclusive luxury Karnataka holiday seamlessly bridges the royal opulence, heritage charm, and cultural grandiosity of Mysore with the serene mist-kissed highlands, sprawling coffee estates, and breathtaking landscapes of Coorg. Perfectly engineered to deliver an unparalleled, deeply immersive family experience, this bespoke getaway effortlessly blends world-class luxury, private chauffeured transfers, signature handpicked hotels, and deeply engaging wildlife and historical explorations.\n\nYour bespoke TRAGUIN travel itinerary begins in the heritage-rich city of Mysore, where palatial elegance stands gracefully alongside vibrant traditional markets. Experience private guided palace walk-throughs and intimate musical fountain viewings before ascending to Coorg via a beautifully scenic route. Surrounded by cascading seasonal waterfalls, spice plantations, and absolute tranquility, your family will discover the pinnacle of luxury, rejuvenation, and comfort on the Best Karnataka Tour Package available.\n\nWhy Visit Karnataka? This iconic pairing delivers the ultimate dual-world Indian holiday—combining ultra-luxury heritage immersion with an exquisite mountain retreat. Mysore captivates multi-generational families with magnificent architectural sites, rich silk weaving heritage, and sandalwood fragrances. Coorg, the Scotland of India, provides a refreshing alpine sanctuary famous for pristine natural ecosystems, sprawling organic coffee estates, and panoramic viewpoints."
        ),
        seo_title='KA-001 | Mysore Coorg Luxury Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Mysore & Coorg package (KA-001 / TRAGUIN-MYS-CRG-001): Mysore Palace, Chamundi Hills, Brindavan Gardens, Dubare Elephant Camp, Abbey Falls, coffee plantation trail, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Seringapatam Fortress, Brindavan Gardens Musical Show & Mysore Palace', 1),
            _ih('Chamundi Hills, Tibetan Golden Temple at Bylakuppe & Coorg plantation immersion', 2),
            _ih('Dubare Elephant Camp, Abbey Falls, Madikeri Fort & Raja\'s Seat sunset', 3),
            _ih('TRAGUIN Signature Experience: Private family bean-to-cup coffee brewing masterclass', 4),
            _ih('Premium Handpicked Hotels: 4-tier luxury properties across Mysore & Coorg', 5),
        ],
        days=[
            _day(1, 'Arrival in Bangalore & Drive to Mysore | Welcome to Royal Grandeur', (
                'Arrive at Bangalore\'s Kempegowda International Airport, where a dedicated TRAGUIN luxury travel representative will warmly greet your family with premium welcome amenities and a private chauffeured luxury vehicle. Smoothly begin your journey toward Mysore, stopping en route to appreciate the historical fortress of Seringapatam. Upon arrival in Mysore, check in to your heritage luxury hotel. After a short period of relaxation, embark on a curated evening exploration of the world-famous Brindavan Gardens. Experience a spectacular, symphonic musical fountain show that brings light, water, and sound together in perfect alignment.'
            ), [
                'Sightseeing Included: Seringapatam Fortress, Brindavan Gardens Musical Show',
                'Optional Activities: Artisanal sandalwood oil shopping excursion',
                'Evening Experience: Illumination walk through pristine palace-side gardens',
                'Overnight Stay: Mysore Premium Luxury Hotel',
                'Meals Included: Gourmet Dinner',
            ]),
            _day(2, 'Mysore Sightseeing & Transfer to Coorg | Journey to the Coffee Kingdom', (
                'Savor a magnificent multi-cuisine breakfast before diving into the definitive Mysore sightseeing experience. Visit the legendary, breathtaking Mysore Palace, an extraordinary blend of Indo-Saracenic architecture filled with grand mahogany ceilings, stained glass windows, and solid silver doors. Next, drive up the historic Chamundi Hills to visit the ancient Sri Chamundeshwari Temple and view the monolithic Nandi Bull structure. In the afternoon, embark on a scenic drive toward the mist-clad hills for your exclusive Coorg family tour. En route, stop at Bylakuppe to witness the Namdroling Monastery, the majestic Golden Temple of the Tibetan community. Check into your ultra-luxury hill resort tucked neatly within a private coffee estate.'
            ), [
                'Sightseeing Included: Mysore Palace, Chamundi Hills, Tibetan Golden Temple',
                'Optional Activities: Premium silk sari weaving workshop visit',
                'Evening Experience: Traditional Kodava welcome drink and cultural bonfire night',
                'Overnight Stay: Coorg Premium Luxury Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(3, 'Coorg Plantation Immersive Experience | Coffee Trails & Eco-Adventures', (
                'Awaken to the soothing sounds of mountain birds and a refreshing alpine breeze. Today features a deeply immersive private bean-to-cup coffee plantation trail curated by TRAGUIN experts. Walk alongside expert botanists through shade-grown Arabica and Robusta plantations, learning the secrets behind harvesting world-class coffee and exotic spices like cardamom and black pepper. Enjoy a premium coffee tasting session right in the heart of the estate. Spend your afternoon at absolute leisure, enjoying the resort\'s premium luxury infinity pool overlooking the canopy, or unwinding completely within the resort\'s premium luxury spa facility.'
            ), [
                'Sightseeing Included: Private Coffee Estate Walk, Spice Plantation Trail',
                'Optional Activities: Organic aroma-therapy wellness spa treatment',
                'Evening Experience: Private family candle-lit patio dinner under a canopy of stars',
                'Overnight Stay: Coorg Premium Luxury Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(4, 'Coorg Sightseeing | Waterfalls, Fortresses & Sunset Panoramas', (
                'Indulge in a rich breakfast spread before heading out for a comprehensive day of Coorg sightseeing. Visit the Dubare Elephant Camp along the banks of the Kaveri River, where your family can experience an interactive session watching elephants bathe and learn about conservation efforts. Next, visit the sparkling, cascading waters of Abbey Falls nestled beautifully within spice gardens. Explore the historic Madikeri Fort, which reflects a unique combination of European and Asian architecture. As late afternoon approaches, your private guide will escort you to Raja\'s Seat (The Seat of Kings), where rolling hills and mist-covered valleys create a phenomenal panorama. Watch a spectacular sunset while capturing unforgettable memories.'
            ), [
                'Sightseeing Included: Dubare Elephant Camp, Abbey Falls, Madikeri Fort, Raja\'s Seat',
                'Optional Activities: Still-water river rafting or plantation zip-lining',
                'Evening Experience: Fine dining featuring signature traditional Kodava cuisine options',
                'Overnight Stay: Coorg Premium Luxury Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(5, 'Coorg to Bangalore | Cherishing Unforgettable Premium Memories', (
                'Enjoy a leisurely breakfast on your private balcony, taking in the serene mountain scenery one final time. Spend your morning at absolute relaxation inside the resort, enjoying a family swim or purchasing artisanal local souvenirs. At the designated check-out time, your professional chauffeur will assist with luggage and drive you safely down the hills back to Bangalore. Your dedicated TRAGUIN holiday concludes as you are smoothly dropped off at Bangalore Airport or your preferred railway terminal, carrying a treasure trove of unforgettable luxury memories from your premium Karnataka escape.'
            ), [
                'Sightseeing Included: Scenic return drive across the Western Ghats landscape',
                'Optional Activities: En-route gourmet lunch stop at a premium highway estate',
                'Evening Experience: Warm farewell at the airport departure gate',
                'Meals Included: Rich Buffet Breakfast',
            ]),
        ],
        hotels=[
            _hotel('Radisson Blu Plaza Hotel Mysore / Club Mahindra Madikeri / Amanvana Spa Resort', 'Mysore / Coorg', '04 Nights', 'Deluxe', 'Superior Room / 1-Bedroom Suite / Private Bungalow (CP/MAP)', 'Breakfast & Dinner (MAP)', 4, 1),
            _hotel('Grand Mercure Mysore / The Tamara Coorg', 'Mysore / Coorg', '04 Nights', 'Premium', 'Deluxe Premium Room / Luxury Cabin (CP/MAP)', 'Breakfast & Dinner (MAP)', 5, 2),
            _hotel('Royal Orchid Metropole / Heritage Inn / Evolve Back, Coorg (Orange County)', 'Mysore / Coorg', '04 Nights', 'Luxury', 'Heritage Royal Suite / Heritage Pool Villa (CP/MAP)', 'Breakfast & Dinner (MAP)', 5, 3),
            _hotel('The Grand Palace Hotel / Lalitha Mahal / Taj Madikeri Resort & Spa, Coorg', 'Mysore / Coorg', '04 Nights', 'Ultra Luxury', 'Grand Maharaja Heritage Suite / Luxury Pool Villa with Valley Panoramic Views (CP/MAP)', 'Breakfast & Dinner (MAP)', 5, 4),
        ],
        inclusions=[
            _inc_included('Elite Accommodation: 04 Nights stay in handpicked, premier luxury properties across Mysore & Coorg', 1),
            _inc_included('Bespoke Meal Plan: Daily lavish breakfast spreads and specialized multi-course culinary dinners', 2),
            _inc_included('Luxury Transportation: All transfers, long-distance touring, and city sightseeing via an exclusive private premium SUV', 3),
            _inc_included('TRAGUIN Signature Welcoming: Traditional flower garland welcome, cold towels, and a premium curated fruit basket upon arrival', 4),
            _inc_included('Interactive Elephant Experience: Exclusive access tickets for family interaction at Dubare Elephant Camp', 5),
            _inc_included('VIP Access & Entry: Pre-booked entry tickets and private professional guides for Mysore Palace and ancient caves/monasteries', 6),
            _inc_included('Full Professional Coverage: All toll fees, border taxes, driver allowances, fuel charges, and state permits', 7),
            _inc_included('TRAGUIN Support: Continuous 24/7 real-time remote concierge support from senior travel specialists', 8),
            _inc_excluded('Domestic or International airfares, flight bookings, or main interstate train ticket expenses', 9),
            _inc_excluded('Personal incidental expenses such as laundry services, mini-bar consumption, telephone calls, and room service', 10),
            _inc_excluded('Any specialized adventure activities, camera/video usage fees at monuments, or optional sightseeing detours', 11),
            _inc_excluded('Any meals, lunches, or beverage selections not specifically detailed in the official itinerary', 12),
            _inc_excluded('Mandatory peak festive season surcharges (Christmas, New Year, and major national holiday weeks)', 13),
            _inc_excluded('Travel insurance coverage and medical expenses of any nature', 14),
        ],
    )
    return package, itinerary


def build_ka_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-002'
    tour_code = 'TRAGUIN-KA-HAMPI-002'
    title = 'Hampi Heritage Luxury Escape'
    duration = '03 Nights / 04 Days'
    slug = 'ka-002-hampi-heritage-luxury-escape'
    itin_slug = 'ka-002-hampi-heritage-luxury-escape-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Premium Heritage & Luxury Vacation', 2),
            _ph('Destinations: Hampi • Hospet • Kishkindha', 3),
            _ph('Ideal for: Families, Connoisseurs, Luxury Travellers', 4),
            _ph('Best season: October to March (Best Time to Visit Hampi)', 5),
            _ph('Vehicle: Private Luxury SUV (Innova Crysta) with Uniformed Chauffeur', 6),
            _ph('Meal Plan: Gourmet Breakfast & Elaborate Traditional Dinners (MAPAI)', 7),
            _ph('Route Plan: Hubli/Jindal Airport → Hampi Sacred Ruins (3N) → Return Departure', 8),
            _ph('TRAGUIN Curated Welcome Kits & 24/7 Dedicated Concierge Care', 9),
            _ph('TRAGUIN Signature Experience: Private family sunset walk on Hemakuta Hill with a dedicated on-site professional historian', 10),
            _ph('Shopping: Anegundi banana fiber bags, handwoven cotton garments, miniature Hampi Chariot stone models', 11),
            _ph('Instagram Spots: Stone Chariot at Vittala Temple, Hemakuta Hill sunset, Lotus Mahal, Virupaksha Temple gopuram', 12),
            _ph('Important: Remove shoes before inner temple shrines; book ultra-luxury rooms 45 days ahead during peak season', 13),
        ],
        moods=['Heritage', 'Family', 'Luxury', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Heritage Tier)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Hampi Heritage Luxury Escape • 03 Nights / 04 Days',
        overview=(
            "Welcome to an unforgettable journey back in time, meticulously designed by TRAGUIN. This exclusive luxury Karnataka holiday introduces you to the crown jewel of India's architectural legacy—the magnificent boulder-strewn ruins of the Vijayanagara Empire at Hampi. This bespoke itinerary transforms an ancient landscape into a living storybook. Experience breathtaking landscapes, premium stays, handpicked hotels, and exclusive experiences curated precisely for multi-generational families and heritage lovers seeking the finest modern luxury wrapped in timeless royal history.\n\nYour premium Hampi Heritage exploration begins with seamless chauffeured private transfers from your point of arrival. Witness iconic attractions, ancient monolithic sculptures, and sacred temple complexes that form the core of this UNESCO World Heritage site. This signature TRAGUIN Karnataka package ensures you experience Hampi sightseeing via an exceptional luxury presentation, including private expert historians, specialized coracle boat rides down the Tungabhadra River, and curated multi-course royal dining menus.\n\nWhy Visit Hampi? As the centerpiece of any premium Karnataka Tour Package, Hampi boasts a surreal topography of massive balancing granite boulders paired perfectly with intricately carved stone palaces. It stands proudly as one of the top tourist places in Karnataka, providing an incredible blend of historical grandeur, spiritual depth, and rustic charm."
        ),
        seo_title='KA-002 | Hampi Heritage Luxury Escape | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Hampi package (KA-002 / TRAGUIN-KA-HAMPI-002): Hemakuta Hill, Vittala Temple Stone Chariot, Lotus Mahal, Virupaksha Temple, Tungabhadra coracle ride, Anegundi Kishkindha trails, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Hemakuta Hill Temples, Sasivekalu Ganesha & Royal Environs sunset', 1),
            _ih('Vittala Temple Stone Chariot, Lotus Mahal & Elephant Stables', 2),
            _ih('Virupaksha Temple, Tungabhadra Coracle Ride & Anegundi Kishkindha Village', 3),
            _ih('TRAGUIN Signature Experience: Private family sunset walk on Hemakuta Hill with professional historian', 4),
            _ih('Premium Handpicked Hotels: 4-tier heritage luxury properties in Hampi / Hospet', 5),
        ],
        days=[
            _day(1, 'Arrival & Welcome to the Royal Realm | Sunset from Hemakuta Hill', (
                'Arrive at Hubli or Jindal Vijaynagar Airport, where a dedicated TRAGUIN premium holiday consultant and your private chauffeured luxury SUV await your arrival. Enjoy your premium welcome amenities as you travel along a highly scenic route towards the ancient imperial plains of Hampi. Check into your ultra-luxury heritage resort, a handpicked masterpiece reflecting classic Vijayanagara palace architecture. After relaxing, join your private personal historian for an afternoon orientation walk. Ascend the gentle slopes of Hemakuta Hill to witness an extraordinary panoramic sunset over a sea of ancient mandapas and spectacular giant boulders, starting your Premium Hampi Experience on a deeply emotional and memorable note.'
            ), [
                'Sightseeing Included: Hemakuta Hill Temples, Sasivekalu Ganesha, Royal Environs',
                'Optional Activities: Traditional Ayurvedic foot relaxation treatment at the resort',
                'Evening Experience: Private sundowner with traditional flute music performance',
                'Overnight Stay: Hampi Premium Luxury Resort',
                'Meals Included: Gourmet Dinner',
            ]),
            _day(2, 'The Architectural Marvels of Hampi | Stone Chariot & Royal Enclaves', (
                'Savor a lavish multi-cuisine breakfast before stepping out for an immersive day of comprehensive Hampi sightseeing. Begin at the world-famous Vijaya Vittala Temple, where you will marvel at the iconic Stone Chariot and the astonishing musical pillars that ring with melodic notes when gently tapped. Following a specially arranged luxury lunch break, explore the inner royal citadel. Admire the elegant geometry of the Lotus Mahal, the monumental Elephant Stables, the grand Mahanavami Dibba platform, and the immaculately carved Stepped Tank. As twilight arrives, enjoy a relaxing, scenic walk along the historic Hampi Bazaar, discovering the incredible scale of India\'s most iconic medieval trading center.'
            ), [
                'Sightseeing Included: Vittala Temple, Stone Chariot, Lotus Mahal, Elephant Stables',
                'Optional Activities: Private golf-cart exploration across the grand monument complex',
                'Evening Experience: Illumination viewing of selected royal monument structures',
                'Overnight Stay: Hampi Premium Luxury Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(3, 'Mythological Kishkindha Trails | Sacred Coracle Ride & Virupaksha Temple', (
                'Awaken early for a magical morning experience. Travel to the banks of the sacred Tungabhadra River for an exclusive, custom coracle boat ride—a traditional circular vessel that floats gracefully past hidden riverbank shrines and sheer granite gorges. Next, explore the grand Virupaksha Temple, an active place of worship since the 7th century, featuring a magnificent gopuram. In the afternoon, cross the river to visit Anegundi, an ancient village belonging to the mythical kingdom of Kishkindha from the epic Ramayana. Conclude your day with a short walk up Malyavanta Hill to hear beautiful live chanting of ancient verses while taking in an incredible panoramic view of the vast valley.'
            ), [
                'Sightseeing Included: Virupaksha Temple, Tungabhadra Coracle Ride, Anegundi Village',
                'Optional Activities: Coracle bird-watching excursion or bouldering for beginners',
                'Evening Experience: Curated royal multicourse culinary dinner at the resort garden',
                'Overnight Stay: Hampi Premium Luxury Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(4, 'Farewell to Hampi | Carrying Home Unforgettable Memories', (
                'Enjoy a relaxed morning breakfast on your private verandah overlooking beautiful lily ponds. Take advantage of your resort\'s world-class amenities with a refreshing swim or a stroll through the lush organic gardens. Your professional chauffeur will assist you with check-out and luggage handling as you begin your smooth return trip toward Hubli or Jindal Airport. Your exceptional TRAGUIN Karnataka tour package concludes as you arrive at the departure terminal, carrying home a collection of unforgettable luxury memories from an extraordinary heritage journey through time.'
            ), [
                'Sightseeing Included: En-route photography stops and panoramic vistas',
                'Optional Activities: Brief visit to the massive Tungabhadra Dam Gardens',
                'Evening Experience: Final warm assistance at the airport departure check-in',
                'Meals Included: Rich Buffet Breakfast',
            ]),
        ],
        hotels=[
            _hotel("Hampi's Boulders Resort / Heritage Resort Hampi", 'Hampi / Hospet', '03 Nights', 'Deluxe', 'Deluxe Cottage / Valley Room', 'Breakfast & Dinner (MAP)', 4, 1),
            _hotel('WelcomHeritage Shivavilas Palace', 'Hampi / Hospet', '03 Nights', 'Premium', 'Deluxe Heritage Room', 'Breakfast & Dinner (MAP)', 4, 2),
            _hotel('Evolve Back Kamalapura Palace, Hampi', 'Hampi / Hospet', '03 Nights', 'Luxury', 'Jal Mahal / Nivasa Suite', 'Breakfast & Dinner (MAP)', 5, 3),
            _hotel('Evolve Back Kamalapura Palace - Private Pool Villa', 'Hampi / Hospet', '03 Nights', 'Ultra Luxury', 'Exclusive Royal Tanishq Suite with Private Pool', 'Breakfast & Dinner (MAP)', 5, 4),
        ],
        inclusions=[
            _inc_included('Elite Accommodation: 03 Nights stay in handpicked, premier luxury properties in Hampi', 1),
            _inc_included('Bespoke Meal Plan: Daily lavish breakfast spreads and specialized multi-course dinners', 2),
            _inc_included('Luxury Transportation: All transfers, long-distance touring, and city sightseeing via an exclusive private premium SUV', 3),
            _inc_included('TRAGUIN Signature Welcoming: Traditional heritage welcome, cold towels, and a premium curated amenity kit upon arrival', 4),
            _inc_included('Exclusive Experiences: Private custom coracle boat ride on the Tungabhadra River', 5),
            _inc_included('Expert Guidance: Pre-booked entry tickets and a private professional historian guide for all key monuments', 6),
            _inc_included('Full Professional Coverage: All toll fees, driver allowances, fuel charges, and state permits', 7),
            _inc_included('TRAGUIN Support: Continuous 24/7 real-time remote concierge support from senior travel specialists', 8),
            _inc_excluded('Domestic or International airfares, flight bookings, or main interstate train ticket expenses', 9),
            _inc_excluded('Personal incidental expenses such as laundry services, mini-bar consumption, telephone calls, and room service', 10),
            _inc_excluded('Any specialized adventure activities, camera/video usage fees at monuments, or optional sightseeing detours', 11),
            _inc_excluded('Any meals, lunches, or beverage selections not specifically detailed in the official itinerary', 12),
            _inc_excluded('Mandatory peak festive season surcharges (Christmas, New Year, and major national holiday weeks)', 13),
            _inc_excluded('Travel insurance coverage and medical expenses of any nature', 14),
        ],
    )
    return package, itinerary


def build_ka_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-003'
    tour_code = 'TRAGUIN-KA-CRG-003'
    title = 'Coorg Romance • Captivating Highlands & Coffee Trails'
    duration = '04 Nights / 05 Days'
    slug = 'ka-003-coorg-romance-captivating-highlands-coffee-trails'
    itin_slug = 'ka-003-coorg-romance-captivating-highlands-coffee-trails-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Luxury Honeymoon Escape', 2),
            _ph('Destinations: Coorg (Madikeri • Kushalnagar)', 3),
            _ph('Ideal for: Newlyweds, Romantic Couples, Nature Lovers', 4),
            _ph('Best season: October to March (Lush Greenery Year-Round)', 5),
            _ph('Starting price: On Request (Premium Luxury Pricing)', 6),
            _ph('Vehicle: Private Luxury Sedan / Premium SUV', 7),
            _ph('Route Plan: Bangalore / Mangalore Arrival → Coorg (4N) → Departure', 8),
            _ph('TRAGUIN Signature Experience: Private candle-lit fine dining setting surrounded by natural coffee plantation valleys', 9),
            _ph('Honeymoon Delights: Romantic bed decoration, honeymoon cake, and non-alcoholic wine', 10),
            _ph('Shopping: Freshly roasted coffee beans, homemade fruit wines, wild honey, green cardamom and black pepper', 11),
            _ph("Instagram Spots: Abbey Falls, Raja's Seat sunset, Mandalpatti Peak, Namdroling Golden Temple", 12),
            _ph('Important: Mandalpatti 4x4 subject to weather; book ultra-luxury pool villas 45–60 days ahead in peak winter', 13),
        ],
        moods=['Romance', 'Nature', 'Luxury', 'Honeymoon'],
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
        tagline='Coorg Romance • Captivating Highlands & Coffee Trails • 04 Nights / 05 Days',
        overview=(
            "Welcome to your forever beginning, beautifully tailored by TRAGUIN. Step into a timeless romantic paradise designed exclusively for couples seeking a truly unforgettable Karnataka Honeymoon Package. Known affectionately as the Scotland of India, Coorg welcomes you into an enchanting realm filled with mist-covered mountain peaks, boundless aromatic spice estates, and cascading emerald waterfalls. This bespoke luxury getaway ensures your intimacy is surrounded by breathtaking landscapes, premium stays, and deeply immersive experiences curated down to the finest details.\n\nYour premium romantic holiday begins with a scenic drive from Bangalore or Mangalore, winding seamlessly upward into the misty highlands of Kodagu. This custom TRAGUIN Karnataka package seamlessly balances private leisure with exquisite handpicked exploration. Throughout your journey, you will enjoy a dedicated luxury vehicle, a personalized meal plan featuring authentic culinary notes, candle-lit fine dining, and exclusive experiences—from waking up to the rich aroma of handpicked coffee plantations to enjoying private nature trails handpicked by our expert advisors.\n\nWhy Choose Coorg for a Luxury Honeymoon Holiday? Coorg is highly celebrated as one of the ultimate honeymoon destinations in India. Its year-round pleasant climate, quiet private villa properties, and spectacular panoramic vistas make it the top choice for couples seeking a premium romantic atmosphere."
        ),
        seo_title='KA-003 | Coorg Romance Captivating Highlands Coffee Trails | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Coorg honeymoon package (KA-003 / TRAGUIN-KA-CRG-003): Raja\'s Seat sunset, Abbey Falls, Mandalpatti 4x4 Jeep, Namdroling Golden Temple, Dubare Elephant Camp, and 4-tier romantic resort accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Scenic Western Ghats Drive & Raja\'s Seat Sunset View', 1),
            _ih('Abbey Falls, Madikeri Fort & Private Coffee Estate Walk', 2),
            _ih('Mandalpatti Peak 4x4 Wilderness Jeep Drive', 3),
            _ih('Namdroling Golden Temple, Dubare Elephant Camp & Cauvery Riverbank', 4),
            _ih('TRAGUIN Signature Experience: Private candle-lit fine dining in coffee plantation valleys', 5),
        ],
        days=[
            _day(1, 'Arrival & Welcome to Coorg | Scenic Spice Drive & Sunset Romance', (
                'Arrive at Bangalore / Mangalore airport or terminal where a premium TRAGUIN representative will receive you with custom welcome amenities. Step into your private luxury vehicle and embark on a mesmerizingly scenic drive toward Coorg. As you climb higher into the Western Ghats, watch the urban scenery transform into breathtaking landscapes of dense forests and cascading greenery. Arrive at your ultra-luxury resort and settle into your private honeymoon cottage featuring a secluded plunge pool. In the late afternoon, enjoy a short romantic stroll to Raja\'s Seat (The Seat of Kings) to view a magical crimson sunset over the rolling misty horizons, accompanied by a premium personalized high-tea service.'
            ), [
                'Sightseeing Included: Scenic Western Ghats Drive, Raja\'s Seat Sunset View',
                'Optional Activities: Couple\'s traditional warm oil spa therapy',
                'Evening Experience: Private sunset high-tea overlooking deep misty valleys',
                'Overnight Stay: Premium Luxury Resort in Madikeri',
                'Meals Included: Curated Welcome Dinner',
            ]),
            _day(2, 'Coorg Heritage & Waterfalls | Immersive Wilderness Experiences', (
                'Wake up to the refreshing mountain breeze and savor an extensive multi-cuisine breakfast spread. Today features a magnificent Coorg Sightseeing path. Venture deep into lush rainforest paths to reach the spectacular Abbey Falls, where water roars down from a height of 70 feet. Walk hand-in-hand across the hanging bridge for perfect romantic photography points. In the afternoon, explore the historical Madikeri Fort and its unique palace museum architecture. Conclude your day\'s journey by returning to your premium resort for an exclusive plantation walk, learning how your favorite morning brews are grown, harvested, and perfectly roasted.'
            ), [
                'Sightseeing Included: Abbey Falls, Madikeri Fort, Private Coffee Estate Walk',
                'Optional Activities: Vintage coffee tasting session with a master barista',
                'Evening Experience: Exclusive candle-lit gourmet poolside dinner with live music',
                'Overnight Stay: Premium Luxury Resort in Madikeri',
                'Meals Included: Breakfast & Candle-Lit Dinner',
            ]),
            _day(3, 'Mandalpatti Off-Road Adventure | Touching the Clouds Together', (
                'An exhilarating morning awaits you. Board a private open-top 4x4 Jeep arranged by TRAGUIN and head towards the majestic Mandalpatti Peak. This off-road drive takes you through rugged wilderness paths and lush mountain grasslands. Reach the summit early to watch the clouds drift below you, creating a dreamlike landscape perfect for your premium honeymoon photoshoot. Return to the resort for a relaxed lunch. Spend your afternoon in complete tranquility, taking advantage of your luxury resort\'s world-class amenities, infinity swimming pool, or enjoying a private couples\' meditation session amidst pristine natural beauty.'
            ), [
                'Sightseeing Included: Mandalpatti Peak, 4x4 Wilderness Jeep Drive',
                'Optional Activities: Professional romantic couple\'s portrait session',
                'Evening Experience: Private bonfire night with premium wines under a starlit sky',
                'Overnight Stay: Premium Luxury Resort in Madikeri',
                'Meals Included: Breakfast & Gourmet Dinner',
            ]),
            _day(4, 'Kushalnagar Spiritual Exploration | Golden Temple & Elephant Sanctuary', (
                'Enjoy breakfast before driving down to Kushalnagar to discover the diverse cultural colors of Coorg. Visit the magnificent Namdroling Monastery, widely known as the Golden Temple, which houses breathtaking 40-foot gilded Buddha statues and exquisite Tibetan frescoes. Soak in the spiritual serenity of this sacred space. Afterward, take a romantic walk to the Dubare Elephant Camp along the banks of the Cauvery River. Here, you can watch these gentle giants being bathed and fed. Return to your mountain sanctuary in the evening for a special farewell experience curated uniquely for you.'
            ), [
                'Sightseeing Included: Namdroling Golden Temple, Dubare, Cauvery Riverbank',
                'Optional Activities: River rafting or coracle boat riding (seasonal)',
                'Evening Experience: Special 5-course signature Kodava tasting dinner',
                'Overnight Stay: Premium Luxury Resort in Madikeri',
                'Meals Included: Breakfast & Farewell Dinner',
            ]),
            _day(5, 'Farewell Coorg | Returning with Unforgettable Romantic Memories', (
                'Savor your final morning breakfast looking out onto the endless green valleys. Enjoy a relaxed morning taking photos around your resort\'s beautiful viewpoints. At your preferred time, check out and board your private luxury vehicle for your smooth return journey to Bangalore or Mangalore. As you descend from the hills, reflect on the wonderful moments from your unforgettable Coorg Honeymoon Package. Your premium vacation experience concludes with a drop-off at your designated airport or station, leaving you with beautiful memories to last a lifetime.'
            ), [
                'Sightseeing Included: Scenic return valley driving routes',
                'Optional Activities: Stopover shopping at local artisanal chocolate boutiques',
                'Evening Experience: Airport departure assistance from your private chauffeur',
                'Meals Included: Elegant Breakfast Buffet',
            ]),
        ],
        hotels=[
            _hotel('Club Mahindra Madikeri / Coorg Cliff Resort', 'Coorg', '04 Nights', 'Deluxe', 'Superior Valley View Room', 'Breakfast & Dinner (MAP)', 4, 1),
            _hotel('Amanvana Spa Resort / Welcomheritage Destination', 'Coorg', '04 Nights', 'Premium', 'Private Romantic Riverview Bungalow', 'Breakfast & Dinner (MAP)', 5, 2),
            _hotel('The Tamara Coorg / Taj Madikeri Resort & Spa', 'Coorg', '04 Nights', 'Luxury', 'Luxury Cottage / Symphony Suite', 'Breakfast & Gourmet Dinner (MAP)', 5, 3),
            _hotel('Evolve Back, Coorg (Formerly Orange County)', 'Coorg', '04 Nights', 'Ultra Luxury', 'Lily Pool Villa / Private Pool Luxury Mansion', 'All Inclusive Premium Plan', 5, 4),
        ],
        inclusions=[
            _inc_included('Premium Accommodations: 04 Nights stay in handpicked ultra-luxury romantic resorts', 1),
            _inc_included('Bespoke Meal Plan: Daily elaborate breakfast spreads and customized dinners across fine restaurants', 2),
            _inc_included('Luxury Private Transfers: All airport transfers and sightseeing via an exclusive air-conditioned premium vehicle', 3),
            _inc_included('Honeymoon Delights: A complimentary beautifully styled romantic bed decoration, honeymoon cake, and non-alcoholic wine', 4),
            _inc_included('Mandalpatti Adventure: Exclusive private 4x4 open Jeep excursion to Mandalpatti cloud view point', 5),
            _inc_included('Exclusive Plantation Trail: Guided intimate walking tour inside a private coffee and spice estate', 6),
            _inc_included('All-Inclusive Coverage: All state taxes, driver allowances, toll fees, parking tickets, and fuel charges', 7),
            _inc_included('TRAGUIN Support: 24/7 dedicated digital concierge support from our senior operations team', 8),
            _inc_excluded('Airfares, train tickets, or main transit bookings from your hometown', 9),
            _inc_excluded('Personal laundry, telephone calls, mini-bar charges, tips, or room service orders', 10),
            _inc_excluded('Monument entrance fees, camera permissions, or local adventure activity tickets', 11),
            _inc_excluded('Lunch meals or any additional beverage orders not listed in the standard inclusions', 12),
            _inc_excluded('Festival surcharges for special long weekends or major public holidays', 13),
        ],
    )
    return package, itinerary


def build_ka_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-004'
    tour_code = 'TRAGUIN-KA-EXPLORER-004'
    title = 'Karnataka Explorer'
    duration = '06 Nights / 07 Days'
    slug = 'ka-004-karnataka-explorer'
    itin_slug = 'ka-004-karnataka-explorer-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Premium Family Vacation', 2),
            _ph('Destinations: Bengaluru • Mysuru • Coorg (Madikeri)', 3),
            _ph('Ideal for: Families, Culture Seekers, Nature Lovers', 4),
            _ph('Best season: October to March (Plus Refreshing Monsoon Trails)', 5),
            _ph('Vehicle: Private Premium SUV (Innova Crysta / Luxury Van)', 6),
            _ph('Meal Plan: Daily Buffet Breakfast & Gourmet Dinners (MAPAI)', 7),
            _ph('Route Plan: Bengaluru (1N) → Mysuru (2N) → Coorg Madikeri (3N) → Bengaluru Drop', 8),
            _ph('TRAGUIN Curated Welcome Kits & 24/7 Priority Travel Concierge Support', 9),
            _ph('TRAGUIN Signature Experience: Private family coffee-tasting session inside an exclusive hundreds-of-years-old private estate in Madikeri', 10),
            _ph('Shopping: Mysore Silk sarees, sandalwood oils, Mysore Pak; Coorg cardamom, pepper, organic honey, Arabica coffee', 11),
            _ph("Instagram Spots: Mysore Palace illumination, Abbey Falls, Golden Temple Bylakuppe, Raja's Seat sunset", 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; hill viewpoint timings may change due to weather safety', 13),
        ],
        moods=['Nature', 'Family', 'Luxury', 'Heritage'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Explorer Tier)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='The Ultimate Heritage, Culture & Coffee Hills Luxury Tour • 06 Nights / 07 Days',
        overview=(
            "Welcome to an unforgettable luxury vacation experience proudly designed by TRAGUIN. This exclusive Karnataka Family Tour seamlessly takes you across the royal heritage lanes of Mysuru, the pristine mist-kissed coffee estates of Coorg, and the vibrant cosmopolitan highlights of Bengaluru. Hand-crafted to balance immersive cultural sightseeing with absolute relaxation, your family will enjoy private premium transportation, curated handpicked hotels, and unique signature touches that make this a truly premium Karnataka holiday package.\n\nYour bespoke TRAGUIN Karnataka Package begins in the dynamic garden city of Bengaluru before transporting your family through centuries of rich royal history in Mysuru. From the majestic monuments of the Wadiyar dynasty, your luxury route ascends into the breathtaking landscapes and scenic beauty of Coorg—the Scotland of India. Prepare for sensory immersion inside sprawling spice estates, encounters with magnificent elephants, and relaxing nights spent in the finest handpicked luxury resorts.\n\nWhy Visit Karnataka? As one of India's most highly rated tourism regions, a luxury Karnataka holiday delivers an exceptional mixture of ancient heritage and ecological richness. Multi-generational groups are continually captivated by the architectural brilliance of the iconic attractions in Mysuru and the refreshing, peaceful wilderness trails found in Coorg."
        ),
        seo_title='KA-004 | Karnataka Explorer | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Karnataka Explorer package (KA-004 / TRAGUIN-KA-EXPLORER-004): Bengaluru Palace, Mysore Palace, Srirangapatna, Namdroling Monastery, Abbey Falls, Talakaveri, and 4-tier luxury accommodation across three cities.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Lalbagh Gardens, Bengaluru Palace & Vidhana Soudha', 1),
            _ih('Srirangapatna Fort, Mysore Palace, Chamundi Hills & Brindavan Gardens', 2),
            _ih('Namdroling Golden Temple, Dubare Elephant Camp & Coorg highland sightseeing', 3),
            _ih('Abbey Falls, Madikeri Fort, Raja\'s Seat & Talakaveri Source', 4),
            _ih('TRAGUIN Signature Experience: Private family coffee-tasting in a centuries-old Madikeri estate', 5),
        ],
        days=[
            _day(1, 'Arrival in Bengaluru | Welcome to the Garden City', (
                'Arrive at Kempegowda International Airport or Bengaluru railway station, where an expert TRAGUIN luxury travel concierge will welcome your family. Transfer via private premium chauffeured vehicle to your premium stay hotel. After a refreshing afternoon, embark on an introductory tour of Bengaluru\'s historic landmarks. Wander through the lush botanical expanses of Lalbagh Gardens, photograph the majestic Tudor-style Bengaluru Palace, and drive past the monumental Vidhana Soudha.'
            ), [
                'Sightseeing Included: Lalbagh Gardens, Bengaluru Palace, Vidhana Soudha',
                'Optional Activities: Microbrewery dining tour in Indiranagar',
                'Evening Experience: Leisurely walking exploration of Cubbon Park lanes',
                'Overnight Stay: Bengaluru Premium Luxury Hotel',
                'Meals Included: Gourmet Welcome Dinner',
            ]),
            _day(2, 'Bengaluru to Mysuru | Heritage Trails of Srirangapatna', (
                'Savor a lavish breakfast and check out to begin your journey toward the royal capital of Mysuru. En route, stop at the historical island fortress town of Srirangapatna to explore Tipu Sultan\'s summer palace (Daria Daulat Bagh) and the ancient Ranganathaswamy Temple. Arrive in Mysuru in the afternoon and check into your grand heritage resort. In the evening, visit the world-famous Brindavan Gardens to witness a spectacular synchronized musical fountain show.'
            ), [
                'Sightseeing Included: Srirangapatna Fort, Summer Palace, Brindavan Gardens',
                'Optional Activities: Local artisanal wooden toy shopping at Channapatna',
                'Evening Experience: Musical fountain view with family photography',
                'Overnight Stay: Mysuru Premium Heritage Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(3, 'Full Day Mysuru Royal Sightseeing | Grand Palaces & Sacred Hills', (
                'Dedicate your day to an unforgettable Mysuru sightseeing journey. Begin with the iconic Mysore Palace, a spectacular masterpiece of Indo-Saracenic design. Next, ascend Chamundi Hills to seek blessings at the historic Chamundeshwari Temple and observe the massive monolith Nandi Bull. In the afternoon, explore the neo-Gothic architecture of St. Philomena\'s Church. Conclude your day with a private walk through the bustling Devaraja Market to experience vibrant sights and aromas.'
            ), [
                'Sightseeing Included: Mysore Palace, Chamundi Hills, St. Philomena\'s Church',
                'Optional Activities: Royal high-tea experience at Lalitha Mahal Palace',
                'Evening Experience: Illuminated palace night photography tour',
                'Overnight Stay: Mysuru Premium Heritage Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(4, 'Mysuru to Coorg | Tibetan Culture & Cascading Waterfalls', (
                'After breakfast, drive into the western ghats toward the breathtaking landscapes of Coorg. En route, visit Bylakuppe, the second largest Tibetan settlement outside Tibet, to witness the spectacular Golden Temple. Continue to the Dubare Elephant Camp along the Kaveri River, where your family can observe elephant bathing and feeding activities. Arrive at Madikeri and check into your handpicked luxury mountain resort nestled among deep coffee plantations.'
            ), [
                'Sightseeing Included: Namdroling Monastery (Golden Temple), Dubare Elephant Camp',
                'Optional Activities: River rafting experience at Dubare (seasonal)',
                'Evening Experience: Relaxing luxury bonfire night inside the resort estate',
                'Overnight Stay: Coorg Premium Wilderness Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(5, 'Coorg Highland Sightseeing | Mist-Kissed Valleys & Fortresses', (
                'Immerse yourself today in a comprehensive Coorg sightseeing trail. Witness the dramatic gush of Abbey Falls surrounded by dense spice plantations. Explore the historic Madikeri Fort, which houses archaeological artifacts and local history. In the late afternoon, gather at Raja\'s Seat, a beautiful historic garden where kings once relaxed to view breathtaking sunset panoramas across the misty mountain horizons.'
            ), [
                'Sightseeing Included: Abbey Falls, Madikeri Fort, Raja\'s Seat Outlook',
                'Optional Activities: Spice plantation walking tour with an expert botanist',
                'Evening Experience: Sunset viewing accompanied by traditional hot local coffee',
                'Overnight Stay: Coorg Premium Wilderness Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(6, 'Talakaveri Exploration | Journey to the River Source', (
                'Embark on a scenic drive to Talakaveri, located on the Brahmagiri hills, recognized as the sacred source of the Kaveri River. Climb the nearby steps to the hilltop for sweeping aerial views of the forest-clad hillsides. On the return route, stop at Bhagamandala to witness the holy confluence of three rivers. Spend your final evening at leisure within your ultra-luxury resort, perhaps enjoying a premium spa treatment or strolling through the coffee walking tracks.'
            ), [
                'Sightseeing Included: Talakaveri Source, Bhagamandala Temple, Brahmagiri Views',
                'Optional Activities: Traditional Kodava culinary cooking class',
                'Evening Experience: Family farewell dinner featuring live traditional music',
                'Overnight Stay: Coorg Premium Wilderness Resort',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(7, 'Coorg to Bengaluru | Heading Home with Premium Memories', (
                'Enjoy a leisurely breakfast on your private veranda overlooking the mist-filled valley. Check out from your mountain sanctuary as your premium private vehicle transfers you smoothly back to Bengaluru. Your exceptional TRAGUIN Karnataka Package concludes with a convenient drop-off at Kempegowda International Airport or the railway terminal, leaving your family with unforgettable memories of a perfect luxury vacation.'
            ), [
                'Sightseeing Included: Scenic return transit drive via the ghats',
                'Optional Activities: Gourmet lunch break at an estate restaurant',
                'Evening Experience: Warm assistance at the airport departure gate',
                'Meals Included: Rich Buffet Breakfast',
            ]),
        ],
        hotels=[
            _hotel('ITC Windsor / Radisson Blu / Radisson Blu Plaza / Grand Mercure / Club Mahindra Madikeri / Amanvana', 'Bengaluru / Mysuru / Coorg', '06 Nights', 'Deluxe', 'Executive Room / Deluxe Room / One Bedroom Suite or Villa (CP/MAP)', 'Breakfast & Dinner (MAP)', 4, 1),
            _hotel('The Leela Palace / JW Marriott / Royal Orchid Metropole / The Tamara Coorg', 'Bengaluru / Mysuru / Coorg', '06 Nights', 'Premium', 'Premier Room / Heritage Suite / Luxury Cabin (CP/MAP)', 'Breakfast & Dinner (MAP)', 5, 2),
            _hotel('Taj West End Bengaluru / Grand Mercure Mysore / Evolve Back, Coorg', 'Bengaluru / Mysuru / Coorg', '06 Nights', 'Luxury', 'Luxury Garden Room / Premium Heritage Suite / Heritage Pool Villa (CP/MAP)', 'Breakfast & Dinner (MAP)', 5, 3),
            _hotel('The Ritz-Carlton Bengaluru / The Oberoi or Lalitha Mahal Palace / Coorg Wilderness Resort & Spa', 'Bengaluru / Mysuru / Coorg', '06 Nights', 'Ultra Luxury', 'Deluxe Club Executive Suite / Grand Royal Suite / Grand Vega Suite with Private Butler (CP/MAP)', 'Breakfast & Dinner (MAP)', 5, 4),
        ],
        inclusions=[
            _inc_included('Premium Stays: 06 Nights stay in carefully selected, top-tier luxury hotels and wilderness resorts', 1),
            _inc_included('Bespoke Meal Plan: Lavish daily breakfast spreads and curated multi-course specialty dinners', 2),
            _inc_included('Luxury Transportation: All inter-city transfers and local sightseeing in an exclusive private premium SUV', 3),
            _inc_included('TRAGUIN Signature Amenities: Traditional welcome reception, cold towels, and customized family travel kits', 4),
            _inc_included('Exclusive Plantations: Private guided spice and coffee estate walk including coffee tasting sessions', 5),
            _inc_included('VIP Monument Access: Pre-booked entry access and private professional local guides at Mysore Palace', 6),
            _inc_included('Comprehensive Coverage: All interstate permits, fuel expenses, parking fees, toll taxes, and driver allowances', 7),
            _inc_included('TRAGUIN Support: 24/7 dedicated remote travel concierge desk assistance', 8),
            _inc_excluded('Domestic or International airline flight tickets or train fares to/from Bengaluru', 9),
            _inc_excluded('Personal expenses such as laundry services, mini-bar use, phone calls, and customized room service orders', 10),
            _inc_excluded('Camera and video recording fees at historical monuments and attractions', 11),
            _inc_excluded('Any lunches or alcoholic beverage selections not explicitly stated in the official meal plan', 12),
            _inc_excluded('Mandatory peak festive season room surcharges (during long national holidays or New Year weeks)', 13),
            _inc_excluded('Comprehensive personal medical and travel insurance policies', 14),
        ],
    )
    return package, itinerary


def build_ka_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-005'
    tour_code = 'TRG-KA-005'
    title = 'Udupi Murudeshwar Pilgrimage Coastal'
    duration = '04 Nights / 05 Days'
    slug = 'ka-005-udupi-murudeshwar-pilgrimage-coastal'
    itin_slug = 'ka-005-udupi-murudeshwar-pilgrimage-coastal-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Pilgrimage & Coastal Luxury', 2),
            _ph('Destinations: Mangalore • Udupi • Murudeshwar • Gokarna • Kollur Mookambika', 3),
            _ph('Ideal for: Family, Elders, Spiritual Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium FIT)', 6),
            _ph('Vehicle: Premium Private Luxury Sedan / SUV (Toyota Innova Crysta / Chauffeur Driven)', 7),
            _ph('Meal Plan: Modified American Plan (Breakfast & Dinner Included)', 8),
            _ph('Route Plan: Mangalore Arrival → Udupi (2N) → Murudeshwar (2N) → Mangalore Departure', 9),
            _ph('TRAGUIN Signature Experience: Private guided spiritual insights describing temple architecture and historical significance', 10),
            _ph('Shopping: Traditional Udupi sarees, authentic spices, sandalwood idols, brass temple lamps, Udupi banana chips', 11),
            _ph('Instagram Spots: Murudeshwar Shiva backdrop, Kapu Lighthouse sunset, St. Mary\'s Island basalt columns', 12),
            _ph('Important: Traditional dress code at coastal shrines; cotton attire recommended; advance booking for sea-facing rooms during festivals', 13),
        ],
        moods=['Pilgrimage', 'Spiritual', 'Family', 'Coastal'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium FIT)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Udupi • Murudeshwar • Kollur • Gokarna • Mangalore Heritage Tour • 04 Nights / 05 Days',
        overview=(
            "Embark on a soul-stirring quest across the golden coastlines and ancient sacred realms with our meticulously designed Karnataka pilgrimage tour. This bespoke itinerary weaves together deep spiritual heritage, breathtaking landscapes, and elite premium stays. From the majestic coastal vistas of Murudeshwar to the serene divine chambers of Udupi, let TRAGUIN orchestrate an immersive experience that leaves you with unforgettable memories and profound inner peace.\n\nCoastal Karnataka is a divine tapestry featuring some of India's most iconic attractions and iconic religious shrines. Choosing the Best Karnataka Tour Package unlocks access to the legendary Udupi Sri Krishna Temple, the sky-high Shiva Statue at Murudeshwar, and the powerful energy of the Kollur Mookambika Temple. Ideal for a deeply rejuvenating Karnataka Family Tour or a peaceful escape into heritage, this circuit offers breathtaking landscapes where the Western Ghats meet the Arabian Sea.\n\nFrom popular Instagram locations like the golden sands of Malpe Beach and St. Mary's Island to the profound ancient architecture of coastal shrines, this Premium Karnataka Experience satisfies both the spiritual seeker and the nature lover."
        ),
        seo_title='KA-005 | Udupi Murudeshwar Pilgrimage Coastal | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days coastal pilgrimage package (KA-005 / TRG-KA-005): Udupi Sri Krishna Temple, St. Mary\'s Island, Kollur Mookambika, Murudeshwar Shiva statue, Gokarna Mahabaleshwar, Kateel Durga Parameshwari, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Udupi Sri Krishna Temple Darshan, Anantheshwara Temple & Malpe Beach', 1),
            _ih("St. Mary's Island, Pajaka Kshetra & Kapu Beach Lighthouse", 2),
            _ih('Kollur Mookambika Temple, Murudeshwar Temple & Raja Gopura', 3),
            _ih('Gokarna Mahabaleshwar Temple, Om Beach & Mirjan Fort excursion', 4),
            _ih('TRAGUIN Signature Experience: Private guided spiritual insights on temple architecture and history', 5),
        ],
        days=[
            _day(1, 'Mangalore to Udupi | Arrival & Immersion in the Spiritual Cradle of Udupi', (
                'Welcome to Mangalore, the gateway to coastal splendor. Upon your arrival, our professional chauffeur will extend a warm luxury reception. Initiate your premium holiday with a smooth transfer towards the divine town of Udupi. Check-in to your handpicked premium hotel and unwind. In the evening, step into the tranquil corridors of the historic Udupi Sri Krishna Matha for an exclusive darshan. Witness the enchanting evening chariot festival and savor the peaceful ambiance. Savor exquisite traditional vegetarian cuisine for dinner.'
            ), [
                'Sightseeing Included: Udupi Sri Krishna Temple Darshan, Anantheshwara Temple',
                'Evening Experience: Traditional Mahapuja and Temple Chariot Procession',
                'Overnight Stay: Premium Handpicked Hotel in Udupi',
                'Meals Included: Dinner',
            ]),
            _day(2, 'Udupi & Surroundings | Exotic Island Adventure & the Secrets of Pajaka', (
                'After a sumptuous breakfast, journey to the pristine Malpe Beach. Board a premium boat to the geological wonder of St. Mary\'s Island, famous for its unique columnar basaltic rock formations and stunning photography points. Return for lunch, then proceed to Pajaka Kshetra, the sacred birthplace of Sri Madhvacharya. Conclude your day walking along the serene Kapu Beach, climbing its historic centenary lighthouse to capture breathtaking landscapes of the sun sinking into the Arabian Sea.'
            ), [
                'Sightseeing Included: St. Mary\'s Island, Pajaka Kshetra, Kapu Beach & Lighthouse',
                'Optional Activities: Water sports at Malpe Beach, local sweet shopping (Udupi Mattu Gulla)',
                'Overnight Stay: Premium Handpicked Hotel in Udupi',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(3, 'Udupi to Murudeshwar via Kollur | Divine Blessings at Kollur Mookambika & Majestic Shiva Visions', (
                'Check-out after breakfast and head through scenic routes toward the foothills of the Kodachadri hills. Arrive at the powerful Kollur Mookambika Temple, nestled beautifully on the banks of the Souparnika River. Experience a seamless and peaceful darshan of the divine mother. Post lunch, drive down to the spectacular coastal town of Murudeshwar. As you arrive, the towering 123-foot Shiva Statue overlooking the sea will take your breath away. Check-in to your premium seaside resort.'
            ), [
                'Sightseeing Included: Kollur Mookambika Temple, Murudeshwar Temple & Raja Gopura',
                'Evening Experience: Spectacular sunset views from the Murudeshwar temple cliffside',
                'Overnight Stay: Luxury Seaside Resort in Murudeshwar',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(4, 'Murudeshwar - Gokarna Excursion | Gokarna Mahabaleshwar Darshan & Untouched Coastal Trails', (
                'Today features a curated luxury excursion to the pristine town of Gokarna. Visit the ancient Mahabaleshwar Temple, housing the sacred Atmalinga, and immerse yourself in its deep mythological tales. Following the spiritual rituals, explore the gorgeous crescent-shaped Om Beach, famed for its natural spiritual outline. Relax at a luxury beachside café, indulge in fresh coconut water, and capture unforgettable memories at these popular Instagram locations before returning back to Murudeshwar for your last evening.'
            ), [
                'Sightseeing Included: Gokarna Mahabaleshwar Temple, Om Beach, Mirjan Fort',
                'Evening Experience: Leisure stroll along the Murudeshwar beach promenade',
                'Overnight Stay: Luxury Seaside Resort in Murudeshwar',
                'Meals Included: Breakfast & Dinner',
            ]),
            _day(5, 'Murudeshwar to Mangalore & Departure | Heritage Finale & Bidding Farewell to the Sacred Coast', (
                'Conclude your luxury holiday with a grand breakfast overlooking the ocean. Pack your bags full of memories as you check out and drive back to Mangalore. Along the way, visit the famous Kateel Durga Parameshwari Temple, situated elegantly on an island in the middle of the Nandini River. Time permitting, explore the historic Mangaladevi Temple. Our premium private vehicle will then drop you at Mangalore Airport or Railway Station for your onward journey, marking the flawless completion of your tour.'
            ), [
                'Sightseeing Included: Kateel Durga Parameshwari Temple, Mangaladevi Temple',
                'Meals Included: Breakfast',
            ]),
        ],
        hotels=[
            _hotel('Hotel Kediyoor / RNS Residency (Standard)', 'Udupi / Murudeshwar', '04 Nights', 'Deluxe', 'Standard Room', 'CP (Breakfast)', 3, 1),
            _hotel('Fortune Inn Valley View / RNS Residency (Sea View)', 'Udupi / Murudeshwar', '04 Nights', 'Premium', 'Sea View Room', 'MAP (Breakfast & Dinner)', 4, 2),
            _hotel('The Ocean Pearl Udupi / RNS Highway Hotel Luxury Suites', 'Udupi / Murudeshwar', '04 Nights', 'Luxury', 'Luxury Suite', 'MAP (Breakfast & Dinner)', 4, 3),
            _hotel('Country Inn & Suites by Radisson / TRAGUIN Elite Selected Private Villa Stay', 'Udupi / Murudeshwar', '04 Nights', 'Ultra Luxury', 'Premium Curated Villa / Suite', 'Premium Curated Meals', 5, 4),
        ],
        inclusions=[
            _inc_included('04 Nights premium handpicked hotel accommodations across Udupi and Murudeshwar', 1),
            _inc_included('Daily breakfast and dinner as specified in the plan', 2),
            _inc_included('All transfers & sightseeing in a private AC Luxury SUV/Sedan', 3),
            _inc_included('Dedicated professional English/Hindi-speaking chauffeur', 4),
            _inc_included('Tolls, fuel charges, parking, and driver allowances', 5),
            _inc_included('VIP Darshan coordination assistance at major shrines', 6),
            _inc_included('Welcome traditional amenities & customized drinking water', 7),
            _inc_included('Round-the-clock TRAGUIN local concierge support', 8),
            _inc_excluded('Airfare or train tickets to/from Mangalore', 9),
            _inc_excluded('Inner-sanctum special ritual/pooja tickets', 10),
            _inc_excluded('Boat cruise tickets to St. Mary\'s Island', 11),
            _inc_excluded('Personal expenses (laundry, telephone, tips)', 12),
            _inc_excluded('Any meals or drinks not explicitly listed', 13),
            _inc_excluded('Travel and medical insurance coverage', 14),
            _inc_excluded('Cost for optional adventure activities or water sports', 15),
        ],
    )
    return package, itinerary

def build_ka_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-006'
    tour_code = 'TRAGUIN-KA-006'
    title = 'Scotland of India Coorg Escape'
    duration = '03 Nights / 04 Days'
    slug = 'ka-006-scotland-of-india-coorg-escape'
    itin_slug = 'ka-006-scotland-of-india-coorg-escape-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Leisure Vacation / Luxury', 2),
            _ph('Destinations: Madikeri • Kushalnagar • Coorg', 3),
            _ph('Ideal for: Families, Couples & Leisure Seekers', 4),
            _ph('Best season: October to May', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Luxury FIT Getaway', 7),
            _ph('Vehicle: Dedicated Luxury Private AC Sedan / Innova Crysta', 8),
            _ph('Meal Plan: Modified American Plan (Buffet Breakfast & Multi-Cuisine Dinners)', 9),
            _ph('Route Map: Bangalore/Mysore Arrival → Kushalnagar → Madikeri (Coorg) → Bangalore Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts to offer an unparalleled leisure retreat with VIP arrival care, custom handpicked hotels, and executive private transportation', 11),
            _ph('Shopping: Local Coffee & Cardamom, Coorg Honey & Homemade Chocolates', 12),
            _ph("Instagram Spots: Majestic misty suspension bridge at Abbey Falls and sunset panoramic backdrops from Raja's Seat", 13),
            _ph('Important: Hotel check-in 14:00 hrs, check-out 11:00 hrs; light winter clothes recommended for late evening walks; book early for highest-rated villa view availability', 14),
        ],
        moods=['Nature', 'Leisure', 'Luxury'],
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
        tagline='Scotland of India Coorg Escape • 03 Nights / 04 Days',
        overview=(
            "Welcome to a mist-laden paradise where lush coffee estates kiss the skies. Curated with perfection by TRAGUIN, this exclusive high-end getaway to Coorg is hand-tailored to provide you with absolute relaxation, pristine scenic beauty, and premium stays. Awaken your senses to the aroma of fresh cardamom and rich Arabica beans while treating your family to world-class hospitality and unforgettable memories.\n\nCoorg, famously heralded as the Scotland of India, remains one of the most highly sought-after destinations for travelers searching for the Best Karnataka Tour Package or a romantic Coorg Honeymoon Package. Known for its rolling green hills, majestic rivers, and ancient temples, this pristine landscape promises a refreshing and soul-soothing mountain escape.\n\nTRAGUIN Curated Touch: This premium layout integrates high-comfort sightseeing, an exclusive private estate bean-to-cup coffee processing tour, majestic waterfall photography access, and curated luxury recommendations by our destination design consultants.\n\nWhy Visit Coorg: From the Tibetan cultural wonders at the Golden Temple in Bylakuppe to the cascading water streams at Abbey Falls and sunset panoramic vistas at Raja's Seat, our signature TRAGUIN Coorg Packages introduce you to iconic attractions through beautifully balanced, immersive experiences."
        ),
        seo_title='KA-006 | Scotland of India Coorg Escape | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Coorg package (KA-006 / TRAGUIN-KA-006): Bylakuppe Golden Temple, Abbey Falls, Madikeri Fort, Talakaveri, coffee estate walk, and 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Bylakuppe Golden Temple Monastery & Nisargadhama Deer Park', 1),
            _ih("Abbey Falls, Madikeri Fort, Omkareshwara Temple & Raja's Seat", 2),
            _ih('Talakaveri Temple, Bhagamandala Sangama & Estate Walk with coffee-tasting', 3),
            _ih('TRAGUIN Signature Experience: Curated by TRAGUIN Experts to offer an unparalleled leisure retreat', 4),
            _ih('Premium Handpicked Hotels: 4-tier luxury plantation resort options', 5),
        ],
        days=[
            _day(
            1,
            'Arrival & Kushalnagar to Coorg',
            (
                'Your premium vacation begins upon arrival at Bangalore or Mysore Airport/Station where a dedicated chauffeured luxury vehicle from TRAGUIN stands ready to greet you. Drive toward the misty hills of Coorg. En route, stop at Kushalnagar to marvel at the grand Bylakuppe Golden Temple (Namdroling Monastery), the second-largest Tibetan settlement outside Tibet, adorned with majestic 40ft gilded statues. Proceed to your handpicked premium luxury resort tucked inside a lush coffee plantation. Enjoy a smooth private check-in and unwind over a steaming cup of freshly brewed local coffee.'
            ),
            [
                'Sightseeing Included: Bylakuppe Golden Temple Monastery, Nisargadhama Deer Park',
                'Evening Experience: Leisure stroll across the tranquil forest trails of the resort or high-tea briefing by our experts',
                'Overnight Stay: Premium Handpicked Luxury Plantation Resort, Coorg',
                'Meals Included: Welcome Signature Drink & Gourmet Buffet Dinner'
            ],
            ),
            _day(
            2,
            'Madikeri Highlights Tour',
            (
                "Indulge in a luxurious, early morning buffet breakfast with a sweeping view of the plantation. Embark on a spectacular full-day journey of Coorg Sightseeing. Head first to the breathtaking Abbey Falls, where water cascades down amidst dense pepper vines and coffee bushes. Next, visit the historical Madikeri Fort to admire its centuries-old stone structures and architecture. As evening approaches, your chauffeur will escort you to the legendary Raja's Seat, a beautifully terraced seasonal garden where Coorg's kings used to sit to witness dramatic golden sunsets painting the valley."
            ),
            [
                "Sightseeing Included: Abbey Falls, Madikeri Fort, Omkareshwara Temple, Raja's Seat",
                "Photography Points: Suspended bridge at Abbey Falls & sunset horizons from Raja's Seat",
                'Overnight Stay: Premium Handpicked Luxury Plantation Resort, Coorg',
                'Meals Included: Full Buffet Breakfast & Fine-Dining Dinner'
            ],
            ),
            _day(
            3,
            'Coffee Estate Experiences & Talakaveri',
            (
                'Begin your morning with an exclusive, TRAGUIN-curated private walk through an expansive coffee estate. Learn from expert planters how premium Arabica and Robusta beans are cultivated, hand-sorted, and roasted to perfection. Following lunch, head uphill through winding mountain roads toward Talakaveri, nestled on the Brahmagiri hill range—the sacred source of the Kaveri River. Climb the steps for a panoramic view of the majestic undulating green vistas spread beneath you.'
            ),
            [
                'Sightseeing Included: Talakaveri Temple, Bhagamandala Sangama, Estate Walk',
                'Immersive Experiences: Coffee-tasting session sampling premium reserve single-origin roasts',
                'Overnight Stay: Premium Handpicked Luxury Plantation Resort, Coorg',
                'Meals Included: Full Buffet Breakfast & Curated Plantation Dinner'
            ],
            ),
            _day(
            4,
            'Coorg to Bangalore / Departure',
            (
                'Savor a relaxed final breakfast surrounded by morning bird-songs and mist. Check out from your premium oasis and head back to Bangalore or Mysore for your return journey. Your premium TRAGUIN Coorg Package concludes as you arrive at the airport or station with a heart filled with tranquility, ready to share beautiful stories of your luxury holiday.'
            ),
            [
                'Transfers Included: Private Chauffeured Intercity Drop-off',
                'Meals Included: Full Buffet Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('Coorg Cliff Resort', 'Coorg', '03 Nights', 'Deluxe', 'Premium Valley View Room', 'Breakfast & Dinner', 4, 1),
            _hotel('Club Mahindra Madikeri / Virajpet', 'Coorg', '03 Nights', 'Premium', 'Luxury Studio Apartment', 'Breakfast & Dinner', 5, 2),
            _hotel('The Tamara Coorg Luxury', 'Coorg', '03 Nights', 'Luxury', 'Luxury Cottage', 'Breakfast & Dinner', 5, 3),
            _hotel('Evolve Back, Coorg (Orange County)', 'Coorg', '03 Nights', 'Ultra Luxury', 'Heritage Pool Villa', 'All Meals & Plantation Tour', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at handpicked elite premium hotels or private pool villas', 1),
            _inc_included('Meals: Daily multi-cuisine buffet breakfasts and dinners at the resort dining rooms', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven AC luxury sedan or SUV for all point-to-point tours', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated professional guest concierge assistance during your trip', 4),
            _inc_included('Complimentary Experiences: Guided coffee estate walking experience and bespoke premium plantation coffee tasting', 5),
            _inc_included('Welcome Amenities: Refreshing welcome drink kit, packed mineral water, and premium sanitizer pack inside the vehicle', 6),
            _inc_included('Taxes: All applicable luxury state toll taxes, driver allowances, and parking fees', 7),
            _inc_excluded('Airfare or interstate rail travel tickets to and from Bangalore/Mysore', 8),
            _inc_excluded('Individual entry tickets, monument fees, safari charges, or activity camera passes', 9),
            _inc_excluded('Personal expenses such as laundry services, phone calls, mini-bar bills, and tips', 10),
            _inc_excluded('Optional tours, extreme sports, or extra vehicle usage beyond the itinerary path', 11),
            _inc_excluded('Comprehensive medical insurance or health emergency covers', 12),
        ],
    )
    return package, itinerary

def build_ka_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-007'
    tour_code = 'TRAGUIN-KA-007'
    title = 'Kabini & Nagarhole Luxury Wildlife Trail'
    duration = '03 Nights / 04 Days'
    slug = 'ka-007-kabini-nagarhole-luxury-wildlife-trail'
    itin_slug = 'ka-007-kabini-nagarhole-luxury-wildlife-trail-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Nature & Luxury Wildlife', 2),
            _ph('Destinations: Kabini • Nagarhole National Park', 3),
            _ph('Ideal for: Wildlife Enthusiasts & Families', 4),
            _ph('Best season: October to May', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Luxury Wildlife Expedition (FIT)', 7),
            _ph('Vehicle: Private Chauffeur-Driven Air-Conditioned Luxury Sedan / SUV', 8),
            _ph('Meal Plan: Jungle American Plan (All Meals Included at Wildlife Lodges)', 9),
            _ph('Route Map: Bangalore / Mysore Arrival → Kabini Backwaters → Nagarhole Jungle Rim → Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with elite lodge accommodations, premium private 4x4 options, and specialized river cruise slot assignments', 11),
            _ph('Shopping: Organic Wilderness Honey and Sandalwood Artworks from certified Mysore government outlets', 12),
            _ph('Important: Safari zones strictly allocated by State Forest Department; wear earth-toned clothing; no single-use plastic in sanctuary', 13),
        ],
        moods=['Wildlife', 'Nature', 'Luxury'],
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
        tagline='Kabini & Nagarhole Luxury Wildlife Trail • 03 Nights / 04 Days',
        overview=(
            "Welcome to the raw, untamed heartland of Southern India. This ultra-luxury nature expedition curated by TRAGUIN invites you into a world of breathtaking landscapes, premium stays, and iconic attractions. Venture through deep teak forests, listen to the call of the wild, and surrender to unforgettable memories across Karnataka's most celebrated forest ecosystems.\n\nFor travelers scouting the absolute Best Karnataka Tour Package or planning an exquisite Karnataka Family Tour, the Kabini river basin and Nagarhole Forest represent the true crest of Indian wildlife tourism. Renowned globally for hosting the highest density of Asian Elephants, majestic Bengal Tigers, and the elusive Indian Black Panther, this sanctuary provides a magnificent Premium Karnataka Experience.\n\nTRAGUIN Curated Touch: This custom luxury itinerary offers immersive experiences, signature open-top custom 4x4 jungle safaris, elite resident naturalist companions, and priority water-cruise bookings tailored for high-end wildlife travelers.\n\nWhy Visit Kabini & Nagarhole: Capture awe-inspiring moments at famous Instagram locations, enjoy a peaceful coracle boat ride on the Kabini River, or spot rare birds from your private deck during dry winter-spring months when wildlife congregations around the riverbed create natural masterpieces."
        ),
        seo_title='KA-007 | Kabini & Nagarhole Luxury Wildlife Trail | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Kabini wildlife package (KA-007 / TRAGUIN-KA-007): Nagarhole jungle safari, Kabini river cruise, coracle ride, eco-village walk, and 4-tier waterfront lodge options.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Scenic Backwater Drive, Naturalist Briefing & Lake Overlook', 1),
            _ih('Nagarhole Jungle Tracks & River Cruise Expedition', 2),
            _ih('Core Zone Safari, Coracle Ride Experience & Eco-Village Walk', 3),
            _ih('TRAGUIN Signature Experience: Elite lodge accommodations and specialized river cruise slot assignments', 4),
            _ih('Premium Handpicked Hotels: Award-winning eco-luxury wildlife lodges', 5),
        ],
        days=[
            _day(
            1,
            'Bangalore / Mysore to Kabini',
            (
                'Arrive at Bangalore or Mysore airport/station, where your private TRAGUIN chauffeur welcomes you. Embark on a premium drive passing through changing terrain into the legendary woods of Kabini. Upon reaching your ultra-luxury jungle resort, enjoy a seamless check-in and refresh with an exotic welcome drink. Spend your afternoon admiring the scenic beauty of the calm waterfront. At dusk, gather by the campfire to watch an insightful documentary presented by an expert wildlife naturalist.'
            ),
            [
                'Sightseeing Included: Scenic Backwater Drive, Naturalist Briefing, Lake Overlook',
                'Evening Experience: A premium curated high-tea on the bank of the river, organized by TRAGUIN experts',
                'Overnight Stay: Ultra-Luxury Handpicked Waterfront Lodge, Kabini',
                'Meals Included: Lunch & Gourmet Wilderness Dinner'
            ],
            ),
            _day(
            2,
            'Kabini & Nagarhole Wildlife Safari',
            (
                'Awake to the crisp morning air and bird songs. Board a specially authorized 4x4 open-top vehicle for a thrilling morning safari through Nagarhole National Park. Trace the paths of tigers, leopards, and giant bison alongside an expert tracker. Return to the resort for a premium breakfast and relaxation. In the late afternoon, enjoy an exclusive boat safari across the Kabini River, capturing magnificent herds of elephants coming down to bathe at water points.'
            ),
            [
                'Sightseeing Included: Nagarhole Jungle Tracks, River Cruise Expedition',
                'Photography Points: Elephant herds along the water edge and pristine forest canopies under golden hour sunlight',
                'Overnight Stay: Ultra-Luxury Waterfront Lodge, Kabini',
                'Meals Included: Jungle Buffet Breakfast, Lunch, and Fine Dining Dinner'
            ],
            ),
            _day(
            3,
            'Jungle Immersion & Experiences',
            (
                'Your day begins with another masterfully coordinated safari session inside deep core zones to tracking big cats. Returning to your resort, savor a lazy afternoon by your private plunge pool. Later, step onto a traditional circular coracle boat for an intimate water excursion. End your evening visiting a local eco-village settlement to hear immersive tales of forest legends, lifestyle habits, and ancestral tribal culture.'
            ),
            [
                'Sightseeing Included: Core Zone Safari, Coracle Ride Experience, Eco-Village Walk',
                'Optional Activities: Relaxing traditional spa treatment overlooking the vast forest rim',
                'Overnight Stay: Premium Handpicked Wilderness Lodge, Kabini',
                'Meals Included: All Gourmet Meals (Breakfast, Lunch & Dinner)'
            ],
            ),
            _day(
            4,
            'Departure from Kabini',
            (
                'Savor an elegant breakfast on the lakeside deck, soaking in final views of the forest landscape. Pack your travel bags filled with unforgettable memories. Your luxury private vehicle will transfer you back comfortably to Mysore or Bangalore for your onward connection home. Your specialized TRAGUIN Karnataka Package concludes perfectly.'
            ),
            [
                'Transfers Included: Private Premium Airport / Station Drop-off',
                'Meals Included: Sumptuous Lakeside Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('Waterwoods Lodges & Resorts, Kabini', 'Kabini', '03 Nights', 'Deluxe', 'Superior Lake View Room', 'Jungle AP (All Meals)', 4, 1),
            _hotel('The Serai Resort, Kabini', 'Kabini', '03 Nights', 'Premium', 'Luxury Waterfront Cabin', 'Jungle AP (All Meals)', 5, 2),
            _hotel('Kaav Safari Lodge, Kabini', 'Kabini', '03 Nights', 'Luxury', 'Luxury Glamping Tent / Cottage', 'Jungle AP (All Meals)', 5, 3),
            _hotel('Evolve Back, Kuruba Safari Lodge', 'Kabini', '03 Nights', 'Ultra Luxury', 'Safari Hut with Private Pool', 'Ultra Luxury All Meals Included', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 3 Nights stay at award-winning premium stays and eco-luxury wildlife lodges', 1),
            _inc_included('Meals: All meals included (Breakfasts, Lunches, High-Teas, and Dinners) during the resort stay', 2),
            _inc_included('Transfers: Private Chauffeur-driven AC Innova Crysta / Premium SUV for all transit paths', 3),
            _inc_included('Sightseeing: Forest entry permits, professional naturalist tracking fees, and scheduled open-top jeep safaris', 4),
            _inc_included('Assistance: 24/7 priority concierge and real-time remote destination monitoring by TRAGUIN support', 5),
            _inc_included('Welcome Amenities: Personalized eco-friendly jungle kit with insulated bottles, natural bug-repellents, and organic treats', 6),
            _inc_excluded('Airfare or inter-state rail transportation tickets to and from Bangalore', 7),
            _inc_excluded('Personal luxury services such as specialized premium body spa therapies, laundry, and vintage alcohol orders', 8),
            _inc_excluded('Excess camera gear permit fees charged directly at forest entry gates', 9),
            _inc_excluded('Travel insurance and expenses emerging from flights delays or natural route diversions', 10),
        ],
    )
    return package, itinerary

def build_ka_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-008'
    tour_code = 'TRAGUIN-KA-008'
    title = 'Gokarna Beach • Murudeshwar Express'
    duration = '04 Nights / 05 Days'
    slug = 'ka-008-gokarna-beach-murudeshwar-express'
    itin_slug = 'ka-008-gokarna-beach-murudeshwar-express-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Beach Leisure / Luxury Vacation', 2),
            _ph('Destinations: Gokarna Beach • Murudeshwar • Netrani Island', 3),
            _ph('Ideal for: Families, Couples, Beach Lovers', 4),
            _ph('Best season: October to March', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Luxury Coastal FIT Getaway', 7),
            _ph('Vehicle: Luxury Chauffeur-Driven Air-Conditioned Sedan / SUV (Crysta)', 8),
            _ph('Meal Plan: Buffet Breakfasts & Curated Gourmet Dinners Included', 9),
            _ph('Route Map: Mangalore/Goa Arrival → Murudeshwar → Gokarna Beach → Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with guaranteed private sea-view accommodations, exclusive high-tea setups during beach sunsets, and seamless VIP lane access at major shrines', 11),
            _ph('Shopping: Gokarna Markets — handmade brass items, natural incense sticks, organic spices, and classic bohemian apparel', 12),
            _ph('Important: Standard check-in starts at 14:00 hrs; coastal belt best explored October to March', 13),
        ],
        moods=['Beach', 'Leisure', 'Luxury'],
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
        tagline='Gokarna Beach • Murudeshwar Express • 04 Nights / 05 Days',
        overview=(
            "Welcome to the mesmerizing coastline of Karnataka. This exclusive, high-end private escape curated carefully by TRAGUIN unrolls a perfect canvas of breathtaking landscapes, sacred wonders, and sun-kissed beaches. From the majestic sea-facing Shiva icon of Murudeshwar to the raw, pristine bohemian allure of Gokarna Beach, indulge in immersive experiences, premium stays, and unforgettable memories tailored precisely for you.\n\nThe coast of Karnataka stands out as one of India's top luxury getaway zones, boasting a perfect blend of rich heritage and tranquil shores. For those planning the Best Karnataka Tour Package or a relaxing Karnataka Family Tour, this tropical circuit offers iconic attractions like the world's second-tallest Shiva statue and untouched golden sands.\n\nTRAGUIN Curated Touch: This Luxury Karnataka Holiday includes handpicked premium beach resorts, a personalized expert itinerary guide, high-tea sunsets over iconic attractions, and zero-fatigue driving maps designed by travel consultants.\n\nWhy Visit Coastal Karnataka: From exploring the unique geological rock formations of Yana to relaxing on the pristine sands of Om Beach, a Luxury Karnataka Holiday promises scenic beauty and spiritual rejuvenation with exclusive beachside dining options."
        ),
        seo_title='KA-008 | Gokarna Beach • Murudeshwar Express | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days coastal Karnataka package (KA-008 / TRAGUIN-KA-008): Murudeshwar Temple, Mirjan Fort, Om Beach, Yana Rocks, and 4-tier beach resort accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Murudeshwar Temple, Tallest Shiva Statue & Raja Gopuram Viewpoint', 1),
            _ih('Mirjan Fort Exploration & Gokarna Town Heritage Tour', 2),
            _ih('Om Beach, Kudle Beach & Paradise Beach Vista', 3),
            _ih('Yana Caves & Monolith Rock Formations, Vibhooti Waterfalls', 4),
            _ih('TRAGUIN Signature Experience: Private sea-view accommodations and VIP shrine access', 5),
        ],
        days=[
            _day(
            1,
            'Arrival & Transfer to Murudeshwar',
            (
                'Arrive at the airport/station where your premium private vehicle awaits. Enjoy a smooth scenic drive through coastal paths to Murudeshwar. Check into your premium sea-facing resort. In the afternoon, visit the legendary Murudeshwar Temple complex and marvel at the colossal 123-foot Lord Shiva statue backdropped by the Arabian Sea. Witness a glorious oceanic sunset directly from the Raja Gopuram tower.'
            ),
            [
                'Sightseeing Included: Murudeshwar Temple, Tallest Shiva Statue, Raja Gopuram Viewpoint',
                'Evening Experience: A relaxing evening walk along the pristine Murudeshwar beach promenade',
                'Overnight Stay: Premium Sea-View Hotel, Murudeshwar',
                'Meals Included: Gourmet Welcome Dinner'
            ],
            ),
            _day(
            2,
            'Murudeshwar to Gokarna',
            (
                'Savor a luxurious breakfast before traveling north along the coast towards the bohemian beach paradise of Gokarna. En route, experience a private heritage tour of the historical Mirjan Fort, a majestic structure reflecting old historical grandeur. Upon arrival in Gokarna, check into your ultra-luxury cliffside beach resort and unwind amidst lush tropical greenery.'
            ),
            [
                'Sightseeing Included: Mirjan Fort Exploration, Gokarna Town Heritage Tour',
                'Photography Points: The moss-covered ancient stone walls of Mirjan Fort',
                'Overnight Stay: Premium Luxury Beach Resort, Gokarna',
                'Meals Included: Full Buffet Breakfast & Dinner'
            ],
            ),
            _day(
            3,
            'Gokarna Beach Trek & Leisure',
            (
                'Today is dedicated to the finest beach destinations in Karnataka. Embark on a highly comfortable, curated boat cruise or a gentle walk around the famous Om Beach, named after its natural spiritual shape. Explore the serene waters of Kudle Beach, Half Moon Beach, and Paradise Beach. Spend your afternoon soaking in the golden sun or enjoying an exclusive spa session at your resort.'
            ),
            [
                'Sightseeing Included: Om Beach, Kudle Beach, Paradise Beach Vista',
                'Optional Activities: Premium speed boat cruise, ayurvedic body massage, or local café hopping',
                'Overnight Stay: Premium Luxury Beach Resort, Gokarna',
                'Meals Included: Breakfast & Seafood Special Dinner'
            ],
            ),
            _day(
            4,
            'Excursion to Yana Rocks',
            (
                'After a delicious morning breakfast, enjoy a scenic drive into the Western Ghats to witness the breathtaking landscape of Yana Rocks. Walk through deep tropical forests to discover two massive, awe-inspiring black crystalline limestone monoliths towering over the valley. Return to Gokarna for your final sunset experience over the cliffs.'
            ),
            [
                'Sightseeing Included: Yana Caves & Monolith Rock Formations, Vibhooti Waterfalls',
                'Immersive Experiences: Dip your feet in the cool natural stream of Vibhooti water cascades',
                'Overnight Stay: Premium Luxury Beach Resort, Gokarna',
                'Meals Included: Breakfast & Candlelit Dinner'
            ],
            ),
            _day(
            5,
            'Departure from Gokarna',
            (
                'Savor a relaxed gourmet breakfast with oceanic panoramas. Enjoy free time for a last dip in the warm waters before boarding your private luxury vehicle. Transfer smoothly back to the airport or station for your return journey. Your unforgettable TRAGUIN Karnataka Package concludes perfectly.'
            ),
            [
                'Transfers Included: Private Airport/Station Drop-off',
                'Meals Included: Full Buffet Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('RNS Residency (Sea View) / Gokarna Forest Resort', 'Murudeshwar / Gokarna', '04 Nights', 'Deluxe', 'Sea View / Forest Room', 'CP (Breakfast Only)', 4, 1),
            _hotel('Naveen Beach Resort / Stone Wood Nature Resort', 'Murudeshwar / Gokarna', '04 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast + Dinner)', 5, 2),
            _hotel('RNS Highway Hotel (Luxury Suite) / Kahani Paradise (Luxury Villa)', 'Murudeshwar / Gokarna', '04 Nights', 'Luxury', 'Luxury Suite / Luxury Villa', 'MAPAI (Breakfast + Dinner)', 5, 3),
            _hotel('The Ocean Bliss Premium / SwaSwara - CGH Earth (Wellness Suite)', 'Murudeshwar / Gokarna', '04 Nights', 'Ultra Luxury', 'Premium Suite / Wellness Suite', 'Gourmet Meal Plan Included', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: Premium luxury stays at handpicked beachside resorts', 1),
            _inc_included('Meals: Daily breakfasts and dinners as per the selected premium meal package', 2),
            _inc_included('Transfers & Sightseeing: All commutes in a private luxury air-conditioned Innova Crysta / Sedan', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated travel advisor assistance and certified local companion guides', 4),
            _inc_included('Welcome Amenities: Refreshing tropical welcome drinks, mineral water, and premium snack kit inside the vehicle', 5),
            _inc_excluded('Flight tickets or railway passes to Mangalore/Goa/Hubli', 6),
            _inc_excluded('Guide tips, photography tickets, and personal laundry charges', 7),
            _inc_excluded('Water sports activities like scuba diving or jet skiing at Netrani Island', 8),
        ],
    )
    return package, itinerary

def build_ka_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-009'
    tour_code = 'TRAGUIN-KA-009'
    title = 'Badami • Aihole • Pattadakal Caves Escape'
    duration = '04 Nights / 05 Days'
    slug = 'ka-009-badami-aihole-pattadakal-caves-escape'
    itin_slug = 'ka-009-badami-aihole-pattadakal-caves-escape-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Offbeat / Heritage / Luxury', 2),
            _ph('Destinations: Badami • Aihole • Pattadakal Caves • Hubli', 3),
            _ph('Ideal for: Heritage Enthusiasts & Couples', 4),
            _ph('Best season: October to March', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Heritage Luxury FIT Getaway', 7),
            _ph('Vehicle: Private Chauffeur-driven Luxury AC SUV (Innova Crysta)', 8),
            _ph('Meal Plan: Modified American Plan (Daily Breakfast & Fine-Dining Dinners)', 9),
            _ph('Route Map: Hubli Arrive → Badami → Pattadakal → Aihole → Hubli Depart', 10),
            _ph('TRAGUIN Signature Experience: Curated carefully by TRAGUIN experts with pre-arranged express monument credentials and top-tier cultural historians', 11),
            _ph('Shopping: Ilkal Handlooms and Handmade Artifacts — miniature sandstone carvings and authentic regional spice mixes', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; comfortable footwear required; vehicle packed with ice-chilled water', 13),
        ],
        moods=['Heritage', 'Culture', 'Luxury'],
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
        tagline='Badami • Aihole • Pattadakal Caves Escape • 04 Nights / 05 Days',
        overview=(
            "Step back in time into the magnificent cradle of Chalukyan architecture. This ultra-premium, expertly curated offbeat heritage holiday by TRAGUIN uncovers the dramatic red sandstone cliffs of Badami, the pristine structural masterpieces of Aihole, and the UNESCO World Heritage monuments of Pattadakal. Crafted flawlessly for modern travelers seeking an elite, deeply immersive cultural experience balanced with private transfers and handpicked accommodations.\n\nUnlocking northern Karnataka's historic landscape presents an unmatched journey through ancient rock-cut cave shrines, timeless inscriptions, and dramatic red monolith cliffs. Perfect as a boutique Karnataka Honeymoon Package or an enriching Karnataka Family Tour, this region delivers absolute tranquility far from standard tourist crowds.\n\nTRAGUIN Curated Touch: This bespoke itinerary includes an authorized architectural specialist guide, private countryside picnics, custom entry assistance across complex monuments, and handpicked premium hotel stays.\n\nWhy Choose This Circuit: From capturing stunning photos at the edge of Agastya Lake to walking through ancient temple complexes that formed the blueprint for South Indian temple design, our Luxury Karnataka Holiday guarantees sophisticated comfort during cooler months where every corner serves as a spectacular backdrop for photography."
        ),
        seo_title='KA-009 | Badami • Aihole • Pattadakal Caves Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days heritage Karnataka package (KA-009 / TRAGUIN-KA-009): Badami Cave Temples, Pattadakal UNESCO site, Aihole Durga Temple, Banashankari & Mahakuta, and 4-tier resort accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Agastya Lake, Bhutanatha Temple group at sunset', 1),
            _ih('Badami Cave Temples (1, 2, 3, and 4), Badami Fort & Museum', 2),
            _ih('Pattadakal Monument Complex, Aihole Durga Temple Group & Ravana Phadi Cave', 3),
            _ih('Banashankari Temple, Mahakuta Temple Complex & Ilkal Weaving Village', 4),
            _ih('TRAGUIN Signature Experience: Express monument credentials and top-tier cultural historians', 5),
        ],
        days=[
            _day(
            1,
            'Hubli to Badami Arrival',
            (
                'Arrive at Hubli Airport where your professional TRAGUIN holiday concierge greets you. Board your private luxury vehicle for a smooth, scenic drive toward Badami. Witness changing landscapes transition into majestic red sandstone formations. Upon arrival, check into your premium hotel and relax. In the evening, visit the serene Bhutanatha Temple complex standing gracefully at the edge of the historic Agastya Lake as the twilight sky sets an elegant mood.'
            ),
            [
                'Sightseeing Included: Agastya Lake, Bhutanatha Temple group at sunset',
                'Evening Experience: A warm custom welcome briefing over local premium high-tea',
                'Overnight Stay: Handpicked Luxury Resort, Badami',
                'Meals Included: Welcome Drink & Gourmet Dinner'
            ],
            ),
            _day(
            2,
            'Badami Caves Exploration',
            (
                'Enjoy a rich, traditional breakfast before entering the iconic Badami Caves. Carved directly into monolithic sandstone cliffs, these four magnificent cave temples feature detailed high-relief sculptures representing Vedic and Jain mythologies. Climb the ancient rock steps accompanied by an expert companion architectural storyteller. Later, explore the Badami Fort paths and the nearby archaeological museum housing rare ancient relics.'
            ),
            [
                'Sightseeing Included: Badami Cave Temples (1, 2, 3, and 4), Badami Fort, Museum',
                'Photography Points: Panoramic views of the old town from Cave 3, and reflection views across Agastya Lake',
                'Overnight Stay: Handpicked Luxury Resort, Badami',
                'Meals Included: Full Breakfast & Curated Course Dinner'
            ],
            ),
            _day(
            3,
            'Excursion to Pattadakal & Aihole',
            (
                'Embark on a grand historical excursion after breakfast. First, arrive at the UNESCO World Heritage site of Pattadakal, positioned gracefully on the banks of the Malaprabha River. Marvel at the Virupaksha Temple, an architectural triumph displaying a perfect fusion of Northern and Southern Indian structural arts. Post lunch, drive to Aihole, universally acknowledged as the cradle of Indian temple architecture, featuring over 120 stone temples. Explore the unique semi-circular design of the Durga Temple and the historic Lad Khan Temple.'
            ),
            [
                'Sightseeing Included: Pattadakal Monument Complex, Aihole Durga Temple Group, Ravana Phadi Cave',
                'Immersive Experiences: Gourmet countryside picnic lunch curated by TRAGUIN experts amidst royal surroundings',
                'Overnight Stay: Handpicked Luxury Resort, Badami',
                'Meals Included: Breakfast, Picnic Lunch, and Dinner'
            ],
            ),
            _day(
            4,
            'Banashankari & Mahakuta Sightseeing',
            (
                "Discover offbeat cultural treasures today. Visit the ancient Banashankar Amma Temple, set near a majestic stone-carved water tank. Proceed next to the hidden valley temple of Mahakuta, a serene forest sanctuary dedicated to Lord Shiva, renowned for its natural mountain spring flowing into a central stone pool. Spend your evening browsing traditional weavers' quarters to witness the creation of the world-famous hand-woven Ilkal sarees."
            ),
            [
                'Sightseeing Included: Banashankari Temple, Mahakuta Temple Complex, Ilkal Weaving Village',
                'Food Suggestions: Savor traditional regional specialties like Jowar Roti accompanied by organic stuffed eggplant dishes',
                'Overnight Stay: Handpicked Luxury Resort, Badami',
                'Meals Included: Breakfast & Festive Farewell Dinner'
            ],
            ),
            _day(
            5,
            'Badami to Hubli Departure',
            (
                'Savor a luxurious breakfast overlooking the morning mist rising from the sandstone cliffs. Pack your belongings and board your premium private vehicle for a comfortable return drive to Hubli. Your incredible TRAGUIN Karnataka Package concludes as your driver drops you directly at the airport for your onward journey home.'
            ),
            [
                'Transfers Included: Private Luxury Airport Drop-off',
                'Meals Included: Full Buffet Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('Badami Court Hotel', 'Badami', '04 Nights', 'Deluxe', 'Deluxe Pool View Room', 'MAP (Breakfast + Dinner)', 4, 1),
            _hotel('Heritage Resort Badami', 'Badami', '04 Nights', 'Premium', 'Premium Executive Cottage', 'MAP (Breakfast + Dinner)', 5, 2),
            _hotel('The Krishna Heritage Luxury / Nilaya Imperial Suite', 'Badami', '04 Nights', 'Luxury', 'Royal Suite / Imperial Suite', 'MAP (Breakfast + Dinner)', 5, 3),
            _hotel('Evolve Back Kamalapura Palace (Hampi Excursion Link)', 'Badami / Hampi', '04 Nights', 'Ultra Luxury', 'Bespoke Palace Suite', 'All Meals Included', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 04 Nights luxury stay at handpicked premium resorts', 1),
            _inc_included('Meals: Daily multi-cuisine buffet breakfasts and fine-dining dinners at properties', 2),
            _inc_included('Transfers & Sightseeing: Entire trip via private luxury AC Innova Crysta with a professional uniform-clad chauffeur', 3),
            _inc_included('TRAGUIN Support: 24/7 priority concierge line and instant back-end itinerary management', 4),
            _inc_included('Complimentary Experiences: Guided village stroll in Ilkal and private sunset tea setups overlooking Agastya Lake', 5),
            _inc_included('Welcome Amenities: Customized travel kit containing refreshing cooling mists, artisanal sweet platters, and unlimited sealed mineral water', 6),
            _inc_excluded('Flights, train tickets, or helicopter charters to Hubli', 7),
            _inc_excluded('Monument entrance tickets, professional camera fees, or local authority taxes', 8),
            _inc_excluded('Personal elements such as laundry bills, room service items, or tips', 9),
            _inc_excluded('Supplemental travel or medical insurance programs', 10),
        ],
    )
    return package, itinerary

def build_ka_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-010'
    tour_code = 'TRAGUIN-KA-010'
    title = 'Bandipur Tiger Reserve Safari Experience'
    duration = '02 Nights / 03 Days'
    slug = 'ka-010-bandipur-tiger-reserve-safari-experience'
    itin_slug = 'ka-010-bandipur-tiger-reserve-safari-experience-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Nature / Wildlife Luxury', 2),
            _ph('Destinations: Bandipur Tiger Reserve', 3),
            _ph('Ideal for: Nature Enthusiasts, Families & Couples', 4),
            _ph('Best season: October to May', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Luxury Wildlife Safari (FIT)', 7),
            _ph('Vehicle: Private Luxury Air-Conditioned SUV for transfers; Specialized Open 4x4 Safari Jeeps for forest exploration', 8),
            _ph('Meal Plan: Jungle Full Board Plan (All Gourmet Meals Included - Breakfast, Lunch, and Dinner)', 9),
            _ph('Route Details: Bangalore/Mysore Arrival → Bandipur National Park Forest Wilderness → Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts to optimize core safari timing loops with priority chalet allocation and custom natural history kits', 11),
            _ph('Shopping: Pure Forest Honey and Sandalwood Products from local tribal cooperatives', 12),
            _ph('Important: Safari allocations strictly controlled; wear earth tones; Bandipur is a strict no-plastic zone', 13),
        ],
        moods=['Wildlife', 'Nature', 'Adventure'],
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
        tagline='Bandipur Tiger Reserve Safari Experience • 02 Nights / 03 Days',
        overview=(
            "Step into the untamed heart of the Nilgiri Biosphere Reserve. This ultra-exclusive, deeply immersive Premium Karnataka Experience meticulously curated by TRAGUIN structural experts transports you into a world of breathtaking landscapes, dense deciduous canopies, and thrilling apex predator encounters. Prepare yourself for premium stays at handpicked hotels, exceptional personalized assistance, and unforgettable memories etched forever into your family's travel story.\n\nBandipur National Park stands proudly as one of the premier eco-tourism hubs of South India, highly sought after by travelers searching for a flawless Karnataka Family Tour or a magical Karnataka Honeymoon Package. Nestled under the shadow of the stunning Western Ghats, this reserve forms a crucial wildlife corridor alongside Mudumalai and Nagarhole.\n\nTRAGUIN Curated Touch: This Luxury Karnataka Holiday includes prioritized custom slots for government-regulated core zone jungle safaris, expert local naturalists, deep birdwatching trails, and premium hospitality tracking.\n\nWhy Visit Bandipur: From incredible Instagram-ready sunset points over the Gopalaswamy Betta peak to specialized cultural tribal interactions, this jungle getaway offers a perfect balance of high-octane adventure and restorative luxury."
        ),
        seo_title='KA-010 | Bandipur Tiger Reserve Safari Experience | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Bandipur safari package (KA-010 / TRAGUIN-KA-010): Core forest deep safari, Himavad Gopalaswamy Peak, and 4-tier jungle lodge accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Scenic Forest Route & Resort Nature Trail', 1),
            _ih('Core Forest Deep Safari & Himavad Gopalaswamy Peak', 2),
            _ih('TRAGUIN Signature Experience: Priority chalet allocation and custom natural history kits', 3),
            _ih('Premium Handpicked Hotels: Finest handpicked jungle resorts', 4),
        ],
        days=[
            _day(
            1,
            'Bangalore / Mysore to Bandipur',
            (
                'Arrive at the designated airport or railway station where your private chauffeur-driven luxury SUV awaits you. Begin a highly scenic, refreshing drive towards the Bandipur Tiger Reserve. As you cross the forest gates, look out for curious Langurs and elegant Spotted Deer greeting you along the roadside. Arrive at your ultra-luxury wilderness resort for a seamless priority check-in. Savor a refreshing traditional welcome beverage, settle into your premium cottage, and enjoy a curated high-tea presentation by wild country specialists.'
            ),
            [
                'Sightseeing Included: Scenic Forest Route, Resort Nature Trail',
                'Evening Experience: A heartwarming wildlife documentary screening followed by a cozy campfire under a star-lit sky',
                'Overnight Stay: Elite Jungle Lodge / Handpicked Luxury Resort, Bandipur',
                'Meals Included: Gourmet Buffet Lunch & Elegant Dinner'
            ],
            ),
            _day(
            2,
            'Bandipur Tiger Reserve',
            (
                'Wake up early to the soothing chorus of exotic birds. Sip freshly brewed local coffee before boarding an exclusive open 4x4 safari vehicle. Led by a highly trained local naturalist, venture deep into the misty core zones of the forest. Train your cameras on fresh pugmarks as you track the elusive leopard or majestic Bengal tiger. Return to your resort for a lavish breakfast and mid-day relaxation by the infinity pool. In the afternoon, embark on an excursion to Himavad Gopalaswamy Betta, the highest peak in the park, featuring an ancient temple and a permanent blanket of rolling clouds offering spectacular photography points.'
            ),
            [
                'Sightseeing Included: Core Forest Deep Safari, Himavad Gopalaswamy Peak',
                'Optional Activities: An instructive afternoon birdwatching walk around the resort perimeter',
                'Overnight Stay: Elite Jungle Lodge / Handpicked Luxury Resort, Bandipur',
                'Meals Included: Jungle Breakfast, Institutional Lunch & Farewell Bush Dinner'
            ],
            ),
            _day(
            3,
            'Bandipur to Bangalore / Mysore Departure',
            (
                "Enjoy a relaxed morning breakfast overlooking the pristine forest canopy. Take a slow walk through the resort's organic gardens or capture final photographs of the breathtaking landscapes. Complete your checkout and board your luxury private vehicle for a smooth transfer back to Mysore or Bangalore for your onward journey home. Your signature Karnataka Sightseeing vacation concludes with timeless stories and unforgettable memories."
            ),
            [
                'Transfers Included: Private Luxury Airport / Station Drop-off',
                'Meals Included: Full Buffet Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('Bandipur Safari Lodge (Jungle Lodges)', 'Bandipur', '02 Nights', 'Deluxe', 'Standard Forest Cottage', 'Jungle Full Board (All Meals)', 4, 1),
            _hotel('The Serai Bandipur', 'Bandipur', '02 Nights', 'Premium', 'Mountain View Cabin', 'Jungle Full Board (All Meals)', 5, 2),
            _hotel('Windflower Tusker Trails', 'Bandipur', '02 Nights', 'Luxury', 'Luxury Jungle Suite', 'Jungle Full Board (All Meals)', 5, 3),
            _hotel('Evolve Back, Kabbi / Premium Bandipur Enclave', 'Bandipur', '02 Nights', 'Ultra Luxury', 'Private Pool Wilderness Villa', 'Ultra All-Inclusive Luxury Plan', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 02 Nights premium stay at the finest handpicked jungle resorts', 1),
            _inc_included('Meals: Complete Full Board plan including 02 Breakfasts, 02 Lunches, and 02 multi-cuisine Dinners', 2),
            _inc_included('Transfers & Sightseeing: All intercity transfers in a dedicated, premium air-conditioned luxury vehicle', 3),
            _inc_included('Exclusive Experiences: Curated deep-woods core zone safari with professional naturalists', 4),
            _inc_included('Assistance: 24/7 dedicated remote concierge tracking and operational security backup', 5),
            _inc_included('Taxes & Amenities: All internal state road taxes, parking permits, resort service charges, and welcome amenities kit', 6),
            _inc_excluded('Commercial domestic flights or express train ticketing to departure hubs', 7),
            _inc_excluded('Individual camera permissions, specialized video gear tags, or park entrance fees', 8),
            _inc_excluded('Personal discretionary items such as laundry, phone tabs, premium alcoholic beverages, and staff tips', 9),
            _inc_excluded('Medical or evacuation coverage premiums', 10),
        ],
    )
    return package, itinerary

def build_ka_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-011'
    tour_code = 'TRAGUIN-KA-011'
    title = 'Mangalore Udupi Coastal Flavors Premium Vacation'
    duration = '03 Nights / 04 Days'
    slug = 'ka-011-mangalore-udupi-coastal-flavors-premium-vacation'
    itin_slug = 'ka-011-mangalore-udupi-coastal-flavors-premium-vacation-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Beach & Culinary Luxury', 2),
            _ph('Destinations: Mangalore • Udupi • Malpe • Kapu', 3),
            _ph('Ideal for: Family / Food Connoisseurs', 4),
            _ph('Best season: October to March', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Coastal Culinary FIT Vacation', 7),
            _ph('Vehicle: Private Luxury Air-Conditioned SUV / Sedan', 8),
            _ph('Meal Plan: Continental Breakfasts & Curated Local Fine-Dining Highlights', 9),
            _ph('Route Map: Mangalore Airport Arrival → Udupi Heritage Route → Malpe Coastline → Kapu Beach → Mangalore Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with finest oceanfront villas, authentic food trails, and custom pre-arranged VIP passes', 11),
            _ph('Shopping: Mangalore Cashew Houses, Udupi Spice Bazaars, and local Karavali handicrafts', 12),
            _ph('Important: Check-in 14:00 hrs; cotton resort wear and sunscreen recommended; vehicle dedicated for itinerary route', 13),
        ],
        moods=['Beach', 'Food', 'Culture'],
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
        tagline='Mangalore Udupi Coastal Flavors Premium Vacation • 03 Nights / 04 Days',
        overview=(
            "Step into an extraordinary world where golden sands meet the legendary aromatic kitchens of Karavali. This premium customized getaway, meticulously crafted by TRAGUIN, invites you on a sensory exploration of coastal Karnataka. From the soul-stirring rhythmic tides of Malpe Beach to the deep legacy of Udupi's spice routes, enjoy breathtaking landscapes and premium stays that cultivate unforgettable memories.\n\nThe pristine coastline of Karnataka offers an exquisite mix of pristine blue beaches, rich spiritual heritage, and unparalleled gastronomic heritage, making it a highly searched landmark for an authentic Karnataka Family Tour or a blissful Karnataka Honeymoon Package.\n\nTRAGUIN Curated Touch: This Luxury Karnataka Holiday includes VIP temple entries, an exclusive traditional boat ride to St. Mary's Island, curated interactions with local culinary master chefs, and 24/7 dedicated local assistance.\n\nWhy Visit Coastal Karnataka: Famous attractions like the ancient Sri Krishna Matha in Udupi, the unique hexagonal basalt structures of St. Mary's Island, and the iconic colonial-era lighthouse at Kapu Beach make it a goldmine for popular Instagram locations."
        ),
        seo_title='KA-011 | Mangalore Udupi Coastal Flavors Premium Vacation | TRAGUIN',
        seo_description="Premium 03 Nights / 04 Days coastal culinary package (KA-011 / TRAGUIN-KA-011): Mangalore culinary walk, Sri Krishna Temple, St. Mary's Island cruise, Malpe Beach, and 4-tier beach resort accommodation.",
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Mangalore Culinary Walk & Kapu Beach Lighthouse Exploration', 1),
            _ih('Sri Krishna Temple, Hasta Shilpa Heritage Village & Maple Marina', 2),
            _ih("St. Mary's Island Private Cruise & Malpe Floating Bridge Walk", 3),
            _ih('St. Aloysius Chapel & Mangalore Local Spice Markets', 4),
            _ih('TRAGUIN Signature Experience: Custom pre-arranged VIP passes and private scenic viewing decks', 5),
        ],
        days=[
            _day(
            1,
            'Mangalore to Udupi',
            (
                'Arrive at Mangalore International Airport to receive a warm, traditional welcome arranged by your dedicated TRAGUIN holiday consultant. Board your private luxury vehicle and proceed directly for an elite food tour of Mangalore, tasting legendary Mangalorean buns and ghee roast delicacies. Afterwards, drive through scenic coastal roads to Udupi. Check into your premium handpicked luxury resort. As evening falls, visit the majestic Kapu Beach, ascending its historic 1901 colonial lighthouse for a jaw-dropping view of the sun melting into the Arabian Sea.'
            ),
            [
                'Sightseeing Included: Mangalore Culinary Walk, Kapu Beach Lighthouse Exploration',
                'Evening Experience: Private seaside tea service with local snacks, organized exclusively by TRAGUIN',
                'Overnight Stay: Handpicked Luxury Beach Resort, Udupi / Malpe',
                'Meals Included: Welcome High Tea & Curated Coastal Dinner'
            ],
            ),
            _day(
            2,
            'Udupi Cultural & Culinary Trail',
            (
                'Awake to the soothing symphony of the ocean waves. Today, experience a deeply immersive journey through the heart of Udupi sightseeing. Experience a VIP morning walkthrough of the iconic Sri Krishna Matha temple, admiring the intricate silver-plated window architecture. Following this spiritual awakening, delve into an exclusive heritage experience at the Hasta Shilpa Heritage Village, a stunning open-air museum displaying authentic restored traditional houses. For lunch, indulge in a luxurious multi-course traditional vegetarian feast served on pristine banana leaves.'
            ),
            [
                'Sightseeing Included: Sri Krishna Temple, Hasta Shilpa Heritage Village, Maple Marina',
                'Photography Points: The beautifully carved wooden structures of Hasta Shilpa and the serene temple ponds',
                'Overnight Stay: Handpicked Luxury Beach Resort, Udupi / Malpe',
                'Meals Included: Gourmet Breakfast & Traditional Satvik Lunch'
            ],
            ),
            _day(
            3,
            "Malpe Beach & St. Mary's Island",
            (
                "Embark on an exhilarating day focused on the region's most magnificent natural wonder. Board a private speed boat from Malpe Beach over to St. Mary's Island. Discover a geographical masterpiece featuring striking, unique vertical hexagonal basalt rock formations created by prehistoric volcanic activity millions of years ago. Spend your morning walking along the shell-filled crystal beaches. Return to the mainland for a late afternoon luxury lunch focusing on the fresh, iconic catches of Karavali, combined with rich coconut milk and signature spices."
            ),
            [
                "Sightseeing Included: St. Mary's Island Private Cruise, Malpe Floating Bridge Walk",
                'Optional Activities: Parasailing or a relaxing therapeutic massage at an elite seaside Ayurvedic center',
                'Overnight Stay: Premium Oceanfront Villa / Luxury Resort, Malpe',
                'Meals Included: Breakfast & Seafood Special Dinner'
            ],
            ),
            _day(
            4,
            'Mangalore Departure',
            (
                'Savor a luxurious slow breakfast overlooking the azure horizon. Check out from your premium stay and transfer back towards Mangalore. Stop at the ancient Aloysius Chapel to witness breathtaking Italian-style frescoes that rival European architectural gems. Enjoy some last-minute boutique shopping for premium quality local cashews and authentic spices before a smooth private drop-off at Mangalore International Airport for your flight home.'
            ),
            [
                'Sightseeing Included: St. Aloysius Chapel, Mangalore Local Spice Markets',
                'Transfers Included: Private Airport Drop-off',
                'Meals Included: Full Buffet Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('Paradise Isle Beach Resort, Malpe', 'Malpe', '03 Nights', 'Deluxe', 'Ocean View Room', 'Breakfast & Dinner', 4, 1),
            _hotel('Fortune Inn Valley View, Manipal', 'Manipal', '03 Nights', 'Premium', 'Club Luxury Room', 'Breakfast & Dinner', 5, 2),
            _hotel('Sai Radha Heritage, Kapu Coast', 'Kapu', '03 Nights', 'Luxury', 'Premium Traditional Villa', 'Breakfast & Dinner', 5, 3),
            _hotel('Country Inn & Suites by Radisson, Manipal', 'Manipal', '03 Nights', 'Ultra Luxury', 'Executive Luxury Suite', 'Breakfast & Dinner', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights elite stay at top-tier handpicked hotels or beach resorts', 1),
            _inc_included('Meals: Daily breakfasts alongside specifically curated fine dining traditional lunches and dinners', 2),
            _inc_included('Transfers & Sightseeing: Chauffeur-driven air-conditioned private luxury vehicle for entire tour', 3),
            _inc_included('Assistance & Taxes: All parking, state taxes, driver charges, and 24/7 priority remote concierge assistance', 4),
            _inc_included('Welcome Amenities: Cold-pressed signature welcome juices, refreshing wet towels, and high-grade travel kits', 5),
            _inc_included("Complimentary Experiences: Exclusive boat cruise tickets to St. Mary's Island and special VIP entry line permits", 6),
            _inc_included('TRAGUIN Support: Uncompromised safety and on-call operations management throughout the trip', 7),
            _inc_excluded('Airfare or interstate train ticketing charges to Mangalore', 8),
            _inc_excluded('Personal nature services including laundry, telephone orders, and minibar expenses', 9),
            _inc_excluded('Individual water sports tickets, camera fees, or optional adventure entry costs', 10),
            _inc_excluded('Travel health insurance premium packages', 11),
        ],
    )
    return package, itinerary

def build_ka_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-012'
    tour_code = 'TRAGUIN-KA-012'
    title = 'Dandeli Water Sports Adventure Experience'
    duration = '03 Nights / 04 Days'
    slug = 'ka-012-dandeli-water-sports-adventure-experience'
    itin_slug = 'ka-012-dandeli-water-sports-adventure-experience-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Adventure / Water Sports', 2),
            _ph('Destinations: Dandeli • Kali River • Syntheri Rocks', 3),
            _ph('Ideal for: Adventure Enthusiasts & Families', 4),
            _ph('Best season: October to May', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Adventure Luxury FIT Getaway', 7),
            _ph('Vehicle: Air-Conditioned Private Luxury Innova Crysta / Premium SUV', 8),
            _ph('Meal Plan: All Meals Included (Jungle Resort Buffet Breakfast, Lunch, High Tea & Dinner)', 9),
            _ph('Route Map: Hubli/Goa Arrival → Dandeli Wilderness → Exploration Spots → Departure Hubli/Goa', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with high-end safety protocols, fast-track activity lines, and premium equipment', 11),
            _ph('Shopping: Pure Forest Honey and Handcrafted Artifacts — bamboo carvings, local herbs, and custom wood souvenirs', 12),
            _ph('Important: Water sports subject to river levels; pack quick-dry clothing and sturdy shoes; book rafting early', 13),
        ],
        moods=['Adventure', 'Nature', 'Wildlife'],
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
        tagline='Dandeli Water Sports Adventure Experience • 03 Nights / 04 Days',
        overview=(
            'Prepare yourself for an adrenaline-fueled luxury escape into the wild heart of Southern India. This signature holiday itinerary, intricately planned by TRAGUIN, offers an unrivaled mixture of raw thrill and refined comfort. Experience high-octane river rafting, zip-lining across dramatic jungle canopies, and relaxing walks alongside breathtaking landscapes, creating unforgettable memories for your family.\n\nAs one of the highest-rated segments under our premium TRAGUIN Karnataka Packages, the dense jungle territories of Dandeli present the perfect setting for a high-end Karnataka Adventure holiday. Recognized globally for its iconic attractions along the gushing waters of the Kali River, this region is a magnet for those looking for a thrill-packed Karnataka Family Tour or an exclusive nature retreat.\n\nTRAGUIN Curated Touch: Includes VIP fast-track access to white-water river activities, certified professional adventure instructors, premium handpicked hotels hidden in deep forests, and elite round-the-clock safety companion coverage.\n\nWhy Visit Dandeli: The Best Time to Visit Karnataka for water sports spans from autumn to early summer, when river rapids match global standards, granting access to rare bird watching trails and secret limestone cave pathways.'
        ),
        seo_title='KA-012 | Dandeli Water Sports Adventure Experience | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Dandeli adventure package (KA-012 / TRAGUIN-KA-012): Kali River white-water rafting, Syntheri Rocks, Crocodile Park, jungle jeep safari, and 4-tier forest resort accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Western Ghats Panoramic Drive & Forest Nature Walk', 1),
            _ih('Kali River Rapids & Water Sports Base Station', 2),
            _ih('Syntheri Rocks Monolith, Crocodile Park & Jungle Jeep Safari', 3),
            _ih('TRAGUIN Signature Experience: Fast-track activity lines and premium international-grade adventure gear', 4),
        ],
        days=[
            _day(
            1,
            'Arrival & Jungle Immersion',
            (
                'Arrive at Hubli or Goa Airport where your dedicated TRAGUIN driver and tour guide welcome you warmly. Board your private luxury vehicle and enjoy a highly scenic route climbing through the breathtaking Western Ghats to reach your handpicked luxury jungle resort in Dandeli. After a seamless private check-in, relax in your premium luxury villa. In the late afternoon, enjoy an introductory guided nature trek around the forest loops to spot unique regional flora and wildlife.'
            ),
            [
                'Sightseeing Included: Western Ghats Panoramic Drive, Forest Nature Walk',
                'Evening Experience: Gather around a cozy private bonfire accompanied by premium live acoustic melodies',
                'Overnight Stay: Handpicked Luxury Jungle Resort, Dandeli',
                'Meals Included: Welcome Drinks, Traditional Lunch & Buffet Dinner'
            ],
            ),
            _day(
            2,
            'Kali River Adventure',
            (
                'Fuel up with a rich buffet breakfast before heading to the roaring Kali River for an unforgettable water sports experience. Guided by certified international instructors, take on thrilling Grade-2 and Grade-3 white-water rafting runs. After a gourmet riverside lunch, dive back into the excitement with open-water swimming, river kayaking, and a thrilling zip-line crossing that finishes directly in the cool river waters.'
            ),
            [
                'Sightseeing Included: Kali River Rapids, Water Sports Base Station',
                'Optional Activities: High-altitude coracle boat rides or zorbing ball runs on the river',
                'Photography Points: Capture incredible active shots mid-rafting and sweeping views from the riverbanks',
                'Overnight Stay: Handpicked Luxury Jungle Resort, Dandeli',
                'Meals Included: Breakfast, Riverside Lunch & Dinner'
            ],
            ),
            _day(
            3,
            'Mountain Geology & Coracle Safari',
            (
                'Today introduces the scenic marvels of your Luxury Karnataka Holiday. Journey deep into the Joida forest areas to visit the magnificent Syntheri Rocks, a stunning 300-foot monolithic granite structure sculpted over centuries by the Kaneri River. After taking in this majestic sight, visit the nearby Crocodile Park for a safe, guided look at these ancient river predators. Spend your final evening enjoying a relaxing open-jeep safari through the buffer zones of the Dandeli Wildlife Sanctuary.'
            ),
            [
                'Sightseeing Included: Syntheri Rocks Monolith, Crocodile Park, Jungle Jeep Safari',
                'Immersive Experiences: Educational bird-watching trek to observe the colorful Malabar Pied Hornbills',
                'Overnight Stay: Handpicked Luxury Jungle Resort, Dandeli',
                'Meals Included: Breakfast, Jungle Buffet Lunch & Farewell Barbecue Dinner'
            ],
            ),
            _day(
            4,
            'Jungle Farewell & Departure',
            (
                "Start your morning with a calming sunrise yoga session or a quiet stroll along the resort's private streams. Enjoy a final premium breakfast spread at the resort before checking out. Your private chauffeur-driven vehicle will arrive to transfer you comfortably back to Hubli or Goa Airport for your return flight home. Your premium adventure crafted by TRAGUIN finishes here, leaving you with incredible stories to share."
            ),
            [
                'Transfers Included: Private Airport Drop-off',
                'Meals Included: Full Breakfast Spread'
            ],
            ),
        ],
        hotels=[
            _hotel('Dandeli Kingfisher Jungle Resort', 'Dandeli', '03 Nights', 'Deluxe', 'Deluxe Cottage', 'All Meals Included (APAI)', 4, 1),
            _hotel('Regenta Resort Dandeli', 'Dandeli', '03 Nights', 'Premium', 'Premium Forest View Room', 'All Meals Included (APAI)', 5, 2),
            _hotel('Bison River Resort', 'Dandeli', '03 Nights', 'Luxury', 'Luxury Waterfront Cottage', 'All Meals Included (APAI)', 5, 3),
            _hotel('Eka Resorts / Magenta Resort Wilderness', 'Dandeli', '03 Nights', 'Ultra Luxury', 'Ultra-Luxury Private Jacuzzi Villa', 'All Meals & Barbecue Box', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at premium handpicked jungle resorts with forest views', 1),
            _inc_included('Meals: All meals included—Daily Breakfast, Lunch, Evening Snacks & Gourmet Dinners', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven private luxury Innova Crysta throughout the journey', 3),
            _inc_included('TRAGUIN Support: 24/7 internal concierge line with a dedicated senior travel planner handler', 4),
            _inc_included('Adventure Gear: Premium international-grade life jackets, helmets, and certified instructor fees', 5),
            _inc_included('Complimentary Experiences: Private open-jeep wildlife safari and a special farewell pool-side barbecue evening', 6),
            _inc_excluded('Flights, train fares, or state transit visa taxes', 7),
            _inc_excluded('Video camera entry permits at wildlife reserves', 8),
            _inc_excluded('Personal expenses such as laundry services, phone calls, or alcoholic drinks', 9),
            _inc_excluded('Optional extreme water activities not mentioned in the inclusions', 10),
        ],
    )
    return package, itinerary

def build_ka_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-013'
    tour_code = 'TRAGUIN-KA-013'
    title = 'Evolve Back Coorg Luxury Stay Experience'
    duration = '03 Nights / 04 Days'
    slug = 'ka-013-evolve-back-coorg-luxury-stay-experience'
    itin_slug = 'ka-013-evolve-back-coorg-luxury-stay-experience-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Luxury Experiential Stay', 2),
            _ph('Destinations: Coorg (Chikkana Halli Estate)', 3),
            _ph('Ideal for: Couples, Families & Nature Connoisseurs', 4),
            _ph('Best season: October to May', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Ultra-Luxury Experiential Stay (FIT)', 7),
            _ph('Vehicle: Private Air-Conditioned Luxury Toyota Innova Crysta / Premium Chauffeur Driven Sedan', 8),
            _ph('Meal Plan: Gourmet Breakfast & Dinners at Specialty Dining Venues', 9),
            _ph('Route Map: Bangalore / Bangalore Airport Arrival → Scenic Drive to Coorg Estate → Immersive Plantation Experience → Bangalore Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with elite local naturalists and premium handpicked villas with private plunge pools', 11),
            _ph('Shopping: Estate Fresh Goods — Arabica and Robusta coffee, cardamom, pepper, organic honey; Tibetan Crafts at Bylakuppe markets', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; light layers recommended; book Evolve Back villas 45–60 days in advance', 13),
        ],
        moods=['Luxury', 'Nature', 'Wellness'],
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
        tagline='Evolve Back Coorg Luxury Stay Experience • 03 Nights / 04 Days',
        overview=(
            'Step into a realm where time slows to the rhythm of a bygone era. Curated with perfection by TRAGUIN, this ultra-luxury retreat invites you to experience the magnificent Luxury Karnataka Holiday format at Evolve Back, Coorg (formerly Orange County). Surrounded by a historic 300-acre working coffee and spice plantation, you will be cocooned in Kodava-styled architecture, treated to premium stays, and left with unforgettable memories of breathtaking landscapes and authentic heritage.\n\nCoorg, famously heralded as the Scotland of India, features rolling green ridges, spectacular misty canopies, and historic plantations, making it a stellar highlight for a premium Karnataka Family Tour or an intimate Karnataka Honeymoon Package. Our custom TRAGUIN Karnataka Packages focus deeply on immersive experiences rather than standard point-to-point transfers.\n\nTRAGUIN Curated Touch: This is an exclusive, zero-fatigue high-end getaway with private plantation trail walks, custom coffee-blending workshops, guided bird-watching sessions, and private plunge pool relaxation options.\n\nWhy Visit Evolve Back Coorg: From exploring Dubare Elephant Camp and the golden Namdroling Monastery to capturing popular Instagram locations within lush spice estates, this premium escape encapsulates the absolute finest of Karnataka Sightseeing between October and May.'
        ),
        seo_title='KA-013 | Evolve Back Coorg Luxury Stay Experience | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Evolve Back Coorg package (KA-013 / TRAGUIN-KA-013): Plantation walk, coffee cupping, Namdroling Golden Temple, Dubare Eco-Zone, and 3-tier luxury villa accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Guided Estate Plantation Walk, Bird Watching & Cultural Pavilion', 1),
            _ih('Namdroling Golden Temple, Dubare Eco-Zone & Local Souvenir Avenue', 2),
            _ih('TRAGUIN Signature Experience: Elite naturalists and premium villas with private plunge pools', 3),
            _ih('Premium Handpicked Hotels: Evolve Back Coorg luxury villa options', 4),
        ],
        days=[
            _day(
            1,
            'Bangalore to Coorg',
            (
                'Arrive at Bangalore International Airport or your residence where a premium TRAGUIN private luxury vehicle awaits you. Leave the city traffic behind as you cruise along high-quality highways towards the lush hills of Western Ghats. Watch the landscape transform into dense woods and aromatic plantations. Arrive at the legendary Evolve Back, Coorg, where you are greeted with a personalized traditional welcome drink made from estate-fresh ingredients. Check into your ultra-luxury private villa and unwind amidst scenic beauty.'
            ),
            [
                'Arrival Experience: Seamless transfer, priority villa check-in, and welcome kit',
                'Evening Experience: Sip on fine estate-brewed coffee while overlooking the infinity pool bordering the Cauvery river',
                'Overnight Stay: Evolve Back Coorg (Private Pool Villa / Lily Pool Villa)',
                'Meals Included: Welcome Amenity & Gourmet Dinner'
            ],
            ),
            _day(
            2,
            'Immersive Plantation Experience',
            (
                "Begin your day with a guided bird-watching walk around the plantation lake, spotting endemic avian species. After a sumptuous breakfast, join the expert naturalist for the Worker's Trail—an exclusive experience where you can walk through coffee and spice fields, learning the art of cultivating cardamom, pepper, and Arabica beans. In the afternoon, partake in a curated coffee-cupping session to blend your own souvenir package. Conclude your day with a traditional cultural performance inside the resort's open pavilion."
            ),
            [
                'Sightseeing Included: Guided Estate Plantation Walk, Bird Watching, Cultural Pavilion',
                'Photography Points: The tranquil lily pools, mist over the Cauvery river bank, and vibrant spice canopies',
                'Overnight Stay: Evolve Back Coorg (Private Pool Villa / Lily Pool Villa)',
                'Meals Included: Gourmet Breakfast & Plantation-Themed Dinner'
            ],
            ),
            _day(
            3,
            'Coorg Iconic Attractions',
            (
                'After breakfast, take a premium excursion to visit the magnificent Namdroling Monastery (Golden Temple) in Bylakuppe, one of the largest Tibetan settlements in India. Marvel at the majestic 40-foot gold-plated Buddha statues and soak in the meditative ambiance. Later, enjoy a short visit to the Dubare Elephant Camp ecosystem to learn about elephant conservation. Return to your resort by afternoon to enjoy your private plunge pool and indulge in a rejuvenating Ayurvedic spa therapy.'
            ),
            [
                'Sightseeing Included: Namdroling Golden Temple, Dubare Eco-Zone, Local Souvenir Avenue',
                "Optional Activities: Book a private dining experience 'By the Lake' or an inside-villa fine culinary layout",
                'Overnight Stay: Evolve Back Coorg (Private Pool Villa / Lily Pool Villa)',
                'Meals Included: Full Buffet Breakfast & Farewell Specialty Dinner'
            ],
            ),
            _day(
            4,
            'Coorg to Bangalore Departure',
            (
                'Savor a final slow breakfast surrounded by nature. Take a casual stroll across the manicured lawns before completing check-out. Your private luxury vehicle will transport you comfortably back to Bangalore International Airport or your preferred destination, concluding your ultra-luxury escape with gorgeous memories.'
            ),
            [
                'Transfers Included: Private Chauffeur Drop-off to Bangalore',
                'Meals Included: Gourmet Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('Evolve Back, Coorg', 'Coorg', '03 Nights', 'Premium', 'Heritage Pool Villa', 'MAPAI (Breakfast + Dinner)', 5, 1),
            _hotel('Evolve Back, Coorg', 'Coorg', '03 Nights', 'Luxury', 'Lily Pool Cottage', 'MAPAI (Breakfast + Dinner)', 5, 2),
            _hotel('Evolve Back, Coorg', 'Coorg', '03 Nights', 'Ultra Luxury', 'Lily Pool Villa (Exclusive Plunge Pool)', 'MAPAI + High Tea Included', 5, 3),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at premium luxury villas at Evolve Back Coorg', 1),
            _inc_included('Meals: Daily gourmet breakfasts and dinners curated across fine dining venues', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven air-conditioned Luxury Innova Crysta for all transfers and tourist places', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated real-time holiday concierge support', 4),
            _inc_included('Complimentary Experiences: Guided Plantation walks, coffee cupping workshops, and resort-organized cultural events', 5),
            _inc_included('Taxes: All applicable luxury resort service charges and local taxes', 6),
            _inc_excluded('Airfare or rail connections to Bangalore', 7),
            _inc_excluded('Individual monument entry fees, camera tickets, or safari boat rides', 8),
            _inc_excluded('Personal premium expenses such as specialty laundry, boutique purchases, or liquor', 9),
            _inc_excluded('Premium Ayurvedic spa therapies or custom private dinner layouts', 10),
        ],
    )
    return package, itinerary

def build_ka_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-014'
    tour_code = 'TRAGUIN-KA-014'
    title = 'Kemmangundi Hills & Kudremukh Trek Escape'
    duration = '04 Nights / 05 Days'
    slug = 'ka-014-kemmangundi-hills-kudremukh-trek-escape'
    itin_slug = 'ka-014-kemmangundi-hills-kudremukh-trek-escape-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Leisure & Adventure', 2),
            _ph('Destinations: Chikkamagaluru • Kemmangundi • Kudremukh', 3),
            _ph('Ideal for: Nature Lovers, Couples & Trekkers', 4),
            _ph('Best season: September to March', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Adventure Luxury FIT Getaway', 7),
            _ph('Vehicle: Private Air-Conditioned Premium SUV (Innova Crysta) throughout the tour', 8),
            _ph('Meal Plan: Modified American Plan (Buffet Breakfast & Specially Prepared Dinners at all resorts)', 9),
            _ph('Route Map: Bengaluru Arrival → Chikkamagaluru → Kemmangundi Hills → Kudremukh National Park → Bengaluru Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with skip-the-line permit clearances and custom-planned nutrition menus for trekking days', 11),
            _ph('Shopping: Premium Estate Coffee, sandalwood carvings, rosewood artifacts, and Channapatna toys', 12),
            _ph('Important: Kudremukh is plastic-free; post-monsoon months offer best views; forest permits highly limited — book early', 13),
        ],
        moods=['Adventure', 'Nature', 'Trekking'],
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
        tagline='Kemmangundi Hills & Kudremukh Trek Escape • 04 Nights / 05 Days',
        overview=(
            "Welcome to the rolling, mist-kissed cloud forests of the Western Ghats. This premium luxury vacation crafted thoughtfully by TRAGUIN unrolls a perfect blend of high-end leisure and exhilarating adventure. Journey deep into the coffee heartlands of Chikkamagaluru, explore the manicured royal gardens of Kemmangundi, and challenge yourself across the iconic spine of Kudremukh Peak. Experience flawless execution, handpicked stays, and unparalleled scenic beauty curated exclusively for you.\n\nThe misty highlands of Chikkamagaluru, Kemmangundi, and Kudremukh present one of the most breathtaking landscapes in South India, making it a highly searched target for an elite Karnataka Family Tour or a romantic Karnataka Honeymoon Package. Known for its endless fields of high-grade Arabica coffee plantations, towering waterfalls, and incredible biodiversity, this region promises unforgettable memories.\n\nTRAGUIN Curated Touch: This Luxury Karnataka Holiday includes a private estate coffee tasting session, specialized forest department certified trekking guides for Kudremukh National Park, and access to exclusive viewpoints away from standard tourist tracks.\n\nWhy Visit the Western Ghats: From capturing the perfect landscape shot at Z Point during sunrise to embarking on the legendary Kudremukh Trekking path shaped like a horse's face, this itinerary covers all the top tourist places in Karnataka's hill country."
        ),
        seo_title='KA-014 | Kemmangundi Hills & Kudremukh Trek Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Western Ghats trek package (KA-014 / TRAGUIN-KA-014): Kemmangundi Z Point, Mullayanagiri Peak, Kudremukh Trek, and 4-tier eco-lodge accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Scenic Western Ghats highway transit & Private estate walk', 1),
            _ih('Rose Garden, Raj Bhavan Viewpoint, Z Point Trek & Hebbe Falls', 2),
            _ih('Mullayanagiri Viewpoint, Seethalayanagiri Temple & Kudremukh Landscape transit', 3),
            _ih('The Epic Kudremukh Peak Trek (~18 km, Moderate difficulty)', 4),
            _ih('TRAGUIN Signature Experience: Skip-the-line permit clearances and certified trekking guides', 5),
        ],
        days=[
            _day(
            1,
            'Bengaluru to Chikkamagaluru',
            (
                'Arrive at Bengaluru International Airport or your preferred location where a professional TRAGUIN chauffeur welcomes you in a premium luxury vehicle. Leave the bustling metro behind as you drive toward the lush green valleys of Chikkamagaluru. Arrive by afternoon and check into your handpicked luxury coffee resort. Spend your evening taking a peaceful stroll through the winding coffee estate paths while the birds echo through the dense canopy.'
            ),
            [
                'Sightseeing Included: Scenic Western Ghats highway transit, Private estate walk',
                'Evening Experience: Curated high-tea served with freshly brewed gourmet estate single-origin coffee',
                'Overnight Stay: Premium Luxury Resort nestled in Chikkamagaluru',
                'Meals Included: Welcome Amenity & Multi-cuisine Buffet Dinner'
            ],
            ),
            _day(
            2,
            'Chikkamagaluru to Kemmangundi',
            (
                "After a lavish breakfast, embark on a scenic drive to Kemmangundi Hills, historically preferred as the summer retreat of the Mysore Kingdom's Royalty. Explore the beautifully manicured Rose Gardens and proceed on an exciting short jeep ride to Z Point for a spectacular view of the surrounding valleys. Later, experience the raw beauty of Hebbe Falls or Kalhatti Falls, where water rushes through sacred rocks, offering deep emotional connection with untouched nature."
            ),
            [
                'Karnataka Sightseeing: Rose Garden, Raj Bhavan Viewpoint, Z Point Trek, Hebbe Falls',
                'Photography Points: Endless green horizons and misty valley ridges from the tip of Z Point',
                'Overnight Stay: Handpicked Luxury Resort, Chikkamagaluru / Kemmangundi area',
                'Meals Included: Full Buffet Breakfast & Dinner'
            ],
            ),
            _day(
            3,
            'Chikkamagaluru Highlights to Kudremukh',
            (
                'Wake up early for a spectacular morning drive up to Mullayanagiri Peak, the highest point in Karnataka. Witness the clouds floating below your feet as the sun rises over the valleys. Return to the resort for breakfast, then pack your bags and head toward the rolling shola grasslands of Kudremukh National Park. Check in to your premium eco-luxury wilderness lodge, and participate in a thorough briefing session by our trek specialist to prepare for the grand expedition tomorrow.'
            ),
            [
                'Sightseeing Included: Mullayanagiri Viewpoint, Seethalayanagiri Temple, Kudremukh Landscape transit',
                'Optional Activities: Gentle evening meditation sessions overlooking the quiet flowing mountain streams',
                'Overnight Stay: Premium Luxury Wilderness Eco-Lodge, Kudremukh',
                'Meals Included: Breakfast & Carbohydrate-rich Energy Dinner'
            ],
            ),
            _day(
            4,
            'The Epic Kudremukh Peak Trek',
            (
                'Today marks the pinnacle of your Premium Karnataka Experience. Early morning, embark on the legendary Kudremukh Trek accompanied by a certified forest naturalist guide. Walk through a magical tapestry of deep tropical rainforests, pristine river crossings, and sweeping emerald shola hills. Reach the ridge to behold the breathtaking landscapes of the horse-faced peak rising majestically against the blue sky. Feel the profound sense of achievement at the summit before descending gracefully to your luxury lodge for a warm celebratory campfire dinner.'
            ),
            [
                'Trek Distance & Difficulty: ~18 km total (Moderate difficulty), safely managed with regular breaks',
                "Immersive Experiences: Standing amidst moving clouds at the summit of South India's finest ridge trek",
                'Overnight Stay: Premium Luxury Wilderness Eco-Lodge, Kudremukh',
                'Meals Included: Breakfast, Packed Energy Lunch & Festive Campfire Dinner'
            ],
            ),
            _day(
            5,
            'Kudremukh to Bengaluru Departure',
            (
                'Enjoy a relaxed morning breakfast as the mountain mist rolls gently across your resort balcony. Take a last look at the pristine mountains before boarding your premium SUV. Journey comfortably back to Bengaluru, reminiscing about the beautiful sights, deep valleys, and thrilling trails. Your iconic TRAGUIN Karnataka Package concludes as you drop off at the airport or your residence.'
            ),
            [
                'Transfers Included: Private Highway Transfer & Airport/City drop-off',
                'Meals Included: Full Gourmet Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('Gateway Chikkamagaluru - IHCL / Silent Valley Resort', 'Chikkamagaluru / Kudremukh', '04 Nights', 'Deluxe', 'Standard Room / Forest Cottage', 'MAPAI (Breakfast + Dinner)', 4, 1),
            _hotel('The Serai Chikkamagaluru / Upasana Retreat', 'Chikkamagaluru / Kudremukh', '04 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast + Dinner)', 5, 2),
            _hotel('Java Rain Resorts / Trivik Hotels & Resorts', 'Chikkamagaluru / Kudremukh', '04 Nights', 'Luxury', 'Luxury Villa / Oak Suite', 'MAPAI (Breakfast + Dinner)', 5, 3),
            _hotel('Evolve Back, Kabini / Luxury Estate Villa / Flameback Lodges', 'Chikkamagaluru / Kudremukh', '04 Nights', 'Ultra Luxury', 'Luxury Estate Villa', 'All Inclusive Luxury Package', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 04 Nights stay at handpicked premium luxury hotels and nature eco-lodges', 1),
            _inc_included('Meals: Daily premium buffet breakfasts and dinners, plus packed trail lunches during the Kudremukh Trek', 2),
            _inc_included('Transfers & Sightseeing: Private chauffeur-driven air-conditioned Innova Crysta for all transfers and tourist places', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated guest relations concierge assistance', 4),
            _inc_included('Trek Essentials: Wildlife forest department entry permissions, permits, and professional certified local companion guides', 5),
            _inc_included('Welcome Amenities: Cold-pressed wellness drinks, signature organic coffee gift hamper, and premium travel accessories kit', 6),
            _inc_excluded('Airfare or rail tickets to and from Bengaluru', 7),
            _inc_excluded('Personal expenses such as laundry, phone calls, premium beverages, and tips', 8),
            _inc_excluded('Individual adventure activities or optional tour extensions not mentioned in the itinerary', 9),
            _inc_excluded('Medical/Travel insurance policies', 10),
        ],
    )
    return package, itinerary

def build_ka_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-015'
    tour_code = 'TRAGUIN-KA-015'
    title = 'Kukke Subrahmanya • Dharmasthala • Mangalore'
    duration = '03 Nights / 04 Days'
    slug = 'ka-015-kukke-subrahmanya-dharmasthala-mangalore'
    itin_slug = 'ka-015-kukke-subrahmanya-dharmasthala-mangalore-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Pilgrimage / Spiritual Luxury', 2),
            _ph('Destinations: Mangalore • Kukke Subrahmanya • Dharmasthala', 3),
            _ph('Ideal for: Families, Seniors & Devotees', 4),
            _ph('Best season: October to March', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Luxury Pilgrimage FIT Tour', 7),
            _ph('Vehicle: Private Air-Conditioned Luxury Innova Crysta / Chauffeur-driven Premium Sedan', 8),
            _ph('Meal Plan: Modified American Plan (Gourmet Breakfasts & Premium Dinners)', 9),
            _ph('Route Map: Mangalore Arrival → Kukke Subrahmanya → Dharmasthala → Mangalore Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with hassle-free priority access, senior-citizen friendly pathways, and elite handpicked hotels', 11),
            _ph('Shopping: Premium Mangalore Cashew nuts, organic spices, sandalwood artifacts, and premium silk dhotis', 12),
            _ph('Important: Traditional clothing required at temples; check-in 14:00 hrs; taste Neer Dosa and local filter coffee', 13),
        ],
        moods=['Pilgrimage', 'Spiritual', 'Culture'],
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
        tagline='Kukke Subrahmanya • Dharmasthala • Mangalore • 03 Nights / 04 Days',
        overview=(
            'Embark on a sacred journey into the spiritual heartland of Western Ghats. This premium divine package meticulously curated by TRAGUIN merges high-end luxury hospitality with seamless, peaceful darshans. From the ancient sarpa-dosha-redeeming shrines of Kukke Subrahmanya to the benevolent heritage of Lord Manjunatha Swamy at Dharmasthala, your family is assured premium stays, comfortable drives, and unforgettable memories filled with divine grace.\n\nFor devotees seeking the Best Karnataka Tour Package or a dedicated Karnataka Family Tour, the sacred belt of Coastal Karnataka presents an unparalleled combination of deep spiritual serenity and breathtaking landscapes. Thousands of travelers seek out a Premium Karnataka Experience each year, making the temples of Kukke Subrahmanya and Dharmasthala the most searched experiences for families and seniors alike.\n\nTRAGUIN Curated Touch: Includes VIP darshan coordination, handpicked premium hotels closest to the sacred temple gates, zero-hurry custom itineraries, and an expert local driver fluent in regional spiritual rituals.\n\nWhy Visit Sacred Coastal Karnataka: From the scenic beauty of the Netravati river banks to the iconic attractions around Mangalore city, TRAGUIN Karnataka Packages provide handpicked hotels and exclusive experiences that let you completely focus on inner peace and devotion.'
        ),
        seo_title='KA-015 | Kukke Subrahmanya • Dharmasthala • Mangalore | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days pilgrimage package (KA-015 / TRAGUIN-KA-015): Kukke Subrahmanya Temple, Dharmasthala Temple, Ratnagiri Bahubali, Mangalore temples, and 4-tier premium hotel accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Mangalore to Kukke transfer & evening orientation at Kukke Subrahmanya Temple', 1),
            _ih('Kukke Main Darshan, Scenic Western Ghats Drive & Dharmasthala Temple complex', 2),
            _ih('Ratnagiri Bahubali Monolith, Kadri Temple, Mangaladevi Temple & Tannirbhavi Beach', 3),
            _ih('TRAGUIN Signature Experience: Priority access arrangements and senior-citizen friendly pathways', 4),
        ],
        days=[
            _day(
            1,
            'Mangalore Arrival to Kukke Subrahmanya',
            (
                'Arrive at Mangalore International Airport or Railway Station, where your professional TRAGUIN tour chauffeur welcomes you warmly. Board your luxury private vehicle and set off on a remarkably scenic drive toward the pristine village of Kukke Subrahmanya, nestled elegantly under the Kumara Parvatha peaks. Upon arrival, check-in smoothly at your premium hotel. In the evening, visit the grand temple dedicated to Lord Subrahmanya, lord of all serpents. Experience a peaceful orientation walk around the holy Kumardhara River banks.'
            ),
            [
                'Sightseeing Included: Mangalore to Kukke transfer, evening orientation visit to Kukke Subrahmanya Temple',
                'Evening Experience: Participate in the divine evening Mangala Arati amidst beautiful chanting',
                'Overnight Stay: Premium Handpicked Hotel, Kukke Subrahmanya',
                'Meals Included: Welcome Drink & Premium Dinner'
            ],
            ),
            _day(
            2,
            'Kukke Subrahmanya to Dharmasthala',
            (
                'Wake up early to experience the mystical morning vibes of the hills. After breakfast, enjoy a peaceful, priority Karnataka Sightseeing experience at the main shrine. Later, board your luxury vehicle for a smooth drive to Dharmasthala, the timeless land of charity, justice, and spiritual benevolence. Check into your luxury eco-resort nearby. In the evening, visit the historic Sri Manjunatha Swamy Temple, a unique site where the deity is worshipped by Shaivite priests and managed by Jain Heggade heritage.'
            ),
            [
                'Sightseeing Included: Kukke Main Darshan, Scenic Western Ghats Drive, Dharmasthala Temple complex',
                'Optional Activities: Walk through the historic paths of Netravati River or visit the local heritage chariot museum',
                'Overnight Stay: Premium Luxury Resort, Dharmasthala / Belthangady',
                'Meals Included: Full Breakfast & Dinner'
            ],
            ),
            _day(
            3,
            'Dharmasthala to Mangalore',
            (
                'Following a delicious traditional breakfast, pay a morning visit to the magnificent 39-foot single-rock monolithic statue of Lord Bahubali at Ratnagiri Hill, offering panoramic views of the valleys. Afterwards, drive back comfortably towards Mangalore. Check-in to your premium luxury city hotel. In the afternoon, visit the famous 9th-century Mangaladevi Temple and Kadri Manjunath Temple. Conclude your evening watching a pristine sunset over the golden sand horizons of Tannirbhavi Beach.'
            ),
            [
                'Sightseeing Included: Ratnagiri Bahubali Monolith, Kadri Temple, Mangaladevi Temple, Tannirbhavi Beach',
                'Photography Points: Scenic hill views from Ratnagiri and beach sunset frames',
                'Overnight Stay: Ultra-Luxury Hotel, Mangalore',
                'Meals Included: Full Breakfast & Festive Farewell Dinner'
            ],
            ),
            _day(
            4,
            'Mangalore Local Shopping to Departure',
            (
                "Savor a luxurious morning breakfast at your leisure. Spend a relaxed morning exploring Mangalore's premium local markets for famous regional specialties. Your private luxury vehicle will then arrive to transfer you smoothly to Mangalore Airport or Railway Station. Your unforgettable TRAGUIN Karnataka Package concludes as you head home carrying divine blessings and unforgettable memories."
            ),
            [
                'Transfers Included: Private Airport/Station Luxury Transfer Drop-off',
                'Meals Included: Full Buffet Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('Hotel SLR Grand / Hotel Srigandha Residency / Goldfinch Hotel Mangalore', 'Kukke / Dharmasthala / Mangalore', '03 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1),
            _hotel('The Rock Regency Resort / Muffins Eco Green Resort / Avatar Hotel & Spa', 'Kukke / Dharmasthala / Mangalore', '03 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 5, 2),
            _hotel('Kukke Regency Premium Suites / Guthu Heritage Mansion Resort / Vivanta Mangalore, Old Port Road', 'Kukke / Dharmasthala / Mangalore', '03 Nights', 'Luxury', 'Premium Suite', 'Breakfast & Dinner', 5, 3),
            _hotel('Luxury Villa Club Presidential / The Gateway Hotel (Taj) - Chikmagalur Border / Radisson Blu Mangalore', 'Kukke / Dharmasthala / Mangalore', '03 Nights', 'Ultra Luxury', 'Presidential Suite', 'Breakfast & Dinner', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at handpicked premium luxury properties close to the temples', 1),
            _inc_included('Meals: 03 Multi-cuisine Buffet Breakfasts and 03 curated fine-dining Dinners at the hotels', 2),
            _inc_included('Transfers & Sightseeing: All coordinates via dedicated private Luxury Air-conditioned Innova Crysta with expert driver', 3),
            _inc_included('TRAGUIN Support: 24/7 priority concierge backing and hassle-free token assistance', 4),
            _inc_included('Welcome Amenities: Personalized pilgrimage kits including holy offering items, traditional stoles, and premium bottled mineral water', 5),
            _inc_included('Taxes: All current applicable tourist vehicle taxes, parking fees, and interstate fuel tolls', 6),
            _inc_excluded('Airfare or main interstate rail tickets into Mangalore', 7),
            _inc_excluded('Special individual sevas or personalized ritual offerings inside temples', 8),
            _inc_excluded('Personal items such as laundry, extra beverages, tips, or phone bills', 9),
            _inc_excluded('Travel insurance or emergency medical coverage costs', 10),
        ],
    )
    return package, itinerary

def build_ka_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-016'
    tour_code = 'TRAGUIN-KA-016'
    title = 'Bangalore • Mysore • Coorg Classic'
    duration = '05 Nights / 06 Days'
    slug = 'ka-016-bangalore-mysore-coorg-classic'
    itin_slug = 'ka-016-bangalore-mysore-coorg-classic-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Luxury Family Vacation', 2),
            _ph('Destinations: Bangalore • Mysore • Coorg', 3),
            _ph('Ideal for: Families & Elite Travelers', 4),
            _ph('Best season: October to May', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private Luxury Family FIT Tour', 7),
            _ph('Vehicle: Private Chauffeur-driven Luxury Air-Conditioned Toyota Innova Crysta', 8),
            _ph('Meal Plan: Deluxe Buffet Breakfasts & Handpicked Specialty Dinners Included', 9),
            _ph('Route Map: Bangalore Arrival → Mysore Palaces → Coorg Hills → Bangalore Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with pre-arranged priority entry lines, seasoned drivers, and handpicked boutique properties', 11),
            _ph('Shopping: Mysore Silk sarees, sandalwood carvings, Mysore Pak; Coorg cardamom, pepper, organic chocolates, and Arabica coffee', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; light sweaters for Coorg evenings; reserve spa sessions in advance', 13),
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
        price_note="On Request (Premium Class)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Bangalore • Mysore • Coorg Classic • 05 Nights / 06 Days',
        overview=(
            "Welcome to an extraordinary exploration of Southern royalty, heritage, and mist-kissed hills. This premium luxury vacation itinerary, seamlessly designed by TRAGUIN, treats your family to breathtaking landscapes and majestic royal palaces. From the vibrant cosmopolitan energy of Bangalore to the heritage splendor of Mysore and the verdant coffee estates of Coorg, prepare to cultivate unforgettable memories during an ultra-luxurious, exclusive experience.\n\nKarnataka offers a magical tapestry of heritage, wild nature, and modern luxury, establishing it as one of India's most searched holiday getaways. For families searching for a top-tier Luxury Karnataka Holiday, this customized journey presents elite heritage circuits and breathtaking scenic beauty.\n\nTRAGUIN Curated Touch: This custom-crafted Karnataka Honeymoon Package and Karnataka Family Tour blends private guided palace walks, a personalized coffee estate harvesting masterclass, and ultra-premium stays designed for complete rest and luxury.\n\nWhy Visit Karnataka: Discover Top Tourist Places including the mesmerizing illuminated Mysore Palace, the peaceful golden Namdroling Monastery in Bylakuppe, and the iconic architectural sights of Bangalore during cool winter and spring months when Coorg coffee plantations are alive with fragrance and color."
        ),
        seo_title='KA-016 | Bangalore • Mysore • Coorg Classic | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Karnataka classic package (KA-016 / TRAGUIN-KA-016): Bangalore Palace, Mysore Palace, Namdroling Monastery, Abbey Falls, Dubare Elephant Camp, and 4-tier luxury accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Bangalore Palace, Tipu Sultan's Summer Palace & Cubbon Park drive", 1),
            _ih('Amba Vilas Mysore Palace, Chamundi Hills & Nandi Bull Statue', 2),
            _ih('Namdroling Monastery, Kushalnagar Deer Park & Coorg sightseeing', 3),
            _ih("Abbey Falls, Madikeri Fort, Raja's Seat & Coffee Plantation Tour", 4),
            _ih('Dubare Elephant Camp & Cauvery Riverbank', 5),
            _ih('TRAGUIN Signature Experience: Priority entry lines and royal guided walk inside Mysore Palace', 6),
        ],
        days=[
            _day(
            1,
            'Bangalore Arrival & Sightseeing',
            (
                'Arrive at Bengaluru International Airport where your dedicated TRAGUIN chauffeur welcomes you warmly. Transfer comfortably to your premium luxury hotel for a seamless check-in. In the afternoon, set out for a sophisticated Bangalore Sightseeing tour. Visit the magnificent Bangalore Palace, an architectural marvel modeled after Windsor Castle, and the historic summer house of Tipu Sultan. Later, drive past the majestic Vidhana Soudha, capturing stunning family photographs alongside its grand columns.'
            ),
            [
                "Sightseeing Included: Bangalore Palace, Tipu Sultan's Summer Palace, Cubbon Park drive",
                'Evening Experience: Leisurely stroll around the upscale high-streets of UB City, followed by a curated welcome dinner',
                'Overnight Stay: Premium Luxury Hotel, Bangalore',
                'Meals Included: Welcome Cocktail & Gourmet Dinner'
            ],
            ),
            _day(
            2,
            'Bangalore to Mysore',
            (
                'Following a lavish buffet breakfast, depart along the newly minted expressway towards the royal city of Mysore. Check in to your handpicked heritage palace hotel. In the afternoon, experience an exclusive guided walk through the legendary Mysore Palace, marveling at its ornate rosewood doors, crystal chandeliers, and majestic durbar halls. As evening approaches, watch the palace transform into a golden spectacle under nearly 100,000 glowing lightbulbs.'
            ),
            [
                'Sightseeing Included: Amba Vilas Mysore Palace, Chamundi Hills, Nandi Bull Statue',
                'Photography Points: Golden hour atop Chamundi Hills overlooking the expansive city',
                'Overnight Stay: Handpicked Premium Heritage Hotel, Mysore',
                'Meals Included: Full Breakfast & Palace View Dinner'
            ],
            ),
            _day(
            3,
            'Mysore to Coorg via Bylakuppe',
            (
                'Enjoy an early morning breakfast before driving toward the mist-covered hill station of Coorg. En route, experience a unique cultural excursion in Bylakuppe, the second-largest Tibetan settlement outside Tibet. Visit the breathtaking Namdroling Monastery (Golden Temple), home to towering 40-foot golden Buddha statues. Arrive in Coorg by afternoon and check in to your ultra-luxury wilderness resort, nestled deep within an expansive private coffee estate.'
            ),
            [
                'Sightseeing Included: Namdroling Monastery, Kushalnagar Deer Park',
                'Evening Experience: Indulge in a signature spa therapy or a private bonfire session curated by TRAGUIN holiday experts',
                'Overnight Stay: Ultra-Luxury Rainforest Resort, Coorg',
                'Meals Included: Full Breakfast & Traditional Coorgi Dinner'
            ],
            ),
            _day(
            4,
            'Coorg Immersive Discovery',
            (
                "Wake up to the refreshing scent of fresh coffee beans. Today features an immersive, privately guided walk through a vintage coffee plantation, learning about the journey from bean to cup. Later, explore the top attractions of Coorg, including the tumbling waters of Abbey Falls and the historic Madikeri Fort. End your afternoon at Raja's Seat, a scenic garden where ancient kings watched the sun set over sweeping mist-shrouded valleys."
            ),
            [
                "Sightseeing Included: Abbey Falls, Madikeri Fort, Raja's Seat, Coffee Plantation Tour",
                'Food Suggestions: Savor authentic Pandi Curry or signature bamboo shoot delicacies at handpicked premium bistros',
                'Overnight Stay: Ultra-Luxury Rainforest Resort, Coorg',
                'Meals Included: Gourmet Breakfast & Plantation Dinner'
            ],
            ),
            _day(
            5,
            'Dubare Elephant Camp & Water Sports',
            (
                'After a premium breakfast, visit the famous Dubare Elephant Camp along the banks of the Cauvery River. Participate in an immersive eco-experience, observing elephant bathing routines and enjoying peaceful nature walks. Spend a relaxed afternoon exploring local markets or enjoying the infinity pools and top-tier amenities at your resort.'
            ),
            [
                'Sightseeing Included: Dubare Elephant Camp, Cauvery Riverbank',
                'Optional Activities: Gentle still-water rafting along the river, or a birdwatching trail with a resort naturalist',
                'Overnight Stay: Ultra-Luxury Rainforest Resort, Coorg',
                'Meals Included: Full Buffet Breakfast & Gala Farewell Dinner'
            ],
            ),
            _day(
            6,
            'Coorg to Bangalore Departure',
            (
                "Savor a final breakfast while taking in Coorg's morning mist. Relax on a smooth return drive to Bangalore. Your luxury private vehicle will drop you directly at Bengaluru International Airport for your departing flight. Your premier TRAGUIN Karnataka Package concludes, leaving you with beautiful memories of a premium, perfectly managed vacation."
            ),
            [
                'Transfers Included: Private Luxury Airport Drop-off',
                'Meals Included: Full Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('ITC Gardenia, a Luxury Collection / Radisson Blu Plaza Hotel / Club Mahindra Madikeri', 'Bangalore / Mysore / Coorg', '05 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1),
            _hotel('The Leela Palace Bengaluru / Grand Mercure Mysuru / Amanvana Spa Resort - Coorg', 'Bangalore / Mysore / Coorg', '05 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 5, 2),
            _hotel('Taj West End, Bangalore / The Heritage Club - Seringapatam / Coorg Wilderness Resort', 'Bangalore / Mysore / Coorg', '05 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 3),
            _hotel('Four Seasons Hotel Bengaluru / Evolve Back, Kabini / Mysore / The Tamara Coorg / Evolve Back Coorg', 'Bangalore / Mysore / Coorg', '05 Nights', 'Ultra Luxury', 'Luxury Suite / Villa', 'Breakfast & Dinner', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 05 Nights stay at handpicked premier luxury properties and private heritage villas', 1),
            _inc_included('Meals: 05 Luxury Buffet Breakfasts and 05 curated specialty dinners at the hotels', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven air-conditioned Luxury Innova Crysta for all planned transfers', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated concierge assistance and prioritized local verification', 4),
            _inc_included('Complimentary Experiences: Private coffee plantation tasting masterclass and royal guided walk inside Mysore Palace', 5),
            _inc_included('Welcome Amenities: Personalized travel kit including premium organic refreshments, traditional silk stoles, and fresh mineral water', 6),
            _inc_excluded('Airfare or interstate train tickets to and from Bangalore', 7),
            _inc_excluded('Any monument entry tickets, camera passes, or guide tips not explicitly listed', 8),
            _inc_excluded('Personal expenses such as laundry, telephone calls, mini-bar usage, and premium spa upgrades', 9),
            _inc_excluded('Optional adventure tours or extra vehicle mileage outside scheduled itineraries', 10),
            _inc_excluded('Comprehensive travel or medical emergency insurance', 11),
        ],
    )
    return package, itinerary

def build_ka_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KA-017'
    tour_code = 'TRAGUIN-KA-017'
    title = 'Chikmagalur Coffee Plantation Getaway'
    duration = '03 Nights / 04 Days'
    slug = 'ka-017-chikmagalur-coffee-plantation-getaway'
    itin_slug = 'ka-017-chikmagalur-coffee-plantation-getaway-itinerary'
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
            _ph('State / Country: Karnataka / India | Category: Family Vacation / Luxury', 2),
            _ph('Destinations: Chikmagalur Coffee Plantations', 3),
            _ph('Ideal for: Families, Leisure Travelers', 4),
            _ph('Best season: September to March', 5),
            _ph("Starting price: On Request (Premium Class)", 6),
            _ph('Travel Format: Private FIT Custom Family Tour', 7),
            _ph('Vehicle: Dedicated Luxury AC Innova Crysta / Chauffeur-Driven Sedan', 8),
            _ph('Meal Plan: Modified American Plan (Daily Breakfast & Multi-Cuisine Dinners)', 9),
            _ph('Route Details: Bangalore Arrival → Chikmagalur Hills → Plantation Estate Sightseeing → Mullayanagiri Peak → Bangalore Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with secured premium vehicle handovers, elite entry privileges, and custom culinary requests', 11),
            _ph('Shopping: Artisanal Single-Origin Coffee and Pure Mountain Spices — cardamom, cinnamon, organic honey, and black pepper', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; light sweater for misty evenings; book peak season villas early', 13),
        ],
        moods=['Nature', 'Leisure', 'Family'],
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
        tagline='Chikmagalur Coffee Plantation Getaway • 03 Nights / 04 Days',
        overview=(
            "Escape into the mist-shrouded hills and endless emerald slopes of India's premier coffee country. This meticulously designed luxury itinerary by TRAGUIN invites you and your family to slow down, breathe the crisp mountain air, and settle into a world of sensory luxury. Surrounded by the gentle whispers of the Western Ghats, experience highly curated experiences, gourmet dining, and premier stays where unforgettable memories are waiting to unfold.\n\nChikmagalur, nested securely in the rugged heart of southwestern Karnataka, is the birthplace of coffee in India and stands out as one of the most sought-after spots for a Luxury Karnataka Holiday. Boasting breathtaking landscapes, cascading waterfalls, and sprawling colonial-style estates, it is universally acknowledged as the definitive destination for an upscale Karnataka Family Tour or an intimate Karnataka Honeymoon Package.\n\nTRAGUIN Curated Note: Includes private bean-to-cup coffee estate walk, candlelight family dinner, and premium handpicked boutique resort stays.\n\nWhy Visit Chikmagalur: Famous for Mullayanagiri Peak, Baba Budangiri hills, and the historic temples of Belur and Halebidu, it offers an immersive blend of eco-adventure, ancient culture, and pure relaxation with mist-covered valley viewpoints perfect for your Instagram feed."
        ),
        seo_title='KA-017 | Chikmagalur Coffee Plantation Getaway | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Chikmagalur package (KA-017 / TRAGUIN-KA-017): Coffee plantation trail, Jhari/Hebbe Waterfalls, Mullayanagiri Peak, Belur Chennakeshava Temple, and 4-tier boutique resort accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Scenic Western Ghats Drive & Resort Leisure Walk', 1),
            _ih('Private Coffee Plantation Trail & Jhari/Hebbe Waterfalls', 2),
            _ih('Mullayanagiri Peak, Seethalayanagiri & Belur Chennakeshava Temple', 3),
            _ih('TRAGUIN Signature Experience: Elite entry privileges and custom culinary requests', 4),
        ],
        days=[
            _day(
            1,
            'Bangalore to Chikmagalur',
            (
                'Arrive at Bangalore International Airport or your residence where your professional luxury vehicle and dedicated chauffeur await. Embark on a beautifully scenic drive as you transition away from the urban expanse toward the rolling green vistas of Western Karnataka. En route, stop for a premium traditional South Indian breakfast. Arrive in Chikmagalur by afternoon, passing through roads flanked by dense coffee bushes and tall silver oak trees. Complete a seamless, private check-in at your handpicked luxury estate resort, receiving a signature welcome drink infused with local spices. Spend your evening relaxing on your private deck overlooking the mist-filled valley.'
            ),
            [
                'Sightseeing Included: Scenic Western Ghats Drive, Resort Leisure Walk',
                'Evening Experience: High tea served at a private viewpoint on the estate grounds',
                'Overnight Stay: Ultra-Luxury Boutique Resort, Chikmagalur',
                'Meals Included: Welcome Drink, High Tea & Gourmet Dinner'
            ],
            ),
            _day(
            2,
            'Chikmagalur Estate Exploration',
            (
                'Awake to the invigorating aroma of fresh coffee beans drifting through the mountain mist. After an exquisite buffet breakfast, participate in an exclusive experience: a privately guided plantation walk led by an expert estate naturalist. Trace the historical journey of coffee from its legendary introduction by Baba Budan to modern-day cultivation techniques. Witness the harvesting of berries and learn the art of professional roasting and blending, followed by a personalized coffee tasting session. In the afternoon, take a comfortable short drive to visit the stunning Hebbe Falls or Jhari Waterfalls, nestled deep within pristine forest clearings—an incredible spot for family photography.'
            ),
            [
                'Sightseeing Included: Private Coffee Plantation Trail, Jhari/Hebbe Waterfalls',
                'Optional Activities: Therapeutic wellness treatment or Ayurvedic spa session at the resort',
                'Overnight Stay: Ultra-Luxury Boutique Resort, Chikmagalur',
                'Meals Included: Full Buffet Breakfast & Traditional Estate Dinner'
            ],
            ),
            _day(
            3,
            'Highest Peaks & Hoysala Heritage',
            (
                "Today features the pinnacle of Karnataka Sightseeing. Depart early in your luxury vehicle to visit Mullayanagiri Peak, the highest summit in Karnataka. As you ascend, witness breathtaking landscapes and sweeping panoramas of the valley unfolding below. A short, highly accessible walk brings you to the crown of the peak, where the clouds literally drift through your hands. Following this refreshing morning, travel down to explore the historical architectural marvels of the Hoysala dynasty at Belur and Halebidu. Marvel at the intricate stone carvings and soapstone temples that have stood for centuries, capturing a glimpse of southern India's golden heritage."
            ),
            [
                'Sightseeing Included: Mullayanagiri Peak, Seethalayanagiri, Belur Chennakeshava Temple',
                'Evening Experience: A special curated family barbecue dinner under a starlit mountain sky',
                'Overnight Stay: Ultra-Luxury Boutique Resort, Chikmagalur',
                'Meals Included: Breakfast & Signature Curated Farewell Dinner'
            ],
            ),
            _day(
            4,
            'Chikmagalur to Bangalore',
            (
                'Enjoy a relaxed morning breakfast out on the sun-dappled lawns. Take one last walk through the aromatic garden pathways or purchase premium single-origin coffee selections from the estate boutique. Pack your bags and check out comfortably as your private vehicle arrives. Your chauffeur will drive you smoothly back to Bangalore, dropping you off directly at the International Airport or your doorstep. Your premium TRAGUIN Karnataka Package concludes, leaving you with rejuvenated spirits and unforgettable memories of the coffee hills.'
            ),
            [
                'Transfers Included: Private Luxury Return Drop-off to Bangalore',
                'Meals Included: Full Buffet Breakfast'
            ],
            ),
        ],
        hotels=[
            _hotel('The Serai Chikmagalur', 'Chikmagalur', '03 Nights', 'Deluxe', 'Estate Villa with Private Deck', 'Breakfast & Dinner', 4, 1),
            _hotel('Java Rain Resorts', 'Chikmagalur', '03 Nights', 'Premium', 'Kaffe Room / Luxury Villa', 'Breakfast & Dinner', 5, 2),
            _hotel('Trivik Hotels & Resorts', 'Chikmagalur', '03 Nights', 'Luxury', 'Oak Suite with Panoramic Mountain View', 'Breakfast & Dinner', 5, 3),
            _hotel('Evolve Back, Chikkamagaluru', 'Chikmagalur', '03 Nights', 'Ultra Luxury', 'Private Pool Villa / Plantation Suite', 'Breakfast & Dinner', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at handpicked premium plantation resorts with top-tier luxury amenities', 1),
            _inc_included('Meals: 03 Gourmet Breakfasts and 03 specially curated multi-cuisine dinners at the resort', 2),
            _inc_included('Transfers & Sightseeing: All commutes and sightseeing via a private, dedicated luxury Innova Crysta', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated digital concierge and local destination support', 4),
            _inc_included('Complimentary Experiences: Private naturalist-led coffee walk, coffee-tasting workshop, and high-tea', 5),
            _inc_included('Welcome Amenities: Premium arrival gift box containing artisanal chocolates and fresh-pressed organic estate samples', 6),
            _inc_excluded('Airfare or interstate train tickets to Bangalore', 7),
            _inc_excluded('Entrance tickets to historical monuments, camera permits, or local forest department jeep fees', 8),
            _inc_excluded('Personal expenses such as premium beverages, laundry, minibar, and tips', 9),
            _inc_excluded('Optional off-road vehicle transfers or sightseeing extensions outside the itinerary layout', 10),
            _inc_excluded('Travel insurance, medical charges, and porterage fees', 11),
        ],
    )
    return package, itinerary



KARNATAKA_DOMESTIC_BUILDERS = [
    build_ka_001,
    build_ka_002,
    build_ka_003,
    build_ka_004,
    build_ka_005,
    build_ka_006,
    build_ka_007,
    build_ka_008,
    build_ka_009,
    build_ka_010,
    build_ka_011,
    build_ka_012,
    build_ka_013,
    build_ka_014,
    build_ka_015,
    build_ka_016,
    build_ka_017,
]
