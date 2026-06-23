#!/usr/bin/env python3
"""Insert GJ-004 Rann of Kutch and GJ-005 Statue of Unity packages from brochure content."""

from __future__ import annotations

from decimal import Decimal

from schemas.itineraries import (
    ItineraryCreate,
    ItineraryDayNested,
    ItineraryHighlightNested,
    ItineraryHotelNested,
    ItineraryInclusionNested,
)
from schemas.packages import PackageCreate, PackageHighlightNested
from services.package_image_specs import GJ_004_PEXELS_IMAGES, GJ_005_PEXELS_IMAGES
from services.package_insert import run_gujarat_package_inserts

GUJARAT_DESTINATION_ID = "07be1b4e-0016-4caa-a680-c130ba86b9f7"

GJ_004_PACKAGE = PackageCreate(
    slug="gj-004-rann-of-kutch-luxury-extravaganza",
    destination_id=GUJARAT_DESTINATION_ID,
    title="Rann of Kutch Luxury Extravaganza",
    duration_label="04 Nights / 05 Days",
    price=0,
    rating=Decimal("4.9"),
    is_featured=True,
    featured_sort_order=4,
    is_published=True,
    highlights=[
        PackageHighlightNested(text="Great Rann white desert sunset & moonrise experiences", sort_order=1),
        PackageHighlightNested(text="Kalo Dungar, craft villages & Rogan art interactions", sort_order=2),
        PackageHighlightNested(text="Vijay Vilas Palace & Mandvi beach coastal retreat", sort_order=3),
        PackageHighlightNested(text="Bhuj heritage palaces, temples & artisan bazaars", sort_order=4),
        PackageHighlightNested(text="Private luxury Innova Crysta with TRAGUIN concierge", sort_order=5),
        PackageHighlightNested(text="VIP White Desert permit handling & welcome kit", sort_order=6),
    ],
    moods=["Culture", "Luxury", "Family"],
)

GJ_004_ITINERARY = ItineraryCreate(
    slug="gj-004-rann-of-kutch-itinerary",
    destination_id=GUJARAT_DESTINATION_ID,
    title="Rann of Kutch Luxury Extravaganza",
    duration_label="04 Nights / 05 Days",
    duration_days=5,
    starting_price=0,
    price_note="On Request (Premium Custom Luxury Pricing)",
    rating=Decimal("4.9"),
    review_count=0,
    tagline="Welcome to the Mystical Salt Kingdom",
    overview=(
        "Step into a mystical landscape where the earth meets the sky in a seamless sheet of brilliant white salt. "
        "This TRAGUIN premium Kutch journey blends the ethereal beauty of the Great Rann with immersive craft heritage, "
        "royal Mandvi coastlines, and Bhuj's palace treasures — with private luxury transfers, curated artisan "
        "interactions, and handpicked desert tent cities and beach resorts for discerning families."
    ),
    seo_title="GJ-004 | Rann of Kutch Luxury Extravaganza | TRAGUIN Premium Gujarat Tour",
    seo_description=(
        "Luxury 04 Nights / 05 Days Rann of Kutch package (GJ-004) covering Bhuj, Hodka, Dhordo, Mandvi, "
        "Kalo Dungar, craft villages, and premium tent city stays. Ideal for families, couples, and "
        "culture enthusiasts."
    ),
    is_featured=True,
    featured_sort_order=4,
    is_published=True,
    highlights=[
        ItineraryHighlightNested(text="Great Rann White Desert", sort_order=1),
        ItineraryHighlightNested(text="Kalo Dungar & Craft Villages", sort_order=2),
        ItineraryHighlightNested(text="Vijay Vilas Palace, Mandvi", sort_order=3),
        ItineraryHighlightNested(text="Aina Mahal & Prag Mahal, Bhuj", sort_order=4),
        ItineraryHighlightNested(text="Luxury Tent City Stay", sort_order=5),
    ],
    days=[
        ItineraryDayNested(
            day_number=1,
            title="Bhuj to Hodka / Dhordo — The White Desert Gateway",
            description=(
                "Begin with a warm traditional welcome at Bhuj Airport or Railway Station and drive through "
                "changing vistas toward the Great Rann. Check in at your ultra-luxury resort or premium Swiss tent "
                "city. After a lavish Kutchi lunch, take your first steps onto the salt-crusted plains and watch "
                "the white desert sparkle under golden sunset rays before folk music and stargazing."
            ),
            activities=[
                "Sightseeing Included: Great Rann of Kutch border vistas, salt desert sunset gallery",
                "Optional Activities: Camel cart ride across the salt flats, paramotoring over the white expanse",
                "Evening Experience: Live Kutchi folk dance and musical performance with traditional campfire",
                "Overnight Stay: Premium resort luxury tents / traditional Bhunga suites (Hodka/Dhordo)",
                "Meals Included: Lunch & gourmet dinner",
            ],
            sort_order=1,
        ),
        ItineraryDayNested(
            day_number=2,
            title="Kalo Dungar & Craft Village Immersion",
            description=(
                "Venture to Kalo Dungar (Black Hill), the highest point in Kutch, for panoramic views of the "
                "ecosystem and Indo-Pak border vistas. Visit the 400-year-old Dattatreya Temple, then explore "
                "Gandhi Nu Gam and Bhirandiyara for Rogan art, Ajrakh block printing, and leather embroidery. "
                "Return for a magical moonrise over the white desert floor."
            ),
            activities=[
                "Sightseeing Included: Kalo Dungar viewpoint, Dattatreya Temple, Gandhi Nu Gam, Bhirandiyara Village",
                "Optional Activities: Professional family photoshoot on the salt desert with traditional costumes",
                "Evening Experience: Cultural interaction and luxury high-tea at a scenic spot",
                "Overnight Stay: Premium resort luxury tents / Bhunga suites (Hodka/Dhordo)",
                "Meals Included: Premium breakfast, lunch & dinner",
            ],
            sort_order=2,
        ),
        ItineraryDayNested(
            day_number=3,
            title="Hodka / Dhordo to Mandvi — Royal Beach Retreat",
            description=(
                "Drive south to historic Mandvi, once the summer retreat of the Maharaos of Kutch. Discover "
                "Vijay Vilas Palace with its red sandstone domes and Bollywood-famous corridors, then unwind "
                "on pristine Mandvi Beach with windmills and an Arabian Sea sunset."
            ),
            activities=[
                "Sightseeing Included: Vijay Vilas Palace, Mandvi private beach, wind farms beach",
                "Optional Activities: Speed boating, banana boat rides, or wooden shipbuilding yard tour",
                "Evening Experience: Romantic seaside walk followed by luxury coastal dinner",
                "Overnight Stay: Luxury beachside resort / premium heritage palace stay, Mandvi",
                "Meals Included: Premium breakfast & dinner",
            ],
            sort_order=3,
        ),
        ItineraryDayNested(
            day_number=4,
            title="Mandvi to Bhuj — Historic Palaces & Heritage Discovery",
            description=(
                "Return to Bhuj for a day of premium cultural attractions — the mirror-work Aina Mahal, "
                "Italian-Gothic Prag Mahal with its bell tower, the white marble Swaminarayan Temple, and "
                "bustling bazaars for bandhani sarees and silver ornaments. Stroll Hamirsar Lake in the evening."
            ),
            activities=[
                "Sightseeing Included: Aina Mahal, Prag Mahal, Bhujia Fort, Shree Swaminarayan Temple, Hamirsar Lake",
                "Optional Activities: Guided food trail exploring Kutchi Dabeli and local sweet shops",
                "Evening Experience: Leisure stroll around Hamirsar Lake with lit fountains",
                "Overnight Stay: Handpicked luxury business/heritage hotel, Bhuj",
                "Meals Included: Premium breakfast & dinner",
            ],
            sort_order=4,
        ),
        ItineraryDayNested(
            day_number=5,
            title="Bhuj Departure with Unforgettable Memories",
            description=(
                "Enjoy a relaxed gourmet breakfast. Visit Bhujodi craft village for woven stoles and carpets "
                "directly from traditional looms before your private transfer to Bhuj Airport or Railway Station."
            ),
            activities=[
                "Sightseeing Included: Bhujodi artisan village complex (time permitting)",
                "Transfers: Dedicated airport/station drop in private premium vehicle",
                "Meals Included: Premium breakfast",
            ],
            sort_order=5,
        ),
    ],
    hotels=[
        ItineraryHotelNested(
            name="Gateway To Rann Resort / Similar",
            location="Hodka/Dhordo (2N)",
            nights_label="02 Nights",
            description="Deluxe AC Bhunga stay near the White Rann.",
            stars=4,
            category_label="Deluxe",
            room_type="AC Bhunga",
            meal_plan="Full Board at Rann stay",
            sort_order=1,
        ),
        ItineraryHotelNested(
            name="Rann Resort Dholavira / Evoke Tents / Similar",
            location="Hodka/Dhordo (2N)",
            nights_label="02 Nights",
            description="Premium tent experience in the Kutch desert.",
            stars=4,
            category_label="Premium",
            room_type="Premium Tent",
            meal_plan="Full Board at Rann stay",
            sort_order=2,
        ),
        ItineraryHotelNested(
            name="Tent City Dhordo / Similar",
            location="Hodka/Dhordo (2N)",
            nights_label="02 Nights",
            description="Luxury Rann Utsav tent city with curated experiences.",
            stars=5,
            category_label="Luxury",
            room_type="Premium Tent",
            meal_plan="Full Board at Rann stay",
            sort_order=3,
        ),
        ItineraryHotelNested(
            name="Tent City Dhordo Darbari Suite / Similar",
            location="Hodka/Dhordo (2N)",
            nights_label="02 Nights",
            description="Ultra-luxury Darbari suite tent city experience.",
            stars=5,
            category_label="Ultra Luxury",
            room_type="Darbari Suite",
            meal_plan="Full Board at Rann stay",
            sort_order=4,
        ),
        ItineraryHotelNested(
            name="Serena Beach Resort / The Beach at Mandvi Palace / Similar",
            location="Mandvi (1N)",
            nights_label="01 Night",
            description="Premium beachside resort on the Mandvi coast.",
            stars=5,
            category_label="Premium",
            room_type="Executive / Luxury Villa",
            meal_plan="MAPAI",
            sort_order=5,
        ),
        ItineraryHotelNested(
            name="Regenta Resort Bhuj / The Fern Residency Bhuj / Similar",
            location="Bhuj (1N)",
            nights_label="01 Night",
            description="Heritage city hotel for Bhuj palace circuit.",
            stars=4,
            category_label="Deluxe",
            room_type="Executive / Suite Room",
            meal_plan="MAPAI",
            sort_order=6,
        ),
    ],
    inclusions=[
        ItineraryInclusionNested(
            kind="included",
            text="04 nights premium accommodation at handpicked hotels and luxury desert resorts",
            sort_order=1,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Daily premium breakfast & dinners; full board at Rann tent city stay",
            sort_order=2,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Private chauffeur-driven Toyota Innova Crysta for all transfers and sightseeing",
            sort_order=3,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="TRAGUIN welcome kit, VIP border permit handling, and 24/7 concierge support",
            sort_order=4,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Driver allowances, tolls, parking, fuel, and applicable state taxes",
            sort_order=5,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Airfare, helicopter transfers, or train tickets to/from Bhuj",
            sort_order=6,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Monument entry tickets, camera fees, and professional guide fees",
            sort_order=7,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Personal expenses, laundry, premium alcohol, and room service",
            sort_order=8,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Optional adventure sports (paramotoring, ATV rides, camel safaris)",
            sort_order=9,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Gala dinner surcharges during Christmas, New Year, or peak festival periods",
            sort_order=10,
        ),
    ],
)

GJ_005_PACKAGE = PackageCreate(
    slug="gj-005-divine-statue-of-unity-circuit",
    destination_id=GUJARAT_DESTINATION_ID,
    title="The Divine & Majestic Statue of Unity Circuit",
    duration_label="04 Nights / 05 Days",
    price=48500,
    rating=Decimal("4.9"),
    is_featured=True,
    featured_sort_order=5,
    is_published=True,
    highlights=[
        PackageHighlightNested(text="Dwarka sacred circuit — Bet Dwarka & Nageshwar Jyotirlinga", sort_order=1),
        PackageHighlightNested(text="Somnath Temple with VIP light & sound show", sort_order=2),
        PackageHighlightNested(text="Statue of Unity viewing gallery & laser show", sort_order=3),
        PackageHighlightNested(text="Porbandar Kirti Mandir heritage stop en route", sort_order=4),
        PackageHighlightNested(text="Premium tent city & valley resort stays", sort_order=5),
        PackageHighlightNested(text="TRAGUIN VIP darshan assistance & 24/7 concierge", sort_order=6),
    ],
    moods=["Pilgrimage", "Heritage", "Luxury"],
)

GJ_005_ITINERARY = ItineraryCreate(
    slug="gj-005-divine-statue-of-unity-itinerary",
    destination_id=GUJARAT_DESTINATION_ID,
    title="The Divine & Majestic Statue of Unity Circuit",
    duration_label="04 Nights / 05 Days",
    duration_days=5,
    starting_price=48500,
    price_note="INR 48,500/- Per Person (Premium)",
    rating=Decimal("4.9"),
    review_count=0,
    tagline="A Soul-Stirring Spiritual Odyssey Across Gujarat",
    overview=(
        "Embark on a soul-stirring and ultra-luxurious spiritual odyssey across Gujarat — from the sacred shores "
        "of Dwarka and Somnath to the monumental Statue of Unity on the Narmada. This TRAGUIN premium circuit "
        "features seamless private transfers, VIP temple access, handpicked luxury resorts and tent cities, and "
        "curated heritage storytelling at every legendary stop."
    ),
    seo_title="GJ-005 | Divine Statue of Unity Circuit | TRAGUIN Premium Gujarat Tour",
    seo_description=(
        "Premium 04 Nights / 05 Days Gujarat pilgrimage package (GJ-005) covering Ahmedabad, Dwarka, Somnath, "
        "Porbandar, and Statue of Unity with VIP darshan, laser shows, and luxury stays. From INR 48,500 per person."
    ),
    is_featured=True,
    featured_sort_order=5,
    is_published=True,
    highlights=[
        ItineraryHighlightNested(text="Dwarkadhish Temple & Bet Dwarka", sort_order=1),
        ItineraryHighlightNested(text="Somnath Temple Light & Sound", sort_order=2),
        ItineraryHighlightNested(text="Statue of Unity Viewing Gallery", sort_order=3),
        ItineraryHighlightNested(text="Kirti Mandir, Porbandar", sort_order=4),
        ItineraryHighlightNested(text="Narmada Valley Eco Attractions", sort_order=5),
    ],
    days=[
        ItineraryDayNested(
            day_number=1,
            title="Ahmedabad to Dwarka via Sightseeing",
            description=(
                "Arrive at Ahmedabad and meet your private chauffeur for the scenic drive to the ancient kingdom "
                "of Dwarka. Check into your ultra-luxury hotel and witness the iconic flag-changing ceremony at "
                "Dwarkadhish Temple. Stroll the Gomti River ghats for stunning photography at dusk."
            ),
            activities=[
                "Sightseeing Included: Dwarkadhish Temple, Gomti River ghats, local heritage markets",
                "Evening Experience: Grand evening aarti and spiritual orientation session",
                "Overnight Stay: Premium luxury beach resort, Dwarka",
                "Meals Included: Welcome drink & premium buffet dinner",
            ],
            sort_order=1,
        ),
        ItineraryDayNested(
            day_number=2,
            title="Dwarka Sacred Circuit & Local Impressions",
            description=(
                "Board a scenic ferry to Bet Dwarka island, visit Nageshwar Jyotirlinga, Gopi Talav, and the "
                "Rukmini Devi Temple. Spend the evening collecting authentic souvenirs and handwoven textiles "
                "at local markets with sunset views over the Arabian Sea."
            ),
            activities=[
                "Sightseeing Included: Bet Dwarka ferry ride, Nageshwar Jyotirlinga, Gopi Talav, Rukmini Devi Temple",
                "Optional Activities: Speedboat rides around Bet Dwarka island",
                "Evening Experience: Relaxing sunset views over the Arabian Sea shoreline",
                "Overnight Stay: Premium luxury beach resort, Dwarka",
                "Meals Included: Continental breakfast & gourmet dinner",
            ],
            sort_order=2,
        ),
        ItineraryDayNested(
            day_number=3,
            title="Dwarka to Somnath via Porbandar",
            description=(
                "Drive along the magnificent coastal highway to Somnath with a stop at Porbandar's Kirti Mandir, "
                "birthplace of Mahatma Gandhi. Visit Somnath Temple on the ocean shore and witness the awe-inspiring "
                "Jay Somnath light & sound show at dusk."
            ),
            activities=[
                "Sightseeing Included: Kirti Mandir (Porbandar), Somnath Temple, Triveni Sangam, Geeta Mandir",
                "Evening Experience: VIP seating for the Somnath light & sound show",
                "Overnight Stay: Elite heritage luxury hotel, Somnath",
                "Meals Included: Breakfast & premium dinner buffet",
            ],
            sort_order=3,
        ),
        ItineraryDayNested(
            day_number=4,
            title="Somnath to Statue of Unity (Kevadia)",
            description=(
                "Transfer to Kevadia, home of the 182-metre Statue of Unity. Check into your luxury glamping tent "
                "or valley-facing resort. Ascend to the viewing gallery for panoramic Satpura and Vindhya vistas "
                "and conclude with the spectacular laser light show on Sardar Vallabhbhai Patel's legacy."
            ),
            activities=[
                "Sightseeing Included: Statue of Unity viewing gallery, Valley of Flowers, Sardar Sarovar Dam viewpoint",
                "Evening Experience: Spectacular laser light show with high-tech projection mapping",
                "Overnight Stay: Premium luxury tent city / exquisite valley resort, Kevadia",
                "Meals Included: Breakfast & lavish multi-cuisine dinner",
            ],
            sort_order=4,
        ),
        ItineraryDayNested(
            day_number=5,
            title="Statue of Unity Sightseeing to Ahmedabad Departure",
            description=(
                "Explore eco-tourism attractions including Glow Garden, Butterfly Garden, or an optional Narmada "
                "River cruise. Drive back to Ahmedabad for your onward flight or train with unforgettable memories "
                "of Gujarat's divine and monumental landmarks."
            ),
            activities=[
                "Sightseeing Included: Glow Garden, Cactus Garden, Unity Glow Garden photography zones",
                "Optional Activities: Narmada River luxury boat cruise",
                "Transfers: Private transfer to Ahmedabad airport or railway station",
                "Meals Included: Premium breakfast",
            ],
            sort_order=5,
        ),
    ],
    hotels=[
        ItineraryHotelNested(
            name="Hawthorn Suites by Wyndham / Similar",
            location="Dwarka (2N)",
            nights_label="02 Nights",
            description="Deluxe beachside stay in Dwarka.",
            stars=4,
            category_label="Deluxe",
            room_type="Executive Room",
            meal_plan="MAPAI",
            sort_order=1,
        ),
        ItineraryHotelNested(
            name="Mercure Dwarka Resort / Similar",
            location="Dwarka (2N)",
            nights_label="02 Nights",
            description="Premium resort with modern amenities in Dwarka.",
            stars=4,
            category_label="Premium",
            room_type="Premium Room",
            meal_plan="MAPAI",
            sort_order=2,
        ),
        ItineraryHotelNested(
            name="Club Mahindra Dwarka / Similar",
            location="Dwarka (2N)",
            nights_label="02 Nights",
            description="Luxury beach resort for extended Dwarka circuit.",
            stars=5,
            category_label="Luxury",
            room_type="Luxury Room",
            meal_plan="MAPAI",
            sort_order=3,
        ),
        ItineraryHotelNested(
            name="Taj Amer Valley Premium Layout / Similar",
            location="Dwarka (2N)",
            nights_label="02 Nights",
            description="Ultra-luxury premium layout near Dwarka.",
            stars=5,
            category_label="Ultra Luxury",
            room_type="Premium Suite",
            meal_plan="MAPAI",
            sort_order=4,
        ),
        ItineraryHotelNested(
            name="The Fern Residency Somnath / Similar",
            location="Somnath (1N)",
            nights_label="01 Night",
            description="Deluxe heritage hotel near Somnath Temple.",
            stars=4,
            category_label="Deluxe",
            room_type="Executive Room",
            meal_plan="MAPAI",
            sort_order=5,
        ),
        ItineraryHotelNested(
            name="The Grand Somnath Palace Suites / Similar",
            location="Somnath (1N)",
            nights_label="01 Night",
            description="Ultra-luxury suites for Somnath pilgrimage stay.",
            stars=5,
            category_label="Ultra Luxury",
            room_type="Palace Suite",
            meal_plan="MAPAI",
            sort_order=6,
        ),
        ItineraryHotelNested(
            name="Tent City 1 / The Fern Sardar Sarovar Resort / Similar",
            location="Statue of Unity, Kevadia (1N)",
            nights_label="01 Night",
            description="Premium tent city or valley resort at Kevadia.",
            stars=5,
            category_label="Luxury",
            room_type="Premium AC Tent / Valley Room",
            meal_plan="MAPAI",
            sort_order=7,
        ),
    ],
    inclusions=[
        ItineraryInclusionNested(
            kind="included",
            text="04 nights luxury accommodation in handpicked premium properties across the circuit",
            sort_order=1,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Daily buffet breakfasts and premium dinners at all hotels",
            sort_order=2,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Dedicated chauffeur-driven AC private luxury vehicle for all transfers and sightseeing",
            sort_order=3,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="VIP darshan assistance and pre-booked premium entry at high-demand temples",
            sort_order=4,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Complimentary laser show tickets at Somnath and Statue of Unity",
            sort_order=5,
        ),
        ItineraryInclusionNested(
            kind="included",
            text="Welcome amenities, daily mineral water, and TRAGUIN 24/7 concierge support",
            sort_order=6,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Airfares or train tickets to/from Ahmedabad",
            sort_order=7,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Personal expenses, laundry, mini-bar, and gratuities",
            sort_order=8,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Camera fees, optional boat rides, and adventure activity charges",
            sort_order=9,
        ),
        ItineraryInclusionNested(
            kind="excluded",
            text="Lunches not outlined in daily meal plans and travel insurance",
            sort_order=10,
        ),
    ],
)


def main() -> None:
    run_gujarat_package_inserts(
        destination_id=GUJARAT_DESTINATION_ID,
        packages=[
            (GJ_004_PACKAGE, GJ_004_ITINERARY, GJ_004_PEXELS_IMAGES),
            (GJ_005_PACKAGE, GJ_005_ITINERARY, GJ_005_PEXELS_IMAGES),
        ],
    )


if __name__ == "__main__":
    main()
