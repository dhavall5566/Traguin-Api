"""Builder functions for UAE-001 through UAE-004 UAE packages (no images)."""

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


def build_uae_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="uae-001-dubai-essentials-family-tour",
        destination_id=destination_id,
        title="Dubai Essentials Family Tour",
        duration_label="04 Nights / 05 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=75,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Dubai (4N) classic family city break", sort_order=1),
            PackageHighlightNested(text="Burj Khalifa, Dubai Mall & Palm Jumeirah city tour", sort_order=2),
            PackageHighlightNested(text="Thrilling desert safari with BBQ dinner under the stars", sort_order=3),
            PackageHighlightNested(text="Global Village cultural pavilions & family entertainment", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-DXB-ESS-2026 | Serial UAE-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Adventure", "Cultural"],
    )
    itinerary = ItineraryCreate(
        slug="uae-001-dubai-essentials-itinerary",
        destination_id=destination_id,
        title="Dubai Essentials Family Tour",
        duration_label="04 Nights / 05 Days",
        duration_days=5,
        starting_price=0,
        price_note="On Request (Premium Dubai Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Dubai • Burj Khalifa • Desert Safari • Palm Jumeirah • Global Village",
        overview=(
            "Discover the dazzling heights and golden dunes of Dubai with this TRAGUIN curated family itinerary. "
            "Designed for excitement and comfort, this Dubai Essentials package offers a flawless blend of futuristic "
            "city exploration and traditional desert adventure — with handpicked hotels and exclusive services."
        ),
        seo_title="UAE-001 | Dubai Essentials Family Tour | TRAGUIN",
        seo_description=(
            "Premium 04 Nights / 05 Days Dubai family package (UAE-001): Burj Khalifa, desert safari, "
            "Palm Jumeirah, and Global Village."
        ),
        is_featured=True,
        featured_sort_order=75,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Burj Khalifa & Dubai Mall", sort_order=1),
            ItineraryHighlightNested(text="Desert Safari & BBQ Dinner", sort_order=2),
            ItineraryHighlightNested(text="Palm Jumeirah City Tour", sort_order=3),
            ItineraryHighlightNested(text="Global Village Family Day", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Dubai", "Arrive in dazzling Dubai. Your private TRAGUIN transfer will escort you to your handpicked hotel. Enjoy a relaxing evening overlooking the city's stunning skyline.", ["Sightseeing Included: VIP airport reception, private hotel transfer", "Overnight Stay: Dubai (Luxury Family Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "City Tour & Burj Khalifa", "Explore the iconic attractions of Dubai. Visit the Burj Khalifa, the Dubai Mall, and Palm Jumeirah. This curated experience offers deep insights into Dubai's rapid development.", ["Sightseeing Included: Burj Khalifa, Dubai Mall, Palm Jumeirah city tour", "Overnight Stay: Dubai (Luxury Family Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Desert Safari Adventure", "Embark on a thrilling desert safari. Experience dune bashing, camel riding, and a traditional BBQ dinner under the stars — a highlight of TRAGUIN's exclusive packages.", ["Sightseeing Included: Desert safari, dune bashing, camel riding, BBQ dinner", "Overnight Stay: Dubai (Luxury Family Hotel)", "Meals Included: Breakfast & Desert BBQ Dinner"]),
            _day(4, "Global Village & Leisure", "A full day of immersive fun at Global Village. Explore cultural pavilions, shopping, and entertainment, creating unforgettable memories.", ["Sightseeing Included: Global Village full-day visit", "Overnight Stay: Dubai (Luxury Family Hotel)", "Meals Included: Breakfast"]),
            _day(5, "Departure", "Enjoy a final family breakfast. Your private TRAGUIN chauffeur ensures a comfortable transfer to the airport.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Atlantis, The Palm / similar", location="Dubai", nights_label="04 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Address Downtown / similar", location="Dubai", nights_label="04 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=2),
        ],
        inclusions=_uae001_inclusions(),
    )
    return package, itinerary


def _uae001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="04 Nights in handpicked premium family hotel in Dubai", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury van transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Dubai city tour — Burj Khalifa, Dubai Mall & Palm Jumeirah", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Desert safari with dune bashing, camel riding & BBQ dinner", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Global Village full-day visit", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International airfare and UAE entry visa processing fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=10),
    ]


def build_uae_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="uae-002-dubai-abu-dhabi-family-tour",
        destination_id=destination_id,
        title="Dubai Abu Dhabi Family Tour",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=76,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Dubai (3N) → Abu Dhabi (2N) classic UAE family circuit", sort_order=1),
            PackageHighlightNested(text="Burj Khalifa, desert safari & Dubai Marina evening", sort_order=2),
            PackageHighlightNested(text="Sheikh Zayed Grand Mosque & Louvre Abu Dhabi", sort_order=3),
            PackageHighlightNested(text="Ferrari World family thrills", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-DXB-AUH-FAM-2026 | Serial UAE-002", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="uae-002-dubai-abu-dhabi-itinerary",
        destination_id=destination_id,
        title="Dubai Abu Dhabi Family Tour",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium UAE Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Dubai • Abu Dhabi • Burj Khalifa • Sheikh Zayed Mosque • Ferrari World",
        overview=(
            "Embark on an unforgettable UAE journey with TRAGUIN's curated family itinerary. Blending the futuristic "
            "pulse of Dubai with the cultural grandeur of Abu Dhabi, this tour offers a seamless mix of excitement "
            "and heritage — ensuring unforgettable memories."
        ),
        seo_title="UAE-002 | Dubai Abu Dhabi Family Tour | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days UAE family package (UAE-002): Dubai city tour, desert safari, "
            "Sheikh Zayed Mosque, Louvre Abu Dhabi, and Ferrari World."
        ),
        is_featured=True,
        featured_sort_order=76,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Burj Khalifa & Dubai City Exploration", sort_order=1),
            ItineraryHighlightNested(text="Desert Safari & Abu Dhabi Transfer", sort_order=2),
            ItineraryHighlightNested(text="Sheikh Zayed Grand Mosque & Louvre", sort_order=3),
            ItineraryHighlightNested(text="Ferrari World Family Day", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Dubai", "Your TRAGUIN family tour begins with a VIP airport welcome. A private luxury van transfers you to your premium hotel. Enjoy a relaxing evening by the Dubai Marina, admiring the breathtaking landscapes of the illuminated city.", ["Sightseeing Included: VIP airport welcome, private luxury van transfer", "Overnight Stay: Dubai (Luxury Family Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Dubai City Exploration", "Explore the best of Dubai. Visit the iconic Burj Khalifa, The Dubai Mall, and Palm Jumeirah. This curated experience offers deep insights into Dubai's luxury living and iconic attractions.", ["Sightseeing Included: Burj Khalifa, Dubai Mall, Palm Jumeirah city tour", "Overnight Stay: Dubai (Luxury Family Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Desert Safari & Transfer to Abu Dhabi", "Experience an adrenaline-filled desert safari before driving to Abu Dhabi. The scenic beauty of the shifting sands sets the stage for a memorable transition to the capital.", ["Sightseeing Included: Desert safari, scenic drive to Abu Dhabi", "Overnight Stay: Abu Dhabi (Luxury Family Hotel)", "Meals Included: Breakfast & Desert BBQ Dinner"]),
            _day(4, "Abu Dhabi Cultural Immersion", "Visit the stunning Sheikh Zayed Grand Mosque and Louvre Abu Dhabi. This immersive experience brings together global art and breathtaking cultural beauty.", ["Sightseeing Included: Sheikh Zayed Grand Mosque, Louvre Abu Dhabi", "Overnight Stay: Abu Dhabi (Luxury Family Hotel)", "Meals Included: Breakfast"]),
            _day(5, "Ferrari World & Family Thrills", "A day of excitement at Ferrari World. Experience speed, luxury, and exclusive experiences designed for the whole family, leaving you with unforgettable memories.", ["Sightseeing Included: Ferrari World full-day visit", "Overnight Stay: Abu Dhabi (Luxury Family Hotel)", "Meals Included: Breakfast"]),
            _day(6, "Departure", "Final breakfast before your TRAGUIN assisted transfer to the airport. Your classic Dubai Abu Dhabi tour concludes with lasting memories.", ["Sightseeing Included: Private airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Atlantis, The Palm / similar", location="Dubai", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Address Downtown / similar", location="Dubai", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=2),
            ItineraryHotelNested(name="Emirates Palace / similar", location="Abu Dhabi", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="St. Regis Abu Dhabi / similar", location="Abu Dhabi", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=4),
        ],
        inclusions=_uae002_inclusions(),
    )
    return package, itinerary


def _uae002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in handpicked premium family hotels across Dubai and Abu Dhabi", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury van transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Dubai city tour — Burj Khalifa, Dubai Mall & Palm Jumeirah", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Desert safari with transfer to Abu Dhabi", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Sheikh Zayed Grand Mosque and Louvre Abu Dhabi visit", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Ferrari World full-day visit", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and UAE entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


def build_uae_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="uae-003-romantic-dubai-honeymoon",
        destination_id=destination_id,
        title="Romantic Dubai Honeymoon",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=77,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Dubai (5N) ultra-luxury honeymoon retreat", sort_order=1),
            PackageHighlightNested(text="Burj Khalifa & Dubai Mall luxury city experience", sort_order=2),
            PackageHighlightNested(text="Intimate desert safari with private BBQ under the stars", sort_order=3),
            PackageHighlightNested(text="Private sunset yacht cruise & couple's spa retreat", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-DXB-ROM-2026 | Serial UAE-003", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Adventure", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="uae-003-romantic-dubai-honeymoon-itinerary",
        destination_id=destination_id,
        title="Romantic Dubai Honeymoon",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Honeymoon Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Dubai • Burj Khalifa • Desert Safari • Palm Jumeirah • Yacht Cruise",
        overview=(
            "Begin your life together in the golden city of dreams with this TRAGUIN curated honeymoon. "
            "From private yacht sunsets to intimate desert dining, this romantic Dubai holiday promises "
            "unforgettable memories, breathtaking landscapes, and exclusive experiences."
        ),
        seo_title="UAE-003 | Romantic Dubai Honeymoon | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Dubai honeymoon package (UAE-003): Burj Khalifa, desert romance, "
            "private yacht cruise, and couple's spa retreat."
        ),
        is_featured=True,
        featured_sort_order=77,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Burj Khalifa & Luxury Shopping", sort_order=1),
            ItineraryHighlightNested(text="Intimate Desert Safari & BBQ Dinner", sort_order=2),
            ItineraryHighlightNested(text="Private Sunset Yacht Cruise", sort_order=3),
            ItineraryHighlightNested(text="Couple's Spa Retreat", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Dubai", "A romantic welcome to the City of Gold. Your private TRAGUIN transfer will escort you to your handpicked hotel. Enjoy a quiet evening admiring the scenic beauty of the Dubai Marina.", ["Sightseeing Included: VIP airport reception, private transfer", "Overnight Stay: Dubai (Ultra-Luxury Couple Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "City Luxury & Burj Khalifa", "Explore the heights of luxury. Visit the Burj Khalifa and indulge in high-end shopping at the Dubai Mall. A curated experience to admire the city's iconic attractions.", ["Sightseeing Included: Burj Khalifa, Dubai Mall luxury experience", "Overnight Stay: Dubai (Ultra-Luxury Couple Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Desert Romance", "Experience an intimate desert safari. Enjoy dune bashing, camel rides, and a private BBQ dinner under the stars — an exclusive experience for couples seeking breathtaking landscapes.", ["Sightseeing Included: Intimate desert safari, dune bashing, private BBQ dinner", "Overnight Stay: Dubai (Ultra-Luxury Couple Hotel)", "Meals Included: Breakfast & Private Desert BBQ Dinner"]),
            _day(4, "Yacht Cruise & Relaxation", "A private sunset yacht cruise, offering scenic beauty of the Dubai skyline. Spend your day enjoying premium stays and relaxation in the lap of luxury.", ["Sightseeing Included: Private sunset yacht cruise", "Overnight Stay: Dubai (Ultra-Luxury Couple Hotel)", "Meals Included: Breakfast"]),
            _day(5, "Leisure & Spa", "Indulge in a couple's spa retreat. Reflect on your unforgettable memories in Dubai with an evening at a world-class restaurant.", ["Sightseeing Included: Couple's spa retreat", "Evening Experience: World-class restaurant dinner", "Overnight Stay: Dubai (Ultra-Luxury Couple Hotel)", "Meals Included: Breakfast & Dinner"]),
            _day(6, "Departure", "Final breakfast and souvenir shopping before your TRAGUIN assisted transfer, concluding your premium Dubai experience.", ["Sightseeing Included: Private airport transfer, souvenir shopping time", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Burj Al Arab / similar", location="Dubai", nights_label="05 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Atlantis, The Palm / similar", location="Dubai", nights_label="05 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=2),
        ],
        inclusions=_uae003_inclusions(),
    )
    return package, itinerary


def _uae003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="05 Nights in handpicked ultra-luxury couple hotel in Dubai", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private chauffeur-driven luxury transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Burj Khalifa and Dubai Mall luxury city experience", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Intimate desert safari with private BBQ dinner under the stars", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Private sunset yacht cruise", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Couple's spa retreat", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated honeymoon concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and UAE entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


def build_uae_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="uae-004-luxury-dubai-tour",
        destination_id=destination_id,
        title="Luxury Dubai Tour",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=78,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Dubai (6N) ultimate luxury discovery", sort_order=1),
            PackageHighlightNested(text="Burj Khalifa & top-tier Dubai Mall luxury shopping", sort_order=2),
            PackageHighlightNested(text="Private desert oasis with falconry & gourmet dinner", sort_order=3),
            PackageHighlightNested(text="Private yacht cruise & Palm Jumeirah spa retreat", sort_order=4),
            PackageHighlightNested(text="Old Dubai heritage & gold souks cultural immersion", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-DXB-LUX-2026 | Serial UAE-004", sort_order=6),
        ],
        moods=["Luxury", "Family", "Adventure", "Cultural", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="uae-004-luxury-dubai-itinerary",
        destination_id=destination_id,
        title="Luxury Dubai Tour",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Ultra-Luxury Dubai Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Dubai • Burj Khalifa • Desert Oasis • Private Yacht • Palm Jumeirah",
        overview=(
            "Indulge in the zenith of opulence with TRAGUIN's curated luxury Dubai escape. Designed for the "
            "discerning traveler, this journey blends futuristic metropolitan glamour with serene coastal "
            "sanctuaries — with exclusive experiences, handpicked hotels, and unforgettable memories."
        ),
        seo_title="UAE-004 | Luxury Dubai Tour | TRAGUIN",
        seo_description=(
            "Ultra-luxury 06 Nights / 07 Days Dubai package (UAE-004): Burj Al Arab, private desert oasis, "
            "yacht cruise, Palm Jumeirah spa, and Old Dubai heritage."
        ),
        is_featured=True,
        featured_sort_order=78,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Burj Khalifa & Metropolitan Luxury", sort_order=1),
            ItineraryHighlightNested(text="Private Desert Oasis & Falconry", sort_order=2),
            ItineraryHighlightNested(text="Private Luxury Yacht Cruise", sort_order=3),
            ItineraryHighlightNested(text="Palm Jumeirah Spa Retreat", sort_order=4),
            ItineraryHighlightNested(text="Old Dubai & Gold Souks Heritage", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Dubai", "Your TRAGUIN luxury escape begins with a VIP chauffeur service. Experience true opulence from the moment you land, followed by a private transfer to your handpicked hotel.", ["Sightseeing Included: VIP chauffeur airport reception, private hotel transfer", "Overnight Stay: Dubai (Burj Al Arab / Armani Hotel)", "Meals Included: Welcome arrangements on arrival"]),
            _day(2, "Metropolitan Luxury", "Visit the iconic Burj Khalifa and experience top-tier luxury shopping at the Dubai Mall. A curated experience to admire the city's breathtaking landscapes.", ["Sightseeing Included: Burj Khalifa, Dubai Mall luxury shopping experience", "Overnight Stay: Dubai (Burj Al Arab / Armani Hotel)", "Meals Included: Breakfast"]),
            _day(3, "Desert Oasis Experience", "A private desert oasis experience. Indulge in exclusive experiences like a private falconry display and a gourmet dinner under the stars amidst breathtaking landscapes.", ["Sightseeing Included: Private desert oasis, falconry display, gourmet dinner", "Overnight Stay: Dubai (Burj Al Arab / Armani Hotel)", "Meals Included: Breakfast & Gourmet Desert Dinner"]),
            _day(4, "Private Yacht Cruise", "Savor the scenic beauty of the Dubai skyline with a private luxury yacht cruise. An immersive experience that defines our premium stays in Dubai.", ["Sightseeing Included: Private luxury yacht cruise", "Overnight Stay: Dubai (Burj Al Arab / Armani Hotel)", "Meals Included: Breakfast"]),
            _day(5, "Palm Jumeirah Retreat", "Relax at an iconic attraction — the Palm Jumeirah. Enjoy a spa day and world-class dining, creating unforgettable memories in ultimate luxury.", ["Sightseeing Included: Palm Jumeirah spa day", "Evening Experience: World-class dining", "Overnight Stay: Dubai (Burj Al Arab / Armani Hotel)", "Meals Included: Breakfast & Dinner"]),
            _day(6, "Culture & Heritage", "Discover old Dubai and the gold souks. This immersive experience contrasts with the modern city, showcasing the rich history of a premium Dubai experience.", ["Sightseeing Included: Old Dubai heritage tour, gold souks visit", "Overnight Stay: Dubai (Burj Al Arab / Armani Hotel)", "Meals Included: Breakfast"]),
            _day(7, "Departure", "Final luxury breakfast before your TRAGUIN chauffeur transfer, concluding your luxury Dubai holiday.", ["Sightseeing Included: VIP chauffeur airport transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Burj Al Arab", location="Dubai", nights_label="06 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Armani Hotel Dubai", location="Dubai", nights_label="06 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=2),
        ],
        inclusions=_uae004_inclusions(),
    )
    return package, itinerary


def _uae004_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="06 Nights in ultra-luxury hotel in Dubai", sort_order=1),
        ItineraryInclusionNested(kind="included", text="VIP chauffeur-driven luxury transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Burj Khalifa and Dubai Mall luxury experience", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private desert oasis with falconry display and gourmet dinner", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Private luxury yacht cruise", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Palm Jumeirah spa day and Old Dubai heritage tour", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated luxury travel concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and UAE entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


UAE_BUILDERS = [
    build_uae_001,
    build_uae_002,
    build_uae_003,
    build_uae_004,
]
