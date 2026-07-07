#!/usr/bin/env python3
"""Generate nagaland_domestic_batch_defs.py from tmp_nl_pdfs text sources."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "_jh_gen", _SCRIPTS / "_generate_jharkhand_domestic_batch_defs.py"
)
_jh = importlib.util.module_from_spec(_spec)
sys.modules["_jh_gen"] = _jh
_spec.loader.exec_module(_jh)

PDF_DIR = _SCRIPTS.parent / "tmp_nl_pdfs"
OUT_PATH = _SCRIPTS / "nagaland_domestic_batch_defs.py"
PRICE_NOTE = "On Request (Premium Class)"
STATE = "Nagaland"

_compact_nights_label = _jh._compact_nights_label
clean_raw = _jh.clean_raw
py_str = _jh.py_str
extract_duration = _jh.extract_duration
extract_category = _jh.extract_category
extract_destinations = _jh.extract_destinations
extract_ideal_for = _jh.extract_ideal_for
extract_best_season = _jh.extract_best_season
extract_vehicle_meals = _jh.extract_vehicle_meals
extract_route = _jh.extract_route
extract_overview_sections = _jh.extract_overview_sections
parse_inclusions_exclusions = _jh.parse_inclusions_exclusions
parse_signature_highlights = _jh.parse_signature_highlights
parse_shopping_notes = _jh.parse_shopping_notes
_infer_nights_from_duration = _jh._infer_nights_from_duration
emit_hotel = _jh.emit_hotel
_dedupe_items = _jh._dedupe_items


def _nl_hotel(
    sort_order: int,
    category: str,
    *,
    nights_label: str,
    room_type: str = "Deluxe Room",
    meal_plan: str = "MAPAI (Breakfast & Dinner)",
    stars: int | None = None,
    description_extra: str = "",
    **cities: str,
) -> dict:
    labels: list[str] = []
    names: list[str] = []
    for label, value in cities.items():
        if value:
            labels.append(label.replace("_", " ").title())
            names.append(value)
    name = " | ".join(names)
    location = " | ".join(labels)
    pipe_desc = " | ".join(names)
    desc = f"OPTION {sort_order:02d} – {category.upper()}: {pipe_desc} | {meal_plan}"
    if description_extra:
        desc += f" | {description_extra}"
    return {
        "sort_order": sort_order,
        "category": category,
        "name": name,
        "location": location,
        "nights_label": _compact_nights_label(nights_label),
        "room_type": room_type,
        "meal_plan": meal_plan,
        "stars": stars if stars is not None else (5 if "ultra" in category.lower() else 4),
        "description": desc,
    }


PACKAGE_META: dict[str, dict] = {
    "NL-001": {
        "tour_code": "TRAGUIN-NL-001",
        "slug": "nl-001-nagaland-discovery-a-premium-custom-travel-experience",
        "title": "Nagaland Discovery: A Premium Custom Travel Experience",
        "moods": ["Family", "Culture", "Luxury"],
        "category": "Premium Luxury Family Vacation",
        "destinations": "Dimapur • Kohima • Khonoma • Mokokchung",
        "ideal_for": "Families, Culture Seekers, Luxury Travelers",
        "best_season": "October to May (Special Hornbill Festival in Dec)",
        "route": "Dimapur → Kohima → Khonoma Green Village → Mokokchung → Dimapur",
        "vehicle_meals": "Private Premium SUV (Innova Crysta) / Modified American Plan (Breakfast & Dinner)",
        "included": [
            "05 Nights luxurious accommodation in handpicked top-rated properties.",
            "Modified American Plan (Daily Premium Breakfast and Chef-Curated Dinners).",
            "Private exclusive airport transfers and all sightseeing via premium SUV (Innova Crysta).",
            "Professional, English-speaking certified local cultural guides for deep storytelling.",
            "All inner line permits (ILP) and state entry documentation handled seamlessly.",
            "Exclusive farm-to-table lunch experience at Khonoma Green Village.",
            "Complimentary welcome amenities and custom travel comfort kits in the vehicle.",
            "24/7 dedicated remote concierge support from TRAGUIN operational headquarters.",
        ],
        "excluded": [
            "Domestic or International Airfare / Train tickets to Dimapur.",
            "Personal expenses (laundry, telephone calls, premium alcoholic beverages).",
            "Camera fees, video recording charges at monument checkpoints.",
            "Optional adventure activities or treks not explicitly outlined.",
            "Travel insurance policies (highly recommended).",
            "Tips and gratuities for drivers, local guides, and hotel staff.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="Hotel Vivor / Equivalent", mokokchung="Hotel Whispering Winds / Equivalent", nights_label="3N Kohima + 2N Mokokchung", meal_plan="Breakfast & Dinner (MAP)"),
            _nl_hotel(2, "Premium", kohima="The Heritage Kohima / Equivalent", mokokchung="Woodland Resort / Equivalent", nights_label="3N Kohima + 2N Mokokchung", meal_plan="Breakfast & Dinner (MAP)"),
            _nl_hotel(3, "Luxury", kohima="Razhu Pru Heritage Mansion / Equivalent", mokokchung="Mopungchuket Luxury Eco-Lodge", nights_label="3N Kohima + 2N Mokokchung", room_type="Heritage Mansion | Luxury Eco-Lodge", meal_plan="Breakfast & Dinner (MAP)", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="Dzukou Valley Luxury Glamping / Tents", mokokchung="TRAGUIN Signature Handpicked Estate", nights_label="3N Kohima + 2N Mokokchung", room_type="Luxury Glamping | Signature Estate", meal_plan="All Meals Custom Curated", stars=5),
        ],
    },
    "NL-002": {
        "tour_code": "TRAGUIN-NL-002",
        "slug": "nl-002-immersive-cultural-odyssey-and-the-legendary-hornbill-festival-experience",
        "title": "Immersive Cultural Odyssey & The Legendary Hornbill Festival Experience",
        "moods": ["Culture", "Heritage", "Festival"],
        "category": "Culture & Heritage",
        "destinations": "Dimapur • Kohima • Kisama Heritage Village • Khonoma Green Village",
        "ideal_for": "Culture Enthusiasts, Photographers, Luxury Explorers, Families & Honeymooners",
        "best_season": "December (Hornbill Festival)",
        "route": "Dimapur to Kohima to Kisama Heritage Village to Khonoma to Dimapur",
        "vehicle_meals": "Private Premium Luxury SUV (Toyota Innova Crysta) / MAPAI",
        "included": [
            "Premium Accommodation: 04 Nights stay in handpicked, top-rated luxury accommodations on twin sharing basis.",
            "Gourmet Meal Plan: Daily elaborate multi-cuisine breakfasts and customized table d'hôte dinners at the properties.",
            "Luxury Transportation: All transfers, inter-city movements, and Nagaland Sightseeing routes in an exclusive, private Toyota Innova Crysta SUV.",
            "VIP Access Passes: Pre-arranged priority entry passes to the main arena seats at the Hornbill Festival grounds.",
            "Curated Tribal Luncheon: An authentic, private ethnic lunch experience in Khonoma Green Village.",
            "Expert Accompaniment: Highly knowledgeable, English-speaking tribal cultural guides certified by local heritage groups.",
            "Welcome Amenities: Personalized luxury travel kit including organic sanitizers, premium local teas, and a customized festival guide block.",
            "Dedicated Support: 24/7 real-time remote concierge support directly from the TRAGUIN guest relations desk.",
            "All Systemic Taxes: Inclusive of all state permits, Inner Line Permits (ILP) documentation charges, fuel surcharges, parking costs, and toll taxes.",
        ],
        "excluded": [
            "Domestic or international airfares to and from Dimapur Airport.",
            "Personal expenses such as laundry, premium alcoholic beverages, mineral water, and telephone calls.",
            "Camera fees, video recording permissions, or specialized drone photography licensing at the sightseeing venues.",
            "Any optional adventure activities, tips for drivers/guides, or expenses incurred due to flight delays or natural disruptions.",
            "Any services or entry costs not explicitly listed under the official TRAGUIN inclusions section.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="Hotel Vivor / The Heritage Kohima", nights_label="4N Kohima", room_type="Executive Room", meal_plan="MAPAI"),
            _nl_hotel(2, "Premium", kohima="Zone Niathu Dimapur By The Park / Hotel Japfü", nights_label="4N Kohima", room_type="Premium Suite", meal_plan="MAPAI"),
            _nl_hotel(3, "Luxury", kohima="The Ultimate Travelling Camp (TUTC) Kohima", nights_label="4N Kohima", room_type="Luxury Safari Tent", meal_plan="MAPAI", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="Exclusive Private Tribal Villa Estate / Royal TUTC Suite", nights_label="4N Kohima", room_type="Ultra Luxury Presidential Tent", meal_plan="MAPAI", stars=5),
        ],
    },
    "NL-003": {
        "tour_code": "TRAGUIN-NL-003",
        "slug": "nl-003-nagaland-explorer-the-ultimate-horizon",
        "title": "Nagaland Explorer: The Ultimate Horizon",
        "moods": ["Adventure", "Culture", "Luxury"],
        "category": "Premium Adventure & Cultural Immersion",
        "destinations": "Dimapur • Kohima • Khonoma • Pfutsero • Mokokchung",
        "ideal_for": "Luxury Explorers, Culture Enthusiasts, Photographers",
        "best_season": "October to May (Includes Hornbill Festival Season)",
        "route": "Dimapur → Kohima → Khonoma → Pfutsero → Mokokchung → Dimapur",
        "vehicle_meals": "Premium 4x4 Luxury SUV (Toyota Innova Crysta) / MAPAI",
        "included": [
            "Premium Accommodations: 06 Nights' stay in handpicked, top-rated luxury properties, boutique heritage homes, and luxury eco-retreats.",
            "Gourmet Meal Plan: Daily premium breakfasts and curated multi-course traditional/continental dinners across all destinations.",
            "Luxury Private Transportation: Exclusive use of a premium 4x4 high-clearance SUV (Toyota Innova Crysta) for all transfers, excursions, and inter-district travel.",
            "Expert Guided Expeditions: Services of a highly knowledgeable, English-speaking local cultural ambassador and expert tribal guides.",
            "Exclusive Experiences: Private audiences with village elders, traditional folk music sessions, and artisan craft demonstrations.",
            "Welcome Amenities: Premium organic welcome kits, mineral water platters daily, and signature local tea tasting baskets.",
            "Hassle-Free Formalities: Complete assistance with securing Inner Line Permits (ILP) and all required local community entry permissions.",
            "TRAGUIN Support: Dedicated 24/7 remote concierge support and emergency assistance throughout your journey.",
        ],
        "excluded": [
            "Airfare & Railfare: Domestic or international flights to and from Dimapur Airport.",
            "Personal Expenses: Laundry, telephone calls, premium alcoholic beverages, and optional tipping for drivers or guides.",
            "Entry Tickets & Camera Fees: Monument entry charges, national park fees, and professional camera/drone permits.",
            "Optional Activities: Unspecified trail excursions, specialized workshops, or personal shopping items.",
            "Insurance: Comprehensive travel, medical, or baggage loss insurance policies.",
            "Unforeseen Expenses: Costs resulting from flight delays, weather-related roadblocks, or political strikes.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="The Sakhrie House / Similar", pfutsero="Pfutsero Tourist Lodge", mokokchung="Hotel Whispering Winds", nights_label="3N Kohima + 1N Pfutsero + 2N Mokokchung", room_type="Executive Room", meal_plan="MAPAI (Breakfast & Dinner)"),
            _nl_hotel(2, "Premium", kohima="Razhu Pru Heritage Home", pfutsero="Glory Peak Eco-Lodge", mokokchung="Mokokchung Resort", nights_label="3N Kohima + 1N Pfutsero + 2N Mokokchung", room_type="Luxury Suite", meal_plan="MAPAI (Breakfast & Dinner)"),
            _nl_hotel(3, "Luxury", kohima="Kohima Camp / Tanhir Estate", pfutsero="Pfutsero High-Altitude Retreat", mokokchung="The Whispering Ridge Luxury", nights_label="3N Kohima + 1N Pfutsero + 2N Mokokchung", room_type="Premium Villa", meal_plan="MAPAI (Breakfast & Dinner)", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="The Ultimate Hornbill Luxury Pavilion", pfutsero="Private Luxury Chalet Pfutsero", mokokchung="Elite Ao Heritage Mansion", nights_label="3N Kohima + 1N Pfutsero + 2N Mokokchung", room_type="Signature Suite", meal_plan="Royal MAPAI Plan", stars=5),
        ],
    },
    "NL-004": {
        "tour_code": "TRG-NAGA-NL004-2026",
        "slug": "nl-004-kohima-experience-mystical-tribal-heritage-pristine-hills",
        "title": "Kohima Experience • Mystical Tribal Heritage • Pristine Hills",
        "moods": ["Family", "Culture", "Heritage"],
        "category": "Premium Family Tour",
        "destinations": "Dimapur • Kohima • Khonoma • Kisama",
        "ideal_for": "Family / Culture Enthusiasts",
        "best_season": "October to May",
        "route": "Dimapur ➔ Kohima ➔ Kisama Heritage Village ➔ Khonoma Green Village ➔ Dimapur",
        "vehicle_meals": "Premium Toyota Innova Crysta / MAPAI (Breakfast & Dinner)",
        "included": [
            "04 Nights premium handpicked hotel stay in Kohima.",
            "Daily premium multi-cuisine breakfasts and gourmet dinners.",
            "Exclusive TRAGUIN Signature Angami Home Lunch in Khonoma.",
            "Chauffeur-driven private Toyota Innova Crysta for all transfers.",
            "Dedicated English-speaking certified local cultural specialist guide.",
            "Inner Line Permits (ILP) documentation for Indian domestic tourists.",
            "Premium welcome amenities, fresh organic fruit baskets on arrival.",
            "All parking fees, luxury toll taxes, driver allowances, and state entry taxes.",
            "24/7 dedicated backend guest assistance via senior TRAGUIN advisors.",
        ],
        "excluded": [
            "Airfares, train bookings, or helicopter transfer costs to Dimapur.",
            "Monument entry fees, camera passes, or local museum tickets.",
            "Optional adventure hikes or custom professional photo shoots.",
            "Laundry, alcoholic beverages, minibar usages, and telephone bills.",
            "Mandatory travel insurance or medical evacuation cover costs.",
            "Tips or gratitude gestures for accompanying drivers and local guides.",
            "Any expenses incurred due to unexpected roadblocks or flight delays.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="Hotel Vivor / Hotel Razhuprat", nights_label="4N Kohima", room_type="Executive Deluxe Room", meal_plan="MAPAI Plan"),
            _nl_hotel(2, "Premium", kohima="The Heritage Kohima / Niraamaya Retreats", nights_label="4N Kohima", room_type="Premium Valley View Room", meal_plan="MAPAI Plan"),
            _nl_hotel(3, "Luxury", kohima="Lazeo Hill Crest Resort / Dzüko Valley Luxury Eco Lodge", nights_label="4N Kohima", room_type="Luxury Suite / Royal Villa", meal_plan="MAPAI Plan", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="Ultimate Tented Suite Concept (Bespoke Curated Private Setup)", nights_label="4N Kohima", room_type="Signature Imperial Royal Tent", meal_plan="All Inclusive Premium", stars=5),
        ],
    },
    "NL-005": {
        "tour_code": "TRAGUIN-NAGA-LUX-005",
        "slug": "nl-005-premium-nagaland-experience",
        "title": "Premium Nagaland Experience",
        "moods": ["Culture", "Luxury", "Heritage"],
        "category": "Luxury Travel / Tribal Heritage",
        "destinations": "Dimapur • Kohima • Khonoma • Kigwema • Touphema",
        "ideal_for": "Connoisseurs of Culture, Luxury Seekers, Honeymooners & Families",
        "best_season": "October to May (Featuring the Iconic Hornbill Festival in December)",
        "route": "Dimapur Arrival • Kohima • Khonoma • Kigwema • Touphema • Dimapur Departure",
        "vehicle_meals": "Premium Toyota Innova Crysta / Full Board (Premium Breakfast, Curated Lunches & Epicurean Dinners)",
        "included": [
            "5 Nights premium accommodation in handpicked, top-tier luxury hotels and heritage resorts.",
            "Comprehensive meal plan featuring custom breakfasts, curated lunches, and elegant evening dinners.",
            "Private transfers and dedicated sightseeing in an exclusive Toyota Innova Crysta.",
            "Accompaniment by an elite, professional local cultural guide throughout the tour.",
            "All inner line permits (ILP), regional entry documentation, and state processing fees.",
            "Bottled mineral water, premium local fruit baskets, and welcome amenities upon arrival.",
            "Exclusive private audience with tribal elders and master artisans.",
            "Complete, 24/7 remote concierge support from our executive travel desk.",
        ],
        "excluded": [
            "Domestic or International airfares to and from Dimapur.",
            "Personal expenses such as laundry, premium beverages, and telephone charges.",
            "Camera, video recording, or professional drone photography licensing fees.",
            "Optional individual activities, personal monument entry tickets, and independent excursions.",
            "Travel insurance policies, medical expenses, and emergency evacuation costs.",
            "Gratuities, tips for drivers, local guides, or hotel hospitality personnel.",
            "Any costs arising from flight delays, weather disruptions, or unexpected roadblocks.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="Hotel Vivor / Razhu Pru (Heritage Suite)", touphema="Touphema Heritage Cottage (Standard)", nights_label="4N Kohima + 1N Touphema", meal_plan="Breakfast & Dinner Included"),
            _nl_hotel(2, "Premium", kohima="The Heritage Dimapur / Grand Pavilion", touphema="Touphema Premium Executive Cottage", nights_label="4N Kohima + 1N Touphema", meal_plan="Full Board (All Meals)"),
            _nl_hotel(3, "Luxury", kohima="Kohima Luxury Eco-Resort (Luxury Villa)", touphema="Touphema Royal Heritage Suite", nights_label="4N Kohima + 1N Touphema", meal_plan="Full Board (Curated Menus)", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="Elite Tented Camp Concept / Premium Custom Resort", touphema="Elite Presidential Tribal Cottage", nights_label="4N Kohima + 1N Touphema", meal_plan="Bespoke Culinary & Private Chef Service", stars=5),
        ],
    },
    "NL-006": {
        "tour_code": "TRAGUIN-NL-006-PREM",
        "slug": "nl-006-kohima-khonoma-mokokchung-elegant-leisure-exploration",
        "title": "Kohima • Khonoma Green Village • Mokokchung • Dimapur — Elegant Leisure Exploration",
        "moods": ["Family", "Leisure", "Culture"],
        "category": "Senior Citizen Leisure",
        "destinations": "Dimapur • Kohima • Khonoma • Mokokchung",
        "ideal_for": "Seniors, Families & Couples",
        "best_season": "October to May",
        "route": "Dimapur → Kohima → Khonoma → Mokokchung",
        "vehicle_meals": "Premium Toyota Innova Crysta / CP / MAP (Premium Buffets)",
        "included": [
            "Accommodation: 05 Nights in handpicked premium hotels matching senior safety rules.",
            "Meals: Nutritious daily breakfasts and curated dinners suited to requested preferences.",
            "Transfers: Dedicated private Toyota Innova Crysta for all smooth transit routes.",
            "Sightseeing: All entries to historic sites, heritage villages, and eco-parks.",
            "Assistance: Full-time 24/7 dedicated TRAGUIN support helpline.",
            "Welcome Amenities: Refreshing traditional welcome drinks and premium organic dry fruit hampers.",
            "Complimentary Experiences: Private interaction with tribal historians and village elders.",
            "Taxes: All standard luxury hospitality service taxes and inner line permit processing fees.",
        ],
        "excluded": [
            "Flights: Domestic or international air tickets to and from Dimapur Airport.",
            "Personal Expenses: Laundry, telephone calls, premium alcoholic beverages, and tips.",
            "Activities: Individual optional tribal shawl weaving purchases or heavy adventure sports.",
            "Insurance: Comprehensive personal medical and travel cancellation insurance covers.",
            "Camera Charges: Special video camera or commercial photography permissions at monuments.",
            "Unspecified Meals: Mid-day snacks or lunches not listed explicitly in the chosen hotel plan.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="Hotel Vivor / Equivalent", mokokchung="Hotel Whispering Winds", nights_label="3N Kohima + 2N Mokokchung", room_type="Executive Room", meal_plan="MAP Plan"),
            _nl_hotel(2, "Premium", kohima="The Heritage Kohima", mokokchung="Signature Boutique Retreat", nights_label="3N Kohima + 2N Mokokchung", room_type="Premium Valley View", meal_plan="MAP Plan"),
            _nl_hotel(3, "Luxury", kohima="Dzüku Valley Resort Luxury Wing", mokokchung="Woodland Luxury Suite Resort", nights_label="3N Kohima + 2N Mokokchung", room_type="Luxury Heritage Suite", meal_plan="All Meals", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="TRAGUIN Elite Partner Estate", mokokchung="Mokokchung Heritage Villa", nights_label="3N Kohima + 2N Mokokchung", room_type="Presidential Tribal Villa", meal_plan="Ultra Luxury VIP", stars=5),
        ],
    },
    "NL-007": {
        "tour_code": "TRAGUIN-NAGA-EDU-007",
        "slug": "nl-007-immersive-educational-expedition-dimapur-kohima-khonoma",
        "title": "An Immersive Educational Expedition: Dimapur • Kohima • Khonoma Green Village",
        "moods": ["Education", "Culture", "Heritage"],
        "category": "Educational Tour",
        "destinations": "Dimapur • Kohima • Khonoma",
        "ideal_for": "Students & Educators",
        "best_season": "October to May",
        "route": "Dimapur Arrival ➔ Kohima Heritage Precincts ➔ Khonoma Eco-Sphere ➔ Dimapur Departure",
        "vehicle_meals": "Premium Dedicated Luxury Coaches / Comprehensive Full Board",
        "included": [
            "Safe Secure Accommodation: 04 Nights stay in verified, safety-compliant premium properties.",
            "All-Tier Meal Plans: 04 Breakfasts, 05 Lunches, and 04 Dinners planned hygienically.",
            "Luxury Ground Logistics: Dedicated deluxe coaches with experienced hill drivers for all routes.",
            "Curated Academic Sightseeing: Entry permissions to museums, heritage spots, and Khonoma eco-zones.",
            "Expert Human Resource: Dedicated TRAGUIN tour director along with certified regional historians.",
            "Institutional Privileges: Interactive student workshops, certificates of completion, and community interaction permissions.",
            "Taxes & Permissions: All inner line permits (ILP), state entry filings, and government GST overheads.",
        ],
        "excluded": [
            "Inbound Airfare/Rail Transit: Mainline tickets from the home institution city to Dimapur.",
            "Personal Student Expenses: Souvenirs, laundry, specialized telephone calls, and individual room service bills.",
            "Insurance Protocols: Individual travel/medical insurance covers (can be appended on request).",
            "Unscheduled Logistics: Deviations from the main group itinerary or unauthorized vehicle detours.",
            "Camera Surcharges: Video/professional DSLR recording fees at specific museum checkpoints.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="Hotel Japfü / Pine Haven Group", nights_label="4N Kohima", room_type="Standard Twin Sharing", meal_plan="Full Board (MAPAI / APAI)"),
            _nl_hotel(2, "Premium", kohima="The Heritage DC Bungalow / Equivalent", nights_label="4N Kohima", room_type="Premium Twin/Triple", meal_plan="Full Board (APAI)"),
            _nl_hotel(3, "Luxury", kohima="Naga Heritage Resort / Razhu Pris", nights_label="4N Kohima", room_type="Executive Cohort Rooms", meal_plan="Full Board + Snacks", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="Touphema Tourist Village / Specialized Eco-Cabins", nights_label="4N Kohima", room_type="Heritage Cottage Suites", meal_plan="Curated Tribal Feast Board", stars=5),
        ],
    },
    "NL-008": {
        "tour_code": "TG-NAG-NL008",
        "slug": "nl-008-dimapur-kohima-khonoma-kigwema-tuophema-immersive-tribal-experience",
        "title": "Dimapur • Kohima • Khonoma • Kigwema • Tuophema — Immersive Tribal Experience",
        "moods": ["Family", "Tribal", "Culture"],
        "category": "Family / Tribal Exploration",
        "destinations": "Dimapur, Kohima, Khonoma, Kigwema, Tuophema",
        "ideal_for": "Family Vacations, Culture Seekers",
        "best_season": "October to May",
        "route": "Dimapur – Kohima – Khonoma – Tuophema – Dimapur",
        "vehicle_meals": "Dedicated Premium SUV (Innova Crysta) / MAPAI",
        "included": [
            "Premium Stays: 05 Nights accommodation in top-tier handpicked hotels/resorts.",
            "Gourmet Meals: Daily breakfast and dinners across properties.",
            "Luxury Transfers: Dedicated private SUV (Innova Crysta) for all routes.",
            "Curated Experiences: Specialized local tribal guides and village entrance permissions.",
            "Welcome Amenities: Personalized arrival gifts and daily packed mineral water.",
            "TRAGUIN Support: 24/7 dedicated on-ground expert remote assistance.",
        ],
        "excluded": [
            "Airfare: Domestic or international flights to/from Dimapur.",
            "Inner Line Permits (ILP): Nominal documentation charges if processed separately.",
            "Personal Expenses: Laundry, telephone calls, alcoholic beverages.",
            "Entry Tickets: Monument entry fees, camera permits, local video charges.",
            "Insurance: Medical or individual travel insurance coverage.",
            "Optional Tours: Any activities not explicitly listed in the itinerary.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="Hotel Japfü Kohima / Similar Standard Premium", nights_label="4N Kohima + 1N Tuophema", room_type="Executive Room", meal_plan="MAPAI (Breakfast + Dinner)"),
            _nl_hotel(2, "Premium", kohima="The Ultimate Frontier Resort Kohima / Similar", nights_label="4N Kohima + 1N Tuophema", room_type="Luxury Suite", meal_plan="MAPAI (Breakfast + Dinner)"),
            _nl_hotel(3, "Luxury", kohima="Razhu Prü Heritage Resort Kohima / Custom Selection", nights_label="4N Kohima + 1N Tuophema", room_type="Heritage Premium Suite", meal_plan="MAPAI (Breakfast + Dinner)", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="TRAGUIN Handpicked Luxury Wilderness Camp / Premium Villas", nights_label="4N Kohima + 1N Tuophema", room_type="Signature Premium Villa", meal_plan="MAPAI (Breakfast + Dinner)", stars=5),
        ],
    },
    "NL-009": {
        "tour_code": "TRG-NAG-ADV-009",
        "slug": "nl-009-dzukou-valley-and-tribal-heritage-luxury-expedition",
        "title": "Dzukou Valley & Tribal Heritage Luxury Expedition",
        "moods": ["Adventure", "Nature", "Luxury"],
        "category": "Luxury Adventure & Trekking",
        "destinations": "Dimapur • Kohima • Jakhama • Dzukou Valley • Khonoma",
        "ideal_for": "Adventure Enthusiasts, Nature Lovers, Luxury Explorers",
        "best_season": "October to May (Treks), June-Sept (Lush Greenery)",
        "route": "Dimapur → Kohima → Jakhama → Dzukou Valley → Khonoma → Dimapur",
        "vehicle_meals": "Premium SUV & All Meals Included",
        "included": [
            "Accommodation: Handpicked premium hotels and luxury glamping.",
            "Meals: All premium breakfast, curated lunches, and gourmet dinners.",
            "Transfers: Dedicated Luxury 4x4 SUV (Innova Crysta / Fortuner) throughout.",
            "Sightseeing: All entry fees, Inner Line Permits (ILP), and local taxes.",
            "Assistance: 24/7 dedicated TRAGUIN concierge support.",
            "Welcome Amenities: Luxury arrival gift hampers and local organic kits.",
            "Trek Support: Professional indigenous guides, certified camp kitchen team, and personal porters.",
        ],
        "excluded": [
            "Flights: Domestic or International airfare to/from Dimapur.",
            "Personal Expenses: Laundry, premium hard beverages, telephone calls.",
            "Insurance: International or domestic medical and travel insurance.",
            "Optional Tours: Any activities not explicitly listed in the itinerary.",
            "Camera Fees: Professional drone or special video camera permits.",
            "Tips: Gratuities for local drivers, porters, and camp staff.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="Hotel Vivor / Razhu Pru (Heritage Room)", dzukou="TRAGUIN Coordinated Standard Dome Tents", nights_label="3N Kohima/Khonoma + 2N Dzukou Valley", meal_plan="MAPAI (Breakfast + Dinner)"),
            _nl_hotel(2, "Premium", kohima="The Horizon / Niraamaya Heritage (Executive)", dzukou="TRAGUIN Private Comfort Camps (Thick Bedding)", nights_label="3N Kohima/Khonoma + 2N Dzukou Valley", meal_plan="APAI (All Meals Included)"),
            _nl_hotel(3, "Luxury", kohima="Dzukou Valley Eco Resort / Luxury Cottages", dzukou="TRAGUIN Premium Heated Glamping Tents", nights_label="3N Kohima/Khonoma + 2N Dzukou Valley", meal_plan="All Inclusive Gourmet", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="The Ultimate Travelling Camp (TUTC) / Signature Elite", dzukou="TRAGUIN VIP Custom Alpine Luxury Geodesic Domes", nights_label="3N Kohima/Khonoma + 2N Dzukou Valley", meal_plan="Royal Bespoke Dining", stars=5),
        ],
    },
    "NL-010": {
        "tour_code": "TRG-NAG-FAM-010",
        "slug": "nl-010-complete-nagaland-immersive-family-luxury-holiday",
        "title": "Complete Nagaland Immersive Family Luxury Holiday",
        "moods": ["Family", "Heritage", "Culture"],
        "category": "Family Luxury Vacation",
        "destinations": "Dimapur • Kohima • Kigwema • Khonoma • Mokokchung • Tuophema",
        "ideal_for": "Multi-Generational Families, Heritage Seekers, Culture Explorers",
        "best_season": "October to May (Pleasant and Festive)",
        "route": "Dimapur → Kohima → Kigwema → Khonoma → Tuophema → Mokokchung → Kohima → Dimapur",
        "vehicle_meals": "Luxury SUV Fleet & All Gourmet Meals",
        "included": [
            "Accommodation: 7 Nights in handpicked premium hotels and eco-resorts.",
            "Meals: All daily breakfasts, custom lunches, and grand festive dinners.",
            "Transfers: Dedicated Luxury SUV Fleet (Innova Crysta / Toyota Fortuner) throughout.",
            "Sightseeing: All destination entry permits, inner-line family passes, and monument taxes.",
            "Assistance: 24/7 dedicated TRAGUIN elite concierge support.",
            "Welcome Amenities: Premium arrival luxury gift hampers, organic treats, and kids' activity journals.",
            "Complimentary Experiences: Private Naga wrestling display and exclusive artisan weaving masterclasses.",
        ],
        "excluded": [
            "Flights: Commercial or chartered domestic airfare to/from Dimapur.",
            "Personal Expenses: Premium vintage spirits, room service laundry, international phone roaming.",
            "Insurance: Multi-risk comprehensive family travel and medical coverage.",
            "Optional Tours: Extra activities or off-route excursions not detailed in the itinerary.",
            "Camera Levies: Special institutional commercial or drone videography fees.",
            "Tips: Optional tips for your professional drivers, local guides, and estate crew.",
        ],
        "hotels": [
            _nl_hotel(1, "Deluxe", kohima="Hotel Vivor (Deluxe Suite)", khonoma_tuophema="Tuophema Village Ethnic Cottages", mokokchung="Hotel Whispering Winds", nights_label="4N Kohima + 2N Khonoma/Tuophema + 2N Mokokchung"),
            _nl_hotel(2, "Premium", kohima="The Horizon Kohima (Executive Suite)", khonoma_tuophema="Khonoma Heritage Eco-Lodge", mokokchung="Bravo Hotel & Resort", nights_label="4N Kohima + 2N Khonoma/Tuophema + 2N Mokokchung"),
            _nl_hotel(3, "Luxury", kohima="Niraamaya Retreats Aradura (Luxury Suite)", khonoma_tuophema="TRAGUIN Private Luxury Villa Units", mokokchung="Mokokchung Elite Eco Resort", nights_label="4N Kohima + 2N Khonoma/Tuophema + 2N Mokokchung", stars=5),
            _nl_hotel(4, "Ultra Luxury", kohima="Signature Elite Estate (VVIP Royal Wing)", khonoma_tuophema="TRAGUIN Custom VIP Glamping Domes", mokokchung="The Majestic Ao Ridge Estate", nights_label="4N Kohima + 2N Khonoma/Tuophema + 2N Mokokchung", stars=5),
        ],
    },
}

BUILDER_ORDER = [f"NL-{i:03d}" for i in range(1, 11)]

_STOP_LINE_RE = re.compile(
    r"^(?:PREMIUM HANDPICKED|HANDPICKED PREMIUM|EXCLUSIVE (?:LUXURY )?HOTEL|PREMIUM ACCOMMODATION|"
    r"PACKAGE INCLUSIONS|PACKAGE TIER|SPECIAL TRAGUIN|SHOPPING|IMPORTANT TRAVEL|IMPORTANT NOTES|"
    r"TRAGUIN Premium|TRAGUIN Complete|TRAGUIN •|CATEGORY$|Option 0|OPTION 0)",
    re.I,
)
_ACTIVITY_LABELS = (
    "Sightseeing Included",
    "Nagaland Sightseeing Included",
    "Sightseeing En-route",
    "Optional Activities",
    "Evening Experience",
    "Overnight Stay",
    "Meals Included",
    "Meals",
    "Transfers Included",
    "Photography Points",
    "Departure",
    "Departure Point",
)


def _trim_body(body: str) -> str:
    kept: list[str] = []
    for ln in body.splitlines():
        stripped = ln.strip()
        if not stripped:
            if kept:
                kept.append("")
            continue
        if _STOP_LINE_RE.match(stripped):
            break
        if re.match(r"^DAY\s*\d+", stripped, re.I):
            break
        kept.append(stripped)
    return "\n".join(kept).strip()


def _merge_activity_lines(raw_lines: list[str]) -> list[str]:
    merged: list[str] = []
    label_re = re.compile(rf"^({'|'.join(_ACTIVITY_LABELS)})\s*:?\s*(.*)$", re.I)
    for line in raw_lines:
        m = label_re.match(line)
        if m:
            label, val = m.group(1).strip(), m.group(2).strip()
            merged.append(f"{label}: {val}" if val else label)
            continue
        if merged and not line[0].isupper() and len(line) < 120:
            merged[-1] = f"{merged[-1]} {line}".strip()
        elif merged and merged[-1].endswith((",", "and", "with", "featuring", "through", "at", "in", "to", "for", "of", "the", "a", "an")):
            merged[-1] = f"{merged[-1]} {line}".strip()
        elif merged and not merged[-1].endswith((".", "!", "?")):
            merged[-1] = f"{merged[-1]} {line}".strip()
        else:
            merged.append(line)
    return merged


def _parse_day_body(day_num: int, title_line: str, body: str) -> dict:
    body = _trim_body(body)
    paragraphs: list[str] = []
    activities: list[str] = []
    current_para: list[str] = []
    desc_lines: list[str] = []
    act_lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(rf"^({'|'.join(_ACTIVITY_LABELS)})\b", stripped, re.I):
            if current_para:
                paragraphs.append(" ".join(current_para))
                current_para = []
            act_lines.append(stripped)
        else:
            if act_lines:
                activities.extend(_merge_activity_lines(act_lines))
                act_lines = []
            current_para.append(stripped)
            desc_lines.append(stripped)
    if act_lines:
        activities.extend(_merge_activity_lines(act_lines))
    if current_para:
        paragraphs.append(" ".join(current_para))
    description = re.sub(r"\s+", " ", " ".join(paragraphs)).strip()
    if not description:
        description = re.sub(r"\s+", " ", " ".join(desc_lines)).strip()
    if not description:
        description = f"Full day curated TRAGUIN experience: {title_line.title()}."
    title_line = re.sub(r"\s+", " ", title_line.strip()).upper()
    if len(title_line) > 120:
        title_line = title_line[:117] + "..."
    return {
        "day_number": day_num,
        "title": title_line,
        "description": description,
        "activities": activities or [f"Full day as per curated TRAGUIN itinerary for Day {day_num}."],
    }


def parse_day_blocks(text: str, serial: str | None = None) -> list[dict]:
    """Parse Nagaland day blocks from PDF text exports."""
    if serial and (meta := PACKAGE_META.get(serial, {})).get("days"):
        return meta["days"]

    start = re.search(
        r"(?:DETAILED DAY-WISE ITINERARY|DAY-WISE ITINERARY|THE CURATED DAILY ITINERARY|DAY 01 \|)",
        text,
        re.IGNORECASE,
    )
    if start:
        section = text[start.end():]
    else:
        day_one = re.search(r"^DAY\s*0?1\b", text, re.MULTILINE | re.IGNORECASE)
        if not day_one:
            return _jh.parse_day_blocks(text)
        section = text[day_one.start():]

    end = re.search(
        r"(?m)^(?:HANDPICKED|PREMIUM HANDPICKED|EXCLUSIVE LUXURY HOTEL|EXCLUSIVE HANDPICKED|"
        r"PREMIUM ACCOMMODATIONS|PREMIUM & LUXURY HANDPICKED|PREMIUM ACCOMMODATION|"
        r"HANDPICKED PREMIUM HOTEL|HANDPICKED PREMIUM ACCOMMODATIONS|PREMIUM HOTEL OPTIONS|"
        r"EXCLUSIVE LUXURY HOTEL OPTIONS|PREMIUM ACCOMMODATIONS & EXCLUSIONS|"
        r"PACKAGE INCLUSIONS|PACKAGE TIER|PREMIUM ACCOMMODATIONS & EXCLUSIONS)",
        section,
    )
    if end:
        section = section[: end.start()]

    section = _jh.FOOTER_RE.sub("", section)
    section = _jh.PAGE_RE.sub("", section)
    section = re.sub(r"^TRAGUIN(?: • Premium Travel & Luxury Holidays| Premium Luxury Holidays[^\n]*)?\s*$", "", section, flags=re.MULTILINE | re.I)

    reverse_matches = list(
        re.finditer(
            r"^([A-Z][A-Za-z0-9 ,.'():&—–-]{12,180})\nDAY\s*(\d+)\s*$",
            section,
            re.MULTILINE,
        )
    )
    reverse_matches = [
        m
        for m in reverse_matches
        if not re.search(r"TRAGUIN|Page \d|Premium Travel|Premium Luxury|Premium Holidays|NL-\d{3}", m.group(1), re.I)
    ]
    if reverse_matches:
        day_nums = [int(m.group(2)) for m in reverse_matches]
        if day_nums[0] == 1 and day_nums == list(range(1, len(day_nums) + 1)):
            parsed = []
            for idx, match in enumerate(reverse_matches):
                day_num = int(match.group(2))
                title_line = match.group(1).strip()
                body_start = match.end()
                body_end = reverse_matches[idx + 1].start() if idx + 1 < len(reverse_matches) else len(section)
                parsed.append(_parse_day_body(day_num, title_line, section[body_start:body_end]))
            return parsed

    solo_day_starts = list(re.finditer(r"^DAY\s*(\d+)\s*$", section, re.MULTILINE | re.IGNORECASE))
    if solo_day_starts:
        parsed = []
        lines = section.splitlines()
        day_line_indices = [section[: m.start()].count("\n") for m in solo_day_starts]
        for idx, match in enumerate(solo_day_starts):
            day_num = int(match.group(1))
            line_idx = day_line_indices[idx]
            next_line_idx = day_line_indices[idx + 1] if idx + 1 < len(solo_day_starts) else len(lines)

            before: list[str] = []
            j = line_idx - 1
            while j >= 0:
                ln = lines[j].strip()
                if not ln:
                    if before:
                        break
                    j -= 1
                    continue
                if re.match(rf"^({'|'.join(_ACTIVITY_LABELS)})\b", ln, re.I) or ln.endswith("."):
                    break
                if re.search(r"TRAGUIN|Page \d|NL-\d{3}|Premium Holidays", ln, re.I):
                    j -= 1
                    continue
                if re.match(r"^DAY\s*\d+", ln, re.I):
                    break
                before.insert(0, ln)
                if len(before) >= 3:
                    break
                j -= 1

            after: list[str] = []
            j = line_idx + 1
            while j < next_line_idx:
                ln = lines[j].strip()
                if not ln:
                    j += 1
                    continue
                if re.match(rf"^({'|'.join(_ACTIVITY_LABELS)})\b", ln, re.I) or ln.endswith("."):
                    break
                if re.match(r"^DAY\s*\d+", ln, re.I):
                    break
                after.append(ln)
                if len(after) >= 3:
                    break
                j += 1

            body_lines = lines[line_idx + 1 : next_line_idx]
            if after and (not before or len(after[0]) < len(before[0])):
                title_line = re.sub(r"\s+", " ", " ".join(after)).strip()
                body_lines = lines[line_idx + 1 + len(after) : next_line_idx]
            elif before:
                title_line = re.sub(r"\s+", " ", " ".join(before)).strip()
            else:
                title_line = f"DAY {day_num:02d}"

            parsed.append(_parse_day_body(day_num, title_line, "\n".join(body_lines)))
        if parsed:
            return parsed

    inline_starts = list(re.finditer(r"^DAY\s*(\d+)\s*(?:\||–|-)\s*(.+)$", section, re.MULTILINE | re.IGNORECASE))
    if inline_starts:
        parsed = []
        for idx, match in enumerate(inline_starts):
            day_num = int(match.group(1))
            title_line = re.sub(r"\s+", " ", match.group(2).strip())
            body_start = match.end()
            body_end = inline_starts[idx + 1].start() if idx + 1 < len(inline_starts) else len(section)
            parsed.append(_parse_day_body(day_num, title_line, section[body_start:body_end]))
        return parsed

    day_starts = list(re.finditer(r"^DAY\s*(\d+)\s+(.+)$", section, re.MULTILINE | re.IGNORECASE))
    parsed = []
    for idx, match in enumerate(day_starts):
        day_num = int(match.group(1))
        title_line = re.sub(r"\s+", " ", match.group(2).strip())
        body_start = match.end()
        body_end = day_starts[idx + 1].start() if idx + 1 < len(day_starts) else len(section)
        parsed.append(_parse_day_body(day_num, title_line, section[body_start:body_end]))
    if parsed:
        return parsed
    return _jh.parse_day_blocks(text)


def build_package_highlights(meta: dict, text: str) -> list[str]:
    serial = meta["serial"]
    tour_code = meta["tour_code"]
    category = meta.get("category") or extract_category(text)
    destinations = meta.get("destinations") or extract_destinations(text)
    ideal_for = meta.get("ideal_for") or extract_ideal_for(text)
    best_season = meta.get("best_season") or extract_best_season(text)
    vehicle_meals = meta.get("vehicle_meals") or extract_vehicle_meals(text)
    route = meta.get("route") or extract_route(text)
    highlights = [
        f"Serial code {serial} | TRAGUIN tour code {tour_code}",
        f"State / Country: {STATE} / India | Category: {category}",
        f"Destinations: {destinations}",
        f"Ideal for: {ideal_for}",
        f"Best season: {best_season}",
        f"Starting price: {PRICE_NOTE}",
        f"Vehicle / Meals: {vehicle_meals}",
    ]
    if route:
        highlights.append(f"Route: {route}")
    for sig in parse_signature_highlights(text)[:4]:
        highlights.append(sig)
    for shop in parse_shopping_notes(text)[:2]:
        highlights.append(shop)
    return highlights[:14]


def build_itinerary_highlights(days: list[dict], text: str) -> list[str]:
    sig = parse_signature_highlights(text)
    out = []
    for day in days[:8]:
        short = day["title"].split("|")[0].strip() if "|" in day["title"] else day["title"]
        out.append(f"Day {day['day_number']:02d}: {short}")
    for s in sig[:3]:
        if s not in out:
            out.append(s)
    return out[:10]


def emit_builder(serial: str, meta: dict, text: str, raw_text: str) -> str:
    num = serial.split("-")[1]
    func = f"build_nl_{num}"
    duration = re.sub(r"\s+", " ", extract_duration(text))
    slug = meta["slug"]
    itin_slug = f"{slug}-itinerary"
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = meta.get("days") or parse_day_blocks(text, serial)
    hotels = meta.get("hotels") or []
    included = meta.get("included") or parse_inclusions_exclusions(raw_text)[0]
    excluded = meta.get("excluded")
    if excluded is None:
        _, excluded = parse_inclusions_exclusions(raw_text)
    overview = meta.get("overview") or extract_overview_sections(text)
    pkg_highlights = build_package_highlights({**meta, "serial": serial}, text)
    itin_highlights = build_itinerary_highlights(days, text)
    tagline = meta.get("tagline") or meta.get("destinations") or extract_destinations(text) or title.split("•")[0].strip()

    if not included:
        included = [
            "Premium accommodation in handpicked Nagaland properties.",
            "Private luxury SUV for all transfers and sightseeing.",
            "Daily premium breakfasts and curated dinners as per itinerary.",
            "Dedicated TRAGUIN concierge support throughout the journey.",
        ]
    if not excluded:
        excluded = [
            "Domestic or international airfare to and from Dimapur.",
            "Personal expenses such as laundry, telephone calls, and tips.",
            "Monument entry fees, camera charges, and optional activities.",
            "Travel insurance and expenses not explicitly listed as included.",
        ]

    day_lines = []
    for day in days:
        acts = ",\n".join(f"                    {py_str(a)}" for a in day["activities"]) or f"                    {py_str('Full day as per curated TRAGUIN itinerary.')}"
        day_lines.append(
            f"""            _day(
                {day['day_number']},
                {py_str(day['title'])},
                (
                    {py_str(day['description'])}
                ),
                [
{acts},
                ],
            )"""
        )

    hotel_lines = ",\n".join(emit_hotel(h, duration) for h in hotels)
    inc_lines = []
    sort = 1
    for item in included:
        inc_lines.append(f"            _inc_included({py_str(item)}, {sort}),")
        sort += 1
    for item in excluded:
        inc_lines.append(f"            _inc_excluded({py_str(item)}, {sort}),")
        sort += 1

    ph_lines = ",\n".join(f"            _ph({py_str(h)}, {i})" for i, h in enumerate(pkg_highlights, 1))
    ih_lines = ",\n".join(f"            _ih({py_str(h)}, {i})" for i, h in enumerate(itin_highlights, 1))
    mood_lines = ", ".join(py_str(m) for m in moods)
    seo_title = f"{serial} | {title.split('•')[0].strip()} | TRAGUIN"
    seo_desc = (
        f"Premium {duration} Nagaland package ({serial} / {tour_code}): "
        f"{(meta.get('destinations') or extract_destinations(text))[:100]} with 4-tier handpicked accommodation."
    )

    return f"""
def {func}(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = {py_str(serial)}
    tour_code = {py_str(tour_code)}
    title = {py_str(title)}
    duration = {py_str(duration)}
    slug = {py_str(slug)}
    itin_slug = {py_str(itin_slug)}
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
{ph_lines}
        ],
        moods=[{mood_lines}],
    )
    itinerary = ItineraryCreate(
        slug=itin_slug,
        destination_id=destination_id,
        title=title,
        duration_label=duration,
        duration_days=_duration_days(duration),
        starting_price=0,
        price_note={py_str(PRICE_NOTE)},
        rating=Decimal("4.9"),
        review_count=0,
        tagline={py_str(tagline[:200])},
        overview={py_str(overview)},
        seo_title={py_str(seo_title[:120])},
        seo_description={py_str(seo_desc[:240])},
        is_featured=False,
        featured_sort_order=None,
        is_published=False,
        highlights=[
{ih_lines}
        ],
        days=[
{",\n".join(day_lines)}
        ],
        hotels=[
{hotel_lines}
        ],
        inclusions=[
{chr(10).join(inc_lines)}
        ],
    )
    return package, itinerary
"""


def main() -> None:
    header = '''"""Builder functions for NL-001 through NL-010 Nagaland domestic packages."""

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

NAGALAND_SLUG = "nagaland"


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

'''
    builders = []
    for serial in BUILDER_ORDER:
        path = PDF_DIR / f"{serial}.txt"
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = clean_raw(raw)
        meta = PACKAGE_META[serial]
        builders.append(emit_builder(serial, meta, text, raw))

    builder_names = [f"build_nl_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nNAGALAND_DOMESTIC_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
