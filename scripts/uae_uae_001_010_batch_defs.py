"""Builder functions for UAE-001 through UAE-010 UAE international packages."""

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

UAE_SLUG = "uae"


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


def build_uae_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-001'
    tour_code = 'TRG-DXB-ESS-2026'
    title = 'Dubai Essentials Family Tour'
    duration = '04 Nights / 05 Days'
    slug = 'uae-001-dubai-essentials-family-tour'
    itin_slug = 'uae-001-dubai-essentials-itinerary'
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
            _ph('Serial code UAE-001 | TRAGUIN tour code TRG-DXB-ESS-2026', 1),
            _ph('Country: Dubai, UAE | Category: Best Dubai Family Tour Package', 2),
            _ph('Destinations: Dubai City', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dubai Essentials Family Tour',
        overview="Dubai • Burj Khalifa • Desert Safari • Palm Jumeirah • Global Village 04 Nights / 05 Days Classic Dubai Family Holiday SERIAL CODE: UAE-001 TRAGUIN TOUR CODE: TRG-DXB-ESS-2026 STATE / COUNTRY: Dubai / UAE CATEGORY: Best Dubai Family Tour Package DURATION: 04 Nights / 05 Days DESTINATIONS: Dubai City\n\nTOUR OVERVIEW\nDiscover the dazzling heights and golden dunes of Dubai with this TRAGUIN curated family itinerary. Designed for excitement and comfort, this Dubai Essentials package offers a flawless blend of futuristic city exploration and traditional desert adventure. Experience the best of Emirati hospitality with TRAGUIN's handpicked hotels and exclusive services. THE IMMERSIVE DUBAI FAMILY EXPERIENCE Dubai is a world-class playground for families, offering endless excitement for all ages. From the towering Burj Khalifa to the thrilling dunes of a desert safari, our curated experiences promise a premium Dubai experience. With TRAGUIN, you get professional support and exclusive experiences that redefine the family holiday. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='UAE-001 | Dubai Essentials Family Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Dubai package (UAE-001 / TRG-DXB-ESS-2026): Dubai City with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DUBAI', 1),
            _ih('Day 02: CITY TOUR & BURJ KHALIFA', 2),
            _ih('Day 03: DESERT SAFARI ADVENTURE', 3),
            _ih('Day 04: GLOBAL VILLAGE & LEISURE', 4),
            _ih('Day 05: DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DUBAI',
                (
                    'Arrive in dazzling Dubai. Your private TRAGUIN transfer will escort you to your handpicked hotel. Enjoy a relaxing evening overlooking the city’s stunning skyline.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'CITY TOUR & BURJ KHALIFA',
                (
                    "Explore the iconic attractions of Dubai. Visit the Burj Khalifa, the Dubai Mall, and Palm Jumeirah. This curated experience offers deep insights into Dubai's rapid development."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'DESERT SAFARI ADVENTURE',
                (
                    "Embark on a thrilling desert safari. Experience dune bashing, camel riding, and a traditional BBQ dinner under the stars—a highlight of TRAGUIN's exclusive packages."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'GLOBAL VILLAGE & LEISURE',
                (
                    'A full day of immersive fun at Global Village. Explore cultural pavilions, shopping, and entertainment, creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'DEPARTURE',
                (
                    'Enjoy a final family breakfast. Your private TRAGUIN chauffeur ensures a comfortable transfer to the airport.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Dubai City',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                1,
                description='OPTION 01 – DELUXE: TRAGUIN Handpicked Deluxe Property',
            ),
            _hotel(
                'TRAGUIN Handpicked Premium Property',
                'Dubai City',
                '4N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'Atlantis, The Palm / Address Downtown',
                'Multi-city UAE',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Atlantis, The Palm / Address Downtown',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Dubai City',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                5,
                4,
                description='OPTION 04 – ULTRA LUXURY: TRAGUIN Handpicked Ultra Luxury Property',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Dubai and the UAE', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-emirate transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and UAE visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_uae_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-002'
    tour_code = 'TRG-DXB-AUH-FAM-2026'
    title = 'Dubai Abu Dhabi Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'uae-002-dubai-abu-dhabi-family-tour'
    itin_slug = 'uae-002-dubai-abu-dhabi-itinerary'
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
            _ph('Serial code UAE-002 | TRAGUIN tour code TRG-DXB-AUH-FAM-2026', 1),
            _ph('Country: Dubai, UAE | Category: Best Dubai Abu Dhabi Family Tour Package', 2),
            _ph('Destinations: Dubai (3N) + Abu Dhabi', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
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
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dubai Abu Dhabi Family Tour',
        overview='Dubai • Abu Dhabi • Burj Khalifa • Sheikh Zayed Mosque • Ferrari World 05 Nights / 06 Days Classic UAE Family Holiday SERIAL CODE: UAE-002 TRAGUIN TOUR CODE: TRG-DXB-AUH-FAM-2026 STATE / COUNTRY: UAE CATEGORY: Best Dubai Abu Dhabi Family Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Dubai (3N) + Abu Dhabi (2N)\n\nTOUR OVERVIEW\nEmbark on an unforgettable UAE journey with our TRAGUIN curated family itinerary. Blending the futuristic pulse of Dubai with the cultural grandeur of Abu Dhabi, this Dubai Abu Dhabi family tour offers a seamless mix of excitement and heritage, ensuring unforgettable memories. THE IMMERSIVE UAE FAMILY EXPERIENCE Dubai and Abu Dhabi are premier destinations for families seeking innovation, luxury, and cultural depth. From the heights of the Burj Khalifa to the tranquility of the Sheikh Zayed Grand Mosque, this Dubai Abu Dhabi discovery delivers exclusive experiences. Let TRAGUIN transform your holiday with premium logistics and handpicked hotels. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='UAE-002 | Dubai Abu Dhabi Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Dubai package (UAE-002 / TRG-DXB-AUH-FAM-2026): Dubai (3N) + Abu Dhabi with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DUBAI', 1),
            _ih('Day 02: DUBAI CITY EXPLORATION', 2),
            _ih('Day 03: DESERT SAFARI & TRANSFER TO ABU DHABI', 3),
            _ih('Day 04: ABU DHABI CULTURAL IMMERSION', 4),
            _ih('Day 05: FERRARI WORLD & FAMILY THRILLS', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DUBAI',
                (
                    'Your TRAGUIN family tour begins with a VIP airport welcome. A private luxury van transfers you to your premium hotel. Enjoy a relaxing evening by the Dubai Marina, admiring the breathtaking landscapes of the illuminated city.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'DUBAI CITY EXPLORATION',
                (
                    "Explore the best of Dubai. Visit the iconic Burj Khalifa, The Dubai Mall, and Palm Jumeirah. This curated experience offers deep insights into Dubai's luxury living and iconic attractions."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'DESERT SAFARI & TRANSFER TO ABU DHABI',
                (
                    'Experience an adrenaline-filled desert safari before driving to Abu Dhabi. The scenic beauty of the shifting sands sets the stage for a memorable transition to the capital.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'ABU DHABI CULTURAL IMMERSION',
                (
                    'Visit the stunning Sheikh Zayed Grand Mosque and Louvre Abu Dhabi. This immersive experience brings together global art and breathtaking cultural beauty.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'FERRARI WORLD & FAMILY THRILLS',
                (
                    'A day of excitement at Ferrari World. Experience speed, luxury, and exclusive experiences designed for the whole family, leaving you with unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final breakfast before your TRAGUIN assisted transfer to the airport. Your classic Dubai Abu Dhabi tour concludes with lasting memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Dubai (3N) + Abu Dhabi',
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
                'Dubai (3N) + Abu Dhabi',
                '5N',
                'Premium',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                2,
                description='OPTION 02 – PREMIUM: TRAGUIN Handpicked Premium Property',
            ),
            _hotel(
                'Atlantis, The Palm / Address Emirates Palace / St. Regis',
                'Multi-city UAE',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — Atlantis, The Palm / Address Emirates Palace / St. Regis',
            ),
            _hotel(
                'TRAGUIN Handpicked Ultra Luxury Property',
                'Dubai (3N) + Abu Dhabi',
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
            _inc_included('Premium handpicked accommodation across Dubai and the UAE', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-emirate transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and UAE visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_uae_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-003'
    tour_code = 'TRG-DXB-ROM-2026'
    title = 'Romantic Dubai Honeymoon'
    duration = '05 Nights / 06 Days'
    slug = 'uae-003-romantic-dubai-honeymoon'
    itin_slug = 'uae-003-romantic-dubai-honeymoon-itinerary'
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
            _ph('Serial code UAE-003 | TRAGUIN tour code TRG-DXB-ROM-2026', 1),
            _ph('Country: Dubai, UAE | Category: Best Dubai Honeymoon Package', 2),
            _ph('Destinations: Dubai City & Desert', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Honeymoon', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Romantic Dubai Honeymoon',
        overview='Dubai • Burj Khalifa • Desert Safari • Palm Jumeirah • Yacht Cruise 05 Nights / 06 Days Ultra-Luxury Honeymoon Retreat SERIAL CODE: UAE-003 TRAGUIN TOUR CODE: TRG-DXB-ROM-2026 STATE / COUNTRY: Dubai / UAE CATEGORY: Best Dubai Honeymoon Package DURATION: 05 Nights / 06 Days DESTINATIONS: Dubai City & Desert Sanctuary\n\nTOUR OVERVIEW\nBegin your life together in the golden city of dreams with this TRAGUIN curated honeymoon. From private yacht sunsets to intimate desert dining, this romantic Dubai holiday promises unforgettable memories, breathtaking landscapes, and exclusive experiences. We ensure every moment is as special as your love story.\n\nWHY CHOOSE OUR ROMANTIC DUBAI HONEYMOON?\nDubai is the ultimate sanctuary for couples, blending urban grandeur with desert mystique. Our curated experiences provide a seamless balance of luxury and romance. With TRAGUIN, enjoy handpicked hotels, private transfers, and a truly premium Dubai experience. Discover the iconic attractions that make Dubai a dream destination. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='UAE-003 | Romantic Dubai Honeymoon | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Dubai package (UAE-003 / TRG-DXB-ROM-2026): Dubai City & Desert with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DUBAI', 1),
            _ih('Day 02: CITY LUXURY & BURJ KHALIFA', 2),
            _ih('Day 03: DESERT ROMANCE', 3),
            _ih('Day 04: YACHT CRUISE & RELAXATION', 4),
            _ih('Day 05: LEISURE & SPA', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DUBAI',
                (
                    'A romantic welcome to the City of Gold. Your private TRAGUIN transfer will escort you to your handpicked hotel. Enjoy a quiet evening admiring the scenic beauty of the Dubai Marina.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'CITY LUXURY & BURJ KHALIFA',
                (
                    "Explore the heights of luxury. Visit the Burj Khalifa and indulge in high-end shopping at the Dubai Mall. A curated experience to admire the city's iconic attractions."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'DESERT ROMANCE',
                (
                    'Experience an intimate desert safari. Enjoy dune bashing, camel rides, and a private BBQ dinner under the stars—an exclusive experience for couples seeking breathtaking landscapes.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'YACHT CRUISE & RELAXATION',
                (
                    'A private sunset yacht cruise, offering scenic beauty of the Dubai skyline. Spend your day enjoying premium stays and relaxation in the lap of luxury.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'LEISURE & SPA',
                (
                    'Indulge in a couple’s spa retreat. Reflect on your unforgettable memories in Dubai with an evening at a world-class restaurant.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final breakfast and souvenir shopping before your TRAGUIN assisted transfer, concluding your premium Dubai experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Dubai City & Desert',
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
                'Dubai City & Desert',
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
                'Dubai City & Desert',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'Burj Al Arab / Atlantis, The Palm',
                'Multi-city UAE',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Burj Al Arab / Atlantis, The Palm',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Dubai and the UAE', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-emirate transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and UAE visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_uae_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-004'
    tour_code = 'TRG-DXB-LUX-2026'
    title = 'Luxury Dubai Tour'
    duration = '06 Nights / 07 Days'
    slug = 'uae-004-luxury-dubai-tour'
    itin_slug = 'uae-004-luxury-dubai-itinerary'
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
            _ph('Serial code UAE-004 | TRAGUIN tour code TRG-DXB-LUX-2026', 1),
            _ph('Country: Dubai, UAE | Category: Best Dubai Luxury Tour Package', 2),
            _ph('Destinations: Dubai', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Luxury Dubai Tour',
        overview='06 Nights / 07 Days Ultimate Luxury Dubai Discovery SERIAL CODE: UAE-004 TRAGUIN TOUR CODE: TRG-DXB-LUX-2026 STATE / COUNTRY: Dubai / UAE CATEGORY: Best Dubai Luxury Tour Package DURATION: 06 Nights / 07 Days DESTINATIONS: Dubai\n\nTOUR OVERVIEW\nIndulge in the zenith of opulence with our TRAGUIN curated luxury Dubai escape. Designed for the discerning traveler, this luxury Dubai holiday blends futuristic metropolitan glamour with serene coastal sanctuaries. Experience exclusive experiences, stay at handpicked hotels, and build unforgettable memories.\n\nWHY CHOOSE OUR LUXURY DUBAI EXPERIENCE?\nDubai is a global beacon of luxury and innovation, offering a lifestyle of sheer sophistication. Our curated experiences ensure your journey is unmatched. With TRAGUIN, enjoy exclusive experiences, private yacht charters, and premium stays that define a premium Dubai experience. Discover the iconic attractions that make Dubai a dream destination. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='UAE-004 | Luxury Dubai Tour | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Dubai package (UAE-004 / TRG-DXB-LUX-2026): Dubai with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DUBAI', 1),
            _ih('Day 02: METROPOLITAN LUXURY', 2),
            _ih('Day 03: DESERT OAK OASIS', 3),
            _ih('Day 04: PRIVATE YACHT CRUISE', 4),
            _ih('Day 05: PALM JUMEIRAH RETREAT', 5),
            _ih('Day 06: CULTURE & HERITAGE', 6),
            _ih('Day 07: DEPARTURE', 7)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DUBAI',
                (
                    'Your TRAGUIN luxury escape begins with a VIP chauffeur service. Experience true opulence from the moment you land, followed by a private transfer to your handpicked hotel.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'METROPOLITAN LUXURY',
                (
                    "Visit the iconic Burj Khalifa and experience top-tier luxury shopping at the Dubai Mall. A curated experience to admire the city's breathtaking landscapes."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'DESERT OAK OASIS',
                (
                    'A private desert oasis experience. Indulge in exclusive experiences like a private falconry display and a gourmet dinner under the stars amidst breathtaking landscapes.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'PRIVATE YACHT CRUISE',
                (
                    'Savor the scenic beauty of the Dubai skyline with a private luxury yacht cruise. An immersive experience that defines our premium stays in Dubai.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'PALM JUMEIRAH RETREAT',
                (
                    'Relax at an iconic attraction—the Palm Jumeirah. Enjoy a spa day and world-class dining, creating unforgettable memories in ultimate luxury.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'CULTURE & HERITAGE',
                (
                    'Discover old Dubai and the gold souks. This immersive experience contrasts with the modern city, showcasing the rich history of a premium Dubai experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                7,
                'DEPARTURE',
                (
                    'Final luxury breakfast before your TRAGUIN chauffeur transfer, concluding your luxury Dubai holiday.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Dubai',
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
                'Dubai',
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
                'Dubai',
                '6N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'Burj Al Arab / Armani Hotel',
                'Multi-city UAE',
                '6N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Burj Al Arab / Armani Hotel',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Dubai and the UAE', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-emirate transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and UAE visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_uae_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-005'
    tour_code = 'TRG-DXB-DSF-2026'
    title = 'Dubai Shopping Festival Tour'
    duration = '05 Nights / 06 Days'
    slug = 'uae-005-dubai-shopping-festival-tour'
    itin_slug = 'uae-005-dubai-shopping-festival-itinerary'
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
            _ph('Serial code UAE-005 | TRAGUIN tour code TRG-DXB-DSF-2026', 1),
            _ph('Country: Dubai, UAE | Category: Female Only Shopping Festival Tour', 2),
            _ph('Destinations: Dubai', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dubai Shopping Festival Tour',
        overview="Dubai • DSF Shopping • Global Village • Luxury Boutiques • Girls' Retreat 05 Nights / 06 Days Exclusive Female-Only Shopping Escape SERIAL CODE: UAE-005 TRAGUIN TOUR CODE: TRG-DXB-DSF-2026 STATE / COUNTRY: Dubai / UAE CATEGORY: Female Only Shopping Festival Tour DURATION: 05 Nights / 06 Days DESTINATIONS: Dubai\n\nTOUR OVERVIEW\nCelebrate the world's most spectacular retail event with this TRAGUIN curated female-only shopping escape. Designed for fashion enthusiasts, this Dubai Shopping Festival (DSF) tour combines high-fashion luxury with the cultural magic of Dubai, promising unforgettable memories, breathtaking landscapes, and exclusive experiences.\n\nWHY CHOOSE OUR DUBAI SHOPPING FESTIVAL TOUR?\nDubai during the Shopping Festival is a global icon of style and savings. Our curated experiences provide a seamless balance of high-street luxury and cultural exploration. With TRAGUIN, enjoy exclusive experiences, private shopper assistance, and premium stays that define a premium Dubai experience. Discover the iconic attractions that make Dubai the ultimate shopping destination. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='UAE-005 | Dubai Shopping Festival Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Dubai package (UAE-005 / TRG-DXB-DSF-2026): Dubai with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DUBAI', 1),
            _ih('Day 02: DSF RETAIL EXTRAVAGANZA', 2),
            _ih('Day 03: GLOBAL VILLAGE & CULTURE', 3),
            _ih('Day 04: GOLD SOUK & SPA RETREAT', 4),
            _ih('Day 05: SUNSET YACHT & GALA DINNER', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DUBAI',
                (
                    'A glamorous welcome to the City of Gold. Your private TRAGUIN transfer escorts you to your handpicked hotel. Enjoy a relaxing evening at a chic lounge, admiring the scenic beauty of the city skyline.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'DSF RETAIL EXTRAVAGANZA',
                (
                    'A full day dedicated to the Dubai Shopping Festival! Explore mega-malls, luxury boutiques, and designer flagships. A curated experience to satisfy every fashion desire with our professional shopping concierge.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'GLOBAL VILLAGE & CULTURE',
                (
                    'Visit the vibrant Global Village. Explore cultural pavilions, international shopping, and exclusive experiences. Immerse yourself in the iconic attractions and global flair.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'GOLD SOUK & SPA RETREAT',
                (
                    'Discover the dazzling Gold Souk for exquisite jewelry, followed by a luxury spa afternoon. The perfect mix of scenic beauty and premium stays for complete rejuvenation.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'SUNSET YACHT & GALA DINNER',
                (
                    'A private sunset yacht cruise, offering breathtaking landscapes and a grand finale celebration dinner—an exclusive experience for lasting unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Final shopping and gourmet breakfast before your TRAGUIN assisted transfer, concluding your premium Dubai experience.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Dubai',
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
                'Dubai',
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
                'Dubai',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'Address Fountain Views / Palace Downtown',
                'Multi-city UAE',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Address Fountain Views / Palace Downtown',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Dubai and the UAE', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-emirate transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and UAE visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_uae_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-006'
    tour_code = 'TRG-DXB-DLX-2026'
    title = 'Dubai Family Tour'
    duration = '05 Nights / 06 Days'
    slug = 'uae-006-dubai-family-tour'
    itin_slug = 'uae-006-dubai-family-itinerary'
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
            _ph('Serial code UAE-006 | TRAGUIN tour code TRG-DXB-DLX-2026', 1),
            _ph('Country: Dubai, UAE | Category: Best Dubai Family Tour Package', 2),
            _ph('Destinations: Dubai City', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Family', 'Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dubai Family Tour',
        overview="05 Nights / 06 Days Classic Dubai Family Holiday SERIAL CODE: UAE-006 TRAGUIN TOUR CODE: TRG-DXB-DLX-2026 STATE / COUNTRY: Dubai / UAE CATEGORY: Best Dubai Family Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Dubai City\n\nTOUR OVERVIEW\nDiscover the dazzling heights and golden dunes of Dubai with this TRAGUIN curated family itinerary. Designed for excitement and comfort, this Dubai Deluxe package offers a flawless blend of futuristic city exploration and traditional desert adventure. Experience the best of Emirati hospitality with TRAGUIN's handpicked hotels and exclusive services, creating unforgettable memories. THE IMMERSIVE DUBAI FAMILY EXPERIENCE Dubai is a world-class playground for families, offering endless excitement for all ages. From the towering Burj Khalifa to the thrilling dunes of a desert safari, our curated experiences promise a premium Dubai experience. With TRAGUIN, you get professional support and exclusive experiences that redefine the family holiday. Discover the iconic attractions that make Dubai a dream destination. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='UAE-006 | Dubai Family Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Dubai package (UAE-006 / TRG-DXB-DLX-2026): Dubai City with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DUBAI', 1),
            _ih('Day 02: CITY TOUR & BURJ KHALIFA', 2),
            _ih('Day 03: DESERT SAFARI ADVENTURE', 3),
            _ih('Day 04: GLOBAL VILLAGE & LEISURE', 4),
            _ih('Day 05: AQUATIC FUN', 5),
            _ih('Day 06: DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DUBAI',
                (
                    'Arrive in dazzling Dubai. Your private TRAGUIN transfer will escort you to your handpicked hotel. Enjoy a relaxing evening overlooking the city’s stunning skyline.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                2,
                'CITY TOUR & BURJ KHALIFA',
                (
                    "Explore the iconic attractions of Dubai. Visit the Burj Khalifa, the Dubai Mall, and Palm Jumeirah. This curated experience offers deep insights into Dubai's luxury living and iconic attractions."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                3,
                'DESERT SAFARI ADVENTURE',
                (
                    "Embark on a thrilling desert safari. Experience dune bashing, camel rides, and a traditional BBQ dinner under the stars—a highlight of TRAGUIN's exclusive packages."
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                4,
                'GLOBAL VILLAGE & LEISURE',
                (
                    'A full day of immersive fun at Global Village. Explore cultural pavilions, shopping, and entertainment, creating unforgettable memories.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                5,
                'AQUATIC FUN',
                (
                    'Spend a day enjoying breathtaking landscapes at a premier water park. Experience exclusive experiences that define our luxury family holiday.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            ),
            _day(
                6,
                'DEPARTURE',
                (
                    'Enjoy a final family breakfast. Your private TRAGUIN chauffeur ensures a comfortable transfer to the airport.'
                ),
                [
                    'Full day as per curated TRAGUIN itinerary.',
                ],
            )
        ],
        hotels=[
            _hotel(
                'TRAGUIN Handpicked Deluxe Property',
                'Dubai City',
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
                'Dubai City',
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
                'Dubai City',
                '5N',
                'Luxury',
                'Deluxe Room',
                'MAPAI (Breakfast & Dinner)',
                4,
                3,
                description='OPTION 03 – LUXURY: TRAGUIN Handpicked Luxury Property',
            ),
            _hotel(
                'Atlantis, The Palm / Address Downtown',
                'Multi-city UAE',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Atlantis, The Palm / Address Downtown',
            )
        ],
        inclusions=[
            _inc_included('Premium handpicked accommodation across Dubai and the UAE', 1),
            _inc_included('Private luxury airport transfers and dedicated chauffeur-driven executive van', 2),
            _inc_included('Inter-emirate transfers and curated sightseeing as per itinerary', 3),
            _inc_included('TRAGUIN 24/7 dedicated on-ground concierge support', 4),
            _inc_excluded('International airfare and UAE visa fees', 5),
            _inc_excluded('Personal expenses, laundry, room service, and mini-bar charges', 6),
            _inc_excluded('Optional sightseeing excursions not specified in the itinerary', 7),
            _inc_excluded('Tipping, porterage fees, and travel insurance', 8),
        ],
    )
    return package, itinerary

def build_uae_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-007'
    tour_code = 'TRG-DXB-SEN-2026'
    title = 'Leisure Dubai Senior Tour'
    duration = '05 Nights / 06 Days'
    slug = 'uae-007-leisure-dubai-senior-tour'
    itin_slug = 'uae-007-leisure-dubai-senior-itinerary'
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
            _ph('Serial code UAE-007 | TRAGUIN tour code TRG-DXB-SEN-2026', 1),
            _ph('Country: Dubai, UAE | Category: Best Dubai Senior Citizen Tour Package', 2),
            _ph('Destinations: Leisure Dubai', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Leisure Dubai Senior Tour',
        overview="Dubai City • Burj Khalifa • Palm Monorail • Al Fahidi Heritage • Miracle Garden 05 Nights / 06 Days Optimized Senior Citizen Leisure Vacation SERIAL CODE: UAE-007 TRAGUIN TOUR CODE: TRG-DXB-SEN-2026 STATE / COUNTRY: Dubai / UAE CATEGORY: Best Dubai Senior Citizen Tour Package DURATION: 05 Nights / 06 Days DESTINATIONS: Leisure Dubai Exploration\n\nTOUR OVERVIEW\nWelcome to an exceptional, slowly paced exploration of the emirate designed by TRAGUIN Experts for senior travelers who prioritize ease of mobility, premium comfort, and enriching cultural immersion. This exclusive Leisure Dubai itinerary carefully minimizes unnecessary walking, avoids peak daytime heat, and handles all logistical details seamlessly, ensuring a compilation of unforgettable memories. Welcome Note from TRAGUIN: We understand that true luxury lies in comfort and care. Your tour features private executive transport, skip-the-line entries, step-free access routes, and highly rated culinary experiences backed by our 24/7 on-ground customer support.\n\nWHY CHOOSE OUR LEISURE DUBAI SENIOR ITINERARY?\nDubai is an elite destination offering total accessibility, world-renowned hospitality, and mesmerizing cityscapes. Booking our signature Dubai Senior Citizen Tour Package ensures your family experiences premium leisure without fatigue. This itinerary features targeted travel keywords for Google ranking, showcasing premier Dubai Sightseeing elements at a relaxed pace. Uncover the city's iconic attractions: experience breathtaking views from the top of Burj Khalifa via prioritized elevators, relax along the scenic walkways of Dubai Marina, glide over pristine waters on a private Creek Abra cruise, and stroll through the flat paths of the Dubai Miracle Garden. It is the absolute Best Time to Visit Dubai to capture stunning photographs, experience immersive experiences, and indulge in a truly rewarding Premium Dubai Experience. THE DEFINITIVE DAY-WISE ITINERARY",
        seo_title='UAE-007 | Leisure Dubai Senior Tour | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Dubai package (UAE-007 / TRG-DXB-SEN-2026): Leisure Dubai with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DUBAI & MARINA WALKWAY', 1),
            _ih('Day 02: MODERN CITY ICONS & PRIORITY BURJ KHALIFA', 2),
            _ih('Day 03: SCENIC PALM MONORAIL EXPEDITION', 3),
            _ih('Day 04: COMFORT HERITAGE SOJOURN & CREEK CRUISE', 4),
            _ih('Day 05: DUBAI MIRACLE GARDEN & GLOBAL VILLAGE', 5),
            _ih('Day 06: FAREWELL DUBAI DEPARTURE', 6)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DUBAI & MARINA WALKWAY',
                (
                    'Arrive in Dubai to a warm VIP greeting inside the terminal. Your private TRAGUIN chauffeur-driven executive van will comfortably escort you to your hotel. After checking in, enjoy a peaceful, gentle evening stroll along the wide, flat wooden promenades of Dubai Marina, soaking in the gentle ocean breeze and coastal city lights. Sightseeing Included: VIP Airport logistics, Dubai Marina orientation stroll. Evening Experience: Relaxed waterfront dinner at a premium accessible restaurant.'
                ),
                [
                    'Overnight Stay: Dubai City (Handpicked Senior-Friendly Hotel)',
                    'Meals Included: International Welcome Buffet Dinner',
                ],
            ),
            _day(
                2,
                'MODERN CITY ICONS & PRIORITY BURJ KHALIFA',
                (
                    "Enjoy a leisurely breakfast before heading out. Today, explore the modern architectural wonders of New Dubai. Your private vehicle transfers you directly to the Dubai Mall entrance. Utilizing our pre-booked Fast- Track Priority Passes, bypass all standard queues to scale the world's tallest tower, the Burj Khalifa, up to Levels 124/125. Take in the breathtaking landscapes in complete comfort. Sightseeing Included: Burj Khalifa Level 124/125 entry, Mall accessible fountain paths. Evening Experience: Reserved terrace seating for the spectacular Dubai Fountain Light Show over refreshments."
                ),
                [
                    'Overnight Stay: Dubai City (Handpicked Senior-Friendly Hotel)',
                    'Meals Included: International Breakfast & Premium View Terrace Dinner',
                ],
            ),
            _day(
                3,
                'SCENIC PALM MONORAIL EXPEDITION',
                (
                    "ELEVATED TRANSITS – SPECTACULAR MAN-MADE HORIZONS A relaxing morning drive brings you to the gateway station of Palm Jumeirah. Board the fully automated, panoramic Palm Monorail for a scenic journey high above the island's tree spine. Admire luxury villas and coastal waters from your climate-controlled cabin with zero walking fatigue. Arrive at the iconic Atlantis area to explore flat avenues and relax at beachfront cafés. Sightseeing Included: Palm Monorail panoramic tickets, Atlantis waterfront exploration."
                ),
                [
                    'Overnight Stay: Dubai City (Handpicked Senior-Friendly Hotel)',
                    'Meals Included: International Breakfast & Casual Seaside Lunch',
                ],
            ),
            _day(
                4,
                'COMFORT HERITAGE SOJOURN & CREEK CRUISE',
                (
                    'Delve into the historic soul of old Dubai. Visit the beautifully preserved Al Fahidi Cultural Quarter, enjoying flat, shaded lanes that reflect historical wind-tower living. Later, board a stable, private traditional wooden Abra ferry boat chartered exclusively by TRAGUIN for a smooth cruise across Dubai Creek, exploring spice markets and old-world gold souks at an easy pace. Sightseeing Included: Al Fahidi historic quarter walk, private chartered Abra cruise, Old Souks trail.'
                ),
                [
                    'Overnight Stay: Dubai City (Handpicked Senior-Friendly Hotel)',
                    'Meals Included: International Breakfast & Traditional Heritage Lunch',
                ],
            ),
            _day(
                5,
                'DUBAI MIRACLE GARDEN & GLOBAL VILLAGE',
                (
                    'Explore the breathtaking floral structures inside the Dubai Miracle Garden, moving smoothly along wide, well- paved, step-free networks with plenty of seating spaces. In the evening, visit the vibrant Global Village to discover cultural pavilions, international crafts, and evening theatrical performances, celebrating with a beautiful grand finale dinner party. Sightseeing Included: Miracle Garden flower tickets, Global Village evening pavilion passes.'
                ),
                [
                    'Overnight Stay: Dubai City (Handpicked Senior-Friendly Hotel)',
                    'Meals Included: International Breakfast & Grand Farewell Dinner',
                ],
            ),
            _day(
                6,
                'FAREWELL DUBAI DEPARTURE',
                (
                    'Savor your final morning breakfast at your leisure. Our concierge team takes full care of your luggage logistics and smooth checkout. Your private vehicle transfers you smoothly to Dubai International Airport for your return flight, concluding a flawless premium holiday. Transfers: Private luxury van departure transfer, comprehensive luggage assistance.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'JW Marriott Marquis Dubai Excellent layout, minimized hallway walks.',
                'Multi-city UAE',
                '5N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — JW Marriott Marquis Dubai Excellent layout, minimized hallway walks.',
            ),
            _hotel(
                'Taj Dubai Downtown Priority elevator blocks for elderly guests.',
                'Multi-city UAE',
                '5N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Taj Dubai Downtown Priority elevator blocks for elderly guests.',
            ),
            _hotel(
                'The Palace Downtown Dubai Direct flat surface step-free access to fountains.',
                'Multi-city UAE',
                '5N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Palace Downtown Dubai Direct flat surface step-free access to fountains.',
            ),
            _hotel(
                'Armani Hotel Dubai (Burj Khalifa)24/7 dedicated personal butler concierge care.',
                'Multi-city UAE',
                '5N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Armani Hotel Dubai (Burj Khalifa)24/7 dedicated personal butler concierge care.',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: 05 Nights stay in senior-optimized luxury rooms', 1),
            _inc_included('Meals: Bountiful breakfasts and daily comfort-first multi-cuisine dinners', 2),
            _inc_included('Transfers: All ground logistics in Private Luxury Executive AC Vans', 3),
            _inc_included('Sightseeing: Skip-the-line VIP entries for Burj Khalifa & attractions', 4),
            _inc_included('TRAGUIN Support: 24/7 dedicated medical concierge assistance and local guide', 5),
            _inc_included('Accommodation: 05 Nights stay in senior-optimized luxury rooms', 6),
            _inc_included('Meals: Bountiful breakfasts and daily comfort-first multi-cuisine dinners', 7),
            _inc_included('Transfers: All ground logistics in Private Luxury Executive AC Vans', 8),
            _inc_included('Sightseeing: Skip-the-line VIP entries for Burj Khalifa & attractions', 9),
            _inc_included('TRAGUIN Support: 24/7 dedicated medical concierge assistance and local guide', 10),
            _inc_excluded('Flights & Travel Insurance fees', 11),
            _inc_excluded('Personal expenses, laundry, telephone calls', 12),
            _inc_excluded('Tipping, porterage, or optional entry tours not specified', 13),
            _inc_excluded('Flights & Travel Insurance fees', 14),
            _inc_excluded('Personal expenses, laundry, telephone calls', 15),
            _inc_excluded('Tipping, porterage, or optional entry tours not specified', 16),
        ],
    )
    return package, itinerary

def build_uae_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-008'
    tour_code = 'TRG-DXB-ADV-2026'
    title = 'Dubai Desert Adventure'
    duration = '04 Nights / 05 Days'
    slug = 'uae-008-dubai-desert-adventure-tour'
    itin_slug = 'uae-008-dubai-desert-adventure-itinerary'
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
            _ph('Serial code UAE-008 | TRAGUIN tour code TRG-DXB-ADV-2026', 1),
            _ph('Country: Dubai, UAE | Category: Luxury Desert Adventure Holiday', 2),
            _ph('Destinations: Red Dunes Dune Bashing • Quad Biking • Skydive Dubai • Desert Safari Night', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Desert', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Dubai Desert Adventure',
        overview="04 Nights / 05 Days High-Octane Luxury Adventure Expedition SERIAL CODE: UAE-008 TRAGUIN TOUR CODE: TRG-DXB-ADV-2026 STATE / COUNTRY: Dubai / UAE CATEGORY: Luxury Desert Adventure Holiday DURATION: 04 Nights / 05 Days Dubai City & Red Dunes Sanctuary\n\nTOUR OVERVIEW\nUnleash your adrenaline with this high-octane TRAGUIN curated adventure. Designed specifically for thrill- seekers, this Dubai Desert Adventure merges the cutting-edge extreme sports of the city with the raw beauty of Lahbab's red dunes. Experience exclusive experiences, enjoy premium stays, and walk away with absolute unforgettable memories. Adventure Note from TRAGUIN: Thrill requires precision. Your expedition is operated under professional guidelines, featuring high-powered customized 4x4 vehicles, certified instructors, private transfers, and unique desert stays with 24/7 on-ground assistance.\n\nWHY CHOOSE OUR DUBAI ADVENTURE & DESERT PACKAGE?\nDubai is a dynamic global capital for thrill-seekers, balancing legendary sand sports with record-breaking extreme athletics. Booking our signature Dubai Adventure Tour Package guarantees action-packed discovery. This itinerary features targeted travel keywords for Google ranking, showcasing premier Dubai Sightseeing and extreme landmarks. Explore the iconic attractions: experience high-powered quad biking across steep sands, sandboarding down monolithic dunes, skydiving options over Palm Jumeirah, and immersive overnight stargazing inside luxury desert camps. It is the absolute Best Time to Visit Dubai to capture breathtaking landscapes, experience thrilling immersive experiences, and indulge in an unmatched Premium Dubai Experience. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='UAE-008 | Dubai Desert Adventure | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Dubai package (UAE-008 / TRG-DXB-ADV-2026): Red Dunes Dune Bashing • Quad Biking • Skydive Dubai • Desert Safari Night with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DUBAI & JET CAR THRILL', 1),
            _ih('Day 02: DEEP DESERT EXPLORATION & QUAD BIKING', 2),
            _ih('Day 03: HOT AIR BALLOON SUNRISE & SKYDIVING OPTION', 3),
            _ih('Day 04: DEEP DIVE DUBAI & HELICOPTER FLIGHT', 4),
            _ih('Day 05: SOUVENIR TRACKS & DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DUBAI & JET CAR THRILL',
                (
                    "Arrive in Dubai to a premium welcome. Your private TRAGUIN chauffeur transfers you to your city hotel. In the afternoon, dive straight into action with an adrenaline-pumping Water Jet Car ride at Dubai Marina, speeding through ocean waves alongside magnificent yachts, experiencing the city's scenic beauty from the water. Sightseeing Included: Private executive airport transit, Marina Water Jet Car thrill ride. Evening Experience: Trendy high-energy dinner party at an upscale marina restaurant."
                ),
                [
                    'Overnight Stay: Dubai Marina (Handpicked Premium Action-Hub Hotel)',
                    'Meals Included: Welcome Gala Dinner',
                ],
            ),
            _day(
                2,
                'DEEP DESERT EXPLORATION & QUAD BIKING',
                (
                    "Fuel up with breakfast before heading into the vast expanse of Lahbab's famous red dunes. Board a high- powered 400cc Quad Bike or Dune Buggy for a rugged off-road self-drive adventure across massive sand crests. Later, experience an intense session of sandboarding down vertical slopes, capturing breathtaking landscapes. Sightseeing Included: Lahbab red dunes transit, high-powered quad biking trail, sandboarding. Evening Experience: Private desert camp sunset views with a live fire show and traditional BBQ."
                ),
                [
                    'Overnight Stay: Lahbab Desert Sanctuary (Luxury Air-Conditioned Bedouin Glamping Dome)',
                    'Meals Included: Breakfast & Live Flame Desert Grill Dinner',
                ],
            ),
            _day(
                3,
                'HOT AIR BALLOON SUNRISE & SKYDIVING OPTION',
                (
                    "An early morning wake-up call leads to an incredible sunrise Hot Air Balloon ride floating 4,000 feet above the desert, observing wild oryx roaming below. In the afternoon, return to the city for a heart-stopping optional Skydive over the Palm Jumeirah or a high-speed zipline ride through Dubai Marina's high-rises. Sightseeing Included: Sunrise hot air balloon flight, private return city transit tracks. Optional Activities: Skydive Dubai Palm Jumeirah jump or XLine Marina Zipline flight."
                ),
                [
                    'Overnight Stay: Dubai City Centre (Premium Stay)',
                    'Meals Included: Gourmet Desert Breakfast & City Centre Dinner',
                ],
            ),
            _day(
                4,
                'DEEP DIVE DUBAI & HELICOPTER FLIGHT',
                (
                    "Discover the world's deepest pool at Deep Dive Dubai, exploring a sunken underwater city at a depth of up to 60 meters under professional guidance. In the evening, ascend skyward for a private helicopter tour over the city's futuristic architecture, taking in the scenic beauty of Burj Khalifa and Palm Jumeirah from above. Sightseeing Included: Deep Dive Dubai exploration, private helicopter flight over city skyline."
                ),
                [
                    'Overnight Stay: Dubai City Centre (Premium Stay)',
                    'Meals Included: Breakfast & Farewell Premium Dining Event',
                ],
            ),
            _day(
                5,
                'SOUVENIR TRACKS & DEPARTURE',
                (
                    'Enjoy a hearty breakfast, reviewing your extreme captures and video edits. Spend a free morning shopping for tactical gear or local souvenirs before your private TRAGUIN chauffeur transfers you to Dubai International Airport for your flight home, concluding an epic adventure. Transfers: Private luxury van airport departure transit, complete luggage handling.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'Rove Marina / Aloft Palm JumeirahArabian Oryx Glamping Camp',
                'Multi-city UAE',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — Rove Marina / Aloft Palm JumeirahArabian Oryx Glamping Camp',
            ),
            _hotel(
                'Radisson Red Marina / Media OneMysk Al Faya Retreat Domes',
                'Multi-city UAE',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Radisson Red Marina / Media OneMysk Al Faya Retreat Domes',
            ),
            _hotel(
                'W Dubai - The Mina Seyahi Bab Al Shams Desert Resort',
                'Multi-city UAE',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — W Dubai - The Mina Seyahi Bab Al Shams Desert Resort',
            ),
            _hotel(
                'Armani Hotel / Atlantis The Royal Al Maha Luxury Desert Resort & Spa',
                'Multi-city UAE',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Armani Hotel / Atlantis The Royal Al Maha Luxury Desert Resort & Spa',
            )
        ],
        inclusions=[
            _inc_included('Stays: 3 Nights in city thrill-hubs, 1 Night in a luxury air-conditioned desert camp dome', 1),
            _inc_included('Meals: Daily hearty breakfasts and high-protein curated dinners', 2),
            _inc_included('Activities: High-powered Quad Biking, Sunrise Hot Air Balloon, Sandboarding, Water Jet Car', 3),
            _inc_included('Transfers: Dedicated 4x4 off-road vehicles and private luxury vans for ground transits', 4),
            _inc_included('Support: 24/7 dedicated TRAGUIN adventure manager on-site', 5),
            _inc_excluded('International Flights, Visa fees, Travel Insurance', 6),
            _inc_excluded('Skydive Dubai / XLine Zipline ticket charges (Available as add-ons)', 7),
            _inc_excluded('Personal expenses, tipping, meals not specified', 8),
        ],
    )
    return package, itinerary

def build_uae_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-009'
    tour_code = 'TRG-DXB-MICE-2026'
    title = 'Corporate Dubai MICE'
    duration = '04 Nights / 05 Days'
    slug = 'uae-009-corporate-dubai-mice-tour'
    itin_slug = 'uae-009-corporate-dubai-mice-itinerary'
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
            _ph('Serial code UAE-009 | TRAGUIN tour code TRG-DXB-MICE-2026', 1),
            _ph('Country: Dubai, UAE | Category: Corporate MICE & Incentive Travel', 2),
            _ph('Destinations: Dubai Central Business', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Corporate Dubai MICE',
        overview="DWTC Conferences • Team Building Teamwork • Business Networking • Mega Yacht Charter 04 Nights / 05 Days High-Impact Corporate Business & Incentive Showcase SERIAL CODE: UAE-009 TRAGUIN TOUR CODE: TRG-DXB-MICE-2026 STATE / COUNTRY: Dubai / UAE CATEGORY: Corporate MICE & Incentive Travel DURATION: 04 Nights / 05 Days DESTINATIONS: Dubai Central Business District & Business Hubs\n\nTOUR OVERVIEW\nEmpower your corporate collective with our high-end TRAGUIN curated corporate incentive. Designed specifically for elite teams, executive conferences, and corporate retreats, this Corporate Dubai showcase balances cutting-edge business infrastructure with premium off-site team dynamics. Discover an unmatched platform for building partnerships, rewarding top performers, and securing unforgettable memories. MICE Team Note from TRAGUIN: Corporate execution demands precision. Your itinerary is fully managed under tight coordination, featuring dedicated luxury group coaches, high-end meeting venues, priority gala entries, and 24/7 dedicated event management assistance on the ground.\n\nWHY CHOOSE OUR CORPORATE DUBAI MICE PACKAGE?\nDubai is a global powerhouse for corporate networking, providing world-class convention domains alongside unmatched luxury hospitality lines. Choosing this Best Corporate Dubai MICE Tour Package ensures flawless event logistics and unique team integration paths. This master framework integrates high-ranking corporate travel keywords to elevate corporate presentations and business alignment. TRAGUIN Corporate MICE • Uncover major business and leisure attractions: hold state-of-the-art presentations at top convention hubs, experience high-impact team-building dynamics across red dunes, reward leadership with exclusive mega- yacht networking, and capture the scenic beauty of the city's futuristic architecture. It is the absolute Best Time to Visit Dubai to ensure business success and experience a truly premium Luxury Dubai Holiday tailored for corporate victory. THE IMMERSIVE DAY-WISE ITINERARY",
        seo_title='UAE-009 | Corporate Dubai MICE | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Dubai package (UAE-009 / TRG-DXB-MICE-2026): Dubai Central Business with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL & NETWORKING RECEPTION', 1),
            _ih('Day 02: CONFERENCE SESSIONS & DOWNTOWN SIGHTSEEING', 2),
            _ih('Day 03: DESERT TEAM-BUILDING & EXPERIENCES', 3),
            _ih('Day 04: MEGA YACHT GALA AWARDS CELEBRATION', 4),
            _ih('Day 05: CORPORATE CHECKOUT & DEPARTURE', 5)
        ],
        days=[
            _day(
                1,
                'ARRIVAL & NETWORKING RECEPTION',
                (
                    "Arrive in Dubai to an exclusive group greeting. Your private TRAGUIN Corporate Group Coaches transfer your delegation to your selected business resort. In the evening, inaugurate the corporate gathering with a high-end networking reception at a premium skyline lounge, taking in the city's scenic beauty and setting major business goals. MICE Logistics Included: Airport dedicated group clearing assistance, private group coach transits. Evening Experience: Corporate ice-breaking cocktail reception with premium catering lines."
                ),
                [
                    'Overnight Stay: Business Bay / SZR (Handpicked Premium Corporate Convention Hotel)',
                    'Meals Included: Welcome Reception Buffet & Premium Open Bar',
                ],
            ),
            _day(
                2,
                'CONFERENCE SESSIONS & DOWNTOWN SIGHTSEEING',
                (
                    'A full day dedicated to strategic corporate alignment. Utilize state-of-the-art ballroom or convention center spaces for your general assembly, tech setups, and panel discussions. In the late afternoon, transition to a curated Dubai Sightseeing track, visiting the observation decks of Burj Khalifa using priority fast-track avenues. MICE Logistics Included: Full-day executive boardroom/ballroom venue rental, premium AV support. TRAGUIN Corporate MICE •'
                ),
                [
                    'Sightseeing Included: Burj Khalifa Levels 124/125 fast-track group entry passes.',
                    'Overnight Stay: Business Bay / SZR (Handpicked Premium Corporate Convention Hotel)',
                    'Meals Included: Executive Breakfast, Dual Coffee Breaks, Working Lunch, & Downtown Dinner',
                ],
            ),
            _day(
                3,
                'DESERT TEAM-BUILDING & EXPERIENCES',
                (
                    'Ignite teamwork and strategic collaboration with a dedicated desert team-building program. Board luxury 4x4 vehicles for a journey to a private desert arena. Participate in coordinated team problem-solving challenges, off-road navigation simulations, and sandboarding tournaments across the majestic breathtaking landscapes. MICE Logistics Included: Custom corporate team-building facilitators, private sand sports staging. Evening Experience: Exclusive desert oasis stargazing dinner with live entertainment structures.'
                ),
                [
                    'Overnight Stay: Business Bay / SZR (Handpicked Premium Corporate Convention Hotel)',
                    'Meals Included: Executive Breakfast & Premium Desert Barbecue Gala Dinner',
                ],
            ),
            _day(
                4,
                'MEGA YACHT GALA AWARDS CELEBRATION',
                (
                    'Spend a free morning exploring retail innovations at The Dubai Mall or holding small breakout group meetings. In the afternoon, board a massive private luxury Mega Yacht chartered exclusively by TRAGUIN at Dubai Marina. Host your annual corporate awards ceremony and leadership presentations while cruising past Palm Jumeirah during a stunning sunset sunset. MICE Logistics Included: Private Mega Yacht charter, onboard sound/stage setups, red carpet entry. Evening Experience: Grand corporate gala awards dinner on the cruise with premium dining.'
                ),
                [
                    'Overnight Stay: Business Bay / SZR (Handpicked Premium Corporate Convention Hotel)',
                    'Meals Included: Executive Breakfast & Yacht Cruise International Gala Dinner',
                ],
            ),
            _day(
                5,
                'CORPORATE CHECKOUT & DEPARTURE',
                (
                    'Savor your final group breakfast, wrapping up key business summaries and action items. Our dedicated corporate concierge handlers manage all group checkouts, hotel key consolidation, and team luggage logistics before boarding your private coaches to Dubai International Airport for your departures. Transfers: Private corporate coach airport departure transits, priority group luggage handling. TRAGUIN Corporate MICE •'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                "JW Marriott Marquis Dubai World's tallest hotel, massive ballroom cluster capacity.",
                'Multi-city UAE',
                '4N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description="Option 01: Deluxe — JW Marriott Marquis Dubai World's tallest hotel, massive ballroom cluster capacity.",
            ),
            _hotel(
                'Grand Hyatt Dubai / Hilton Al HabtoorPhenomenal convention center capacities and breakout rooms.',
                'Multi-city UAE',
                '4N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Grand Hyatt Dubai / Hilton Al HabtoorPhenomenal convention center capacities and breakout rooms.',
            ),
            _hotel(
                'The Address Boulevard DowntownDirect connected access to Dubai Mall, prestige executive hub.',
                'Multi-city UAE',
                '4N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Address Boulevard DowntownDirect connected access to Dubai Mall, prestige executive hub.',
            ),
            _hotel(
                'Armani Hotel Dubai / Atlantis The RoyalIconic flagship venues for top-tier executive leadership retreats.',
                'Multi-city UAE',
                '4N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Armani Hotel Dubai / Atlantis The RoyalIconic flagship venues for top-tier executive leadership retreats.',
            )
        ],
        inclusions=[
            _inc_included('Accommodation: 04 Nights stay in premier business hotel rooms with executive desks', 1),
            _inc_included('Conferencing: 1 Full-day ballroom/venue rental with premium AV, projector setups, and tech support', 2),
            _inc_included('Catering: Daily executive breakfasts, working luncheons, coffee breaks, and gala dinners', 3),
            _inc_included('Activities: Private Mega Yacht Charter, Desert Team-Building Program, Fast-Track Burj Khalifa entry', 4),
            _inc_included('Logistics: Dedicated private luxury group coaches for all ground transits and transfers', 5),
            _inc_included('TRAGUIN Support: Dedicated on-site MICE project manager and hospitality desk 24/7', 6),
            _inc_excluded('International flight tickets and entry visa processing fees', 7),
            _inc_excluded('Any alcohol packages beyond what is explicitly stated in the gala dinner package', 8),
            _inc_excluded('Personal expenses, hotel room room service, or individual laundry charges', 9),
        ],
    )
    return package, itinerary

def build_uae_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'UAE-010'
    tour_code = 'TRG-DXB-GRD-2026'
    title = 'Grand Dubai Tour'
    duration = '07 Nights / 08 Days'
    slug = 'uae-010-grand-dubai-tour'
    itin_slug = 'uae-010-grand-dubai-itinerary'
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
            _ph('Serial code UAE-010 | TRAGUIN tour code TRG-DXB-GRD-2026', 1),
            _ph('Country: Dubai, UAE | Category: Premium Grand Dubai Tour Package', 2),
            _ph('Destinations: Burj Al Arab Dining • Premium Desert Oasis • Private Yacht Charter • Lapita Parks • Abu', 3),
            _ph('Ideal for: Luxury Travelers', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request', 6),
            _ph('Vehicle / Meals: Private Luxury Van / Buffet Breakfast & Curated Dinners', 7)
        ],
        moods=['Luxury', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium UAE Experience)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Grand Dubai Tour',
        overview='Dhabi Day Cross 07 Nights / 08 Days Ultimate Grand Dubai Ultra-Luxury Showcase SERIAL CODE: UAE-010 TRAGUIN TOUR CODE: TRG-DXB-GRD-2026 STATE / COUNTRY: Dubai / UAE CATEGORY: Premium Grand Dubai Tour Package DURATION: 07 Nights / 08 Days Dubai Full Exploration & Abu Dhabi Inclusion\n\nTOUR OVERVIEW\nStep into the absolute zenith of opulent travel with our flagship TRAGUIN curated itinerary. Designed with rigorous attention to detail, this Grand Dubai tour provides a comprehensive showcase of the Arabian Gulf’s finest landmarks. Experience exclusive experiences, indulge in premium stays, and cherish unforgettable memories on a truly definitive Luxury [Destination] Holiday. Branding Note from TRAGUIN: Distinction is our standard. Your 8-day private expedition includes full VIP chauffeured ground logistics in private Mercedes V-Class or luxury coaches, skip-the-line sky platform admissions, and Michelin-tier culinary highlights backed by our elite 24/7 guest care concierge desk.\n\nWHY CHOOSE OUR GRAND DUBAI LUXURY PACKAGE?\nDubai is a global icon of architectural triumphs and unparalleled hospitality, making it the perfect choice for families and couples seeking elite comfort. Selecting this Best Dubai Tour Package promises a comprehensive exploration of the region’s finest treasures. This professional framework incorporates top-tier corporate, honeymoon, and leisure strings to serve as a stellar client quotation format. Uncover all prominent iconic attractions: feast inside the magnificent Burj Al Arab, ascend the sky structures of Burj Khalifa via private elevators, relax during private sunset yacht charters, explore luxury beachfront developments across Palm Jumeirah, and capture the breathtaking landscapes of the deep desert. It is the absolute Best Time to Visit Dubai to witness premier Dubai Sightseeing landmarks and enjoy a truly rewarding Premium Dubai Experience. THE IMMERSIVE DAY-WISE ITINERARY',
        seo_title='UAE-010 | Grand Dubai Tour | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Dubai package (UAE-010 / TRG-DXB-GRD-2026): Burj Al Arab Dining • Premium Desert Oasis • Private Yacht Charter • Lapita Parks • Abu with 4-tier handpicked accommodation.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Day 01: ARRIVAL IN DUBAI & NETWORKING CRUISE', 1),
            _ih('Day 02: MODERN CITY ICONS & FAST-TRACK BURJ KHALIFA', 2),
            _ih('Day 03: BURJ AL ARAB HIGH TEA & COMRADE MARKETS', 3),
            _ih('Day 04: PREMIUM DESERT RETREAT & OVERNIGHT OASIS', 4),
            _ih('Day 05: SCENIC RESORT RELAXATION & PRIVATE YACHT GALA', 5),
            _ih('Day 06: GRAND ABU DHABI CROSSING & MOSQUE TOUR', 6),
            _ih('Day 07: RESORT LEISURE, MIRACLE GARDEN & FINALE', 7),
            _ih('Day 08: HIGH-END CHECKOUT & DEPARTURE', 8)
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN DUBAI & NETWORKING CRUISE',
                (
                    'Arrive in glittering Dubai to a VIP terminal greeting. Your private TRAGUIN luxury chauffeur will transfer you to your premium hotel. In the evening, unwind with a private, relaxing dhow cruise across the historic Dubai Creek, taking in the scenic beauty of illuminated spice and gold markets while enjoying refreshments. Sightseeing Included: VIP airport personalized clearance, private luxury vehicle transfer. Evening Experience: Private cruise with traditional Arabic catering and ambient music tracks.'
                ),
                [
                    'Overnight Stay: Downtown Dubai (Handpicked Premium Luxury Hotel)',
                    'Meals Included: Welcome International Gala Dinner',
                ],
            ),
            _day(
                2,
                'MODERN CITY ICONS & FAST-TRACK BURJ KHALIFA',
                (
                    'Savor a luxurious breakfast before embarking on a guided tour of New Dubai. Visit the iconic Dubai Mall and bypass all crowded queues using our pre-booked priority passes to ascend the towering Burj Khalifa up to Levels 124/125. Conclude the afternoon exploring Palm Jumeirah luxury promenades. Sightseeing Included: Burj Khalifa entry passes, Dubai Mall, Palm Jumeirah island drive. Evening Experience: Reserved terrace lounge dining facing the synchronized Dubai Fountain Show.'
                ),
                [
                    'Overnight Stay: Downtown Dubai (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast & Premium View Fountain Dinner',
                ],
            ),
            _day(
                3,
                'BURJ AL ARAB HIGH TEA & COMRADE MARKETS',
                (
                    'Indulge in a regal afternoon. Your luxury chauffeur transfers you to the world-famous sail-shaped landmark, the Burj Al Arab, for an exclusive, curated culinary experience. Later, enjoy a guided heritage stroll through the historic wind-towers of Al Fahidi Quarter, shopping for rare oud and silks. Sightseeing Included: Burj Al Arab ultra-luxury entry, Al Fahidi heritage Quarter walk.'
                ),
                [
                    'Overnight Stay: Downtown Dubai (Handpicked Premium Luxury Hotel)',
                    'Meals Included: International Breakfast, Burj Al Arab High Tea, & Fine Dining Dinner',
                ],
            ),
            _day(
                4,
                'PREMIUM DESERT RETREAT & OVERNIGHT OASIS',
                (
                    'Transition from city glitz to majestic timelessness. Enter a private desert conservation reserve in customized 4x4 vehicles for a premium safari. Experience dune-bashing, falconry demonstrations, and sandboarding before checking into an ultra-exclusive desert resort nestled deep in the sand hills. Sightseeing Included: Conservation reserve private safari entries, deep sand exploration tracks. Evening Experience: Private candle-lit oasis dinner with celestial stargazing presentations.'
                ),
                [
                    'Overnight Stay: Desert Conservation Reserve (Ultra-Luxury Desert Sanctuary Resort)',
                    'Meals Included: Breakfast & Live Flame Desert Grill Gala Dinner',
                ],
            ),
            _day(
                5,
                'SCENIC RESORT RELAXATION & PRIVATE YACHT GALA',
                (
                    'Wake up to the serene silent beauty of the desert sunrise. In the afternoon, return to the city and head to Dubai Marina to board a private luxury yacht chartered exclusively by TRAGUIN. Sip fine mocktails while cruising past JBR Beach and Bluewaters Island during sunset, capturing stunning photos. Sightseeing Included: Private luxury yacht charter cruise, Marina coastline exploration tracks.'
                ),
                [
                    'Overnight Stay: Palm Jumeirah Beachfront Resort (Premium Stay)',
                    'Meals Included: Gourmet Resort Breakfast & Yacht Sunset Seafood Dinner',
                ],
            ),
            _day(
                6,
                'GRAND ABU DHABI CROSSING & MOSQUE TOUR',
                (
                    'A full-day excursion to the majestic capital of the UAE, Abu Dhabi. Travel via a private executive vehicle along the scenic highway. Tour the breathtaking Sheikh Zayed Grand Mosque, admiring its marble architecture. Later, visit the spectacular Louvre Abu Dhabi museum before returning to Dubai. Sightseeing Included: Sheikh Zayed Grand Mosque guided tour, Louvre Abu Dhabi entry passes.'
                ),
                [
                    'Overnight Stay: Palm Jumeirah Beachfront Resort (Premium Stay)',
                    'Meals Included: International Breakfast & Abu Dhabi Yas Island Luxury Dinner',
                ],
            ),
            _day(
                7,
                'RESORT LEISURE, MIRACLE GARDEN & FINALE',
                (
                    "Spend a free morning relaxing at your beachfront resort pool. In the afternoon, visit the world's largest natural flower sanctuary, the Dubai Miracle Garden, admiring spectacular floral structures. Conclude your final evening with a grand farewell dinner event, celebrating a remarkable journey. Sightseeing Included: Dubai Miracle Garden flower passes, private city return logistics. Evening Experience: Grand finale corporate or family celebration dinner party."
                ),
                [
                    'Overnight Stay: Palm Jumeirah Beachfront Resort (Premium Stay)',
                    'Meals Included: International Breakfast & Farewell Grand Finale Dinner',
                ],
            ),
            _day(
                8,
                'HIGH-END CHECKOUT & DEPARTURE',
                (
                    'Savor a luxurious final breakfast, enjoying the serene beach view block. Our on-ground concierge team handles all checkout and luggage arrangements seamlessly. Your private vehicle transfers you smoothly to Dubai International Airport for your return flight home, concluding an epic grand holiday. Transfers: Private luxury van airport departure transit, complete luggage handling.'
                ),
                [
                    'Meals Included: International Buffet Breakfast',
                ],
            )
        ],
        hotels=[
            _hotel(
                'JW Marriott Marquis DubaiArabian Oryx Luxury CampRadisson Resort Palm Jumeirah',
                'Multi-city UAE',
                '7N',
                'Deluxe',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                1,
                description='Option 01: Deluxe — JW Marriott Marquis DubaiArabian Oryx Luxury CampRadisson Resort Palm Jumeirah',
            ),
            _hotel(
                'Taj Dubai Downtown Mysk Al Badayer RetreatHilton Dubai The Palm',
                'Multi-city UAE',
                '7N',
                'Premium',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                2,
                description='Option 02: Premium — Taj Dubai Downtown Mysk Al Badayer RetreatHilton Dubai The Palm',
            ),
            _hotel(
                'The Palace Downtown DubaiBab Al Shams Desert Resort The Westin Dubai Mina Seyahi',
                'Multi-city UAE',
                '7N',
                'Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                4,
                3,
                description='Option 03: Luxury — The Palace Downtown DubaiBab Al Shams Desert Resort The Westin Dubai Mina Seyahi',
            ),
            _hotel(
                'Armani Hotel Dubai Al Maha Desert Resort & Spa Atlantis The Royal / One&Only',
                'Multi-city UAE',
                '7N',
                'Ultra Luxury',
                'Deluxe Room',
                'Buffet Breakfast (CP)',
                5,
                4,
                description='Option 04: Ultra Luxury — Armani Hotel Dubai Al Maha Desert Resort & Spa Atlantis The Royal / One&Only',
            )
        ],
        inclusions=[
            _inc_included('Gourmet Experiences: Ultra-premium Burj Al Arab dining access and 7 customized high-end dinners', 1),
            _inc_included('VIP Support: Fast-Track priority entrance passes for Burj Khalifa and all specified major landmarks', 2),
            _inc_included('TRAGUIN Protection: Dedicated 24/7 on-call travel expert assistance and local hospitality desk', 3),
            _inc_excluded('International Flight tickets and UAE entry visa processing fees', 4),
            _inc_excluded('Personal expenses, tipping, laundry, mini-bar consumptions', 5),
            _inc_excluded('Optional extreme tours or water sports not specified in the main flow', 6),
        ],
    )
    return package, itinerary

UAE_UAE_001_010_BUILDERS = [
    build_uae_001,
    build_uae_002,
    build_uae_003,
    build_uae_004,
    build_uae_005,
    build_uae_006,
    build_uae_007,
    build_uae_008,
    build_uae_009,
    build_uae_010,
]
