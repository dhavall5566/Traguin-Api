"""Builder functions for TN-006 through TN-016 Tamil Nadu domestic packages."""

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

TAMIL_NADU_SLUG = "tamil-nadu"


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

def build_tn_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-006'
    tour_code = 'TRAGUIN-TN-006'
    title = 'Premium Tamil Nadu Spiritual Tour'
    duration = '04 Nights / 05 Days'
    slug = 'tn-006-premium-tamil-nadu-spiritual-tour'
    itin_slug = 'tn-006-premium-tamil-nadu-spiritual-tour-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu, India | Category: Pilgrimage / Spiritual', 2),
            _ph('Destinations: Madurai • Rameshwaram • Kanyakumari', 3),
            _ph('Ideal for: Families & Spiritual Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Vehicle Allocated: Dedicated Chauffeur-Driven Air-Conditioned Luxury Sedan / Innova Crysta', 6),
            _ph('Meal Plan: Modified American Plan (Buffet Breakfast & Gourmet Vegetarian Dinners)', 7),
            _ph('Route Map: Madurai Arrival → Rameshwaram Island → Kanyakumari Shoreline → Trivandrum / Madurai Departure', 8),
            _ph('TRAGUIN Curated Experience Note: This custom luxury proposal prioritizes VIP lines at all major temples, specialist companion guides for sacred history narration, smooth transit across the iconic Pamban landscape, and handpicked premium properties.', 9),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts to offer an unhurried, peaceful pilgrimage experience. From front-row access during key temple rituals to personalized, stress-free transportation arrangements, your spiritual retreat is seamlessly managed.', 10),
            _ph('Shopping & Local Souvenirs: Madurai Markets: Bring home world-famous, authentic Sungudi cotton sarees and aromatic fresh jasmine flowers. Coastal Crafts: Discover hand-carved sea shell artifacts, premium multi-colored beach sands, and traditional bronze oil lamps.', 11),
            _ph('Important Notes: Dress Code Guidelines: Traditional attire is strictly required for temple entries (Dhoti/Saree/Salwar). Leather accessories are prohibited inside temple complexes. Weather Insights: The coastal breeze creates warm days with pleasant, cool evenings. Carrying light, breathable cotton wear is recommended. Booking Policy: VIP Darshan experiences are subject to local administrative schedules and should be secured well in advance via TRAGUIN support.', 12),
        ],
        moods=['Pilgrimage', 'Spiritual', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Premium Tamil Nadu Spiritual Tour • Madurai • Rameshwaram • Kanyakumari • 04 Nights / 05 Days',
        overview=('Step into an extraordinary, sacred soul-journey across the divine corridors of South India. Vetted and beautifully curated by TRAGUIN, this signature itinerary balances the grand architecture of ancient temples with supreme, comforting premium stays. From the majestic echoing halls of Madurai Meenakshi Temple to the breathtaking landscapes where three oceans merge at Kanyakumari, surrender yourself to an immersive experience that perfectly blends sacred heritage with elite luxury.\n\nTOUR OVERVIEW\nVehicle Allocated: Dedicated Chauffeur-Driven Air-Conditioned Luxury Sedan / Innova Crysta\nMeal Plan: Modified American Plan (Buffet Breakfast & Gourmet Vegetarian Dinners)\nRoute Map: Madurai Arrival → Rameshwaram Island → Kanyakumari Shoreline → Trivandrum / Madurai Departure\n\nTRAGUIN Curated Experience Note:\nThis custom luxury proposal prioritizes VIP lines at all major temples, specialist companion guides for sacred history narration, smooth transit across the iconic Pamban landscape, and handpicked premium properties.\n\nFor discerning families seeking a life-changing Tamil Nadu Pilgrimage Package or an elegant Tamil Nadu Family Tour, the sacred lands of Madurai, Rameshwaram, and Kanyakumari offer an unmatched cultural retreat. Witness the towering sculptured gopurams of ancient shrines, participate in sacred bathing rituals at the 22 holy wells of Ramanathaswamy Temple, and capture iconic Instagram spots overlooking the majestic Vivekananda Rock Memorial at sunset. With TRAGUIN Tamil Nadu Packages, every single element of your premium holiday is synchronized to offer effortless luxury, zero fatigue, and deep, profound peace.'),
        seo_title='TN-006 | Premium Tamil Nadu Spiritual Tour | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Tamil Nadu package (TN-006 / TRAGUIN-TN-006): Madurai, Rameshwaram, Kanyakumari spiritual pilgrimage with VIP temple access and 2-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Meenakshi Amman Temple, Thirumalai Nayakkar Palace, and Pamban Bridge transit', 1),
            _ih('Ramanathaswamy Temple VIP visit, Agnitheertham, Dhanushkodi Beach, and coastal sunset', 2),
            _ih('Vivekananda Rock Memorial, Thiruvalluvar Statue, Padmanabhapuram Palace, and triple-ocean confluence', 3),
            _ih('TRAGUIN Signature Experience with VIP darshan access and chartered ferry tickets to Vivekananda Rock', 4),
            _ih('Handpicked 2-tier premium accommodation across Madurai, Rameshwaram, and Kanyakumari', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN MADURAI', ("Arrive in the historical city of Madurai. Meet your dedicated TRAGUIN tour representative at the airport or railway station for a smooth, air-conditioned transfer to your premium hotel. Following a relaxed check-in and refreshment, set out to witness the glorious Meenakshi Amman Temple. A local scholar will guide you through the awe-inspiring 1,000-pillar hall, unraveling the epic stories carved beautifully into stone. In the evening, witness the legendary night ceremony where Lord Shiva is carried to Meenakshi's shrine."), [
                'Sightseeing Included: Meenakshi Amman Temple, Thirumalai Nayakkar Palace.',
                'Evening Experience: VIP Darshan access and high tea briefing arranged exclusively by travel specialists.',
                'Overnight Stay: Handpicked Luxury Hotel, Madurai.',
                'Meals Included: Welcome Drink & Curated Dinner.',
            ]),
            _day(2, 'MADURAI TO RAMESHWARAM', ('Enjoy a delicious traditional breakfast before checking out. Journey toward the sacred island of Rameshwaram. The drive features a breathtaking landscape as you cross the historic Pamban Bridge over the bright turquoise sea—a fantastic photography point. Upon arrival, check into your premium seaside resort. Spend a reflective evening visiting the local sights or enjoying the quiet scenic beauty of the coast.'), [
                'Sightseeing Included: Pamban Bridge Transit, APJ Abdul Kalam Memorial.',
                'Food Suggestions: Savor fresh tender coconut water and elite traditional South Indian filter coffee.',
                'Overnight Stay: Premium Handpicked Resort, Rameshwaram.',
                'Meals Included: Full Breakfast & Gourmet Dinner.',
            ]),
            _day(3, 'RAMESHWARAM TO KANYAKUMARI', ('Begin early with a spiritual morning at the Ramanathaswamy Temple. Participate in the sacred ritual of bathing at the 22 holy teerthams (wells) inside the temple complex, followed by an effortless VIP darshan. Later, explore Dhanushkodi, the atmospheric ghost town at the edge of the island where the Bay of Bengal meets the Indian Ocean. Afterward, embark on a comfortable private drive to Kanyakumari, the southernmost tip of mainland India, arriving just in time to witness a spectacular coastal sunset.'), [
                'Sightseeing Included: Ramanathaswamy Temple VIP Visit, Agnitheertham, Dhanushkodi Beach, Sunset Viewpoint.',
                "Immersive Experiences: Walking along the unique land's end strip of Dhanushkodi with panoramic ocean views.",
                'Overnight Stay: Premium Luxury Hotel, Kanyakumari.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'KANYAKUMARI EXPLORATION', ('Wake up to a magical sunrise over the ocean. Board an exclusive ferry to visit the iconic Vivekananda Rock Memorial and the colossal Thiruvalluvar Statue towering majestically over the waves. Spend quiet moments meditating in the peaceful dhyana mandapam. In the afternoon, explore the historical 300-year-old Padmanabhapuram Palace, a masterpiece of traditional wooden architecture, before spending a relaxed evening shopping for authentic handicrafts.'), [
                'Sightseeing Included: Vivekananda Rock, Thiruvalluvar Statue, Kanyakumari Temple, Padmanabhapuram Palace.',
                'Photography Points: The striking sunset where the Arabian Sea, Bay of Bengal, and Indian Ocean meet.',
                'Overnight Stay: Premium Luxury Hotel, Kanyakumari.',
                'Meals Included: Breakfast & Festive Farewell Dinner.',
            ]),
            _day(5, 'DEPARTURE VIA TRIVANDRUM', ('Indulge in a final morning buffet breakfast while listening to the distant call of the ocean waves. Your luxury private vehicle will arrive to transfer you smoothly to the Trivandrum International Airport (or Madurai Airport) for your flight home. Your premium TRAGUIN Tamil Nadu Experience concludes, leaving you with unforgettable memories and a deeply enriched soul.'), [
                'Transfers Included: Private Airport / Station drop-off.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Courtyard by Marriott / Daiwik Hotels / Annai Resorts & Spa', 'Madurai • Rameshwaram • Kanyakumari', '04 Nights', 'Premium', 'Premium Handpicked Rooms', 'Modified American Plan (Buffet Breakfast & Gourmet Vegetarian Dinners)', 4, 1, description='OPTION 01 – PREMIUM: Courtyard by Marriott (Madurai) • Daiwik Hotels (Rameshwaram) • Annai Resorts & Spa (Kanyakumari)'),
            _hotel('Heritage Madurai Resort / Cabana Coral Reef Resort / The Gopinivas Grand', 'Madurai • Rameshwaram • Kanyakumari', '04 Nights', 'Luxury', 'Luxury Handpicked Rooms', 'Modified American Plan (Buffet Breakfast & Gourmet Vegetarian Dinners)', 5, 2, description='OPTION 02 – LUXURY: Heritage Madurai Resort (Madurai) • Cabana Coral Reef Resort (Rameshwaram) • The Gopinivas Grand (Kanyakumari)'),
        ],
        inclusions=[
            _inc_included('Accommodation: Luxury stays at highly rated handpicked premium hotels and coastal resorts.', 1),
            _inc_included('Meals: Daily premium breakfast buffets and meticulously prepared gourmet vegetarian dinners.', 2),
            _inc_included('Transfers & Sightseeing: Chauffeur-driven luxury Innova Crysta / Sedan for effortless, private transit.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local concierge assistance and VIP skip-the-line temple bookings.', 4),
            _inc_included('Complimentary Experiences: Private local heritage companion guide fees and chartered ferry tickets to Vivekananda Rock.', 5),
            _inc_excluded('Airfare or interstate train tickets to Tamil Nadu.', 6),
            _inc_excluded('Personal elements such as specialized pooja items, laundry, telephone charges, and tipping.', 7),
            _inc_excluded('Any monument entrance or camera permits not explicitly specified.', 8),
            _inc_excluded('Travel insurance or unexpected medical expenses.', 9),
        ],
    )
    return package, itinerary

def build_tn_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-007'
    tour_code = 'TRAGUIN-TN-007'
    title = 'Chennai • Mahabalipuram Coastal Express'
    duration = '03 Nights / 04 Days'
    slug = 'tn-007-chennai-mahabalipuram-coastal-express'
    itin_slug = 'tn-007-chennai-mahabalipuram-coastal-express-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu, India | Category: Family Vacation / Coastal Leisure', 2),
            _ph('Destinations: Chennai • Mahabalipuram Coastal Belt', 3),
            _ph('Ideal for: Family Getaways & Luxury Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Vehicle Allocated: Dedicated Luxury Chauffeur-driven Air-Conditioned Vehicle', 6),
            _ph('Meal Plan: Deluxe Continental Breakfast (CP Plus Plan Hotels)', 7),
            _ph('Route Track: Chennai Arrival & Urban Tour → ECR Scenic Drive → Mahabalipuram Coastal Escapes → Cochin/Chennai Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Experience the finest elements of a Premium Tamil Nadu Experience. This escape guarantees top tourist places in Tamil Nadu with expert companion guidance, flexible family-friendly timings, and private shorefront leisure.', 9),
            _ph('TRAGUIN Signature Experience: Handcrafted to maximize family relaxation. Skip standard vehicle waiting with prioritized hotel check-ins, custom roadside break suggestions, and elite destination curation from premier holiday experts.', 10),
            _ph('Shopping & Local Souvenirs: Authentic Kanchipuram Silks: Pick out high-quality traditional handloomed sarees and ethnic textiles from verified legacy outlets. Stone Sculptures: Purchase miniature hand-carved stone models sculpted meticulously by traditional artisans of Mahabalipuram.', 11),
            _ph('Important Notes: Resort Check Times: Check-in window begins at 14:00 hours; departures are managed at 11:00 hours. Options are flexible based on premium resort load status. Seasonal Dress Recommendations: Light clothing fabrics work best throughout the year. Bringing dynamic sunblock options or broad shades ensures maximum comfort.', 12),
        ],
        moods=['Family', 'Coastal', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Best Tamil Nadu Tour Package • Chennai • Mahabalipuram Coastal Express • 03 Nights / 04 Days',
        overview=('Welcome to a land where ancient soul meets pristine coastlines. Handcrafted elegantly by your premier holiday curators at TRAGUIN, this exclusive Tamil Nadu Honeymoon Package and Tamil Nadu Family Tour option invites your loved ones to witness majestic rock-cut wonders, serene beach shores, and heritage luxury. Let us turn miles into moments with handpicked hotels, seamless transfers, and immersive stories.\n\nTOUR OVERVIEW\nVehicle Allocated: Dedicated Luxury Chauffeur-driven Air-Conditioned Vehicle\nMeal Plan: Deluxe Continental Breakfast (CP Plus Plan Hotels)\nRoute Track: Chennai Arrival & Urban Tour → ECR Scenic Drive → Mahabalipuram Coastal Escapes → Cochin/Chennai Departure\n\nTRAGUIN Curated Experience Note:\nExperience the finest elements of a Premium Tamil Nadu Experience. This escape guarantees top tourist places in Tamil Nadu with expert companion guidance, flexible family-friendly timings, and private shorefront leisure.\n\nWhy plan a spectacular Luxury Tamil Nadu Holiday? Boasting deep historical significance, breathtaking landscapes, and beautiful shorelines, Tamil Nadu stands tall as a treasure trove of culture. From the dynamic cityscapes of Chennai to the legendary Shore Temple architectures in Mahabalipuram, this itinerary reveals the absolute best of Tamil Nadu Sightseeing options.'),
        seo_title='TN-007 | Chennai Mahabalipuram Coastal Express | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Tamil Nadu package (TN-007 / TRAGUIN-TN-007): Chennai, Mahabalipuram ECR coastal tour with 4-tier handpicked beachfront accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('San Thome Cathedral, Marina Beach Coastline Walk, and Kapaleeshwarar Temple', 1),
            _ih('ECR Coastal Drive, DakshinaChitra Cultural Stopover, and beachside resort leisure', 2),
            _ih("UNESCO Shore Temple, Five Rathas, Arjuna's Penance, and Krishna's Butterball", 3),
            _ih('TRAGUIN Signature Experience with prioritized hotel check-ins and elite destination curation', 4),
            _ih('Premium 4-tier handpicked accommodation across Chennai and Mahabalipuram', 5),
        ],
        days=[
            _day(1, 'CHENNAI ARRIVAL', ('Your premium gateway into Tamil Nadu starts at Chennai International Airport/Railway Station. Meet your specialized TRAGUIN chauffeur who will welcome you and ensure your luggage is securely placed into your private luxury transport. Check into your chosen handpicked premium stay and unwind. In the afternoon, enjoy an urban drive covering the historic San Thome Cathedral Basilica, built over the tomb of St. Thomas. Conclude the day watching the golden sun set at Marina Beach, the second longest natural urban beach in the world, filled with crisp sea breezes and lively local evening stalls.'), [
                'Sightseeing Included: San Thome Cathedral, Marina Beach Coastline Walk, Kapaleeshwarar Temple.',
                'Photography Points: Majestic gopurams of Kapaleeshwarar Temple and the wide expanse of Marina Beach at twilight.',
                'Overnight Stay: Handpicked Luxury Resort / Premium Hotel, Chennai.',
                'Meals Included: Welcome Drinks & Refreshing High Tea.',
            ]),
            _day(2, 'CHENNAI TO MAHABALIPURAM VIA ECR', ('Savor a luxurious morning breakfast before starting a magnificent drive down the famous East Coast Road (ECR) towards the ancient port town of Mahabalipuram. En route, make a special stop at DakshinaChitra Living History Museum, a curated cultural village representing the traditional crafts, lifestyles, and performing arts of South India. Upon arriving in Mahabalipuram, check into an premium beachside resort. Spend your evening listening to waves right from your resort patio or relaxing pool-side.'), [
                'Sightseeing Included: ECR Coastal Drive, DakshinaChitra Cultural Stopover.',
                'Evening Experience: Private family dinner suggestions featuring authentic Chettinad preparations or coastal catching varieties.',
                'Overnight Stay: Handpicked Premium Beach Resort, Mahabalipuram.',
                'Meals Included: Premium Buffet Breakfast.',
            ]),
            _day(3, 'MAHABALIPURAM SIGHTSEEING', ("Wake up to a crisp coastal sunrise. Today, explore the Top Tourist Places in Tamil Nadu based within this historical sanctuary. Visit the spectacular Shore Temple, standing gracefully since the 8th century on the edge of the roaring Bay of Bengal. Wander across to the Five Rathas, monolith structures sculpted out of solid granite rocks, reflecting brilliant Dravidian artistry. Witness Arjuna's Penance, one of the largest open-air rock reliefs anywhere on earth. Finish your day marveling at Krishna's Butterball, a giant natural boulder perched miraculously on a hillside slope."), [
                "Sightseeing Included: UNESCO Shore Temple, Five Rathas, Arjuna's Penance, Krishna's Butterball.",
                'Optional Activities: Indulge in an exclusive beach surfing introduction or premium traditional spa treatments at the resort.',
                'Overnight Stay: Handpicked Premium Beach Resort, Mahabalipuram.',
                'Meals Included: Full Breakfast spread.',
            ]),
            _day(4, 'MAHABALIPURAM TO CHENNAI DEPARTURE', ('Enjoy a relaxed morning breakfast overlooking the beachfront palms. Pack your belongings with unforgettable memories of your premium coastal vacation. Your chauffeur will drive you comfortably back to Chennai. Before dropping you off, make a brief stop to pick up iconic traditional handlooms or locally sculpted stone keepsakes. Smooth transfer to Chennai Airport or Central Railway Station for your return trip home.'), [
                'Transfers Included: Private Airport/Station drop-off vehicle transfers.',
                'Meals Included: Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Pride Hotel Chennai / Chariot Beach Resort', 'Chennai • Mahabalipuram', '03 Nights', 'Deluxe', 'Standard Comfort Room', 'CP Plan (Breakfast)', 4, 1, description='OPTION 01 – DELUXE: The Pride Hotel Chennai • Chariot Beach Resort (CP Plan Breakfast)'),
            _hotel('The Residency Towers / Radisson Blu Resort Temple Bay', 'Chennai • Mahabalipuram', '03 Nights', 'Premium', 'Premium Room', 'CP Plan (Breakfast)', 4, 2, description='OPTION 02 – PREMIUM: The Residency Towers • Radisson Blu Resort Temple Bay (CP Plan Breakfast)'),
            _hotel('Taj Connemara Chennai / InterContinental Chennai Mahabalipuram', 'Chennai • Mahabalipuram', '03 Nights', 'Luxury', 'Luxury Room', 'CP Plan (Breakfast)', 5, 3, description='OPTION 03 – LUXURY: Taj Connemara, Chennai • InterContinental Chennai Mahabalipuram (CP Plan Breakfast)'),
            _hotel("The Leela Palace Chennai / Taj Fisherman's Cove Resort & Spa", 'Chennai • Mahabalipuram', '03 Nights', 'Ultra Luxury', 'Luxury Suite / Beach Villa', 'Gourmet Breakfast + Welcome Amenities', 5, 4, description="OPTION 04 – ULTRA LUXURY: The Leela Palace Chennai • Taj Fisherman's Cove Resort & Spa (Gourmet Breakfast + Welcome Amenities)"),
        ],
        inclusions=[
            _inc_included('Accommodation: Curated stay at handpicked hotels and beachfront coastal resorts.', 1),
            _inc_included('Meals: Generous morning breakfast buffets at all standard property choices.', 2),
            _inc_included('Transfers & Sightseeing: Private air-conditioned luxury transportation with dedicated polite chauffeur.', 3),
            _inc_included('Welcome Amenities: Personalized arrival greeting kits and pure bottled drinking water allocations throughout the road tour.', 4),
            _inc_included('TRAGUIN Support: 24/7 round-the-clock backend execution help and professional travel expert care.', 5),
            _inc_excluded('Airfare or inter-state rail ticket purchases to reach Chennai.', 6),
            _inc_excluded('Individual historical monument ticket admission fees or photography passes.', 7),
            _inc_excluded('Personal bills (laundry, room service snacks, phone calling, and driver gratuity tips).', 8),
            _inc_excluded('Optional coastal water sport activities or vehicle modifications.', 9),
        ],
    )
    return package, itinerary

def build_tn_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-008'
    tour_code = 'TRAGUIN-TN-008'
    title = 'Trichy & Velankanni Divine Cruise'
    duration = '03 Nights / 04 Days'
    slug = 'tn-008-trichy-velankanni-divine-cruise'
    itin_slug = 'tn-008-trichy-velankanni-divine-cruise-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu, India | Category: Family Vacation / Divine Tour', 2),
            _ph('Destinations: Trichy • Velankanni', 3),
            _ph('Ideal for: Families & Spiritual Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Vehicle Allocated: Dedicated Luxury AC Sedan / Innova Crysta Chauffeur Car', 6),
            _ph('Meal Plan: Modified American Plan (Buffet Breakfast & Private Dinners)', 7),
            _ph('Route Map: Trichy Arrival → Srirangam & Rockfort → Velankanni Coast Line → Trichy Departure', 8),
            _ph('TRAGUIN Curated Experience Note: This custom quote follows a highly specialized travel consultant tone, guaranteeing seamless VIP temple entries, premium stays, curated seashore reflections, and absolute travel comfort for your entire family.', 9),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts to offer zero stress for modern families. Enjoy custom temple-timings to avoid crowded rush hours, prime executive seats during shoreline road transits, and priority check-ins.', 10),
            _ph('Shopping & Local Souvenirs: Trichy Bazaars: Pick up high-quality Tanjore paintings, beautiful brass lamps, and traditional Trichy handloom sarees. Velankanni Markets: Beautiful church candles, handcrafted shell art pieces, and holy devotional relics for home altars.', 11),
            _ph('Important Notes: Dress Code: Traditional attire is strictly required to enter Srirangam Temple. Avoid shorts and sleeveless shirts. Check-in Policies: Early check-ins are completely subject to seasonal availability.', 12),
        ],
        moods=['Family', 'Spiritual', 'Coastal'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0, price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='TRAGUIN Premium Tamil Nadu Tour • Trichy & Velankanni Divine Cruise • 03 Nights / 04 Days',
        overview=(
            'Welcome to a journey of divine peace and deep ancestral roots. Crafted beautifully by TRAGUIN, this exclusive family-focused spiritual exploration merges the rich heritage temples of Trichy with the blissful coastal sanctity of the Velankanni shrine. Surrender your senses to breathtaking landscapes, immersive experiences, and handpicked hotels that guarantee unforgettable memories.\n\nTOUR OVERVIEW\nVehicle Allocated: Dedicated Luxury AC Sedan / Innova Crysta Chauffeur Car\nMeal Plan: Modified American Plan (Buffet Breakfast & Private Dinners)\nRoute Map: Trichy Arrival → Srirangam & Rockfort → Velankanni Coast Line → Trichy Departure\n\nTRAGUIN Curated Experience Note:\nThis custom quote follows a highly specialized travel consultant tone, guaranteeing seamless VIP temple entries, premium stays, curated seashore reflections, and absolute travel comfort for your entire family.\n\nIf you are searching for the Best Tamil Nadu Tour Package or a relaxing Tamil Nadu Family Tour, this coastal divine trail covers iconic attractions loved across generations. Experience the immense spiritual energy of the world\'s largest functioning Hindu temple at Srirangam and feel the deep grace at the Basilica of Our Lady of Good Health in Velankanni.'
        ),
        seo_title='TN-008 | Trichy Velankanni Divine Cruise | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Tamil Nadu package (TN-008 / TRAGUIN-TN-008): Trichy, Velankanni divine cruise with VIP temple access and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Rockfort Temple Complex, Thayumanaswamy Shrine, and golden sunset over Cauvery river basin', 1),
            _ih('Srirangam Temple Complex, Velankanni Main Shrine, and candlelit rosary procession', 2),
            _ih('Morning Mass, Our Lady\'s Tank, Offering Church Museum, and beachfront sunset gathering', 3),
            _ih('TRAGUIN Signature Experience with custom temple timings and priority check-ins', 4),
            _ih('Premium 4-tier handpicked accommodation across Trichy and Velankanni', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN TRICHY', (
                'Your premium divine vacation starts as you land at Trichy Airport/Railway Station. Receive a warm traditional welcome from your dedicated TRAGUIN driver-companion. Transfer smoothly to your luxury handpicked hotel for check-in. In the late afternoon, climb the historic Rockfort Ucchi Pillayar Temple via clean, well-maintained stone steps to witness a panoramic golden sunset over the Cauvery river basin.'
            ), [
                'Sightseeing Included: Rockfort Temple Complex, Thayumanaswamy Shrine.',
                'Evening Experience: Leisure family dinner featuring authentic local South Indian specialties at the hotel restaurant.',
                'Overnight Stay: Premium Luxury Hotel, Trichy.',
                'Meals Included: Welcome Amenity & Dinner.',
            ]),
            _day(2, 'TRICHY TO VELANKANNI', (
                'After a rich buffet breakfast, proceed for a special VIP visit to the world-renowned Sri Ranganathaswamy Temple at Srirangam, a masterpiece of Dravidian architecture boasting 21 magnificent gopurams. Following this deep immersion, take a scenic cross-state drive towards the coastal holy town of Velankanni. Arrive by afternoon and check into your premium seaside resort. In the evening, attend the soothing candlelit rosary procession at the shrine.'
            ), [
                'Sightseeing Included: Srirangam Temple Complex, Velankanni Main Shrine.',
                'Optional Activities: A serene beach walk behind the Basilica as the sea breeze rolls in.',
                'Overnight Stay: Handpicked Beachfront Luxury Resort, Velankanni.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'VELANKANNI SPIRITUAL HOLY DAY', (
                'Devote your day to the peaceful atmosphere of Our Lady of Good Health Basilica. Participate in the morning Holy Mass, visit the holy path to the Tank Shrine where miracles took place, and explore the comprehensive Museum of Offerings. In the evening, TRAGUIN has organized an exclusive beachfront family high-tea experience to let you unwind together beside the rolling waves of the Bay of Bengal.'
            ), [
                'Sightseeing Included: Morning Mass, Our Lady\'s Tank, Offering Church Museum.',
                'Evening Experience: Private beach-view sunset gathering curated specially for your family.',
                'Overnight Stay: Handpicked Beachfront Luxury Resort, Velankanni.',
                'Meals Included: Full Breakfast & Dinner.',
            ]),
            _day(4, 'VELANKANNI TO TRICHY & DEPARTURE', (
                'Enjoy a relaxed coastal breakfast with views of the sea. Pack your bags loaded with divine blessings and beautiful memories. Embark on a comfortable smooth return drive to Trichy. If time permits, stop at the magnificent 11th-century Grand Anicut (Kallanai Dam). You will then be dropped off at Trichy Airport/Station for your journey home, concluding your premium TRAGUIN Tamil Nadu Package.'
            ), [
                'Transfers Included: Return Airport/Station Drop-off.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Hotel Grand Arcadia / Clinton Park Inn', 'Trichy • Velankanni', '03 Nights', 'Deluxe', 'Standard Room', 'MAPAI (Breakfast + Dinner)', 4, 1, description='OPTION 01 – DELUXE: Hotel Grand Arcadia (Trichy, 1 Night) • Clinton Park Inn (Velankanni, 2 Nights) — MAPAI (Breakfast + Dinner)'),
            _hotel('SRM Hotel By building blocks / MGM Sunshine Beach Resort', 'Trichy • Velankanni', '03 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast + Dinner)', 4, 2, description='OPTION 02 – PREMIUM: SRM Hotel By building blocks (Trichy) • MGM Sunshine Beach Resort (Velankanni) — MAPAI (Breakfast + Dinner)'),
            _hotel('Courtyard by Marriott Trichy / Seagate Church View Resort', 'Trichy • Velankanni', '03 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Premium Dining)', 5, 3, description='OPTION 03 – LUXURY: Courtyard by Marriott Trichy • Seagate Church View Resort — MAPAI (Premium Dining)'),
            _hotel('Courtyard by Marriott (Executive Suite) / The Premium Beachside Luxury Villa', 'Trichy • Velankanni', '03 Nights', 'Ultra Luxury', 'Executive Suite / Luxury Villa', 'MAPAI + High Tea Services', 5, 4, description='OPTION 04 – ULTRA LUXURY: Courtyard by Marriott (Executive Suite) • The Premium Beachside Luxury Villa — MAPAI + High Tea Services'),
        ],
        inclusions=[
            _inc_included('Accommodation: Premium stays across handpicked properties in Trichy and Velankanni.', 1),
            _inc_included('Meals: Generous daily breakfasts and curated luxury dinners included at all hotel options.', 2),
            _inc_included('Private Fleet: Dedicated air-conditioned Luxury vehicle for entire sightseeing and smooth transit.', 3),
            _inc_included('TRAGUIN Support: 24/7 priority concierge backing from assignment experts.', 4),
            _inc_included('Welcome Tokens: Spiritual welcome box with local traditional sweets and divine mementos.', 5),
            _inc_excluded('Train / Flight bookings to and from Trichy.', 6),
            _inc_excluded('Special fast-track archana tickets or personal ceremonial offerings inside temples/shrines.', 7),
            _inc_excluded('Laundry, tips, premium beverages, and telephone charges.', 8),
            _inc_excluded('Insurance cover or expenses arising from unplanned delays.', 9),
        ],
    )
    return package, itinerary

def build_tn_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-009'
    tour_code = 'TRAGUIN-TN-009'
    title = 'Grand Tamil Nadu Heritage & Hills Vacation'
    duration = '08 Nights / 09 Days'
    slug = 'tn-009-grand-tamil-nadu-heritage-hills-vacation'
    itin_slug = 'tn-009-grand-tamil-nadu-heritage-hills-vacation-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu, India | Category: Family Vacation / Premium Heritage', 2),
            _ph('Destinations: Chennai • Mahabalipuram • Pondicherry • Tanjore • Madurai • Ooty', 3),
            _ph('Ideal for: Families, Leisure Travelers & Heritage Seekers', 4),
            _ph('Best season: October to March', 5),
            _ph('Vehicle Allocated: Private Air-Conditioned Luxury Innova Crysta (Chauffeur-Driven)', 6),
            _ph('Meal Plan: Modified American Plan (Buffet Breakfast & Specially Curated Dinners)', 7),
            _ph('Route Map: Chennai → Mahabalipuram → Pondicherry → Tanjore → Madurai → Ooty → Coimbatore Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Every stop along this premium path has been vetted by our destination experts. Enjoy priority VIP entrances at historical sites, certified professional storytellers, handpicked luxury stays, and seamless logistical execution.', 9),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts for discerning families. Enjoy seamless execution with zero delays, direct contact with local artisan guilds, VIP temple entries, and unparalleled luxury throughout the diverse landscape.', 10),
            _ph('Shopping & Local Souvenirs: Kanchipuram & Madurai: Buy world-famous authentic hand-woven Kanchipuram silk sarees and Sungudi fabrics. Tanjore & Ooty: Pick up traditional gold-leaf paintings, bronze artifacts, Nilgiri organic tea varieties, and homemade chocolates.', 11),
            _ph('Important Notes: Hotel Policies: Standard check-in is at 14:00 hrs and check-out at 11:00 hrs. Early arrival options are subject to availability. Dress Codes: Traditional modest attire is required for entry into major temples like Madurai Meenakshi Temple. Weather Notes: Please carry warm clothing or shawls for your evenings in Ooty and Coonoor, where temperatures decrease.', 12),
        ],
        moods=['Family', 'Heritage', 'Hills'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Best Tamil Nadu Tour Package • Grand Tamil Nadu Heritage & Hills Vacation • 08 Nights / 09 Days',
        overview=('Welcome to a majestic realm where ancient history meets cloud-kissed mountain peaks. This exclusive, high-end itinerary curated beautifully by TRAGUIN takes your family on an unforgettable journey through time and nature. From the towering Dravidian gopurams of Madurai to the cool, colonial air of misty Ooty, prepare to live a truly premium travel experience filled with handpicked hotels, breathtaking landscapes, and immersive experiences.\n\nTOUR OVERVIEW\nVehicle Allocated: Private Air-Conditioned Luxury Innova Crysta (Chauffeur-Driven)\nMeal Plan: Modified American Plan (Buffet Breakfast & Specially Curated Dinners)\nRoute Map: Chennai → Mahabalipuram → Pondicherry → Tanjore → Madurai → Ooty → Coimbatore Departure\n\nTRAGUIN Curated Experience Note:\nEvery stop along this premium path has been vetted by our destination experts. Enjoy priority VIP entrances at historical sites, certified professional storytellers, handpicked luxury stays, and seamless logistical execution.\n\nTamil Nadu is a treasure trove of culture, home to majestic UNESCO World Heritage monuments, spiritual architecture, and serene hill stations. Whether you are seeking a grand Tamil Nadu Family Tour or a romantic Tamil Nadu Honeymoon Package, this state fulfills every travel dream with its unique diversity.'),
        seo_title='TN-009 | Grand Tamil Nadu Heritage & Hills Vacation | TRAGUIN',
        seo_description='Premium 08 Nights / 09 Days Tamil Nadu package (TN-009 / TRAGUIN-TN-009): Chennai, Mahabalipuram, Pondicherry, Tanjore, Madurai, Ooty heritage and hills tour with 4-tier accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Scenic Coastal ECR Drive, Shore Temple, Five Rathas, and French Quarter Promenade', 1),
            _ih('Auroville Matrimandir Viewpoint, Sri Aurobindo Ashram, and Brihadeeswarar Temple UNESCO site', 2),
            _ih('Meenakshi Amman Temple, Thousand Pillar Hall, and Nilgiri Mountain scenic drive to Ooty', 3),
            _ih('Nilgiri Heritage Toy Train, Sims Park Coonoor, and Botanical Gardens', 4),
            _ih('TRAGUIN Signature Experience with private gold-leaf painting session and confirmed Nilgiri Toy Train tickets', 5),
        ],
        days=[
            _day(1, 'CHENNAI TO MAHABALIPURAM', ('Arrive at Chennai International Airport, where a dedicated TRAGUIN executive gives you a premium traditional welcome. Board your luxury vehicle and embark on a smooth scenic drive along the beautiful East Coast Road toward Mahabalipuram. Check into your ultra-premium beachside resort. Spend a relaxing evening watching the sunset over the Bay of Bengal.'), [
                'Sightseeing Included: Scenic Coastal ECR Drive, Beachfront Relaxation.',
                'Evening Experience: Private beachside high-tea organized exclusively by TRAGUIN experts.',
                'Overnight Stay: Luxury Beach Resort, Mahabalipuram.',
                'Meals Included: Welcome Drink & Gourmet Buffet Dinner.',
            ]),
            _day(2, 'MAHABALIPURAM TO PONDICHERRY', ("After an early gourmet breakfast, explore the iconic attractions of Mahabalipuram, starting with the magnificent rock-cut Shore Temple and the massive relief of Arjuna's Penance. Afterward, drive down to the charming coastal town of Pondicherry. Check into your heritage boutique hotel and spend the afternoon exploring the pristine, colorful French Quarter with its colonial architecture and quiet cafes."), [
                "Sightseeing Included: Shore Temple, Five Rathas, Arjuna's Penance, French Quarter Promenade.",
                'Photography Points: The striking seaside view of Shore Temple and yellow colonial walls of White Town.',
                'Overnight Stay: Handpicked Luxury Heritage Hotel, Pondicherry.',
                'Meals Included: Full Breakfast & Curated French-Indian Fusion Dinner.',
            ]),
            _day(3, 'PONDICHERRY EXPLORATION', ('Immerse yourself in spiritual peace with a morning visit to Auroville and the architectural marvel of the Matrimandir viewpoint. Spend your afternoon at the serene Sri Aurobindo Ashram. In the evening, enjoy a peaceful stroll down the famous Promenade Beach, feeling the crisp sea breeze.'), [
                'Sightseeing Included: Auroville Matrimandir Viewpoint, Sri Aurobindo Ashram, Promenade Beach.',
                'Food Suggestions: Taste freshly baked wood-fired pizzas and gourmet pastries at local French bistros.',
                'Overnight Stay: Luxury Heritage Hotel, Pondicherry.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'PONDICHERRY TO TANJORE', ('Drive deeper into the cultural heartland of Tamil Nadu towards Tanjore (Thanjavur). Upon arrival, explore the majestic Brihadeeswarar Temple (The Big Temple), a UNESCO World Heritage site built by Raja Raja Chola I. Marvel at its breathtaking architecture and monolithic stone Nandi, which stands as a monumental symbol of ancient Indian engineering.'), [
                'Sightseeing Included: Brihadeeswarar Temple, Thanjavur Royal Palace & Museum.',
                'Local Experiences: Private demonstration of the authentic gold-leaf Tanjore Painting technique.',
                'Overnight Stay: Premium Luxury Resort, Tanjore.',
                'Meals Included: Breakfast & Traditional South Indian Royal Dinner.',
            ]),
            _day(5, 'TANJORE TO MADURAI', ('Depart for Madurai, one of the oldest continuously inhabited cities in the world. Check into your premium resort situated on the peaceful slopes of Pasumalai. In the evening, visit the historic Thirumalai Nayakkar Mahal to witness a spectacular sound and light show narrating the royal history of the region.'), [
                'Sightseeing Included: Thirumalai Nayakkar Palace, Evening Cultural Light Show.',
                'Overnight Stay: Premium Handpicked Resort, Madurai.',
                'Meals Included: Breakfast & Gourmet Dinner.',
            ]),
            _day(6, 'MADURAI SOULFUL EXPLORATION', ('Begin your morning with a premium guided visit to the iconic Meenakshi Amman Temple. Beholding its massive intricately carved gopurams reaching toward the sky and explore the breathtaking Hall of a Thousand Pillars. Spend a relaxed afternoon exploring the historic markets of Madurai or relaxing at your luxury resort.'), [
                'Sightseeing Included: Meenakshi Amman Temple, Thousand Pillar Hall, Gandhi Memorial Museum.',
                'Food Suggestions: Try the famous local refreshing sweet beverage called Jigarthanda.',
                'Overnight Stay: Premium Luxury Resort, Madurai.',
                'Meals Included: Breakfast & Festive Dinner.',
            ]),
            _day(7, 'MADURAI TO OOTY', ('Leave the plains behind as your premium private vehicle begins a scenic climb up into the Nilgiri Hills. Pass through misty pine forests and sprawling tea gardens before arriving in beautiful Ooty. Check into your ultra-luxury colonial-style estate resort and unwind next to a cozy fireplace.'), [
                'Sightseeing Included: Nilgiri Mountain Scenic Drive, Tea Garden Viewpoints.',
                'Evening Experience: Premium tea-tasting experience overlooking the misty valleys.',
                'Overnight Stay: Premium Colonial Estate / Luxury Resort, Ooty.',
                'Meals Included: Breakfast & Warm Premium Dinner.',
            ]),
            _day(8, 'OOTY & COONOOR SIGHTSEEING', ("Enjoy a beautiful day exploring the best of Ooty and Coonoor. Board the historic UNESCO heritage Nilgiri Mountain Toy Train for a nostalgic, breathtaking ride down to Coonoor. Visit Sims Park and the spectacular Dolphin's Nose viewpoint before returning to Ooty to explore the lush Botanical Gardens."), [
                'Sightseeing Included: Ooty Botanical Gardens, Ooty Lake, Nilgiri Heritage Toy Train, Sims Park Coonoor.',
                "Photography Points: Panoramic views of tea plantations from Dolphin's Nose.",
                'Overnight Stay: Premium Colonial Estate, Ooty.',
                'Meals Included: Breakfast & Farewell Grand Dinner.',
            ]),
            _day(9, 'OOTY TO COIMBATORE DEPARTURE', ('Enjoy a slow breakfast while looking out over the misty hills. Pack your bags with beautiful souvenirs and memorable moments. Drive down to Coimbatore International Airport for your flight back home, bringing an end to your flawless Premium Tamil Nadu Experience handled with care by TRAGUIN.'), [
                'Transfers Included: Private Airport Drop-off at Coimbatore.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Chariot Beach Resort / Promenade Hotel Sterling Ooty Fern Hill', 'Heritage Route • Ooty', '08 Nights', 'Deluxe', 'Standard Room', 'MAPAI (Breakfast & Dinner)', 4, 1, description='OPTION 01 – DELUXE: Chariot Beach Resort / Promenade Hotel (Heritage Route) • Sterling Ooty Fern Hill (Ooty) — MAPAI (Breakfast & Dinner)'),
            _hotel('Radisson Blu Resort Temple Bay / Palais de Mahe / Savoy - IHCL SeleQtions', 'Heritage Route • Ooty', '08 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast & Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Radisson Blu Resort Temple Bay / Palais de Mahe (Heritage Route) • Savoy - IHCL SeleQtions (Ooty) — MAPAI (Breakfast & Dinner)'),
            _hotel('InterContinental Chennai / Heritage Madurai / WelcomHeritage Savoy Hotel', 'Heritage Route • Ooty', '08 Nights', 'Luxury', 'Luxury Room', 'MAPAI (Gourmet Meals)', 5, 3, description='OPTION 03 – LUXURY: InterContinental Chennai / Heritage Madurai (Heritage Route) • WelcomHeritage Savoy Hotel (Ooty) — MAPAI (Gourmet Meals)'),
            _hotel('The Leela Palace Chennai / Taj Pasumalai Madurai / The Tamara Ooty (Luxury Suite)', 'Heritage Route • Ooty', '08 Nights', 'Ultra Luxury', 'Luxury Suite', 'Luxury MAPAI Premium', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Leela Palace Chennai / Taj Pasumalai Madurai (Heritage Route) • The Tamara Ooty (Luxury Suite) — Luxury MAPAI Premium'),
        ],
        inclusions=[
            _inc_included('Accommodation: 08 Nights stay in handpicked premium luxury hotels and heritage properties.', 1),
            _inc_included('Meals: Daily multi-cuisine breakfast spreads and curated gourmet dinners included.', 2),
            _inc_included('Transfers & Sightseeing: Entire journey covered by a dedicated luxury air-conditioned Innova Crysta.', 3),
            _inc_included('TRAGUIN Support: 24/7 priority concierge assistance and certified regional guides.', 4),
            _inc_included('Complimentary Experiences: Private gold-leaf painting session in Tanjore and confirmed tickets for the Nilgiri Toy Train.', 5),
            _inc_included('Welcome Amenities: Premium arrival kit containing traditional stoles, organic refreshments, and wet tissues.', 6),
            _inc_excluded('Domestic or international airfare to Chennai and from Coimbatore.', 7),
            _inc_excluded('Direct entry tickets to monuments or camera charges unless specified.', 8),
            _inc_excluded('Personal expenses such as laundry, phone calls, room service, or tips.', 9),
            _inc_excluded('Any optional adventure activities or vehicle extensions.', 10),
        ],
    )
    return package, itinerary

def build_tn_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-010'
    tour_code = 'TRAGUIN-TN-010'
    title = 'Queen of Hills Ooty Special'
    duration = '03 Nights / 04 Days'
    slug = 'tn-010-queen-of-hills-ooty-special'
    itin_slug = 'tn-010-queen-of-hills-ooty-special-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu / India | Category: Leisure', 2),
            _ph('Destinations: Ooty • Coonoor', 3),
            _ph('Ideal for: Families, Couples & Senior Citizens', 4),
            _ph('Best season: October to June', 5),
            _ph('Travel Vehicle: Private Air-Conditioned Luxury Sedan / Sedan Utility (Chauffeur-Driven)', 6),
            _ph('Meal Plan: Modified American Plan (Gourmet Breakfasts & Dinners Included)', 7),
            _ph('Route Map: Coimbatore Arrival → Ooty Hills → Coonoor Day Excursion → Coimbatore Departure', 8),
            _ph('TRAGUIN Curated Experience Note: This premium getaway focuses on relaxed travel pacing, handpicked high-end hotels, private heritage tea factory access, and tailored assistance to avoid heavy tourist queues.', 9),
            _ph('TRAGUIN Signature Experience: Hand-crafted by TRAGUIN specialists to prioritize premium hospitality and seamless transit. Enjoy pre-cleared hotel check-ins, top-vetted properties, expert drivers who double as destination companions, and access to private vantage points away from crowded queues.', 10),
            _ph('Shopping & Local Nilgiri Experiences: Commercial Road & Charring Cross: Purchase authentic Nilgiri orthodox black tea, homemade gourmet truffles, and aromatic eucalyptus oils. Toda Artisans: Discover the unique and intricately sewn red-and-black traditional handloom embroidery crafted by local Toda artisans.', 11),
            _ph('Important Notes: Booking Policy: Standard resort check-in begins at 14:00 hours, and check-out is fixed at 11:00 hours. Early check-in remains subject to premium property availability. Weather Guidance: Ooty maintains a crisp and chilly climate year-round. It is highly recommended to carry warm layers or cardigans for early mornings and late evenings. Toy Train Operations: Nilgiri Mountain Railway operations depend on seasonal weather conditions and scheduling clear-outs by southern railway authorities.', 12),
        ],
        moods=['Family', 'Hills', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='TRAGUIN Premium Tamil Nadu Tour • Queen of Hills Ooty Special • 03 Nights / 04 Days',
        overview=('Welcome to the mesmerizing Nilgiris, where misty mountain peaks embrace rolling tea fields. This luxury holiday plan, curated meticulously by TRAGUIN travel consultants, invites you to unravel the timeless charm of Ooty and Coonoor. Savor breathtaking landscapes, exquisite colonial bungalows, and tranquil botanical vistas on this private holiday designed to promise unforgettable memories.\n\nTOUR OVERVIEW\nTravel Vehicle: Private Air-Conditioned Luxury Sedan / Sedan Utility (Chauffeur-Driven)\nMeal Plan: Modified American Plan (Gourmet Breakfasts & Dinners Included)\nRoute Map: Coimbatore Arrival → Ooty Hills → Coonoor Day Excursion → Coimbatore Departure\n\nTRAGUIN Curated Experience Note:\nThis premium getaway focuses on relaxed travel pacing, handpicked high-end hotels, private heritage tea factory access, and tailored assistance to avoid heavy tourist queues.\n\nHailed globally as the Queen of Hills, Ooty in Tamil Nadu remains a timeless treasure trove of scenic beauty, emerald lakes, and misty colonial heritage.'),
        seo_title='TN-010 | Queen of Hills Ooty Special | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Tamil Nadu package (TN-010 / TRAGUIN-TN-010): Ooty, Coonoor hill station tour with Nilgiri Toy Train and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Government Botanical Garden, Rose Garden, Doddabetta Peak, and Telescope House', 1),
            _ih("Heritage Nilgiri Mountain Railway Toy Train, Sim's Park, Dolphin's Nose, and Private Tea Factory", 2),
            _ih('Scenic Mountain Drive, Ooty Lake Leisure Walk, and Pykara Lake', 3),
            _ih('TRAGUIN Signature Experience with pre-booked Toy Train tickets and private estate tea lounge tasting', 4),
            _ih('Premium 4-tier handpicked accommodation in Ooty', 5),
        ],
        days=[
            _day(1, 'COIMBATORE TO OOTY', ('Arrive at Coimbatore International Airport or Railway Station where your elite TRAGUIN chauffeur welcomes you. Board your private vehicle and embark on a picturesque road journey to Ooty. Watch the dense plains give way to 36 sweeping hairpin curves lined with rich reserve forests and wild aromatic orchards. Upon arrival, check in smoothly to your premium resort and spend a relaxed evening walking through manicured garden lawns.'), [
                'Sightseeing Included: Scenic Mountain Drive, Ooty Lake Leisure Walk.',
                'Evening Experience: Sip warm Nilgiri spice tea during a personal welcome briefing by your coordinator.',
                'Overnight Stay: Handpicked Luxury Resort, Ooty.',
                'Meals Included: Welcome Amenity & Gourmet Buffet Dinner.',
            ]),
            _day(2, 'OOTY SIGHTSEEING', ("Savor a luxurious breakfast overlooking the cloud-kissed valley. Today, your curated itinerary unveils Ooty's historical wonders. Tour the 22-hectare Government Botanical Garden, which features a 20-million-year-old fossilized tree trunk. Next, wander through the terraced layout of the Ooty Rose Garden, home to thousands of rare rose varieties. Conclude the afternoon by driving up to Doddabetta Peak—the highest vantage point in South India—for a panoramic vista of the misty ranges."), [
                'Sightseeing Included: Government Botanical Garden, Rose Garden, Doddabetta Peak, Telescope House.',
                'Photography Points: The symmetrical flower terraces and panoramic blue-mountain vistas from Doddabetta.',
                'Overnight Stay: Handpicked Luxury Resort, Ooty.',
                'Meals Included: Full Buffet Breakfast & Fine Dining Dinner.',
            ]),
            _day(3, 'COONOOR DAY EXCURSION', ("Today brings an immersive cultural experience. Board the iconic Nilgiri Mountain Railway Toy Train (UNESCO World Heritage Site) for a historic ride through tunnels and dark ravines down to Coonoor. Your private vehicle meets you at Coonoor station to explore Sim's Park and the dramatic drop of Dolphin's Nose. Spend the afternoon inside a handpicked private tea estate to witness how fine orthodox tea leaves are expertly hand-rolled, ending with an exclusive blend-tasting experience."), [
                "Sightseeing Included: Heritage Toy Train Ride, Sim's Park, Dolphin's Nose, Private Tea Factory.",
                "Optional Activities: Guided forest walk around the parameters of Coonoor's old colonial estates.",
                'Overnight Stay: Handpicked Luxury Resort, Ooty.',
                'Meals Included: Full Breakfast & Farewell Dinner.',
            ]),
            _day(4, 'OOTY TO COIMBATORE DEPARTURE', ('Enjoy a slow breakfast at the resort while catching the soft morning sun. Check out of your room and visit the peaceful Pykara Lake if your flight schedule allows. Your premium vehicle will carry you back to Coimbatore International Airport, bringing your seamless TRAGUIN Tamil Nadu Package to a beautiful close as you carry home lifelong memories.'), [
                'Transfers Included: Private Luxury Airport / Station Transfer.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Gem Park, Ooty', 'Ooty', '03 Nights', 'Deluxe', 'Deluxe Valley View Room', 'MAP (Breakfast + Dinner)', 4, 1, description='OPTION 01 – DELUXE: Gem Park, Ooty — Deluxe Valley View Room — MAP (Breakfast + Dinner)'),
            _hotel('Fortune Resort Sullivan Court', 'Ooty', '03 Nights', 'Premium', 'Premium Room', 'MAP (Breakfast + Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Fortune Resort Sullivan Court — Premium Room — MAP (Breakfast + Dinner)'),
            _hotel('Savoy - IHCL SeleQtions', 'Ooty', '03 Nights', 'Luxury', 'Heritage Premium Room', 'MAP (Breakfast + Dinner)', 5, 3, description='OPTION 03 – LUXURY: Savoy - IHCL SeleQtions — Heritage Premium Room — MAP (Breakfast + Dinner)'),
            _hotel('WelcomHeritage Fernhills Royal Palace', 'Ooty', '03 Nights', 'Ultra Luxury', 'Royal Luxury Suite', 'MAP Luxury Dining Plan', 5, 4, description='OPTION 04 – ULTRA LUXURY: WelcomHeritage Fernhills Royal Palace — Royal Luxury Suite — MAP Luxury Dining Plan'),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at handpicked premium luxury properties with panoramic views.', 1),
            _inc_included('Meals: 03 Buffet Breakfasts and 03 specially prepared gourmet dinners at the resorts.', 2),
            _inc_included('Transfers & Sightseeing: All drives and sightseeing conducted via a dedicated private luxury sedan or premium utility vehicle.', 3),
            _inc_included('TRAGUIN Support: 24/7 prioritized destination concierge care and assistance.', 4),
            _inc_included('Welcome Amenities: Personalized hill station travel kit featuring local essential oils, gourmet chocolates, and bottled spring water.', 5),
            _inc_included('Complimentary Experiences: Pre-booked heritage Nilgiri Toy Train tickets and a private estate tea lounge tasting tour.', 6),
            _inc_excluded('Airfare or interstate rail travel tickets to Coimbatore.', 7),
            _inc_excluded('Individual entry tickets for botanical gardens or special photography passes.', 8),
            _inc_excluded('Personal laundry, room service orders, tips, and signature alcoholic beverages.', 9),
            _inc_excluded('Optional off-route tours or extended use of the vehicle outside standard hours.', 10),
        ],
    )
    return package, itinerary

def build_tn_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-011'
    tour_code = 'TRAGUIN-TN-011'
    title = 'Kodaikanal • Princess of Hills Escape'
    duration = '03 Nights / 04 Days'
    slug = 'tn-011-kodaikanal-princess-of-hills-escape'
    itin_slug = 'tn-011-kodaikanal-princess-of-hills-escape-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu / India | Category: Leisure Vacation', 2),
            _ph('Destinations: Kodaikanal (Princess of Hills)', 3),
            _ph('Ideal for: Families, Couples & Leisure Seekers', 4),
            _ph('Best season: October to March (Pleasant all year)', 5),
            _ph('Vehicle Allocated: Luxury Private Air-Conditioned Sedan / SUV (Innova Crysta)', 6),
            _ph('Meal Plan: Modified American Plan (Daily Buffet Breakfast & Gourmet Dinners)', 7),
            _ph('Route Map: Madurai/Coimbatore Arrival → Kodaikanal Hills Exploration → Madurai/Coimbatore Departure', 8),
            _ph('TRAGUIN Curated Experience Note: This signature escape offers premium stays combined with exclusive personalized assistance. Features private lakeside boating arrangements, customized heritage plantation walks, and local culinary discoveries.', 9),
            _ph('TRAGUIN Signature Experience: Handcrafted by travel experts to avoid rushing, providing a seamless blend of leisure and immersive exploration. Benefit from direct room upgrades (subject to availability), premium luxury transportation, and carefully vetted destination experiences.', 10),
            _ph('Shopping & Local Specialties: Handmade Chocolates: Indulge in rich, local dark chocolates, white almond varieties, and mint truffles. Essential Oils & Spices: Buy premium organic Eucalyptus oil, Lemongrass extract, and fresh hill spices like cardamom and pepper.', 11),
            _ph('Important Notes: Hotel Policies: Vetted standard check-in time is 14:00 hrs and check-out is 11:00 hrs. Early access depends on room availability. Weather Conditions: Kodaikanal maintains a cool climate. Carrying light woolen clothes or cardigans is highly recommended all year round. Advance Booking: Peak summer and winter periods see significant demand. Early confirmation ensures premium villa category retention.', 12),
        ],
        moods=['Family', 'Hills', 'Leisure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='TRAGUIN Premium Tamil Nadu Tour • Kodaikanal • Princess of Hills Escape • 03 Nights / 04 Days',
        overview=("Escape into the misty valleys, dense shola forests, and pristine lakeside trails of South India's ultimate hill retreat. Curated carefully by TRAGUIN experts, this exclusive itinerary highlights the serene beauty and panoramic vistas of Kodaikanal. Prepare yourself for immersive experiences, handpicked hotels, and breathtaking landscapes that stay etched in your memory forever.\n\nTOUR OVERVIEW\nVehicle Allocated: Luxury Private Air-Conditioned Sedan / SUV (Innova Crysta)\nMeal Plan: Modified American Plan (Daily Buffet Breakfast & Gourmet Dinners)\nRoute Map: Madurai/Coimbatore Arrival → Kodaikanal Hills Exploration → Madurai/Coimbatore Departure\n\nTRAGUIN Curated Experience Note:\nThis signature escape offers premium stays combined with exclusive personalized assistance. Features private lakeside boating arrangements, customized heritage plantation walks, and local culinary discoveries."),
        seo_title='TN-011 | Kodaikanal Princess of Hills Escape | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Tamil Nadu package (TN-011 / TRAGUIN-TN-011): Kodaikanal hill station escape with private row-boat ride and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Coaker's Walk, Bryant Park, Pillar Rocks, Guna Caves, and Kodaikanal Lake private row-boat cruise", 1),
            _ih('Pine Forest, Green Valley View (Suicide Point), Kurinji Andavar Temple, and Berijam Lake', 2),
            _ih('Scenic Mountain Drive and Silver Cascade Waterfalls en route', 3),
            _ih('TRAGUIN Signature Experience with tailored row-boat ride and private guided spice-market exploration', 4),
            _ih('Premium 4-tier handpicked accommodation in Kodaikanal', 5),
        ],
        days=[
            _day(1, 'ARRIVAL & DRIVE TO KODAIKANAL', ('Arrive at Madurai or Coimbatore airport/railway station where your professional TRAGUIN driver greets you with custom welcome amenities. Board your premium luxury transportation and begin a scenic uphill journey through winding mountain roads and lush valleys. Feel the air turn wonderfully crisp as you ascend into the Palani Hills. Check into your handpicked premium resort and spend the evening enjoying the peaceful mountain ambiance at your leisure.'), [
                'Sightseeing Included: Scenic Mountain Drive, Silver Cascade Waterfalls en route.',
                'Evening Experience: A warm welcome high-tea served by the resort overlooking misty valleys.',
                'Overnight Stay: Handpicked Luxury Resort, Kodaikanal.',
                'Meals Included: Welcome Drink & Gourmet Dinner.',
            ]),
            _day(2, 'KODAIKANAL SIGHTSEEING EXTRAVAGANZA', ("After a luxurious breakfast, step out for a comprehensive Kodaikanal Sightseeing experience. Stroll along the edge of Coaker's Walk, a pedestrian pathway providing spectacular panoramic views of the plains. Next, visit the magnificent Pillar Rocks—three vertical granite boulders standing majestic at a height of 400 feet. Spend your afternoon at the iconic star-shaped Kodaikanal Lake, enjoying a private row-boat cruise curated by TRAGUIN experts."), [
                "Sightseeing Included: Coaker's Walk, Bryant Park, Pillar Rocks, Guna Caves, Kodaikanal Lake.",
                'Photography Points: Misty backdrop of Pillar Rocks and sunset views over the serene lake waters.',
                'Overnight Stay: Premium Luxury Resort, Kodaikanal.',
                'Meals Included: Full Buffet Breakfast & Dinner.',
            ]),
            _day(3, 'HIDDEN GEMS & FOREST TRAILS', ('Today is dedicated to exploring the serene nature paths of Kodaikanal. Wander through the towering rows of the Pine Forest, one of the most popular Instagram spots in Tamil Nadu. Continue your drive to the tranquil Berijam Lake (subject to forest department permits), located deep inside a protected ecosystem. In the evening, visit local heritage lanes to discover quaint cafes and witness a live artisan presentation of homemade chocolate crafting.'), [
                'Sightseeing Included: Pine Forest, Green Valley View (Suicide Point), Kurinji Andavar Temple.',
                'Local Experiences: Private chocolate tasting and spice shopping trail.',
                'Overnight Stay: Handpicked Luxury Resort, Kodaikanal.',
                'Meals Included: Full Buffet Breakfast & Dinner.',
            ]),
            _day(4, 'KODAIKANAL TO DEPARTURE', ('Wake up to a crisp mountain morning and enjoy a relaxed breakfast. Wrap up your packing and check out of your resort. Your private premium vehicle will arrive to transfer you comfortably back down the hills to Madurai or Coimbatore for your onward flight or train home. Your luxury TRAGUIN Kodaikanal Package finishes with beautiful, lifelong memories.'), [
                'Transfers Included: Private Luxury Airport / Station Drop-off.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Carlton Kodaikanal', 'Kodaikanal', '03 Nights', 'Deluxe', 'Deluxe Lake View Room', 'MAPAI (Breakfast + Dinner)', 4, 1, description='OPTION 01 – DELUXE: The Carlton Kodaikanal — Deluxe Lake View Room — MAPAI (Breakfast + Dinner)'),
            _hotel('Le Poshe by Sparsa', 'Kodaikanal', '03 Nights', 'Premium', 'Premium Valley Suite', 'MAPAI (Breakfast + Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Le Poshe by Sparsa — Premium Valley Suite — MAPAI (Breakfast + Dinner)'),
            _hotel('The Tamara Kodaikanal', 'Kodaikanal', '03 Nights', 'Luxury', 'Luxury Suite', 'MAPAI (Breakfast + Dinner)', 5, 3, description='OPTION 03 – LUXURY: The Tamara Kodaikanal — Luxury Suite — MAPAI (Breakfast + Dinner)'),
            _hotel('The Tamara Kodaikanal', 'Kodaikanal', '03 Nights', 'Ultra Luxury', 'Super Premium Neelakurinji Suite', 'MAPAI + Private Bonfire', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Tamara Kodaikanal — Super Premium Neelakurinji Suite — MAPAI + Private Bonfire'),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at premium handpicked hotels and luxury hillside resorts.', 1),
            _inc_included('Meals: 03 Luxury Buffet Breakfasts and 03 curated multi-cuisine dinners at the resort.', 2),
            _inc_included('Transfers & Sightseeing: Entire journey covered via private air-conditioned luxury Innova Crysta.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated remote concierge assistance and personalized on-ground updates.', 4),
            _inc_included('Complimentary Experiences: Tailored row-boat ride at Kodaikanal Lake and a private guided spice-market exploration.', 5),
            _inc_included('Welcome Amenities: Refreshing herbal travel kit, local organic tea samples, and packed mineral water.', 6),
            _inc_excluded('Airfare or interstate train tickets to Madurai/Coimbatore.', 7),
            _inc_excluded('Entry tickets to monuments, forest parks, and camera permissions.', 8),
            _inc_excluded('Personal charges like room service, laundry, telephone calls, and gratuities.', 9),
            _inc_excluded('Optional adventure tours or night safari rides.', 10),
            _inc_excluded('Personal travel and medical insurance covers.', 11),
        ],
    )
    return package, itinerary

def build_tn_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-012'
    tour_code = 'TRAGUIN-TN-012'
    title = 'Madurai & Tanjore Temple Architecture Special'
    duration = '04 Nights / 05 Days'
    slug = 'tn-012-madurai-tanjore-temple-architecture-special'
    itin_slug = 'tn-012-madurai-tanjore-temple-architecture-special-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu, India | Category: Culture & Architecture', 2),
            _ph('Destinations: Madurai • Thanjavur (Tanjore) • Trichy', 3),
            _ph('Ideal for: Heritage Enthusiasts & Families', 4),
            _ph('Best season: October to March', 5),
            _ph('Vehicle Allocated: Dedicated Luxury AC Chauffeur Sedan / Innova Crysta', 6),
            _ph('Meal Plan: Daily Multi-Cuisine Premium Breakfast & Specialized Dinners', 7),
            _ph('Route Map: Madurai Arrival & Sightseeing → Trichy Landmarks → Thanjavur Heritage → Trichy/Madurai Departure', 8),
            _ph('TRAGUIN Curated Experience Note: Includes VIP fast-track temple entry access, private expert heritage guides, exclusive bronze casting artisan workshop visits, and premium handpicked hotels reflecting authentic cultural luxury.', 9),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this itinerary features verified local historians, seamless queue management at top landmarks, and private handicraft studio access. Enjoy handpicked boutique accommodations, dedicated luxury transportation, and highly responsive travel assistance every step of the way.', 10),
            _ph('Shopping & Local Heritage Souvenirs: Madurai Markets: Procure genuine hand-woven Madurai Sungudi sarees and fragrant local jasmine garlands. Thanjavur Handicrafts: Invest in timeless 22-karat gold foil Tanjore Paintings, brass lamps, or authentic bronze statuettes.', 11),
            _ph('Important Notes: Dress Codes: Traditional, conservative attire covering shoulders and knees is mandatory for temple entry in Tamil Nadu. Hotel Policies: Check-in is at 14:00 hrs; check-out at 11:00 hrs. Early access requests depend strictly on room availability. Seasonal Advice: Monuments feature stone pavements; soft slip-on footwear and cotton socks are suggested for daytime walking.', 12),
        ],
        moods=['Heritage', 'Culture', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Best Tamil Nadu Tour Package • Madurai & Tanjore Temple Architecture Special • 04 Nights / 05 Days',
        overview=('Step into a living museum of ancient Dravidian legacy. Handcrafted with flawless precision by TRAGUIN, this signature itinerary unlocks the sacred architectural mysteries of the Chola and Pandya dynasties. Wander through towering gopurams, marvel at monolithic stone carvings, and relax in ultra-premium heritage stays while creating unforgettable memories of classical India.\n\nTOUR OVERVIEW\nVehicle Allocated: Dedicated Luxury AC Chauffeur Sedan / Innova Crysta\nMeal Plan: Daily Multi-Cuisine Premium Breakfast & Specialized Dinners\nRoute Map: Madurai Arrival & Sightseeing → Trichy Landmarks → Thanjavur Heritage → Trichy/Madurai Departure\n\nTRAGUIN Curated Experience Note:\nIncludes VIP fast-track temple entry access, private expert heritage guides, exclusive bronze casting artisan workshop visits, and premium handpicked hotels reflecting authentic cultural luxury.'),
        seo_title='TN-012 | Madurai Tanjore Temple Architecture Special | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Tamil Nadu package (TN-012 / TRAGUIN-TN-012): Madurai, Trichy, Thanjavur temple architecture tour with VIP shrine access and 4-tier accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Meenakshi Amman Temple Complex, Thirumalai Nayakkar Palace, and night ceremony', 1),
            _ih('Trichy Rockfort, Srirangam Temple Complex, and scenic highway drive', 2),
            _ih('Brihadeeswarar Temple UNESCO site, Maratha Palace, and gold-leaf Tanjore Painting demonstration', 3),
            _ih('TRAGUIN Signature Experience with fast-track VIP queue entries and artisan workshop tours', 4),
            _ih('Premium 4-tier handpicked accommodation across Madurai and Thanjavur', 5),
        ],
        days=[
            _day(1, 'MADURAI ARRIVAL', ("Arrive at Madurai International Airport or Railway Station. Receive a grand, personalized greeting by your private TRAGUIN chauffeur. Transfer in air-conditioned luxury to your handpicked premium hotel. After a seamless check-in, unwind inside your elite room. In the late afternoon, your private heritage guide will escort you to the legendary Meenakshi Amman Temple, admiring its 14 soaring gopurams encrusted with thousands of stone figures. Witness the emotional night ceremony where Lord Shiva is carried to Meenakshi's shrine amidst traditional chants and music."), [
                'Sightseeing Included: Meenakshi Amman Temple Complex, Late Evening Night Ceremony.',
                'Evening Experience: Private walking tour through the oil-lamp lit prakarams of the inner temple.',
                'Overnight Stay: Premium Luxury Heritage Hotel, Madurai.',
                'Meals Included: Welcome Drink & Gourmet Dinner.',
            ]),
            _day(2, 'MADURAI ARCHITECTURAL HIGHLIGHTS', ('Indulge in a premium South Indian breakfast. Today, explore the majestic Thirumalai Nayakkar Mahal, an architectural fusion of Italian, Islamic, and Dravidian styles. Stand awestruck among the massive white pillars that outline the grand courtyard. Next, visit the historic Vandiyur Mariamman Teppakulam tank, featuring a central island temple. Spend your afternoon exploring local handloom weavers specializing in traditional Sungudi silk sarees, an exclusive recommendations highlight by TRAGUIN experts.'), [
                'Sightseeing Included: Thirumalai Nayakkar Palace, Teppakulam, Gandhi Memorial Museum.',
                "Food Suggestions: Taste the iconic local cold dessert 'Jigarthanda' at a handpicked artisanal cafe.",
                'Overnight Stay: Premium Luxury Heritage Hotel, Madurai.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'MADURAI TO THANJAVUR VIA TRICHY', ("Following a delightful breakfast, check out and drive along smooth highways toward the imperial capital of the Cholas—Thanjavur. En route, pause at Tiruchirappalli (Trichy) for magnificent historical discoveries. Ascend the legendary Rockfort Ucchi Pillayar Temple, a structure carved directly from a 270-foot-high ancient rock. Follow this with a visit to the colossal Sri Ranganathaswamy Temple in Srirangam, celebrated as the world's largest functioning temple complex. Arrive in Thanjavur by evening and check in to your ultra-luxury estate stay."), [
                'Sightseeing Included: Trichy Rockfort, Srirangam Temple Complex, Scenic Highway Drive.',
                "Photography Points: Golden vimana views from Srirangam's white tower overlooks.",
                'Overnight Stay: Ultra Luxury Palace Resort, Thanjavur.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'THANJAVUR FULL DAY DISCOVERY', ('Devote your morning to the crowning achievement of medieval Indian engineering: the UNESCO World Heritage Brihadeeswarar Temple (The Big Temple). Your certified scholar guide will reveal how the 80-tonne single-stone granite kumbam was raised to the apex of the 216-foot vimana tower. Touch the cool, glass-smooth ancient frescoes inside the corridors. In the afternoon, visit the Thanjavur Maratha Palace Complex and its Saraswathi Mahal Library. Conclude with an immersive, private demonstration of traditional gold-leaf Tanjore Painting making.'), [
                'Sightseeing Included: Brihadeeswarar Temple, Maratha Palace, Royal Museum, Saraswathi Library.',
                'Exclusive Experiences: Private interaction with National Award-winning Chola bronze-casting artisans.',
                'Overnight Stay: Ultra Luxury Palace Resort, Thanjavur.',
                'Meals Included: Breakfast & Festive Traditional Thali Dinner.',
            ]),
            _day(5, 'THANJAVUR TO TRICHY / DEPARTURE', ('Savor a luxurious morning breakfast amidst the peaceful grounds of your palace resort. Collect your exclusive heritage souvenirs and check out. Your private chauffeur-driven luxury vehicle will transfer you comfortably to Trichy or Madurai Airport/Railway Station for your onward journey home. Your premium Tamil Nadu Honeymoon Package or cultural escape concludes with unforgettable memories orchestrated flawlessly by TRAGUIN.'), [
                'Transfers Included: Private Luxury Airport / Station Drop-off.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Heritage Madurai (Deluxe Room) / Hotel Sangam (Standard Room)', 'Madurai • Thanjavur', '04 Nights', 'Deluxe', 'Deluxe / Standard Room', 'CP (Breakfast Only)', 4, 1, description='OPTION 01 – DELUXE: Heritage Madurai (Deluxe Room) • Hotel Sangam (Standard Room) — CP (Breakfast Only)'),
            _hotel('The Gateway Hotel Pasumalai Madurai / Great Trails River View resort by GRT', 'Madurai • Thanjavur', '04 Nights', 'Premium', 'Premium Room', 'MAPAI (Breakfast + Dinner)', 4, 2, description='OPTION 02 – PREMIUM: The Gateway Hotel Pasumalai Madurai • Great Trails River View resort by GRT — MAPAI (Breakfast + Dinner)'),
            _hotel('Heritage Madurai (Luxury Villa) / Svatma - Heritage Boutique Hotel', 'Madurai • Thanjavur', '04 Nights', 'Luxury', 'Luxury Villa / Heritage Room', 'MAPAI (Breakfast + Dinner)', 5, 3, description='OPTION 03 – LUXURY: Heritage Madurai (Luxury Villa) • Svatma - Heritage Boutique Hotel — MAPAI (Breakfast + Dinner)'),
            _hotel('The Gateway Pasumalai (Executive Suite) / Svatma (Millennium Premium Suite)', 'Madurai • Thanjavur', '04 Nights', 'Ultra Luxury', 'Executive Suite / Millennium Premium Suite', 'Gourmet MAPAI + Experiences', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Gateway Pasumalai (Executive Suite) • Svatma (Millennium Premium Suite) — Gourmet MAPAI + Experiences'),
        ],
        inclusions=[
            _inc_included('Accommodation: 04 Nights stay across handpicked hotels and luxury heritage resorts.', 1),
            _inc_included('Meals: Daily premium breakfast buffet and signature culinary dinners included at all destinations.', 2),
            _inc_included('Transfers & Sightseeing: All point-to-point transfers via a private luxury chauffeur sedan or SUV.', 3),
            _inc_included('TRAGUIN Support: 24/7 priority concierge line and dedicated ground assistance.', 4),
            _inc_included('Welcome Amenities: Traditional silk-scarf greeting on arrival, fresh floral garlands, and premium mineral water.', 5),
            _inc_included('Complimentary Experiences: Fast-track VIP queue entries inside main shrines and dedicated artisan workshop tours.', 6),
            _inc_excluded('Flights, train fares, or interstate permit costs.', 7),
            _inc_excluded('Camera or video recording clearance tickets at monuments.', 8),
            _inc_excluded('Private religious offerings or custom ritual performance costs.', 9),
            _inc_excluded('Personal incidentals, alcoholic beverages, laundry services, or driver tipping.', 10),
        ],
    )
    return package, itinerary

def build_tn_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-013'
    tour_code = 'TRAGUIN-TN-013'
    title = 'Chettinad Mansion Culture Tour'
    duration = '03 Nights / 04 Days'
    slug = 'tn-013-chettinad-mansion-culture-tour'
    itin_slug = 'tn-013-chettinad-mansion-culture-tour-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu, India | Category: Heritage / Luxury Culture', 2),
            _ph('Destinations: Madurai • Karaikudi (Chettinad) • Kanadukathan', 3),
            _ph('Ideal for: Heritage Connoisseurs & Families', 4),
            _ph('Best season: October to March', 5),
            _ph('Vehicle Allocated: Chauffeur-driven Private Luxury AC Sedan / SUV (Innova Crysta)', 6),
            _ph('Meal Plan: Modified American Plan (Premium Breakfast & Authentic Local Dinners)', 7),
            _ph('Route Map: Madurai Arrival → Karaikudi (Chettinad Heritage Zone) → Athangudi Village → Madurai Departure', 8),
            _ph('TRAGUIN Curated Experience Note: This meticulously tailored itinerary provides a premium, low-fatigue experience perfect for culture lovers. Enjoy exclusive entry to private 19th-century merchant mansions, live tile-making art demonstrations, and custom culinary sessions.', 9),
            _ph('TRAGUIN Signature Experience: Curated carefully by TRAGUIN experts, this exclusive heritage journey blends luxury with absolute comfort. Enjoy guaranteed flexible check-in times, priority mansion suite upgrades whenever available, and specialized insider access to landmarks away from tourist crowds.', 10),
            _ph('Shopping & Local Experiences: Karaikudi Antique Shops: Discover marvelous authentic collectibles, old enamelware from Sweden, and premium Burmese teak carvings. Kandangi Sarees: Purchase gorgeous, traditional hand-woven cotton sarees directly from local master weavers.', 11),
            _ph('Important Notes: Hotel Policies: Check-in time is generally 14:00 hrs and check-out is 11:00 hrs. Early check-in remains subject to premium resort availability. Dress Code: When visiting the sacred Madurai Meenakshi Temple, traditional attire is mandatory (sarees/salwars for women, dhotis/formal trousers for men). Weather Guide: The local climate is pleasant during winter months. Light cotton wear is highly recommended for daytime walks.', 12),
        ],
        moods=['Heritage', 'Culture', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Chettinad Mansion Culture Tour • Madurai • Karaikudi • Kanadukathan • Athangudi • 03 Nights / 04 Days',
        overview=("Step into an era of grand merchant palaces and timeless architectural marvels. Curated with absolute perfection by TRAGUIN, this exclusive luxury holiday welcomes you to the heart of Tamil Nadu's architectural royalty. From the towering gopurams of Madurai to the palatial, sun-drenched courtyards of handpicked heritage mansions in Chettinad, every moment promises immersive experiences, breathtaking landscapes, and unforgettable memories.\n\nTOUR OVERVIEW\nVehicle Allocated: Chauffeur-driven Private Luxury AC Sedan / SUV (Innova Crysta)\nMeal Plan: Modified American Plan (Premium Breakfast & Authentic Local Dinners)\nRoute Map: Madurai Arrival → Karaikudi (Chettinad Heritage Zone) → Athangudi Village → Madurai Departure\n\nTRAGUIN Curated Experience Note:\nThis meticulously tailored itinerary provides a premium, low-fatigue experience perfect for culture lovers. Enjoy exclusive entry to private 19th-century merchant mansions, live tile-making art demonstrations, and custom culinary sessions."),
        seo_title='TN-013 | Chettinad Mansion Culture Tour | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Tamil Nadu package (TN-013 / TRAGUIN-TN-013): Madurai, Chettinad heritage mansions, Athangudi tiles, and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Kanadukathan Heritage Lane, Private Mansion Tour, Antique Market, and folk performance', 1),
            _ih('Athangudi Tile Workshop, Athangudi Palace, and Kandangi Weaving Center', 2),
            _ih('Madurai Meenakshi Temple, Thirumalai Nayakkar Palace, and heritage architectural orientation', 3),
            _ih('TRAGUIN Signature Experience with exclusive mansion entry and live tile-making demonstration', 4),
            _ih('Premium 4-tier handpicked heritage mansion accommodation in Karaikudi', 5),
        ],
        days=[
            _day(1, 'ARRIVAL IN MADURAI & TRANSFER TO CHETTINAD', ('Arrive at Madurai Airport or Railway Station where your professional TRAGUIN tour manager warmly welcomes you. Step into your premium luxury private vehicle and set off on a smooth, scenic route towards the magical heritage zone of Chettinad (Karaikudi). Check in effortlessly to your handpicked ultra-luxury heritage mansion hotel. Spend the afternoon soaking in the palatial atmosphere, admiring teak pillars from Burma, Italian marble floors, and Belgian glass features. In the evening, witness a captivating traditional folk performance inside the central courtyard.'), [
                'Sightseeing Included: Scenic Countryside Drive, Traditional Mansion Welcome.',
                'Evening Experience: Indulge in an exclusive high-tea session followed by a heritage architectural orientation by our local experts.',
                'Overnight Stay: Handpicked Luxury Heritage Mansion, Karaikudi.',
                'Meals Included: Welcome Drink & Gourmet Dinner.',
            ]),
            _day(2, 'CHETTINAD MANSION & VILLAGE TOUR', ('Savor a luxurious traditional breakfast before exploring the majestic town of Kanadukathan. Gaze upon the iconic architecture of the grand Chettinad Palace, a stunning masterclass of symmetry and engineering. Take a slow, immersive walk along heritage lanes lined with majestic mansions, learning about the fascinating global trade history of the Chettiar community. In the afternoon, visit the famous local antique markets of Karaikudi to see magnificent collectibles, imported glassware, and vintage wooden carvings.'), [
                'Sightseeing Included: Kanadukathan Heritage Lane, Private Mansion Tour, Antique Market.',
                'Photography Points: The breathtaking endless linear courtyards and carved ornate main doorways of Kanadukathan.',
                'Overnight Stay: Handpicked Luxury Heritage Mansion, Karaikudi.',
                'Meals Included: Full Buffet Breakfast & Authentic Multi-course Chettinad Dinner.',
            ]),
            _day(3, 'ATHANGUDI TILES & HANDLOOM WEAVING', ('Today features the centerpiece of your cultural immersion. Travel to the heritage village of Athangudi, world-renowned for its beautiful, uniquely patterned, and polished handmade clay tiles. Witness an exclusive, live step-by-step masterclass by third-generation local artisans who craft these beautiful eco-friendly tiles using local soil and glass molds. Later, visit a traditional handloom center to observe the painstaking creation of the famous, vibrant Kandangi cotton sarees.'), [
                'Sightseeing Included: Athangudi Tile Workshop, Athangudi Palace, Kandangi Weaving Center.',
                "Optional Activities: Participate in a private culinary demonstration with the mansion's master chef to understand local spice blend secrets.",
                'Overnight Stay: Handpicked Luxury Heritage Mansion, Karaikudi.',
                'Meals Included: Full Breakfast & Festive Farewell Dinner.',
            ]),
            _day(4, 'MADURAI SIGHTSEEING & DEPARTURE', ('After a beautiful morning breakfast, check out and drive back towards the historic city of Madurai. Enjoy a premium, comfortable visit to the majestic Meenakshi Amman Temple, admiring its breathtaking 14 towering gopurams and the magnificent Thousand Pillar Hall. Afterward, visit the historic Thirumalai Nayakkar Mahal palace. Your luxury private vehicle will then transfer you smoothly to Madurai Airport or Railway Station for your return journey, concluding your magnificent holiday.'), [
                'Sightseeing Included: Madurai Meenakshi Temple, Thirumalai Nayakkar Palace, Airport/Station Drop-off.',
                'Meals Included: Full Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('The Bangala, Karaikudi', 'Karaikudi (Chettinad)', '03 Nights', 'Deluxe', 'Heritage Standard Room', 'MAPAI (Breakfast + Dinner)', 4, 1, description='OPTION 01 – DELUXE: The Bangala, Karaikudi — Heritage Standard Room — MAPAI (Breakfast + Dinner)'),
            _hotel('Chidambara Vilas, Kadiapatti', 'Karaikudi (Chettinad)', '03 Nights', 'Premium', 'Heritage Deluxe Suite', 'MAPAI (Breakfast + Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Chidambara Vilas, Kadiapatti — Heritage Deluxe Suite — MAPAI (Breakfast + Dinner)'),
            _hotel('Visalam - CGH Earth, Karaikudi', 'Karaikudi (Chettinad)', '03 Nights', 'Luxury', 'Heritage Mansion Room', 'MAPAI (Breakfast + Dinner)', 5, 3, description='OPTION 03 – LUXURY: Visalam - CGH Earth, Karaikudi — Heritage Mansion Room — MAPAI (Breakfast + Dinner)'),
            _hotel('Mantra Kulam / Custom Private Villa Stay', 'Karaikudi (Chettinad)', '03 Nights', 'Ultra Luxury', 'Palatial Royal Suite', 'MAPAI + Private Chef Experience', 5, 4, description='OPTION 04 – ULTRA LUXURY: Mantra Kulam / Custom Private Villa Stay — Palatial Royal Suite — MAPAI + Private Chef Experience'),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at award-winning premium luxury heritage hotel properties.', 1),
            _inc_included('Meals: 03 Lavish Buffet Breakfasts and 03 curated local dinners at the hotels.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated private chauffeur-driven AC Luxury Innova Crysta for all transfers and landmarks.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated telephone concierge assistance and certified guide companions.', 4),
            _inc_included('Complimentary Experiences: Exclusive live Athangudi tile-making demonstration and private textile handloom village tour.', 5),
            _inc_included('Welcome Amenities: Personalized heritage travel welcome kit containing hand-crafted notebooks, immunity waters, and traditional stoles.', 6),
            _inc_excluded('Airfare or interstate train tickets to and from Madurai.', 7),
            _inc_excluded('Monument entrance fees, video camera permits, or local temple fast-track tickets.', 8),
            _inc_excluded('Personal expenses such as laundry, specialty boutique shopping, tips, and minibar charges.', 9),
            _inc_excluded('Optional culinary workshop materials or extra vehicle usage outside the planned path.', 10),
            _inc_excluded('Travel insurance or medical companion fees.', 11),
        ],
    )
    return package, itinerary

def build_tn_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-014'
    tour_code = 'TRAGUIN-TN-014'
    title = 'Mahabalipuram Luxury Surf Stay'
    duration = '02 Nights / 03 Days'
    slug = 'tn-014-mahabalipuram-luxury-surf-stay'
    itin_slug = 'tn-014-mahabalipuram-luxury-surf-stay-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu / India | Category: Beach / Luxury Surf Stay', 2),
            _ph('Destinations: Mahabalipuram Beach', 3),
            _ph('Ideal for: Luxury Travelers & Surf Enthusiasts', 4),
            _ph('Best season: October to March', 5),
            _ph('Starting price: On Request (Premium)', 6),
            _ph('Vehicle Allocated: Private Air-Conditioned Chauffeur-driven Luxury Sedan / SUV', 7),
            _ph('Meal Plan: Modified American Plan (Daily Breakfast & Gourmet Seafood Dinners)', 8),
            _ph('Route Map: Chennai Arrival → Mahabalipuram Surf Resort → Chennai Departure', 9),
            _ph('TRAGUIN Curated Experience Note: Private surf lesson with international certified coaches and VIP access to seaside monuments.', 10),
            _ph('TRAGUIN Signature Experience: Private oceanfront dinners and exclusive surf sessions. Curated by TRAGUIN Experts: Handpicked hotels and meticulously checked beach routes. Personalized Assistance: Dedicated chauffeur and local specialized destination ambassadors. Exclusive Recommendations: Access to elite hidden beach cafes and local boutique sea-shell studios.', 11),
            _ph('Shopping & Local Experiences: Local Markets: Mahabalipuram Craft Village for hand-carved soapstone and granite sculptures. Famous Shopping Items: Elegant stone ornaments, intricate sea-shell curios, and local beach apparel. Cafes & Food Recommendations: Try authentic South Indian filter coffee or dine at surf-themed seaside shacks offering grilled tiger prawns. Instagram Spots: The majestic sunrise backdrop at the Shore Temple and atop the waves during your private surf lesson.', 12),
            _ph('Important Notes: Hotel Policies: Standard check-in is at 14:00 hours; early check-in is subject to premium resort occupancy. Weather Notes: Light, breezy cotton clothing is highly suggested. Always wear ocean-friendly sun protection. Seasonal Activities: Surfing quality is highly wave and tide-dependent; safety instructions from coaches must be followed. Advance Booking Suggestions: High-end luxury beach chalets fill up months in advance; early booking ensures priority allocation.', 13),
        ],
        moods=['Beach', 'Luxury', 'Adventure'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium)',
        rating=Decimal("4.9"), review_count=0,
        tagline='TRAGUIN Premium Tamil Nadu Tour • Mahabalipuram Luxury Surf Stay • 02 Nights / 03 Days',
        overview=('Welcome note: Bask in the ultra-luxury coastal vibes where heritage architecture seamlessly meets global surf culture. Curated exclusively by TRAGUIN, this private weekend escape in Tamil Nadu promises the finest boutique ocean-view accommodation, professional surf coaching, and pristine wellness therapies alongside breathtaking landscapes.\n\nTOUR OVERVIEW\nTravel Dates: Flexible / Custom FIT\nGroup / FIT: Customized Luxury Private Tour (FIT)\nVehicle Allocated: Private Air-Conditioned Chauffeur-driven Luxury Sedan / SUV\nMeal Plan: Modified American Plan (Daily Breakfast & Gourmet Seafood Dinners)\nRoute Map: Chennai Arrival → Mahabalipuram Surf Resort → Chennai Departure\n\nTRAGUIN Curated Experience Note: Private surf lesson with international certified coaches and VIP access to seaside monuments.'),
        seo_title='TN-014 | Mahabalipuram Luxury Surf Stay | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Tamil Nadu package (TN-014 / TRAGUIN-TN-014): Mahabalipuram luxury surf stay with private ISA-certified coaching and 4-tier beachfront accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Shore Temple sunset stroll, Private Beach Leisure, and candlelit oceanfront dinner', 1),
            _ih("Private ISA-certified surfing lesson, Five Rathas, Arjuna's Penance, Krishna's Butterball, and spa session", 2),
            _ih('Beachside sunrise yoga, meditation, and private beach walk', 3),
            _ih('TRAGUIN Signature Experience with private surf training and complementary spa resort voucher', 4),
            _ih('Premium 4-tier handpicked ocean-view accommodation in Mahabalipuram', 5),
        ],
        days=[
            _day(1, 'CHENNAI TO MAHABALIPURAM', ('Your premium coastal journey begins with a smooth pickup from Chennai Airport or your location in a private luxury vehicle. Cruise along the gorgeous East Coast Road (ECR), treating your eyes to scenic beauty and beautiful coastal vistas. Arrive at your handpicked ultra-luxury beachfront surf resort in Mahabalipuram. After a seamless private check-in, relax in your villa overlooking the Bay of Bengal. In the late afternoon, enjoy an exclusive guided Tamil Nadu Sightseeing stroll to the iconic Shore Temple, listening to emotional historical storytelling as the setting sun paints the ancient monolithic structures in hues of gold.'), [
                'Sightseeing Included: Shore Temple, Private Beach Leisure.',
                'Evening Experience: A premium candlelit oceanfront dinner featuring handpicked local catch and gourmet delicacies.',
                'Overnight Stay: Ultra-Luxury Surf Resort / Private Beach Villa, Mahabalipuram.',
                'Meals Included: Welcome Amenities & Dinner.',
            ]),
            _day(2, 'MAHABALIPURAM SURF ESCAPE', ("Awake to the soothing rhythm of crashing waves. Today promises an unforgettable immersive experience. Head to the beach for an exclusive, custom-tailored private surfing lesson led by ISA-certified international instructors. Perfect for beginners and advanced surfers alike, feel the exhilaration of riding the renowned waves of Mahabalipuram. After lunch, explore the top tourist places in Mahabalipuram including Five Rathas, Arjuna's Penance, and the gravity-defying Krishna's Butterball—all fantastic photography points for unforgettable memories. Conclude your day with a soothing deep-tissue spa session at the resort."), [
                "Sightseeing Included: Five Rathas, Arjuna's Penance, Krishna's Butterball.",
                'Optional Activities: Catamaran boat ride with local fishermen to see submerged temples.',
                'Evening Experience: A relaxing premium beach bonfire experience under a canopy of stars.',
                'Overnight Stay: Premium Ocean Villa, Mahabalipuram.',
                'Meals Included: Gourmet Breakfast & Dinner.',
            ]),
            _day(3, 'MAHABALIPURAM TO CHENNAI', ("Greet the morning dawn with a curated beachside sunrise yoga and meditation session. Enjoy a final lavish buffet breakfast at the resort's open-air pavilion. Take a leisurely walk along the private beach or buy unique stone carvings from local artisans. Later, pack your memories as your luxury vehicle transfers you comfortably back to Chennai Airport or your preferred destination, concluding your highly polished premium travel experience."), [
                'Transfers Included: Chauffeur-driven Private Luxury Transfer to Chennai.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Chariot Beach Resort', 'Mahabalipuram', '02 Nights', 'Deluxe', 'Sea View Room', 'Breakfast & Dinner (MAP)', 4, 1, description='OPTION 01 – DELUXE: Chariot Beach Resort — Sea View Room — Breakfast & Dinner (MAP)'),
            _hotel('Radisson Blu Resort Temple Bay', 'Mahabalipuram', '02 Nights', 'Premium', 'Chalet Ocean View', 'Breakfast & Dinner (MAP)', 4, 2, description='OPTION 02 – PREMIUM: Radisson Blu Resort Temple Bay — Chalet Ocean View — Breakfast & Dinner (MAP)'),
            _hotel('InterContinental Chennai Mahabalipuram Resort', 'Mahabalipuram', '02 Nights', 'Luxury', 'Resort Sea View Room', 'Breakfast & Dinner (MAP)', 5, 3, description='OPTION 03 – LUXURY: InterContinental Chennai Mahabalipuram Resort — Resort Sea View Room — Breakfast & Dinner (MAP)'),
            _hotel("Taj Fisherman's Cove Resort & Spa", 'Mahabalipuram', '02 Nights', 'Ultra Luxury', 'Luxury Beach Villa with Private Plunge Pool', 'Ultra-Luxury Gourmet Meal Plan', 5, 4, description="OPTION 04 – ULTRA LUXURY: Taj Fisherman's Cove Resort & Spa — Luxury Beach Villa with Private Plunge Pool — Ultra-Luxury Gourmet Meal Plan"),
        ],
        inclusions=[
            _inc_included('Accommodation: 02 Nights stay in handpicked premium hotels / ultra-luxury resorts.', 1),
            _inc_included('Meals: Gourmet breakfasts and curated specialty coastal dinners.', 2),
            _inc_included('Transfers: All airport and city transfers using private luxury transportation.', 3),
            _inc_included('Sightseeing: Guided private tour of UNESCO world heritage shore attractions.', 4),
            _inc_included('Assistance & Taxes: 24/7 dedicated local concierge and all applicable government taxes.', 5),
            _inc_included('Welcome Amenities: Customized luxury welcome kit including coconut waters, cold towels, and wellness treats.', 6),
            _inc_included('Complimentary Experiences: Private 1-on-1 premium surf training and complementary spa resort voucher.', 7),
            _inc_included('TRAGUIN Support: Priority backend monitoring and emergency travel support.', 8),
            _inc_excluded('Flights, train fares, or interstate permit costs.', 9),
            _inc_excluded('Entry tickets to monuments or camera fees not specified.', 10),
            _inc_excluded('Personal expenses such as laundry, telephone calls, alcoholic beverages, and mini-bar.', 11),
            _inc_excluded('Insurance cover, medical expenses, and tipping.', 12),
            _inc_excluded('Optional tours, watersports, and activities not detailed in the itinerary.', 13),
        ],
    )
    return package, itinerary

def build_tn_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-015'
    tour_code = 'TRAGUIN-TN-015'
    title = 'Valparai Unexplored Western Ghats Luxury Holiday'
    duration = '03 Nights / 04 Days'
    slug = 'tn-015-valparai-unexplored-western-ghats-luxury-holiday'
    itin_slug = 'tn-015-valparai-unexplored-western-ghats-luxury-holiday-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu / India | Category: Offbeat Luxury / Nature & Wildlife', 2),
            _ph('Destinations: Coimbatore • Valparai • Sholayar • Athirapally Ext.', 3),
            _ph('Ideal for: Nature Lovers, Honeymooners, Corporate Groups', 4),
            _ph('Best season: September to March', 5),
            _ph('Starting price: On Request (Premium Custom)', 6),
            _ph('Vehicle Allocated: Private Luxury SUV (Chauffeur-Driven Innova Crysta)', 7),
            _ph('Meal Plan: Modified American Plan (Premium Breakfast & Dinners Included)', 8),
            _ph('Route Map: Coimbatore Arrival → Aliyar Dam → Valparai Hairpin Bends → Sholayar Dam → Coimbatore Departure', 9),
            _ph('TRAGUIN Curated Note: Includes private estate walks, hornbill spotting excursions, and elite plantation stays handpicked by experts.', 10),
            _ph('TRAGUIN Signature Experience: Curated by our elite destination experts, this route ensures a flawless balance of offbeat adventure and slow-paced luxury. Take advantage of our handpicked hidden viewpoints, direct private interactions with local estate naturalists, and top-tier luxury transportation throughout the Western Ghats.', 11),
            _ph('Shopping & Local Experiences: Premium Nilgiri Tea & Coffee: Purchase aromatic single-origin green, white, and black teas directly from local estate factories. Fresh Mountain Spices: Take home organic cardamom, clove, pepper, and pure honey sourced directly from forest hamlets. Instagram Spots: The endless green horizon at Nallamudi Viewpoint and the mist-laden paths of Monica Estate.', 12),
            _ph('Important Notes: Hotel Policies: Standard check-in is at 14:00 hrs; check-out is at 11:00 hrs. Early check-in or late check-out options are subject to seasonal occupancy. Weather Notes: Valparai maintains a refreshing cool climate throughout the year. Carrying light winter wear and umbrellas is highly recommended. Wildlife Protocol: Valparai is a sensitive eco-zone. Respect animal habitats, maintain safe distances, and strictly avoid night driving unless specified. Advance Booking: Heritage estate bungalows possess highly limited inventory. Advance reservation is highly recommended to secure premium categories.', 13),
        ],
        moods=['Nature', 'Wildlife', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Custom)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Best Tamil Nadu Tour Package • Valparai Unexplored Western Ghats Luxury Holiday • 03 Nights / 04 Days',
        overview=('Welcome to an untamed paradise where emerald-shrouded peaks kiss the floating mist. This Premium Tamil Nadu Experience, masterfully curated by travel specialists, whisks you away into the deep, ancient canopy of the Southern Western Ghats. Escape the ordinary and journey deep into Valparai, a pristine haven of endless tea estates, gushing waterfalls, and exotic rare wildlife, ensuring a soul-stirring luxury escape and unforgettable memories.\n\nTOUR OVERVIEW\nTravel Dates: Customizable Private Tour (FIT)\nVehicle Allocated: Private Luxury SUV (Chauffeur-Driven Innova Crysta)\nMeal Plan: Modified American Plan (Premium Breakfast & Dinners Included)\nRoute Map: Coimbatore Arrival → Aliyar Dam → Valparai Hairpin Bends → Sholayar Dam → Coimbatore Departure\n\nTRAGUIN Curated Note: Includes private estate walks, hornbill spotting excursions, and elite plantation stays handpicked by experts.'),
        seo_title='TN-015 | Valparai Unexplored Western Ghats Luxury Holiday | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Tamil Nadu package (TN-015 / TRAGUIN-TN-015): Valparai Western Ghats luxury holiday with wildlife spotting and 4-tier plantation bungalow accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih("Aliyar Dam, Loam's View Point, Attakatti Deep Valleys, and 40 hairpin bends ascent", 1),
            _ih('Nallamudi Viewpoint, Carver Marsh View, Private Tea Factory Tour, and hornbill spotting', 2),
            _ih('Sholayar Dam View, Nirar Dam, Urulanthi Rain Forest Borders, and gourmet picnic lunch', 3),
            _ih('TRAGUIN Signature Experience with guided plantation trail walk and private bird watching trek', 4),
            _ih('Premium 4-tier handpicked luxury plantation bungalow accommodation in Valparai', 5),
        ],
        days=[
            _day(1, 'COIMBATORE TO VALPARAI', ('Arrive at Coimbatore Airport or Railway Station where your elite private driver extends a warm premium welcome. Board your luxury SUV and begin your scenic drive towards the hidden hills of Valparai. Pause near the base to view the expansive Aliyar Dam, a breathtaking landscape reflecting the blue sky. As you ascend, navigate the thrilling 40 hairpin bends. Keep your cameras ready at the 9th hairpin bend—a highly searched photography point where the rare Nilgiri Tahr can often be spotted grazing along the sheer cliff faces. Check in seamlessly into your premium handpicked luxury heritage plantation bungalow.'), [
                "Sightseeing Included: Aliyar Dam, Loam's View Point, Attakatti Deep Valleys.",
                'Evening Experience: Indulge in an exclusive high-tea session overlooking private emerald tea fields.',
                'Overnight Stay: Luxury Heritage Plantation Villa, Valparai.',
                'Meals Included: Welcome Drink & Gourmet Dinner.',
            ]),
            _day(2, 'VALPARAI DEEP EXPLORATION', ('Wake up to the refreshing call of the Malabar Whistling Thrush. After a luxurious breakfast, venture out for a day of spectacular Valparai Sightseeing. Visit the stunning Nallamudi Viewpoint, requiring a gentle, rewarding walk through private tea carpets to reveal a dramatic view of deep valleys and tribal settlements. Later, explore the misty cascade of Monkey Falls and Balaji Temple. In the late afternoon, our local naturalist guides you on an exclusive walk to spot the endemic Lion-tailed Macaque and magnificent Great Indian Hornbills nested in the forest canopy.'), [
                'Sightseeing Included: Nallamudi Viewpoint, Carver Marsh View, Private Tea Factory Tour.',
                'Immersive Experiences: Private guided tea-tasting session inside a century-old processing unit.',
                'Overnight Stay: Premium Luxury Bungalow, Valparai.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(3, 'SHOLAYAR DAM & RAINFORESTS', ('Today, travel deeper toward the border of Kerala to witness the magnificent Sholayar Dam, one of the deepest reservoirs in Asia. The drive is an immersive experience in itself, passing through dense tropical rainforests and premium remote estates. Experience tranquility as the morning mist rolls over the vast water expanse. Discover hidden brooks and enjoy a gourmet picnic lunch packed by your resort chefs next to a secret waterfall stream. Return to the town area for an evening of relaxed local culture and souvenir shopping.'), [
                'Sightseeing Included: Sholayar Dam View, Nirar Dam, Urulanthi Rain Forest Borders.',
                'Optional Activities: Evening tribal folklore storytelling and campfire setup inside estate grounds.',
                'Overnight Stay: Luxury Heritage Plantation Villa, Valparai.',
                'Meals Included: Breakfast & Dinner.',
            ]),
            _day(4, 'VALPARAI TO COIMBATORE DEPARTURE', ('Savor your last morning breakfast amidst the peaceful rustling of tea leaves. Take a final walk around the estate for photography points before packing your memories. Descend the winding ghat roads comfortably in your premium vehicle. Transfer back to Coimbatore Airport or Station for your onward journey home. Your signature luxury holiday concludes, leaving you with memories that linger long after the destination.'), [
                'Transfers Included: Private Luxury Airport / Station Drop-off.',
                'Meals Included: Gourmet Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Valparai Heritage Inn / Tea Valley Resort', 'Valparai', '03 Nights', 'Deluxe', 'Deluxe Cottage', 'MAP (Breakfast + Dinner)', 4, 1, description='OPTION 01 – DELUXE: Valparai Heritage Inn / Tea Valley Resort — Deluxe Cottage — MAP (Breakfast + Dinner)'),
            _hotel('Stanmore Garden Bungalow (Woodbriar)', 'Valparai', '03 Nights', 'Premium', 'Standard Plantation Room', 'MAP (Breakfast + Dinner)', 4, 2, description='OPTION 02 – PREMIUM: Stanmore Garden Bungalow (Woodbriar) — Standard Plantation Room — MAP (Breakfast + Dinner)'),
            _hotel("Sinna Dorai's Bungalow, Valparai", 'Valparai', '03 Nights', 'Luxury', 'Luxury Estate Suite', 'MAP Premium Dining', 5, 3, description="OPTION 03 – LUXURY: Sinna Dorai's Bungalow, Valparai — Luxury Estate Suite — MAP Premium Dining"),
            _hotel('The Monica Garden Bungalow / Elite Private Villa', 'Valparai', '03 Nights', 'Ultra Luxury', 'Presidential Heritage Bungalow', 'All Inclusive Custom Meals', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Monica Garden Bungalow / Elite Private Villa — Presidential Heritage Bungalow — All Inclusive Custom Meals'),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at ultra-premium handpicked luxury hotels and bungalows.', 1),
            _inc_included('Meals: Daily multi-cuisine buffet Breakfasts and Dinners at the properties.', 2),
            _inc_included('Transfers & Sightseeing: All commutes in a private luxury air-conditioned Chauffeur-driven Innova Crysta.', 3),
            _inc_included('Assistance & Taxes: 24/7 dedicated remote concierge assistance and all applicable luxury resort taxes.', 4),
            _inc_included('Welcome Amenities: Executive welcome kit including fresh organic hill-station chocolates, spices, and premium mineral water.', 5),
            _inc_included('Complimentary Experiences: Guided plantation trail walk, private bird watching trek, and tea tasting entry.', 6),
            _inc_excluded('Airfare or rail tickets connecting your hometown to Coimbatore.', 7),
            _inc_excluded('Entry tickets, camera charges, and forest department permit fees at sightseeing points.', 8),
            _inc_excluded('Personal expenses such as premium laundry, boutique shopping, and alcoholic beverages.', 9),
            _inc_excluded('Optional tours, jungle safaris, or vehicle extensions not mentioned in the itinerary.', 10),
            _inc_excluded('Mandatory holiday travel and medical insurance covers.', 11),
        ],
    )
    return package, itinerary

def build_tn_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'TN-016'
    tour_code = 'TRAGUIN-TN-016'
    title = 'Yercaud Serene Hill Getaway'
    duration = '02 Nights / 03 Days'
    slug = 'tn-016-yercaud-serene-hill-getaway'
    itin_slug = 'tn-016-yercaud-serene-hill-getaway-itinerary'
    package = PackageCreate(
        slug=slug, serial_code=serial, traguin_tour_code=tour_code,
        destination_id=destination_id, title=title, duration_label=duration,
        price=0, rating=Decimal("4.9"), is_featured=False,
        featured_sort_order=None, is_published=False,
        highlights=[
            _ph(f"Serial code {serial} | TRAGUIN tour code {tour_code}", 1),
            _ph('State / Country: Tamil Nadu / India | Category: Leisure / Premium Hill Getaway', 2),
            _ph('Destinations: Yercaud (Jewel of the South)', 3),
            _ph('Ideal for: Families, Couples & Corporate Rejuvenation', 4),
            _ph('Best season: October to June', 5),
            _ph('Travel Style: Customized FIT / Elite Leisure Weekend Break', 6),
            _ph('Vehicle Allocated: Dedicated Luxury Chauffeur-driven Private AC Sedan / SUV', 7),
            _ph('Meal Plan: Continental Breakfast & Multi-cuisine Dinners Included', 8),
            _ph('TRAGUIN Curated Experience Note: Our professional travel consultants have handpicked premier stays featuring panoramic terrace balconies, private curated spice walks, and specialized hassle-free transport rules.', 9),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts, this itinerary guarantees a stress-free mountain escape. Enjoy pre-booked premium rooms, custom route pacing to minimize travel fatigue, and exclusive recommendations on boutique coffee estates.', 10),
            _ph('Shopping & Local Experiences: Local Markets: Purchase pure mountain honey, freshly ground plantation coffee powder, and homemade organic chocolates. Spices & Cosmetics: Discover natural eucalyptus oils, black pepper, and pure herbal skincare products unique to the Shevaroy range.', 11),
            _ph('Important Notes: Hotel Policies: Resort check-in standard time is 14:00 hrs. Early occupancy depends entirely on room availability. Weather Notes: The best time to visit Yercaud is during winter/summer. Carrying a light sweater or jacket for breezy evenings is advised. Advance Booking: Peak season weekends get occupied rapidly. We suggest completing bookings 3-4 weeks in advance.', 12),
        ],
        moods=['Hills', 'Leisure', 'Family'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug, destination_id=destination_id, title=title,
        duration_label=duration, duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"), review_count=0,
        tagline='Best Tamil Nadu Tour Package • Yercaud Serene Hill Getaway • 02 Nights / 03 Days',
        overview=('Welcome to the mesmerizing trails of the Shevaroy Hills. This premium getaway, beautifully planned by TRAGUIN, offers an emotional escape into mist-kissed orange orchards, aromatic coffee estates, and silent glassy lakes. As a leading choice for a Premium Tamil Nadu Experience, we blend elite comfort with raw natural splendor to leave you with unforgettable memories.\n\nTOUR OVERVIEW\nTravel Style: Customized FIT / Elite Leisure Weekend Break\nVehicle Allocated: Dedicated Luxury Chauffeur-driven Private AC Sedan / SUV\nMeal Plan: Continental Breakfast & Multi-cuisine Dinners Included\n\nTRAGUIN Curated Experience Note:\nOur professional travel consultants have handpicked premier stays featuring panoramic terrace balconies, private curated spice walks, and specialized hassle-free transport rules.\n\nYercaud, affectionately known as the Jewel of the South, stands out as an idyllic mountain retreat perfect for a Tamil Nadu Family Tour or an intimate Tamil Nadu Honeymoon Package.'),
        seo_title='TN-016 | Yercaud Serene Hill Getaway | TRAGUIN',
        seo_description='Premium 02 Nights / 03 Days Tamil Nadu package (TN-016 / TRAGUIN-TN-016): Yercaud serene hill getaway with private boating and 4-tier handpicked accommodation.',
        is_featured=False, featured_sort_order=None, is_published=False,
        highlights=[
            _ih('Emerald Yercaud Lake, Deer Park, Anna Park, and private boating at sunset', 1),
            _ih("32-km Loop Road, Shevaroy Temple Peak, Lady's Seat, and National Orchidarium", 2),
            _ih('Private Spice Garden Walk, Pagoda Point, and plantation coffee tour', 3),
            _ih('TRAGUIN Signature Experience with guided plantation walks and private boat ride tokens on Yercaud Lake', 4),
            _ih('Premium 4-tier handpicked luxury resort accommodation in Yercaud', 5),
        ],
        days=[
            _day(1, 'ARRIVAL & YERCAUD HILL IMMERSION', ('Your premium holiday begins with a scenic drive up the pristine 20 hairpin bends from Salem. Arrive at your handpicked resort where the cool mountain breeze welcomes you. After a seamless check-in experience, embark on your afternoon Tamil Nadu Sightseeing. Stroll along the beautiful paths of Yercaud Lake, surrounded by dense gardens and woods. Enjoy an exclusive private boating experience as the sun dips below the hills, painting the sky in deep shades of gold.'), [
                'Sightseeing Included: Emerald Yercaud Lake, Deer Park, Anna Park.',
                'Evening Experience: A relaxing walk through local markets followed by an immersive high-tea experience at the resort.',
                'Photography Points: Sunset reflection over the calm lake waters and mist rolling onto the lake banks.',
                'Overnight Stay: Handpicked Luxury Resort, Yercaud.',
                'Meals Included: Welcome Drink & Gourmet Buffet Dinner.',
            ]),
            _day(2, 'EXPLORING ICONIC ATTRACTIONS & LOOPS', ("Awake to the refreshing aroma of fresh coffee beans. Today, your luxury vehicle takes you along the famous 32-km Loop Road, a stunning stretch weaving through ancient coffee plantations and tribal hamlets. Visit the historic Shevaroy Temple, located at the highest point of the hill range. Later, step out to Lady's Seat and Gentleman's Seat—dramatic rock formations offering a bird's-eye view of the plains far below. End your afternoon exploring the diverse flora at the spectacular Orchidarium."), [
                "Sightseeing Included: 32-km Loop Road, Shevaroy Temple Peak, Lady's Seat, National Orchidarium.",
                'Optional Activities: A guided colonial heritage walk or an estate-level coffee processing tour.',
                'Evening Experience: Gather around a private bonfire setup under a starry sky with light acoustic music.',
                'Overnight Stay: Handpicked Luxury Resort, Yercaud.',
                'Meals Included: Premium Breakfast & Curated Theme Dinner.',
            ]),
            _day(3, 'SPICE GARDENS & DEPARTURE', ('Savor a luxurious morning breakfast overlooking the valleys. Before bidding farewell, visit a premium spice plantation to learn about pepper cultivation and organic farming methods. Take a last peaceful look at the breathtaking landscapes before checking out. Your private vehicle transfers you smoothly back to the Salem or Coimbatore station/airport for your onward journey home.'), [
                'Sightseeing Included: Private Spice Garden Walk, Pagoda Point.',
                'Transfers Included: Private Luxury Station / Airport Drop-off.',
                'Meals Included: Full Buffet Breakfast.',
            ]),
        ],
        hotels=[
            _hotel('Sterling Yercaud', 'Yercaud', '02 Nights', 'Deluxe', 'Premier Valley View Room', 'Continental Breakfast & Multi-cuisine Dinners', 4, 1, description='OPTION 01 – DELUXE: Sterling Yercaud — Premier Valley View Room — 02 Nights'),
            _hotel('Grange Resort', 'Yercaud', '02 Nights', 'Premium', 'Luxury Boutique Cabin', 'Continental Breakfast & Multi-cuisine Dinners', 4, 2, description='OPTION 02 – PREMIUM: Grange Resort — Luxury Boutique Cabin — 02 Nights'),
            _hotel('Great Trails Yercaud by GRT Hotels', 'Yercaud', '02 Nights', 'Luxury', 'Timber Cabin / Sky Villa', 'Continental Breakfast & Multi-cuisine Dinners', 5, 3, description='OPTION 03 – LUXURY: Great Trails Yercaud by GRT Hotels — Timber Cabin / Sky Villa — 02 Nights'),
            _hotel('The Regent Hill Villa & Spa', 'Yercaud', '02 Nights', 'Ultra Luxury', 'Grand Royal Panoramic Suite', 'Continental Breakfast & Multi-cuisine Dinners', 5, 4, description='OPTION 04 – ULTRA LUXURY: The Regent Hill Villa & Spa — Grand Royal Panoramic Suite — 02 Nights'),
        ],
        inclusions=[
            _inc_included('Accommodation: Luxury stay at handpicked hotels with premium vantage viewpoints.', 1),
            _inc_included('Meals: 02 Buffet Breakfasts and 02 multi-cuisine dinners curated by executive chefs.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven private luxury AC vehicle for all transfers.', 3),
            _inc_included('TRAGUIN Support: 24/7 priority remote assistance and ground coordination.', 4),
            _inc_included('Welcome Amenities: Refreshing welcome drink, organic wet towels, and seasonal fruit basket upon arrival.', 5),
            _inc_included('Complimentary Experiences: Guided plantation walks and private boat ride tokens on Yercaud Lake.', 6),
            _inc_excluded('Airfare or interstate train ticketing expenses.', 7),
            _inc_excluded('Individual entry monuments or cameras fees.', 8),
            _inc_excluded('Optional tours, adventure sports (zip-lining), or personal laundry expenses.', 9),
            _inc_excluded('Goods and Services Tax or travel insurance packages.', 10),
        ],
    )
    return package, itinerary

TAMIL_NADU_DOMESTIC_BUILDERS = [
    build_tn_006,
    build_tn_007,
    build_tn_008,
    build_tn_009,
    build_tn_010,
    build_tn_011,
    build_tn_012,
    build_tn_013,
    build_tn_014,
    build_tn_015,
    build_tn_016,
]
