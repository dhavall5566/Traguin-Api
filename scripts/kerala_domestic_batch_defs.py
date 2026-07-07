"""Builder functions for KL-011 through KL-025 Kerala domestic packages."""

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

KERALA_SLUG = "kerala"
KERALA_DESTINATION_ID = "2d170ff5-019f-4284-9eec-a403e2b49749"


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

def build_kl_011(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-011'
    tour_code = 'TRAGUIN-KL-011'
    title = 'Munnar • Alleppey Express'
    duration = '04 Nights / 05 Days'
    slug = 'kl-011-munnar-alleppey-express'
    itin_slug = 'kl-011-munnar-alleppey-express-itinerary'
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
            _ph('State / Country: Kerala, India | Category: Family Vacation / Luxury', 2),
            _ph('Destinations: Munnar • Alleppey Backwaters • Cochin', 3),
            _ph('Ideal for: Families & Couples', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Luxury FIT Getaway', 7),
            _ph('Vehicle: Private Air-Conditioned Luxury Sedan / Innova Crysta', 8),
            _ph('Meal Plan: Daily Premium Breakfast & All Meals on the Houseboat', 9),
            _ph('Route Map: Cochin Arrival → Munnar Hills → Alleppey Backwaters → Cochin Departure', 10),
            _ph('TRAGUIN Signature Experience: Includes a private spice plantation tour, exclusive Kathakali live cultural performance, premium handpicked luxury stays, and a dedicated travel concierge throughout the journey.', 11),
            _ph('Shopping: Premium spices and tea from Munnar; exotic spices, Kasavu sarees, and local souvenirs from Fort Cochin Jew Town', 12),
            _ph('Important: Hotel check-in 14:00 hrs, check-out 11:00 hrs; book early for highest-rated villa view availability', 13),
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Munnar • Alleppey Express • 04 Nights / 05 Days',
        overview=(
            "Immerse yourself into the majestic layers of God's Own Country. Designed expertly by TRAGUIN, this signature itinerary combines the rolling emerald tea plantations of Munnar with the dreamy floating houseboats of Alleppey. Crafted exclusively for elite families who value luxury, private curated experiences, and pristine hospitality.\n\nSeeking the Best Kerala Tour Package or an elegant Kerala Honeymoon Package? Our specialized route showcases the most searched iconic attractions of South India. Enjoy premium misty hill-station escapes in Munnar, dynamic photo spots over Mattupetty Dam, and deeply cultural heritage sights in historical Fort Cochin. With TRAGUIN Kerala Packages, your family is guaranteed a flawlessly synchronized luxury holiday filled with breathtaking landscapes.\n\nTRAGUIN Curated Touch: Includes a private spice plantation tour, exclusive Kathakali live cultural performance, premium handpicked luxury stays, and a dedicated travel concierge throughout the journey."
        ),
        seo_title='KL-011 | Munnar Alleppey Express | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kerala package (KL-011 / TRAGUIN-KL-011): Munnar • Alleppey Backwaters • Cochin. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Cheeyappara & Valara Waterfalls en route to Munnar', 1),
            _ih('Eravikulam National Park, Mattupetty Dam, Echo Point & spice plantation', 2),
            _ih('Private luxury Alleppey houseboat on Vembanad Lake', 3),
            _ih('Fort Cochin Chinese Fishing Nets, Mattancherry Palace & Jew Town', 4),
            _ih('TRAGUIN Signature Experience with private spice tour and Kathakali performance', 5),
        ],
        days=[
            _day(
                1,
                'ARRIVAL COCHIN TO MUNNAR',
                (
                    'Land at Cochin International Airport and receive a personalized premium welcome from your TRAGUIN coordinator. Board your luxury private vehicle and proceed along a gorgeous winding drive toward Munnar. En route, pause to behold the majestic spray of the Cheeyappara and Valara waterfalls. Check in seamlessly to your premium mountain valley resort.'
                ),
                [
                    'Sightseeing Included: Cheeyappara & Valara Waterfalls, Tea Garden Viewpoints.',
                    'Overnight Stay: Handpicked Luxury Resort, Munnar.',
                    'Meals Included: Welcome Amenities & Dinner.',
                ],
            ),
            _day(
                2,
                'MUNNAR FULL DAY TOUR',
                (
                    'Savor a gourmet morning breakfast. Explore Mattupetty Dam, Echo Point, and the beautifully preserved Eravikulam National Park (famous for the rare Nilgiri Tahr). In the afternoon, enjoy an immersive walk through a premium handpicked spice plantation followed by an authentic tea tasting session.'
                ),
                [
                    'Sightseeing Included: Eravikulam National Park, Mattupetty Dam, Echo Point, Spice Gardens.',
                    'Overnight Stay: Luxury Mountain Resort, Munnar.',
                    'Meals Included: Full Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'MUNNAR TO ALLEPPEY HOUSEBOAT',
                (
                    'After a scenic breakfast, descend the hills towards the serene backwaters of Alleppey. Step inside your private luxury TRAGUIN-vetted Houseboat. Gliding through networks of tranquil canals, coconut groves, and emerald paddy fields, enjoy traditional Kerala cuisines freshly prepared onboard by your personal chef.'
                ),
                [
                    'Sightseeing Included: Alleppey Backwater Canals, Vembanad Lake.',
                    'Overnight Stay: Premium Private Houseboat, Alleppey.',
                    'Meals Included: Breakfast, Traditional Lunch, High Tea & Seafood Dinner.',
                ],
            ),
            _day(
                4,
                'ALLEPPEY TO COCHIN SIGHTSEEING',
                (
                    'Disembark your houseboat after breakfast and drive back to Cochin. Discover the rich historical lanes of Fort Cochin. Witness the iconic Chinese Fishing Nets, visit the ancient St. Francis Church, and shop for exotic spices and local souvenirs at Jew Town.'
                ),
                [
                    'Sightseeing Included: Chinese Fishing Nets, Mattancherry Palace, Jew Town.',
                    'Overnight Stay: Premium Luxury Hotel, Cochin.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'COCHIN DEPARTURE',
                (
                    'Enjoy a final relaxed breakfast at your hotel before transferring comfortably back to Cochin International Airport for your journey home, fully refreshed by your unforgettable premium experience.'
                ),
                [
                    'Transfers Included: Private Airport Drop-off.',
                    'Meals Included: Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Blanket Hotel & Spa', 'Munnar', '02 Nights', 'Luxury', 'Premium Valley View Room', 'Breakfast & Dinner', 5, 1),
            _hotel('Premium AC Private Houseboat', 'Alleppey', '01 Night', 'Luxury', 'AC Private Cabin', 'All Meals on Houseboat', 5, 2),
            _hotel('The Panoramic Getaway', 'Munnar', '02 Nights', 'Ultra Luxury', 'Luxury Suite', 'Breakfast & Dinner', 5, 3),
            _hotel('Luxury Glass-Wall Private Houseboat', 'Alleppey', '01 Night', 'Ultra Luxury', 'Glass-Wall Suite', 'All Meals on Houseboat', 5, 4),
        ],
        inclusions=[
            _inc_included('Luxury stays at handpicked premium resorts & houseboats.', 1),
            _inc_included('Fully dedicated AC Innova Crysta for all planned sightseeing.', 2),
            _inc_included('24/7 on-call TRAGUIN support and assistance.', 3),
            _inc_excluded('Airfare, monument entries, and personal activities.', 4),
        ],
    )
    return package, itinerary

def build_kl_012(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-012'
    tour_code = 'TRAGUIN-KL-012'
    title = 'Cochin Munnar Thekkady Luxury Beach Escape'
    duration = '06 Nights / 07 Days'
    slug = 'kl-012-cochin-munnar-thekkady-luxury-beach-escape'
    itin_slug = 'kl-012-cochin-munnar-thekkady-luxury-beach-escape-itinerary'
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
            _ph('State / Country: Kerala, India | Category: Family Tour / Luxury', 2),
            _ph('Destinations: Cochin • Munnar • Thekkady • Marari / Kovalam Beach', 3),
            _ph('Ideal for: Premium Family Vacations', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Premium Family FIT Vacation', 7),
            _ph('Vehicle: Dedicated Private Luxury Air-Conditioned Innova Crysta / Executive Sedan', 8),
            _ph('Meal Plan: Modified American Plan (Gourmet Breakfast & Dinners Included)', 9),
            _ph('Route Map: Cochin Arrival → Munnar Hills → Thekkady Sanctuary → Luxury Beach Resort → Cochin Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts to offer an optimal balance of adventure and relaxation with priority check-ins and handpicked rooms with premium valley or sea views.', 11),
            _ph('Shopping: Green cardamom, black pepper, cloves, vanilla from Thekkady; premium tea from Munnar; Kasavu sarees from local weavers', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; light layers advised for Munnar evenings; book early for peak season', 13),
        ],
        moods=['Family', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Cochin Munnar Thekkady Luxury Beach Escape • 06 Nights / 07 Days',
        overview=(
            "Immerse your family in the timeless splendor of God's Own Country with this ultra-luxurious, grand holiday escape. Meticulously curated by TRAGUIN experts, this bespoke premium journey winds through the misty cloud-kissed tea estates of Munnar, wildlife-rich sanctuaries of Thekkady, historical coastal streets of Cochin, and finishes at a pristine sun-drenched private beach resort. Crafted exclusively for discerning families seeking an immersive, slow-paced luxury experience. WELCOME TO THE HERITAGE COAST TOUR OVERVIEW\n\nis tailored with exclusive benefits: zero-hassle private check-ins, immersive tea and spice plantation masterclasses, traditional live performance arts, and family photography milestones among breathtaking landscapes. WHY CHOOSE OUR LUXURY KERALA HOLIDAY? Kerala stands as one of India's most highly searched destinations for a reason—offering a majestic blend of rich traditional culture, breathtaking landscapes, and unparalleled hospitality. For families researching the ultimate Kerala Family Tour or couples mapping out a signature Kerala Honeymoon Package, this carefully designed route encompasses the absolute best tourist places in Kerala. From exploring world-renowned spice routes to enjoying exclusive luxury wellness treatments, your stay is centered around premium handpicked hotels known for top-tier service. Discover popular Instagram locations including majestic waterfalls, infinite green valleys, and sweeping coastal backdrops. With TRAGUIN Kerala Packages, your family values are seamlessly integrated with a high-end travel experience.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts to offer an optimal balance of adventure and relaxation with priority check-ins and handpicked rooms with premium valley or sea views."
        ),
        seo_title='KL-012 | Cochin Munnar Thekkady Luxury Beach Escape | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Kerala package (KL-012 / TRAGUIN-KL-012): Cochin • Munnar • Thekkady • Marari / Kovalam Beach. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Fort Cochin heritage walk with Kathakali cultural evening', 1),
            _ih('Munnar tea estates, Eravikulam National Park & Mattupetty Dam', 2),
            _ih('Thekkady spice plantations and Periyar Lake boat cruise', 3),
            _ih('Premium Marari or Kovalam beach resort leisure', 4),
            _ih('TRAGUIN Signature Experience with plantation masterclasses', 5),
        ],
        days=[
            _day(
                1,
                'COCHIN ARRIVAL',
                (
                    'Arrive at Cochin International Airport where your dedicated private chauffeur welcomes your family. Transfer elegantly to your boutique luxury hotel in Fort Cochin. Spend the afternoon exploring iconic attractions such as the historic Chinese Fishing Nets, the 16th-century Mattancherry Dutch Palace, and the oldest European church in India, St. Francis Church. Walk hand-in-hand down Jew Town, breathing in centuries of spice-trading history.'
                ),
                [
                    'Sightseeing Included: Fort Cochin Heritage Walk, Chinese Fishing Nets, Mattancherry Palace, Jew Town.',
                    'Evening Experience: Witness an exclusive, colorful Kathakali classical dance performance at a private',
                    'Overnight Stay: Premium Luxury Hotel, Cochin.',
                    'Meals Included: Welcome Drink & Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'COCHIN TO MUNNAR',
                (
                    "Enjoy a leisurely breakfast before checking out and driving towards Munnar—the crown jewel of South India's hill stations. Your route winds past scenic beauty, pristine rivers, and mountain gaps. Stop for a breathtaking photography session at the spectacular Cheeyappara and Valara Waterfalls, where white foam cascades amidst dense tropical forests. Arrive in Munnar, check in smoothly to your handpicked luxury mountain resort, and breathe in the refreshing, crisp tea-scented mountain air."
                ),
                [
                    'Sightseeing Included: Cheeyappara Waterfalls, Valara Eco-spots, Tea Valley Viewpoints.',
                    'Photography Points: Majestic mountain drops and mist rolling over the endless valley edges.',
                    'Overnight Stay: Premium Mountain Resort, Munnar.',
                    'Meals Included: Full Buffet Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'MUNNAR SIGHTSEEING',
                (
                    'A full-day dedicated to the top tourist places in Munnar. Visit the rolling heights of Eravikulam National Park (Rajamalai), home to the endangered Nilgiri Tahr mountain goat. Later, enjoy a private family drive to the tranquil Mattupetty Dam, Echo Point, and Kundala Lake. Walk along the lakeside paths where voices echo clearly over the water, and capture unforgettable memories with a family portrait set against a backdrop of infinite tea plantations.'
                ),
                [
                    'Sightseeing Included: Eravikulam National Park, Mattupetty Dam, Echo Point, Kundala Lake.',
                    'Immersive Experiences: A curated private tour of an estate tea factory to see artisanal brewing methods up',
                    'Overnight Stay: Premium Mountain Resort, Munnar.',
                    'Meals Included: Full Buffet Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'MUNNAR TO THEKKADY',
                (
                    'Travel from the hills down into the rich spice heartlands of Thekkady (Periyar). The scenic drive takes you past rubber estates, cardamom groves, and coffee hills. Check in to your ultra-luxury jungle resort. In the afternoon, enjoy a guided Spice Plantation Tour where you can touch, smell, and taste fresh black pepper, vanilla, cinnamon, and nutmeg straight from the branch.'
                ),
                [
                    'Sightseeing Included: Periyar Forest Rim, Cardamom and Pepper Plantations.',
                    'Optional Activities: Experience a thrilling family elephant interaction and grooming session.',
                    'Overnight Stay: Premium Eco-Luxury Resort, Thekkady.',
                    'Meals Included: Full Buffet Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'THEKKADY TO BEACH RESORT (MARARI / KOVALAM)',
                (
                    "Wake early for a calm morning boat cruise across the pristine Periyar Lake, watching for wild elephants, otters, and exotic birds along the water's edge. Return to the resort for breakfast, then drive to your premium coastal beach resort (Marari or Kovalam). Step onto white sands, hear the rustle of coconut palms, and enjoy private luxury beach living at its finest."
                ),
                [
                    'Sightseeing Included: Periyar Lake Boat Cruise, Coastal Highway Drive.',
                    'Evening Experience: Relax on the beach at sunset, or pamper the family with an authentic Ayurvedic oil',
                    'Overnight Stay: Premium Luxury Beach Resort, Marari / Kovalam.',
                    'Meals Included: Full Buffet Breakfast & Dinner.',
                ],
            ),
            _day(
                6,
                'BEACH RESORT LEISURE',
                (
                    "A completely open day designed for premium relaxation. Bask beside your resort's infinity pool, take a peaceful morning stroll on a clean beach, or try a family pottery class. This is your time to slow down, build unforgettable memories, and enjoy the calming rhythm of the ocean waves."
                ),
                [
                    'Sightseeing Included: Pure Beach Leisure & In-Resort Curated Activities.',
                    'Food Suggestions: Enjoy fresh, caught-to-order coastal seafood infused with coconut milk and local spices.',
                    'Overnight Stay: Premium Luxury Beach Resort, Marari / Kovalam.',
                    'Meals Included: Full Buffet Breakfast & Grand Farewell Dinner.',
                ],
            ),
            _day(
                7,
                'COCHIN DEPARTURE',
                (
                    'Enjoy a relaxed breakfast at the resort while looking out over the sea. Your private vehicle will arrive to transfer your family back to Cochin International Airport for your flight home. Your signature TRAGUIN Kerala Package concludes smoothly, leaving your family with memories to cherish forever.'
                ),
                [
                    'Transfers Included: Private Airport Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('The Leaf Munnar', 'Munnar', '02 Nights', 'Deluxe', 'Executive Room', 'Breakfast & Dinner', 4, 1),
            _hotel('Forest Canopy', 'Thekkady', '01 Night', 'Deluxe', 'Executive Room', 'Breakfast & Dinner', 4, 2),
            _hotel('Abad Turtle Beach', 'Marari / Kovalam', '02 Nights', 'Deluxe', 'Executive Room', 'Breakfast & Dinner', 4, 3),
            _hotel('Blanket Hotel & Spa', 'Munnar', '02 Nights', 'Premium', 'Premium Room / Suite', 'Breakfast & Dinner', 4, 4),
            _hotel('The Elephant Court', 'Thekkady', '01 Night', 'Premium', 'Premium Room / Suite', 'Breakfast & Dinner', 4, 5),
            _hotel('Marari Beach Resort - CGH Earth', 'Marari / Kovalam', '02 Nights', 'Premium', 'Premium Room / Suite', 'Breakfast & Dinner', 4, 6),
            _hotel('The Panoramic Getaway', 'Munnar', '02 Nights', 'Luxury', 'Luxury Room / Suite', 'Breakfast & Dinner', 5, 7),
            _hotel('Spice Village - CGH Earth', 'Thekkady', '01 Night', 'Luxury', 'Luxury Room / Suite', 'Breakfast & Dinner', 5, 8),
            _hotel('The Leela Kovalam, Raviz', 'Marari / Kovalam', '02 Nights', 'Luxury', 'Luxury Room / Suite', 'Breakfast & Dinner', 5, 9),
            _hotel("Chandy's Windy Woods (Suite)", 'Munnar', '02 Nights', 'Ultra Luxury', 'Luxury Suite / Villa', 'Breakfast & Dinner', 5, 10),
            _hotel('Niraamaya Retreats Cardamom Club', 'Thekkady', '01 Night', 'Ultra Luxury', 'Luxury Suite / Villa', 'Breakfast & Dinner', 5, 11),
            _hotel('Taj Green Cove Resort & Spa', 'Marari / Kovalam', '02 Nights', 'Ultra Luxury', 'Luxury Suite / Villa', 'Breakfast & Dinner', 5, 12),
        ],
        inclusions=[
            _inc_included('Accommodation: 06 Nights stay at premium handpicked hotels and luxury coastal resorts.', 1),
            _inc_included('Meals: 06 Premium Buffet Breakfasts and 06 multi-cuisine Dinners at the properties.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven AC Innova Crysta for smooth city-to-city transfers.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated concierge assistance and curated landmark routing.', 4),
            _inc_included('Complimentary Experiences: Private Spice Garden walking entry, Periyar Lake cruise, and Fort Cochin heritage walk.', 5),
            _inc_included('Welcome Amenities: Cold towels, fresh fruit platters upon arrival, and standard packed mineral water during transits. PACKAGE EXCLUSIONS', 6),
            _inc_excluded('Airfare or interstate train ticketing expenses.', 7),
            _inc_excluded('Camera or entry passes at national monuments not noted.', 8),
            _inc_excluded('Personal expenses such as boutique laundry, liquor orders, phone usage, or tips.', 9),
            _inc_excluded('Optional activities (e.g., Elephant rides, deep Ayurvedic spa sessions).', 10),
            _inc_excluded('Anything not explicitly listed under the standard inclusion block.', 11),
        ],
    )
    return package, itinerary

def build_kl_013(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-013'
    tour_code = 'TRAGUIN-KL-013'
    title = 'Kumarakom Backwater Heritage'
    duration = '03 Nights / 04 Days'
    slug = 'kl-013-kumarakom-backwater-heritage'
    itin_slug = 'kl-013-kumarakom-backwater-heritage-itinerary'
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
            _ph('State / Country: Kerala / India | Category: Family Vacation / Luxury Heritage', 2),
            _ph('Destinations: Cochin • Kumarakom Backwaters', 3),
            _ph('Ideal for: Families, Couples & Heritage Lovers', 4),
            _ph('Best season: September to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Heritage FIT Tour', 7),
            _ph('Vehicle: Dedicated Chauffeur-driven AC Luxury Sedan / Innova Crysta', 8),
            _ph('Meal Plan: Modified American Plan (Premium Breakfast & Gourmet Dinners)', 9),
            _ph('Route Map: Cochin Airport Arrival → Kumarakom Backwaters → Heritage Village Immersion → Cochin Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts to give your family a deeply immersive experience with pre-arranged resort check-ins and luxury transportation.', 11),
            _ph('Shopping: Organic black pepper, pure vanilla beans, cardamom; miniature brass Aranmula Kannadi mirrors and hand-sculpted wooden houseboats', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; lightweight cotton clothing recommended; advance bookings advised for houseboat experiences', 13),
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
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kumarakom Backwater Heritage • 03 Nights / 04 Days',
        overview=(
            "Step into an ancestral wonderland where emerald waters sync with absolute tranquility. Designed seamlessly by TRAGUIN, this iconic luxury holiday package brings you face-to-face with the timeless charm of Kumarakom. Melt away into unforgettable memories as you traverse deep heritage lanes, rest inside elite lakeside premium stays, and surrender to the soothing rhythm of Kerala's legendary scenic beauty.\n\nKumarakom is globally celebrated for its collection of pristine canals, dense mangrove forests, and the massive Vembanad Lake. If you are looking for the Best Kerala Tour Package or a relaxing Kerala Family Tour, this destination offers an idyllic slower alternative to busy holiday spots. From exploring the iconic attractions of the Kumarakom Bird Sanctuary to experiencing a traditional houseboat lunch cruise, our Luxury Kerala Holiday guarantees absolute peace. Key elements include handpicked luxury lakeside properties, immersive cultural activities, and high-standard photography spots. Choosing TRAGUIN Kerala Packages ensures top-tier comfort, smooth transfers, and premium personalized assistance at every step.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts to give your family a deeply immersive experience with pre-arranged resort check-ins and luxury transportation."
        ),
        seo_title='KL-013 | Kumarakom Backwater Heritage | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Kerala package (KL-013 / TRAGUIN-KL-013): Cochin • Kumarakom Backwaters. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Sunset canoe ride and luxury heritage houseboat lunch cruise', 1),
            _ih('Kumarakom Bird Sanctuary trail with naturalist guide', 2),
            _ih('Authentic Ayurvedic spa therapy at lakeside resort', 3),
            _ih('Heritage village coir making and handloom weaving', 4),
            _ih('TRAGUIN Signature Experience with pre-arranged resort check-ins', 5),
        ],
        days=[
            _day(
                1,
                'COCHIN TO KUMARAKOM',
                (
                    'Arrive at Cochin International Airport where your private professional chauffeur welcomes you warmly. Board your premium vehicle and begin a beautiful, scenic route towards the backwater paradise of Kumarakom. As you pull into your ultra-luxury lakeside resort, enjoy a refreshing traditional welcome drink. Spend the afternoon settling into your premium villa, soaking in the serene breathtaking landscapes of Vembanad Lake.'
                ),
                [
                    'Sightseeing Included: Smooth Airport Transfer, Scenic Backwater Drive.',
                    'Evening Experience: A relaxing sunset canoe ride organized exclusively by TRAGUIN experts to see local fishing nets up close.',
                    'Overnight Stay: Handpicked Luxury Resort, Kumarakom.',
                    'Meals Included: Welcome Drink & Gourmet Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'KUMARAKOM',
                (
                    'Wake up to a crisp morning over the lake. Today, enjoy an exclusive private day-cruise on a beautifully structured luxury heritage Kettuvallam (houseboat). Drift gently past local villages, lush green paddy fields, and lines of coconut trees. Taste authentic, freshly-prepared traditional Kerala dishes cooked by your private chef onboard. Later, explore local art centers to witness a live demonstration of coir making and traditional handloom weaving.'
                ),
                [
                    'Sightseeing Included: Premium Houseboat Backwater Cruise, Heritage Village Walk.',
                    'Photography Points: Endless horizons of Vembanad Lake from the open-deck houseboat.',
                    'Overnight Stay: Handpicked Luxury Resort, Kumarakom.',
                    'Meals Included: Full Breakfast, Traditional Houseboat Lunch & Gourmet Dinner.',
                ],
            ),
            _day(
                3,
                'KUMARAKOM',
                (
                    'In the early hours, proceed for a mild walking trail inside the famous Kumarakom Bird Sanctuary accompanied by a certified naturalist guide. Spot beautiful migratory birds flying across the treetops. Return to your premium stay for a lavish breakfast. The afternoon is kept completely at leisure to experience immersive wellness rituals. Indulge in an authentic, synchronized Ayurvedic spa therapy session right at the resort wellness wing.'
                ),
                [
                    'Sightseeing Included: Kumarakom Bird Sanctuary Trail, Pathiramanal Island view.',
                    'Optional Activities: Premium traditional Ayurvedic rejuvenation massage session.',
                    'Overnight Stay: Handpicked Luxury Resort, Kumarakom.',
                    'Meals Included: Full Buffet Breakfast & Farewell Dinner.',
                ],
            ),
            _day(
                4,
                'KUMARAKOM TO COCHIN DEPARTURE',
                (
                    'Savor a luxurious morning breakfast overlooking the calm waters. Take a final walk around the landscaped property gardens to capture beautiful photos. Pack your bags and bid farewell to this heritage haven. Your private luxury vehicle will transfer you smoothly back to Cochin Airport for your return flight home, wrapping up an exceptional premium holiday experience.'
                ),
                [
                    'Transfers Included: Private Comfort Airport Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Waterscapes KTDC Backwater Resort', 'Kumarakom', '03 Nights', 'Deluxe', 'Canal View Exotic Cottage', 'MAP (Breakfast + Dinner)', 4, 1),
            _hotel('Aveda Resorts & Spa', 'Kumarakom', '03 Nights', 'Premium', 'Luxury Lake-Facing Room', 'MAP (Breakfast + Dinner)', 4, 2),
            _hotel('The Zuri Kumarakom, Kerala Resort', 'Kumarakom', '03 Nights', 'Luxury', 'Zuri Deluxe Lagoon View Room', 'MAP (Breakfast + Dinner)', 5, 3),
            _hotel('Kumarakom Lake Resort / Taj Kumarakom', 'Kumarakom', '03 Nights', 'Ultra Luxury', 'Heritage Luxury Villa with Private Pool', 'MAP + Houseboat Lunch Included', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights exquisite stay at ultra-premium lakeside luxury properties.', 1),
            _inc_included('Meals: Daily premium buffet breakfasts and 03 curated multi-cuisine gourmet dinners at the resort.', 2),
            _inc_included('Transfers & Sightseeing: All city transfers and backwater tour circuits via a private luxury AC Innova Crysta.', 3),
            _inc_included('TRAGUIN Support: 24/7 priority concierge desk and localized operational assistance.', 4),
            _inc_included('Complimentary Experiences: Exclusive 02-Hour traditional houseboat ride with onboard local delicacies.', 5),
            _inc_included('Welcome Amenities: Cold-pressed aromatic oils, traditional hand-woven stoles, and premium mineral water bottles.', 6),
            _inc_excluded('Commercial/Domestic flight tickets or railway bookings.', 7),
            _inc_excluded('Individual entry tickets to monuments, sanctuaries, or personal video camera passes.', 8),
            _inc_excluded('Laundry charges, telephone bills, internal room orders, and tipping expenses.', 9),
            _inc_excluded('Any insurance plans, emergency medical coverage, or expenses caused by flight delays.', 10),
        ],
    )
    return package, itinerary

def build_kl_014(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-014'
    tour_code = 'TRAGUIN-KL-014'
    title = 'Athirapally Waterfalls & Munnar Premium Escape'
    duration = '04 Nights / 05 Days'
    slug = 'kl-014-athirapally-waterfalls-munnar-premium-escape'
    itin_slug = 'kl-014-athirapally-waterfalls-munnar-premium-escape-itinerary'
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
            _ph('State / Country: Kerala, India | Category: Luxury Family Holiday', 2),
            _ph('Destinations: Athirapally • Munnar • Cochin', 3),
            _ph('Ideal for: Premium Family Tour & Honeymooners', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Premium Family FIT Tour', 7),
            _ph('Vehicle: Dedicated Luxury AC Innova Crysta with Professional Chauffeur', 8),
            _ph('Meal Plan: Modified American Plan (Daily Breakfast & Gourmet Buffets)', 9),
            _ph('Route Map: Cochin Arrival → Athirapally Waterfalls → Munnar Hills → Cochin Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with fast-track luxury waterfall access, exclusive guided tea plantation trail, and elite handpicked hotels.', 11),
            _ph('Shopping: Fresh green cardamom, black peppercorns, cloves, vanilla from Munnar; Kasavu sarees and rosewood elephant figurines from Fort Cochin', 12),
            _ph('Important: Advance bookings advised during high season; check-in 14:00 hrs, check-out 11:00 hrs; light woolens suggested for Munnar evenings', 13),
        ],
        moods=['Family', 'Nature', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Athirapally Waterfalls & Munnar Premium Escape • 04 Nights / 05 Days',
        overview=(
            "Welcome to God's Own Country. This luxury itinerary, thoughtfully designed by TRAGUIN, invites your family to rediscover the timeless charm of lush wilderness, sprawling tea hills, and misty valley vistas. From the thundering cascade of Athirapally to the serene tea horizons of Munnar, immerse yourself in premium stays and handpicked holiday magic tailored perfectly to generate unforgettable memories. TOUR OVERVIEW\n\ncomfort is handled with an impeccable travel consultant tone. Let TRAGUIN Kerala Packages elevate your luxury vacation through immersive experiences, spice estate exploration, and traditional food encounters.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts with fast-track luxury waterfall access, exclusive guided tea plantation trail, and elite handpicked hotels."
        ),
        seo_title='KL-014 | Athirapally Waterfalls & Munnar Premium Escape | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kerala package (KL-014 / TRAGUIN-KL-014): Athirapally • Munnar • Cochin. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Athirapally Waterfalls and Vazhachal Forest Rapids', 1),
            _ih('Munnar Eravikulam National Park, Mattupetty Dam & Tea Museum', 2),
            _ih('Fort Cochin Chinese Fishing Nets and Jew Town heritage walk', 3),
            _ih('Guided organic spice estate trail and tea-tasting sessions', 4),
            _ih('TRAGUIN Signature Experience with fast-track waterfall access', 5),
        ],
        days=[
            _day(
                1,
                'COCHIN TO ATHIRAPALLY',
                (
                    'Arrive at Cochin International Airport where your private professional chauffeur will extend a warm traditional welcome. Board your air-conditioned luxury vehicle and embark on a scenic route toward the majestic Athirapally Waterfalls. As you approach, the soothing roar of water echoing through dense green canopies instantly sets an emotional storytelling backdrop. Check into your ultra-luxury resort overlooking the falls. Spend the afternoon exploring the scenic forest pathways and capture magnificent photos at designated photography points.'
                ),
                [
                    'Sightseeing Included: Athirapally Main Falls, Vazhachal Forest Rapids.',
                    'Evening Experience: Relax on your private resort deck, sipping locally brewed cardamom tea while watching',
                    'Overnight Stay: Handpicked Luxury Rainforest Resort, Athirapally.',
                    'Meals Included: Welcome Drink & Gourmet Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'ATHIRAPALLY TO MUNNAR HILLS',
                (
                    'Indulge in a luxurious breakfast before checking out. Embark on a spectacular drive through winding roads to the queen of hill stations—Munnar. En route, witness the mesmerizing Valara and Cheeyappara waterfalls, which serve as iconic attractions and perfect backdrops for family portraits. As you ascend, feel the temperature drop and the air grow crisp with the scent of wild mountain flora. Reach your handpicked premium stays perched safely on the mist-kissed slopes of Munnar and check in seamlessly.'
                ),
                [
                    'Sightseeing Included: Cheeyappara & Valara Waterfalls, Karadipara Viewpoint.',
                    'Local Experiences: A brief stop at a local roadside spice market to observe artisanal farming methods.',
                    'Overnight Stay: Premium Luxury Mountainside Resort, Munnar.',
                    'Meals Included: Full Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'MUNNAR HIGHLANDS SIGHTSEEING',
                (
                    'Dedicate your morning to an exclusive, immersive experience within Eravikulam National Park, the famous sanctuary sheltering the endangered Nilgiri Tahr. Next, marvel at the engineering marvel of Mattupetty Dam, where gentle boating options can be enjoyed by families. Walk through the natural acoustic pathways of Echo Point and capture unforgettable memories by the lakeside. Later, discover the rich heritage of tea processing with an informative guided excursion inside a colonial-era tea factory museum.'
                ),
                [
                    'Sightseeing Included: Eravikulam National Park, Mattupetty Dam, Echo Point, Tea Museum.',
                    'Optional Activities: Serene private speed-boating across Mattupetty reservoir lake.',
                    'Overnight Stay: Premium Luxury Mountainside Resort, Munnar.',
                    'Meals Included: Full Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'MUNNAR TO COCHIN',
                (
                    'Savor a relaxed breakfast, absorbing the breathtaking landscapes for one last morning before driving back to the historical port city of Cochin. In the afternoon, enjoy a cultural dive into Fort Cochin. Admire the iconic Chinese Fishing Nets operating gracefully against the horizon and visit the historic St. Francis Church. Conclude your evening walking through the vintage colonial lanes of Jew Town, browsing antique markets and high-end cafes.'
                ),
                [
                    'Sightseeing Included: Fort Cochin Chinese Nets, Mattancherry Palace, Jew Town.',
                    'Food Suggestions: Taste fresh coastal Malabar seafood at a premium heritage restaurant in Fort Cochin.',
                    'Overnight Stay: Ultra-Luxury Boutique Hotel, Cochin.',
                    'Meals Included: Full Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'COCHIN DEPARTURE',
                (
                    'Relish a slow morning breakfast overlooking the harbour waters. Pack your bags loaded with authentic local souvenirs, premium spices, and beautiful memories. Your private luxury transportation will pick you up from the lobby and transfer you comfortably to Cochin International Airport for your flight back home. Your premium holiday curated by TRAGUIN concludes seamlessly.'
                ),
                [
                    'Transfers Included: Private Airport Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Athirapally Green Trees', 'Athirapally', '01 Night', 'Deluxe', 'Executive Room', 'Breakfast & Dinner', 4, 1),
            _hotel('Blanket Hotel & Spa (Executive)', 'Munnar', '02 Nights', 'Deluxe', 'Executive Room', 'Breakfast & Dinner', 4, 2),
            _hotel('Rainforest Resort (Luxury Room)', 'Athirapally', '01 Night', 'Premium', 'Luxury Room', 'Breakfast & Dinner', 4, 3),
            _hotel('The Panoramic Getaway (Deluxe View)', 'Munnar', '02 Nights', 'Premium', 'Deluxe View Room', 'Breakfast & Dinner', 4, 4),
            _hotel('Rainforest Resort (Treehouse Option)', 'Athirapally', '01 Night', 'Luxury', 'Treehouse', 'Breakfast & Dinner', 5, 5),
            _hotel('Spice Tree Munnar (Classic Jacuzzi Suite)', 'Munnar', '02 Nights', 'Luxury', 'Classic Jacuzzi Suite', 'Breakfast & Dinner', 5, 6),
            _hotel('Niraamaya Retreats Samroha', 'Athirapally', '01 Night', 'Ultra Luxury', 'Luxury Villa', 'Breakfast & Dinner', 5, 7),
            _hotel('Elixir Hills Suites Resort & Spa', 'Munnar', '02 Nights', 'Ultra Luxury', 'Luxury Suite', 'Breakfast & Dinner', 5, 8),
        ],
        inclusions=[
            _inc_included('Accommodation: 04 Nights premium stays at selected ultra-luxury and boutique hotel resorts.', 1),
            _inc_included('Meals: 04 Premium Breakfasts & 04 curated Gourmet Dinners at the resorts.', 2),
            _inc_included('Transfers & Sightseeing: All luxury transfers managed in a private, air-conditioned Innova Crysta.', 3),
            _inc_included('Welcome Amenities: Personalized arrival greeting kits containing traditional Kerala stoles and cold-pressed juices.', 4),
            _inc_included('Complimentary Experiences: Guided organic spice estate walking trail and interactive tea-tasting sessions.', 5),
            _inc_included('TRAGUIN Support: Full 24/7 priority concierge backing from our backend corporate travel desk.', 6),
            _inc_excluded('Flight tickets, airport taxes, or interstate railway fares.', 7),
            _inc_excluded('Individual entry monuments cards, camera licenses, and national park safari slips.', 8),
            _inc_excluded('Personal expenses such as laundry, long-distance phone billing, mini-bar consumption, and gratuities.', 9),
            _inc_excluded('Optional adventure tours or extra vehicle kilometers outside planned boundaries.', 10),
        ],
    )
    return package, itinerary

def build_kl_015(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-015'
    tour_code = 'TRAGUIN-KL-015'
    title = 'Kanyakumari with South Kerala Express'
    duration = '06 Nights / 07 Days'
    slug = 'kl-015-kanyakumari-with-south-kerala-express'
    itin_slug = 'kl-015-kanyakumari-with-south-kerala-express-itinerary'
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
            _ph('State / Country: Kerala & Tamil Nadu, India | Category: Luxury Family Tour', 2),
            _ph('Destinations: Cochin • Munnar • Alleppey Houseboat • Kovalam • Kanyakumari', 3),
            _ph('Ideal for: Families, Couples & Leisure Travelers', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Multi-Destination FIT Tour', 7),
            _ph('Vehicle: Dedicated Luxury Air-Conditioned Toyota Innova Crysta / Premium Sedan', 8),
            _ph('Meal Plan: Modified American Plan (Gourmet Breakfasts & Dinners at all resorts; All meals included on Houseboat)', 9),
            _ph('Route Map: Cochin Arrival → Munnar Hills → Alleppey Backwaters → Kovalam Beach → Kanyakumari Confluence → Trivandrum Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by premium travel specialists with priority check-ins, complimentary tea tasting in Munnar, and private backwater high-tea experience.', 11),
            _ph('Shopping: Fresh tea leaves and eucalyptus oils from Munnar; Kasavu sarees, banana chips, and cashew nuts from Trivandrum & Kovalam', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; houseboat AC 21:00–06:00 hrs on standard boats; traditional attire required at Padmanabhaswamy Temple', 13),
        ],
        moods=['Family', 'Culture', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kanyakumari with South Kerala Express • 06 Nights / 07 Days',
        overview=(
            'Welcome to an unforgettable voyage slicing through the cultural heart and spectacular maritime edges of South India. This signature itinerary, thoughtfully curated by TRAGUIN, perfectly blends the high green hills of Munnar, the calm emerald channels of Alleppey, the golden beach horizons of Kovalam, and the sacred ocean confluence at Kanyakumari. Prepare for a seamless premium stay where luxury hospitality meets timeless natural heritage. Premium Travel Proposal Page\n\nAre you searching for the definitive Best Kerala Tour Package or a high-end Kerala Honeymoon Package? This specialized cross-state route targets the absolute top tourist places in Kerala and South India. Experience the timeless allure of the Munnar tea heritage, explore popular Instagram locations along Kovalam’s crescent coastlines, and take in the spiritual scenic beauty of Kanyakumari where three grand oceans meet. Choosing our signature TRAGUIN Kerala Packages ensures that your family steps away from crowded mass tours. Our focus centers on curated experiences, breathtaking landscapes, and premium stays. Whether it’s an eco-adventure inside Eravikulam or shopping for aromatic spices in old trade ports, this is the ultimate luxury Kerala holiday your family deserves. EMERALD HILLS WELCOME TEA ESTATES & EXOTIC WILDLIFE\n\nTRAGUIN Curated Touch: Curated by premium travel specialists with priority check-ins, complimentary tea tasting in Munnar, and private backwater high-tea experience.'
        ),
        seo_title='KL-015 | Kanyakumari with South Kerala Express | TRAGUIN',
        seo_description='Premium 06 Nights / 07 Days Kerala package (KL-015 / TRAGUIN-KL-015): Cochin • Munnar • Alleppey Houseboat • Kovalam • Kanyakumari. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Munnar Eravikulam National Park and Tata Tea Museum', 1),
            _ih('Private Alleppey Kettuvallam houseboat cruise', 2),
            _ih('Kovalam Lighthouse Beach and Ayurvedic spa', 3),
            _ih('Kanyakumari Vivekananda Rock Memorial and sunset confluence', 4),
            _ih('Padmanabhaswamy Temple and Kuthira Malika Palace in Trivandrum', 5),
        ],
        days=[
            _day(
                1,
                'COCHIN TO MUNNAR',
                (
                    'Arrive at Cochin International Airport where your professional TRAGUIN driver manager extends a warm, personalized welcome. Board your luxury private vehicle and quickly leave the city bustle behind as you ascend toward Munnar. The scenic route winds past misty gaps and the dramatic cascading sprays of Cheeyappara and Valara waterfalls. Arrive at your handpicked luxury mountain resort for a seamless check-in and an evening at total leisure.'
                ),
                [
                    'Sightseeing Included: Cheeyappara Waterfalls, Valara Eco-points, Tea Garden driveways.',
                    'Evening Experience: Sip on fine, locally grown cardamom tea during a welcome briefing by our local expert.',
                    'Overnight Stay: Premium Luxury Mountain Resort, Munnar.',
                    'Meals Included: Welcome Drink & Gourmet Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'MUNNAR SIGHTSEEING',
                (
                    "Enjoy a beautiful hill-station breakfast before a full-day exploration of Munnar's iconic attractions. Ride up to Eravikulam National Park, the sanctuary of the endangered Nilgiri Tahr, offering panoramic vistas of clouds resting on green peaks. Later, visit the engineering marvel of Mattupetty Dam, enjoy the natural acoustics at Echo Point, and stroll hand-in-hand through rows of a historic spice plantation."
                ),
                [
                    'Sightseeing Included: Eravikulam National Park, Mattupetty Dam, Echo Point, Tata Tea Museum.',
                    'Photography Points: The symmetrical, velvety tea fields of Kundala Lake.',
                    'Overnight Stay: Premium Luxury Mountain Resort, Munnar.',
                    'Meals Included: Full Buffet Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'MUNNAR TO ALLEPPEY HOUSEBOAT',
                (
                    'After breakfast, descend the hills towards the tranquil backwaters of Alleppey. Step aboard your private luxury Kettuvallam (Houseboat), exclusively vetted by TRAGUIN. Drift past quiet palm-fringed canals, traditional lakeside hamlets, and vast paddy fields. Relax as your personal onboard chef serves fresh, authentic Malabar delicacies tailored to your preference.'
                ),
                [
                    'Sightseeing Included: Vembanad Lake Cruise, Alleppey narrow backwater canals.',
                    'Overnight Stay: Premium Private AC Houseboat, Alleppey.',
                    'Meals Included: Breakfast, Traditional Lunch, High-Tea Snacks & Seafood Dinner.',
                ],
            ),
            _day(
                4,
                'ALLEPPEY TO KOVALAM',
                (
                    'Wake up to a quiet morning over the waters. Disembark after breakfast and drive south to Kovalam Beach, a premier coastal paradise. Check into an ultra-luxury cliff resort overlooking the Arabian Sea. Spend your afternoon relaxing on the iconic Light House Beach, or walking across the soft sands of Hawa Beach as waves roll in.'
                ),
                [
                    'Sightseeing Included: Light House Beach, Vizhinjam Marine Aquarium, Sagarika Marine Gallery.',
                    'Optional Activities: Indulge in an authentic, rejuvenating Ayurvedic full-body massage at the resort spa.',
                    'Overnight Stay: Ultra-Luxury Beachfront Resort, Kovalam.',
                    'Meals Included: Full Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'KOVALAM TO KANYAKUMARI',
                (
                    'Following breakfast, take a beautiful coastal drive across the border into Tamil Nadu to reach Kanyakumari. Board a safe private ferry to the iconic Vivekananda Rock Memorial and the colossal Thiruvalluvar Statue towering over the sea. In the evening, gather at the viewing point to witness a breathtaking sunset where the Arabian Sea, the Bay of Bengal, and the Indian Ocean merge.'
                ),
                [
                    'Sightseeing Included: Vivekananda Rock Memorial, Thiruvalluvar Statue, Kumari Amman Temple, Sunset',
                    'Emotional Storytelling: Stand at the literal geographic tip of India, absorbing the spiritual energy of the rocky',
                    'Overnight Stay: Premium Ocean-View Hotel, Kanyakumari.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                6,
                'KANYAKUMARI TO KOVALAM (VIA TRIVANDRUM)',
                (
                    "Witness a magnificent Kanyakumari sunrise over the ocean. After breakfast, drive back towards Kovalam, stopping in Trivandrum to visit the architectural masterpiece of Padmanabhaswamy Temple (the world's richest temple). Admire the classical wooden art at Kuthira Malika Palace before returning to your luxury Kovalam resort for a final celebratory evening."
                ),
                [
                    'Sightseeing Included: Sri Padmanabhaswamy Temple, Kuthira Malika Palace Museum, Napier Museum.',
                    'Food Suggestions: Enjoy a luxury lunch featuring traditional sadhya served on a banana leaf in Trivandrum.',
                    'Overnight Stay: Ultra-Luxury Beachfront Resort, Kovalam.',
                    'Meals Included: Breakfast & Festive Farewell Dinner.',
                ],
            ),
        ],
        hotels=[
            _hotel('Tea Castle Munnar', 'Munnar', '02 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1),
            _hotel('Deluxe AC Houseboat', 'Alleppey', '01 Night', 'Deluxe', 'Deluxe AC Cabin', 'All Meals on Houseboat', 4, 2),
            _hotel('Soma Palmshore Resort', 'Kovalam', '02 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 3),
            _hotel('Hotel Seaview', 'Kanyakumari', '01 Night', 'Deluxe', 'Sea View Room', 'Breakfast & Dinner', 4, 4),
            _hotel('Blanket Hotel & Spa', 'Munnar', '02 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 5),
            _hotel('Premium AC Houseboat', 'Alleppey', '01 Night', 'Premium', 'Premium AC Cabin', 'All Meals on Houseboat', 4, 6),
            _hotel('Uday Samudra Beach Resort', 'Kovalam', '02 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 7),
            _hotel('Sparsa Resort Kanyakumari', 'Kanyakumari', '01 Night', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 8),
            _hotel('The Panoramic Getaway', 'Munnar', '02 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 9),
            _hotel('Luxury Private Cruise', 'Alleppey', '01 Night', 'Luxury', 'Luxury Private Cabin', 'All Meals on Houseboat', 5, 10),
            _hotel('The Leela Kovalam (Garden View)', 'Kovalam', '02 Nights', 'Luxury', 'Garden View Room', 'Breakfast & Dinner', 5, 11),
            _hotel('Annai Resorts & Spa', 'Kanyakumari', '01 Night', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 12),
            _hotel("Chandy's Windy Woods", 'Munnar', '02 Nights', 'Ultra Luxury', 'Suite', 'Breakfast & Dinner', 5, 13),
            _hotel('Premium Glass Houseboat', 'Alleppey', '01 Night', 'Ultra Luxury', 'Premium Glass Cabin', 'All Meals on Houseboat', 5, 14),
            _hotel('The Leela Kovalam (Club Suite)', 'Kovalam', '02 Nights', 'Ultra Luxury', 'Club Suite', 'Breakfast & Dinner', 5, 15),
            _hotel('Hotel Tri Sea (Suite Room)', 'Kanyakumari', '01 Night', 'Ultra Luxury', 'Suite Room', 'Breakfast & Dinner', 5, 16),
        ],
        inclusions=[
            _inc_included('Accommodation: 06 Nights stay at top-rated, handpicked luxury hotels and premium beach resorts.', 1),
            _inc_included('Meals: 06 Buffet Breakfasts & 06 curated dinners at hotels, plus all meals prepared live on the Alleppey Houseboat.', 2),
            _inc_included('Transfers & Sightseeing: Chauffeur-driven, air-conditioned luxury Innova Crysta for smooth private transfers and all sightseeing destinations.', 3),
            _inc_included('Assistance: 24/7 dedicated concierge desk and support during the entire journey.', 4),
            _inc_included('Taxes: All applicable luxury resort taxes, toll fees, and driver permits included.', 5),
            _inc_included('Welcome Amenities: Cold towels, traditional fresh garlands, and a basket of curated tropical fruits upon arrival.', 6),
            _inc_excluded('Airfare or interstate train tickets to Cochin / from Trivandrum.', 7),
            _inc_excluded('Entry tickets to monuments, museums, or ferry rides at Vivekananda Rock.', 8),
            _inc_excluded('Personal expenses such as laundry, phone bills, premium beverages, and tipping.', 9),
            _inc_excluded('Optional tours, water sports, or independent vehicle usage outside the planned hours.', 10),
            _inc_excluded('Mandatory international travel insurance or medical cover.', 11),
        ],
    )
    return package, itinerary

def build_kl_016(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-016'
    tour_code = 'TRAGUIN-KL-016'
    title = 'Misty Hills & Houseboat Romance Premium Holiday'
    duration = '05 Nights / 06 Days'
    slug = 'kl-016-misty-hills-houseboat-romance-premium-holiday'
    itin_slug = 'kl-016-misty-hills-houseboat-romance-premium-holiday-itinerary'
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
            _ph('State / Country: Kerala / India | Category: Honeymoon / Romance', 2),
            _ph('Destinations: Munnar • Thekkady • Alleppey Backwaters • Cochin', 3),
            _ph('Ideal for: Newlyweds & Couples', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Luxury Honeymoon FIT Getaway', 7),
            _ph('Vehicle: Private Executive Air-Conditioned Sedan / Innova Crysta Chauffeur Driven', 8),
            _ph('Meal Plan: Deluxe Buffet Breakfast at Resorts & All Gourmet Meals on the Houseboat', 9),
            _ph('Route Map: Cochin Arrival → Munnar Hills (2N) → Thekkady Wildlife Sanctuary (1N) → Alleppey Floating Houseboat (1N) → Cochin Heritage (1N) & Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with priority room check-ins, custom sweet treats, premium panoramic views, and executive private transport.', 11),
            _ph('Shopping: Plantation tea, homemade chocolates, eucalyptus oils from Munnar; cardamom and pepper from Thekkady; Kasavu sarees and brass lamps from Jew Town', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; light warm clothing for Munnar; houseboat AC 21:00–06:00 hrs unless ultra-luxury option chosen', 13),
        ],
        moods=['Romance', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Misty Hills & Houseboat Romance Premium Holiday • 05 Nights / 06 Days',
        overview=(
            "Step into a realm where nature sings a love song. Handcrafted with passion by TRAGUIN, this ultra-luxury escape invites you to experience the breathtaking landscapes of God's Own Country. From the crisp misty layers of Munnar's endless tea carpets to the golden, sun-kissed channels of the Alleppey backwaters, let us wrap your new beginnings in curated experiences and unforgettable memories. Premium Luxury Proposal Page\n\nflower bed arrangements, a candlelit dinner, custom honeymoon cake, private spice garden tours, and immersive sunset cruises away from the crowds. THE ULTIMATE LUXURY KERALA HOLIDAY: WHY VISIT? Kerala stands unmatched as India's premier romantic destination. If you are seeking the absolute Best Kerala Tour Package or a completely tailored Kerala Family Tour, the unique blend of hill stations, forests, and inland channels presents premium stays of a lifetime. Witness top tourist places in Kerala including the iconic attractions of Eravikulam National Park, Mattupetty Dam, and the Periyar Wildlife Sanctuary. Our signature TRAGUIN Kerala Packages ensure immersive experiences, such as witnessing Kathakali dance arts, exploring aromatic fields, and photographing the popular Instagram locations of Fort Cochin's historical avenues. The best time to visit Kerala is during the refreshing winter and spring months, when the scenic beauty is at its grandest.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts with priority room check-ins, custom sweet treats, premium panoramic views, and executive private transport."
        ),
        seo_title='KL-016 | Misty Hills & Houseboat Romance Premium Holiday | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kerala package (KL-016 / TRAGUIN-KL-016): Munnar • Thekkady • Alleppey Backwaters • Cochin. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Munnar Eravikulam National Park and Mattupetty boating', 1),
            _ih('Thekkady spice plantation walk and Periyar Lake safari', 2),
            _ih('Private Alleppey houseboat with honeymoon cake and decorations', 3),
            _ih('Fort Cochin Chinese Fishing Nets and Jew Town', 4),
            _ih('TRAGUIN honeymoon amenities with candlelit dining', 5),
        ],
        days=[
            _day(
                1,
                'COCHIN TO MUNNAR',
                (
                    'Arrive at Cochin International Airport where your private luxury vehicle and executive chauffeur await you. Embark on a breathtakingly scenic drive towards the hills of Munnar. As you ascend, watch the transformation into lush green mountain terrain dotted with roaring waterfalls. Stop by the beautiful Valara and Cheeyappara waterfalls for iconic photography points. Arrive at your handpicked hotel and check in to a beautifully decorated room.'
                ),
                [
                    'Sightseeing Included: Cheeyappara & Valara Falls, Munnar Tea Gardens.',
                    'Evening Experience: A refreshing complimentary high-tea welcome by TRAGUIN experts amidst the tea',
                    'Overnight Stay: Handpicked Luxury Resort, Munnar.',
                    'Meals Included: Welcome Drink & Gourmet Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'MUNNAR EXCURSION',
                (
                    'Wake up to the sounds of mountain birds. Today, embark on a full-day Kerala sightseeing journey across Munnar. Visit the famous Eravikulam National Park, home to the endangered Nilgiri Tahr, and catch dramatic panoramic views of cloud-shrouded peaks. Continue to Mattupetty Dam for a private boating session, visit the enchanting Echo Point, and stroll hand-in-hand through blossom-filled valley gardens.'
                ),
                [
                    'Sightseeing Included: Eravikulam National Park, Mattupetty Lake, Echo Point, Tea Museum.',
                    "Optional Activities: A romantic premium couple's spa session overlooking the misty valleys.",
                    'Overnight Stay: Luxury Mountain Resort, Munnar.',
                    'Meals Included: Premium Breakfast & Candlelit Honeymoon Dinner.',
                ],
            ),
            _day(
                4,
                'THEKKADY TO ALLEPPEY HOUSEBOAT',
                (
                    'Leave the hills behind as you slide into the iconic water-kingdom of Alleppey. Check into your exclusive, private luxury TRAGUIN-vetted houseboat. Cruise along the vast, shimmering expanse of Vembanad Lake, passing palm-lined canals, remote villages, and floating water lilies. Witness the sunset over the horizon while your onboard personal chef prepares delicacies just for you.'
                ),
                [
                    'Sightseeing Included: Alleppey Backwaters Cruise, Traditional Fishing Nets View.',
                    'Honeymoon Highlights: Complimentary custom honeymoon cake, flower decorations, and fresh seafood',
                    'Overnight Stay: Private Luxury AC Houseboat, Alleppey.',
                    'Meals Included: Traditional Lunch, Evening High Tea, and Premium Dinner.',
                ],
            ),
            _day(
                5,
                'ALLEPPEY TO COCHIN',
                (
                    "Disembark your houseboat after a tranquil breakfast and drive to the historic port city of Cochin. Spend the afternoon exploring Fort Cochin's colonial past. Walk along the beach to admire the massive Chinese Fishing Nets, visit the ancient Santa Cruz Basilica, and wander through Jew Town to explore local antique boutiques and colorful spice markets."
                ),
                [
                    'Sightseeing Included: Fort Cochin Beach, Chinese Fishing Nets, Mattancherry Palace, Jew Town.',
                    'Food Suggestions: Dine at iconic upscale cafes tucked into old Dutch colonial warehouses.',
                    'Overnight Stay: Premium Luxury Boutique Hotel, Cochin.',
                    'Meals Included: Breakfast & Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'COCHIN DEPARTURE',
                (
                    'Conclude your luxury holiday with a rich breakfast buffet. Take a final walk along the historic coastal drive before your private vehicle arrives to transfer you comfortably to Cochin International Airport for your journey home. Your premium TRAGUIN romance package concludes with memories to cherish forever.'
                ),
                [
                    'Transfers Included: Private Luxury Airport Drop-off.',
                    'Meals Included: Full Breakfast Buffet.',
                ],
            ),
        ],
        hotels=[
            _hotel('Amber Dale Luxury Hotel', 'Munnar', '02 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1),
            _hotel('The Elephant Court', 'Thekkady', '01 Night', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 2),
            _hotel('Deluxe Private AC Houseboat', 'Alleppey', '01 Night', 'Deluxe', 'Deluxe AC Cabin', 'Full Board on Houseboat', 4, 3),
            _hotel('Blanket Hotel & Spa', 'Munnar', '02 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 4),
            _hotel('Poetree Sarovar Portico', 'Thekkady', '01 Night', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 5),
            _hotel('Premium Luxury Houseboat', 'Alleppey', '01 Night', 'Premium', 'Premium Cabin', 'Full Board on Houseboat', 4, 6),
            _hotel('The Panoramic Getaway', 'Munnar', '02 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 7),
            _hotel('Greenwoods Resort', 'Thekkady', '01 Night', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 8),
            _hotel('Luxury Super Luxury Glass-Wall Boat', 'Alleppey', '01 Night', 'Luxury', 'Glass-Wall Suite', 'Full Board on Houseboat', 5, 9),
            _hotel("Chandy's Windy Woods Ultra", 'Munnar', '02 Nights', 'Ultra Luxury', 'Ultra Suite', 'Breakfast & Dinner', 5, 10),
            _hotel('Spice Village CGH Earth', 'Thekkady', '01 Night', 'Ultra Luxury', 'Heritage Cottage', 'Breakfast & Dinner', 5, 11),
            _hotel('Ultra-Luxury Floating Villa', 'Alleppey', '01 Night', 'Ultra Luxury', 'Floating Villa', 'Full Board on Houseboat', 5, 12),
        ],
        inclusions=[
            _inc_included('Accommodation: Premium handpicked luxury hotels and resort stays across Kerala.', 1),
            _inc_included('Meals: Daily multi-cuisine buffet breakfasts and full board culinary meals inside your private houseboat.', 2),
            _inc_included('Transfers & Sightseeing: All sightseeing tours by air-conditioned executive luxury vehicle with dedicated driver.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated professional destination concierge management.', 4),
            _inc_included('Honeymoon Amenities: Flower bed layout decoration, complimentary customized cake, and private candlelit dining setup.', 5),
            _inc_included('Taxes & Fees: All local toll taxes, driver parking allowances, and fuel surcharges included.', 6),
            _inc_excluded('Airfare or interstate train tickets to Cochin.', 7),
            _inc_excluded('Direct monument entry tickets, camera tickets, or local guide services.', 8),
            _inc_excluded('Personal expenses such as premium alcoholic beverages, laundry, and room tip tips.', 9),
            _inc_excluded('Optional activities such as river rafting or elephant rides.', 10),
        ],
    )
    return package, itinerary

def build_kl_017(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-017'
    tour_code = 'TRAGUIN-KL-017'
    title = 'Varkala Cliff Beach Honeymoon'
    duration = '03 Nights / 04 Days'
    slug = 'kl-017-varkala-cliff-beach-honeymoon'
    itin_slug = 'kl-017-varkala-cliff-beach-honeymoon-itinerary'
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
            _ph('State / Country: Kerala, India | Category: Luxury Honeymoon Package', 2),
            _ph('Destinations: Varkala Cliff Beach • Trivandrum • Kappil', 3),
            _ph('Ideal for: Newlyweds & Couples', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Coastal Honeymoon FIT Escape', 7),
            _ph('Vehicle: Private Air-Conditioned Premium Sedan (Luxury Chauffeur-driven)', 8),
            _ph('Meal Plan: Continental Breakfast & Specially Curated Honeymoon Dinners', 9),
            _ph('Route Map: Trivandrum Arrival → Varkala Cliff Beach → Kappil Beach Backwaters → Trivandrum Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts specifically for newlyweds with priority room upgrades, premium cliffside dining decks, and customized photography assistance.', 11),
            _ph('Shopping: Lightweight cotton beachwear, silver jewelry, Tibetan handicrafts, incense, and aromatic oils from Varkala Cliff markets', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; swimming subject to lifeguard instructions; reserve paragliding and Ayurvedic spa in advance', 13),
        ],
        moods=['Romance', 'Beach', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Varkala Cliff Beach Honeymoon • 03 Nights / 04 Days',
        overview=(
            'Welcome note: Step into a coastal dreamland where majestic red cliffs meet the endless expanse of the Arabian Sea. This romantic, high-end travel proposal by TRAGUIN is expertly tailored to deliver an intimate blend of relaxation, dramatic oceanside vistas, and modern luxury. Indulge in private candlelight dinners, soothing wellness rituals, and mesmerizing sunsets crafted to ignite lifelong romantic memories. Premium Honeymoon Experiences Page\n\nromantic escape with zero-stress scheduling, premium stays, intimate oceanside locations, and bespoke styling designed flawlessly for discerning couples. THE ULTIMATE LUXURY VARKALA EXPERIENCE: WHY VISIT? Varkala, celebrated for its striking lateral geological cliffs, stands out as one of the most romantic destinations in South India. For couples searching for the Best Kerala Tour Package or a memorable Kerala Honeymoon Package, this itinerary seamlessly combines beachside allure with high-end tranquility. From exploring the iconic attractions along the active Varkala Cliff to capturing breathtaking sunset photographs at the highly searched Kappil Beach and Backwaters, our Luxury Kerala Holiday guarantees top-tier comfort. Key romantic highlights include dining on top-rated seaside decks, participating in deep spiritual legacy walks near the Janardanaswamy Temple, and lounging at premium handpicked cliffside resorts. Let our TRAGUIN Kerala Packages elevate your luxury journey with unmatched local hospitality.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts specifically for newlyweds with priority room upgrades, premium cliffside dining decks, and customized photography assistance.'
        ),
        seo_title='KL-017 | Varkala Cliff Beach Honeymoon | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Kerala package (KL-017 / TRAGUIN-KL-017): Varkala Cliff Beach • Trivandrum • Kappil. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Varkala Cliff coastal walk and Papanasam Beach', 1),
            _ih('Janardanaswamy Temple and cliff-edge candlelight dinner', 2),
            _ih('Kappil Beach and Edava Lagoon mangrove country boat cruise', 3),
            _ih('Optional Ayurvedic wellness or paragliding experiences', 4),
            _ih('TRAGUIN honeymoon floral setup and custom cake', 5),
        ],
        days=[
            _day(
                1,
                'ARRIVAL TRIVANDRUM TO VARKALA CLIFF',
                (
                    'Arrive at Trivandrum International Airport, where your personal premium vehicle and professional chauffeur await you. Experience a smooth, scenic journey as you drive towards the breathtaking landscapes of Varkala. Arrive at your handpicked ultra-luxury cliffside resort and check in seamlessly to your premium ocean-view cottage. Enjoy a relaxed afternoon with your loved one. As evening sets in, enjoy an intimate walk along the lively Varkala Cliff, exploring boho-chic cafes and listening to the rhythmic crashing of the waves below.'
                ),
                [
                    'Sightseeing Included: Private Airport Transfer, Varkala Cliff Coastal Walk.',
                    'Evening Experience: Indulge in a welcoming signature high-tea set against the setting sun, curated by',
                    'Overnight Stay: Handpicked Ultra-Luxury Cliff Resort, Varkala.',
                    'Meals Included: Welcome Drink & Romantic Welcome Dinner.',
                ],
            ),
            _day(
                2,
                'VARKALA CLIFF & BEACH IMMERSION',
                (
                    'Savor a luxurious floating breakfast in your private plunge pool. Spend your morning relaxing on the golden sands of Papanasam Beach (Varkala Beach), framed beautifully by majestic red cliffs. In the afternoon, enjoy an immersive local culture experience with a visit to the 2,000-year-old Janardanaswamy Temple. For sunset, your chauffeur will escort you to an exclusive beach photography point to capture unforgettable memories. Cap off the night with an exquisite private candlelight dinner right on the cliff edge.'
                ),
                [
                    'Sightseeing Included: Varkala Beach, Janardanaswamy Temple, Cliff Viewpoint.',
                    "Optional Activities: Couples' traditional Ayurvedic wellness massage or a tandem paragliding session off the",
                    'Evening Experience: Bespoke private candlelight dinner with a custom premium cake.',
                    'Overnight Stay: Handpicked Ultra-Luxury Cliff Resort, Varkala.',
                    'Meals Included: Gourmet Breakfast & Private Candlelight Dinner.',
                ],
            ),
            _day(
                3,
                'KAPPIL BEACH & EDAVA LAGOON',
                (
                    'After a relaxed premium breakfast, take a highly scenic drive towards Kappil Beach, located just north of Varkala. Here, witness a spectacular natural phenomenon where the calm backwaters run parallel to the crashing sea, separated only by a narrow road. Embark on a private, safely designed country boat cruise through the tranquil mangroves of Edava Lagoon. Spend your afternoon at leisure, shopping for local souvenirs or unwinding at an iconic cliffside cafe overlooking the ocean.'
                ),
                [
                    'Sightseeing Included: Kappil Beach road drive, Edava Lagoon Mangrove Cruise, Odayam Beach.',
                    'Photography Points: The breathtaking narrow bridge of Kappil flanked by water on both sides.',
                    'Overnight Stay: Handpicked Ultra-Luxury Cliff Resort, Varkala.',
                    'Meals Included: Full Breakfast & Seafood Specialty Dinner.',
                ],
            ),
            _day(
                4,
                'DEPARTURE FROM TRIVANDRUM',
                (
                    'Awake to the soothing melody of ocean waves. Savor a final, relaxed breakfast at your resort while taking in your last views of the Arabian Sea. Your premium private vehicle will arrive to transfer you comfortably back to Trivandrum International Airport for your return flight home. Your unforgettable TRAGUIN Kerala Honeymoon Package concludes, leaving you with timeless memories of a magical coastal escape.'
                ),
                [
                    'Transfers Included: Private Chauffeur Airport Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Clafouti Beach Resort', 'Varkala', '03 Nights', 'Deluxe', 'Superior Sea View Room', 'CP (Breakfast Only)', 4, 1),
            _hotel('The Gateway Hotel Varkala (IHCL)', 'Varkala', '03 Nights', 'Premium', 'Superior Ocean View Room', 'MAP (Breakfast + Dinner)', 4, 2),
            _hotel('Elixir Cliff Beach Resort & Spa', 'Varkala', '03 Nights', 'Luxury', 'Luxury Ocean Jacuzzi Suite', 'MAP (Breakfast + Special Dinner)', 5, 3),
            _hotel("B'Canti Boutique Beach Resort", 'Varkala', '03 Nights', 'Ultra Luxury', 'Private Plunge Pool Garden Villa', 'Honeymoon Premium (All Inclusive Setup)', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights stay at premium handpicked hotels with direct ocean views.', 1),
            _inc_included('Meals: Daily gourmet breakfasts and 03 specially designed romantic dinners.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven premium air-conditioned vehicle for all transfers and iconic attractions.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local concierge assistance for smooth experiences.', 4),
            _inc_included('Welcome Amenities: Honeymoon welcome floral setup, premium bed decorations, and a custom cake upon arrival.', 5),
            _inc_included('Complimentary Experiences: Private mangrove country boat cruise at Edava Lagoon. PACKAGE EXCLUSIONS', 6),
            _inc_excluded('Flights or Interstate train tickets to and from Trivandrum.', 7),
            _inc_excluded('Entry tickets to monuments, water sports, paragliding, or camera passes.', 8),
            _inc_excluded('Personal expenses such as laundry, liquor, telephone calls, and tips.', 9),
            _inc_excluded('Optional tours, Ayurvedic spa sessions, or vehicle usage outside specified routes.', 10),
            _inc_excluded('Mandatory travel insurance and GST/TCS taxes.', 11),
        ],
    )
    return package, itinerary

def build_kl_018(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-018'
    tour_code = 'TRAGUIN-KL-018'
    title = 'Complete Malabar & Kovalam Luxury Express'
    duration = '07 Nights / 08 Days'
    slug = 'kl-018-complete-malabar-kovalam-luxury-express'
    itin_slug = 'kl-018-complete-malabar-kovalam-luxury-express-itinerary'
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
            _ph('State / Country: Kerala, India | Category: Luxury Holiday', 2),
            _ph('Destinations: Calicut • Wayanad • Bekal (Malabar) • Kovalam', 3),
            _ph('Ideal for: Couples, Families & Luxury Seekers', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Grand Malabar FIT Tour', 7),
            _ph('Vehicle: Private Chauffeur-driven AC Toyota Innova Crysta / Luxury Sedan', 8),
            _ph('Meal Plan: Daily Premium Buffet Breakfast & Gourmet Dinners at Resorts', 9),
            _ph('Route Map: Calicut Arrival → Wayanad Hills → Bekal Fort Coast → Internal Flight/Transfer → Kovalam Beach → Trivandrum Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with finest luxury stays, personalized on-ground assistance, private charters, and exclusive beachfront recommendations.', 11),
            _ph('Shopping: Premium black pepper, organic cardamom, and vanilla pods from Wayanad; Balaramapuram Kasavu sarees and traditional dhotis from Trivandrum', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; traditional modest attire required at temple heritage zones in Trivandrum', 13),
        ],
        moods=['Luxury', 'Nature', 'Beach'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Complete Malabar & Kovalam Luxury Express • 07 Nights / 08 Days',
        overview=(
            "Wayanad Bekal (Malabar) Kovalam IDEAL FOR: Couples, Families & Luxury Seekers BEST SEASON: September to May TRAGUIN TOUR CODE: TRAGUIN-KL-018 TRAGUIN PREMIUM KERALA TOUR PACKAGE COMPLETE MALABAR & KOVALAM LUXURY EXPRESS Embark on a grand, highly selective journey spanning from the untouched royal coastal heritage of Malabar down to the world-famous cliff beaches of Southern Kerala. Specially curated by TRAGUIN, this ultra-luxury vacation brings together pristine handpicked hotels, majestic backwaters, misty hills, and rich cultural immersion into an elite custom itinerary.\n\nFor discerning globetrotters seeking the absolute Best Kerala Tour Package or an unforgettable Kerala Honeymoon Package, this grand route showcases top tourist places in Kerala that are rich in scenic beauty and heritage. From the misty high-altitude rainforests of Wayanad and the majestic coastal ramparts of Bekal Fort to the pristine crescent beaches of Kovalam, our Luxury Kerala Holiday offers an unmatched blend of privacy and luxury. Avoid the crowded conventional paths and explore the elite side of God's Own Country. Our TRAGUIN Kerala Packages ensure immersive local experiences including private spice walk tours, classical backwater boat cruises, luxury spa access, and memorable regional dining points.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts with finest luxury stays, personalized on-ground assistance, private charters, and exclusive beachfront recommendations."
        ),
        seo_title='KL-018 | Complete Malabar & Kovalam Luxury Express | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Kerala package (KL-018 / TRAGUIN-KL-018): Calicut • Wayanad • Bekal (Malabar) • Kovalam. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Wayanad Edakkal Caves, Pookode Lake & Banasura Sagar Dam', 1),
            _ih('Bekal Fort and Valiyaparamba private backwater cruise', 2),
            _ih('Kovalam Lighthouse Beach and private candlelight dinner', 3),
            _ih('Trivandrum Padmanabhaswamy Temple and Napier Museum', 4),
            _ih('TRAGUIN Signature Experience with elite five-star properties', 5),
        ],
        days=[
            _day(
                1,
                'ARRIVAL CALICUT TO WAYANAD',
                (
                    'Arrive at Calicut (Kozhikode) International Airport. Enjoy a premium welcoming reception organized by your TRAGUIN holiday concierge. Board your luxury private vehicle and embark on a breathtaking drive through the famous 9 hairpin curves of the Thamarassery Churam pass to reach the misty green hills of Wayanad. Check into your ultra-luxury nature resort nestled inside deep coffee plantations.'
                ),
                [
                    'Sightseeing Included: Thamarassery Mountain Pass Viewpoint, Plantation Walk.',
                    'Overnight Stay: Handpicked Luxury Resort, Wayanad.',
                    'Meals Included: Welcome High Tea & Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'WAYANAD EXPLORATION',
                (
                    "Indulge in a fresh organic breakfast. Visit the historic Edakkal Caves, showcasing prehistoric rock carvings dating back thousands of years. Later, experience a quiet private boat cruise on the peaceful waters of Pookode Lake, surrounded by dense evergreen woods. Spend your evening enjoying a luxury therapeutic couples massage at the resort's premium spa."
                ),
                [
                    'Sightseeing Included: Edakkal Caves, Pookode Lake, Banasura Sagar Dam.',
                    "Photography Points: Stunning landscape shots from the top of Banasura Sagar Dam (India's largest earth",
                    'Overnight Stay: Handpicked Luxury Resort, Wayanad.',
                    'Meals Included: Full Breakfast & Gourmet Dinner.',
                ],
            ),
            _day(
                3,
                'WAYANAD TO BEKAL',
                (
                    'After a scenic breakfast, check out and enjoy a beautiful coastal drive towards the northernmost gem of Malabar—Bekal. Known for its secluded sands and rich fortress history, Bekal offers complete privacy. Arrive and check into your sprawling five-star beach villa resort featuring private plunge pools and direct sea access.'
                ),
                [
                    'Sightseeing Included: Kappil Beach, Coastal Drive.',
                    'Evening Experience: Watch a majestic sunset over the Arabian Sea directly from your resort deck.',
                    'Overnight Stay: Ultra-Luxury Beach Resort, Bekal.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                4,
                'BEKAL FORT & BACKWATERS',
                (
                    'Explore the magnificent Bekal Fort, a stunning 17th-century seaside fortress that stands as one of the top tourist places in Kerala. Walk along the historic brick ramparts as the ocean waves crash below. In the afternoon, embark on an exclusive private motor-yacht cruise through the untouched Valiyaparamba backwaters, a highly searched premium experience in Malabar.'
                ),
                [
                    'Sightseeing Included: Bekal Fort complex, Bekal Beach Park, Valiyaparamba cruise.',
                    'Overnight Stay: Ultra-Luxury Beach Resort, Bekal.',
                    'Meals Included: Breakfast & curated Seafood Dinner.',
                ],
            ),
            _day(
                5,
                'BEKAL TO KOVALAM',
                (
                    'Enjoy a leisurely morning. Transfer comfortably to the airport for your internal transit flight/express connectivity down to Trivandrum. Upon arrival, your private chauffeur-driven vehicle will transfer you directly to your iconic cliff-top luxury resort in Kovalam. Relax in your premium suite overlooking the vast sea lines.'
                ),
                [
                    'Transfers Included: Luxury Airport Transfers & Inter-city Transit.',
                    'Overnight Stay: Iconic 5-Star Cliff Resort, Kovalam.',
                    'Meals Included: Breakfast & Dinner.',
                ],
            ),
            _day(
                6,
                'KOVALAM BEACH EXPERIENCE',
                (
                    'Spend a glorious day enjoying the premium beaches of Kovalam. Visit the iconic Lighthouse Beach, Hawah Beach, and Samudra Beach. Climb the famous striped lighthouse for a stunning panoramic view of the coastline. In the evening, TRAGUIN experts have arranged a private beachfront candlelit dinner with a personalized menu to create unforgettable memories.'
                ),
                [
                    'Sightseeing Included: Vizhinjam Lighthouse, Marine Aquarium, Beach Promenades.',
                    'Evening Experience: Private candlelight dinner on a secluded stretch of Kovalam beach.',
                    'Overnight Stay: Iconic 5-Star Cliff Resort, Kovalam.',
                    'Meals Included: Breakfast & Custom Candlelight Dinner.',
                ],
            ),
            _day(
                7,
                'TRIVANDRUM DAY EXCURSION',
                (
                    'Take a short drive into Trivandrum city to discover its historic royal heritage. View the grand architecture of the Kuthiramalika Palace Museum (Horse Palace) and explore the rich collections inside the Napier Museum and Sri Chitra Art Gallery. Return to Kovalam for a relaxed final evening by your private infinity pool.'
                ),
                [
                    'Sightseeing Included: Padmanabhaswamy Temple area, Napier Museum, Kuthiramalika Palace.',
                    'Overnight Stay: Iconic 5-Star Cliff Resort, Kovalam.',
                    'Meals Included: Breakfast & Farewell Dinner.',
                ],
            ),
            _day(
                8,
                'DEPARTURE FROM TRIVANDRUM',
                (
                    'Enjoy a final luxurious breakfast watching the morning waves. Your premium vehicle will provide a smooth transfer to Trivandrum International Airport for your journey home. Your signature TRAGUIN Kerala Package concludes with beautiful memories of a premium, hassle-free holiday.'
                ),
                [
                    'Transfers Included: Private Luxury Airport Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Vythiri Resort', 'Wayanad', '02 Nights', 'Luxury', 'Heritage Cottage', 'Breakfast & Dinner', 5, 1),
            _hotel('Evolve Back, Kabini / Wayanad Wild', 'Wayanad', '02 Nights', 'Ultra Luxury', 'Safari Land Hut with Private Pool', 'Breakfast & Dinner', 5, 2),
            _hotel('Taj Bekal Resort & Spa', 'Bekal', '02 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 3),
            _hotel('Taj Bekal Premium Plunge Pool Villa', 'Bekal', '02 Nights', 'Ultra Luxury', 'Premium Plunge Pool Villa', 'Breakfast & Dinner', 5, 4),
            _hotel('The Leela Kovalam, A Raviz Hotel', 'Kovalam', '03 Nights', 'Luxury', 'Garden View Room', 'Breakfast & Dinner', 5, 5),
            _hotel('The Leela Kovalam Club Suite with Panoramic View', 'Kovalam', '03 Nights', 'Ultra Luxury', 'Club Suite with Panoramic View', 'Breakfast & Dinner', 5, 6),
        ],
        inclusions=[
            _inc_included('Accommodation: 07 Nights stay at handpicked 5-star premium luxury luxury resorts.', 1),
            _inc_included('Meals: Daily multi-cuisine buffet Breakfasts and curated Dinners at the properties.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated air-conditioned Luxury Innova Crysta for all planned transfers & tours.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated local concierge assistance and VIP airport assistance.', 4),
            _inc_included('Complimentary Experiences: Private candlelight beach dinner in Kovalam & exclusive Valiyaparamba backwater cruise.', 5),
            _inc_excluded('Main flights / Train fares and internal regional flight tickets.', 6),
            _inc_excluded('Personal expenses such as premium spa therapies, laundry, and beverage charges.', 7),
            _inc_excluded('Entry tickets to monuments or camera passes.', 8),
        ],
    )
    return package, itinerary

def build_kl_019(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-019'
    tour_code = 'TRAGUIN-KL-019'
    title = 'Wayanad Nature Hideaway Premium Luxury Holiday'
    duration = '03 Nights / 04 Days'
    slug = 'kl-019-wayanad-nature-hideaway-premium-luxury-holiday'
    itin_slug = 'kl-019-wayanad-nature-hideaway-premium-luxury-holiday-itinerary'
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
            _ph('State / Country: Kerala / India | Category: Leisure / Nature Escapes', 2),
            _ph('Destinations: Wayanad Nature Hideaway', 3),
            _ph('Ideal for: Families, Couples & Nature Lovers', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Luxury)', 6),
            _ph('Travel Format: Customized Private Nature FIT Tour', 7),
            _ph('Vehicle: Private Chauffeur-Driven Luxury SUV / Innova Crysta', 8),
            _ph('Meal Plan: Modified American Plan (Daily Premium Breakfast & Dinners)', 9),
            _ph('Route Map: Cochin / Calicut Arrival → Wayanad Hills → Cochin / Calicut Departure', 10),
            _ph('TRAGUIN Signature Experience: Handcrafted plantation tours away from common tourist herds with fully customized pathways engineered for optimum comfort and zero physical fatigue.', 11),
            _ph('Shopping: Pure Wayanad spices, organic robusta coffee beans, and herbal tea leaves; Chembra Peak and Banasura Dam Instagram spots', 12),
            _ph('Important: Resort check-in 14:00 hrs; light pullover advised for early morning plantation trails in Wayanad', 13),
        ],
        moods=['Nature', 'Luxury', 'Wellness'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Luxury)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Wayanad Nature Hideaway Premium Luxury Holiday • 03 Nights / 04 Days',
        overview=(
            'Wayanad Nature Hideaway IDEAL FOR: Families, Couples & Nature Lovers BEST SEASON: September to May STARTING PRICE: On Request (Premium Luxury) TRAGUIN TOUR CODE: TRAGUIN-KL-019 --- --- BEST KERALA TOUR PACKAGE WAYANAD NATURE HIDEAWAY PREMIUM LUXURY HOLIDAY Welcome to a realm where the clouds kiss the emerald peaks. Curated exclusively by TRAGUIN, this premium travel itinerary takes you deep into the heart of the mist-laden hills of Wayanad. Escape the noise of everyday life and surrender to a refreshing retreat featuring breathtaking Luxury Custom Holidays Page\n\nWayanad is highly ranked as one of the ultimate gems of any high-end Kerala Honeymoon Package or Kerala Family Tour. Famous for its sprawling spice plantations, mist-covered mountains, and\n\nTRAGUIN Curated Touch: Handcrafted plantation tours away from common tourist herds with fully customized pathways engineered for optimum comfort and zero physical fatigue.'
        ),
        seo_title='KL-019 | Wayanad Nature Hideaway Premium Luxury Holiday | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Kerala package (KL-019 / TRAGUIN-KL-019): Wayanad Nature Hideaway. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Thamarassery Churam pass and Lakkidi Viewpoint', 1),
            _ih('Edakkal Caves prehistoric petroglyphs and Pookode Lake boating', 2),
            _ih('Banasura Sagar Dam private speed-boat cruise', 3),
            _ih('Organic spice plantation trail with Ayurvedic spa option', 4),
            _ih('TRAGUIN handcrafted plantation tours away from tourist herds', 5),
        ],
        days=[
            _day(
                1,
                'COCHIN / CALICUT TO WAYANAD',
                (
                    'Arrive at the airport where your dedicated luxury transport and tour companion from TRAGUIN await you. Enjoy a picturesque drive through the iconic Thamarassery Churam mountain pass, boasting nine hairpin curves surrounded by dense tropical rainforests. Check in smoothly to your ultra-premium treehouse or plantation luxury resort. Savor a complimentary welcome drink and unwind amidst unforgettable memories of nature.'
                ),
                [
                    'Sightseeing Included: Lakkidi Viewpoint, Chain Tree Pass.',
                    'Evening Experience: A relaxing evening spent overlooking valleys with fresh plantation coffee served on your',
                    'Overnight Stay: Premium Handpicked Luxury Resort, Wayanad.',
                    'Meals Included: Welcome Drink & Curated Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'WAYANAD NATURE EXPLORATION',
                (
                    "Fuel up with a luxurious breakfast. Embark on a journey to the legendary Edakkal Caves, world- renowned for Neolithic petroglyphs and rich archaeological heritage. In the afternoon, experience the tranquil scenic beauty of Pookode Lake, a natural freshwater lake shaped like India's map, where a private row-boating experience has been pre-arranged for you by your consultant team."
                ),
                [
                    'Sightseeing Included: Edakkal Caves, Pookode Lake, Soochipara Waterfalls.',
                    'Photography Points: Panorama viewpoints atop Edakkal and the reflections on Pookode Lake.',
                    'Overnight Stay: Premium Luxury Resort, Wayanad.',
                    'Meals Included: Full Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'BANASURA EARTHEN DAM & SPICE PLANTATIONS',
                (
                    "Today, experience the grandeur of Banasura Sagar Dam. Embark on an exclusive private speed-boat cruise navigating through islands formed by the reservoir's pristine blue waters. Later, walk hand-in-hand through an organic spice plantation trail, learning the delicate history behind Kerala's world-famous cardamom, pepper, and vanilla crops."
                ),
                [
                    'Sightseeing Included: Banasura Sagar Dam, Karlad Lake Adventure Points, Spice Gardens.',
                    'Optional Activities: Therapeutic Ayurvedic spa rejuvenation ritual at the resort wellness center.',
                    'Overnight Stay: Premium Handpicked Luxury Resort, Wayanad.',
                    'Meals Included: Full Breakfast & Festive Candlelight Dinner.',
                ],
            ),
            _day(
                4,
                'DEPARTURE FROM WAYANAD',
                (
                    'Savor your last morning breakfast overlooking the canopy of clouds. Check out of your resort and enjoy a comfortable private transfer back to the airport or railway station. Your premium Kerala Sightseeing holiday wraps up seamlessly, leaving you with memories that linger far beyond the destination itself.'
                ),
                [
                    'Transfers Included: Private Airport/Station Drop-off.',
                    'Meals Included: Full Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Vythiri Resort Wayanad', 'Wayanad', '03 Nights', 'Deluxe', 'Serene Vythiri Haven Villa', 'MAP (Breakfast + Dinner)', 4, 1),
            _hotel('Pepper Trail Heritage Plantation Resort', 'Wayanad', '03 Nights', 'Premium', 'Luxury Treehouse Suite', 'MAP (Breakfast + Dinner)', 4, 2),
            _hotel('Evolve Back, Kabini / Wayanad Outskirts', 'Wayanad', '03 Nights', 'Luxury', 'Safari Land Hut with Private Pool', 'MAP (Breakfast + Dinner)', 5, 3),
            _hotel('The Windflower Resorts & Spa Wayanad', 'Wayanad', '03 Nights', 'Ultra Luxury', 'Ultra Luxury Private Villa with Private Plunge Pool', 'Ultra Luxury MAP', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights premium stays at handpicked luxury hotels and jungle resorts.', 1),
            _inc_included('Meals: High-end gourmet Breakfasts and Dinners curated by regional executive chefs.', 2),
            _inc_included('Transfers & Sightseeing: Entire journey covered via private luxury AC Innova Crysta/SUV with professional chauffeur.', 3),
            _inc_included('Assistance & Support: 24/7 dedicated TRAGUIN support helpline and verified route assistance.', 4),
            _inc_included('Welcome Amenities: Refreshing wellness kit on arrival including premium tribal organic honey, wet wipes, and natural juices.', 5),
            _inc_included('Complimentary Experiences: Private speed-boat safari at Banasura Sagar Dam and guided plantation walks.', 6),
            _inc_excluded('Flights, train bookings, or entry flight taxes into Cochin/Calicut.', 7),
            _inc_excluded('Any personal monument entrance fees, camera permissions, or historic guild tickets.', 8),
            _inc_excluded('Personal spending accounts like laundry services, special minibar usage, and telephone fees.', 9),
            _inc_excluded('Optional tours, customized safari trails, or activities not listed in the itinerary.', 10),
        ],
    )
    return package, itinerary

def build_kl_020(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-020'
    tour_code = 'TRAGUIN-KL-020'
    title = 'Kovalam Beach Poovar Island Luxury'
    duration = '04 Nights / 05 Days'
    slug = 'kl-020-kovalam-beach-poovar-island-luxury'
    itin_slug = 'kl-020-kovalam-beach-poovar-island-luxury-itinerary'
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
            _ph('State / Country: Kerala, India | Category: Beach & Backwater Island Luxury', 2),
            _ph('Destinations: Trivandrum • Kovalam Beach • Poovar Island', 3),
            _ph('Ideal for: Luxury Honeymooners, Families & Couples', 4),
            _ph('Best season: September to April', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Coastal Island FIT Escape', 7),
            _ph('Vehicle: Private Chauffeur-Driven Luxury Sedan / SUV (AC Innova Crysta)', 8),
            _ph('Meal Plan: Modified American Plan (Gourmet Daily Breakfast & Dinners Included)', 9),
            _ph('Route Map: Trivandrum Arrival → Kovalam Beach Cliffs → Poovar Estuary Island → Trivandrum Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated meticulously by TRAGUIN experts with automated early check-ins, VIP luxury transportation, and hand-selected local experiences.', 11),
            _ph('Shopping: Cardamom, pepper, beach garments, and seashell jewelry from Kovalam; Kerala Kasavu sarees and white dhotis from Trivandrum handlooms', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; pack lightweight linen and sunscreen; book Poovar floating cottages 45–60 days ahead', 13),
        ],
        moods=['Beach', 'Luxury', 'Romance'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kovalam Beach Poovar Island Luxury • 04 Nights / 05 Days',
        overview=(
            'Immerse yourself into an elite tropical dreamscape where golden shores melt into endless azure horizons. Designed flawlessly by TRAGUIN, this premium itinerary features a stunning harmony of legendary seaside cliffs and isolated floating backwater sanctuaries. Experience curated luxury hospitality crafted precisely for sophisticated travelers seeking breathtaking landscapes, premium stays, and unforgettable memories.\n\nKerala’s southern coastline represents the pinnacle of luxury beach getaways in India. If you are searching for the Best Kerala Tour Package, a magical Kerala Honeymoon Package, or a refreshing Kerala Family Tour, this destination offers unparalleled scenic beauty. The iconic attractions of Kovalam feature the famous crescent-shaped beaches separated by rocky headlands, while the pristine estuary of Poovar Island remains a unique paradise where a river, sea, and backwaters meet. Our Luxury Kerala Holiday showcases premium handpicked resorts, golden-sand beaches, and exclusive coastal photography points. With premium TRAGUIN Kerala Packages, dive into authentic local culture, top tourist places, and immersive wellness experiences.\n\nTRAGUIN Curated Touch: Curated meticulously by TRAGUIN experts with automated early check-ins, VIP luxury transportation, and hand-selected local experiences.'
        ),
        seo_title='KL-020 | Kovalam Beach Poovar Island Luxury | TRAGUIN',
        seo_description='Premium 04 Nights / 05 Days Kerala package (KL-020 / TRAGUIN-KL-020): Trivandrum • Kovalam Beach • Poovar Island. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Kovalam Lighthouse Beach, Samudra Beach & Marine Aquarium', 1),
            _ih('Poovar Island mangrove boat transfer and catamaran cruise', 2),
            _ih('Ayurvedic rejuvenation massage and beach leisure', 3),
            _ih('Padmanabhaswamy Temple and Kuthira Malika Palace', 4),
            _ih('TRAGUIN private sunset catamaran and wellness sessions', 5),
        ],
        days=[
            _day(
                1,
                'TRIVANDRUM TO KOVALAM',
                (
                    'Arrive at Trivandrum International Airport or railway station, where your private luxury chauffeur awaits you with a personalized warm greeting. Transfer comfortably to your premium handpicked beach resort in Kovalam. Enjoy a smooth, expedited check-in and unwind in your sea-facing luxury room. In the late afternoon, venture down to the golden sands of Lighthouse Beach. Take a leisurely walk along the shoreline, witnessing the iconic red-and-white striped lighthouse towering over the rocky cliffs as the sun dips below the Arabian Sea.'
                ),
                [
                    'Sightseeing Included: Lighthouse Beach, Hawa Beach, Kovalam Sightseeing.',
                    'Evening Experience: Sip on fresh, chilled organic coconut water while watching a dramatic coastal sunset.',
                    'Overnight Stay: Handpicked Luxury Beach Resort, Kovalam.',
                    'Meals Included: Welcome Amenity & Gourmet Buffet Dinner.',
                ],
            ),
            _day(
                2,
                'KOVALAM BEACH',
                (
                    'Awake to the soothing rhythm of ocean waves and enjoy a luxurious breakfast. Today is dedicated to exploring the scenic beauty and historical marvels around Kovalam. Visit the serene Samudra Beach and the magnificent Vizhinjam Marine Aquarium. In the afternoon, return to your resort to experience an authentic, handpicked Ayurvedic full-body rejuvenation massage, curated by certified wellness masters. Conclude your day with a tranquil beachside evening.'
                ),
                [
                    'Sightseeing Included: Samudra Beach, Vizhinjam Rock Cut Cave Temple, Marine Aquarium.',
                    'Optional Activities: A personalized yoga or meditation session overlooking the sea cliffs.',
                    'Overnight Stay: Handpicked Luxury Beach Resort, Kovalam.',
                    'Meals Included: Full Buffet Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'KOVALAM TO POOVAR ISLAND',
                (
                    'Following a delightful breakfast, check out from Kovalam and drive towards the pristine mangrove sanctuaries of Poovar Island. Upon reaching the boarding jetty, embark on an exclusive private motorized boat transfer navigating through thick, emerald mangrove forests. Arrive at your ultra-luxury island resort where your premium cottage floats over tranquil waters. In the late afternoon, enjoy an exclusive private catamaran cruise to the golden sandbar where the Neyyar River gracefully merges into the sea.'
                ),
                [
                    'Sightseeing Included: Mangrove Forest Canals, Poovar Beach Sandbar, Estuary Cruise.',
                    'Photography Points: The stunning junction where river waters meet the ocean at sunset.',
                    'Overnight Stay: Luxury Floating or Land-Based Premium Cottage, Poovar Island.',
                    'Meals Included: Full Breakfast & Candlelit Dinner.',
                ],
            ),
            _day(
                4,
                'POOVAR ISLAND LEISURE',
                (
                    'Savor a luxurious morning breakfast on your private deck. Spend the day indulging in the curated experiences of this untouched paradise. You can opt for a guided bird-watching boat trip through the deep inner backwater lakes, or simply relax by the infinity pool of your luxury resort. Witness the fascinating local fishing culture and peaceful rural life that lines the pristine river banks.'
                ),
                [
                    'Sightseeing Included: Backwater villages, floating churches and local bird sanctuaries.',
                    'Food Suggestions: Try local Malabar-style grilled seafood at a specialty floating restaurant.',
                    'Overnight Stay: Luxury Floating or Land-Based Premium Cottage, Poovar Island.',
                    'Meals Included: Full Breakfast & Festive Farewell Dinner.',
                ],
            ),
            _day(
                5,
                'POOVAR TO TRIVANDRUM DEPARTURE',
                (
                    'Enjoy your final breakfast surrounded by calm backwaters. Check out of the resort via a private boat transfer and drive to Trivandrum for a brief city heritage tour. Visit the awe-inspiring Sree Padmanabhaswamy Temple (known as the richest temple in the world) and admire the royal architecture of Kuthira Malika Palace. Later, your private vehicle will drop you off smoothly at Trivandrum International Airport for your flight home, concluding your premium TRAGUIN Kerala Package with unforgettable memories.'
                ),
                [
                    'Sightseeing Included: Padmanabhaswamy Temple exterior, Kuthira Malika Palace, Airport Transfer.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Soma Palmshore Beach Resort', 'Kovalam', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAP (Breakfast + Dinner)', 4, 1),
            _hotel('Poovar Island Resort (Land Cottage)', 'Poovar Island', '02 Nights', 'Deluxe', 'Land Cottage', 'MAP (Breakfast + Dinner)', 4, 2),
            _hotel('Turtle on the Beach', 'Kovalam', '02 Nights', 'Premium', 'Premium Room', 'MAP (Breakfast + Dinner)', 4, 3),
            _hotel('Over the Hill Resort / Poovar Premium', 'Poovar Island', '02 Nights', 'Premium', 'Premium Cottage', 'MAP (Breakfast + Dinner)', 4, 4),
            _hotel('Gokulam Grand Turtle on the Beach', 'Kovalam', '02 Nights', 'Luxury', 'Luxury Room', 'MAP (Breakfast + Dinner)', 5, 5),
            _hotel('Estuary Sarovar Portico (Estuary Premium)', 'Poovar Island', '02 Nights', 'Luxury', 'Estuary Premium Cottage', 'MAP (Breakfast + Dinner)', 5, 6),
            _hotel('The Leela Kovalam, a Raviz Hotel (Garden View)', 'Kovalam', '02 Nights', 'Ultra Luxury', 'Garden View Suite', 'MAP (Gourmet Dining)', 5, 7),
            _hotel('Poovar Island Resort (Floating AC Cottage)', 'Poovar Island', '02 Nights', 'Ultra Luxury', 'Floating AC Cottage', 'MAP (Gourmet Dining)', 5, 8),
        ],
        inclusions=[
            _inc_included('Accommodation: 02 Nights in Kovalam and 02 Nights in Poovar Island at ultra-luxury handpicked properties.', 1),
            _inc_included('Meals: 04 Premium Buffet Breakfasts and 04 Gourmet Dinners at resort fine-dining restaurants.', 2),
            _inc_included('Transfers & Sightseeing: Fully dedicated luxury air-conditioned Innova Crysta for all airport transfers and destination drives.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated professional travel concierge assistance throughout the trip.', 4),
            _inc_included('Complimentary Experiences: Private motorized boat cruises in the Poovar Estuary and mangrove forest networks.', 5),
            _inc_included('Welcome Amenities: Refreshing non-alcoholic tropical mocktails upon arrival and special personalized travel amenity kits.', 6),
            _inc_excluded('Domestic or international airfare, train tickets, and airport taxes.', 7),
            _inc_excluded('Monument entry keys, camera permissions, or local temple offering charges.', 8),
            _inc_excluded('Personal expenses such as telephone calls, laundry, minibar orders, or crew tips.', 9),
            _inc_excluded('Optional water sports (scuba diving, speed boating) and extra vehicle usage.', 10),
            _inc_excluded('Mandatory travel insurance policies.', 11),
        ],
    )
    return package, itinerary

def build_kl_021(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-021'
    tour_code = 'TRAGUIN-KL-021'
    title = 'Ayurveda & Yoga Healing Tour Munnar Kumarakom Kovalam'
    duration = '07 Nights / 08 Days'
    slug = 'kl-021-ayurveda-yoga-healing-tour-munnar-kumarakom-kovalam'
    itin_slug = 'kl-021-ayurveda-yoga-healing-tour-munnar-kumarakom-kovalam-itinerary'
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
            _ph('State / Country: Kerala / India | Category: Wellness & Healing', 2),
            _ph('Destinations: Cochin • Munnar • Kumarakom • Kovalam', 3),
            _ph('Ideal for: Wellness Seekers, Couples & Families', 4),
            _ph('Best season: September to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Customized Luxury Wellness FIT Portfolio', 7),
            _ph('Vehicle: Private Executive Luxury Chauffeur Sedan / SUV', 8),
            _ph('Meal Plan: Wellness Full Board (Organic, Personalized Ayurvedic Spa Nutrition)', 9),
            _ph('Route Map: Cochin Arrival → Munnar Wellness Hills → Kumarakom Backwaters → Kovalam Beach → Trivandrum Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with priority wellness suite booking, direct access to premium medical supervisors, and post-trip wellness checkups.', 11),
            _ph('Shopping: Authentic therapeutic oils, organic spices, and wellness preparations; traditional Kasavu sarees and hand-carved coir souvenirs', 12),
            _ph('Important: Retreat check-in 14:00 hrs; minimize digital usage and alcohol during therapeutic stay; monsoon and winter phases ideal for Ayurvedic routines', 13),
        ],
        moods=['Wellness', 'Luxury', 'Nature'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Ayurveda & Yoga Healing Tour Munnar Kumarakom Kovalam • 07 Nights / 08 Days',
        overview=(
            'Step into a sanctuary of profound rejuvenation and pure equilibrium. This bespoke, luxury holistic healing sanctuary itinerary by TRAGUIN coordinates authentic Vedic therapies, soul-stirring yoga regimes, and deep organic nutrition frameworks across the iconic landscapes of Kerala. Luxury Wellness\n\nEXPERIENCE Recognized worldwide as the birthplace of traditional healing, Kerala is the perfect haven for a transformational Kerala Honeymoon Package or an enriching Kerala Family Tour. The unique synthesis of tropical humidity, therapeutic plant estates, and calming marine horizons transforms the region into an unmatched sanctuary for a Luxury Kerala Holiday. From the crisp air of the mist-laden hills of Munnar to the languid, calming channels of Kumarakom and the golden medical coastline of Kovalam, our premium customized routes balance immersive excursions with intentional space for physical rest. Enjoy top tourist places in Kerala while indulging in curated wellness sessions. This specialized Premium Kerala Experience guarantees a profound sensory alignment, delivering unforgettable memories.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts with priority wellness suite booking, direct access to premium medical supervisors, and post-trip wellness checkups.'
        ),
        seo_title='KL-021 | Ayurveda & Yoga Healing Tour Munnar Kumarakom Kovalam | TRAGUIN',
        seo_description='Premium 07 Nights / 08 Days Kerala package (KL-021 / TRAGUIN-KL-021): Cochin • Munnar • Kumarakom • Kovalam. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Munnar sunrise yoga and curated tea plantation trail', 1),
            _ih('Kumarakom Ayurvedic pulse diagnosis and Abhyanga therapy', 2),
            _ih('Kovalam Shirodhara and Elakizhi herbal poultice massage', 3),
            _ih('Private sound healing workshop and wellness consultation', 4),
            _ih('TRAGUIN wellness full-board organic Ayurvedic cuisine', 5),
        ],
        days=[
            _day(
                1,
                'ARRIVAL IN COCHIN TO MUNNAR',
                (
                    'Arrive at Cochin International Airport where your elite TRAGUIN chauffeur welcomes you warmly. Board your private luxury transport and embark on a scenic route scaling the emerald slopes towards Munnar. Pause gracefully to enjoy the crisp mist of Valara and Cheeyappara waterfalls. Check in seamlessly to your premium mountain sanctuary and meet with an onsite wellness expert for your preliminary wellness briefing.'
                ),
                [
                    'Sightseeing Included: Cheeyappara & Valara Falls, Tea Estate Horizons.',
                    'Evening Experience: A soothing herbal welcome dynamic over an organic sunset tea.',
                    'Overnight Stay: Handpicked Luxury Wellness Resort, Munnar.',
                    'Meals Included: Detox Dinner.',
                ],
            ),
            _day(
                2,
                'MUNNAR HILLS SIGHTSEEING',
                (
                    'Awake to a peaceful sunrise yoga session overlooking mist-covered valleys. Following a tailored holistic breakfast, take a gentle, slow-paced walk through premium spice plantations and quiet walking tracks. Visit the serene Mattupetty Lake and Echo Point to absorb the tranquil acoustic properties of nature, perfect for calming the nervous system.'
                ),
                [
                    'Sightseeing Included: Mattupetty Reservoir, Echo Point, Curated Tea Plantation Trail.',
                    'Photography Points: Panorama peaks overlooking expansive tea estates.',
                    'Overnight Stay: Handpicked Luxury Wellness Resort, Munnar.',
                    'Meals Included: Organic Breakfast, Lunch & Ayurvedic Dinner.',
                ],
            ),
            _day(
                3,
                'MUNNAR TO KUMARAKOM BACKWATERS',
                (
                    'Descend from the hills to the languid lake country of Kumarakom. Check into an award-winning ultra- luxury waterfront sanctuary. In the afternoon, undergo an intensive pulse diagnosis and personal consultation with a veteran Ayurvedic physician to outline your customized dosha-balancing therapy program.'
                ),
                [
                    'Sightseeing Included: Bird Sanctuary Borders, Private Lake Cruise.',
                    'Evening Experience: Relaxing private backwater cruise at twilight.',
                    'Overnight Stay: Premium Heritage Backwater Resort, Kumarakom.',
                    'Meals Included: Breakfast, Lunch & Curated Dinner.',
                ],
            ),
            _day(
                4,
                'KUMARAKOM HOLISTIC AYURVEDA',
                (
                    'Your healing day begins with morning meditation and pranayama exercises. Experience an authentic full-body Abhyanga massage administered by synchronized therapists using hand-infused organic medicated oils. Spend the afternoon reading, walking among lily ponds, or resting in absolute privacy.'
                ),
                [
                    'Local Experiences: Hands-on traditional pottery or customized weaving observation.',
                    'Therapy Included: 60-Minute Authentic Abhyanga Rejuvenation Therapy.',
                    'Overnight Stay: Premium Heritage Backwater Resort, Kumarakom.',
                    'Meals Included: Balanced Ayurvedic Full Board.',
                ],
            ),
            _day(
                5,
                'KUMARAKOM TO KOVALAM BEACH',
                (
                    'Drive south along the coastal highways toward the golden clifftops of Kovalam. Check in to an elite wellness estate hanging over the Arabian Sea. Conclude the afternoon with an immersive Shirodhara therapy, where warm, continuously streaming herbal oils are gently applied across the forehead to induce profound mental peace and alleviate neurological tension.'
                ),
                [
                    'Sightseeing Included: Kovalam Coastal Bluffs, Marine Horizon Promenade.',
                    'Therapy Included: Authentic Stress-Relief Shirodhara Session.',
                    'Overnight Stay: Ultra-Luxury Cliff Ocean Resort, Kovalam.',
                    'Meals Included: Healthy Full Board.',
                ],
            ),
            _day(
                6,
                'KOVALAM YOGA & IMMERSION',
                (
                    'Participate in an open-air Hatha Yoga assembly on the ocean-facing platform. After a refreshing green juice and breakfast, enjoy a brief, curated excursion to local historical landmarks. Return for a localized herbal poultice treatment (Elakizhi) to dissolve body weariness and improve circulation.'
                ),
                [
                    'Sightseeing Included: Vizhinjam Rock Cut Cave, Golden Beach shores.',
                    'Therapy Included: Elakizhi (Herbal Poultice Massage).',
                    'Overnight Stay: Ultra-Luxury Cliff Ocean Resort, Kovalam.',
                    'Meals Included: Healthy Full Board.',
                ],
            ),
            _day(
                7,
                'KOVALAM SOUND EXPERIENCES',
                (
                    'Savor a luxurious wellness schedule. Today includes an advanced sound healing workshop alongside your closing consultation with the Ayurvedic medical faculty. Receive a tailored ongoing lifestyle map to safely maintain your newfound vitality and body equilibrium at home.'
                ),
                [
                    'Sightseeing Included: Leisure beach walking routes, shopping for premium wellness oils.',
                    'Special Experience: Private Sound Healing and meditative vibrational therapy.',
                    'Overnight Stay: Ultra-Luxury Cliff Ocean Resort, Kovalam.',
                    'Meals Included: Festive Organic Farewell Dinner.',
                ],
            ),
            _day(
                8,
                'KOVALAM TO TRIVANDRUM DEPARTURE',
                (
                    'Conclude your transformational travel program with a light morning meditation. Transfer elegantly with your private chauffeur to Trivandrum International Airport for your onward flight. Your signature TRAGUIN Kerala Package concludes, leaving you with renewed physical health and beautiful, timeless memories.'
                ),
                [
                    'Transfers Included: Private Executive Airport Drop-off.',
                    'Meals Included: Alkaline Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Ambady Estate', 'Munnar', '02 Nights', 'Deluxe', 'Executive Room', 'Wellness Full Board', 4, 1),
            _hotel('Coconut Lagoon', 'Kumarakom', '02 Nights', 'Deluxe', 'Heritage Bungalow', 'Wellness Full Board', 4, 2),
            _hotel('Travancore Heritage', 'Kovalam', '03 Nights', 'Deluxe', 'Heritage Room', 'Wellness Full Board', 4, 3),
            _hotel('Blanket Hotel & Spa', 'Munnar', '02 Nights', 'Premium', 'Premium Room', 'Wellness Full Board', 4, 4),
            _hotel('Kumarakom Lake Resort', 'Kumarakom', '02 Nights', 'Premium', 'Lake View Room', 'Wellness Full Board', 4, 5),
            _hotel('Niraamaya Retreats Surya Samudra', 'Kovalam', '03 Nights', 'Premium', 'Premium Room', 'Wellness Full Board', 4, 6),
            _hotel('The Panoramic Getaway', 'Munnar', '02 Nights', 'Luxury', 'Luxury Suite', 'Wellness Full Board', 5, 7),
            _hotel('The Zuri Kumarakom', 'Kumarakom', '02 Nights', 'Luxury', 'Lagoon View Room', 'Wellness Full Board', 5, 8),
            _hotel('The Leela Kovalam, A Raviz Hotel', 'Kovalam', '03 Nights', 'Luxury', 'Club Room', 'Wellness Full Board', 5, 9),
            _hotel("Chandy's Windy Woods (Suite)", 'Munnar', '02 Nights', 'Ultra Luxury', 'Suite', 'Wellness Full Board', 5, 10),
            _hotel('Carnoustie Ayurveda Resort', 'Kumarakom', '02 Nights', 'Ultra Luxury', 'Ayurveda Villa', 'Wellness Full Board', 5, 11),
            _hotel('Somatheeram Ayurveda Resort', 'Kovalam', '03 Nights', 'Ultra Luxury', 'Ayurveda Suite', 'Wellness Full Board', 5, 12),
        ],
        inclusions=[
            _inc_included('Accommodation: 07 Nights stay at handpicked premium luxury hotels and wellness retreats.', 1),
            _inc_included('Meals: Customized full-board organic Ayurvedic cuisine curated specifically to your metabolic profile.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven air-conditioned private luxury vehicle.', 3),
            _inc_included('TRAGUIN Support: 24/7 global priority concierge and professional travel assistance.', 4),
            _inc_included('Complimentary Experiences: Private wellness consultation, sunset cruise, and specialized sound healing workshop.', 5),
            _inc_included('Welcome Amenities: Personalized rejuvenation check-in hamper including herbal infusions and premium copper vessels.', 6),
            _inc_excluded('Airfare or intermediate rail tickets to Kerala.', 7),
            _inc_excluded('Entry permissions for monuments and camera fees outside the schedule.', 8),
            _inc_excluded('Private telephone expenses, laundry services, and tips.', 9),
            _inc_excluded('Ancillary medicines or therapeutic extra-sessions requested individually.', 10),
            _inc_excluded('Individual traveler comprehensive health insurance.', 11),
        ],
    )
    return package, itinerary

def build_kl_022(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-022'
    tour_code = 'TRAGUIN-KL-022'
    title = 'Vagamon Pine Valleys & Bekal Coastal Trail'
    duration = '05 Nights / 06 Days'
    slug = 'kl-022-vagamon-pine-valleys-bekal-coastal-trail'
    itin_slug = 'kl-022-vagamon-pine-valleys-bekal-coastal-trail-itinerary'
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
            _ph('State / Country: Kerala / India | Category: Offbeat / Experiential Luxury', 2),
            _ph('Destinations: Vagamon Pine Hills • Bekal Coastal Trail', 3),
            _ph('Ideal for: Luxury Explorers & Families', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Offbeat Experiential FIT Tour', 7),
            _ph('Vehicle: Private Chauffeur-driven Luxury SUV (Innova Crysta) throughout the journey', 8),
            _ph('Meal Plan: Modified American Plan (Gourmet Breakfasts & Specialty Dinners)', 9),
            _ph('Route Map: Cochin Arrival → Vagamon Hills → Calicut → Bekal Coastal Trail → Mangalore / Cochin Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts for authentic slow-paced exploration with private entry arrangements, premium local escorts, and customized culinary trails.', 11),
            _ph('Shopping: Banana chips, coconut oil, and Kozhikodan sweet halwas from Calicut; bamboo crafts, hand-woven cotton textiles, and organic spice assortments', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; light layer for Vagamon hills; reserve 4–6 weeks ahead for premium ocean or valley view rooms', 13),
        ],
        moods=['Adventure', 'Nature', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Vagamon Pine Valleys & Bekal Coastal Trail • 05 Nights / 06 Days',
        overview=(
            "Vagamon Pine Hills Bekal Coastal Trail IDEAL FOR: Luxury Explorers & Families BEST SEASON: September to May TRAGUIN TOUR CODE: TRAGUIN-KL-022 BEST KERALA TOUR PACKAGE - EXPERIENTIAL LUXURY VAGAMON PINE VALLEYS & BEKAL COASTAL TRAIL 05 NIGHTS / 06 DAYS Step far away from the predictable paths and enter a mesmerizing world of mist-shrouded green meadows, dramatic seaside cliffs, and historical fortresses. Carefully designed by TRAGUIN, this signature itinerary unlocks the raw, untouched magic of God's Own Country. From the crisp\n\nFor anyone looking for an unmatched Kerala Honeymoon Package or an unforgettable Kerala Family Tour, exploring the hidden treasures of Vagamon and Bekal offers a refreshing escape from mainstream crowded hotspots. This itinerary combines the stunning green hillsides of South Kerala with the majestic, uncrowded fort beaches of the North, ensuring a truly Premium Kerala Experience. From capturing pictures at famous Instagram spots like the Vagamon Pine Forest to walking on the grand ramparts of Bekal Fort overlooking the Arabian Sea, our Luxury Kerala Holiday focuses on slow, meaningful journeys. With TRAGUIN Kerala Packages, you get complete comfort, rare culinary trails, and exclusive privacy.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts for authentic slow-paced exploration with private entry arrangements, premium local escorts, and customized culinary trails."
        ),
        seo_title='KL-022 | Vagamon Pine Valleys & Bekal Coastal Trail | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kerala package (KL-022 / TRAGUIN-KL-022): Vagamon Pine Hills • Bekal Coastal Trail. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Vagamon Pine Forest, Meadows and Suicide Point', 1),
            _ih('Calicut Beach and authentic Malabar cuisine trail', 2),
            _ih('Bekal Fort sunset tour and Valiyaparamba backwater cruise', 3),
            _ih('Kappil Beach where backwaters meet the sea', 4),
            _ih('TRAGUIN offbeat slow-paced exploration with private escorts', 5),
        ],
        days=[
            _day(
                2,
                'VAGAMON EXPLORATION',
                (
                    'Wake up to the refreshing mountain breeze. Today you will explore the iconic attractions of Vagamon. Walk through the quiet rows of the towering Vagamon Pine Forest, a perfect photography point. Afterward, visit the rolling green Vagamon Meadows, where endless velvet hills spread out beneath the blue sky. Finish your afternoon with a peaceful visit to Kurisumala Ashram or the Kurisumala hill trails for panoramic views.'
                ),
                [
                    'Sightseeing Included: Vagamon Pine Forest, Vagamon Meadows, Suicide Point, Lake Walk.',
                    'Optional Activities: Gentle off-road jeep safari to the spectacular hidden waterfalls of Vagamon.',
                    'Overnight Stay: Premium Hill Resort, Vagamon.',
                    'Meals Included: Full Breakfast & Dinner.',
                ],
            ),
            _day(
                3,
                'VAGAMON TO COSTA TRAIL (CALICUT PAUSE)',
                (
                    'After a wonderful breakfast, descend the green hills and head north along the scenic coastal route towards the historical spice port of Calicut (Kozhikode). Check into a premium seaside property. Spend the late afternoon walking along Calicut Beach and tasting the famous Malabar cuisine, including authentic Kozhikodan Halwa and rich local seafood recipes.'
                ),
                [
                    'Sightseeing Included: Calicut Beach, historical street walks, local handicraft markets.',
                    'Food Suggestions: Enjoy a luxury lunch serving authentic Malabar Biryani at a premium coastal restaurant.',
                    'Overnight Stay: Luxury Beachside Hotel, Calicut.',
                    'Meals Included: Breakfast & Specialized Coastal Dinner.',
                ],
            ),
            _day(
                4,
                'CALICUT TO BEKAL',
                (
                    "Drive further north along the beautiful coastal highway to reach Bekal, home to one of Kerala's best-kept secrets. Check into an ultra-luxury villa resort. In the late afternoon, enjoy an exclusive private tour of the majestic Bekal Fort. This key-hole shaped fortress extends right into the Arabian Sea, offering breathtaking landscapes and wonderful ocean views as waves crash against its ancient stone walls."
                ),
                [
                    'Sightseeing Included: Bekal Fort Exploration, Bekal Fort Beach Walk.',
                    'Photography Points: The top observation towers of Bekal Fort during a dramatic ocean sunset.',
                    'Overnight Stay: Premium Ultra-Luxury Beach Resort, Bekal.',
                    'Meals Included: Breakfast & Gourmet Dinner.',
                ],
            ),
            _day(
                5,
                'BEKAL COASTAL TRAIL & BACKWATERS',
                (
                    'Today features an incredible, uncrowded backwater cruise. Travel a short distance to Valiyaparamba, a peaceful coastal backwater stretch away from mainstream tourism. Board a private luxury country boat or houseboat to glide through calm waters lined with coconut groves. Spend your evening relaxing on the pristine sands of Kappil Beach, where the backwaters meet the sea.'
                ),
                [
                    'Sightseeing Included: Valiyaparamba Private Boat Cruise, Kappil Beach.',
                    "Immersive Experiences: Traditional interactive cooking demonstration with the resort's master chef.",
                    'Overnight Stay: Premium Ultra-Luxury Beach Resort, Bekal.',
                    'Meals Included: Breakfast & Farewell Festive Dinner.',
                ],
            ),
            _day(
                6,
                'BEKAL TO DEPARTURE',
                (
                    'Enjoy a relaxed breakfast at your luxury resort while listening to the sound of the ocean waves. After check-out, your private vehicle will transport you comfortably to Mangalore International Airport (the closest airport) or back to Cochin for your return flight home. Your premium holiday concludes with beautiful, long-lasting memories.'
                ),
                [
                    'Transfers Included: Private Luxury Airport Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Winter Vale Green Stay Resort', 'Vagamon', '02 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 1),
            _hotel('Malabar Ocean Resort & Spa', 'Bekal', '02 Nights', 'Deluxe', 'Deluxe Room', 'Breakfast & Dinner', 4, 2),
            _hotel('Vagamon Hide Out & Heritage Resort', 'Vagamon', '02 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 3),
            _hotel('The Gateway Hotel Bekal (Taj)', 'Bekal', '02 Nights', 'Premium', 'Premium Room', 'Breakfast & Dinner', 4, 4),
            _hotel('The Fog Resort & Spa Vagamon', 'Vagamon', '02 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 5),
            _hotel('Taj Bekal Resort & Spa, Kerala', 'Bekal', '02 Nights', 'Luxury', 'Luxury Room', 'Breakfast & Dinner', 5, 6),
            _hotel('Elixir Hills Premium Suites', 'Vagamon', '02 Nights', 'Ultra Luxury', 'Premium Suite', 'Breakfast & Dinner', 5, 7),
            _hotel('The Lalit Resort & Spa Bekal', 'Bekal', '02 Nights', 'Ultra Luxury', 'Luxury Suite', 'Breakfast & Dinner', 5, 8),
        ],
        inclusions=[
            _inc_included('Accommodation: Luxury stays at handpicked premium resorts and private beach villas.', 1),
            _inc_included('Meals: 05 Buffet Breakfasts and 05 curated specialty dinners at hotel properties.', 2),
            _inc_included('Transfers & Sightseeing: All journeys in a private Chauffeur-driven air-conditioned Luxury Innova Crysta.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated telephone concierge assistance during the trip.', 4),
            _inc_included('Complimentary Experiences: Private chartered country boat ride across Valiyaparamba backwaters.', 5),
            _inc_included('Welcome Amenities: Personalized travel kit containing traditional handloom towels and organic spice samples.', 6),
            _inc_excluded('Airfare or interstate train tickets to Kerala.', 7),
            _inc_excluded('Entrance tickets to monuments, forts, or camera charges. ✘ Personal expenses such as premium drinks, laundry, tips, and room services.', 8),
            _inc_excluded('Optional off-road jeep safaris or water sports activities.', 9),
        ],
    )
    return package, itinerary

def build_kl_023(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-023'
    tour_code = 'TRAGUIN-KL-023'
    title = 'Periyar Wildlife Sanctuary & Spice Plantation Experience'
    duration = '03 Nights / 04 Days'
    slug = 'kl-023-periyar-wildlife-sanctuary-spice-plantation-experience'
    itin_slug = 'kl-023-periyar-wildlife-sanctuary-spice-plantation-experience-itinerary'
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
            _ph('State / Country: Kerala / India | Category: Nature / Wildlife / Wellness', 2),
            _ph('Destinations: Cochin • Thekkady (Periyar)', 3),
            _ph('Ideal for: Nature Lovers, Couples, Families', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Wildlife & Spice FIT Tour', 7),
            _ph('Vehicle: Dedicated Luxury Chauffeur-Driven Air-Conditioned Sedan/SUV', 8),
            _ph('Meal Plan: Modified American Plan (CP/MAP - Premium Breakfast & Dinners Included)', 9),
            _ph('Route Map: Cochin Airport Arrival → Thekkady Forest Highlands → Cochin Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts with handpicked eco-resorts, luxury transportation, and exclusive recommendations for local dining and sightseeing.', 11),
            _ph('Shopping: Green cardamom, organic black pepper, cinnamon, saffron, and vanilla from Kumily Spice Market; rosewood elephant figurines and aromatherapy oils', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; secure early Periyar Lake boat safari booking; light jacket or umbrella advised for highland showers', 13),
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
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Periyar Wildlife Sanctuary & Spice Plantation Experience • 03 Nights / 04 Days',
        overview=(
            "Step into the deep emerald heart of God's Own Country. This luxury nature vacation, meticulously crafted by TRAGUIN, invites you to unravel the secrets of the rainforests, misty spice highlands, and rare wildlife preserves of Thekkady. Designed for discerning travelers seeking an elegant balance of immersive experiences, wildlife exploration, and raw scenic beauty. JOURNEY TO THE SPICE HIGHLANDS TOUR OVERVIEW\n\nThekkady, home to the iconic Periyar Wildlife Sanctuary, represents one of the most sought-after wilderness corridors for a Luxury Kerala Holiday. Ideal for a rejuvenating Kerala Family Tour or a romantic Kerala Honeymoon Package, it presents a landscape covered in dense spice hills, wild herds of elephants, and aromatic spice estates. When shortlisting the Top Tourist Places in Kerala, the mist-cloaked highlands of Periyar rank supreme. Visitors can participate in highly searched premium experiences like organic spice trekking, looking over scenic viewpoints, capturing popular Instagram locations inside the mist, and enjoying local cultural highlights. Choosing TRAGUIN Kerala Packages ensures that every detail of your journey is flawlessly managed with premier comfort.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts with handpicked eco-resorts, luxury transportation, and exclusive recommendations for local dining and sightseeing."
        ),
        seo_title='KL-023 | Periyar Wildlife Sanctuary & Spice Plantation Experience | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Kerala package (KL-023 / TRAGUIN-KL-023): Cochin • Thekkady (Periyar). Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Periyar Lake boat safari and wildlife sanctuary trail', 1),
            _ih('Kalaripayattu and Kathakali cultural performances', 2),
            _ih('Private guided spice plantation walk and heritage bazaars', 3),
            _ih('Traditional banana-leaf lunch at premium plantation house', 4),
            _ih('TRAGUIN eco-resort stays with 24/7 concierge', 5),
        ],
        days=[
            _day(
                1,
                'COCHIN TO THEKKADY',
                (
                    'Arrive at Cochin International Airport where your dedicated TRAGUIN chauffeur welcomes you warmly. Board your premium vehicle and begin a highly scenic ascent toward the spice capital of Kerala— Thekkady. The route treats you to breathtaking landscapes, cascading waterfalls, and rows of pristine rubber and tea estates. Upon arriving in Thekkady, check into your ultra-luxury eco-resort nestled seamlessly amidst nature. Spend a relaxed evening listening to the ambient sounds of the jungle canopy.'
                ),
                [
                    'Sightseeing Included: Scenic Mountain Drive, Periyar Hilltop Views.',
                    'Evening Experience: A warm, curated welcome presentation over premium organic high-tea by local',
                    'Overnight Stay: Handpicked Luxury Resort, Thekkady.',
                    'Meals Included: Welcome Amenity & Gourmet Dinner.',
                ],
            ),
            _day(
                2,
                'PERIYAR WILDLIFE EXCURSION',
                (
                    "Wake up to a crisp, mist-kissed morning and head early for an exclusive cruise on the calm waters of Periyar Lake. Keep your cameras ready at prime photography points to capture wild elephants, Nilgiri langurs, sambar deer, and a rich variety of exotic waterbirds along the shoreline. After a delicious buffet breakfast back at your resort, spend your afternoon discovering the true roots of Kerala's heritage with an immersive live demonstration of Kalaripayattu (the world's oldest martial art) and a soulful Kathakali performance."
                ),
                [
                    'Sightseeing Included: Periyar Lake Boat Safari, Periyar Wildlife Sanctuary Trail, Culture Center.',
                    'Optional Activities: Guided nature walk with a forest naturalist or a premium Ayurvedic body rejuvenation',
                    'Overnight Stay: Handpicked Luxury Resort, Thekkady.',
                    'Meals Included: Full Breakfast & Curated Dinner.',
                ],
            ),
            _day(
                3,
                'PRIVATE SPICE PLANTATION WALK',
                (
                    'Today is dedicated to an absolute highlight of your Premium Kerala Experience. Embark on a private, curated walk through a lush, award-winning spice plantation. A specialized estate guide will show you how cardamoms, black pepper, vanilla, and cinnamon are grown, harvested, and cured. The afternoon is yours to stroll through local spice markets, perfect for picking up pure souvenirs, followed by an elegant culinary session showcasing traditional Kerala flavors.'
                ),
                [
                    'Sightseeing Included: Spice Plantation Tour, Local Heritage Spice Bazaars.',
                    'Food Suggestions: Enjoy a traditional lunch served gracefully on a fresh banana leaf at a premium plantation',
                    'Overnight Stay: Handpicked Luxury Resort, Thekkady.',
                    'Meals Included: Full Breakfast & Farewell Festive Dinner.',
                ],
            ),
            _day(
                4,
                'DEPARTURE FROM COCHIN',
                (
                    'Savor a luxurious morning breakfast overlooking the pool or misty forests. Say a fond goodbye to the serene wilderness of Periyar as your luxury vehicle transfers you comfortably back to Cochin International Airport for your departure flight. Your premium travel experience concludes with timeless memories of a beautifully managed holiday.'
                ),
                [
                    'Transfers Included: Private Airport Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Greenwoods Resort / Poetree Sarovar Portico', 'Thekkady', '03 Nights', 'Deluxe', 'Aranya Deluxe Room', 'MAP (Breakfast + Dinner)', 4, 1),
            _hotel('The Elephant Court / Cardamom County', 'Thekkady', '03 Nights', 'Premium', 'Patio Room / Suite', 'MAP (Breakfast + Dinner)', 4, 2),
            _hotel('Spice Village - CGH Earth', 'Thekkady', '03 Nights', 'Luxury', 'Spice Garden Cottage', 'MAPAI (Gourmet Meals)', 5, 3),
            _hotel('Niraamaya Retreats Cardamom Club', 'Thekkady', '03 Nights', 'Ultra Luxury', 'Luxury Private Garden Villa', 'Ultimate Full Board Elite Plan', 5, 4),
        ],
        inclusions=[
            _inc_included('Accommodation: 03 Nights accommodation at premium stays / handpicked hotels of your choice.', 1),
            _inc_included('Meals: 03 Premium Buffet Breakfasts and 03 curated gourmet Dinners at the resort.', 2),
            _inc_included('Transfers & Sightseeing: Whole tour via dedicated, fully sanitized air-conditioned luxury transportation.', 3),
            _inc_included('TRAGUIN Support: 24/7 dedicated customer assistance and certified holiday experts support.', 4),
            _inc_included('Complimentary Experiences: Private entry for a guided Spice Plantation Tour and welcome amenities kit upon arrival.', 5),
            _inc_included('Taxes: All applicable luxury resort service taxes and state permit fees. PACKAGE EXCLUSIONS', 6),
            _inc_excluded('Flights or interstate railway ticketing costs to Cochin.', 7),
            _inc_excluded('Entry tickets for activities like the Periyar Lake Boat Safari, elephant rides, or cultural shows.', 8),
            _inc_excluded('Personal expenses such as laundry services, phone calls, mini-bar orders, and driver gratuities.', 9),
            _inc_excluded('Any optional tours or extended detours not mentioned in the core itinerary.', 10),
            _inc_excluded('Travel insurance coverage.', 11),
        ],
    )
    return package, itinerary

def build_kl_024(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-024'
    tour_code = 'TRAGUIN-KL-024'
    title = 'Grand Malabar Heritage (Calicut)'
    duration = '05 Nights / 06 Days'
    slug = 'kl-024-grand-malabar-heritage-calicut'
    itin_slug = 'kl-024-grand-malabar-heritage-calicut-itinerary'
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
            _ph('State / Country: Kerala / India | Category: Culture & Heritage Luxury', 2),
            _ph('Destinations: Calicut (Kozhikode) • Wayanad • Beypore • Kappad', 3),
            _ph('Ideal for: Culture Seekers, Families & Connoisseurs', 4),
            _ph('Best season: September to March', 5),
            _ph('Starting price: On Request (Premium Class)', 6),
            _ph('Travel Format: Private Culture & Leisure FIT Tour', 7),
            _ph('Vehicle: Private Air-Conditioned Luxury Sedan / Premium SUV', 8),
            _ph('Meal Plan: Modified American Plan (Gourmet Breakfast & Specialized Dinners)', 9),
            _ph('Route Map: Calicut Arrival → Kappad → Beypore Heritage Village → Wayanad Hills → Calicut Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN Experts introducing elite travelers to untold histories of Northern Kerala with private luxury transportation and master craftsmen access.', 11),
            _ph('Shopping: Malabari Kozhikodan Halwa, banana chips, and premium spices from S.M. Street; miniature wooden Uru ships from Beypore master carpenters', 12),
            _ph('Important: Check-in 14:00 hrs, check-out 11:00 hrs; lightweight cotton for Calicut coast, soft jacket for Wayanad evenings; early confirmations recommended', 13),
        ],
        moods=['Culture', 'Heritage', 'Luxury'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Class)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Grand Malabar Heritage (Calicut) • 05 Nights / 06 Days',
        overview=(
            'Wayanad Beypore Kappad IDEAL FOR: Culture Seekers, Families & Connoisseurs BEST SEASON: September to March TRAGUIN TOUR CODE: TRAGUIN-KL-024 TRAGUIN PREMIUM KERALA TOUR PACKAGE GRAND MALABAR HERITAGE (CALICUT) 05 NIGHTS / 06 DAYS Step into the cradle of spice trading history, coastal grandeur, and timeless royalty. This exclusive Grand Malabar Heritage Tour curated by TRAGUIN uncovers the magnificent cultural depth of North Kerala. From the legendary ports of Calicut where ancient global explorers dropped anchor to the misty tribal hills of Wayanad, embark on an emotional journey of immersive experiences, handpicked hotels, and breathtaking landscapes designed to stay in your heart forever. TRAGUIN Exclusive Malabar\n\nNorthern Kerala presents a starkly different, pristine alternative to the traditional tourist circuits. When planning the Best Kerala Tour Package or a sophisticated Kerala Family Tour, the Grand Malabar Heritage region stands out for its raw, unfiltered historical charm. Kozhikode, historically known as Calicut, is highly searched as the culinary capital of South India, rich in architectural marvels and sensory stories. From exploring the iconic attractions of Forts and ancient shipyards to setting foot on Kappad Beach where Vasco da Gama arrived, this Luxury Kerala Holiday blends history with breathtaking landscapes. Famous attractions include the\n\nTRAGUIN Curated Touch: Curated by TRAGUIN Experts introducing elite travelers to untold histories of Northern Kerala with private luxury transportation and master craftsmen access.'
        ),
        seo_title='KL-024 | Grand Malabar Heritage (Calicut) | TRAGUIN',
        seo_description='Premium 05 Nights / 06 Days Kerala package (KL-024 / TRAGUIN-KL-024): Calicut (Kozhikode) • Wayanad • Beypore • Kappad. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Kappad Beach Vasco da Gama landing monument', 1),
            _ih('Beypore Uru shipyard and Sweet Meat Street halwa tasting', 2),
            _ih('Wayanad Edakkal Caves and Thamarassery Ghat drive', 3),
            _ih('Pookode Lake row-boat ride and organic spice farm', 4),
            _ih('Exclusive private Kalaripayattu performance in Calicut', 5),
        ],
        days=[
            _day(
                1,
                'CALICUT',
                (
                    "Arrive at Calicut International Airport where your elite TRAGUIN chauffeur welcomes you. Transfer in comfort to your premium heritage stay overlooking the Arabian Sea. After a seamless check-in and refreshing afternoon rest, proceed to the historic Kappad Beach. Stand at the historic spot marked by a stone monument where global maritime history transformed forever with Vasco da Gama's arrival in 1498. Walk along the beach walkway as the golden sun sets into the horizon."
                ),
                [
                    'Sightseeing Included: Kappad Beach Discovery, Calicut Beach Pier Walkway.',
                    'Evening Experience: A sunset high-tea briefing at a seaside lounge discussing the upcoming heritage details.',
                    'Overnight Stay: Handpicked Luxury Resort, Calicut.',
                    'Meals Included: Welcome Drink & Traditional Malabari Dinner.',
                ],
            ),
            _day(
                2,
                'BEYPORE & CALICUT',
                (
                    "After a premium breakfast, visit the historic port town of Beypore located at the mouth of the Chaliyar River. Beypore is world-famous for its ancient wooden shipbuilding yards where master artisans have designed massive seafaring vessels known as 'Urus' entirely by hand for over 1500 years. Witness these architectural marvels up close. Later, discover the rich alleys of Sweet Meat Street (Mithai Theruvu) to taste the famous Calicut Halwa and enjoy premium spice shopping at the bustling local bazaar."
                ),
                [
                    'Sightseeing Included: Beypore Uru Shipyard, Beypore Pulimuttu (Sea Bridge), Mithai Theruvu Shopping, Tali',
                    'Optional Activities: Sampling authentic Kozhikode Biryani at an iconic culinary heritage restaurant.',
                    'Photography Points: The towering skeletons of wooden ships at the shipyard and the unique 1-km long stone',
                    'Overnight Stay: Handpicked Luxury Resort, Calicut.',
                    'Meals Included: Breakfast & Specialized Regional Dinner.',
                ],
            ),
            _day(
                3,
                'CALICUT TO WAYANAD',
                (
                    'Today, your private luxury transport steers into the verdant mountains of Wayanad. Negotiate the famous Thamarassery Lakkidi Ghat pass featuring nine hairpin turns, with each curve revealing sweeping panoramas of lush valleys and breathtaking landscapes. Stop at the high-altitude Lakkidi Viewpoint for incredible photography. Upon arrival, check into a premium eco-luxury rainforest estate hotel tucked away inside rolling tea plantations.'
                ),
                [
                    'Sightseeing Included: Thamarassery Ghat Drive, Lakkidi Viewpoint, Pookode Lake.',
                    'Evening Experience: A peaceful private row-boat ride across the natural freshwater mirror of Pookode Lake,',
                    'Overnight Stay: Premium Handpicked Wilderness Resort, Wayanad.',
                    'Meals Included: Breakfast & Gourmet Estate Dinner.',
                ],
            ),
            _day(
                4,
                'WAYANAD',
                (
                    'Delve into prehistoric antiquity today. Journey to the magnificent Edakkal Caves, situated 1,200 meters up on Ambukuthi Mala. These are not geological caves but an extraordinary natural rock cleft housing petroglyphs dating back over 8,000 years to the Neolithic era. Spend time marveling at the ancient human and animal engravings. In the afternoon, explore a beautifully manicured organic spice farm to witness how pepper, cardamom, and vanilla are harvested.'
                ),
                [
                    'Sightseeing Included: Edakkal Caves Heritage Exploration, Ambalavayal Museum, Organic Spice Farm.',
                    "Immersive Experiences: Guided plantation walk with an expert botanist detailing Malabar's historical spice",
                    'Overnight Stay: Premium Handpicked Wilderness Resort, Wayanad.',
                    'Meals Included: Full Buffet Breakfast & Dinner.',
                ],
            ),
            _day(
                5,
                'WAYANAD TO CALICUT',
                (
                    'Descend the misty mountains back to the sunny shores of Calicut. Check back into your premium seaside luxury sanctuary. Spend your afternoon choosing exquisite souvenirs, high-grade spices, and local banana chips. In the evening, TRAGUIN presents an exclusive private performance of **Kalaripayattu**—the ancient mother of all martial arts, featuring gravity-defying moves and incredible traditional fire-sword play.'
                ),
                [
                    'Sightseeing Included: Calicut Regional Crafts Village, S.M. Street Souvenirs.',
                    'Evening Experience: Exclusive private Kalaripayattu performance followed by an interaction with the master',
                    'Overnight Stay: Handpicked Luxury Resort, Calicut.',
                    'Meals Included: Breakfast & Grand Royal Farewell Dinner.',
                ],
            ),
            _day(
                6,
                'CALICUT DEPARTURE',
                (
                    'Savor a luxurious morning breakfast as the sea breeze rolls over your balcony. Take a last walk along the sandy beachfront before checking out. Your private vehicle will arrive to transfer you smoothly to Calicut International Airport for your flight home. Your elite TRAGUIN Kerala Package concludes with deep cultural insights and unforgettable memories.'
                ),
                [
                    'Transfers Included: Private Airport Drop-off.',
                    'Meals Included: Full Gourmet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('The Raviz Calicut', 'Calicut', '03 Nights', 'Deluxe', 'Deluxe Room', 'MAP (Breakfast + Dinner)', 4, 1),
            _hotel('Sterling Wayanad', 'Wayanad', '02 Nights', 'Deluxe', 'Deluxe Room', 'MAP (Breakfast + Dinner)', 4, 2),
            _hotel('The Gateway Hotel Beach Road', 'Calicut', '03 Nights', 'Premium', 'Premium Room', 'MAP (Breakfast + Dinner)', 4, 3),
            _hotel('Vythiri Village Resort', 'Wayanad', '02 Nights', 'Premium', 'Premium Room', 'MAP (Breakfast + Dinner)', 4, 4),
            _hotel('The Raviz Kadavu (Heritage Resort)', 'Calicut', '03 Nights', 'Luxury', 'Heritage Room', 'MAP (Gourmet Dining)', 5, 5),
            _hotel('Pepper Trail Luxury Plantation Resort', 'Wayanad', '02 Nights', 'Luxury', 'Plantation Villa', 'MAP (Gourmet Dining)', 5, 6),
            _hotel('The Raviz Kadavu (Luxury Suite/Pool Villa)', 'Calicut', '03 Nights', 'Ultra Luxury', 'Luxury Suite / Pool Villa', 'MAP + Immersive inclusions', 5, 7),
            _hotel('Evolve Back, Kabini / Vythiri Resort Luxury Tree House', 'Wayanad', '02 Nights', 'Ultra Luxury', 'Luxury Tree House', 'MAP + Immersive inclusions', 5, 8),
        ],
        inclusions=[
            _inc_included('Accommodation: 05 Nights stay at handpicked premium deluxe/luxury hotels selected for superior comfort.', 1),
            _inc_included('Meals: 05 Premium Buffet Breakfasts and 05 curated gourmet theme Dinners highlighting Malabar spices.', 2),
            _inc_included('Transfers & Sightseeing: Dedicated Chauffeur-driven air-conditioned private vehicle for entire duration as per itinerary.', 3),
            _inc_included('TRAGUIN Support: 24/7 on-call concierge assistance and local guide companion at key historical zones.', 4),
            _inc_included('Complimentary Experiences: Private boat cruise at Pookode Lake and exclusive VIP entrance for live Kalaripayattu performance.', 5),
            _inc_included('Welcome Amenities: Personalized welcome kit with premium Malabar spice samples, natural refreshments, and packaged mineral water.', 6),
            _inc_excluded('Airfare or rail tickets to and from Calicut (Kozhikode).', 7),
            _inc_excluded('Any monument entrance tickets, camera fees, or local porter charges.', 8),
            _inc_excluded('Personal items such as laundry, phone bills, alcoholic beverages, and tips.', 9),
            _inc_excluded('Optional activities or vehicle usage outside of standard day requirements.', 10),
            _inc_excluded('Travel and medical insurance policies.', 11),
        ],
    )
    return package, itinerary

def build_kl_025(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = 'KL-025'
    tour_code = 'TRAGUIN-KL-025'
    title = 'Kumarakom Luxury Corporate Meet'
    duration = '03 Nights / 04 Days'
    slug = 'kl-025-kumarakom-luxury-corporate-meet'
    itin_slug = 'kl-025-kumarakom-luxury-corporate-meet-itinerary'
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
            _ph('State / Country: Kerala / India | Category: Corporate MICE / Luxury Meet', 2),
            _ph('Destinations: Cochin • Kumarakom Luxury Backwaters', 3),
            _ph('Ideal for: Corporate Delegations & Executives', 4),
            _ph('Best season: September to May', 5),
            _ph('Starting price: On Request (Premium Quote)', 6),
            _ph('Travel Format: Corporate Delegation MICE Program', 7),
            _ph('Vehicle: Private AC Luxury Coach & Premium Sedans', 8),
            _ph('Meal Plan: All Inclusive Corporate Gala Plan (APAI)', 9),
            _ph('Route Map: Cochin Airport → Kumarakom Backwaters → Cochin Departure', 10),
            _ph('TRAGUIN Signature Experience: Curated by TRAGUIN corporate MICE specialists with dedicated airport help desks, express group hotel check-ins, and VIP luxury transportation channels.', 11),
            _ph('Shopping: Premium ginger-infused cafes and antique shops in Jew Town Fort Cochin; export spices, coconut shell curiosities, aromatic oils, and Kasavu sarees', 12),
            _ph('Important: Group check-in 14:00 hrs, check-out 11:00 hrs; submit AV and stage specifications 14 days prior; breathable business-casual apparel recommended', 13),
        ],
        moods=['Corporate', 'Luxury', 'Culture'],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note='On Request (Premium Quote)',
        rating=Decimal("4.9"),
        review_count=0,
        tagline='Kumarakom Luxury Corporate Meet • 03 Nights / 04 Days',
        overview=(
            "Welcome to an elite corporate environment set against the emerald backwaters of God's Own Country. This highly professional, premium Kerala Corporate Package by TRAGUIN merges Exclusive Corporate Proposal Page\n\nFamily Tour framework or a dedicated corporate outbound meeting space, Kumarakom provides world-class convention resorts and scenic beauty. From high-tech presentations overlooking Vembanad Lake to customized team-building activities along legendary waterways, our TRAGUIN Kerala Packages ensure zero logistics friction. Discover iconic attractions, luxury houseboat networking lunches, and the absolute Best Time to Visit Kerala with customized hospitality setups curated beautifully to maximize productivity and relaxation.\n\nTRAGUIN Curated Touch: Curated by TRAGUIN corporate MICE specialists with dedicated airport help desks, express group hotel check-ins, and VIP luxury transportation channels."
        ),
        seo_title='KL-025 | Kumarakom Luxury Corporate Meet | TRAGUIN',
        seo_description='Premium 03 Nights / 04 Days Kerala package (KL-025 / TRAGUIN-KL-025): Cochin • Kumarakom Luxury Backwaters. Handpicked luxury stays and private transfers by TRAGUIN.',
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih('Vembanad Lake sunset corporate networking cruise', 1),
            _ih('State-of-the-art conference hall with AV equipment', 2),
            _ih('Chartered premium houseboat networking lunch', 3),
            _ih('Fort Cochin Chinese Fishing Nets heritage tour', 4),
            _ih('TRAGUIN dedicated MICE manager and gala arrangements', 5),
        ],
        days=[
            _day(
                1,
                'COCHIN TO KUMARAKOM',
                (
                    'Arrive at Cochin International Airport where dedicated TRAGUIN representatives orchestrate an exclusive premium welcome process for your team. Board the private air-conditioned luxury coach and embark on a scenic route toward the quiet backwater paradise of Kumarakom. Check in smoothly at your ultra-luxury waterfront convention resort with dedicated corporate hospitality desks. In the late afternoon, enjoy an immersive experience onboard a luxury traditional cruise across Vembanad Lake for spectacular photography points and corporate networking as the sun sets over breathtaking landscapes.'
                ),
                [
                    'Sightseeing Included: Scenic Backwater Drive, Vembanad Lake Sunset Cruise.',
                    'Evening Experience: Ice-breaking corporate cocktail dinner accompanied by classical live instrumental fusion',
                    'Overnight Stay: Ultra-Luxury Waterfront Resort, Kumarakom.',
                    'Meals Included: Welcome Drink, Buffet Lunch & Gala Dinner.',
                ],
            ),
            _day(
                2,
                'KUMARAKOM LUXURY MEET',
                (
                    "Begin with an early morning wellness or yoga session overlooking the tranquil lagoons. Following a lavish international buffet breakfast, convene at the state-of-the-art conference hall for your primary corporate meet. The resort's convention spaces provide premium audio-visual equipment and tailored high-tea breaks managed by TRAGUIN consultants. After a productive afternoon session, transition into an evening of cultural storytelling with a live, mesmerizing Kathakali performance, concluding with an expansive awards night and gala dinner."
                ),
                [
                    'Sightseeing Included: In-house Luxury Retreat Spaces, Evening Cultural Theater.',
                    'Optional Activities: Dedicated Ayurvedic wellness spa treatments or organic village walks during breaks.',
                    'Evening Experience: Corporate Excellence Awards Night with themed gourmet culinary counters.',
                    'Overnight Stay: Ultra-Luxury Waterfront Resort, Kumarakom.',
                    'Meals Included: Full Breakfast, Executive Conference Lunch & Gala Dinner.',
                ],
            ),
            _day(
                3,
                'KUMARAKOM TO COCHIN',
                (
                    'Following breakfast, check out and step directly onto an exclusive chartered premium luxury houseboat. Embark on a spectacular networking cruise through the deep interconnected backwater canals of Alleppey and Kumarakom, enjoying traditional Malabari seafood delicacies prepared by an onboard private chef. In the afternoon, transfer comfortably back to Cochin to explore top tourist places including the historic Fort Cochin lanes, iconic Chinese Fishing Nets, and heritage colonial architecture.'
                ),
                [
                    'Sightseeing Included: Houseboat Backwater Cruise, Chinese Fishing Nets, St. Francis Church Fort Cochin.',
                    'Evening Experience: Elegant farewell dinner at a premium luxury boutique venue in Cochin harbor.',
                    'Overnight Stay: Handpicked Luxury Hotel, Cochin.',
                    'Meals Included: Breakfast, Houseboat Seafood Lunch & Farewell Dinner.',
                ],
            ),
            _day(
                4,
                'COCHIN DEPARTURE',
                (
                    'Savor a final relaxed breakfast at the premium hotel. Depending on your flight departure schedules, enjoy a light shopping tour to pick up premium local spices, high-quality organic tea blends, and traditional Kerala handloom souvenirs. Your luxury private coach will arrive punctually to transfer your delegation to Cochin International Airport, concluding an elite, high-performance corporate event with unforgettable memories.'
                ),
                [
                    'Sightseeing Included: Luxury Spice Market Visit, Guided Shopping Experience.',
                    'Transfers Included: Private Airport Group Drop-off.',
                    'Meals Included: Full Buffet Breakfast.',
                ],
            ),
        ],
        hotels=[
            _hotel('Lake Song Resort Kumarakom', 'Kumarakom', '02 Nights', 'Deluxe', 'Deluxe Room', 'APAI (All Meals Included)', 4, 1),
            _hotel('Trident Hotel Cochin', 'Cochin', '01 Night', 'Deluxe', 'Deluxe Room', 'APAI (All Meals Included)', 4, 2),
            _hotel('Zuri Kumarakom Resort & Spa', 'Kumarakom', '02 Nights', 'Premium', 'Premium Room', 'APAI (All Meals Included)', 4, 3),
            _hotel('Casino Hotel Kochi', 'Cochin', '01 Night', 'Premium', 'Premium Room', 'APAI (All Meals Included)', 4, 4),
            _hotel('Kumarakom Lake Resort', 'Kumarakom', '02 Nights', 'Luxury', 'Heritage Villa', 'APAI (Luxury Meal Plan)', 5, 5),
            _hotel('Brunton Boatyard Kochi', 'Cochin', '01 Night', 'Luxury', 'Heritage Room', 'APAI (Luxury Meal Plan)', 5, 6),
            _hotel('Taj Green Cove / Niraamaya Retreats', 'Kumarakom', '02 Nights', 'Ultra Luxury', 'Executive Villa', 'Custom Elite Corporate VIP Plan', 5, 7),
            _hotel('Grand Hyatt Kochi Bolgatty', 'Cochin', '01 Night', 'Ultra Luxury', 'Grand Suite', 'Custom Elite Corporate VIP Plan', 5, 8),
        ],
        inclusions=[
            _inc_included('Accommodation: Premium luxury stays across handpicked properties with dedicated executive corporate setups.', 1),
            _inc_included('Corporate Venue: Complimentary access to conference infrastructure, AV systems, podiums, and dual high-tea pairings daily.', 2),
            _inc_included('Transfers & Logistics: Premium air-conditioned large luxury coaches for all continuous transfers and local sightseeing.', 3),
            _inc_included('Gala Arrangements: Private chartered lake cruise, tailored regional floral welcome amenities, and dedicated TRAGUIN manager support on-site.', 4),
            _inc_included('Taxes: All current applicable tourism and hospitality service taxes are included.', 5),
            _inc_excluded('Commercial domestic or international airfares, airport terminal taxes, or visa processing documentation fees.', 6),
            _inc_excluded('Individual liquor licenses or specific vintage premium bar packages during gala nights unless pre-purchased.', 7),
            _inc_excluded('Personal laundry bills, micro-bar expenses inside premium resort suites, and independent tips.', 8),
            _inc_excluded('Optional extended vehicle tracking hours or additional excursions outside the itinerary scope.', 9),
        ],
    )
    return package, itinerary

KERALA_DOMESTIC_BUILDERS = [
    build_kl_011,
    build_kl_012,
    build_kl_013,
    build_kl_014,
    build_kl_015,
    build_kl_016,
    build_kl_017,
    build_kl_018,
    build_kl_019,
    build_kl_020,
    build_kl_021,
    build_kl_022,
    build_kl_023,
    build_kl_024,
    build_kl_025,
]
