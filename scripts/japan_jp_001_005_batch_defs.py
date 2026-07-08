"""Builder functions for JP-001 through JP-005 Japan international packages."""

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

JAPAN_SLUG = "japan"


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


def build_jp_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JP-001'
    tour_code = 'TRG-JPN-HIGHLIGHTS-2026'
    title = 'Japan Highlights Family Tour'
    duration = '06 Nights / 07 Days'
    slug = 'jp-001-japan-highlights-family-tour'
    itin_slug = 'jp-001-japan-highlights-itinerary'
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
            _ph('Serial code JP-001 | TRAGUIN tour code TRG-JPN-HIGHLIGHTS-2026', 1),
            _ph('Country: Japan, East Asia | Category: Best Japan Family Tour Package', 2),
            _ph('Destinations: Tokyo • Mt. Fuji • Bullet Train Shinkansen • Kyoto Temples • Osaka Dotonbori', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Japan Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Japan Highlights Family Tour',
        overview="Tokyo • Mt. Fuji • Bullet Train Shinkansen • Kyoto Temples • Osaka Dotonbori 06 Nights / 07 Days Classic Japan Family Heritage Expedition SERIAL CODE: JP-001 TRAGUIN TOUR CODE: TRG-JPN-HIGHLIGHTS-2026 STATE / COUNTRY: Japan / East Asia CATEGORY: Best Japan Family Tour Package DURATION: 06 Nights / 07 Days Tokyo (3N) • Kyoto (2N) • Osaka (1N)\n\nTOUR OVERVIEW\nStep into a world where ancient traditions seamlessly blend with ultra-futuristic innovations on this magnificent TRAGUIN curated family heritage expedition. Connecting the neon high-rises and tech hubs of Tokyo, the timeless shrines of Kyoto, and the rich culinary streets of Osaka, this Luxury Japan Holiday guarantees a beautiful combination of deep cultural enrichment, scenic wonder, and unforgettable memories across generations. Family Comfort Note from TRAGUIN: Japan's complex logistics require meticulous planning. This 7-day optimized family journey features completely private executive air-conditioned vans, first-class Bullet Train (Shinkansen) tickets with coordinated luggage forwarding services, pre-booked skip-the-line admissions, and family-friendly dining paths backed by our 24/7 on-ground bilingual concierge support.\n\nWHY CHOOSE OUR JAPAN HIGHLIGHTS FAMILY TOUR?\nThe Land of the Rising Sun is an incredible storybook of majestic castles, historical shrines, and spectacular landscapes, creating the ultimate backdrop for multi-generational travel. Selecting this Best Japan Tour Package guarantees a smooth and rewarding traversal across the country's main Golden Route. This framework incorporates top-ranked travel keywords optimized for Google ranking, ensuring an exceptional client quotation and presentation format for premier Japan Sightseeing landmarks. Discover Top Tourist Places in Japan: admire the snow-capped majesty of Mt. Fuji, wander through the historic red torii gates of Fushimi Inari, experience a private sushi-making masterclass in Tokyo, and explore the dazzling neon corridors of Osaka's Dotonbori district—a premier popular Instagram location. It is the absolute Best Time to Visit Japan to witness private curated experiences, celebrate exclusive experiences, photograph immense scenic beauty, and secure an unparalleled Premium Japan Experience. TRAGUIN Family Signatures: Private family sushi-making masterclass with a master chef, first-class Shinkansen bullet train tickets, private luxury van transits throughout, seamless hotel-to-hotel luggage transport, and reserved front-row seating at culture showcases. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='JP-001 | Japan Highlights Family Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Japan package (JP-001 / TRG-JPN-HIGHLIGHTS-2026): Tokyo • Mt. Fuji • Bullet Train Shinkansen • Kyoto Temples • Osaka Dotonbori with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN TOKYO & NEON INITIAL EXPLORATION', 1),
            _ih('Day 02: HISTORIC ASAKUSA & PRIVATE SUSHI MASTERCLASS', 2),
            _ih('Day 03: MT. FUJI SPECTACULAR LANDSCAPES & HAKONE CRUISE', 3),
            _ih('Day 04: BULLET TRAIN SHINKANSEN TRANSIT TO TIMELESS KYOTO', 4),
            _ih('Day 05: KYOTO RED TORII GATES & GOLDEN PAVILION', 5),
            _ih('Day 06: OSAKA CASTLE MAJESTY & DOTONBORI STREET GALA', 6),
            _ih('Day 07: SEAMLESS AIRPORT TRANSIT & DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN TOKYO & NEON INITIAL EXPLORATION',
                (
                    'Welcome to Tokyo! Your grand family holiday begins with a premium airport reception at Narita or Haneda Airport. Your private TRAGUIN chauffeur-driven luxury van transfers you safely to your central property. In the evening, enjoy a slow orientation walk through the dazzling neon-lit high-rises of Shinjuku or Shibuya, capturing beautiful family photographs crossing the famous Shibuya Scramble pedestrian path. Sightseeing Included: VIP Airport meet & greet reception, private luxury van transfer, Shibuya Scramble trail. Evening Experience: Family welcome dinner at an upscale traditional Japanese Izakaya style restaurant.'
                ),
                [
                    'Overnight Stay: Tokyo City Centre (Handpicked Premium Family-Friendly Luxury Hotel)',
                    'Meals Included: Traditional Japanese Welcome Dinner',
                ],
            ),
            _day(
                2,
                'HISTORIC ASAKUSA & PRIVATE SUSHI MASTERCLASS',
                (
                    "Savor a bountiful breakfast before delving into Tokyo's rich historic contrast. Visit Senso-ji, Tokyo’s oldest Buddhist temple in Asakusa, walking down Nakamise street for local crafts. In the afternoon, participate in a highlight event: a private family sushi-making masterclass led by an expert Japanese chef, learning the delicate art of rolling maki and shaping nigiri before feasting on your creations. Sightseeing Included: Senso-ji Temple guided tour, TeamLab Planets digital art immersive experience entry passes. Special Curation:Private family culinary sushi-making masterclass and premium lunch."
                ),
                [
                    'Overnight Stay: Tokyo City Centre (Handpicked Premium Family-Friendly Luxury Hotel)',
                    'Meals Included: International Breakfast & Private Masterclass Sushi Lunch',
                ],
            ),
            _day(
                3,
                'MT. FUJI SPECTACULAR LANDSCAPES & HAKONE CRUISE',
                (
                    'Check out after breakfast as your private vehicle drives towards the iconic majesty of Mt. Fuji. Ascend to the Subaru 5th Station for panoramic view blocks of the snow-capped peak. Later, head into Hakone for a relaxing, scenic cruise on Lake Ashi aboard a historic pirate ship, taking in the scenic beauty of the red torii gate standing inside the pristine mountain waters. Sightseeing Included: Mt. Fuji 5th Station entrance tracks, Lake Ashi panoramic cruise, Hakone Komagatake Ropeway. Logistics Highlight: TRAGUIN seamless hotel-to-hotel luggage forwarding services handle your heavy bags to Kyoto.'
                ),
                [
                    'Overnight Stay: Hakone Onsen Resort (Premium Ryokan with Private Family Hot Springs)',
                    'Meals Included: International Breakfast & Traditional multi-course Kaiseki Dinner',
                ],
            ),
            _day(
                4,
                'BULLET TRAIN SHINKANSEN TRANSIT TO TIMELESS KYOTO',
                (
                    'Board Japan’s world-famous Shinkansen Bullet Train in first-class comfort. Experience incredible speeds of up to 320 km/h with total stability while your family relaxes in spacious layouts. Arrive in Kyoto, the cultural heart of Japan. Check into your hotel and spend the afternoon wandering through the wooden tea houses of the historic Gion district, learning traditional stories. Sightseeing Included: First-Class Bullet Train Shinkansen ticket, Gion wooden heritage district guided walking tour.'
                ),
                [
                    'Overnight Stay: Kyoto Heritage Centre (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Gourmet Kyoto Bento Lunch',
                ],
            ),
            _day(
                5,
                'KYOTO RED TORII GATES & GOLDEN PAVILION',
                (
                    'Wake up early for an immersive experience inside Fushimi Inari Shrine. Stroll through the thousands of iconic vermilion torii gates winding up the sacred mountain forest. In the afternoon, visit Kinkaku-ji (The Golden Pavilion), a Zen temple completely covered in brilliant gold leaf, reflecting beautifully across its pristine mirror pond. Sightseeing Included: Fushimi Inari Torii Gate trail, Kinkaku-ji Golden Pavilion entry, Arashiyama Bamboo Grove.'
                ),
                [
                    'Overnight Stay: Kyoto Heritage Centre (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Traditional Kyoto Cuisine Dinner',
                ],
            ),
            _day(
                6,
                'OSAKA CASTLE MAJESTY & DOTONBORI STREET GALA',
                (
                    'A brief morning private van transfer brings your family to the dynamic commercial hub of Osaka. Tour the monumental Osaka Castle, learning about the ancient samurai legacy. In the evening, celebrate with a highlights event: a street-food exploration tour through the blinding neon-lit pathways of Dotonbori, tasting local takoyaki and okonomiyaki during a grand farewell dinner. Sightseeing Included: Osaka Castle park guided entry, Dotonbori neon district culinary walking tour. Evening Experience: Grand farewell family celebration dinner party.'
                ),
                [
                    'Overnight Stay: Osaka Bay / Centre (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Dotonbori Street-Food Farewell Feast',
                ],
            ),
            _day(
                7,
                'SEAMLESS AIRPORT TRANSIT & DEPARTURE',
                (
                    'Savor your final morning breakfast at your premium hotel, capturing a final round of family photographs. Our concierge handlers coordinate your seamless checkout and take full care of all group luggage logistics. Your private luxury van transfers your family comfortably to Kansai International Airport (or Tokyo connection) for your flight home, concluding your classical expedition. Transfers: Private luxury van airport departure transfer, comprehensive luggage coordination.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Keio Plaza Hotel TokyoHakone Yumoto OnsenThe Thousand Kyoto / Cross Osaka',
                'Multi-city Japan',
                '6N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Keio Plaza Hotel TokyoHakone Yumoto OnsenThe Thousand Kyoto / Cross Osaka',
            ),
            _hotel(
                'Cerulean Tower Tokyu Hotel Hakone Kowakien Ten- yu Kyoto Tokyu Hotel / Swissotel Nankai',
                'Multi-city Japan',
                '6N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Cerulean Tower Tokyu Hotel Hakone Kowakien Ten- yu Kyoto Tokyu Hotel / Swissotel Nankai',
            ),
            _hotel(
                'The Capitol Hotel TokyuGora Kadan Ryokan The Ritz-Carlton Kyoto / W Osaka',
                'Multi-city Japan',
                '6N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Capitol Hotel TokyuGora Kadan Ryokan The Ritz-Carlton Kyoto / W Osaka',
            ),
            _hotel(
                'Aman Tokyo / Palace Hotel Hoshinoya Fuji / Gora Kadan Aman Kyoto / St. Regis Osaka',
                'Multi-city Japan',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Aman Tokyo / Palace Hotel Hoshinoya Fuji / Gora Kadan Aman Kyoto / St. Regis Osaka',
            )
        ],
        inclusions=[
            _inc_included('Stays: 06 Nights accommodation in family-friendly premium luxury hotel rooms or traditional Ryokan', 1),
            _inc_included('Catering: Bountiful daily breakfasts, a traditional multi-course Kaiseki feast, and curated specialty dinners', 2),
            _inc_included('Bullet Train: First-class Bullet Train Shinkansen tickets from Hakone/Tokyo to Kyoto', 3),
            _inc_included('Luggage Care: TRAGUIN seamless hotel-to-hotel luggage forwarding service (1 bag per person)', 4),
            _inc_included('VIP Access Passes: Skip-the-line entries to TeamLab Planets, Kinkaku-ji, and specified major landmarks', 5),
            _inc_included('Specialty Curation: Private Family Sushi-making Masterclass led by an expert Japanese sushi chef', 6),
            _inc_included('TRAGUIN Support: 24/7 dedicated on-call guest assistance hotline and bilingual destination managers', 7),
            _inc_excluded('International Flight tickets and Japan entry Visa processing fees', 8),
            _inc_excluded('Personal expenses, hotel room service laundry bills, mini-bar billing', 9),
            _inc_excluded('Tipping, porterage fees, or optional sightseeing excursions not mentioned in the flow', 10),
        ],
    )
    return package, itinerary

def build_jp_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JP-002'
    tour_code = 'TRG-JPN-FAMILY-2026'
    title = 'Japan Family Expedition'
    duration = '07 Nights / 08 Days'
    slug = 'jp-002-japan-family-expedition'
    itin_slug = 'jp-002-japan-family-expedition-itinerary'
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
            _ph('Serial code JP-002 | TRAGUIN tour code TRG-JPN-FAMILY-2026', 1),
            _ph('Country: Japan, East Asia | Category: Best Japan Family Tour Package', 2),
            _ph('Destinations: Tokyo • Mt. Fuji • Bullet Train Shinkansen • Osaka Universal • Kyoto Shrines', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Japan Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Japan Family Expedition',
        overview="07 Nights / 08 Days Immersive Golden Route Family Explorer SERIAL CODE: JP-002 TRAGUIN TOUR CODE: TRG-JPN-FAMILY-2026 STATE / COUNTRY: Japan / East Asia CATEGORY: Best Japan Family Tour Package DURATION: 07 Nights / 08 Days Tokyo (3N) • Osaka (2N) • Kyoto (2N)\n\nTOUR OVERVIEW\nEmbark on the ultimate multigenerational family journey through the Land of the Rising Sun with this beautifully paced TRAGUIN curated itinerary. Seamlessly connecting the neon sky-high horizons of Tokyo, the cinematic thrilling theme worlds of Osaka, and the peaceful UNESCO heritage forests of Kyoto, this Luxury Japan Holiday guarantees a rich balance of absolute comfort, technical marvel, and unforgettable memories. Family Comfort Note from TRAGUIN: Seamless operation is our commitment. This 8-day grand expedition relies on dedicated private luxury executive vans, first-class Shinkansen Bullet Train tickets, TRAGUIN Luggage Forwarding services to eliminate handling heavy bags on trains, and pre-vetted family dining reservations backed by our 24/7 bilingual on-ground support.\n\nWHY CHOOSE OUR TOKYO, OSAKA & KYOTO FAMILY FRAMEWORK?\nJapan is an incredibly rich storybook where ancient shrines stand alongside neon towers, making it the premier safe global environment for family bonding. Selecting this Best Japan Tour Package delivers a comprehensive exploration across the country's iconic Golden Route. Our narrative relies on topsearched travel terms optimized for Google ranking, ensuring an exceptional client quotation and presentation layout for premier Japan Sightseeing milestones. Discover Top Tourist Places in Japan: look across the snow-capped peak of Mt. Fuji, wander through Kyoto's historic red torii paths, enjoy a private sushi-making masterclass with a master chef in Tokyo, and experience Universal Studios Japan in Osaka—a premier popular Instagram location. It is the absolute Best Time to Visit Japan to enjoy curated experiences, experience high-end exclusive experiences, photograph breathtaking landscapes, and secure an unmatched Premium Japan Experience. TRAGUIN Family Signatures: Private family sushi masterclass, TeamLab Planets digital art priority passes, First-Class bullet train seating, hotel-to-hotel luggage transits, and private luxury executive van allocations throughout. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='JP-002 | Japan Family Expedition | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Japan package (JP-002 / TRG-JPN-FAMILY-2026): Tokyo • Mt. Fuji • Bullet Train Shinkansen • Osaka Universal • Kyoto Shrines with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN TOKYO & SHIBUYA NEON CRUISE', 1),
            _ih('Day 02: HISTORIC ASAKUSA & PRIVATE SUSHI MASTERCLASS', 2),
            _ih('Day 03: MT. FUJI PANORAMIC LANDSCAPES & LAKE ASHI CRUISE', 3),
            _ih('Day 04: FIRST-CLASS BULLET TRAIN TO OSCILLATING OSAKA', 4),
            _ih('Day 05: UNIVERSAL STUDIOS JAPAN FULL-DAY IMMERSION', 5),
            _ih('Day 06: OSAKA CASTLE TO THE BAMBOO FORESTS OF KYOTO', 6),
            _ih('Day 07: GOLDEN PAVILION & RED TORII PATHWAYS GALA', 7),
            _ih('Day 08: HIGH-END TRANSIT & KANSAI DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN TOKYO & SHIBUYA NEON CRUISE',
                (
                    'Welcome to Tokyo! Your grand family holiday begins with a premium airport reception at Narita or Haneda Airport. Your private TRAGUIN chauffeur transfers your family in a spacious executive van directly to your central hotel. In the evening, explore the blinding neon-lit pathways of Shibuya, capturing beautiful family photographs crossing the famous Shibuya Scramble pedestrian paths. Sightseeing Included: VIP Airport reception, private luxury van transit, Shibuya Scramble walking trail. Evening Experience: Family welcome dinner at an upscale traditional Japanese restaurant.'
                ),
                [
                    'Overnight Stay: Tokyo City Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: Traditional Japanese Welcome Dinner',
                ],
            ),
            _day(
                2,
                'HISTORIC ASAKUSA & PRIVATE SUSHI MASTERCLASS',
                (
                    'Savor a bountiful breakfast before discovering Tokyo’s historic core. Visit Senso-ji Temple in Asakusa, walking down Nakamise craft street. In the afternoon, participate in a highlights event: a private family sushi-making masterclass led by an expert Japanese chef. Learn to roll maki and shape nigiri before enjoying your delicious creations for a family lunch. Conclude with priority entry to teamLab Planets immersive digital art maze. Sightseeing Included: Senso-ji Temple guided tour, TeamLab Planets priority entry passes. Special Curation:Private family sushi-making masterclass with a master chef.'
                ),
                [
                    'Overnight Stay: Tokyo City Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Masterclass Sushi Lunch',
                ],
            ),
            _day(
                3,
                'MT. FUJI PANORAMIC LANDSCAPES & LAKE ASHI CRUISE',
                (
                    'Check out as your private luxury van drives towards the majestic snow-capped peak of Mt. Fuji. Ascend to the Subaru 5th Station for spectacular view blocks of the valley below. Later, head into Hakone for a relaxing, scenic cruise across Lake Ashi aboard an ornate pirate ship, taking in the scenic beauty of mountain peaks and red torii gates reflecting in the pristine lake waters. Sightseeing Included: Mt. Fuji 5th Station access, Lake Ashi panoramic pirate ship cruise. Logistics Highlight: TRAGUIN seamless luggage forwarding services handle your heavy bags directly from Tokyo to Osaka.'
                ),
                [
                    'Overnight Stay: Tokyo City Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Casual Fuji-view Lunch',
                ],
            ),
            _day(
                4,
                'FIRST-CLASS BULLET TRAIN TO OSCILLATING OSAKA',
                (
                    'HIGH-SPEED REFINEMENT – SHINKANSEN TO ARABIAN FUTURISM Board Japan’s world-famous Shinkansen Bullet Train in First-Class Comfort. Experience incredible speeds of up to 320 km/h with total stability while your family relaxes in spacious layouts. Arrive in the dynamic culinary capital of Osaka. Check into your premium hotel and spend a vibrant evening exploring the glowing neon- lined canal walkways of Dotonbori, photographing the iconic Glico Man banner. Sightseeing Included: First-Class Bullet Train Shinkansen ticket, Dotonbori neon district orientation walk.'
                ),
                [
                    'Overnight Stay: Osaka Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Dotonbori Street-Food Culinary Dinner',
                ],
            ),
            _day(
                5,
                'UNIVERSAL STUDIOS JAPAN FULL-DAY IMMERSION',
                (
                    'A thrilling day for the entire family. Enter Universal Studios Japan with pre-arranged express passes to minimize all lines. Explore Super Nintendo World, race inside Mario Kart tracks, and experience the Wizarding World of Harry Potter. This highly engaging theme kingdom delivers endless smiles and unforgettable memories for children and adults alike. Sightseeing Included: Universal Studios Japan full-day admission tickets, Express priority passes.'
                ),
                [
                    'Overnight Stay: Osaka Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Theme Park Dine-around Vouchers',
                ],
            ),
            _day(
                6,
                'OSAKA CASTLE TO THE BAMBOO FORESTS OF KYOTO',
                (
                    'Tour the monumental Osaka Castle park, learning about historic samurai legends. In the afternoon, your private vehicle transfers your family to Kyoto, the cultural heart of Japan. Walk through the soaring, emerald Arashiyama Bamboo Grove, where towering stalks move with the wind, creating an otherworldly, sensory immersive experience. Sightseeing Included: Osaka Castle park guided tour, Arashiyama Bamboo Grove walking trail.'
                ),
                [
                    'Overnight Stay: Kyoto Heritage Centre (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Traditional Kyoto Cuisine Dinner',
                ],
            ),
            _day(
                7,
                'GOLDEN PAVILION & RED TORII PATHWAYS GALA',
                (
                    'Explore Kyoto’s architectural crown, Kinkaku-ji (The Golden Pavilion), entirely covered in gold leaf and reflecting over a mirror pond. Later, discover Fushimi Inari Shrine, walking past thousands of brilliant vermilion torii gates winding up the sacred forest. Celebrate your final evening with a grand farewell dinner party at a historic garden terrace restaurant. Sightseeing Included: Kinkaku-ji Golden Pavilion entry, Fushimi Inari Torii Gate trail. Evening Experience: Grand farewell family culinary feast with local cultural performances.'
                ),
                [
                    'Overnight Stay: Kyoto Heritage Centre (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Grand Farewell Gala Dinner',
                ],
            ),
            _day(
                8,
                'HIGH-END TRANSIT & KANSAI DEPARTURE',
                (
                    'Savor a final luxurious breakfast, reviewing your incredible photo library. Our corporate concierge assistants handle your seamless checkout and manage all group luggage logistics smoothly. Your private luxury van transfers your family comfortably to Osaka Kansai International Airport for your departure flight, concluding an epic grand holiday. Transfers: Private luxury van airport departure transit, priority luggage coordination.'
                ),
                [
                    'Meals Included: International固定 Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Keio Plaza Hotel TokyoCross Hotel Osaka The Thousand Kyoto',
                'Multi-city Japan',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Keio Plaza Hotel TokyoCross Hotel Osaka The Thousand Kyoto',
            ),
            _hotel(
                'Cerulean Tower TokyuSwissotel Nankai Osaka Kyoto Tokyu Hotel',
                'Multi-city Japan',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Cerulean Tower TokyuSwissotel Nankai Osaka Kyoto Tokyu Hotel',
            ),
            _hotel(
                'The Capitol Hotel TokyuW Osaka The Ritz-Carlton Kyoto',
                'Multi-city Japan',
                '7N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Capitol Hotel TokyuW Osaka The Ritz-Carlton Kyoto',
            ),
            _hotel(
                'Aman Tokyo / Palace Hotel St. Regis Osaka Aman Kyoto / Suiran Luxury Collection',
                'Multi-city Japan',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Aman Tokyo / Palace Hotel St. Regis Osaka Aman Kyoto / Suiran Luxury Collection',
            )
        ],
        inclusions=[
            _inc_included('Stays: 07 Nights accommodation in family-friendly premium luxury hotel rooms or suites', 1),
            _inc_included('Catering: Bountiful daily breakfast spreads and curated specialty fine dinners as per itinerary', 2),
            _inc_included('Bullet Train: First-class Shinkansen Bullet train tickets from Tokyo to Osaka', 3),
            _inc_included('Luggage Care: TRAGUIN seamless hotel-to-hotel luggage forwarding service (1 bag per person)', 4),
            _inc_included('Specialty Curation: Private Family Sushi-making Masterclass led by an expert Japanese sushi chef', 5),
            _inc_excluded('International Flight tickets and Japan entry Visa processing fees', 6),
            _inc_excluded('Personal expenses, hotel room service laundry bills, mini-bar billing', 7),
            _inc_excluded('Tipping, porterage fees, or optional sightseeing excursions not mentioned in the flow', 8),
        ],
    )
    return package, itinerary

def build_jp_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JP-003'
    tour_code = 'TRG-JPN-ROMANCE-2026'
    title = 'Romantic Japan Honeymoon'
    duration = '07 Nights / 08 Days'
    slug = 'jp-003-romantic-japan-honeymoon'
    itin_slug = 'jp-003-romantic-japan-itinerary'
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
            _ph('Serial code JP-003 | TRAGUIN tour code TRG-JPN-ROMANCE-2026', 1),
            _ph('Country: Japan, East Asia | Category: Luxury Romantic Japan Honeymoon Package', 2),
            _ph('Destinations: Tokyo Skyline Romance • Mt. Fuji Hideaway • Bullet Train Luxury • Kyoto Bamboo', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium Japan Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Romantic Japan Honeymoon',
        overview="Tokyo Skyline Romance • Mt. Fuji Hideaway • Bullet Train Luxury • Kyoto Bamboo Serenade • Osaka Twilight 07 Nights / 08 Days Ultra-Luxury Romantic Japan Honeymoon Sanctuary SERIAL CODE: JP-003 TRAGUIN TOUR CODE: TRG-JPN-ROMANCE-2026 STATE / COUNTRY: Japan / East Asia CATEGORY: Luxury Romantic Japan Honeymoon Package DURATION: 07 Nights / 08 Days Tokyo (2N) • Hakone Onsen (1N) • Kyoto (3N) • Osaka (1N)\n\nTOUR OVERVIEW\nBegin your life together in the land where timeless ancient elegance meets the edge of tomorrow. Curated to absolute perfection by , this Romantic Japan escape weaves together Michelin-tier high-rise dining, intimate private volcanic hot-spring encounters, seamless first-class transits, and quiet strolls through historical geisha districts. This tailored Luxury Japan Holiday guarantees a beautiful collection of unforgettable memories. Honeymoon Note from TRAGUIN: True romance requires flawless execution. Our bespoke program features completely private luxury executive van transits, first-class Shinkansen bullet train seating, specialized TRAGUIN Luggage Forwarding services to bypass public bag carriage, and intimate candlelight dining venues overlooking breathtaking panoramas with 24/7 bilingual on-ground assistance.\n\nWHY CHOOSE OUR ROMANTIC JAPAN HONEYMOON SANCTUARY?\nJapan is a deeply poetic love letter written in cherry blossoms, mountain mist, and golden shrines, presenting a spectacularly dramatic backdrop for a luxury honeymoon celebration. Selecting this elite Japan Honeymoon Package provides a seamless blend of vibrant energy and quiet, luxurious isolation. This master framework features top-performing searched keywords optimized for Google ranking, showcasing premier Japan Sightseeing landmarks through a deeply emotional lens. Discover Top Tourist Places in Japan designed for couples: toast your union against the snow-capped peak of Mt. Fuji, share an intimate rickshaw journey through Kyoto's towering Arashiyama Bamboo Grove, wander through thousands of crimson torii gates at Fushimi Inari, and watch Osaka's neon horizons illuminate at twilight. It is the absolute Best Time to Visit Japan to experience private curated experiences, photograph immense scenic beauty, and secure an unparalleled Premium Japan Experience. TRAGUIN Honeymoon Signatures: Private helicopter skyline cruise over Tokyo, traditional luxury Ryokan stay with private open-air volcanic onsen baths, first-class Shinkansen bullet train tickets, private traditional tea ceremony in a secret Kyoto temple, and hotel-to-hotel luggage forwarding transits. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='JP-003 | Romantic Japan Honeymoon | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Japan package (JP-003 / TRG-JPN-ROMANCE-2026): Tokyo Skyline Romance • Mt. Fuji Hideaway • Bullet Train Luxury • Kyoto Bamboo with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN TOKYO & HELICOPTER SKYLINE CRUISE', 1),
            _ih('Day 02: TOKYO ART INSIGHTS & THE TEAMLAB MAZE', 2),
            _ih('Day 03: MOUNT FUJI HIDEAWAY & REJUVENATING HOT SPRINGS', 3),
            _ih('Day 04: FIRST-CLASS BULLET TRAIN TO POETIC KYOTO', 4),
            _ih('Day 05: PRIVATE TEMPLE TEA CEREMONY & BAMBOO SERENADE', 5),
            _ih('Day 06: THE GOLDEN PAVILION & CRIMSON TORII PATHWAYS', 6),
            _ih('Day 07: TRANSIT TO DYNAMIC OSAKA & NEON FAREWELL GALA', 7),
            _ih('Day 08: HIGH-END RESORT FAREWELL & DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN TOKYO & HELICOPTER SKYLINE CRUISE',
                (
                    'Your romantic Japan Honeymoon begins with an elite airport meet-and-greet reception at Narita or Haneda Airport. Your private TRAGUIN executive van transfers you comfortably to your ultra-luxury hotel. In the afternoon, lift off for an ultimate milestone experience: a private helicopter flight over the endless glowing horizons of Tokyo, taking in the scenic beauty of Tokyo Tower and Tokyo Skytree against a magnificent sunset backdrop. Sightseeing Included: VIP Airport reception, private luxury van transit, private helicopter skyline cruise. Honeymoon Touch: Chilled champagne and fresh seasonal strawberries awaiting in your suite on arrival.'
                ),
                [
                    'Overnight Stay: Tokyo Center (Handpicked Ultra-Luxury Sky-high Property)',
                    'Meals Included: Waterfront Candlelight Welcome Dinner',
                ],
            ),
            _day(
                2,
                'TOKYO ART INSIGHTS & THE TEAMLAB MAZE',
                (
                    'Savor a gourmet breakfast overlooking the Tokyo skyline. Spend a relaxed morning exploring the high-fashion boutiques of Ginza. In the afternoon, enjoy priority skip-the-line entries into the world-famous teamLab Planets, wandering through infinite immersive digital flower rooms and mirrored water labyrinths, capturing incredible photography points. Sightseeing Included: TeamLab Planets priority admission passes, Ginza fashion boulevard walking trail.'
                ),
                [
                    'Overnight Stay: Tokyo Center (Handpicked Ultra-Luxury Sky-high Property)',
                    'Meals Included: International Breakfast & Intimate Sushi Fine-Dining Lunch',
                ],
            ),
            _day(
                3,
                'MOUNT FUJI HIDEAWAY & REJUVENATING HOT SPRINGS',
                (
                    'Check out smoothly as your private vehicle drives towards the iconic majesty of Mt. Fuji. Arrive at a traditional luxury Ryokan in Hakone, nestled among forested volcanic hills. Check into your premium suite featuring a private outdoor thermal onsen hot-spring bath. Soak in the healing mineral waters with your partner, looking across the breathtaking landscapes in total privacy. Sightseeing Included: Mt. Fuji scenic valley trail, private hot spring hot-tub relaxation corridors. Logistics Highlight: TRAGUIN seamless luggage forwarding services handle your heavy bags directly from Tokyo to Kyoto.'
                ),
                [
                    'Overnight Stay: Hakone (Elite Luxury Onsen Ryokan Resort)',
                    'Meals Included: International Breakfast & Multi-course Traditional Kaiseki Feast',
                ],
            ),
            _day(
                4,
                'FIRST-CLASS BULLET TRAIN TO POETIC KYOTO',
                (
                    'HIGH-SPEED REFINEMENT – SHINKANSEN SEATING & GION TWILIGHT Board the legendary Shinkansen Bullet Train in First-Class Comfort. Relax in wide recliners as the train glides silently through mountain ranges. Arrive in Kyoto, the cultural soul of Japan. In the evening, take an intimate private guided walk through the wooden geisha lanes of Gion, watching lanterns light up along the Shirakawa canal walkway. Sightseeing Included: First-Class Bullet Train Shinkansen ticket, Gion wooden heritage district guided evening walk.'
                ),
                [
                    'Overnight Stay: Kyoto Riverside (Handpicked Ultra-Luxury Boutique Palace Resort)',
                    'Meals Included: International Breakfast & Traditional Kyoto Cuisine Bistro Dinner',
                ],
            ),
            _day(
                5,
                'PRIVATE TEMPLE TEA CEREMONY & BAMBOO SERENADE',
                (
                    'Wake up early for a spectacular experience. Board a traditional private rickshaw for an intimate cruise through the emerald Arashiyama Bamboo Grove, catching the morning sun beams filtering through the stalks. Later, access a hidden temple pavilion for a completely private Matcha Tea Ceremony hosted by an expert master, experiencing zen immersive experiences. Sightseeing Included: Arashiyama Bamboo Grove private rickshaw ride, private zen temple tea master ceremony.'
                ),
                [
                    'Overnight Stay: Kyoto Riverside (Handpicked Ultra-Luxury Boutique Palace Resort)',
                    'Meals Included: International Breakfast & Fine Dining Kaiseki Lunch',
                ],
            ),
            _day(
                6,
                'THE GOLDEN PAVILION & CRIMSON TORII PATHWAYS',
                (
                    'Visit Kinkaku-ji (The Golden Pavilion), a stunning structure covered entirely in gold leaf, reflecting across a glass-like mirror pond. In the afternoon, discover the legendary Fushimi Inari Shrine, walking past thousands of brilliant vermilion torii gates winding up the sacred mountain forest pathways, creating an absolute popular Instagram location. Sightseeing Included: Kinkaku-ji Golden Pavilion entry, Fushimi Inari Torii Gate mountain trail.'
                ),
                [
                    'Overnight Stay: Kyoto Riverside (Handpicked Ultra-Luxury Boutique Palace Resort)',
                    'Meals Included: International Breakfast & Premium Wagyu Beef Dinner Event',
                ],
            ),
            _day(
                7,
                'TRANSIT TO DYNAMIC OSAKA & NEON FAREWELL GALA',
                (
                    'A brief morning private transit brings you to the lively streets of Osaka. Visit the historic Osaka Castle park. In the evening, celebrate the finale of your honeymoon with an intimate culinary walking tour through the glowing, neon-lit canal pathways of Dotonbori. Toast your love during a grand farewell dinner at a private riverfront terrace, sealing unforgettable memories. Sightseeing Included: Osaka Castle park guided tour, Dotonbori neon canal district culinary trail. Evening Experience: Grand honeymoon finale candlelight dinner party.'
                ),
                [
                    'Overnight Stay: Osaka Centre (Handpicked Ultra-Luxury Modern Property)',
                    'Meals Included: International Breakfast & Riverfront Gastronomy Farewell Dinner',
                ],
            ),
            _day(
                8,
                'HIGH-END RESORT FAREWELL & DEPARTURE',
                (
                    'Enjoy a luxurious final breakfast, looking out over the city skyline. Our corporate concierge handlers handle your seamless checkout and luggage transits perfectly. Your private vehicle transfers your family comfortably to Osaka Kansai International Airport (or Tokyo connection) for your flight home, concluding an epic grand honeymoon vacation. Transfers: Private luxury van airport departure transfer, priority luggage coordination. HANDPICKED ELITE HONEYMOON ACCOMMODATIONS Category Tokyo (2 Nights) Hakone Ryokan (1 Night) Kyoto & Osaka (4 Nights) OPTION 01 – DELUXE Keio Plaza Hotel TokyoHakone Yumoto OnsenThe Thousand Kyoto / Cross Osaka OPTION 02 – PREMIUMCerulean Tower TokyuHakone Kowakien Ten-yuKyoto Tokyu Hotel / Swissotel Nankai OPTION 03 – LUXURY The Capitol Hotel Tokyu Gora Kadan Ryokan The Ritz-Carlton Kyoto / W Osaka OPTION 04 – ULTRA LUXURY Aman Tokyo / Palace Hotel Hoshinoya Fuji / Gora Kadan Aman Kyoto / St. Regis Osaka'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Keio Plaza Hotel TokyoHakone Yumoto OnsenThe Thousand Kyoto / Cross Osaka',
                'Multi-city Japan',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Keio Plaza Hotel TokyoHakone Yumoto OnsenThe Thousand Kyoto / Cross Osaka',
            ),
            _hotel(
                'Cerulean Tower TokyuHakone Kowakien Ten-yuKyoto Tokyu Hotel / Swissotel Nankai',
                'Multi-city Japan',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Cerulean Tower TokyuHakone Kowakien Ten-yuKyoto Tokyu Hotel / Swissotel Nankai',
            ),
            _hotel(
                'The Capitol Hotel Tokyu Gora Kadan Ryokan The Ritz-Carlton Kyoto / W Osaka',
                'Multi-city Japan',
                '7N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Capitol Hotel Tokyu Gora Kadan Ryokan The Ritz-Carlton Kyoto / W Osaka',
            ),
            _hotel(
                'Aman Tokyo / Palace Hotel Hoshinoya Fuji / Gora Kadan Aman Kyoto / St. Regis Osaka',
                'Multi-city Japan',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Aman Tokyo / Palace Hotel Hoshinoya Fuji / Gora Kadan Aman Kyoto / St. Regis Osaka',
            )
        ],
        inclusions=[
            _inc_included('Amenities: Complimentary chilled champagne, seasonal strawberries, and floral arrangements on arrival', 1),
            _inc_included('Air Logistics: Private Helicopter Flight skyline cruise over Tokyo landmarks', 2),
            _inc_included('Transfers: Private luxury water crafts, high-speed Executive trains, and private Mercedes transits', 3),
            _inc_included('Luggage Care: TRAGUIN seamless hotel-to-hotel luggage forwarding service (1 bag per person)', 4),
            _inc_included('TRAGUIN Support: VIP fast-track skip-the-line entries, 24/7 on-call honeymoon concierge desk support', 5),
            _inc_included('Amenities: Complimentary chilled champagne, seasonal strawberries, and floral arrangements on arrival', 6),
            _inc_included('Air Logistics: Private Helicopter Flight skyline cruise over Tokyo landmarks', 7),
            _inc_included('Transfers: Private luxury water crafts, high-speed Executive trains, and private Mercedes transits', 8),
            _inc_included('Luggage Care: TRAGUIN seamless hotel-to-hotel luggage forwarding service (1 bag per person)', 9),
            _inc_included('TRAGUIN Support: VIP fast-track skip-the-line entries, 24/7 on-call honeymoon concierge desk support', 10),
            _inc_excluded('International flight tickets and Japan entry Visa processing fees', 11),
            _inc_excluded('Personal expenses, hotel laundry, room service orders, mini-bar billing', 12),
            _inc_excluded('Tipping, porterage fees, or extra sightseeing entry tours not specified in the flow', 13),
            _inc_excluded('International flight tickets and Japan entry Visa processing fees', 14),
        ],
    )
    return package, itinerary

def build_jp_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JP-004'
    tour_code = 'TRG-JPN-LUXURY-2026'
    title = 'Luxury Japan Showcase'
    duration = '08 Nights / 09 Days'
    slug = 'jp-004-luxury-japan-showcase'
    itin_slug = 'jp-004-luxury-japan-itinerary'
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
            _ph('Serial code JP-004 | TRAGUIN tour code TRG-JPN-LUXURY-2026', 1),
            _ph('Country: Japan, East Asia | Category: Luxury Japan Holiday Sovereign Showcase', 2),
            _ph('Destinations: Tokyo Private Geisha Gala • Mt. Fuji VIP Helicopters • Gran Class Bullet Rail • Kyoto', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium Japan Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Japan Showcase',
        overview="Royal Shrines • Osaka Michelin Nights 08 Nights / 09 Days Ultimate Luxury Japan Imperial Sovereign Expedition SERIAL CODE: JP-004 TRAGUIN TOUR CODE: TRG-JPN-LUXURY-2026 STATE / COUNTRY: Japan / East Asia CATEGORY: Luxury Japan Holiday Sovereign Showcase DURATION: 08 Nights / 09 Days Tokyo (3N) • Hakone Luxury (1N) • Kyoto (3N) • Osaka (1N)\n\nTOUR OVERVIEW\nIndulge in the ultimate peak of Asian opulence with our crown jewel TRAGUIN curated imperial sovereign expedition. Meticulously engineered for the world's most discerning high-net-worth travelers, this Luxury Japan Holiday weaves private helicopter ridge crossings, exclusive Michelin-starred gastronomic feasts, private traditional performances closed to the public, and premier palace properties to secure an elite trail of unforgettable memories. Sovereign Note from TRAGUIN: Uncompromised distinction is our signature. This 9-day private journey includes full VIP tarmac transfers, premium chauffeured luxury fleets (Mercedes S-Class/V-Class), prioritized fast-track entries to historical sanctuaries, and personal 24/7 dedicated concierge managers handling your logistics flawlessly.\n\nWHY CHOOSE OUR ULTIMATE LUXURY JAPAN FRAMEWORK?\nThe Land of the Rising Sun represents the planet's finest integration of hyper-modern industrial triumph, meticulous aesthetic codes, and regal ancient history. Booking our flagship Premium Japan Experience guarantees an unparalleled curation of the country's ultimate secrets. This professional framework relies on topsearched travel keywords optimized for Google ranking, ensuring an exceptional presentation format for high-end Japan Sightseeing elements. Discover Top Tourist Places in Japan through unprecedented elite access: explore Tokyo via private helicopter flights, relax inside centuries-old traditional hot-spring palaces, bypass all public channels at Kyoto’s Golden Pavilion, and experience high-end gastronomic celebrations inside Osaka. It is the absolute Best Time to Visit Japan to witness private curated experiences, experience exclusive experiences, photograph immense breathtaking landscapes, and secure an unmatched Premium Japan Experience. TRAGUIN Sovereign Signatures: Private helicopter flight over Mount Fuji, Gran Class (Ultra-VIP) Shinkansen bullet train tickets, private exclusive Geisha dinner performance in Kyoto, private water transits and digital art gallery access after-hours, and continuous 24/7 dedicated luggage forwarding care. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='JP-004 | Luxury Japan Showcase | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Japan package (JP-004 / TRG-JPN-LUXURY-2026): Tokyo Private Geisha Gala • Mt. Fuji VIP Helicopters • Gran Class Bullet Rail • Kyoto with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: TOKYO SOVEREIGN ARRIVAL & ROOFTOP NETWORKING', 1),
            _ih('Day 02: PRIVATE TOKYO DISCOVERY & AFTER-HOURS ART PRIVILEGE', 2),
            _ih('Day 03: MT. FUJI HELICOPTER FLIGHT & ELITE ONSEN RYOKAN', 3),
            _ih('Day 04: GRAN CLASS BULLET TRAIN TRANSIT TO KYOTO PALACES', 4),
            _ih('Day 05: EXCLUSIVE TEMPLE ACCESS & PRIVATE GEISHA GALA DINNER', 5),
            _ih('Day 06: CRIMSON TORII PATHWAYS & PRIVATE MATCHA REVELATIONS', 6),
            _ih('Day 07: NARA DEER PARK TRAIL TO DYNAMIC OSAKA', 7),
            _ih('Day 08: SAMURAI CASTLE HERITAGE & NEON FAREWELL GALA', 8)
        ],
        days=[
            _day(
                1,
                'TOKYO SOVEREIGN ARRIVAL & ROOFTOP NETWORKING',
                (
                    "Your grand Luxury Japan expedition begins with a VIP aircraft-side greeting at Tokyo Narita or Haneda Airport. Clear customs smoothly via private diplomatic tracks as your dedicated TRAGUIN luxury chauffeur transfers you to your ultra-luxury hotel. In the evening, unwind with an intimate welcome family dinner party at a Michelin-starred rooftop restaurant overlooking the glowing Shinjuku skyline, taking in the city's infinite scenic beauty. Sightseeing Included: VIP airfield tarmac reception, private luxury vehicle airport transfer, skyline trail."
                ),
                [
                    'Overnight Stay: Tokyo Center (Handpicked Ultra-Luxury Palace Sky Property)',
                    'Meals Included: Michelin Gastronomy Welcome Tasting Menu',
                ],
            ),
            _day(
                2,
                'PRIVATE TOKYO DISCOVERY & AFTER-HOURS ART PRIVILEGE',
                (
                    'Savor a luxurious breakfast served privately by your floor butler. Spend a relaxed morning on a private guided architecture tour of the Meiji Shrine and Imperial Palace outer gardens. In the evening, enjoy unprecedented privilege: a completely private, after-hours admission to the world-famous teamLab Planets digital art maze, wandering through infinite mirrored rooms and flower tapestries in absolute serenity, capturing unique Sightseeing Included: Meiji Shrine private guide, TeamLab Planets after-hours exclusive private opening.'
                ),
                [
                    'photography points: .',
                    'Overnight Stay: Tokyo Center (Handpicked Ultra-Luxury Palace Sky Property)',
                    'Meals Included: International Breakfast & Premium Ginza Sushi Omakase Lunch',
                ],
            ),
            _day(
                3,
                'MT. FUJI HELICOPTER FLIGHT & ELITE ONSEN RYOKAN',
                (
                    'Check out as your luxury sedan transfers your family to the private helipad. Lift off in a premium helicopter for a breathtaking flight south, soaring past the towering, snow-capped peak of Mount Fuji. Land directly inside the serene, forested mountains of Hakone. Check into your ultra-luxury traditional Ryokan resort, spending your afternoon soaking in your private outdoor volcanic thermal hot spring baths, looking across immense breathtaking landscapes. Sightseeing Included: Private chartered helicopter flight over Mt. Fuji & Hakone ridges, private thermal hot spring layouts. Logistics Highlight: TRAGUIN dedicated luggage forwarding service handles all heavy bags directly from Tokyo to Kyoto.'
                ),
                [
                    'Overnight Stay: Hakone Mountain Range (Elite Ultra-Luxury Traditional Ryokan Sanctuary)',
                    'Meals Included: International Breakfast & Traditional 12-Course Kaiseki Dinner Feast',
                ],
            ),
            _day(
                4,
                'GRAN CLASS BULLET TRAIN TRANSIT TO KYOTO PALACES',
                (
                    'THE IMPERIAL TRANSIT – BULLET RAIL APEX & RICKSHAW RIDE Board the legendary Shinkansen Bullet Train in Gran Class Comfort (the ultra-VIP first-class cabin featuring leather sleeper shells and personal attendant service). Arrive seamlessly in Kyoto, the cultural soul of Japan. In the afternoon, board a traditional private rickshaw for a peaceful, curated journey through the towering Arashiyama Bamboo Grove, catching the golden sun filtering through the stalks. Sightseeing Included: Gran Class Shinkansen Bullet Train tickets, Arashiyama Bamboo Grove private rickshaw trail.'
                ),
                [
                    'Overnight Stay: Kyoto Riverside (Handpicked Ultra-Luxury Boutique Waterfront Palace)',
                    'Meals Included: International Breakfast & Premium Kyoto Bento Lunch Box',
                ],
            ),
            _day(
                5,
                'EXCLUSIVE TEMPLE ACCESS & PRIVATE GEISHA GALA DINNER',
                (
                    'Experience true cultural isolation. Spend your morning exploring the golden architectural spires of Kinkaku-ji (The Golden Pavilion) with pre-arranged skip-the-line VIP entries. In the evening, step inside a historic, century-old private tea house. Participate in a highly exclusive, private dinner gala featuring traditional musical and dance performances by authentic Kyoto Geishas—a rare, unforgettable experience. Sightseeing Included: Kinkaku-ji Golden Pavilion priority entry, Private Tea House access. Special Curation:Completely private Geisha dinner presentation with live musical accompaniment.'
                ),
                [
                    'Overnight Stay: Kyoto Riverside (Handpicked Ultra-Luxury Boutique Waterfront Palace)',
                    'Meals Included: International Breakfast & Royal Kaiseki Geisha Dinner Gala',
                ],
            ),
            _day(
                6,
                'CRIMSON TORII PATHWAYS & PRIVATE MATCHA REVELATIONS',
                (
                    'Discover the legendary Fushimi Inari Shrine early in the morning, walking past thousands of brilliant vermilion torii gates winding up the mountain slope. Later in the afternoon, access a private zen temple pavilion closed to the public. Participate in an authentic Matcha Tea Ceremony hosted by an expert tea master, learning centuries-old methods of mindfulness and zen immersive experiences. Sightseeing Included: Fushimi Inari mountain torii gate trail, Private zen temple tea master masterclass.'
                ),
                [
                    'Overnight Stay: Kyoto Riverside (Handpicked Ultra-Luxury Boutique Waterfront Palace)',
                    'Meals Included: International Breakfast & Premium A5 Kobe Beef Dinner Event',
                ],
            ),
            _day(
                7,
                'NARA DEER PARK TRAIL TO DYNAMIC OSAKA',
                (
                    "Check out as your private luxury van drives south towards Osaka, stopping en route at Nara Deer Park. Stand among hundreds of friendly bowing deer and tour the colossal Todai-ji Temple, viewing the world's largest bronze Buddha statue. Arrive in Osaka and check into your ultra-luxury modern suite, spending a free evening exploring retail innovations. Sightseeing Included: Nara Deer Park entry, Todai-ji Temple bronze Buddha guided tour, Osaka city drive."
                ),
                [
                    'Overnight Stay: Osaka City Centre (Handpicked Ultra-Luxury Flagship Property)',
                    'Meals Included: International Breakfast & Traditional Osaka Gastronomy Lunch',
                ],
            ),
            _day(
                8,
                'SAMURAI CASTLE HERITAGE & NEON FAREWELL GALA',
                (
                    'Tour the monumental Osaka Castle park with your private historian guide, gaining exclusive entry into the top tower viewpoints. In the evening, celebrate the grand finale of your sovereign expedition with an intimate culinary walking tour through the glowing neon-lit canal paths of Dotonbori. Toast your family or team during a grand farewell dinner at a private riverfront terrace, cementing unforgettable memories. Sightseeing Included: Osaka Castle tower private entry, Dotonbori neon canal district culinary walking trail. Evening Experience: Grand finale corporate or family celebration dinner party.'
                ),
                [
                    'Overnight Stay: Osaka City Centre (Handpicked Ultra-Luxury Flagship Property)',
                    'Meals Included: International Breakfast & Grand Farewell Riverfront Feast',
                ],
            ),
            _day(
                9,
                'SOVEREIGN CLOSING & KANSAI DEPARTURE',
                (
                    'Savor a luxurious final breakfast, enjoying the city skyline view blocks. Your dedicated personal butler handles your seamless checkout and coordinates all luggage transits smoothly. Your private executive van transfers your family comfortably to Osaka Kansai International Airport for your departure flight home, concluding an extraordinary grand holiday. Transfers: Private luxury van airport departure transfer, priority luggage handling. HANDPICKED ELITE SOVEREIGN ACCOMMODATIONS Category Tokyo Centre Palace (3N) Hakone Sanctuary (1N) Kyoto Waterfront (3N) Osaka Flagship (1N) OPTION 01 – DELUXE Keio Plaza Hotel Tokyo Hakone Yumoto Onsen The Thousand KyotoCross Hotel Osaka OPTION 02 – PREMIUM Cerulean Tower Tokyu Hakone Kowakien Ten-yu Kyoto Tokyu Hotel Swissotel Nankai Osaka OPTION 03 – LUXURY The Capitol Hotel Tokyu Gora Kadan RyokanThe Ritz-Carlton Kyoto W Dubai / W Osaka OPTION 04 – ULTRA LUXURY Aman Tokyo / Palace Hotel Hoshinoya Fuji / Gora Kadan Aman Kyoto / Suiran Luxury St. Regis Osaka'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Keio Plaza Hotel Tokyo Hakone Yumoto Onsen The Thousand KyotoCross Hotel Osaka',
                'Multi-city Japan',
                '8N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Keio Plaza Hotel Tokyo Hakone Yumoto Onsen The Thousand KyotoCross Hotel Osaka',
            ),
            _hotel(
                'Cerulean Tower Tokyu Hakone Kowakien Ten-yu Kyoto Tokyu Hotel Swissotel Nankai Osaka',
                'Multi-city Japan',
                '8N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Cerulean Tower Tokyu Hakone Kowakien Ten-yu Kyoto Tokyu Hotel Swissotel Nankai Osaka',
            ),
            _hotel(
                'The Capitol Hotel Tokyu Gora Kadan RyokanThe Ritz-Carlton Kyoto W Dubai / W Osaka',
                'Multi-city Japan',
                '8N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Capitol Hotel Tokyu Gora Kadan RyokanThe Ritz-Carlton Kyoto W Dubai / W Osaka',
            ),
            _hotel(
                'Aman Tokyo / Palace Hotel Hoshinoya Fuji / Gora Kadan Aman Kyoto / Suiran Luxury St. Regis Osaka',
                'Multi-city Japan',
                '8N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Aman Tokyo / Palace Hotel Hoshinoya Fuji / Gora Kadan Aman Kyoto / Suiran Luxury St. Regis Osaka',
            )
        ],
        inclusions=[
            _inc_included('Air Logistics: Private Chartered Helicopter Flight across Mount Fuji peak and Hakone mountain ridges', 1),
            _inc_included('Bullet Train: Ultra-VIP Gran Class Shinkansen Bullet Train tickets from Hakone/Tokyo to Kyoto', 2),
            _inc_included('Luggage Forwarding: Full TRAGUIN hotel-to-hotel seamless luggage transit care across cities', 3),
            _inc_included('TRAGUIN Protection: Dedicated 24/7 on-call travel expert concierge assistance and local guides', 4),
            _inc_included('Air Logistics: Private Chartered Helicopter Flight across Mount Fuji peak and Hakone mountain ridges', 5),
            _inc_included('Bullet Train: Ultra-VIP Gran Class Shinkansen Bullet Train tickets from Hakone/Tokyo to Kyoto', 6),
            _inc_included('Luggage Forwarding: Full TRAGUIN hotel-to-hotel seamless luggage transit care across cities', 7),
            _inc_included('TRAGUIN Protection: Dedicated 24/7 on-call travel expert concierge assistance and local guides', 8),
            _inc_excluded('International flight tickets and Japan entry Visa processing fees', 9),
            _inc_excluded('Personal expenses, hotel room service laundry bills, mini-bar billing', 10),
            _inc_excluded('Tipping, porterage fees, or optional extreme sightseeing excursions not mentioned in the flow', 11),
            _inc_excluded('International flight tickets and Japan entry Visa processing fees', 12),
            _inc_excluded('Personal expenses, hotel room service laundry bills, mini-bar billing', 13),
            _inc_excluded('Tipping, porterage fees, or optional extreme sightseeing excursions not mentioned in the flow', 14),
        ],
    )
    return package, itinerary

def build_jp_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'JP-005'
    tour_code = 'TRG-JPN-GRAND-2026'
    title = 'Grand Japan Tour'
    duration = '10 Nights / 11 Days'
    slug = 'jp-005-grand-japan-tour'
    itin_slug = 'jp-005-grand-japan-itinerary'
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
            _ph('Serial code JP-005 | TRAGUIN tour code TRG-JPN-GRAND-2026', 1),
            _ph('Country: Japan, East Asia | Category: Premium Grand Japan Tour Package', 2),
            _ph('Destinations: Tokyo • Mt. Fuji • Bullet Train Shinkansen • Kyoto Shrines • Nara Park • Osaka Universal •', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Executive Van / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium Japan Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Grand Japan Tour',
        overview="Hiroshima Peace Memorial 10 Nights / 11 Days Grand Japan Panoramic Luxury Masterpiece Exploration SERIAL CODE: JP-005 TRAGUIN TOUR CODE: TRG-JPN-GRAND-2026 STATE / COUNTRY: Japan / East Asia CATEGORY: Premium Grand Japan Tour Package DURATION: 10 Nights / 11 Days Tokyo (3N) • Hakone (1N) • Kyoto (3N) • Hiroshima (1N) • Osaka (2N)\n\nTOUR OVERVIEW\nUnveil the definitive masterpiece of Far East exploration with this highly comprehensive TRAGUIN curated panoramic itinerary. Sweeping seamlessly through the technological neon centers of Tokyo, the tranquil mountain hot springs of Hakone, the ancient geisha cores of Kyoto, the profound historical monuments of Hiroshima, and the vibrant culinary streets of Osaka, this Luxury Japan Holiday guarantees an incredible blend of deep cultural enrichment, scenic wonder, and unforgettable memories across generations. Welcome Note from TRAGUIN: Distinction demands flawless logistical design. This 11-day optimized grand expedition features continuous private luxury executive van transits, first-class Shinkansen Bullet Train connections, specialized luggage forwarding services to eliminate handling heavy bags on platforms, and handpicked premium properties providing unparalleled comfort.\n\nWHY CHOOSE OUR GRAND JAPAN PANORAMIC PACKAGE?\nJapan remains the world's most dramatic storybook where ancient stone shrines stand perfectly beside high- speed magnetic railways, creating a sublime canvas for an all-encompassing family vacation. Selecting this Best Japan Tour Package promises a flawless, expertly paced traversal across the entire length of the main island. This master framework features top-performing travel keywords optimized for Google ranking, ensuring an exceptional presentation format for high-end Japan Sightseeing paths. Explore all premier iconic attractions: view the snow-capped peak of Mount Fuji from an ornate lake cruise, wander through thousands of crimson torii gates at Fushimi Inari, step into the peaceful Miyajima Island floating torii gate, experience Universal Studios Japan with priority express passes, and enjoy a private sushi- making masterclass in Tokyo. It is the absolute Best Time to Visit Japan to experience private curated experiences, celebrate exclusive experiences, photograph immense breathtaking landscapes, and secure an unparalleled Premium Japan Experience. TRAGUIN Grand Signatures: Private family sushi-making masterclass with an executive chef, first-class Shinkansen bullet train tickets, private luxury van transits throughout, Universal Studios Japan VIP Express passes, hotel-to-hotel luggage transport care, and private traditional tea ceremony with a master. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='JP-005 | Grand Japan Tour | TRAGUIN',
        seo_description='Premium 10 Nights / 11 Days Japan package (JP-005 / TRG-JPN-GRAND-2026): Tokyo • Mt. Fuji • Bullet Train Shinkansen • Kyoto Shrines • Nara Park • Osaka Universal • with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN TOKYO & SHIBUYA NEON INITIAL EXPLORATION', 1),
            _ih('Day 02: HISTORIC ASAKUSA & PRIVATE SUSHI MASTERCLASS', 2),
            _ih('Day 03: MOUNT FUJI CHUREITO PAGODA & LAKE ASHI CRUISE', 3),
            _ih("Day 04: BULLET TRAIN TRANSIT TO KYOTO'S GEISHA HERITAGE", 4),
            _ih('Day 05: KYOTO RED TORII GATES & GOLDEN PAVILION', 5),
            _ih('Day 06: NARA DEER PARK & PRIVATE ZEN TEA CEREMONY', 6),
            _ih('Day 07: BULLET TRAIN TRANSIT TO HISTORIC HIROSHIMA', 7),
            _ih('Day 08: TRANSIT TO DYNAMIC OSAKA & DOTONBORI GALA', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN TOKYO & SHIBUYA NEON INITIAL EXPLORATION',
                (
                    'Welcome to Tokyo! Your grand panoramic journey begins with a seamless airport reception at Narita or Haneda Airport. Your private TRAGUIN chauffeur transfers your family in a spacious executive van directly to your central hotel. In the evening, explore the blinding neon-lit pathways of Shibuya, capturing beautiful family photographs crossing the famous Shibuya Scramble pedestrian paths. Sightseeing Included: VIP Airport reception, private luxury van transit, Shibuya Scramble walking trail. Evening Experience: Family welcome dinner at an upscale traditional Japanese Izakaya style restaurant.'
                ),
                [
                    'Overnight Stay: Tokyo City Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: Traditional Japanese Welcome Dinner',
                ],
            ),
            _day(
                2,
                'HISTORIC ASAKUSA & PRIVATE SUSHI MASTERCLASS',
                (
                    'Savor a bountiful breakfast before discovering Tokyo’s historic core. Visit Senso-ji Temple in Asakusa, walking down Nakamise craft street. In the afternoon, participate in a highlights event: a private family sushi-making masterclass led by an expert Japanese chef. Learn to roll maki and shape nigiri before enjoying your delicious creations for lunch. Conclude with priority entry to teamLab Planets immersive digital art maze. Sightseeing Included: Senso-ji Temple guided tour, TeamLab Planets priority entry passes. Special Curation:Private family sushi-making masterclass with a master chef.'
                ),
                [
                    'Overnight Stay: Tokyo City Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Masterclass Sushi Lunch',
                ],
            ),
            _day(
                3,
                'MOUNT FUJI CHUREITO PAGODA & LAKE ASHI CRUISE',
                (
                    'Check out as your private luxury van drives towards the majestic snow-capped peak of Mt. Fuji. Visit the famous Chureito Pagoda for the iconic postcard view of the peak behind the red pagoda. Later, head into Hakone for a relaxing, scenic cruise across Lake Ashi aboard an ornate pirate ship, taking in the scenic beauty of mountain peaks reflecting in the pristine lake waters. Sightseeing Included: Chureito Pagoda trail, Lake Ashi panoramic pirate ship cruise, Hakone Komagatake Ropeway. Logistics Highlight: TRAGUIN seamless luggage forwarding services handle your heavy bags directly from Tokyo to Kyoto.'
                ),
                [
                    'Overnight Stay: Hakone Mountain Range (Premium Ryokan with Private Family Hot Springs)',
                    'Meals Included: International Breakfast & Traditional multi-course Kaiseki Dinner Feast',
                ],
            ),
            _day(
                4,
                "BULLET TRAIN TRANSIT TO KYOTO'S GEISHA HERITAGE",
                (
                    'Board Japan’s world-famous Shinkansen Bullet Train in First-Class Comfort. Experience incredible speeds with total stability while your family relaxes in spacious layouts. Arrive in Kyoto, the cultural heart of Japan. Check into your hotel and spend the afternoon wandering through the wooden tea houses of the historic Gion district with a private local guide, learning traditional heritage stories. Sightseeing Included: First-Class Bullet Train Shinkansen ticket, Gion wooden heritage district guided walking tour.'
                ),
                [
                    'Overnight Stay: Kyoto Heritage Centre (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Gourmet Kyoto Bento Lunch',
                ],
            ),
            _day(
                5,
                'KYOTO RED TORII GATES & GOLDEN PAVILION',
                (
                    'Wake up early for an immersive experience inside Fushimi Inari Shrine. Stroll through the thousands of iconic vermilion torii gates winding up the sacred mountain forest. In the afternoon, visit Kinkaku-ji (The Golden Pavilion), a Zen temple completely covered in brilliant gold leaf, reflecting beautifully across its pristine mirror pond, capturing wonderful photography points. Sightseeing Included: Fushimi Inari Torii Gate trail, Kinkaku-ji Golden Pavilion entry, Arashiyama Bamboo Grove.'
                ),
                [
                    'Overnight Stay: Kyoto Heritage Centre (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Traditional Kyoto Cuisine Dinner',
                ],
            ),
            _day(
                6,
                'NARA DEER PARK & PRIVATE ZEN TEA CEREMONY',
                (
                    "Excursion to Japan's ancient capital, Nara. Visit Nara Deer Park to stand among hundreds of friendly bowing deer and view the massive bronze Buddha statue inside Todai-ji Temple. In the afternoon, return to Kyoto for a completely private Matcha Tea Ceremony hosted by an expert master inside a hidden temple pavilion, learning centuries-old methods of mindfulness. Sightseeing Included: Nara Deer Park entry, Todai-ji Temple bronze Buddha tour, private zen tea ceremony."
                ),
                [
                    'Overnight Stay: Kyoto Heritage Centre (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Premium Matcha Dessert Tasting',
                ],
            ),
            _day(
                7,
                'BULLET TRAIN TRANSIT TO HISTORIC HIROSHIMA',
                (
                    'Check out as you board the Shinkansen Bullet Train heading west to Hiroshima. Upon arrival, take a peaceful private ferry to Miyajima Island to view the majestic Itsukushima Shrine and its iconic floating torii gate standing inside the sea water. Return to the city core to view the profound Hiroshima Peace Memorial Park and Genbaku Dome. Sightseeing Included: Miyajima Island private ferry, Itsukushima floating torii gate trail, Peace Memorial Park & Museum. Logistics Highlight: TRAGUIN luggage forwarding services handle your heavy bags directly from Kyoto to Osaka.'
                ),
                [
                    'Overnight Stay: Hiroshima Centre (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Local Hiroshima-style Okonomiyaki Dinner',
                ],
            ),
            _day(
                8,
                'TRANSIT TO DYNAMIC OSAKA & DOTONBORI GALA',
                (
                    'Board the morning bullet train back to the dynamic commercial capital of Osaka. Check into your premium hotel and spend a vibrant evening exploring the glowing neon-lined canal walkways of Dotonbori, photographing the iconic Glico Man banner—a premier popular Instagram location—and enjoying an executive family dinner party. Sightseeing Included: Shinkansen transit to Osaka, Dotonbori neon district orientation walk.'
                ),
                [
                    'Overnight Stay: Osaka Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Local Osaka Gourmet Feast',
                ],
            ),
            _day(
                9,
                'UNIVERSAL STUDIOS JAPAN FULL-DAY EXPRESS IMMERSION',
                (
                    'A thrilling day for the entire family. Enter Universal Studios Japan with pre-arranged express passes to minimize all lines. Explore Super Nintendo World, race inside Mario Kart tracks, and experience the Wizarding World of Harry Potter. This highly engaging theme kingdom delivers endless smiles and unforgettable memories. Sightseeing Included: Universal Studios Japan admission tickets, Express priority passes.'
                ),
                [
                    'Overnight Stay: Osaka Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & Theme Park Dine-around Vouchers',
                ],
            ),
            _day(
                10,
                'SAMURAI CASTLE HERITAGE & GRAND FAREWELL FEAST',
                (
                    'Tour the monumental Osaka Castle park with your private historian guide, gaining exclusive entry into the top tower viewpoints. Spend a free afternoon shopping for high-end electronics in Umeda or picking up unique souvenirs. Celebrate your final evening with a grand farewell dinner party at a historic garden terrace restaurant, sealing unforgettable memories. Sightseeing Included: Osaka Castle tower private entry, Umeda district luxury retail exploration. Evening Experience: Grand farewell family culinary feast with local cultural performances.'
                ),
                [
                    'Overnight Stay: Osaka Centre (Handpicked Premium Family Hotel)',
                    'Meals Included: International Breakfast & A5 Hida Wagyu Farewell Dinner Celebration',
                ],
            ),
            _day(
                11,
                'HIGH-END TRANSIT & KANSAI DEPARTURE',
                (
                    'Savor a luxurious final breakfast, enjoying the city skyline view blocks. Our corporate concierge assistants handle your seamless checkout and manage all group luggage logistics smoothly. Your private luxury van transfers your family comfortably to Osaka Kansai International Airport for your departure flight, concluding your epic grand panoramic vacation. Transfers: Private luxury van airport departure transit, priority luggage coordination.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Keio Plaza Hotel Tokyo / The Thousand Kyoto Hakone Yumoto Onsen / Sheraton Hiroshima Cross Hotel Osaka',
                'Multi-city Japan',
                '10N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Keio Plaza Hotel Tokyo / The Thousand Kyoto Hakone Yumoto Onsen / Sheraton Hiroshima Cross Hotel Osaka',
            ),
            _hotel(
                'Cerulean Tower Tokyu / Kyoto Tokyu Hotel Hakone Ten-yu / Ana Crowne Plaza Swissotel Nankai Osaka',
                'Multi-city Japan',
                '10N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Cerulean Tower Tokyu / Kyoto Tokyu Hotel Hakone Ten-yu / Ana Crowne Plaza Swissotel Nankai Osaka',
            ),
            _hotel(
                'The Capitol Hotel Tokyu / Ritz- Carlton Kyoto Gora Kadan Ryokan / Hilton Hiroshima W Osaka',
                'Multi-city Japan',
                '10N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Capitol Hotel Tokyu / Ritz- Carlton Kyoto Gora Kadan Ryokan / Hilton Hiroshima W Osaka',
            ),
            _hotel(
                'Aman Tokyo / Aman Kyoto Hoshinoya Fuji / Kihiro RyokanSt. Regis Osaka',
                'Multi-city Japan',
                '10N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Aman Tokyo / Aman Kyoto Hoshinoya Fuji / Kihiro RyokanSt. Regis Osaka',
            )
        ],
        inclusions=[
            _inc_included('Regional Bullet Rail: Continuous First-Class Shinkansen Bullet Train tickets across all regional sectors', 1),
            _inc_included('Regional Bullet Rail: Continuous First-Class Shinkansen Bullet Train tickets across all regional sectors', 2),
            _inc_excluded('International flight tickets and Japan entry Visa processing fees', 3),
            _inc_excluded('Personal expenses, hotel room service laundry bills, mini-bar billing', 4),
            _inc_excluded('Tipping, porterage fees, or optional sightseeing excursions not mentioned in the flow', 5),
        ],
    )
    return package, itinerary

JAPAN_JP_001_005_BUILDERS = [
    build_jp_001,
    build_jp_002,
    build_jp_003,
    build_jp_004,
    build_jp_005,
]
