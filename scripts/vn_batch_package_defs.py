"""Builder functions for VN-001 through VN-005 Vietnam packages (no images)."""

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


def _vn_excluded() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="excluded", text="International airfare and Vietnam entry visa processing fees", sort_order=100),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=101),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=102),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=103),
    ]


def build_vn_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="vn-001-vietnam-explorer-family-tour",
        destination_id=destination_id,
        title="Vietnam Explorer Family Tour",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=82,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Hanoi (2N) → Halong Bay (2N) → Da Nang/Hoi An (3N) explorer circuit", sort_order=1),
            PackageHighlightNested(text="Hanoi heritage exploration & Old Quarter cultural vibe", sort_order=2),
            PackageHighlightNested(text="Ultra-luxury Halong Bay cruise with cave & cove adventures", sort_order=3),
            PackageHighlightNested(text="Hoi An Ancient Town UNESCO heritage & coastal celebration", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-VNM-EXP-2026 | Serial VN-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure", "Nature", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="vn-001-vietnam-explorer-itinerary",
        destination_id=destination_id,
        title="Vietnam Explorer Family Tour",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Vietnam Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Hanoi • Halong Bay • Da Nang • Hoi An • Scenic Heritage Discovery",
        overview=(
            "Discover the absolute best of Vietnam with TRAGUIN's curated family explorer expedition. From the "
            "historic northern charm of Hanoi and the emerald serenity of Halong Bay to the central coastal beauty "
            "of Da Nang and Hoi An, this comprehensive journey ensures unforgettable memories across this stunning nation."
        ),
        seo_title="VN-001 | Vietnam Explorer Family Tour | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Vietnam family explorer package (VN-001): Hanoi, Halong Bay cruise, "
            "Da Nang, and Hoi An Ancient Town."
        ),
        is_featured=True,
        featured_sort_order=82,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Hanoi Heritage & Old Quarter", sort_order=1),
            ItineraryHighlightNested(text="Ultra-Luxury Halong Bay Cruise", sort_order=2),
            ItineraryHighlightNested(text="Hoi An UNESCO Ancient Town", sort_order=3),
            ItineraryHighlightNested(text="Coastal Leisure & Farewell Gala", sort_order=4),
        ],
        days=_vn_explorer_highlights_days(explorer=True),
        hotels=_vn_explorer_hotels(),
        inclusions=_vn_family_8d_inclusions("explorer"),
    )
    return package, itinerary


def build_vn_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="vn-002-vietnam-highlights-family-tour",
        destination_id=destination_id,
        title="Vietnam Highlights Family Tour",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=83,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Hanoi (2N) → Halong Bay (2N) → Da Nang/Hoi An (3N) highlights circuit", sort_order=1),
            PackageHighlightNested(text="Hanoi city highlights & historic Old Quarter", sort_order=2),
            PackageHighlightNested(text="Halong Bay ultra-luxury cruise through limestone karsts", sort_order=3),
            PackageHighlightNested(text="Hoi An lantern-lit streets & beachfront farewell gala", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-VNM-HIG-2026 | Serial VN-002", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Adventure", "Nature", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="vn-002-vietnam-highlights-itinerary",
        destination_id=destination_id,
        title="Vietnam Highlights Family Tour",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Vietnam Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Hanoi • Halong Bay Cruise • Hoi An Ancient Town • Da Nang Beaches",
        overview=(
            "Discover the absolute highlights of Vietnam with TRAGUIN's curated family expedition. This comprehensive "
            "8-day journey takes your family through the vibrant capital of Hanoi, the serene majesty of Halong Bay, "
            "and the cultural charm of Hoi An and Da Nang — creating unforgettable memories across Vietnam's iconic landscapes."
        ),
        seo_title="VN-002 | Vietnam Highlights Family Tour | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Vietnam family highlights package (VN-002): Hanoi, Halong Bay, "
            "Hoi An Ancient Town, and Da Nang beaches."
        ),
        is_featured=True,
        featured_sort_order=83,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Hanoi Highlights City Tour", sort_order=1),
            ItineraryHighlightNested(text="Halong Bay Limestone Karst Cruise", sort_order=2),
            ItineraryHighlightNested(text="Hoi An Ancient Town Lantern Streets", sort_order=3),
            ItineraryHighlightNested(text="Beachfront Farewell Dinner Gala", sort_order=4),
        ],
        days=_vn_explorer_highlights_days(explorer=False),
        hotels=_vn_highlights_hotels(),
        inclusions=_vn_family_8d_inclusions("highlights"),
    )
    return package, itinerary


def _vn_explorer_highlights_days(*, explorer: bool) -> list[ItineraryDayNested]:
    day2_title = "Hanoi Heritage Exploration" if explorer else "Hanoi Highlights"
    day2_desc = (
        "Guided city tour of Hanoi's most significant cultural and historical landmarks. "
        "A perfect educational introduction to Vietnam's heritage."
        if explorer
        else "A comprehensive city tour covering Hanoi's most famous landmarks, providing a rich educational experience for your family."
    )
    day3_title = "Halong Bay Cruise Commencement" if explorer else "Halong Bay Cruise"
    day4_desc = (
        "Enjoy exclusive activities aboard the cruise, including cave exploration, swimming in hidden coves, "
        "and spectacular sunset deck views — unforgettable memories."
        if explorer
        else "Explore hidden caves and enjoy guided activities on the water. A day filled with unforgettable memories and stunning views."
    )
    day6_title = "Ancient Town & Cultural Magic" if explorer else "Hoi An Ancient Town"
    day7_desc = (
        "A day of leisure at your coastal resort, followed by a grand farewell dinner celebrating your premium Vietnam family explorer expedition."
        if explorer
        else "A relaxing day at the resort, followed by a grand farewell dinner gala at a beachfront restaurant — an exclusive experience for the family."
    )
    return [
        _day(1, "Arrival in Hanoi", "Arrive in Hanoi. Private transfer to your handpicked premium hotel. Evening at leisure in the historic Old Quarter.", ["Sightseeing Included: VIP airport reception, private hotel transfer", "Overnight Stay: Hanoi (Premium Heritage Hotel)", "Meals Included: Welcome arrangements on arrival"]),
        _day(2, day2_title, day2_desc, ["Sightseeing Included: Guided Hanoi city tour", "Overnight Stay: Hanoi (Premium Heritage Hotel)", "Meals Included: Premium Breakfast"]),
        _day(3, day3_title, "Travel to Halong Bay. Board your ultra-luxury cruise vessel for an extraordinary journey through the limestone islands with gourmet dining.", ["Sightseeing Included: Transfer to Halong Bay, ultra-luxury cruise boarding", "Overnight Stay: Halong Bay (Ultra-Luxury Cruise)", "Meals Included: Premium Breakfast & Gourmet Cruise Dinner"]),
        _day(4, "Halong Bay Adventure", day4_desc, ["Sightseeing Included: Cave exploration, water activities, sunset deck views", "Overnight Stay: Halong Bay (Ultra-Luxury Cruise)", "Meals Included: Premium Breakfast & Gourmet Cruise Dining"]),
        _day(5, "Flight to Da Nang & Hoi An", "Morning cruise brunch. Transfer to the airport for your flight to Da Nang. Check into your luxury coastal family resort in Hoi An.", ["Sightseeing Included: Cruise brunch, domestic flight to Da Nang, resort transfer", "Overnight Stay: Hoi An/Da Nang (Luxury Coastal Resort)", "Meals Included: Premium Breakfast & Cruise Brunch"]),
        _day(6, day6_title, "A guided tour of Hoi An's Ancient Town, a UNESCO World Heritage site known for its charming architecture, night markets, and traditional lanterns.", ["Sightseeing Included: Hoi An Ancient Town guided tour", "Overnight Stay: Hoi An/Da Nang (Luxury Coastal Resort)", "Meals Included: Premium Breakfast"]),
        _day(7, "Coastal Leisure & Celebration", day7_desc, ["Evening Experience: Grand farewell dinner gala", "Overnight Stay: Hoi An/Da Nang (Luxury Coastal Resort)", "Meals Included: Premium Breakfast & Farewell Dinner"]),
        _day(8, "Departure", "Final breakfast before your TRAGUIN private transfer to the airport, completing your premium Vietnam journey.", ["Sightseeing Included: Private airport transfer", "Meals Included: Premium Breakfast"]),
    ]


def _vn_explorer_hotels() -> list[ItineraryHotelNested]:
    return [
        ItineraryHotelNested(name="Selected Heritage Hotels / similar", location="Hanoi", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
        ItineraryHotelNested(name="Ultra-Luxury Cruise Vessel / similar", location="Halong Bay", nights_label="02 Nights", category_label="Premium", meal_plan="Full Board", stars=5, sort_order=2),
        ItineraryHotelNested(name="Luxury Coastal Resort / similar", location="Hoi An/Da Nang", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
    ]


def _vn_highlights_hotels() -> list[ItineraryHotelNested]:
    return [
        ItineraryHotelNested(name="Heritage City Hotels / similar", location="Hanoi", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
        ItineraryHotelNested(name="Ultra-Luxury Cruise / similar", location="Halong Bay", nights_label="02 Nights", category_label="Premium", meal_plan="Full Board", stars=5, sort_order=2),
        ItineraryHotelNested(name="Luxury Beachfront Resort / similar", location="Hoi An/Da Nang", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
    ]


def _vn_family_8d_inclusions(variant: str) -> list[ItineraryInclusionNested]:
    label = "explorer" if variant == "explorer" else "highlights"
    return [
        ItineraryInclusionNested(kind="included", text=f"07 Nights in handpicked premium family stays across Hanoi, Halong Bay, and Hoi An/Da Nang ({label} route)", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private executive chauffeur-driven luxury ground transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Domestic flight Da Nang sector and Halong Bay ultra-luxury cruise", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Guided Hanoi city tour and Hoi An Ancient Town visit", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Halong Bay cave exploration and onboard activities", sort_order=5),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=6),
        *_vn_excluded(),
    ]


def build_vn_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="vn-003-romantic-vietnam-couple-tour",
        destination_id=destination_id,
        title="Romantic Vietnam Couple Tour",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=84,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Hanoi (2N) → Halong Bay (2N) → Hoi An (1N) romantic sanctuary", sort_order=1),
            PackageHighlightNested(text="Intimate Hanoi welcome dinner & slow-paced cultural harmony", sort_order=2),
            PackageHighlightNested(text="Ultra-luxury private Halong Bay cruise with candlelit dinners", sort_order=3),
            PackageHighlightNested(text="Hoi An lantern-lit Ancient Town magic at night", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-VNM-ROM-2026 | Serial VN-003", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Cultural", "Nature", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="vn-003-romantic-vietnam-itinerary",
        destination_id=destination_id,
        title="Romantic Vietnam Couple Tour",
        duration_label="05 Nights / 06 Days",
        duration_days=6,
        starting_price=0,
        price_note="On Request (Premium Honeymoon Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Hanoi Charm • Halong Bay Private Cruise • Hoi An Romantic Streets",
        overview=(
            "Begin your romantic journey together in the enchanting landscapes of Vietnam. This TRAGUIN curated "
            "couple's sanctuary blends the colonial charm of Hanoi, the serene luxury of a private cruise in Halong Bay, "
            "and the intimate streets of Hoi An — ensuring unforgettable memories in a truly romantic setting."
        ),
        seo_title="VN-003 | Romantic Vietnam Couple Tour | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Vietnam honeymoon package (VN-003): Hanoi, private Halong Bay cruise, "
            "and Hoi An lantern magic."
        ),
        is_featured=True,
        featured_sort_order=84,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Intimate Hanoi Welcome Dinner", sort_order=1),
            ItineraryHighlightNested(text="Private Halong Bay Cruise", sort_order=2),
            ItineraryHighlightNested(text="Sunset Deck & Candlelit Cruise Dinner", sort_order=3),
            ItineraryHighlightNested(text="Hoi An Lantern-Lit Ancient Town", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Hanoi & Intimate Welcome", "Arrive in Hanoi. Private transfer to your intimate boutique hotel. Savor a quiet, romantic welcome dinner in the heart of the city.", ["Sightseeing Included: Private transfer, romantic welcome dinner", "Overnight Stay: Hanoi (Boutique Heritage Hotel)", "Meals Included: Welcome Dinner"]),
            _day(2, "Hanoi Cultural Harmony", "A slow-paced, romantic exploration of Hanoi's hidden streets, museums, and local charms, perfect for couples wanting to discover cultural richness.", ["Sightseeing Included: Slow-paced Hanoi cultural exploration", "Overnight Stay: Hanoi (Boutique Heritage Hotel)", "Meals Included: Premium Breakfast"]),
            _day(3, "Halong Bay Private Cruise", "Transfer to Halong Bay. Board your ultra-luxury private cruise vessel for an intimate getaway on the emerald waters.", ["Sightseeing Included: Transfer to Halong Bay, private cruise boarding", "Overnight Stay: Halong Bay (Ultra-Luxury Private Cruise)", "Meals Included: Premium Breakfast & Gourmet Cruise Dinner"]),
            _day(4, "Halong Bay Serenity", "A day of private exploration, featuring sunset deck relaxation, cave visits, and candlelit dinners under the stars — unforgettable memories.", ["Sightseeing Included: Cave visits, sunset deck relaxation, candlelit dinner", "Overnight Stay: Halong Bay (Ultra-Luxury Private Cruise)", "Meals Included: Premium Breakfast & Candlelit Dinner"]),
            _day(5, "Hoi An Lantern Magic", "Flight to Da Nang, followed by a romantic transfer to Hoi An. Experience the magic of the lantern-lit Ancient Town at night.", ["Sightseeing Included: Domestic flight to Da Nang, Hoi An Ancient Town evening visit", "Overnight Stay: Hoi An (Romantic Resort Retreat)", "Meals Included: Premium Breakfast"]),
            _day(6, "Departure", "Final luxury breakfast before your TRAGUIN private transfer, completing your premium romantic Vietnam sojourn.", ["Sightseeing Included: Private airport transfer", "Meals Included: Premium Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Boutique Heritage Hotels / similar", location="Hanoi", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Ultra-Luxury Private Cruise / similar", location="Halong Bay", nights_label="02 Nights", category_label="Premium", meal_plan="Full Board", stars=5, sort_order=2),
            ItineraryHotelNested(name="Romantic Resort Retreat / similar", location="Hoi An", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
        ],
        inclusions=[
            ItineraryInclusionNested(kind="included", text="05 Nights in handpicked romantic hotels and private cruise across Hanoi, Halong Bay, and Hoi An", sort_order=1),
            ItineraryInclusionNested(kind="included", text="Private chauffeur-driven luxury transfers throughout", sort_order=2),
            ItineraryInclusionNested(kind="included", text="Ultra-luxury private Halong Bay cruise with candlelit dining", sort_order=3),
            ItineraryInclusionNested(kind="included", text="Domestic flight to Da Nang and Hoi An Ancient Town evening experience", sort_order=4),
            ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated honeymoon concierge support", sort_order=5),
            *_vn_excluded(),
        ],
    )
    return package, itinerary


def build_vn_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="vn-004-luxury-vietnam-tour",
        destination_id=destination_id,
        title="Luxury Vietnam Tour",
        duration_label="06 Nights / 07 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=85,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Hanoi (2N) → Halong Bay (2N) → Da Nang/Hoi An (2N) ultra-luxury circuit", sort_order=1),
            PackageHighlightNested(text="VIP Hanoi arrival & exclusive heritage private tour", sort_order=2),
            PackageHighlightNested(text="Ultra-luxury Halong Bay cruise with spa & gourmet dining", sort_order=3),
            PackageHighlightNested(text="Hoi An private discovery & farewell gala dinner", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 luxury travel concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-VNM-LUX-2026 | Serial VN-004", sort_order=6),
        ],
        moods=["Luxury", "Family", "Cultural", "Nature", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="vn-004-luxury-vietnam-itinerary",
        destination_id=destination_id,
        title="Luxury Vietnam Tour",
        duration_label="06 Nights / 07 Days",
        duration_days=7,
        starting_price=0,
        price_note="On Request (Ultra-Luxury Vietnam Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Hanoi • Ultra-Luxury Halong Bay Cruise • Da Nang • Exclusive Heritage Tours",
        overview=(
            "Indulge in the absolute height of sophistication across Vietnam with TRAGUIN's curated luxury expedition. "
            "From opulent five-star stays and private cruises to exclusive cultural tours and premium concierge service, "
            "this journey is designed for the discerning traveler — ensuring unforgettable memories in ultimate luxury."
        ),
        seo_title="VN-004 | Luxury Vietnam Tour | TRAGUIN",
        seo_description=(
            "Ultra-luxury 06 Nights / 07 Days Vietnam package (VN-004): Sofitel Legend Metropole Hanoi, "
            "elite Halong Bay cruise, and InterContinental Danang Resort."
        ),
        is_featured=True,
        featured_sort_order=85,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="VIP Arrival & Gourmet Hanoi Welcome", sort_order=1),
            ItineraryHighlightNested(text="Exclusive Private Hanoi Heritage Tour", sort_order=2),
            ItineraryHighlightNested(text="Ultra-Luxury Halong Bay Cruise & Spa", sort_order=3),
            ItineraryHighlightNested(text="Hoi An Private Discovery & Gala Dinner", sort_order=4),
        ],
        days=[
            _day(1, "VIP Arrival & Hanoi Luxury", "Arrive in Hanoi. VIP chauffeur transfer to your world-class hotel. Evening gourmet welcome dinner overlooking the historic city center.", ["Sightseeing Included: VIP chauffeur airport reception", "Evening Experience: Gourmet welcome dinner", "Overnight Stay: Hanoi (Sofitel Legend Metropole Hanoi)", "Meals Included: Welcome Dinner"]),
            _day(2, "Exclusive Hanoi Heritage", "Private guided tour of Hanoi's most prestigious historical landmarks, providing a rich exclusive experience of Vietnamese culture.", ["Sightseeing Included: Private guided Hanoi heritage tour", "Overnight Stay: Hanoi (Sofitel Legend Metropole Hanoi)", "Meals Included: Premium Breakfast"]),
            _day(3, "Ultra-Luxury Cruise Commencement", "Transfer to Halong Bay. Board your ultra-luxury cruise vessel. Experience gourmet dining while sailing through breathtaking limestone islands.", ["Sightseeing Included: VIP transfer to Halong Bay, elite cruise boarding", "Overnight Stay: Halong Bay (Elite Cruise Vessel)", "Meals Included: Premium Breakfast & Gourmet Cruise Dinner"]),
            _day(4, "Halong Bay Serenity", "Enjoy personalized activities, spa therapies, and gourmet relaxation aboard your vessel, surrounded by stunning scenery.", ["Sightseeing Included: Personalized cruise activities and spa therapies", "Overnight Stay: Halong Bay (Elite Cruise Vessel)", "Meals Included: Premium Breakfast & Gourmet Cruise Dining"]),
            _day(5, "Flight to Da Nang", "Morning brunch on the cruise. Private transfer to airport for your flight to Da Nang. Check into an ultra-luxury coastal resort.", ["Sightseeing Included: Cruise brunch, domestic flight to Da Nang, VIP resort transfer", "Overnight Stay: Da Nang/Hoi An (InterContinental Danang Resort)", "Meals Included: Premium Breakfast & Cruise Brunch"]),
            _day(6, "Hoi An Private Discovery", "Private guided exploration of Hoi An's Ancient Town, focusing on premium crafts and historical charm. Evening farewell gala dinner.", ["Sightseeing Included: Private Hoi An Ancient Town tour", "Evening Experience: Farewell gala dinner", "Overnight Stay: Da Nang/Hoi An (InterContinental Danang Resort)", "Meals Included: Premium Breakfast & Gala Dinner"]),
            _day(7, "Departure", "Final luxury breakfast. VIP chauffeur transfer to the airport, concluding your premium Vietnam luxury expedition.", ["Sightseeing Included: VIP chauffeur airport transfer", "Meals Included: Premium Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Sofitel Legend Metropole Hanoi", location="Hanoi", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Elite Cruise Vessels / similar", location="Halong Bay", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Full Board", stars=5, sort_order=2),
            ItineraryHotelNested(name="InterContinental Danang Resort", location="Da Nang/Hoi An", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=3),
        ],
        inclusions=[
            ItineraryInclusionNested(kind="included", text="06 Nights in ultra-luxury hotels and elite cruise across Hanoi, Halong Bay, and Da Nang/Hoi An", sort_order=1),
            ItineraryInclusionNested(kind="included", text="VIP chauffeur-driven luxury ground transfers throughout", sort_order=2),
            ItineraryInclusionNested(kind="included", text="Ultra-luxury Halong Bay cruise with spa therapies and gourmet dining", sort_order=3),
            ItineraryInclusionNested(kind="included", text="Private Hanoi heritage tour and Hoi An private discovery", sort_order=4),
            ItineraryInclusionNested(kind="included", text="Domestic flight to Da Nang", sort_order=5),
            ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated luxury travel concierge support", sort_order=6),
            *_vn_excluded(),
        ],
    )
    return package, itinerary


def build_vn_005(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="vn-005-vietnam-ladies-escape",
        destination_id=destination_id,
        title="Vietnam Ladies Escape",
        duration_label="05 Nights / 06 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=86,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Hanoi (3N) → Coastal Sanctuary (2N) premium ladies retreat", sort_order=1),
            PackageHighlightNested(text="Chic Hanoi shopping gems & fashion boutique tour", sort_order=2),
            PackageHighlightNested(text="Exclusive Vietnamese culinary masterclass", sort_order=3),
            PackageHighlightNested(text="Coastal spa rejuvenation & farewell gala under the stars", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 ladies retreat concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-VNM-LAD-2026 | Serial VN-005", sort_order=6),
        ],
        moods=["Solo", "Luxury", "Cultural", "Beach", "Spiritual"],
    )
    itinerary = ItineraryCreate(
        slug="vn-005-vietnam-ladies-escape-itinerary",
        destination_id=destination_id,
        title="Vietnam Ladies Escape",
        duration_label="05 Nights / 06 Days",
        starting_price=0,
        price_note="On Request (Premium Ladies Retreat Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        duration_days=6,
        tagline="Hanoi Shopping • Boutique Stays • Culinary Masterclasses • Coastal Relaxation",
        overview=(
            "Rejuvenate, explore, and bond with TRAGUIN's curated Vietnam Ladies Escape. Designed for style and "
            "relaxation, this journey combines the chic boutiques of Hanoi, private culinary masterclasses, and "
            "ultimate coastal rejuvenation — ensuring unforgettable memories in the most elegant corners of Vietnam."
        ),
        seo_title="VN-005 | Vietnam Ladies Escape | TRAGUIN",
        seo_description=(
            "Premium 05 Nights / 06 Days Vietnam ladies retreat (VN-005): Hanoi shopping, culinary masterclass, "
            "and coastal spa rejuvenation."
        ),
        is_featured=True,
        featured_sort_order=86,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Stylish Hanoi Welcome Dinner", sort_order=1),
            ItineraryHighlightNested(text="Chic Shopping & Fashion Boutiques", sort_order=2),
            ItineraryHighlightNested(text="Private Vietnamese Culinary Masterclass", sort_order=3),
            ItineraryHighlightNested(text="Coastal Spa & Farewell Gala", sort_order=4),
        ],
        days=[
            _day(1, "Arrival in Hanoi & Style Welcome", "Arrive in Hanoi. Private chauffeur transfer to a handpicked boutique hotel. Evening welcome dinner in a stylish, garden-setting restaurant.", ["Sightseeing Included: Private chauffeur transfer, stylish welcome dinner", "Overnight Stay: Hanoi (Boutique Heritage Hotel)", "Meals Included: Welcome Dinner"]),
            _day(2, "Chic Shopping & Hanoi Charm", "A guided tour of Hanoi's hidden shopping gems and chic fashion boutiques. Perfect for a day of style and discovery, creating unforgettable memories.", ["Sightseeing Included: Guided shopping and boutique tour", "Overnight Stay: Hanoi (Boutique Heritage Hotel)", "Meals Included: Premium Breakfast"]),
            _day(3, "Culinary Masterclass", "Join an exclusive culinary masterclass, learning to prepare authentic Vietnamese dishes in a beautiful, private garden setting.", ["Sightseeing Included: Private Vietnamese culinary masterclass", "Overnight Stay: Hanoi (Boutique Heritage Hotel)", "Meals Included: Premium Breakfast & Masterclass Lunch"]),
            _day(4, "Coastal Rejuvenation", "Transfer to a pristine coastal sanctuary. Spend the day indulging in personalized spa therapies and relaxation by the private beach — a premium retreat.", ["Sightseeing Included: Transfer to coastal sanctuary, personalized spa therapies", "Overnight Stay: Coastal Sanctuary (Luxury Resort & Spa)", "Meals Included: Premium Breakfast"]),
            _day(5, "Coastal Leisure & Farewell Gala", "Final day of coastal leisure and boutique shopping, followed by a grand farewell gala dinner under the stars, celebrating the perfect ladies' escape.", ["Evening Experience: Grand farewell gala dinner under the stars", "Overnight Stay: Coastal Sanctuary (Luxury Resort & Spa)", "Meals Included: Premium Breakfast & Gala Dinner"]),
            _day(6, "Departure", "Final luxury breakfast before your TRAGUIN private chauffeur transfer to the airport, completing your premium Vietnam retreat.", ["Sightseeing Included: Private chauffeur airport transfer", "Meals Included: Premium Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Boutique Heritage Hotels / similar", location="Hanoi", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Luxury Coastal Resort & Spa / similar", location="Coastal Sanctuary", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=2),
        ],
        inclusions=[
            ItineraryInclusionNested(kind="included", text="05 Nights in handpicked boutique hotels across Hanoi and a coastal sanctuary", sort_order=1),
            ItineraryInclusionNested(kind="included", text="Private chauffeur-driven luxury transfers throughout", sort_order=2),
            ItineraryInclusionNested(kind="included", text="Guided Hanoi shopping and fashion boutique tour", sort_order=3),
            ItineraryInclusionNested(kind="included", text="Exclusive private Vietnamese culinary masterclass", sort_order=4),
            ItineraryInclusionNested(kind="included", text="Personalized spa therapies and coastal rejuvenation", sort_order=5),
            ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated ladies retreat concierge support", sort_order=6),
            *_vn_excluded(),
        ],
    )
    return package, itinerary


VN_BUILDERS = [
    build_vn_001,
    build_vn_002,
    build_vn_003,
    build_vn_004,
    build_vn_005,
]
