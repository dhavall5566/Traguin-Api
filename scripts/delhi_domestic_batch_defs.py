"""Builder functions for DL-001 through DL-010 Delhi packages."""

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

DELHI_SLUG = "delhi"


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


def build_dl_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-001"
    tour_code = "TRG-DEL-001"
    title = "Delhi Highlights"
    duration = "02 Nights / 03 Days"
    slug = "dl-001-delhi-highlights"
    itin_slug = "dl-001-delhi-highlights-itinerary"
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
            _ph("State / Country: Delhi / India | Category: Premium Family Tour", 2),
            _ph("Destinations: Old Delhi • New Delhi • Lutyens' Zone • Qutub Complex", 3),
            _ph("Ideal for: Family Getaways, Cultural Explorers & Luxury Travelers", 4),
            _ph("Best season: October to March (Pleasant Winters)", 5),
            _ph("Starting price: On Request (Bespoke Luxury Tier)", 6),
            _ph("Vehicle / Meals: Luxury Private MUV / MAPAI (Breakfast & Dinner)", 7),
            _ph(
                "Route Map: Delhi Arrival → Lutyens' Imperial Tour → Old Delhi Chronicles → "
                "Qutub Complex & Sunder Nursery → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private, reserved fast-track seating at the spectacular "
                "Akshardham evening water light show.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Custom routing designed to avoid major traffic zones, "
                "maximizing your holiday leisure time.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Connaught Place or Khan Market for premium brands; Dilli Haat "
                "for hand-woven textiles, sandalwood crafts, and traditional jewelry.",
                11,
            ),
            _ph(
                "Important Notes: Check-in 14:00 hrs, check-out 12:00 noon; winter fog Nov-Jan; book 30 days "
                "ahead for high-security monuments.",
                12,
            ),
        ],
        moods=["Family", "Cultural", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Bespoke Luxury Tier)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Delhi Highlights • The Imperial Capital Experience",
        overview=(
            "Welcome to an unforgettable journey into the beating heart of India, curated exclusively by TRAGUIN. "
            "Embark on the finest Delhi Family Tour designed to reveal the magnificent heritage, spectacular "
            "architecture, and unmatched culinary tales of this historic empire city. As your premier travel "
            "consultants, TRAGUIN transforms your stay into a seamless luxury holiday, combining handpicked hotels, "
            "elite private transfers, and deeply immersive experiences. From the chaotic charm of Old Delhi to the "
            "sprawling elegance of New Delhi, every detail is engineered to create unforgettable memories for your "
            "family.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored premium luxury vacation balances the classic heritage of a historic empire with "
            "the sophisticated comfort of a modern metropolis. Traveling in a dedicated private luxury transport "
            "vehicle with a professional chauffeur-driven assistant, your family will enjoy absolute safety and style. "
            "Featuring a carefully curated meal plan with expansive premium breakfasts and specialized dinners, this "
            "route represents the definitive premium Delhi experience. Every step of your itinerary includes the "
            "signature touch of TRAGUIN curated experiences, ensuring VIP skip-the-line privileges, local "
            "storytelling insights, and 24/7 bespoke backend support.\n\n"
            "WHY CHOOSE THE BEST DELHI TOUR PACKAGE?\n"
            "When planning a Luxury Delhi Holiday, discerning families seek a deeper connection to history alongside "
            "uncompromising modern luxury. Delhi is an incredible mosaic of empires, showcasing iconic attractions "
            "that bridge centuries. From the towering majesty of the Qutub Minar and the architectural brilliance of "
            "Humayun's Tomb to the solemn grandeur of India Gate, Delhi sightseeing offers an unparalleled journey "
            "through time. For couples and families looking at a Delhi Honeymoon Package or an elegant Delhi Family "
            "Tour, the city boasts world-class popular Instagram locations such as Sunder Nursery, Lodhi Art District, "
            "and the beautiful steps of Agrasen ki Baoli. Whether you want to enjoy a private rickshaw ride through "
            "the culinary streets of Chandni Chowk, indulge in high-end luxury shopping at Chanakyapuri, or "
            "experience a meditative evening at the Lotus Temple, our tailored TRAGUIN Delhi Packages guarantee "
            "premium stays, handpicked hotels, and exclusive experiences during the best time to visit Delhi."
        ),
        seo_title="DL-001 | Delhi Highlights Premium Family Tour | TRAGUIN",
        seo_description=(
            "Premium 02 Nights / 03 Days Delhi package (DL-001 / TRG-DEL-001): Lutyens' Delhi, Old Delhi, "
            "Qutub Minar, Sunder Nursery, Akshardham water show, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("India Gate, Rashtrapati Bhavan, Humayun's Tomb & National War Memorial on Day 01", 1),
            _ih("Red Fort, Jama Masjid, Chandni Chowk, Lotus Temple & Akshardham on Day 02", 2),
            _ih("Qutub Minar, Iron Pillar, Sunder Nursery & Connaught Place on Day 03", 3),
            _ih("TRAGUIN Signature Experience: Private fast-track seating at Akshardham evening water light show", 4),
            _ih("Curated by TRAGUIN Experts: Custom routing to avoid traffic zones and maximize leisure time", 5),
        ],
        days=[
            _day(
                1,
                "Arrival in Delhi & Imperial Lutyens' Tour | Welcome to India's Capital – The Majesty of New Delhi",
                (
                    "Your premium Delhi experience begins with a warm VIP pickup from New Delhi Airport or Railway "
                    "Station by your private luxury transport vehicle. Transfer smoothly to your ultra-luxury handpicked "
                    "hotel for a traditional welcome check-in. In the afternoon, explore the magnificent Lutyens' Delhi "
                    "zone. Drive along the monumental Rajpath to capture spectacular photography points at India Gate, "
                    "Rashtrapati Bhavan, and the Parliament House. Conclude your day with a peaceful visit to the "
                    "beautifully manicured lawns of Humayun's Tomb."
                ),
                [
                    "Sightseeing Included: India Gate, Rashtrapati Bhavan (drive-past), Humayun's Tomb, National War Memorial.",
                    "Evening Experience: A curated multi-course gourmet welcome dinner at a legendary premium restaurant.",
                    "Overnight Stay: New Delhi (Premium / Ultra-Luxury Heritage Hotel).",
                    "Meals Included: Welcome Drink & Luxury Dinner.",
                ],
            ),
            _day(
                2,
                "Old Delhi Chronicles & Spiritual Echoes | Empire Heritage, Rickshaw Sojourns & Street Food Legends",
                (
                    "Savor a lavish buffet breakfast before heading into the historic lanes of Old Delhi. Experience an "
                    "emotional, immersive storytelling tour of the iconic Red Fort, followed by a private rickshaw ride "
                    "through Chandni Chowk, one of India's oldest and busiest markets. Photograph the magnificent Jama "
                    "Masjid and sample world-famous local delicacies. In the afternoon, transition to the serene, "
                    "architectural beauty of the Lotus Temple and the grand Akshardham Temple complex, where a private "
                    "evening musical fountain show has been pre-booked for your family."
                ),
                [
                    "Sightseeing Included: Red Fort, Jama Masjid, Chandni Chowk, Lotus Temple, Akshardham Temple Complex.",
                    "Optional Activities: Private heritage walking tour with an expert historian through the spice market of Khari Baoli.",
                    "Overnight Stay: New Delhi (Premium / Ultra-Luxury Heritage Hotel).",
                    "Meals Included: Premium Breakfast & Specialized Dinner.",
                ],
            ),
            _day(
                3,
                "Antiquity to Departure | Ancient Monuments, Botanical Splendour & Farewell",
                (
                    "Enjoy an early breakfast before visiting the world-famous Qutub Minar complex, a top tourist place "
                    "in Delhi showcasing exquisite 12th-century stone carving. Take a relaxing walk through the "
                    "breathtaking landscapes of Sunder Nursery, a beautifully restored Mughal-era park filled with "
                    "fountains and historic tombs. After a magnificent farewell lunch, your private vehicle will chauffeur "
                    "you back to the airport or railway station, concluding an unforgettable luxury vacation."
                ),
                [
                    "Sightseeing Included: Qutub Minar, Iron Pillar, Sunder Nursery Heritage Park, Connaught Place.",
                    "Transfers Included: Private luxury departure transfer drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "The Claridges / Eros Hotel New Delhi / similar",
                "New Delhi",
                "02 Nights",
                "Deluxe",
                "Deluxe Executive Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: The Claridges / Eros Hotel New Delhi / similar | Deluxe Executive Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Taj Mahal Hotel (Mansingh Road) / Shangri-La",
                "New Delhi",
                "02 Nights",
                "Premium",
                "Premium City View Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="OPTION 02 – PREMIUM: Taj Mahal Hotel (Mansingh Road) / Shangri-La | Premium City View Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Leela Palace New Delhi / The Imperial Delhi",
                "New Delhi",
                "02 Nights",
                "Luxury",
                "Grand Luxury Heritage Suite",
                "MAPAI + Welcome Amenities",
                5,
                3,
                description="OPTION 03 – LUXURY: The Leela Palace New Delhi / The Imperial Delhi | Grand Luxury Heritage Suite | MAPAI + Welcome Amenities",
            ),
            _hotel(
                "The Oberoi New Delhi (Overlooking Golf Course)",
                "New Delhi",
                "02 Nights",
                "Ultra Luxury",
                "VVIP Custom Luxury Premier Suite",
                "Bespoke Royal MAPAI Plan",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: The Oberoi New Delhi (Overlooking Golf Course) | VVIP Custom Luxury Premier Suite | Bespoke Royal MAPAI Plan",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: 02 Nights in highly rated luxury hotels.", 1),
            _inc_included("Luxury Transportation: Private dedicated AC vehicle for all transfers and tours.", 2),
            _inc_included("Curated Meal Plan: Daily premium breakfasts and gourmet multi-cuisine dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 personalized customer care assistance.", 4),
            _inc_included("Complimentary Experience: Private family rickshaw ride inside Chandni Chowk.", 5),
            _inc_included("Welcome Amenities: Personalized family gift kit, taxes, and highway surcharges.", 6),
            _inc_excluded("Airfare, domestic flights, or train tickets to Delhi.", 7),
            _inc_excluded("Monument entry tickets, professional guide fees, and camera permits.", 8),
            _inc_excluded("Personal expenses such as laundry, telephone calls, or mini-bar usage.", 9),
            _inc_excluded("Optional activities, premium spa services, or items not mentioned.", 10),
        ],
    )
    return package, itinerary


def build_dl_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-002"
    tour_code = "TRG-DEL-002"
    title = "Old and New Delhi Heritage"
    duration = "03 Nights / 04 Days"
    slug = "dl-002-old-and-new-delhi-heritage"
    itin_slug = "dl-002-old-and-new-delhi-heritage-itinerary"
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
            _ph("State / Country: Delhi / India | Category: Premium Heritage & Luxury Culture", 2),
            _ph("Destinations: Old Delhi • New Delhi • Lutyens' Zone • Sunder Nursery", 3),
            _ph("Ideal for: Families, Connoisseurs of History & Luxury Travellers", 4),
            _ph("Best season: October to March (Pleasant Winters)", 5),
            _ph("Starting price: On Request (Premium Bespoke Curation)", 6),
            _ph("Vehicle / Meals: Private Luxury Executive Sedan / MAPAI", 7),
            _ph(
                "Route Map: Imperial Welcome → Mughal Chronicles & Old Delhi → Architectural Masterpieces → "
                "Bangla Sahib & Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private walking tour through Sunder Nursery's hidden botanical paths "
                "accompanied by a historian.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Smart daily schedules designed to avoid peak city traffic jams, "
                "maximizing relaxation.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Janpath and Khan Market for pashmina shawls, Khari Baoli spices, "
                "silver jewelry, and designer Indian ensembles.",
                11,
            ),
            _ph(
                "Important Notes: Check-in 14:00 hrs, check-out 11:00 hrs; Sunder Nursery best at golden hours; "
                "book 30 days ahead for peak winter.",
                12,
            ),
        ],
        moods=["Family", "Heritage", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Bespoke Curation)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Old and New Delhi Heritage • Chronicle of Empires & Icons",
        overview=(
            "Welcome to an extraordinary passage through time curated exclusively by TRAGUIN. Experience the "
            "ultimate Delhi Family Tour and bespoke Delhi Honeymoon Package designed to reflect the sublime "
            "grandiosity of India's capital city. As your highly professional travel consultants, TRAGUIN transforms "
            "your exploration into a seamless luxury holiday combining handpicked hotels, legendary historical "
            "insights, and exclusive privileges. From the chaotic charm of old-world Mughal bastions to the stately "
            "elegance of New Delhi, discover iconic attractions and breathtaking landscapes that will leave you with "
            "beautiful, unforgettable memories.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored luxury holiday package provides a meticulously balanced itinerary across India's "
            "imperial capital. Traveling in a fully private, chauffeured executive luxury vehicle, you will experience "
            "unmatched urban comfort. Enjoy an extensive meal plan comprising expansive breakfast spreads and "
            "uniquely curated dinners showcasing legendary North Indian culinary styles. This premium Delhi experience "
            "is further enhanced by the signature TRAGUIN curated experience note, which guarantees fast-track VIP "
            "access parameters, personalized expert local guides, and 24/7 dedicated guest hospitality.\n\n"
            "WHY CHOOSE THE BEST DELHI TOUR PACKAGE?\n"
            "To truly appreciate a Luxury Delhi Holiday, sophisticated travelers look past standard itineraries to "
            "unlock the complex soul of this historic capital. From the colossal red sandstone ramparts of the Red "
            "Fort to the elegant geometric perfection of Humayun's Tomb, Delhi sightseeing presents some of the "
            "world's most dramatic architecture. It is a timeless city where thousands of years of dynastic history "
            "seamlessly mesh with contemporary high-end urban living. Whether you are seeking a memorable Delhi "
            "Family Tour or a romantic Delhi Honeymoon Package, the city offers popular Instagram locations like the "
            "towering Qutub Minar, the sprawling manicured lawns of Sunder Nursery, and the iconic India Gate. "
            "Indulge in elite local street food trails in Old Delhi, discover premium high-fashion shopping at "
            "Connaught Place, and immerse yourself in the deep spiritual serenity of Bangla Sahib. Choosing our "
            "signature TRAGUIN Delhi Packages guarantees unmatched safety, handpicked luxury stays, and curated "
            "immersive experiences during the absolute best time to visit Delhi."
        ),
        seo_title="DL-002 | Old and New Delhi Heritage Premium Tour | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Delhi heritage package (DL-002 / TRG-DEL-002): Red Fort, Chandni Chowk, "
            "Qutub Minar, Humayun's Tomb, Sunder Nursery, Bangla Sahib, and 4-tier handpicked accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("India Gate, Rashtrapati Bhavan, Parliament House & Connaught Place on Day 01", 1),
            _ih("Red Fort, Jama Masjid, Chandni Chowk, Khari Baoli & Raj Ghat on Day 02", 2),
            _ih("Qutub Minar, Humayun's Tomb, Sunder Nursery & Lotus Temple on Day 03", 3),
            _ih("Gurudwara Bangla Sahib & departure transfer on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Private walking tour through Sunder Nursery with a historian", 5),
            _ih("Curated by TRAGUIN Experts: Smart schedules to avoid peak traffic and maximize relaxation", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Delhi – The Imperial Welcome | Lutyens' Majesty & Stately Urban Elegance",
                (
                    "Your premium Delhi experience begins as you touch down at Indira Gandhi International Airport, "
                    "where a private luxury executive transport vehicle and uniform-clad chauffeur await your family. "
                    "Transfer directly to your handpicked premium luxury hotel for a smooth check-in. In the "
                    "afternoon, enjoy a majestic drive down Rajpath (Kartavya Path) to view the stately Rashtrapati "
                    "Bhavan and India Gate. Conclude your evening at the historic Connaught Place for architectural "
                    "photography and high-end boutique shopping."
                ),
                [
                    "Sightseeing Included: India Gate, Parliament House (Drive-by), Rashtrapati Bhavan exterior vistas, Connaught Place.",
                    "Evening Experience: Welcome dinner with an authentic Awadhi/Mughlai menu specially arranged by TRAGUIN experts.",
                    "Overnight Stay: New Delhi (Premium / Luxury Central Heritage Hotel).",
                    "Meals Included: Welcome Drinks & Gourmet Dinner.",
                ],
            ),
            _day(
                2,
                "Mughal Chronicles & Old Delhi Insights | Chandni Chowk Chronicles & Rickshaw Safaris",
                (
                    "Following a lavish breakfast, dive into the bustling heart of Old Delhi. Explore the grand Red "
                    "Fort, the primary residence of the Mughal emperors for nearly two centuries. Board a privately "
                    "arranged luxury rickshaw safari through the narrow lanes of Chandni Chowk, passing historic spice "
                    "markets and ancient mansion facades. Visit the towering Jama Masjid, one of India's largest "
                    "mosques. In the afternoon, shift to quiet reflection with a peaceful walk through Raj Ghat, the "
                    "memorial dedicated to Mahatma Gandhi."
                ),
                [
                    "Sightseeing Included: Red Fort (UNESCO Site), Jama Masjid, Chandni Chowk Khari Baoli, Raj Ghat.",
                    "Optional Activities: Guided street-food tasting trail featuring historic sweet shops dating back to the 19th century.",
                    "Overnight Stay: New Delhi (Premium / Luxury Central Heritage Hotel).",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                3,
                "Architectural Masterpieces & Heritage Parks | Soaring Minarets, Royal Tombs & Sunset Gardens",
                (
                    "Dedicate your day to exploring Delhi's iconic attractions. Begin at the Qutub Minar complex, a "
                    "73-meter-tall sandstone victory tower showcasing exquisite Islamic calligraphy and ancient iron "
                    "pillars. Next, visit Humayun's Tomb, the gorgeous garden-tomb that directly inspired the Taj "
                    "Mahal. Spend your late afternoon wandering through the breathtaking landscapes of Sunder "
                    "Nursery, a beautifully restored heritage park and one of the city's most popular Instagram "
                    "locations."
                ),
                [
                    "Sightseeing Included: Qutub Minar, Humayun's Tomb, Sunder Nursery Heritage Park, Lotus Temple (Bahá'í House of Worship).",
                    "Evening Experience: Private evening tea session inside Sunder Nursery followed by the tranquil sunset illumination tour.",
                    "Overnight Stay: New Delhi (Premium / Luxury Central Heritage Hotel).",
                    "Meals Included: Premium Breakfast & Luxury Buffet Dinner.",
                ],
            ),
            _day(
                4,
                "Departure – Carrying Memories of Kings | Spiritual Serenity & Farewell Transfers",
                (
                    "Savor your last lavish breakfast at your premium hotel. Check out and visit Gurudwara Bangla "
                    "Sahib, experiencing its massive community kitchen (Langar) and peaceful holy pool. Afterwards, "
                    "your private luxury transport vehicle will safely drop you back at New Delhi Airport or the "
                    "railway station for your onward journey. Return home carrying beautiful family bonds and "
                    "unforgettable memories meticulously structured by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door departure drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "The Suryaa New Delhi / Welcomhotel Dwarka",
                "New Delhi",
                "03 Nights",
                "Deluxe",
                "Executive Deluxe Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: The Suryaa New Delhi / Welcomhotel Dwarka | Executive Deluxe Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Lalit New Delhi / Le Meridien / similar",
                "New Delhi",
                "03 Nights",
                "Premium",
                "Premium Club City View Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="OPTION 02 – PREMIUM: The Lalit New Delhi / Le Meridien / similar | Premium Club City View Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Taj Mahal Hotel (Mansingh Road) / The Imperial",
                "New Delhi",
                "03 Nights",
                "Luxury",
                "Luxury Heritage Suite",
                "MAPAI + Welcome Curated Amenities",
                5,
                3,
                description="OPTION 03 – LUXURY: Taj Mahal Hotel (Mansingh Road) / The Imperial | Luxury Heritage Suite | MAPAI + Welcome Curated Amenities",
            ),
            _hotel(
                "The Leela Palace New Delhi / The Lodhi",
                "New Delhi",
                "03 Nights",
                "Ultra Luxury",
                "Grande Luxury Room with Plunge Pool",
                "VVIP Custom Tailored Meal Curation",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: The Leela Palace New Delhi / The Lodhi | Grande Luxury Room with Plunge Pool | VVIP Custom Tailored Meal Curation",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: 03 Nights in handpicked heritage/luxury urban properties.", 1),
            _inc_included("Luxury Transportation: Private dedicated executive sedan for all sightseeing.", 2),
            _inc_included("Curated Meal Plan: Daily premium breakfast spreads and fine-dining dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 personalized customer care and guest assistance tracking.", 4),
            _inc_included("Welcome Amenities: Personalized travel kit, traditional stoles, and refreshments.", 5),
            _inc_included("Complimentary Experience: Private custom rickshaw ride through old Chandni Chowk lanes.", 6),
            _inc_excluded("Airfare, domestic flights, or long-distance interstate train tickets.", 7),
            _inc_excluded("Monument entry fees, camera permits, and specialized archaeological guides.", 8),
            _inc_excluded("Personal expenses such as boutique laundry, liquor, and driver tips.", 9),
            _inc_excluded("Optional culinary walks, night excursions, or travel insurance covers.", 10),
        ],
    )
    return package, itinerary


def build_dl_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-003"
    tour_code = "TRG-DEL-003"
    title = "Educational Delhi Tour"
    duration = "03 Nights / 04 Days"
    slug = "dl-003-educational-delhi-tour"
    itin_slug = "dl-003-educational-delhi-tour-itinerary"
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
            _ph("State / Country: Delhi / India | Category: School Educational Tour", 2),
            _ph("Destinations: New Delhi • Old Delhi • National Science Centre • Akshardham", 3),
            _ph("Ideal for: Students, Academic Batches & Institution Scholars", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Student Tariff)", 6),
            _ph("Vehicle / Meals: Premium AC Luxury Coach / APAI (All Meals Included)", 7),
            _ph(
                "Route Map: Imperial Exploration → Science Discovery → Old Delhi Heritage & Akshardham → "
                "Crafts Museum & Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private interactive session with leading historical preservationists "
                "inside the Red Fort quarter.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Seamless routes designed to avoid heavy urban rush hour traffic, "
                "prioritizing safety and student focus.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Janpath Market and Dilli Haat for traditional puppets, ethnic "
                "bookmarks, regional paintings, and sandalwood souvenirs.",
                11,
            ),
            _ph(
                "Important Notes: Room discipline required; luxury coach on pre-approved corridors; pre-approve "
                "monuments 30 days prior.",
                12,
            ),
        ],
        moods=["Educational", "Family", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Student Tariff)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Educational Delhi Tour • Unveiling History & Innovation",
        overview=(
            "Welcome to an expertly crafted scholastic journey designed and managed by TRAGUIN. This specialized "
            "Educational Delhi Tour is engineered to immerse young scholars in the iconic attractions, cultural "
            "milestones, and monumental milestones of the national capital. As premium travel consultants, TRAGUIN "
            "blends luxury student logistics with high-value learning to create unforgettable memories. From the power "
            "corridors of New Delhi to the ancient heritage sites of Old Delhi, this journey promises safe, premium "
            "stays, immersive experiences, and deep intellectual inspiration.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-designed academic itinerary presents a seamless balance between Delhi sightseeing, "
            "experiential discovery, and scientific innovation. Travelling in a high-end, safety-vetted luxury coach "
            "with full onboard GPS tracking and dedicated tour managers, the students enjoy peak comfort. Offering an "
            "all-inclusive premium meal plan with strict hygiene standards, the route showcases the finest heritage "
            "landmarks and modern institutional zones. Every detail incorporates a specialized TRAGUIN curated "
            "experience note, encompassing pre-approved student entries, expert historical guides, and 24/7 dedicated "
            "security protocol.\n\n"
            "WHY BOOK THE BEST DELHI TOUR PACKAGE FOR STUDENTS?\n"
            "An enrichment-led Luxury Delhi Holiday serves as a vital cornerstone for experiential academic growth. "
            "When booking a specialized Delhi Family Tour or a premium Delhi Educational Tour, institutions gain "
            "unparalleled access to the top tourist places in Delhi. Scholars dive straight into live architectural "
            "studies at the spectacular Qutub Minar, observe the governance mechanics at Rashtrapati Bhavan, and "
            "explore evolutionary physics inside the National Science Centre. For educational groups looking for "
            "cultural depth, Delhi highlights highly sought-after, popular Instagram locations such as the grand India "
            "Gate and the sprawling, tech-forward Akshardham Temple complex. From heritage shopping strolls in Janpath "
            "to tasting historic culinary methods in traditional hubs, our premium TRAGUIN Delhi Packages ensure "
            "handpicked hotels with separate safe blocks for boys and girls, making any season the best time to visit "
            "Delhi for a high-value, organized institutional journey."
        ),
        seo_title="DL-003 | Educational Delhi Tour Premium Student Package | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days educational Delhi package (DL-003 / TRG-DEL-003): National Science Centre, "
            "Qutub Minar, Red Fort, Akshardham, Crafts Museum, and secure 4-tier student accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("India Gate, Rashtrapati Bhavan, National War Memorial & student debate workshop on Day 01", 1),
            _ih("Qutub Minar, National Science Centre & Humayun's Tomb on Day 02", 2),
            _ih("Red Fort, Old Delhi Heritage Quarter & Akshardham Sahaj Anand Water Show on Day 03", 3),
            _ih("National Crafts Museum, artisan interactions & departure on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Private session with historical preservationists at Red Fort", 5),
            _ih("Personalized Assistance: Certified first-aid trained coordinators throughout the journey", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Delhi & Imperial Exploration | Chronicles of Nationhood – The Colonial Epicentre",
                (
                    "Your premium educational journey kicks off with a warm, organized reception by the TRAGUIN field "
                    "staff at New Delhi Airport or Railway Station. Board your private luxury coach and transfer "
                    "directly to your handpicked hotel for briefing and check-in. In the afternoon, start your premium "
                    "Delhi experience with a grand drive along Rajpath. Explore the stunning architecture of India "
                    "Gate, photograph the prestigious Rashtrapati Bhavan, and tour the National War Memorial to learn "
                    "about the nation's contemporary history."
                ),
                [
                    "Sightseeing Included: India Gate, Rashtrapati Bhavan (Drive past), National War Memorial, Sansad Bhavan view.",
                    "Evening Experience: Interactive student debate workshop on modern Indian history led by academic guides.",
                    "Overnight Stay: New Delhi (Premium / Secured Student Wing Hotel).",
                    "Meals Included: Welcome Drink, Mid-day Refreshments & Institutional Dinner.",
                ],
            ),
            _day(
                2,
                "Historic Delhi & Science Discovery | From Medieval Monuments to Revolutionary Science",
                (
                    "Begin the day with an early breakfast, followed by a visit to the UNESCO World Heritage Site—"
                    "Qutub Minar, a prime example of Indo-Islamic architecture. Next, shift focus to technological "
                    "exploration at the National Science Centre. Here, students engage in immersive experiences across "
                    "human biology galleries, nuclear physics exhibits, and live science demonstration labs. Wind up the "
                    "afternoon with a visit to Humayun's Tomb, the architectural inspiration behind the Taj Mahal."
                ),
                [
                    "Sightseeing Included: Qutub Minar Complex, Iron Pillar of Delhi, National Science Centre, Humayun's Tomb.",
                    "Optional Activities: Private planetarium show or 3D innovation lab workshop at the science centre.",
                    "Overnight Stay: New Delhi (Premium / Secured Student Wing Hotel).",
                    "Meals Included: Nutritious Breakfast, Packaged Hot Lunch & Premium Dinner.",
                ],
            ),
            _day(
                3,
                "Heritage of Old Delhi & Akshardham Evening | Ancient Ramparts to Extravagant Multimedia Spectacles",
                (
                    "Dive into the classic side of the city with an immersive tour of the monumental Red Fort, tracing "
                    "the rise and fall of empires. Walk past the historic Jama Masjid, experiencing the cultural pulse "
                    "of Old Delhi. In the afternoon, transition to the majestic Akshardham Temple complex. Here, "
                    "students explore ancient Indian heritage through cultural boat rides, robotics exhibitions, and a "
                    "spectacular evening multimedia musical fountain show."
                ),
                [
                    "Sightseeing Included: Red Fort, Old Delhi Heritage Quarter, Swaminarayan Akshardham Complex & Exhibition Halls.",
                    "Evening Experience: The iconic Sahaj Anand Water Show—a breathtaking display of multi-color lasers and fire tech.",
                    "Overnight Stay: New Delhi (Premium / Secured Student Wing Hotel).",
                    "Meals Included: Premium Breakfast, Buffet Lunch & Grand Farewell Dinner.",
                ],
            ),
            _day(
                4,
                "Crafts Museum & Knowledge Retreat / Departure | Handlooms, Heritage & Sweet Departure Memories",
                (
                    "Following your morning breakfast, explore the National Crafts Museum, styled like a traditional "
                    "Indian village. Students can interact directly with rural master artisans, learning about "
                    "sustainable materials, traditional block-printing, and ancient terracotta arts. After a group "
                    "photo and an academic feedback session, board your luxury coach for your transfer to the station "
                    "or airport, concluding a journey filled with unforgettable memories tailored by TRAGUIN."
                ),
                [
                    "Transfers Included: Group escort and private airport/station luxury drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast & Continental Lunch.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Hotel Pride Plaza / Fortune Park / similar",
                "New Delhi",
                "03 Nights",
                "Deluxe",
                "Standard Triple Sharing",
                "APAI (All Meals Included) | CCTV Monitored Corridor, Guarded Entry",
                4,
                1,
                description="OPTION 01 – DELUXE: Hotel Pride Plaza / Fortune Park / similar | Standard Triple Sharing | CCTV Monitored Corridor, Guarded Entry",
            ),
            _hotel(
                "Radisson Blu / Welcomhotel by ITC / similar",
                "New Delhi",
                "03 Nights",
                "Premium",
                "Premium Twin/Triple Beds",
                "APAI (All Meals Included) | Dedicated Wing, Electronic Smart Keys",
                4,
                2,
                description="OPTION 02 – PREMIUM: Radisson Blu / Welcomhotel by ITC / similar | Premium Twin/Triple Beds | Dedicated Wing, Electronic Smart Keys",
            ),
            _hotel(
                "The Grand New Delhi / Eros Hotel / similar",
                "New Delhi",
                "03 Nights",
                "Luxury",
                "Executive Club Twin Room",
                "APAI (All Meals Included) | In-house Medical Assistance Desk",
                5,
                3,
                description="OPTION 03 – LUXURY: The Grand New Delhi / Eros Hotel / similar | Executive Club Twin Room | In-house Medical Assistance Desk",
            ),
            _hotel(
                "Taj Palace / The Leela Palace New Delhi",
                "New Delhi",
                "03 Nights",
                "Ultra Luxury",
                "Grand Luxury Garden Suite",
                "APAI (All Meals Included) | Elite Multi-tier Security Clearances",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: Taj Palace / The Leela Palace New Delhi | Grand Luxury Garden Suite | Elite Multi-tier Security Clearances",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: Secure, handpicked student-friendly luxury properties.", 1),
            _inc_included("Luxury Transportation: Private air-conditioned luxury coach for all transfers.", 2),
            _inc_included("Curated Meal Plan: High-nutrition hygienic meals (APAI: Breakfast, Lunch, Dinner).", 3),
            _inc_included("TRAGUIN Support: Dedicated round-the-clock student welfare manager.", 4),
            _inc_included("Welcome Amenities: Customized student travel journals, pens, and identity badges.", 5),
            _inc_included("Complimentary Experience: Pre-booked entry tickets to Akshardham Exhibitions.", 6),
            _inc_excluded("Airfare, train ticketing fees from the home institution city.", 7),
            _inc_excluded("Personal expenses such as arcade games, laundry, room service drinks.", 8),
            _inc_excluded("Any insurance fees or unexpected medical costs outside basic first-aid.", 9),
            _inc_excluded("Optional excursions or extra site visits not explicitly part of the schedule.", 10),
        ],
    )
    return package, itinerary


def build_dl_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-004"
    tour_code = "TRG-DEL-AGR-004"
    title = "Delhi Agra Gateway"
    duration = "04 Nights / 05 Days"
    slug = "dl-004-delhi-agra-gateway"
    itin_slug = "dl-004-delhi-agra-gateway-itinerary"
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
            _ph("State / Country: Delhi & Uttar Pradesh / India | Category: Premium Family Tour", 2),
            _ph("Destinations: New Delhi • Old Delhi • Yamuna Expressway • Agra", 3),
            _ph("Ideal for: Family Vacations, Heritage Enthusiasts & Luxury Lovers", 4),
            _ph("Best season: October to March (Pleasant Winter Capital Season)", 5),
            _ph("Starting price: On Request (Premium Bespoke Family Rate)", 6),
            _ph("Vehicle / Meals: Private Luxury SUV / MAPAI (Lavish Breakfast & Dinner)", 7),
            _ph(
                "Route Map: Delhi Arrival → Full Day Delhi Sightseeing → Yamuna Expressway to Agra → "
                "Taj Mahal Sunrise & Agra Fort → Return to Delhi",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private sunrise timing synchronization for optimal Taj Mahal "
                "lighting and crowd avoidance.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Chauffeur routing structured to utilize peak highway conditions, "
                "giving you more time for leisure.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Khan Market textiles in Delhi; Agra marble inlay (Pietra Dura), "
                "leather goods, and Zardozi embroidery.",
                11,
            ),
            _ph(
                "Important Notes: Valid photo ID required; Taj Mahal closed Fridays; book 30–45 days ahead for "
                "monument-view rooms.",
                12,
            ),
        ],
        moods=["Family", "Heritage", "Romantic"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Bespoke Family Rate)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Delhi Agra Gateway • Empires, Elegance & Eternal Romance",
        overview=(
            "Welcome to an unforgettable voyage through time, art, and imperial legacy curated exclusively by "
            "TRAGUIN. Embark on the finest Delhi Family Tour and Agra getaway, engineered to introduce your loved "
            "ones to the breathtaking landscapes, sprawling fortresses, and monumental wonders of India's golden "
            "heritage core. As your elite travel consultants, TRAGUIN transforms this iconic route into a seamless "
            "luxury holiday featuring premium stays, handpicked hotels, and deeply moving historical storytelling. "
            "Witness the monumental grace of Delhi and the timeless majesty of Agra's Taj Mahal to gather sweet, "
            "unforgettable memories.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored luxury holiday itinerary offers an unparalleled heritage balance between the "
            "old-world lanes of Shahjahanabad, the polished avenues of Lutyens' New Delhi, and the eternal romance "
            "of Mughal Agra. Travelling in a dedicated private premium AC vehicle with an expert, background-verified "
            "chauffeur, your family will experience flawless connectivity. With a meticulously curated meal plan "
            "comprising daily multi-cuisine breakfasts and specialized elite dining, this getaway sets the gold "
            "standard for a premium Delhi experience. Every segment includes the signature touch of TRAGUIN curated "
            "experiences, assuring priority entry privileges and round-the-clock boutique assistance.\n\n"
            "WHY CHOOSE THE BEST DELHI AGRA TOUR PACKAGE?\n"
            "When considering a Luxury Delhi Holiday or an iconic Golden Triangle snippet, discerning travelers "
            "look for a path that minimizes transit stress and maximizes cultural depth. This route offers a window "
            "into the most famous attractions of Northern India. From the soaring minarets of Qutub Minar and the "
            "stately dome of Humayun's Tomb—top tourist places in Delhi—to the legendary ivory-white marble contours "
            "of the Taj Mahal in Agra, every turn reveals absolute grandeur. For couples and modern families seeking "
            "a tailored Delhi Honeymoon Package or Agra Family Tour, the region unveils highly sought-after, popular "
            "Instagram locations like Sunder Nursery, Connaught Place, Safdarjung Tomb, and the reflective banks of "
            "the Yamuna River at Mehtab Bagh. Indulge in premium handicraft shopping, explore historic bazaars, or "
            "sample legendary culinary delights. Our signature TRAGUIN Delhi Packages seamlessly blend handpicked "
            "luxury stays and curated exclusive experiences, guaranteeing that you enjoy the best time to visit Delhi "
            "and Agra with absolute distinction."
        ),
        seo_title="DL-004 | Delhi Agra Gateway Premium Family Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Delhi Agra package (DL-004 / TRG-DEL-AGR-004): Old & New Delhi, "
            "Yamuna Expressway, Mehtab Bagh, Taj Mahal sunrise, Agra Fort, and 4-tier multi-city accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("India Gate, Rashtrapati Bhavan, Connaught Place & welcome dinner on Day 01", 1),
            _ih("Red Fort, Jama Masjid, Chandni Chowk, Humayun's Tomb & Qutub Minar on Day 02", 2),
            _ih("Yamuna Expressway to Agra, Mehtab Bagh sunset & cultural artisan show on Day 03", 3),
            _ih("Taj Mahal sunrise, Agra Fort & Baby Taj on Day 04", 4),
            _ih("Return to Delhi & departure transfer on Day 05", 5),
            _ih("TRAGUIN Signature Experience: Private sunrise timing for optimal Taj Mahal lighting", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Delhi | Welcome to the Imperial Capital – Urban Luxury & Elite Welcome",
                (
                    "Your premium Delhi experience begins as your flight or train lands in the national capital. A "
                    "dedicated private luxury transport vehicle will greet you with custom refreshments and escort you "
                    "directly to your handpicked premium luxury hotel. After a refreshing check-in and afternoon at "
                    "leisure, step out to explore the polished avenues of Lutyens' Delhi. Drive past the historic India "
                    "Gate, the majestic Rashtrapati Bhavan, and the ultra-modern architecture of the new Parliament "
                    "House, taking beautiful photos as dusk settles over the capital."
                ),
                [
                    "Sightseeing Included: India Gate, Kartavya Path, Rashtrapati Bhavan exterior, Connaught Place.",
                    "Evening Experience: Elite welcome dinner at a curated culinary restaurant specializing in royal frontier cuisine.",
                    "Overnight Stay: New Delhi (Premium / Luxury Selected Hotel).",
                    "Meals Included: Welcome Drink & Fine-Dining Dinner.",
                ],
            ),
            _day(
                2,
                "Full Day Delhi Sightseeing | The Tale of Two Cities – Chronicles of Old & New Delhi",
                (
                    "Awake to a lavish breakfast before diving into a detailed Delhi sightseeing tour. Start in Old Delhi "
                    "with a private premium rickshaw ride through the bustling alleys of Chandni Chowk, admiring the "
                    "grand walls of the Red Fort and visiting the monumental Jama Masjid. In the afternoon, shift to the "
                    "peaceful oasis of New Delhi to explore Humayun's Tomb, a magnificent precursor to the Taj Mahal, "
                    "and the soaring, ancient stone masterpiece of the Qutub Minar complex."
                ),
                [
                    "Sightseeing Included: Red Fort, Jama Masjid, Chandni Chowk rickshaw ride, Humayun's Tomb, Qutub Minar.",
                    "Optional Activities: Bespoke evening high-tea experience inside the elegant corridors of the heritage Imperial Hotel.",
                    "Overnight Stay: New Delhi (Premium / Luxury Selected Hotel).",
                    "Meals Included: Premium Luxury Breakfast & Dinner.",
                ],
            ),
            _day(
                3,
                "Delhi to Agra (Via Yamuna Expressway) | Journey to the Mughal Seat – Twilight at Mehtab Bagh",
                (
                    "Following a sumptuous breakfast, check out and embark on a smooth, comfortable drive along the "
                    "modern Yamuna Expressway to Agra. Arrive by afternoon and check into your ultra-luxury resort, "
                    "where rooms can be curated to overlook the monument lines. In the golden hours of the evening, "
                    "enjoy a private visit to Mehtab Bagh (The Moonlight Garden), located across the river. Take stunning "
                    "photographs as the sunset casts soft golden hues over the white marble of the Taj Mahal."
                ),
                [
                    "Sightseeing Included: Expressway scenic transit, Mehtab Bagh, sunset riverside viewpoint.",
                    "Evening Experience: Private viewing of a local cultural artisan show detailing the history of the Taj Mahal.",
                    "Overnight Stay: Agra (Premium / Ultra Luxury Hotel).",
                    "Meals Included: Breakfast & Traditional Awadhi Style Dinner.",
                ],
            ),
            _day(
                4,
                "Agra Sightseeing Excursion | The Epitome of Eternal Love & Formidable Citadels",
                (
                    "Experience a magical sunrise visit to the Taj Mahal, the world's ultimate monument to love. Walk "
                    "the serene pathways accompanied by an expert historian who will bring the Mughal era to life with "
                    "emotional storytelling. Return to the resort for a fresh breakfast, then head out to explore the "
                    "massive red sandstone ramparts of Agra Fort, a UNESCO World Heritage site full of grand palaces "
                    "and courtyards."
                ),
                [
                    "Sightseeing Included: The Taj Mahal (Sunrise tour), Agra Fort, Tomb of Itmad-ud-Daulah (Baby Taj).",
                    "Optional Activities: An excursion to Fatehpur Sikri, the preserved red sandstone Mughal city (optional).",
                    "Overnight Stay: Agra (Premium / Ultra Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Luxury Gala Dinner.",
                ],
            ),
            _day(
                5,
                "Agra to Delhi / Departure | Returning with Cherished Memories Beyond Destinations",
                (
                    "Enjoy a final luxury breakfast at your premium hotel before starting your return drive to Delhi. "
                    "Your private luxury transport will take you smoothly back along the expressway, dropping you off "
                    "directly at New Delhi Airport or Railway Station for your onward journey. Return home carrying "
                    "beautiful family bonds and unforgettable memories meticulously designed by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door expressway drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Radisson Blu / Welcomhotel Dwarka | Crystal Sarovar Premiere / Radisson Agra",
                "Delhi (2 Nights) / Agra (2 Nights)",
                "04 Nights",
                "Deluxe",
                "Deluxe Room",
                "MAPAI (Breakfast & Dinner included)",
                4,
                1,
                description="OPTION 01 – DELUXE: Radisson Blu / Welcomhotel Dwarka (Delhi, 2 Nights) | Crystal Sarovar Premiere / Radisson Agra (Agra, 2 Nights) | MAPAI (Breakfast & Dinner included)",
            ),
            _hotel(
                "Crowne Plaza Okhla / Hyatt Regency | Taj Hotel & Convention Centre Agra",
                "Delhi (2 Nights) / Agra (2 Nights)",
                "04 Nights",
                "Premium",
                "Premium Room",
                "MAPAI + Elevated Room View Amenities",
                5,
                2,
                description="OPTION 02 – PREMIUM: Crowne Plaza Okhla / Hyatt Regency (Delhi, 2 Nights) | Taj Hotel & Convention Centre Agra (Agra, 2 Nights) | MAPAI + Elevated Room View Amenities",
            ),
            _hotel(
                "The Leela Ambience / Taj Palace Delhi | ITC Mughal, A Luxury Collection Hotel",
                "Delhi (2 Nights) / Agra (2 Nights)",
                "04 Nights",
                "Luxury",
                "Luxury Room",
                "MAPAI + Signature Wellness Spa Access",
                5,
                3,
                description="OPTION 03 – LUXURY: The Leela Ambience / Taj Palace Delhi (Delhi, 2 Nights) | ITC Mughal, A Luxury Collection Hotel (Agra, 2 Nights) | MAPAI + Signature Wellness Spa Access",
            ),
            _hotel(
                "The Lodhi / The Imperial New Delhi | The Oberoi Amarvilas (Taj View Rooms)",
                "Delhi (2 Nights) / Agra (2 Nights)",
                "04 Nights",
                "Ultra Luxury",
                "Luxury Suite / Taj View Room",
                "Bespoke Custom Platinum Luxury Menu",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: The Lodhi / The Imperial New Delhi (Delhi, 2 Nights) | The Oberoi Amarvilas Taj View Rooms (Agra, 2 Nights) | Bespoke Custom Platinum Luxury Menu",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: Luxury accommodations in top handpicked hotels.", 1),
            _inc_included("Luxury Transportation: Private dedicated SUV for all sightseeing and transfers.", 2),
            _inc_included("Curated Meals: Daily luxury breakfast and fine-dining dinners as specified.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated travel concierge and guest assistance.", 4),
            _inc_included("Welcome Kit: Traditional welcome, customized family travel kit, and wet wipes.", 5),
            _inc_included("Complimentary Experience: Private heritage rickshaw ride through old lanes.", 6),
            _inc_excluded("Airfare, domestic flights, or train tickets to Delhi.", 7),
            _inc_excluded("Monument entry tickets, professional guide fees, or camera permits.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, drinks, and tips.", 9),
            _inc_excluded("Any optional excursions or services not specifically outlined above.", 10),
        ],
    )
    return package, itinerary


def build_dl_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-005"
    tour_code = "TRG-DEL-005"
    title = "Luxury Delhi Escape"
    duration = "04 Nights / 05 Days"
    slug = "dl-005-luxury-delhi-escape"
    itin_slug = "dl-005-luxury-delhi-escape-itinerary"
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
            _ph("State / Country: Delhi / India | Category: Luxury Holiday / Ultra-Premium Experience", 2),
            _ph("Destinations: Lutyens' Delhi • Old Delhi • Mehrauli Heritage Complex • New Delhi", 3),
            _ph("Ideal for: Connoisseurs of Heritage, High-End Corporate & Family Getaways", 4),
            _ph("Best season: October to April", 5),
            _ph("Starting price: On Request (Ultra-Luxury Customised)", 6),
            _ph("Vehicle / Meals: Chauffeur-Driven Luxury SUV / Premium Gourmet Breakfast & Dinner", 7),
            _ph(
                "Route Map: Imperial Welcome → Old Delhi Exploration → Southern Heritage → Lutyens' & Akshardham → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private, curated access to a beautiful sunset viewing point "
                "overlooking Old Delhi.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Handpicked routing designed to maximize relaxation and avoid "
                "metropolitan transit bottlenecks.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Dariba Kalan silver jewelry, Kashmiri pashminas, embroidered "
                "textiles, and bespoke brassware.",
                11,
            ),
            _ph(
                "Important Notes: Book 30-45 days ahead; dedicated vehicle for specified itinerary; check-in "
                "14:00 hrs, check-out 12:00 noon.",
                12,
            ),
        ],
        moods=["Luxury", "Heritage", "Family"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Ultra-Luxury Customised)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Luxury Delhi Escape • An Imperial Journey Through Time",
        overview=(
            "Welcome to an extraordinary exploration of India's capital, masterfully curated by TRAGUIN. This "
            "bespoke Luxury Delhi Tour Package invites you to touch the timeless majesty of an imperial city. As "
            "your professional travel consultants, TRAGUIN transforms a classic vacation into a premium luxury "
            "holiday complete with premium stays, breathtaking landscapes of manicured royal gardens, and deep "
            "historical resonance. From the legendary avenues of Old Delhi to the elegant luxury of Lutyens' "
            "structures, each second is orchestrated to offer unforgettable memories for our guests.\n\n"
            "TOUR OVERVIEW\n"
            "This elite itinerary is meticulously built for high-end FIT travellers, corporate guests, and discerning "
            "families seeking the finest immersive experiences. Traveling in an executive private luxury vehicle with a "
            "dedicated professional chauffeur, you will navigate Delhi in complete safety and unparalleled relaxation. "
            "Featuring a curated meal plan with exquisite fine dining breakfasts and special gastronomic dinners, this "
            "premium route is a definitive showcase of regal hospitality. Every day includes a specialized TRAGUIN "
            "curated experience note, bringing you custom entry permissions, behind-the-scenes historical storytelling, "
            "and around-the-clock specialized assistance.\n\n"
            "WHY CHOOSE THE BEST DELHI TOUR PACKAGE?\n"
            "When exploring a Luxury Delhi Holiday, sophisticated travelers want to experience the absolute depths "
            "of history and modern splendor. Delhi stands as an epic crossroads of dynasties, offering an exceptional "
            "backdrop for a magnificent Delhi Family Tour or a lavish, romantic Delhi Honeymoon Package. From the "
            "iconic attractions of the UNESCO-listed Humayun's Tomb and Qutub Minar to the grand architectural "
            "structures of India Gate, Delhi sightseeing offers timeless awe. This premium journey brings you straight "
            "to highly popular Instagram locations like the serene Lotus Temple, Sunder Nursery, and the majestic "
            "stepwells of Agrasen ki Baoli. Indulge in designer boutique shopping at Khan Market or the Emporio Mall, "
            "savor traditional Mughal feasts at historic culinary establishments, and dive deep into ancient heritage. "
            "Booking one of our signature TRAGUIN Delhi Packages guarantees exclusive experiences, handpicked "
            "hotels, and customized service during the absolute best time to visit Delhi."
        ),
        seo_title="DL-005 | Luxury Delhi Escape Ultra-Premium Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days luxury Delhi package (DL-005 / TRG-DEL-005): Old Delhi, Qutub Minar, "
            "Sunder Nursery, Mehrauli, Akshardham, and 4-tier ultra-luxury accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("India Gate, Kartavya Path & signature welcome dinner on Day 01", 1),
            _ih("Red Fort, Jama Masjid, Chandni Chowk & Khari Baoli on Day 02", 2),
            _ih("Qutub Minar, Humayun's Tomb, Sunder Nursery & Mehrauli sunset high tea on Day 03", 3),
            _ih("Lotus Temple, Khan Market, Akshardham water fountain show on Day 04", 4),
            _ih("Departure transfer on Day 05", 5),
            _ih("TRAGUIN Signature Experience: Private sunset viewing point overlooking Old Delhi", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Delhi | Imperial Welcome – Opulent Beginnings in the Capital",
                (
                    "Your premium Delhi experience begins as you touch down at Indira Gandhi International Airport, "
                    "where a private luxury transport vehicle stands ready to escort you. Transfer to your handpicked "
                    "premium luxury hotel in Lutyens' Delhi. After a seamless private check-in, enjoy a relaxed afternoon "
                    "tea. In the evening, visit India Gate and the beautifully lit Kartavya Path for stunning twilight "
                    "photography before experiencing a signature welcome dinner."
                ),
                [
                    "Sightseeing Included: India Gate, Kartavya Path, Rashtrapati Bhavan architecture views.",
                    "Evening Experience: Exclusive curated multi-course fine dining preview orchestrated by TRAGUIN experts.",
                    "Overnight Stay: New Delhi (Ultra-Luxury Hotel).",
                    "Meals Included: Welcome Amenities & Luxury Dinner.",
                ],
            ),
            _day(
                2,
                "Old Delhi Imperial Exploration | Chandni Chowk Chronicles & Mughal Majesty",
                (
                    "Dive deep into history with a trip to Old Delhi after a gourmet breakfast. Experience the legendary "
                    "Red Fort before entering the bustling avenues of Chandni Chowk in a private, customized rickshaw. "
                    "View the majestic Jama Masjid and explore the hidden spice markets of Khari Baoli. Stop to enjoy "
                    "high-end traditional street delicacies at historic food stands before returning to your oasis hotel "
                    "to relax and unwind."
                ),
                [
                    "Sightseeing Included: Red Fort, Jama Masjid, Chandni Chowk, Khari Baoli Spice Market.",
                    "Optional Activities: Private heritage photography tour through hidden 17th-century havelis.",
                    "Overnight Stay: New Delhi (Ultra-Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Authentic Mughal Dinner.",
                ],
            ),
            _day(
                3,
                "Southern Delhi Heritage & Architecture | Ancient Minarets, Royal Tombs & Refined Botanicals",
                (
                    "Spend a beautiful day visiting the finest archeological treasures of South Delhi. Explore the grand "
                    "Qutub Minar complex and view its exquisite ancient stone carvings. Head over to Humayun's Tomb, a "
                    "magnificent garden tomb that inspired the Taj Mahal. Take a leisurely stroll through Sunder "
                    "Nursery, a beautifully restored 16th-century heritage parkland packed with lush landscapes and "
                    "pristine monuments."
                ),
                [
                    "Sightseeing Included: Qutub Minar, Humayun's Tomb, Sunder Nursery Botanical Gardens.",
                    "Evening Experience: Private sunset high tea within the scenic beauty of the Mehrauli heritage ruins.",
                    "Overnight Stay: New Delhi (Ultra-Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Designer Contemporary Dinner.",
                ],
            ),
            _day(
                4,
                "Lutyens' Delhi & Modern Marvels | Artisan Shopping, Modern Faiths & Spiritual Splendor",
                (
                    "Explore the grand modern architecture and spiritual focal points of New Delhi. Tour the peaceful "
                    "Lotus Temple and experience its pristine marble architecture. Spend your afternoon wandering through "
                    "the National Gallery of Modern Art or shopping at the elite Khan Market. Conclude your evening with "
                    "an exclusive VIP tour of Akshardham Temple, including their premium multimedia water fountain "
                    "spectacular."
                ),
                [
                    "Sightseeing Included: Lotus Temple, Khan Market boutique lanes, Swaminarayan Akshardham Complex.",
                    "Optional Activities: Bespoke fashion consulting tour with elite luxury Indian designers at DLF Emporio.",
                    "Overnight Stay: New Delhi (Ultra-Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Grand Farewell Dinner.",
                ],
            ),
            _day(
                5,
                "Delhi Departure | Cherishing the Memories of Empires",
                (
                    "Indulge in a final, decadent buffet breakfast at your hotel. Enjoy a leisurely morning at your "
                    "resort until your private luxury vehicle transfers you directly to the airport or railway station. "
                    "Head home carrying unforgettable memories and beautiful bonds crafted meticulously by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door airport or station drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "The Grand New Delhi / Vivanta Dwarka / similar",
                "New Delhi",
                "04 Nights",
                "Deluxe",
                "Premium Deluxe Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: The Grand New Delhi / Vivanta Dwarka / similar | Premium Deluxe Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Taj Palace / Shangri-La Eros / similar",
                "New Delhi",
                "04 Nights",
                "Premium",
                "Executive City View Suite",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="OPTION 02 – PREMIUM: Taj Palace / Shangri-La Eros / similar | Executive City View Suite | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Leela Palace New Delhi / The Lodhi",
                "New Delhi",
                "04 Nights",
                "Luxury",
                "Premier Pool View Suite",
                "Premium MAPAI Luxury Package",
                5,
                3,
                description="OPTION 03 – LUXURY: The Leela Palace New Delhi / The Lodhi | Premier Pool View Suite | Premium MAPAI Luxury Package",
            ),
            _hotel(
                "The Oberoi New Delhi / Imperial Delhi",
                "New Delhi",
                "04 Nights",
                "Ultra Luxury",
                "Lutyens' View Presidential Suite",
                "Bespoke Signature Fine-Dining Plan",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: The Oberoi New Delhi / Imperial Delhi | Lutyens' View Presidential Suite | Bespoke Signature Fine-Dining Plan",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: 04 Nights accommodation in handpicked, top-tier elite properties.", 1),
            _inc_included("Luxury Transportation: Chauffeur-driven private luxury vehicle for entire tour duration.", 2),
            _inc_included("Curated Meal Plan: Daily premium breakfast and special gourmet dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest experience manager and on-ground help.", 4),
            _inc_included("Welcome Amenities: Personalized welcome kit, elite local snacks, and refreshments.", 5),
            _inc_included("Complimentary Experience: Private rickshaw safari and custom high tea in Mehrauli.", 6),
            _inc_excluded("Airfare, domestic flights, or train ticket bookings.", 7),
            _inc_excluded("Personal expenses such as laundry, telephone calls, or boutique tips.", 8),
            _inc_excluded("Monument entry tickets, professional guide fees, camera permits.", 9),
            _inc_excluded("Any optional activities, shopping expenses, or premium tours not listed.", 10),
        ],
    )
    return package, itinerary


def build_dl_006(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-006"
    tour_code = "TRG-DEL-006"
    title = "Delhi Heritage Leisure"
    duration = "03 Nights / 04 Days"
    slug = "dl-006-delhi-heritage-leisure"
    itin_slug = "dl-006-delhi-heritage-leisure-itinerary"
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
            _ph("State / Country: Delhi / India | Category: Senior Citizen Special", 2),
            _ph("Destinations: Lutyens' Delhi • Old Delhi • Qutub Complex • Akshardham", 3),
            _ph("Ideal for: Senior Citizens, Families & Leisure Travelers", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Bespoke Luxury Customised)", 6),
            _ph("Vehicle / Meals: Luxury Toyota Innova Crysta / MAPAI (Breakfast & Dinner)", 7),
            _ph(
                "Route Map: Imperial Comfort → Old Delhi Rickshaw → Qutub & Akshardham → Shopping & Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private family interaction and history briefing prior to monument tours.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Custom-paced, relaxed travel loops prioritizing safety and avoiding rush hours.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Central Cottage Industries Emporium for silk scarves, sandalwood "
                "carvings, Indian tea, and brass oil lamps.",
                11,
            ),
            _ph(
                "Important Notes: Check-in 14:00 hrs, check-out 11:00 hrs; woolens Nov-Jan; book wheelchair-accessible "
                "rooms 30 days ahead.",
                12,
            ),
        ],
        moods=["Family", "Heritage", "Leisure"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Bespoke Luxury Customised)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Delhi Heritage Leisure • A Slow-Paced Regal Experience",
        overview=(
            "Welcome to an expertly paced, majestic journey through India's capital city, curated exclusively by "
            "TRAGUIN. This bespoke Delhi Family Tour is specifically optimized as a serene, relaxed Delhi Heritage "
            "Leisure experience for senior citizens who wish to explore the magnificent history of the capital without "
            "physical strain. As your dedicated luxury travel consultants, TRAGUIN transforms your stay into an "
            "unforgettable memory featuring premium stays, wheelchair-accessible pathways, and a highly courteous "
            "chauffeur. Witness the iconic attractions and historic monuments of Delhi unfold before you in complete "
            "tranquility.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored luxury holiday package focuses on premium comfort, slow-paced travel loops, and "
            "smooth point-to-point transitions. Travel in an ultra-luxurious, spacious AC sedan or MUV with a "
            "professional chauffeur specializing in senior-citizen assistance. Featuring a curated meal plan with "
            "nutritious breakfast and dinner layouts at handpicked hotels, this specific route minimizes walking and "
            "maximizes comfort. Every fine detail incorporates the signature touch of TRAGUIN curated experiences, "
            "including pre-booked monument entry passes, premium seating arrangements, and dedicated local travel "
            "assistant support.\n\n"
            "WHY CHOOSE THE BEST DELHI TOUR PACKAGE?\n"
            "When exploring a Luxury Delhi Holiday, travelers seek the fine line where majestic ancient architecture "
            "perfectly intertwines with modern Indian hospitality. This meticulously structured itinerary offers the "
            "ultimate Premium Delhi Experience. Delhi is a city of layers, boasting iconic attractions that range from "
            "the serene, beautifully manicured gardens of Lutyens' Delhi to the towering stone masonry of the Qutub "
            "Minar—a top tourist place in Delhi. For couples and generations looking for a balanced Delhi Honeymoon "
            "Package or an multi-generational Delhi Family Tour, the city presents beautiful Instagram locations such "
            "as the peaceful Lotus Temple and the grand architecture of Akshardham Temple. Whether you wish to enjoy "
            "cultural shopping at state emporiums, sample delicate rich heritage foods, or appreciate the historic "
            "spiritual tranquility of Bangla Sahib, booking our TRAGUIN Delhi Packages guarantees the best time to "
            "visit Delhi with unparalleled relaxation."
        ),
        seo_title="DL-006 | Delhi Heritage Leisure Senior Citizen Tour | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days senior-friendly Delhi package (DL-006 / TRG-DEL-006): Lutyens' Delhi, "
            "Old Delhi rickshaw, Qutub Minar, Akshardham, and 4-tier accessible accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("India Gate, Rashtrapati Bhavan, National War Memorial & Lodi Gardens on Day 01", 1),
            _ih("Red Fort, Chandni Chowk rickshaw, Gurudwara Bangla Sahib on Day 02", 2),
            _ih("Qutub Complex, Humayun's Tomb & Akshardham fountain show on Day 03", 3),
            _ih("Connaught Place shopping & departure on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Private family history briefing before monument tours", 5),
            _ih("Luxury Transportation: Patient drivers trained in senior citizen assistance", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Delhi & Imperial Comfort | Welcome to the Imperial Capital – Lutyens' Rajpath Drive",
                (
                    "Your premium Delhi experience begins with a seamless VIP pickup from New Delhi Airport or "
                    "Railway Station. Your dedicated luxury transportation vehicle will smoothly transfer you to your "
                    "handpicked premium hotel. After a relaxed check-in and lunch, enjoy a comfortable, smooth drive "
                    "past the architectural highlights of Lutyens' Delhi, including the spectacular India Gate, "
                    "Rashtrapati Bhavan, and Parliament House. Beautifully paved walkways make this an iconic "
                    "photography point for senior citizens."
                ),
                [
                    "Sightseeing Included: India Gate drive-through, Rashtrapati Bhavan lawns view, National War Memorial layout.",
                    "Evening Experience: A relaxed stroll or sitting at the lush, scenic beauty of Lodi Gardens, followed by gourmet dinner.",
                    "Overnight Stay: New Delhi (Premium / Ultra-Luxury Hotel).",
                    "Meals Included: Welcome High-Tea & Luxury Dinner.",
                ],
            ),
            _day(
                2,
                "Historic Old Delhi Exploration | Old World Charm – Traditional Comfortable Rickshaw Ride",
                (
                    "Indulge in a premium breakfast before heading to Old Delhi for a nostalgic look at the city's "
                    "heritage. To ensure maximum comfort and completely avoid walking through crowds, TRAGUIN has "
                    "arranged private, cushioned cycle rickshaws to take you past Chandni Chowk and the historic red "
                    "sandstone walls of the Red Fort. Conclude the morning with a spiritually uplifting visit to the "
                    "serene Gurudwara Bangla Sahib, where you can listen to peaceful hymns by the holy Sarovar lake."
                ),
                [
                    "Sightseeing Included: Red Fort (outer view), Raj Ghat, Chandni Chowk heritage loop, Gurudwara Bangla Sahib.",
                    "Optional Activities: A curated luxury lunchtime dining experience at a converted heritage haveli.",
                    "Overnight Stay: New Delhi (Premium / Ultra-Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Dinner.",
                ],
            ),
            _day(
                3,
                "Architectural Spectacles of South Delhi | Ancient Wonders & Spiritual Grandeur",
                (
                    "Following a leisurely breakfast, journey to South Delhi to admire the majestic Qutub Minar, "
                    "featuring smooth, wheel-chair accessible walking ramps. Next, visit the architectural masterpiece "
                    "of Humayun's Tomb, beautifully surrounded by symmetrical Mughal gardens and gentle water "
                    "channels. In the afternoon, explore the grand Swaminarayan Akshardham Temple complex to witness its "
                    "incredible stone carvings and enjoy a comfortable indoor exhibition cruise."
                ),
                [
                    "Sightseeing Included: Qutub Complex monument trails, Humayun's Tomb, Akshardham cultural complex.",
                    "Evening Experience: Musical fountain show at Akshardham Temple with special reserved seating.",
                    "Overnight Stay: New Delhi (Premium / Ultra-Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Festive Farewell Dinner.",
                ],
            ),
            _day(
                4,
                "Cultural Shopping & Departure | Souvenir Hunting – Cherishing Unforgettable Memories",
                (
                    "Savor your last morning breakfast at your premium hotel before checking out. Visit Connaught "
                    "Place or Baba Kharak Singh Marg Emporiums for a quiet, comfortable shopping experience to pick "
                    "up authentic Indian handicrafts and textiles. Your private luxury transport will then drive you "
                    "comfortably to New Delhi Airport or Railway Station. Return home carrying beautiful stories and "
                    "unforgettable memories tailored beautifully by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door departure drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "The Suryaa New Delhi / Vivanta Dwarka",
                "New Delhi",
                "03 Nights",
                "Deluxe",
                "Executive Premium Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: The Suryaa New Delhi / Vivanta Dwarka | Executive Premium Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Crowne Plaza Okhla / Eros Hotel Nehru Place",
                "New Delhi",
                "03 Nights",
                "Premium",
                "Luxury Club Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="OPTION 02 – PREMIUM: Crowne Plaza Okhla / Eros Hotel Nehru Place | Luxury Club Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Taj Mahal Hotel / The Leela Palace New Delhi",
                "New Delhi",
                "03 Nights",
                "Luxury",
                "Grand Deluxe City View Room",
                "MAPAI + Senior Care Welcome Kit",
                5,
                3,
                description="OPTION 03 – LUXURY: The Taj Mahal Hotel / The Leela Palace New Delhi | Grand Deluxe City View Room | MAPAI + Senior Care Welcome Kit",
            ),
            _hotel(
                "The Oberoi New Delhi / Imperial Hotel Lutyens'",
                "New Delhi",
                "03 Nights",
                "Ultra Luxury",
                "VVIP Premier Heritage Luxury Suite",
                "Signature Bespoke Gourmet MAPAI",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: The Oberoi New Delhi / Imperial Hotel Lutyens' | VVIP Premier Heritage Luxury Suite | Signature Bespoke Gourmet MAPAI",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: 03 Nights in top-rated hotels offering wheelchair and step-free access.", 1),
            _inc_included("Luxury Transportation: Chauffeur-driven AC Toyota Innova Crysta for all transfers.", 2),
            _inc_included("Curated Meal Plan: Lavish daily breakfasts and specialized low-spice dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated guest manager with senior care briefing.", 4),
            _inc_included("Welcome Amenities: Personalized travel kit containing healthy snacks and herbal drinks.", 5),
            _inc_included("Complimentary Experience: Private, cushioned cycle rickshaw ride through Old Delhi.", 6),
            _inc_excluded("Airfare, flight bookings, or mainline train ticket charges.", 7),
            _inc_excluded("Monument entry fees, camera passes, and local tour guide fees.", 8),
            _inc_excluded("Personal expenses such as laundry services, phone calls, or tips.", 9),
            _inc_excluded("Any medical equipment rentals or specialized single-nurse assistance.", 10),
        ],
    )
    return package, itinerary


def build_dl_007(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-007"
    tour_code = "TRG-DEL-MICE-007"
    title = "Corporate Delhi MICE"
    duration = "03 Nights / 04 Days"
    slug = "dl-007-corporate-delhi-mice"
    itin_slug = "dl-007-corporate-delhi-mice-itinerary"
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
            _ph("State / Country: Delhi / India | Category: MICE / Corporate Presentation", 2),
            _ph("Destinations: New Delhi • Lutyens' Zone • Aerocity • Connaught Place • Old Delhi", 3),
            _ph("Ideal for: Corporate Conferences, Team Building & Leadership Retreats", 4),
            _ph("Best season: October to March (Ideal Corporate Event Windows)", 5),
            _ph("Starting price: On Request (Premium Corporate B2B Rates)", 6),
            _ph("Vehicle / Meals: Luxury Multi-Axle Coaches / MAPAI (With Gala Dinner Extravaganza)", 7),
            _ph(
                "Route Map: Aerocity Check-in → Power Conference & Lutyens' → Heritage & Gala Night → "
                "Corporate Shopping & Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private corporate branding integrated throughout the luxury fleet "
                "and banquet venues.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Tailored timing schedules to ensure absolute corporate productivity "
                "without fatigue.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: State Emporiums at Connaught Place for hand-loomed textiles, brass "
                "items, and blue pottery corporate gifts.",
                11,
            ),
            _ph(
                "Important Notes: Corporate authorization letters required; finalize contracts 60 days ahead; coaches "
                "follow Lutyens' traffic timelines.",
                12,
            ),
        ],
        moods=["Corporate", "MICE", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Corporate B2B Rates)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Corporate Delhi MICE • Legacy, Innovation & Networking",
        overview=(
            "Welcome to an elite corporate experience curated exclusively by TRAGUIN. Presenting the ultimate "
            "Corporate Delhi MICE itinerary, engineered precisely to combine strategic business objectives with top-tier "
            "luxury. As your premier business travel consultants, TRAGUIN elevates your company retreat into a world-"
            "class luxury holiday featuring premium stays, seamless convention spaces, and high-energy team building "
            "sessions. Witness the perfect harmony of historic power centers and cutting-edge corporate infrastructure, "
            "creating unforgettable memories and deeper professional bonds for your entire team.\n\n"
            "TOUR OVERVIEW\n"
            "This custom-tailored luxury holiday proposal is designed for high-performing corporate teams, dealers, and "
            "executive boards. Moving fluidly through the nation's capital in dedicated premium luxury transportation "
            "with around-the-clock concierge assistance, your group will experience unparalleled logistical efficiency. "
            "Featuring a highly selective premium meal plan including expansive business breakfasts, formal working "
            "lunches, and customized gala themed dinners, this journey sets the gold standard for a premium Delhi "
            "experience. Every detail includes the signature touch of TRAGUIN curated experiences, assuring flawless "
            "presentation, high-end production integration, and seamless VIP management.\n\n"
            "WHY CHOOSE THE BEST DELHI TOUR PACKAGE FOR MICE?\n"
            "When evaluating the Best Delhi Tour Package for upscale corporate events, corporate planners require far "
            "more than standard itineraries. They require a balanced blend of professional convention space, historical "
            "prestige, and fine dining. New Delhi serves as the geopolitical heart of the country, making a Luxury "
            "Delhi Holiday the definitive choice for executive retreats, global assemblies, and rewards programs. From "
            "iconic attractions like India Gate and Rashtrapati Bhavan to contemporary business hubs like Aerocity, "
            "Delhi sightseeing delivers an inspiring sense of scale. For organizations searching for an impactful Delhi "
            "Family Tour extension or an elegant Delhi Honeymoon Package style reward for top executives, the capital "
            "provides access to famous Instagram locations like Sunder Nursery and Lodhi Art District. Whether "
            "participating in private heritage walks through Old Delhi, indulging in corporate gifting shopping at "
            "Connaught Place, or hosting high-profile banquets, our TRAGUIN Delhi Packages offer handpicked hotels, "
            "meticulous scheduling, and curated exclusive experiences during the best time to visit Delhi."
        ),
        seo_title="DL-007 | Corporate Delhi MICE Premium Retreat | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days corporate Delhi MICE package (DL-007 / TRG-DEL-MICE-007): Aerocity "
            "conferences, Lutyens' sightseeing, Old Delhi heritage, gala night, and 4-tier MICE hotels."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Aerocity check-in, ice-breaking session & networking dinner on Day 01", 1),
            _ih("Corporate conference, India Gate & National War Memorial on Day 02", 2),
            _ih("Old Delhi heritage rickshaw tour & TRAGUIN Gala Extravaganza on Day 03", 3),
            _ih("Corporate gifting shopping & departure on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Corporate branding across luxury fleet and banquet venues", 5),
            _ih("Premium Handpicked Hotels: Superior Wi-Fi and high-capacity ballrooms", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Delhi & Aerocity Check-in | Welcome to the Seat of Power – The Ultimate Corporate Convergence",
                (
                    "Your premium Delhi experience commences with a warm VIP reception at Indira Gandhi International "
                    "Airport by the TRAGUIN corporate logistics squad. Board your dedicated luxury transportation "
                    "coaches and transfer to your handpicked ultra-luxury hotel in Aerocity. After a smooth corporate "
                    "group check-in, host an elite afternoon ice-breaking session in a premium state-of-the-art "
                    "boardroom. Wrap up the day with a high-end networking reception at an exclusive open-air lounge."
                ),
                [
                    "Sightseeing Included: Aerocity upscale commercial promenade, curated executive lounge access.",
                    "Evening Experience: High-level corporate ice-breaker cocktail dinner with professional sound & lighting infrastructure.",
                    "Overnight Stay: New Delhi Aerocity (Ultra-Luxury Hotel Category).",
                    "Meals Included: Welcome Amenities, High Tea & Corporate Networking Dinner.",
                ],
            ),
            _day(
                2,
                "Power Conference & Lutyens' Sightseeing | Strategic Symposiums & Iconic Architectural Landmarks",
                (
                    "Begin your morning with a grand buffet breakfast, followed by your main annual corporate "
                    "conference inside a magnificent pillarless ballroom. TRAGUIN experts provide comprehensive "
                    "audio-visual assistance and seamless registration desks. In the afternoon, transition into an "
                    "immersive experience across Lutyens' Delhi. Enjoy private, chauffeur-driven transfers around the "
                    "iconic attractions of India Gate, Parliament House, and Rashtrapati Bhavan, offering excellent "
                    "photography points for corporate group portraits."
                ),
                [
                    "Sightseeing Included: Drive-past of Rashtrapati Bhavan & Parliament, stopping at India Gate and National War Memorial.",
                    "Optional Activities: Interactive leadership team building exercises on manicured lawns or indoor experiential simulations.",
                    "Overnight Stay: New Delhi Aerocity / Central Delhi Luxury Property.",
                    "Meals Included: Premium Working Breakfast, Business Lunch & Formal Table Dinner.",
                ],
            ),
            _day(
                3,
                "Heritage Inspiration & Gala Night | Emotional Storytelling in Old Delhi & A Celebrity Gala Retreat",
                (
                    "Indulge in a premium breakfast before heading to Old Delhi for an enriching heritage experience. "
                    "Experience a safely managed, private rickshaw tour through the historic streets of Chandni Chowk and "
                    "view the majestic Red Fort. This historic journey serves as an inspiring lesson in resilience and "
                    "legacy. In the evening, get ready for the grand TRAGUIN Signature Gala Night, featuring award "
                    "distributions, live entertainment, and an unforgettable gourmet experience."
                ),
                [
                    "Sightseeing Included: Red Fort (outer view), Chandni Chowk, Khari Baoli, Connaught Place shopping blocks.",
                    "Evening Experience: TRAGUIN Gala Extravaganza: Custom branding backdrops, award ceremonies, and live musical entertainment.",
                    "Overnight Stay: New Delhi Luxury Property.",
                    "Meals Included: Premium Breakfast, Traditional Local Lunch & Luxury Gala Dinner.",
                ],
            ),
            _day(
                4,
                "Shopping Excursion & Corporate Departure | Cherishing Team Milestones & Rewarding Journeys",
                (
                    "Savor a final lavish breakfast at your premium stay. Utilize your morning for upscale corporate "
                    "gifting shopping at the famous state emporiums on Baba Kharak Singh Marg or visit top tourist "
                    "places in Delhi like Qutub Minar for premium photography points. In the afternoon, board your "
                    "private luxury transportation for a smooth transfer to the airport or railway station. Return home "
                    "carrying shared team triumphs and unforgettable memories beautifully organized by TRAGUIN."
                ),
                [
                    "Transfers Included: End-to-end luxury coach drop-offs with airport luggage assistance.",
                    "Meals Included: Lavish International Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Novotel Aerocity / Pride Plaza Delhi / similar",
                "Aerocity & Central Delhi",
                "03 Nights",
                "Deluxe",
                "Superior Business Room",
                "MAPAI | Standard Conference Hall Setup",
                4,
                1,
                description="OPTION 01 – DELUXE: Novotel Aerocity / Pride Plaza Delhi / similar | Superior Business Room | Standard Conference Hall Setup",
            ),
            _hotel(
                "Pullman Aerocity / Andaz Delhi / similar",
                "Aerocity & Central Delhi",
                "03 Nights",
                "Premium",
                "Premium Runway View Room",
                "MAPAI | Pillarless Ballroom Access",
                5,
                2,
                description="OPTION 02 – PREMIUM: Pullman Aerocity / Andaz Delhi / similar | Premium Runway View Room | Pillarless Ballroom Access",
            ),
            _hotel(
                "JW Marriott Aerocity / Leela Palace New Delhi",
                "Aerocity & Central Delhi",
                "03 Nights",
                "Luxury",
                "Deluxe Executive Suite",
                "MAPAI | VIP Lounge & Custom Dining Areas",
                5,
                3,
                description="OPTION 03 – LUXURY: JW Marriott Aerocity / Leela Palace New Delhi | Deluxe Executive Suite | VIP Lounge & Custom Dining Areas",
            ),
            _hotel(
                "The Roseate New Delhi / The Taj Mahal Hotel Mansingh",
                "Aerocity & Central Delhi",
                "03 Nights",
                "Ultra Luxury",
                "VVIP Ultra-Luxury Villa / Presidential Suite",
                "MAPAI | Bespoke Corporate Event Production",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: The Roseate New Delhi / The Taj Mahal Hotel Mansingh | VVIP Ultra-Luxury Villa / Presidential Suite | Bespoke Corporate Event Production",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: 03 Nights in top-tier luxury hotels with business amenities.", 1),
            _inc_included("Luxury Transportation: High-end air-conditioned multi-axle corporate coaches.", 2),
            _inc_included("Curated Meal Plan: Daily lavish breakfasts, lunches, and high-end gala dinners.", 3),
            _inc_included("TRAGUIN Support: On-site event managers and dedicated corporate help desk.", 4),
            _inc_included("Welcome Amenities: Customized corporate welcome kits and branding materials.", 5),
            _inc_included("Complimentary Experiences: Private heritage rickshaw tour and curated cultural evening.", 6),
            _inc_excluded("Domestic or International airfares and ticketing taxes.", 7),
            _inc_excluded("Extra alcoholic beverages or customized premium bar menus during dinners.", 8),
            _inc_excluded("Personal resort expenses such as laundry, spa therapies, or room service.", 9),
            _inc_excluded("Professional artist bookings or external motivational speaker honorariums.", 10),
        ],
    )
    return package, itinerary


def build_dl_008(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-008"
    tour_code = "TRG-DEL-008"
    title = "Delhi Shopping Tour"
    duration = "03 Nights / 04 Days"
    slug = "dl-008-delhi-shopping-tour"
    itin_slug = "dl-008-delhi-shopping-tour-itinerary"
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
            _ph("State / Country: Delhi / India | Category: Premium Family Shopping Tour", 2),
            _ph("Destinations: Connaught Place • Chandni Chowk • Khan Market • Dilli Haat • South Extension", 3),
            _ph("Ideal for: Connoisseurs, Fashion Seekers & Families", 4),
            _ph("Best season: October to March (Pleasant Shopping Weather)", 5),
            _ph("Starting price: On Request (Premium Tailor-made Luxury Plan)", 6),
            _ph("Vehicle / Meals: Private Luxury SUV / MAPAI (Breakfast & Dinner)", 7),
            _ph(
                "Route Map: Connaught Place & Khan Market → Chandni Chowk & Emporio → Dilli Haat & South Extension → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private family insider guide map highlighting famous antique shops "
                "and hidden silk stores.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Perfect route management ensuring seamless pick-up and drop-offs "
                "at busy market entries.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Chandni Chowk bridal couture; Khan Market lifestyle; Dilli Haat "
                "silver jewelry, tribal arts, pashminas.",
                11,
            ),
            _ph(
                "Important Notes: Check-in 14:00 hrs, check-out 11:00 hrs; markets closed Sun/Mon may adjust "
                "schedule; book 30 days ahead.",
                12,
            ),
        ],
        moods=["Shopping", "Family", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Tailor-made Luxury Plan)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Delhi Shopping Tour • Ultimate Retail Luxury Escape",
        overview=(
            "Welcome to a shopping extravaganza crafted meticulously by TRAGUIN. This exclusive Delhi Family Tour "
            "opens the doors to the finest high-end boutiques, legendary heritage bazaars, and contemporary haute "
            "couture hubs. As your premier luxury travel consultants, TRAGUIN ensures your experience is enhanced "
            "with premium stays, seamless transfers, and deep local insight. Immerse yourselves in the vivid colors "
            "and premium retail layers of India's capital city, transforming your holiday into a series of beautiful, "
            "unforgettable memories.\n\n"
            "TOUR OVERVIEW\n"
            "This elite corporate presentation style itinerary is thoughtfully designed for family groups seeking a "
            "perfect blend of high-end indulgence and historic charm. Traveling inside a private luxury SUV alongside "
            "a highly experienced, professional uniform-clad chauffeur, you will easily glide past metropolitan "
            "traffic. With customized lunch maps and pre-reserved tables at world-class restaurants, your days "
            "remain structured and perfectly balanced. Every moment includes a unique TRAGUIN curated experience "
            "note, ensuring complete comfort, priority assistance, and personalized shopping guides.\n\n"
            "WHY CHOOSE THE BEST DELHI TOUR PACKAGE?\n"
            "When shortlisting a Luxury Delhi Holiday, a passionate traveler seeks a flawless balance between "
            "historical depth and absolute comfort. Delhi stands proudly as India's ultimate retail capital, making a "
            "premium Delhi Shopping Tour an exceptional choice for families and bridal look seekers. From exploring "
            "the labyrinthine lanes of Old Delhi's historic spice markets to navigating the sophisticated rows of "
            "globally praised designer showrooms, Delhi sightseeing unfolds a marvelous story of trade and artistry. "
            "For discerning couples or larger groups picking out a customized Delhi Honeymoon Package or Delhi "
            "Family Tour, the city highlights extremely popular Instagram locations such as Sunder Nursery, the "
            "elegant arches of Connaught Place, and the colorful artisan stalls of Dilli Haat. Discover intricate "
            "traditional wedding jewelry, buy magnificent Kashmiri shawls, or treat your family to iconic fine dining. "
            "Our signature TRAGUIN Delhi Packages promise handpicked hotels, highly exclusive experiences, and "
            "refined assistance during the best time to visit Delhi."
        ),
        seo_title="DL-008 | Delhi Shopping Tour Premium Retail Escape | TRAGUIN",
        seo_description=(
            "Premium 03 Nights / 04 Days Delhi shopping package (DL-008 / TRG-DEL-008): Connaught Place, "
            "Chandni Chowk, DLF Emporio, Dilli Haat, South Extension, and 4-tier luxury accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Connaught Place inner circle & Khan Market on Day 01", 1),
            _ih("Chandni Chowk, Dariba Kalan, Kinari Bazaar & DLF Emporio on Day 02", 2),
            _ih("Dilli Haat craft village & South Extension couture on Day 03", 3),
            _ih("Final souvenir shopping & departure on Day 04", 4),
            _ih("TRAGUIN Signature Experience: Private insider guide map for antique shops and silk stores", 5),
            _ih("Personalized Assistance: Package management and delivery coordination support", 6),
        ],
        days=[
            _day(
                1,
                "Arrival & Heritage Chic | Connaught Place & Emerald Khan Market Lounging",
                (
                    "Your premium journey starts the moment you land, with a warm greeting at New Delhi Airport by a "
                    "personal chauffeur-driven luxury vehicle. After checking into your premium handpicked hotel, drive "
                    "down the wider boulevard lines toward Connaught Place—a beautiful colonial-era masterpiece of "
                    "white arches and premium luxury boutiques. Spend your late afternoon browsing premium Indian "
                    "labels at Khan Market, a globally renowned high street. Enjoy excellent opportunities for vintage "
                    "photography, or unwind at a luxury artisan café."
                ),
                [
                    "Sightseeing Included: Connaught Place inner circle, Khan Market high-end lifestyle stroll.",
                    "Evening Experience: A welcome dinner and curated orientation session hosted inside a premium heritage lounge.",
                    "Overnight Stay: New Delhi (Ultra Luxury Hotel Option).",
                    "Meals Included: Welcome Drink & Fine-Dining Dinner.",
                ],
            ),
            _day(
                2,
                "Couture & Old World Charm | Chandni Chowk Royal Bazaars & Emporio Luxury",
                (
                    "Indulge in a magnificent breakfast before experiencing the old-world majesty of Old Delhi. Travel "
                    "by private, eco-friendly luxury cycle-rickshaws through the lanes of Chandni Chowk, Dariba Kalan "
                    "(The Street of Silver), and Kinari Bazaar. Witness dazzling wedding couture and traditional "
                    "embroideries. In the afternoon, shift to the modern world at DLF Emporio mall in Vasant Kunj—"
                    "India's primary temple of international luxury brands and master Indian couturiers."
                ),
                [
                    "Sightseeing Included: Chandni Chowk, Spice Market overlooks, DLF Emporio Luxury Pavilion.",
                    "Food Suggestions: Savor legendary Mughlai delicacies or experience highly elevated modern Indian street food.",
                    "Overnight Stay: New Delhi (Ultra Luxury Hotel Option).",
                    "Meals Included: Premium Breakfast & Crafted Dinner.",
                ],
            ),
            _day(
                3,
                "Ethnic Masterpieces & High Fashion | Dilli Haat Artisans & South Extension Couture Spree",
                (
                    "Dedicate your morning to the scenic beauty and vibrant craft stalls of Dilli Haat, an open-air "
                    "food and craft plaza. Handpicked by TRAGUIN experts for its cultural richness, you can purchase "
                    "authentic pashmina shawls, rosewood carvings, and silk sarees directly from national award-winning "
                    "master weavers. In the afternoon, explore South Extension or Greater Kailash markets to browse "
                    "stunning jewelry galleries and premium designer studios."
                ),
                [
                    "Sightseeing Included: Dilli Haat craft village, South Extension couture high street.",
                    "Photography Points: Vibrant handicraft stalls and beautiful architectural backgrounds of South Delhi.",
                    "Overnight Stay: New Delhi (Ultra Luxury Hotel Option).",
                    "Meals Included: Premium Breakfast & Special Celebration Dinner.",
                ],
            ),
            _day(
                4,
                "Departure with Treasures | Souvenir Finals & Farewell Transfers",
                (
                    "Enjoy a final luxury breakfast at your hotel. Spend your morning at leisure collecting last-minute "
                    "boutique souvenirs or fine teas. Your private luxury transport will safely drive you to New Delhi "
                    "Airport or the railway station for your onward journey. Return home carrying premium treasures and "
                    "unforgettable memories designed beautifully by TRAGUIN."
                ),
                [
                    "Transfers Included: Private door-to-door luxury airport terminal drop-off.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "Radisson Blu Plaza / Vivanta Dwarka / similar",
                "New Delhi",
                "03 Nights",
                "Deluxe",
                "Superior Executive Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: Radisson Blu Plaza / Vivanta Dwarka / similar | Superior Executive Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Eros Hotel Nehru Place / Hyatt Regency",
                "New Delhi",
                "03 Nights",
                "Premium",
                "Premium City View Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="OPTION 02 – PREMIUM: The Eros Hotel Nehru Place / Hyatt Regency | Premium City View Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Taj Mahal Hotel (Mansingh Road) / ITC Maurya",
                "New Delhi",
                "03 Nights",
                "Luxury",
                "Luxury Heritage Club Room",
                "MAPAI + Executive Lounge Access",
                5,
                3,
                description="OPTION 03 – LUXURY: The Taj Mahal Hotel (Mansingh Road) / ITC Maurya | Luxury Heritage Club Room | MAPAI + Executive Lounge Access",
            ),
            _hotel(
                "The Leela Palace New Delhi / The Oberoi New Delhi",
                "New Delhi",
                "03 Nights",
                "Ultra Luxury",
                "Grand Deluxe Royal Suite",
                "Bespoke Gourmet Dine-around MAPAI",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: The Leela Palace New Delhi / The Oberoi New Delhi | Grand Deluxe Royal Suite | Bespoke Gourmet Dine-around MAPAI",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: 03 Nights accommodation in selected elite properties.", 1),
            _inc_included("Luxury Transportation: Chauffeur-driven luxury vehicle for all routing.", 2),
            _inc_included("Curated Meal Plan: Lavish daily breakfasts and fine dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 dedicated concierge desk on call.", 4),
            _inc_included("Welcome Amenities: Customized family luxury welcome kit and shopping map.", 5),
            _inc_included("Complimentary Experience: Private heritage rickshaw ride through Chandni Chowk bazaars.", 6),
            _inc_excluded("Airfare, flight upgrades, or long-distance train tickets.", 7),
            _inc_excluded("Direct purchases, shopping bills, and tailoring charges.", 8),
            _inc_excluded("Monument entry tickets, commercial video permissions, camera fees.", 9),
            _inc_excluded("Personal expenses such as laundry, phone calls, or tips.", 10),
        ],
    )
    return package, itinerary


def build_dl_009(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-009"
    tour_code = "TRG-DEL-009"
    title = "Mughal Delhi Trail"
    duration = "04 Nights / 05 Days"
    slug = "dl-009-mughal-delhi-trail"
    itin_slug = "dl-009-mughal-delhi-trail-itinerary"
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
            _ph("State / Country: Delhi / India | Category: Heritage Explorer", 2),
            _ph("Destinations: Old Delhi • New Delhi • Mehrauli Heritage Zone", 3),
            _ph("Ideal for: History Connoisseurs, Family Vacations & Luxury Seekers", 4),
            _ph("Best season: October to March", 5),
            _ph("Starting price: On Request (Premium Bespoke)", 6),
            _ph("Vehicle / Meals: Luxury Chauffeur Sedan / MAPAI (Breakfast & Dinner)", 7),
            _ph(
                "Route Map: Imperial Landing → Old Delhi Heritage → Garden Tombs & Akshardham → "
                "Qutub Minar & Connaught Place → Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private, guided evening culinary stroll highlighting Delhi's "
                "storied historic food culture.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Custom routing designed to bypass typical city congestion, "
                "giving you more time to relax.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Dariba Kalan silver jewelry, pashminas at Connaught Place, "
                "designer bridal fashion in Shahpur Jat, Dilli Haat arts.",
                11,
            ),
            _ph(
                "Important Notes: Check-in 14:00 hrs, check-out 12:00 noon; autumn to spring ideal; confirm "
                "hotel allocations 30 days ahead.",
                12,
            ),
        ],
        moods=["Heritage", "Family", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Bespoke)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Mughal Delhi Trail • Echoes of Imperial Opulence",
        overview=(
            "Welcome to an unforgettable journey into the heart of India's capital, masterfully curated by TRAGUIN. "
            "This bespoke Mughal Delhi Trail is crafted to immerse you in the sweeping romance, architectural "
            "timelessness, and majestic legacy of old imperial empires. As your dedicated luxury travel consultants, "
            "TRAGUIN brings you a premium Delhi experience that transforms historical exploration into a seamless, "
            "guest-facing masterpiece. From the labyrinthine corridors of Old Delhi to the sprawling manicured avenues "
            "of New Delhi, prepare to collect unforgettable memories framed by breathtaking landscapes and iconic "
            "attractions.\n\n"
            "TOUR OVERVIEW\n"
            "This elite corporate-ready proposal presents a fine luxury holiday designed for discerning travellers who "
            "demand uncompromising sophistication. Your travel dates will be paired with an independent FIT model "
            "utilizing a high-end, private, chauffeur-driven luxury vehicle for effortless transit. The comprehensive "
            "meal plan features lavish artisanal breakfasts paired with curated heritage dinners. Following a majestic "
            "historical route, this package includes unique TRAGUIN curated experiences—from skip-the-line VIP entries "
            "to personal culinary historians, ensuring an elite, immersive experience across India's historical heart.\n\n"
            "WHY CHOOSE THE BEST DELHI TOUR PACKAGE?\n"
            "When exploring the possibility of a Luxury Delhi Holiday, experienced global travelers seek a precise "
            "balance of sensory storytelling and uncompromised comfort. Delhi stands as an epic open-air museum where "
            "ancient history effortlessly intersects with high-end cosmopolitan living. A curated Delhi Honeymoon "
            "Package or Delhi Family Tour allows couples and families to wander through architectural timelessness, "
            "admiring top tourist places in Delhi that have defined the subcontinent for generations. The city features "
            "an array of popular Instagram locations, from the symmetry of Humayun's Tomb to the iconic sandstone "
            "arches of India Gate and the towering peak of Qutub Minar. Beyond the classic Delhi sightseeing trails, "
            "guests can explore vibrant world-renowned street food enclaves, luxury designer boutiques, and deep "
            "spiritual heritage sites. Utilizing our signature TRAGUIN Delhi Packages guarantees exclusive experiences, "
            "handpicked hotels, and customized local insight, making any time the best time to visit Delhi when "
            "traveling with our elite assistance."
        ),
        seo_title="DL-009 | Mughal Delhi Trail Heritage Explorer | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Mughal Delhi package (DL-009 / TRG-DEL-009): Red Fort, Chandni Chowk, "
            "Humayun's Tomb, Lodi Gardens, Qutub Minar, Akshardham, and 4-tier premium accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("India Gate, Rashtrapati Bhavan & welcome high-tea on Day 01", 1),
            _ih("Red Fort, Jama Masjid, Chandni Chowk & Khari Baoli on Day 02", 2),
            _ih("Humayun's Tomb, Lodi Gardens & Akshardham fountain show on Day 03", 3),
            _ih("Qutub Minar, Mehrauli Archaeological Park & Connaught Place on Day 04", 4),
            _ih("Departure transfer on Day 05", 5),
            _ih("TRAGUIN Signature Experience: Private evening culinary stroll of historic food culture", 6),
        ],
        days=[
            _day(
                1,
                "Arrival in Delhi | Welcome to the Imperial Capital – Luxury Landing",
                (
                    "Your premium Delhi experience begins with a royal welcome. As you touch down at Indira Gandhi "
                    "International Airport, a private luxury transportation vehicle awaits to transport you smoothly "
                    "to your handpicked premium stay. After checking in and enjoying a curated welcome amenity, spend "
                    "your afternoon relaxing. In the evening, your personal chauffeur will drive you down the "
                    "monumental ceremonial avenue of Rajpath, pausing at India Gate for an evening photography session "
                    "as the structure illuminates beautifully against the twilight sky."
                ),
                [
                    "Sightseeing Included: India Gate, Rashtrapati Bhavan exterior drive, National War Memorial layout.",
                    "Evening Experience: A bespoke welcome orientation and high-tea experience arranged by TRAGUIN experts.",
                    "Overnight Stay: New Delhi (Handpicked 5-Star Luxury Hotel).",
                    "Meals Included: Welcome Drink & Fine-dining Dinner.",
                ],
            ),
            _day(
                2,
                "Old Delhi Heritage Trail | Shahjahanabad – Mughal Majesty & Vibrant Bazaars",
                (
                    "Dive deep into the historic realm of the Mughal empire. Following a gourmet breakfast, travel to "
                    "Old Delhi for a private, customized cycle-rickshaw ride through Chandni Chowk's chaotic and historic "
                    "streets. Stand before the towering red sandstone walls of the iconic Red Fort, built by Emperor "
                    "Shah Jahan. Walk through the tranquil courtyard of Jama Masjid, one of the largest mosques in "
                    "India, before stopping for an emotional storytelling culinary tour of authentic Old Delhi flavors."
                ),
                [
                    "Sightseeing Included: Red Fort (Lal Qila), Jama Masjid, Chandni Chowk, Khari Baoli Spice Market.",
                    "Optional Activities: Private heritage photography walk with a certified regional historian.",
                    "Overnight Stay: New Delhi (Handpicked 5-Star Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Heritage Muglai Dinner.",
                ],
            ),
            _day(
                3,
                "New Delhi Architectural Splendour | The Garden Tombs & Romantic Symmetry",
                (
                    "Dedicate your day to exploring the breathtaking landscapes and monument poetry of New Delhi. Your "
                    "first destination is Humayun's Tomb, a magnificent UNESCO World Heritage Site and the primary "
                    "inspiration behind the Taj Mahal. Stroll through the lush manicured lawns, capturing stunning "
                    "frames of Persian architectural symmetry. Later, visit the serene Lodi Gardens, a popular Instagram "
                    "location where massive 15th-century dome tombs rest quietly amidst expansive botanic beauty. "
                    "Conclude with an evening visit to the majestic Akshardham Temple complex for an immersive "
                    "multi-media water show."
                ),
                [
                    "Sightseeing Included: Humayun's Tomb, Lodi Gardens, Swaminarayan Akshardham Temple & Fountain Show.",
                    "Evening Experience: VIP reserved musical water fountain show seats at Akshardham.",
                    "Overnight Stay: New Delhi (Handpicked 5-Star Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Elegant Multi-cuisine Dinner.",
                ],
            ),
            _day(
                4,
                "The Southern Sultanates Trail | Ancient Minarets & Contemporary Luxury Living",
                (
                    "Journey south to Mehrauli, home to some of the oldest layered historical attractions in Delhi. "
                    "Marvel at the Qutub Minar, a soaring 73-meter victory tower adorned with intricate calligraphic "
                    "carvings. Explore the surrounding archaeological park before transiting to the high-end "
                    "contemporary lifestyle district of New Delhi. Spend your late afternoon discovering premium shopping "
                    "options at Khan Market or the luxurious DLF Emporio mall, followed by a relaxed evening stroll "
                    "around the white colonnaded arcades of Connaught Place."
                ),
                [
                    "Sightseeing Included: Qutub Minar Complex, Mehrauli Archaeological Park, Connaught Place.",
                    "Optional Activities: An exclusive luxury shopping assistant tour for premium Indian textiles and jewelry.",
                    "Overnight Stay: New Delhi (Handpicked 5-Star Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Farewell Chef's Tasting Menu Dinner.",
                ],
            ),
            _day(
                5,
                "Departure from Delhi | Cherishing Unforgettable Memories",
                (
                    "Indulge in a final, leisurely breakfast at your premium hotel. Spend your morning at leisure "
                    "capturing final photographs or enjoying your resort's luxury spa. At the designated hour, your "
                    "private luxury transport vehicle will transfer you to the airport or railway station. Bid farewell "
                    "to the historic city, carrying unforgettable memories of an exceptional journey designed perfectly "
                    "by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door airport or terminal drop-off.",
                    "Meals Included: Lavish Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "The Grand New Delhi / Vivanta Dwarka",
                "New Delhi",
                "04 Nights",
                "Deluxe",
                "Deluxe King Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: The Grand New Delhi / Vivanta Dwarka | Deluxe King Room | 04 Nights (Full Stay) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Taj Palace / Shangri-La Eros New Delhi",
                "New Delhi",
                "04 Nights",
                "Premium",
                "Premium City View Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="OPTION 02 – PREMIUM: Taj Palace / Shangri-La Eros New Delhi | Premium City View Room | 04 Nights (Full Stay) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Leela Palace New Delhi / The Imperial",
                "New Delhi",
                "04 Nights",
                "Luxury",
                "Grand Deluxe Heritage Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                3,
                description="OPTION 03 – LUXURY: The Leela Palace New Delhi / The Imperial | Grand Deluxe Heritage Room | 04 Nights (Full Stay) | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Oberoi New Delhi",
                "New Delhi",
                "04 Nights",
                "Ultra Luxury",
                "Luxury Landmark View Suite",
                "MAPAI (Breakfast & Dinner)",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: The Oberoi New Delhi | Luxury Landmark View Suite | 04 Nights (Full Stay) | MAPAI (Breakfast & Dinner)",
            ),
        ],
        inclusions=[
            _inc_included("Accommodation: Premium hotel stays as per your selected choice.", 1),
            _inc_included("Luxury Transportation: All transfers & sightseeing in a private AC vehicle.", 2),
            _inc_included("Meals: Daily breakfasts & dinners included as part of the curated MAPAI plan.", 3),
            _inc_included("TRAGUIN Support: 24/7 personalized customer care concierge support.", 4),
            _inc_included("Welcome Amenities: Refreshing arrival kit with traditional stoles and treats.", 5),
            _inc_included("Complimentary Experiences: Private old-city cycle-rickshaw exploration ride.", 6),
            _inc_excluded("Inbound or outbound flights and interstate train bookings.", 7),
            _inc_excluded("All monument entry tickets, museum passes, and camera authorization fees.", 8),
            _inc_excluded("Personal expenses such as laundry services, bar tabs, and tips.", 9),
            _inc_excluded("Optional custom tours, specialized guides, or independent activities.", 10),
        ],
    )
    return package, itinerary


def build_dl_010(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = "DL-010"
    tour_code = "TRG-DEL-010"
    title = "Capital Explorer"
    duration = "05 Nights / 06 Days"
    slug = "dl-010-capital-explorer"
    itin_slug = "dl-010-capital-explorer-itinerary"
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
            _ph("State / Country: Delhi / India | Category: Premium Family Tour", 2),
            _ph("Destinations: Old Delhi • New Delhi • Lutyens' Zone • Qutub Complex • Akshardham", 3),
            _ph("Ideal for: Family Vacations, Heritage Enthusiasts & Luxury Explorers", 4),
            _ph("Best season: October to March (Pleasant Winter)", 5),
            _ph("Starting price: On Request (Premium Customized Custom Plan)", 6),
            _ph("Vehicle & Meal Plan: Private Luxury SUV / MAPAI (Breakfast & Dinner)", 7),
            _ph(
                "Route Map: Royal Reception → Old Delhi Heritage → Lutyens' & Humayun's Tomb → "
                "Qutub Minar & Lotus Temple → Akshardham & Dilli Haat → Final Shopping & Departure",
                8,
            ),
            _ph(
                "TRAGUIN Signature Experience: Private family historical briefing by a cultural expert before "
                "visiting the Old Delhi monuments.",
                9,
            ),
            _ph(
                "Curated by TRAGUIN Experts: Optimized city routing designed to avoid heavy traffic zones, "
                "maximizing your leisure time.",
                10,
            ),
            _ph(
                "Shopping & Local Experiences: Khan Market designer boutiques; Dilli Haat and Janpath for "
                "handloom textiles, pashmina shawls, silver jewelry.",
                11,
            ),
            _ph(
                "Important Notes: Check-in 14:00 hrs, check-out 11:00 hrs; woolens Oct-Mar; book 30–45 days ahead.",
                12,
            ),
        ],
        moods=["Family", "Heritage", "Luxury"],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note="On Request (Premium Customized Custom Plan)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Capital Explorer • Imperial Heritage & Modern Splendour",
        overview=(
            "Welcome to an unforgettable odyssey through time, exclusively curated and presented by TRAGUIN. "
            "Embark on the definitive Delhi Family Tour, engineered to showcase the grand history, architectural "
            "marvels, and dynamic lifestyle of India's eternal capital city. As your highly professional luxury travel "
            "consultants, TRAGUIN turns this exploration into an absolute premium luxury holiday. From the narrow, "
            "story-filled alleys of Chandni Chowk to the majestic, manicured avenues of Lutyens' Delhi and the towering "
            "grandeur of the Qutub Minar, you will experience the state's iconic attractions while enjoying premium "
            "stays, handpicked hotels, and exclusive experiences that promise unforgettable memories for your family.\n\n"
            "TOUR OVERVIEW\n"
            "This bespoke 5 Nights / 06 Days family itinerary is thoughtfully balanced to bridge the historic soul of "
            "Old Delhi with the imperial grace of New Delhi. Guests will travel in a fully private, chauffeured premium "
            "luxury vehicle, eliminating the stress of city commutes. Enjoy an upscale meal plan (MAPAI) comprising rich "
            "gourmet breakfast buffets and specially arranged fine dining experiences in the evenings. Backed by a "
            "signature TRAGUIN curated experience note, this vacation includes VIP entry privileges at prominent sites, "
            "private guided historical briefings, and 24/7 dedicated guest relation assistance.\n\n"
            "WHY VISIT DELHI? THE BEST DELHI TOUR PACKAGE EXPERIENCE\n"
            "When arranging a Luxury Delhi Holiday, families seek an enriching dive into the heart of India's "
            "political, culinary, and architectural epicenter. Delhi holds an incredible collection of top tourist "
            "places in Delhi, combining pristine UNESCO World Heritage sites with modern design masterpieces. Choosing "
            "the right Delhi Tour Package ensures that you witness the striking contrasts of India's heritage "
            "comfortably and completely. For couples and modern families seeking a tailored Delhi Honeymoon Package "
            "or an multi-generational Delhi Family Tour, the capital opens up highly sought-after, popular Instagram "
            "locations such as the mesmerizing Humayun's Tomb, the architectural symmetry of the Lotus Temple, and "
            "the magnificent, vibrant avenues of Sunder Nursery. From high-end luxury boutique shopping at Khan Market "
            "to experiencing traditional street food and imperial Mughlai dining, our specialized TRAGUIN Delhi "
            "Packages bring together premium handpicked hotels and immersive experiences during the absolute best time "
            "to visit Delhi."
        ),
        seo_title="DL-010 | Capital Explorer Premium Family Tour | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Delhi family package (DL-010 / TRG-DEL-010): Old Delhi, Lutyens' Delhi, "
            "Qutub Minar, Lotus Temple, Akshardham, Dilli Haat, and 4-tier luxury accommodation."
        ),
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
            _ih("Connaught Place heritage circle & welcome dinner on Day 01", 1),
            _ih("Red Fort, Chandni Chowk, Jama Masjid & Raj Ghat on Day 02", 2),
            _ih("India Gate, Humayun's Tomb & Sunder Nursery on Day 03", 3),
            _ih("Qutub Minar, Lotus Temple & Hauz Khas Village on Day 04", 4),
            _ih("Akshardham Temple, Dilli Haat & farewell dinner on Day 05", 5),
            _ih("Final shopping & departure on Day 06", 6),
            _ih("TRAGUIN Signature Experience: Private family historical briefing before Old Delhi monuments", 7),
        ],
        days=[
            _day(
                1,
                "Arrival in Delhi | Royal Reception & Luxurious Urban Indulgence",
                (
                    "Your premium Delhi experience begins the moment you touch down. Meet your dedicated private "
                    "chauffeur at New Delhi Airport (IGI) or Delhi Railway Station, who will assist with your baggage "
                    "and escort you in a private luxury SUV. Drive to your handpicked premium luxury hotel for a "
                    "smooth check-in. Spend the afternoon relaxing and rejuvenating with premium welcome amenities. In "
                    "the evening, take a leisurely drive through the beautifully lit Connaught Place or choose a premium "
                    "dinner at a renowned fine-dining venue."
                ),
                [
                    "Delhi Sightseeing Included: Connaught Place heritage circle drive, Central Park evening walk.",
                    "Evening Experience: Bespoke welcome dinner featuring a fusion of imperial North Indian flavors.",
                    "Overnight Stay: New Delhi (Premium / Ultra Luxury Hotel).",
                    "Meals Included: Welcome Drink & Fine-Dining Dinner.",
                ],
            ),
            _day(
                2,
                "Old Delhi Heritage Exploration | Mughal Majesty, Rickshaw Rides & Historic Streets",
                (
                    "Savor a lavish buffet breakfast before stepping out to explore the ancient heartbeat of Old Delhi. "
                    "Witness the colossal red sandstone walls of the iconic Red Fort. Embark on a specially curated, "
                    "private premium rickshaw ride through the bustling lanes of Chandni Chowk, taking in the incredible "
                    "sights and scents of Asia's largest spice market, Khari Baoli. Visit the grand Jama Masjid, one of "
                    "India's largest mosques, before paying tribute at Raj Ghat, the peaceful memorial of Mahatma Gandhi."
                ),
                [
                    "Delhi Sightseeing Included: Red Fort (photo stop), Chandni Chowk, Khari Baoli, Jama Masjid, Raj Ghat.",
                    "Optional Activities: A guided culinary tasting tour of legendary Old Delhi multi-generational eateries.",
                    "Overnight Stay: New Delhi (Premium / Ultra Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Luxury Dinner.",
                ],
            ),
            _day(
                3,
                "Imperial Lutyens' & Sunset at Tombs | The Grand Cold War Architecture & The Mughal Precursor",
                (
                    "Today, explore the imperial grace of New Delhi. Drive down the magnificent Rajpath to view the "
                    "stately Rashtrapati Bhavan (President's House) and the Parliament House. Stop at the iconic India "
                    "Gate, a proud war memorial surrounded by sprawling lush lawns. In the afternoon, enjoy an immersive "
                    "experience at Humayun's Tomb—a gorgeous UNESCO World Heritage Site and a popular Instagram "
                    "location whose architecture directly inspired the Taj Mahal. End your afternoon wandering through "
                    "the tranquil paths of Sunder Nursery."
                ),
                [
                    "Delhi Sightseeing Included: India Gate, Rashtrapati Bhavan & Parliament Buildings (drive-by), Humayun's Tomb, Sunder Nursery.",
                    "Evening Experience: High tea experience at a luxury colonial-style café in Khan Market.",
                    "Overnight Stay: New Delhi (Premium / Ultra Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Gourmet Dinner.",
                ],
            ),
            _day(
                4,
                "Ancient South Delhi Minars & Spiritual Marvels | Towering Islamic Monuments & Contemporary Architecture",
                (
                    "Following breakfast, head south into the oldest residential settlements of Delhi. Explore the iconic "
                    "Qutub Minar complex, marveling at the 73-meter-tall brick minaret and the ancient iron pillar that "
                    "has defied rust for over 1,600 years. Later, experience the peaceful ambiance and breathtaking "
                    "architectural design of the Lotus Temple, shaped like a blooming flower. Spend your evening "
                    "exploring the upscale art galleries, boutique cafes, and lifestyle shopping complexes at the chic "
                    "Hauz Khas Village."
                ),
                [
                    "Delhi Sightseeing Included: Qutub Minar complex, Mehrauli Archaeological Park, Lotus Temple, Hauz Khas Village.",
                    "Photography Points: The iconic arches of Qutub Minar and the sunset views overlooking Hauz Khas lake.",
                    "Overnight Stay: New Delhi (Premium / Ultra Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Selected Dinner.",
                ],
            ),
            _day(
                5,
                "Akshardham Majesty & Craft Villages | Spiritual Odyssey & Cultural Immersion",
                (
                    "Dedicate your morning to the breathtaking landscapes and artistic genius of the Swaminarayan "
                    "Akshardham Temple, one of the world's largest comprehensive Hindu temple complexes. Experience its "
                    "immersive cultural boat ride, informative exhibitions, and massive carved stone pillars. In the "
                    "afternoon, visit Dilli Haat, an open-air food and craft bazaar showcasing rural artisans from every "
                    "state in India—perfect for authentic handicraft shopping and tasting varied regional foods."
                ),
                [
                    "Delhi Sightseeing Included: Swaminarayan Akshardham Temple, Cultural Exhibits, Dilli Haat INA.",
                    "Evening Experience: The magnificent musical water fountain show at Akshardham Temple.",
                    "Overnight Stay: New Delhi (Premium / Ultra Luxury Hotel).",
                    "Meals Included: Premium Breakfast & Farewell Special Dinner.",
                ],
            ),
            _day(
                6,
                "Final Shopping & Departure | Cherishing Unforgettable Memories Beyond Destinations",
                (
                    "Indulge in a final, delicious breakfast at your luxury hotel. Depending on your flight time, your "
                    "private vehicle is available for last-minute souvenir shopping at the upscale Khan Market or the "
                    "historic Janpath boutique stands. Later, your private chauffeur will provide a smooth drop-off at "
                    "New Delhi International Airport or Railway Station. Return home carrying a heart filled with "
                    "beautiful family bonds and unforgettable memories curated flawlessly by TRAGUIN."
                ),
                [
                    "Transfers Included: Private luxury door-to-door airport/station transfer.",
                    "Meals Included: Sumptuous Buffet Breakfast.",
                ],
            ),
        ],
        hotels=[
            _hotel(
                "The Suryaa New Delhi / Radisson Blu / similar",
                "New Delhi",
                "05 Nights",
                "Deluxe",
                "Deluxe Executive Room",
                "MAPAI (Breakfast & Dinner)",
                4,
                1,
                description="OPTION 01 – DELUXE: The Suryaa New Delhi / Radisson Blu / similar | Deluxe Executive Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "The Lalit New Delhi / Eros Hotel / similar",
                "New Delhi",
                "05 Nights",
                "Premium",
                "Premium Club Room",
                "MAPAI (Breakfast & Dinner)",
                5,
                2,
                description="OPTION 02 – PREMIUM: The Lalit New Delhi / Eros Hotel / similar | Premium Club Room | MAPAI (Breakfast & Dinner)",
            ),
            _hotel(
                "Taj Palace / The Leela Palace New Delhi",
                "New Delhi",
                "05 Nights",
                "Luxury",
                "Luxury Garden View Suite",
                "MAPAI + Executive Lounge Access",
                5,
                3,
                description="OPTION 03 – LUXURY: Taj Palace / The Leela Palace New Delhi | Luxury Garden View Suite | MAPAI + Executive Lounge Access",
            ),
            _hotel(
                "The Oberoi New Delhi / The Imperial New Delhi",
                "New Delhi",
                "05 Nights",
                "Ultra Luxury",
                "VVIP Royal Panoramic Suite",
                "Bespoke Signature MAPAI Plan",
                5,
                4,
                description="OPTION 04 – ULTRA LUXURY: The Oberoi New Delhi / The Imperial New Delhi | VVIP Royal Panoramic Suite | Bespoke Signature MAPAI Plan",
            ),
        ],
        inclusions=[
            _inc_included("Premium Stays: 05 Nights in chosen handpicked luxury properties in Delhi.", 1),
            _inc_included("Luxury Transportation: Private dedicated SUV for all point-to-point sightseeing.", 2),
            _inc_included("Curated Meal Plan: Daily premium breakfast and specially selected dinners.", 3),
            _inc_included("TRAGUIN Support: 24/7 personalized guest experience manager on call.", 4),
            _inc_included("Welcome Amenities: Customized family travel kit and refreshments on arrival.", 5),
            _inc_included("Complimentary Experience: Private rickshaw tour through old heritage routes.", 6),
            _inc_excluded("Airfare, domestic flight tickets, or long-distance train travel.", 7),
            _inc_excluded("Monument entry tickets, camera permits, and local guide fees.", 8),
            _inc_excluded("Personal expenses such as laundry, phone calls, drinks, or tips.", 9),
            _inc_excluded("Any optional museum activities or extended excursions outside Delhi.", 10),
        ],
    )
    return package, itinerary


DELHI_DOMESTIC_BUILDERS = [
    build_dl_001,
    build_dl_002,
    build_dl_003,
    build_dl_004,
    build_dl_005,
    build_dl_006,
    build_dl_007,
    build_dl_008,
    build_dl_009,
    build_dl_010,
]
