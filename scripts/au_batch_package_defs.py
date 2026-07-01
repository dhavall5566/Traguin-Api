"""Builder functions for AU-001 through AU-004 Australia packages (no images)."""

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


def build_au_001(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="au-001-australia-highlights-family-tour",
        destination_id=destination_id,
        title="Australia Highlights Family Tour",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=30,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Sydney (3N) → Cairns (2N) → Gold Coast (2N) family circuit", sort_order=1),
            PackageHighlightNested(text="Sydney Opera House, Taronga Zoo & Blue Mountains", sort_order=2),
            PackageHighlightNested(text="Great Barrier Reef luxury snorkel expedition", sort_order=3),
            PackageHighlightNested(text="Gold Coast beaches & theme park VIP access", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 dedicated family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-AUS-HIGHLIGHTS-2026 | Serial AU-001", sort_order=6),
        ],
        moods=["Family", "Luxury", "Nature", "Wildlife", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="au-001-australia-highlights-itinerary",
        destination_id=destination_id,
        title="Australia Highlights Family Tour",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Australia Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Sydney • Great Barrier Reef • Gold Coast",
        overview=(
            "Embark on an epic Southern Hemisphere journey with TRAGUIN's curated Australian family expedition. "
            "Blending the iconic skyline of Sydney, the marine wonders of the Great Barrier Reef, and the vibrant coastal "
            "surf culture of the Gold Coast, this luxury Australia holiday offers unforgettable memories, breathtaking "
            "landscapes, and exclusive experiences for your family. Includes private executive vehicle transits, "
            "pre-vetted family-friendly accommodation hubs, and skip-the-line group entry protocols backed by 24/7 "
            "on-ground concierge support. Best season: September to April."
        ),
        seo_title="AU-001 | Australia Highlights Family Tour | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Australia family package (AU-001): Sydney Opera House, Great Barrier Reef, "
            "Blue Mountains, Taronga Zoo, and Gold Coast theme parks."
        ),
        is_featured=True,
        featured_sort_order=30,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Sydney Opera House Private Tour", sort_order=1),
            ItineraryHighlightNested(text="Great Barrier Reef Snorkel Cruise", sort_order=2),
            ItineraryHighlightNested(text="Blue Mountains & Three Sisters", sort_order=3),
            ItineraryHighlightNested(text="Taronga Zoo Wildlife Encounter", sort_order=4),
            ItineraryHighlightNested(text="Gold Coast Theme Park Express Entry", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Sydney & Harbour Welcome", "Private chauffeur transfer to your waterfront hotel. Evening walk around Circular Quay with views of the Sydney Opera House and Harbour Bridge.", ["Sightseeing Included: VIP airport reception, Circular Quay orientation walk", "Evening Experience: Family welcome dinner at upscale waterfront restaurant", "Overnight Stay: Sydney Harbour (Premium Family Hotel)", "Meals Included: International Welcome Buffet Dinner"]),
            _day(2, "Sydney Icons & Wildlife Encounter", "Private tour of the Sydney Opera House. Afternoon at Taronga Zoo with koalas and kangaroos.", ["Sightseeing Included: Opera House guided tour, Taronga Zoo wildlife encounter", "Overnight Stay: Sydney Harbour (Premium Family Hotel)", "Meals Included: Breakfast & Casual Lunch"]),
            _day(3, "Blue Mountains Adventure", "Day trip to the Blue Mountains including Three Sisters viewpoint and Scenic World railway and cable car adventures.", ["Sightseeing Included: Blue Mountains tour, Three Sisters viewpoint, Scenic World adventure passes", "Overnight Stay: Sydney Harbour (Premium Family Hotel)", "Meals Included: Breakfast & Picnic Lunch"]),
            _day(4, "Sydney to Cairns & Reef Gateway", "Fly to Cairns and check into your tropical resort. Relaxed afternoon by the pool or Cairns Esplanade stroll.", ["Sightseeing Included: Flight transit, tropical resort check-in", "Overnight Stay: Cairns (Luxury Family Resort)", "Meals Included: Breakfast & Dinner"]),
            _day(5, "Great Barrier Reef Expedition", "Luxury vessel cruise to the Great Barrier Reef with snorkeling in pristine coral waters.", ["Sightseeing Included: Private cruise to Great Barrier Reef, snorkeling activities", "Overnight Stay: Cairns (Luxury Family Resort)", "Meals Included: Breakfast & Buffet Reef Lunch"]),
            _day(6, "Cairns to Gold Coast Beaches", "Fly to the Gold Coast and check into a beachfront resort. Afternoon at Surfers Paradise beach.", ["Sightseeing Included: Flight transit, beachfront relaxation time", "Overnight Stay: Gold Coast (Premium Beachfront Resort)", "Meals Included: Breakfast & Dinner"]),
            _day(7, "Gold Coast Theme Park Fun", "Full day at a famous Gold Coast theme park with express entry. Grand farewell gala dinner.", ["Sightseeing Included: Theme park day pass, express entry", "Evening Experience: Grand farewell gala dinner party", "Overnight Stay: Gold Coast (Premium Beachfront Resort)", "Meals Included: Breakfast & Farewell Dinner"]),
            _day(8, "Departure", "Final luxury breakfast before private airport transfer.", ["Sightseeing Included: Private airport transit, luggage assistance", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Pier One Sydney Harbour / similar", location="Sydney", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Pullman Reef Hotel Casino / similar", location="Cairns", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Mantra Legends Surfers Paradise / similar", location="Gold Coast", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Shangri-La Sydney", location="Sydney", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Crystalbrook Riley", location="Cairns", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Sheraton Grand Mirage", location="Gold Coast", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Crown Towers Sydney", location="Sydney", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Silky Oaks Lodge", location="Cairns / Port Douglas", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="The Darling", location="Gold Coast", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Park Hyatt Sydney", location="Sydney", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="Pullman Reef Hotel", location="Cairns", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
            ItineraryHotelNested(name="The Langham Gold Coast", location="Gold Coast", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
        ],
        inclusions=_au001_inclusions(),
    )
    return package, itinerary


def _au001_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in handpicked premium family hotels across Sydney, Cairns, and Gold Coast", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private executive chauffeur-driven luxury ground transfers", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Domestic flight coordination between Sydney, Cairns, and Gold Coast sectors", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Great Barrier Reef luxury cruise with snorkeling activities", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Theme park express entry passes on Gold Coast", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Skip-the-line group entry protocols to major parks and attractions", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated on-ground family concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Australia entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


def build_au_002(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="au-002-romantic-australia-honeymoon",
        destination_id=destination_id,
        title="Romantic Australia Honeymoon Sanctuary",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=31,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Sydney (3N) → Port Douglas (2N) → Whitsundays (2N) romantic circuit", sort_order=1),
            PackageHighlightNested(text="Private harbour sunset cruise with sparkling wine welcome", sort_order=2),
            PackageHighlightNested(text="Great Barrier Reef private helicopter & sand cay snorkel", sort_order=3),
            PackageHighlightNested(text="Whitehaven Beach & private candlelight island dinner", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 honeymoon concierge desk support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-AUS-ROM-2026 | Serial AU-002", sort_order=6),
        ],
        moods=["Romantic", "Luxury", "Nature", "Beach"],
    )
    itinerary = ItineraryCreate(
        slug="au-002-romantic-australia-itinerary",
        destination_id=destination_id,
        title="Romantic Australia Honeymoon Sanctuary",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Ultra-Luxury Romantic Sanctuary)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Sydney • Daintree • Whitsunday Islands",
        overview=(
            "Begin your lifelong love story amid the most dramatic and sun-drenched landscapes of the southern hemisphere "
            "with this signature TRAGUIN curated honeymoon retreat. Intimate harbour sunset cruises, private rainforest "
            "canopy walks, and isolated sapphire-water island escapes guarantee unforgettable memories. Includes private "
            "luxury harbour vessels, executive ground transits, skip-the-line VIP sanctuary admissions, and private "
            "dining terraces overlooking iconic Australian horizons with 24/7 concierge support."
        ),
        seo_title="AU-002 | Romantic Australia Honeymoon Sanctuary | TRAGUIN",
        seo_description=(
            "Luxury 07 Nights / 08 Days Australia honeymoon (AU-002): Sydney harbour cruise, Daintree Rainforest, "
            "Great Barrier Reef helicopter flight, and Whitsunday Islands private escape."
        ),
        is_featured=True,
        featured_sort_order=31,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Private Sydney Harbour Sunset Cruise", sort_order=1),
            ItineraryHighlightNested(text="Daintree Rainforest Canopy Walk", sort_order=2),
            ItineraryHighlightNested(text="Great Barrier Reef Helicopter Flight", sort_order=3),
            ItineraryHighlightNested(text="Whitehaven Beach Private Escape", sort_order=4),
            ItineraryHighlightNested(text="Secluded Beach Candlelight Finale Dinner", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Sydney & Private Harbour Cruise", "VIP airport transfer to harbour-view hotel. Evening private sunset cruise past Opera House and Harbour Bridge with sparkling wine welcome in suite.", ["Sightseeing Included: VIP airport reception, private luxury vessel sunset harbor cruise", "Honeymoon Highlight: Complimentary chilled Australian sparkling wine and rose petals in suite", "Overnight Stay: Sydney Harbour (Ultra-Luxury Harbor-view Hotel)", "Meals Included: Harbor Cruise Gourmet Welcome Dinner"]),
            _day(2, "Sydney Icons & Coastal Cliff Walks", "Private Opera House tour and Bondi to Coogee coastal cliff walk. Rooftop harbour dinner.", ["Sightseeing Included: Private Opera House guided tour, Bondi coastal cliff walk", "Overnight Stay: Sydney Harbour (Ultra-Luxury Harbor-view Hotel)", "Meals Included: International Breakfast & Casual Coastal Bistro Lunch"]),
            _day(3, "Fly to Cairns & Daintree Rainforest", "Flight to Cairns and private transfer to Daintree Rainforest for guided canopy walk.", ["Sightseeing Included: Private executive transit to Daintree Rainforest, guided canopy walk", "Overnight Stay: Port Douglas / Daintree (Luxury Boutique Rainforest Retreat)", "Meals Included: International Breakfast & Rainforest Gastronomy Dinner"]),
            _day(4, "Great Barrier Reef Helicopter Expedition", "Private helicopter flight over the reef with sand cay landing and exclusive snorkeling session.", ["Sightseeing Included: Private helicopter reef flight, private sand cay snorkeling session", "Overnight Stay: Port Douglas / Daintree (Luxury Boutique Rainforest Retreat)", "Meals Included: International Breakfast & Gourmet Reef Picnic Lunch"]),
            _day(5, "Whitsunday Islands Private Escape", "Flight to Whitsundays. Afternoon on Whitehaven Beach with pristine silica sand and turquoise waters.", ["Sightseeing Included: Private island transit, Whitehaven Beach exploration", "Overnight Stay: Whitsunday Islands (Ultra-Luxury Private Island Resort)", "Meals Included: International Breakfast & Island Beachside Dinner"]),
            _day(6, "Isolated Beach Gala & Stargazing", "Private luxury vessel to secret beach picnic. Candlelight farewell dinner under southern stars with acoustic music.", ["Sightseeing Included: Private luxury beach picnic, sunset stargazing gala", "Honeymoon Finale: Candlelight farewell dinner with acoustic music performance", "Overnight Stay: Whitsunday Islands (Ultra-Luxury Private Island Resort)", "Meals Included: International Breakfast & Grand Honeymoon Finale Candlelight Dinner"]),
            _day(7, "Sunset Checkout & Sydney Departure Transit", "Final Whitsunday breakfast. Private vessel and luxury van transfer to airport for Sydney transit night.", ["Transfers: Private island boat and luxury van departure transit, luggage assistance", "Overnight Stay: Sydney Harbour (Premium Luxury Hotel near Airport)", "Meals Included: International Buffet Breakfast"]),
            _day(8, "Farewell Australia", "Final luxury breakfast before private departure transfer.", ["Transfers: Private luxury van departure transfer", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Pullman Quay Grand Sydney Harbour / similar", location="Sydney", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Pullman Reef Hotel Casino / similar", location="Port Douglas", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Reef View Hotel / similar", location="Whitsunday Islands", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=3),
            ItineraryHotelNested(name="Shangri-La Sydney", location="Sydney", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Crystalbrook Riley", location="Port Douglas", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Hamilton Island Resort", location="Whitsunday Islands", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Crown Towers Sydney", location="Sydney", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Silky Oaks Lodge", location="Port Douglas", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="InterContinental Hayman Island", location="Whitsunday Islands", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Park Hyatt Sydney", location="Sydney", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="Silky Oaks Lodge", location="Port Douglas", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
            ItineraryHotelNested(name="Qualia / Hamilton Island", location="Whitsunday Islands", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
        ],
        inclusions=_au002_inclusions(),
    )
    return package, itinerary


def _au002_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in ultra-luxury harbor, rainforest, and private island suites", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Complimentary chilled sparkling wine, fresh fruits, and roses on arrival", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private luxury vessels, executive ground vehicles, and helicopter flight transits", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Private harbour sunset cruise and Great Barrier Reef helicopter expedition", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Secluded island candlelight farewell dinner with acoustic music", sort_order=5),
        ItineraryInclusionNested(kind="included", text="VIP fast-track skip-the-line entries and 24/7 honeymoon concierge support", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="International flight tickets and entry visa processing fees", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, hotel laundry, room service, and mini-bar billing", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, or optional sightseeing not specified in the flow", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Travel insurance and personal incidentals", sort_order=10),
    ]


def build_au_003(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="au-003-luxury-australia-grand-expedition",
        destination_id=destination_id,
        title="Luxury Australia Grand Expedition",
        duration_label="08 Nights / 09 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=32,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Sydney (3N) → Cairns (2N) → Whitsundays (2N) → Gold Coast (1N)", sort_order=1),
            PackageHighlightNested(text="Private Sydney harbour yacht charter & coastal helicopter flight", sort_order=2),
            PackageHighlightNested(text="Daintree luxury retreat & reef heli-tour", sort_order=3),
            PackageHighlightNested(text="Whitsunday private island & Gold Coast VIP theme park", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 sovereign concierge & destination managers", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-AUS-LUX-2026 | Serial AU-003", sort_order=6),
        ],
        moods=["Luxury", "Family", "Nature", "Beach", "Adventure"],
    )
    itinerary = ItineraryCreate(
        slug="au-003-luxury-australia-itinerary",
        destination_id=destination_id,
        title="Luxury Australia Grand Expedition",
        duration_label="08 Nights / 09 Days",
        duration_days=9,
        starting_price=0,
        price_note="On Request (Ultimate Ultra-Luxury Sovereign Expedition)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Sydney • Daintree • Whitsundays • Gold Coast",
        overview=(
            "Indulge in the absolute zenith of Southern Hemisphere opulence with TRAGUIN's crown jewel sovereign expedition. "
            "This luxury Australia holiday links exclusive harbour-side private charter vessels, ultra-luxury reef heli-tours, "
            "secluded private island retreats, and elite rainforest sanctuary stays. Includes comprehensive VIP arrivals, "
            "dedicated luxury ground logistics, priority fast-track entry protocols, and personal concierge managers "
            "throughout your journey."
        ),
        seo_title="AU-003 | Luxury Australia Grand Expedition | TRAGUIN",
        seo_description=(
            "Ultra-luxury 08 Nights / 09 Days Australia expedition (AU-003): Sydney harbour charter, Daintree retreat, "
            "Great Barrier Reef helicopter, Whitsunday Islands, and Gold Coast elite finale."
        ),
        is_featured=True,
        featured_sort_order=32,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Private Sydney Harbour Yacht Charter", sort_order=1),
            ItineraryHighlightNested(text="Coastal Helicopter Panoramic Flight", sort_order=2),
            ItineraryHighlightNested(text="Great Barrier Reef Private Heli Expedition", sort_order=3),
            ItineraryHighlightNested(text="Whitehaven Beach Private Island Escape", sort_order=4),
            ItineraryHighlightNested(text="Gold Coast VIP Theme Park Fast-Track", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Sydney & Private Harbour Charter", "VIP airfield greeting and ultra-luxury hotel transfer. Evening private charter yacht sunset cruise past Opera House and Harbour Bridge.", ["Sightseeing Included: VIP airfield greeting, private luxury vessel sunset harbor charter", "Evening Experience: Welcome multi-course dinner at premier harbor-front venue", "Overnight Stay: Sydney Harbour (Ultra-Luxury Hotel)", "Meals Included: Gourmet Tasting Menu Welcome Dinner"]),
            _day(2, "Private Opera House & Skyline Panoramic Trail", "Private Opera House VIP tour and private helicopter flight over Bondi and Manly cliffs.", ["Sightseeing Included: Opera House VIP private guided tour, private coastal helicopter flight", "Overnight Stay: Sydney Harbour (Ultra-Luxury Hotel)", "Meals Included: International Breakfast & Casual Coastal Bistro Lunch"]),
            _day(3, "Fly to Cairns & Daintree Luxury Retreat", "Flight to Cairns and transfer to ultra-luxury Daintree Rainforest sanctuary with private canopy walk.", ["Sightseeing Included: Private executive transit to Daintree Rainforest, guided canopy walk", "Overnight Stay: Port Douglas / Daintree (Luxury Boutique Rainforest Retreat)", "Meals Included: International Breakfast & Rainforest Gastronomy Dinner"]),
            _day(4, "Great Barrier Reef Private Helicopter Expedition", "Private helicopter over the reef with sand cay landing and exclusive snorkeling in sapphire waters.", ["Sightseeing Included: Private helicopter reef flight, private sand cay snorkeling session", "Overnight Stay: Port Douglas / Daintree (Luxury Boutique Rainforest Retreat)", "Meals Included: International Breakfast & Gourmet Reef Picnic Lunch"]),
            _day(5, "Whitsunday Islands Private Escape", "Flight to Whitsundays. Afternoon on Whitehaven Beach with pristine silica sand.", ["Sightseeing Included: Private island transit, Whitehaven Beach exploration", "Overnight Stay: Whitsunday Islands (Ultra-Luxury Private Island Resort)", "Meals Included: International Breakfast & Island Beachside Dinner"]),
            _day(6, "Isolated Beach Gala & Stargazing", "Private vessel to secret beach picnic. Candlelight dinner under southern stars with fine wine.", ["Sightseeing Included: Private luxury beach picnic, sunset stargazing gala", "Overnight Stay: Whitsunday Islands (Ultra-Luxury Private Island Resort)", "Meals Included: International Breakfast & Grand Farewell Candlelight Dinner"]),
            _day(7, "Fly to Gold Coast & Elite Surf Retreat", "Fly to Gold Coast ultra-luxury beachfront resort with private cabana access at Surfers Paradise.", ["Sightseeing Included: Flight transit, beachfront relaxation with private cabana access", "Overnight Stay: Gold Coast (Premium Beachfront Luxury Resort)", "Meals Included: Breakfast & Dinner"]),
            _day(8, "Theme Park Gala & Farewell Evening", "Gold Coast theme park with VIP fast-track access. Grand finale private beach-terrace dinner.", ["Sightseeing Included: Theme park VIP fast-track tickets", "Evening Experience: Grand farewell dinner party event", "Overnight Stay: Gold Coast (Premium Beachfront Luxury Resort)", "Meals Included: Breakfast & Farewell Dinner"]),
            _day(9, "Farewell Australia", "Final luxury breakfast before private departure transfer with priority luggage handling.", ["Transfers: Private luxury van departure transfer, priority luggage handling", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Park Hyatt Sydney", location="Sydney", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=1),
            ItineraryHotelNested(name="Pullman Reef Hotel", location="Cairns", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Qualia", location="Whitsunday Islands", nights_label="02 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="The Langham Gold Coast", location="Gold Coast", nights_label="01 Night", category_label="Deluxe", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Shangri-La Sydney", location="Sydney", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="Crystalbrook Riley", location="Cairns", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Hamilton Island Resort", location="Whitsunday Islands", nights_label="02 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="Sheraton Grand Mirage", location="Gold Coast", nights_label="01 Night", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=8),
            ItineraryHotelNested(name="Crown Towers Sydney", location="Sydney", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=9),
            ItineraryHotelNested(name="Silky Oaks Lodge", location="Cairns", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=10),
            ItineraryHotelNested(name="InterContinental Hayman", location="Whitsunday Islands", nights_label="02 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=11),
            ItineraryHotelNested(name="The Darling", location="Gold Coast", nights_label="01 Night", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=12),
            ItineraryHotelNested(name="Four Seasons Sydney", location="Sydney", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=13),
            ItineraryHotelNested(name="Daintree Ecolodge", location="Cairns", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=14),
            ItineraryHotelNested(name="One&Only Hayman Island", location="Whitsunday Islands", nights_label="02 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=15),
            ItineraryHotelNested(name="The Langham Gold Coast Elite", location="Gold Coast", nights_label="01 Night", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=16),
        ],
        inclusions=_au003_inclusions(),
    )
    return package, itinerary


def _au003_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="08 Nights in world-renowned ultra-luxury harbor, rainforest, and private island suites", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Full ground transits in private high-end chauffeur vehicles", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Private luxury yacht charter in Sydney and Great Barrier Reef helicopter expedition", sort_order=3),
        ItineraryInclusionNested(kind="included", text="VIP skip-the-line Opera House entry and Gold Coast priority fast-track park access", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Dedicated 24/7 on-call travel expert concierge and local destination managers", sort_order=5),
        ItineraryInclusionNested(kind="excluded", text="International flight tickets and Australia entry visa processing fees", sort_order=6),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, hotel room service, laundry, and mini-bar billing", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, or optional sightseeing not mentioned in the flow", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Travel insurance and personal incidentals", sort_order=9),
    ]


def build_au_004(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    package = PackageCreate(
        slug="au-004-australia-family-explorer",
        destination_id=destination_id,
        title="Australia Family Explorer",
        duration_label="07 Nights / 08 Days",
        price=0,
        rating=Decimal("4.9"),
        is_featured=True,
        featured_sort_order=33,
        is_published=True,
        highlights=[
            PackageHighlightNested(text="Sydney (4N) → Melbourne (3N) east-coast family circuit", sort_order=1),
            PackageHighlightNested(text="Opera House, Blue Mountains & harbour sunset cruise", sort_order=2),
            PackageHighlightNested(text="Melbourne laneways, Great Ocean Road & Twelve Apostles", sort_order=3),
            PackageHighlightNested(text="Phillip Island Penguin Parade wildlife gala", sort_order=4),
            PackageHighlightNested(text="TRAGUIN 24/7 family concierge support", sort_order=5),
            PackageHighlightNested(text="Tour code TRG-AUS-FAM-2026 | Serial AU-004", sort_order=6),
        ],
        moods=["Family", "Luxury", "Cultural", "Wildlife", "Nature"],
    )
    itinerary = ItineraryCreate(
        slug="au-004-australia-family-explorer-itinerary",
        destination_id=destination_id,
        title="Australia Family Explorer",
        duration_label="07 Nights / 08 Days",
        duration_days=8,
        starting_price=0,
        price_note="On Request (Premium Australia Experience)",
        rating=Decimal("4.9"),
        review_count=0,
        tagline="Sydney • Melbourne • Great Ocean Road",
        overview=(
            "Embark on an epic Southern Hemisphere journey blending Sydney's iconic harbour-front metropolis with "
            "Melbourne's bohemian art-filled coffee culture. This TRAGUIN curated family expedition includes full luxury "
            "ground transit in private vehicles, pre-booked skip-the-line admissions to world heritage monuments, and "
            "handpicked hotels guaranteeing absolute comfort and premium service for multi-generational families."
        ),
        seo_title="AU-004 | Australia Family Explorer Sydney & Melbourne | TRAGUIN",
        seo_description=(
            "Premium 07 Nights / 08 Days Australia family tour (AU-004): Sydney Opera House, Blue Mountains, "
            "Melbourne laneways, Great Ocean Road, and Phillip Island Penguin Parade."
        ),
        is_featured=True,
        featured_sort_order=33,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text="Sydney Opera House Private Tour", sort_order=1),
            ItineraryHighlightNested(text="Blue Mountains & Three Sisters", sort_order=2),
            ItineraryHighlightNested(text="Melbourne Street-Art Laneways", sort_order=3),
            ItineraryHighlightNested(text="Great Ocean Road & Twelve Apostles", sort_order=4),
            ItineraryHighlightNested(text="Phillip Island Penguin Parade", sort_order=5),
        ],
        days=[
            _day(1, "Arrival in Sydney & Harbour Welcome", "Seamless airport reception and private transfer to harbour-view hotel. Evening Circular Quay walk with Opera House and Harbour Bridge views.", ["Sightseeing Included: Private luxury vehicle airport reception, Circular Quay & Opera House evening walk", "Evening Experience: Family welcome dinner at upscale harbor-front restaurant", "Overnight Stay: Sydney Harbour (Premium Family Hotel)", "Meals Included: International Welcome Dinner"]),
            _day(2, "Sydney Icons & Wildlife Encounter", "Private Opera House tour and Taronga Zoo with koalas and kangaroos.", ["Sightseeing Included: Opera House guided tour, Taronga Zoo wildlife encounter passes", "Overnight Stay: Sydney Harbour (Premium Family Hotel)", "Meals Included: International Breakfast & Casual Lunch"]),
            _day(3, "Blue Mountains Adventure", "Full-day Blue Mountains trip with Three Sisters viewpoint and Scenic World railway and cable car.", ["Sightseeing Included: Blue Mountains tour, Three Sisters viewpoint, Scenic World adventure passes", "Overnight Stay: Sydney Harbour (Premium Family Hotel)", "Meals Included: International Breakfast & Picnic Lunch"]),
            _day(4, "Sydney Leisure & Harbour Cruise", "Relaxed morning at Bondi Beach. Afternoon private harbour cruise along dramatic coastline.", ["Sightseeing Included: Bondi beach leisure afternoon, private harbor sunset cruise", "Overnight Stay: Sydney Harbour (Premium Family Hotel)", "Meals Included: International Breakfast & Farewell Sydney Dinner"]),
            _day(5, "Flight to Melbourne & Lanes Exploration", "Fly to Melbourne. Private guided walking tour of famous art-filled laneways and boutique cafes.", ["Sightseeing Included: Flight transit, Melbourne street-art laneways private guided tour", "Overnight Stay: Melbourne CBD (Premium Family Hotel)", "Meals Included: International Breakfast & City Centre Dinner"]),
            _day(6, "Epic Great Ocean Road Expedition", "Full-day Great Ocean Road tour with Twelve Apostles and wild koalas in forest canopy.", ["Sightseeing Included: Great Ocean Road guided day trip, Twelve Apostles viewing", "Overnight Stay: Melbourne CBD (Premium Family Hotel)", "Meals Included: International Breakfast & Gourmet Roadside Lunch"]),
            _day(7, "Phillip Island Wildlife Gala", "Phillip Island Nature Park and famous Penguin Parade at dusk. Grand farewell gala dinner in Melbourne.", ["Sightseeing Included: Phillip Island Nature Park, Penguin Parade evening ticket", "Evening Experience: Grand farewell gala dinner at terrace restaurant in Melbourne", "Overnight Stay: Melbourne CBD (Premium Family Hotel)", "Meals Included: International Breakfast & Farewell Dinner"]),
            _day(8, "Melbourne Departure", "Final luxury breakfast before private airport transfer.", ["Sightseeing Included: Private airport transit, luggage assistance", "Meals Included: International Buffet Breakfast"]),
        ],
        hotels=[
            ItineraryHotelNested(name="Pier One Sydney Harbour / similar", location="Sydney", nights_label="04 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=1),
            ItineraryHotelNested(name="Crowne Plaza Melbourne / similar", location="Melbourne", nights_label="03 Nights", category_label="Deluxe", meal_plan="Breakfast", stars=4, sort_order=2),
            ItineraryHotelNested(name="Shangri-La Sydney", location="Sydney", nights_label="04 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=3),
            ItineraryHotelNested(name="Crown Towers Melbourne", location="Melbourne", nights_label="03 Nights", category_label="Premium", meal_plan="Breakfast", stars=5, sort_order=4),
            ItineraryHotelNested(name="Crown Towers Sydney", location="Sydney", nights_label="04 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=5),
            ItineraryHotelNested(name="W Melbourne", location="Melbourne", nights_label="03 Nights", category_label="Luxury", meal_plan="Breakfast", stars=5, sort_order=6),
            ItineraryHotelNested(name="Park Hyatt Sydney", location="Sydney", nights_label="04 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=7),
            ItineraryHotelNested(name="The Langham Melbourne", location="Melbourne", nights_label="03 Nights", category_label="Ultra Luxury", meal_plan="Breakfast", stars=5, sort_order=8),
        ],
        inclusions=_au004_inclusions(),
    )
    return package, itinerary


def _au004_inclusions() -> list[ItineraryInclusionNested]:
    return [
        ItineraryInclusionNested(kind="included", text="07 Nights in handpicked premium family hotels in Sydney and Melbourne", sort_order=1),
        ItineraryInclusionNested(kind="included", text="Private luxury chauffeur-driven ground transfers throughout", sort_order=2),
        ItineraryInclusionNested(kind="included", text="Domestic flight coordination between Sydney and Melbourne", sort_order=3),
        ItineraryInclusionNested(kind="included", text="Pre-booked skip-the-line admissions to Opera House, zoos, and nature parks", sort_order=4),
        ItineraryInclusionNested(kind="included", text="Great Ocean Road guided day trip and Phillip Island Penguin Parade tickets", sort_order=5),
        ItineraryInclusionNested(kind="included", text="Private Sydney harbour sunset cruise on Day 4", sort_order=6),
        ItineraryInclusionNested(kind="included", text="TRAGUIN 24/7 dedicated family concierge support", sort_order=7),
        ItineraryInclusionNested(kind="excluded", text="International airfare and Australia entry visa processing fees", sort_order=8),
        ItineraryInclusionNested(kind="excluded", text="Personal expenses, laundry, room service, and mini-bar charges", sort_order=9),
        ItineraryInclusionNested(kind="excluded", text="Optional sightseeing excursions not specified in the itinerary", sort_order=10),
        ItineraryInclusionNested(kind="excluded", text="Tipping, porterage fees, and travel insurance", sort_order=11),
    ]


AU_BUILDERS = [
    build_au_001,
    build_au_002,
    build_au_003,
    build_au_004,
]
