#!/usr/bin/env python3
"""Generate kerala_kl_001_010_domestic_batch_defs.py from tmp_kl_pdfs text sources."""

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

PDF_DIR = _SCRIPTS.parent / "tmp_kl_pdfs"
OUT_PATH = _SCRIPTS / "kerala_kl_001_010_domestic_batch_defs.py"

_compact_nights_label = _jh._compact_nights_label
clean_raw = _jh.clean_raw
py_str = _jh.py_str
extract_duration = _jh.extract_duration
extract_category = _jh.extract_category
extract_destinations = _jh.extract_destinations
extract_ideal_for = _jh.extract_ideal_for
extract_best_season = _jh.extract_best_season
extract_starting_price = _jh.extract_starting_price
extract_vehicle_meals = _jh.extract_vehicle_meals
extract_route = _jh.extract_route
extract_overview_sections = _jh.extract_overview_sections
parse_inclusions_exclusions = _jh.parse_inclusions_exclusions
parse_signature_highlights = _jh.parse_signature_highlights
parse_shopping_notes = _jh.parse_shopping_notes
_infer_nights_from_duration = _jh._infer_nights_from_duration


def _kl_hotel(
    sort_order: int,
    category: str,
    *,
    nights_label: str,
    room_type: str = "Deluxe Room",
    meal_plan: str = "MAPAI (Breakfast & Dinner)",
    stars: int | None = None,
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
    "KL-001": {
        "tour_code": "TG-KRL-FAM-06D",
        "slug": "kl-001-munnar-thekkady-alleppey-family",
        "title": "Munnar • Thekkady • Alleppey • Cochin",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _kl_hotel(1, "Deluxe", munnar="The Leaf Munnar / Amber Dale", thekkady="Elephant Court / Poetree", alleppey="Premium AC Houseboat (Private)", cochin="Trident Cochin / Radisson", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin"),
            _kl_hotel(2, "Premium", munnar="Blanket Hotel / Fragrant Nature", thekkady="Greenwoods Resort / Spice Village", alleppey="Luxury Glass-Walled Houseboat", cochin="Crowne Plaza / Marriott", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin"),
            _kl_hotel(3, "Luxury", munnar="Chandy's Windy Woods / Panoramic Getaway", thekkady="The Niraamaya Retreats Cardamom Club", alleppey="Ultra-Luxury Suite Houseboat", cochin="Grand Hyatt Bolgatty / Le Meridien", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin", stars=5),
            _kl_hotel(4, "Ultra Luxury", munnar="The Panoramic Getaway (Presidential)", thekkady="Spice Village (Private Pool Villa)", alleppey="TRAGUIN Signature Royal Houseboat", cochin="Brunton Boatyard / Taj Malabar Resort", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin", stars=5),
        ],
    },
    "KL-002": {
        "tour_code": "TG-KRL-GRD-08D",
        "slug": "kl-002-cochin-munnar-kovalam-grand-family",
        "title": "Cochin • Munnar • Thekkady • Alleppey • Kovalam",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _kl_hotel(1, "Deluxe", cochin="Trident / Radisson", munnar="The Leaf / Amber Dale", thekkady="Elephant Court / Poetree", alleppey="Premium Private Houseboat", kovalam="Isola Di Cocco / Travancore", nights_label="1N Cochin + 2N Munnar + 1N Thekkady + 1N Alleppey + 2N Kovalam"),
            _kl_hotel(2, "Premium", cochin="Crowne Plaza / Marriott", munnar="Blanket Hotel / Fragrant Nature", thekkady="Greenwoods / Spice Village", alleppey="Luxury Glass-Walled Cruise", kovalam="Turtle on the Beach / Travancore", nights_label="1N Cochin + 2N Munnar + 1N Thekkady + 1N Alleppey + 2N Kovalam"),
            _kl_hotel(3, "Luxury", cochin="Grand Hyatt Bolgatty Resort", munnar="Chandy's Windy Woods Luxury", thekkady="Niraamaya Cardamom Club", alleppey="Ultra-Luxury Private Suite Boat", kovalam="The Leela Kovalam (Garden Suite)", nights_label="1N Cochin + 2N Munnar + 1N Thekkady + 1N Alleppey + 2N Kovalam", stars=5),
            _kl_hotel(4, "Ultra Luxury", cochin="Brunton Boatyard / Taj Malabar", munnar="The Panoramic Getaway (Suites)", thekkady="Spice Village (Private Pool Villa)", alleppey="TRAGUIN Signature Royal Boat", kovalam="The Leela Kovalam (Club Ocean View)", nights_label="1N Cochin + 2N Munnar + 1N Thekkady + 1N Alleppey + 2N Kovalam", stars=5),
        ],
    },
    "KL-003": {
        "tour_code": "TRAGUIN-MNNR-05",
        "slug": "kl-003-munnar-kochi-family",
        "title": "Munnar • Kochi Family Getaway",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _kl_hotel(1, "Deluxe", munnar="The Leaf Munnar / Amber Dale", cochin="Trident Cochin / Radisson Blu", nights_label="3N Munnar + 1N Kochi", meal_plan="Breakfast & Dinner (MAP)"),
            _kl_hotel(2, "Premium", munnar="Blanket Hotel / Fragrant Nature", cochin="Brunton Boatyard / Grand Hyatt Bolgatty", nights_label="3N Munnar + 1N Kochi", meal_plan="Breakfast & Dinner (MAP)"),
            _kl_hotel(3, "Luxury", munnar="Chandy's Windy Woods / Elixir Hills", cochin="Cochin Marriott / Taj Malabar Resort", nights_label="3N Munnar + 1N Kochi", meal_plan="Breakfast & Dinner (MAP)", stars=5),
            _kl_hotel(4, "Ultra Luxury", munnar="Spice Tree / Windermere Estate", cochin="Taj Malabar Heritage / Grand Hyatt Presidential", nights_label="3N Munnar + 1N Kochi", meal_plan="Premium Curated Meals (MAP)", stars=5),
        ],
    },
    "KL-004": {
        "tour_code": "TRAGUIN-KL-004-FAM",
        "slug": "kl-004-premium-kerala-family-beach-vacation",
        "title": "Premium Kerala Family Tour",
        "moods": ["Family", "Luxury", "Beach"],
        "hotels": [
            _kl_hotel(1, "Deluxe", alleppey="Ramada by Wyndham / Lake Palace", kovalam="Isola Di Cocco / Uday Samudra", nights_label="1N Alleppey + 4N Kovalam / Poovar", room_type="Superior Sea View", meal_plan="MAPAI"),
            _kl_hotel(2, "Premium", alleppey="Kumarakom Lake Resort / Vasundhara", kovalam="The Raviz Kovalam / Niraamaya", nights_label="1N Alleppey + 4N Kovalam / Poovar", room_type="Premium Heritage Villa", meal_plan="MAPAI"),
            _kl_hotel(3, "Luxury", alleppey="Forte Kochi / Marari Beach Resort", kovalam="Taj Green Cove Resort & Spa", nights_label="1N Alleppey + 4N Kovalam / Poovar", room_type="Luxury Garden Cottage", meal_plan="MAPAI", stars=5),
            _kl_hotel(4, "Ultra Luxury", alleppey="The Oberoi Vrinda Luxury Cruiser", kovalam="The Leela Kovalam (Club Rooms)", nights_label="1N Alleppey + 4N Kovalam / Poovar", room_type="The Club Suite Ocean View", meal_plan="MAPAI", stars=5),
        ],
    },
    "KL-005": {
        "tour_code": "TRG-KLR-2026-005",
        "slug": "kl-005-romantic-honeymoon-munnar-alleppey",
        "title": "Munnar • Alleppey Houseboat • Cochin Luxury Escape",
        "moods": ["Romantic", "Honeymoon", "Luxury"],
        "hotels": [
            _kl_hotel(1, "Deluxe", munnar="The Leaf Munnar (Valley View Room)", alleppey="Premium AC Houseboat (Private)", cochin="Trident Cochin (Superior Room)", nights_label="2N Munnar + 1N Alleppey + 1N Cochin", meal_plan="CPAI (Munnar) & APAI (Houseboat)"),
            _kl_hotel(2, "Premium", munnar="Blanket Hotel & Spa (Premier Room)", alleppey="Luxury Glass Houseboat (Private)", cochin="Brunton Boatyard (Sea Facing Room)", nights_label="2N Munnar + 1N Alleppey + 1N Cochin", meal_plan="CPAI (Munnar) & APAI (Houseboat)"),
            _kl_hotel(3, "Luxury", munnar="Chandy's Windy Woods (Super Deluxe)", alleppey="Super Luxury Cruise (Upper Deck)", cochin="Grand Hyatt Bolgatty (Club Room)", nights_label="2N Munnar + 1N Alleppey + 1N Cochin", meal_plan="CPAI (Munnar) & APAI (Houseboat)", stars=5),
            _kl_hotel(4, "Ultra Luxury", munnar="Spice Tree Munnar (Classic Pool Villa)", alleppey="TRAGUIN Signature Elite Houseboat", cochin="The Leela Kovalam / Cochin Elite", nights_label="2N Munnar + 1N Alleppey + 1N Cochin", meal_plan="CPAI (Munnar) & APAI (Houseboat)", stars=5),
        ],
    },
    "KL-006": {
        "tour_code": "TRAGUIN-KL-ROMANCE-06",
        "slug": "kl-006-honeymoon-romance-munnar-kovalam",
        "title": "Munnar • Thekkady • Alleppey • Kovalam",
        "moods": ["Romantic", "Honeymoon", "Luxury"],
        "hotels": [
            _kl_hotel(1, "Deluxe", munnar="The Fog Munnar / Leaf Resort", thekkady="Greenwoods Resort / Poetree", alleppey="Premium Private Houseboat", kovalam="Soma Palmshore / Travancore", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Kovalam", room_type="Valley View / Deluxe Room / Deluxe AC Cabin / Standard Sea View"),
            _kl_hotel(2, "Premium", munnar="Blanket Hotel / Amber Dale", thekkady="Elephant Court / Spice Village", alleppey="Luxury Private Houseboat", kovalam="Turtle on the Beach / Isola Di Cocco", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Kovalam", room_type="Premier Valley View / Patio Room / Luxury Glass AC Cabin / Premium Sea View"),
            _kl_hotel(3, "Luxury", munnar="Fragrant Nature / Chandy's Windy Woods", thekkady="Cardamom County / Niraamaya Wilderness", alleppey="Ultra Luxury Houseboat", kovalam="The Leela Kovalam / Taj Green Cove", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Kovalam", room_type="Executive Suite / Garden Cottage / Suite AC Cruise Cabin / Garden View Pavilion", stars=5),
            _kl_hotel(4, "Ultra Luxury", munnar="Elixir Hills / Windermere Estate", thekkady="Spice Village - CGH Earth", alleppey="Xandari Riverscapes Houseboat", kovalam="The Leela Kovalam / Taj Green Cove", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Kovalam", room_type="Private Pool Suite / Private Spice Garden Villa / Ultra Premium Premium Deck / Club Premium Sea View Suite", stars=5),
        ],
    },
    "KL-007": {
        "tour_code": "TG-KRL-MNNR-06D",
        "slug": "kl-007-munnar-thekkady-alleppey-honeymoon",
        "title": "Munnar Thekkady Alleppey Honeymoon",
        "moods": ["Romantic", "Honeymoon", "Luxury"],
        "hotels": [
            _kl_hotel(1, "Deluxe", munnar="The Leaf Munnar / Amber Dale Luxury Resort", thekkady="Elephant Court / Poetree Sarovar Portico", alleppey="Premium Private Houseboat Alliance", cochin="Trident Cochin / Radisson Blu", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin", room_type="Valley View Room / Patio Room / Deluxe AC Cabin / Superior Room", meal_plan="MAPAI"),
            _kl_hotel(2, "Premium", munnar="Fragrant Nature Munnar / Elixir Hills Suites", thekkady="Greenwoods Resort / Spice Village CGH Earth", alleppey="Luxury Cruise Lines Alleppey", cochin="Brunton Boatyard CGH Earth / Casino Hotel", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin", room_type="Tropic Green Suite / Aranya Room / Premium Glass-Wall AC / Sea Facing Room", meal_plan="MAPAI"),
            _kl_hotel(3, "Luxury", munnar="Blanket Hotel & Spa / Chandy's Windy Woods", thekkady="The Niraamaya Retreats Cardamom Club", alleppey="Our Land Island Resort / Xandari Riverscapes", cochin="Grand Hyatt Bolgatty / Kochi Marriott", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin", room_type="Executive Suite / Luxury Garden Cottage / Ultra Luxury Houseboat / Club Lake View Room", meal_plan="MAPAI", stars=5),
            _kl_hotel(4, "Ultra Luxury", munnar="Windermere Estate / Spice Tree Munnar", thekkady="The Elephant Court Elite Pool Villas", alleppey="Kumarakom Lake Resort / Spice Coast Cruises", cochin="The Brunton Boatyard Premium Sea Suites", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin", room_type="Private Pool Villa / Private Pool Suite / Presidential Suite Cruise / Grand Harbour Suite", meal_plan="MAPAI", stars=5),
        ],
    },
    "KL-008": {
        "tour_code": "TRAGUIN-KL-WE-008",
        "slug": "kl-008-kerala-wellness-escape",
        "title": "Kerala Wellness Escape",
        "moods": ["Wellness", "Luxury", "Nature"],
        "included": [
            "Luxury accommodation in handpicked top-rated female-friendly resorts.",
            "Daily buffet breakfasts and expertly curated nutritious gourmet dinners.",
            "All meals included during the luxury Alleppey Houseboat stay.",
            "Premium private Chauffeur-driven luxury SUV for all transfers and sightseeing.",
            "Complimentary traditional Ayurvedic wellness consultation upon arrival.",
            "Complimentary guided organic Spice Plantation tour in Thekkady.",
            "Special welcome amenities and premium TRAGUIN on-ground support.",
            "All current fuel, toll, parking, and driver allowances included.",
        ],
        "excluded": [
            "Domestic or International airfares and train tickets.",
            "Entry tickets to monuments, museums, and national parks.",
            "Personal expenses like laundry, phone calls, and alcoholic beverages.",
            "Optional activities, specialized treks, or extra spa treatments.",
            "Any camera or video tracking fees at sight locations.",
            "Travel and medical insurance policies.",
            "GST/TCS or extra regulatory taxes if applicable.",
        ],
        "hotels": [
            _kl_hotel(1, "Deluxe", munnar="The Fog Munnar (Valley View Room)", thekkady="Elephant Court (Patio Room)", alleppey="Premium A/C Luxury Houseboat", cochin="Trident Cochin (Superior Room)", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin"),
            _kl_hotel(2, "Premium", munnar="Blanket Hotel & Spa", thekkady="Spice Village", alleppey="Ultra-Luxury Private Houseboat", cochin="Fragrant Nature Cochin", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin"),
            _kl_hotel(3, "Luxury", munnar="Chandy's Windy Woods", thekkady="Cardamom County", alleppey="TRAGUIN Signature Cruise", cochin="Brunton Boatyard", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin", stars=5),
            _kl_hotel(4, "Ultra Luxury", munnar="The Panoramic Getaway", thekkady="Niraamaya Cardamom Club", alleppey="Elite Glass-Enclosed Vessel", cochin="Malabar House", nights_label="2N Munnar + 1N Thekkady + 1N Alleppey + 1N Cochin", stars=5),
        ],
    },
    "KL-009": {
        "tour_code": "TRAGUIN-KL-SR-009",
        "slug": "kl-009-senior-citizen-kumarakom-relaxed",
        "title": "Cochin • Munnar • Kumarakom • Alleppey — Relax Kerala Passage",
        "moods": ["Family", "Luxury", "Wellness"],
        "hotels": [
            _kl_hotel(1, "Deluxe", munnar="The Fog Munnar (Ground Floor Valley)", kumarakom="Abad Whispering Palms (Garden Room)", cochin="Trident Cochin (Accessible Superior)", nights_label="2N Munnar + 2N Kumarakom + 1N Cochin"),
            _kl_hotel(2, "Premium", munnar="Blanket Hotel & Spa (Executive Suite)", kumarakom="Kumarakom Lake Resort (Luxury Pavilion)", cochin="Fragrant Nature Cochin (Executive Room)", nights_label="2N Munnar + 2N Kumarakom + 1N Cochin"),
            _kl_hotel(3, "Luxury", munnar="Chandy's Windy Woods (Premium Suite)", kumarakom="The Zuri Kumarakom (Waterfront Villa)", cochin="Brunton Boatyard (Heritage Room)", nights_label="2N Munnar + 2N Kumarakom + 1N Cochin", stars=5),
            _kl_hotel(4, "Ultra Luxury", munnar="The Panoramic Getaway (Elite Suite)", kumarakom="Niraamaya Retreats Backwaters & Beyond", cochin="The Malabar House (Grand Premium Suite)", nights_label="2N Munnar + 2N Kumarakom + 1N Cochin", stars=5),
        ],
    },
    "KL-010": {
        "tour_code": "TG-WYN-ADV-2026",
        "slug": "kl-010-wayanad-adventure-escape",
        "title": "TRAGUIN Wayanad Adventure Escape",
        "moods": ["Adventure", "Nature", "Luxury"],
        "hotels": [
            _kl_hotel(1, "Deluxe", wayanad="Vythiri Village Resort / Wayanad Silver Woods", nights_label="4N Wayanad", room_type="Deluxe Hill View Room", meal_plan="MAP (Breakfast & Dinner)"),
            _kl_hotel(2, "Premium", wayanad="The Woods Resorts / After the Rains", nights_label="4N Wayanad", room_type="Premium Cottage Block", meal_plan="MAP (Breakfast & Dinner)"),
            _kl_hotel(3, "Luxury", wayanad="Mountain Shadows Resort / Pepper Trail Luxury", nights_label="4N Wayanad", room_type="Luxury Lake View Villa", meal_plan="MAP (Breakfast & Dinner)", stars=5),
            _kl_hotel(4, "Ultra Luxury", wayanad="Evolve Back Kabini / Vythiri Resort Treehouse", nights_label="4N Wayanad", room_type="Private Pool Villa / Luxury Treehouse", meal_plan="MAP (Breakfast & Dinner)", stars=5),
        ],
    },
}

BUILDER_ORDER = [f"KL-{i:03d}" for i in range(1, 11)]


def parse_day_blocks(text: str) -> list[dict]:
    start = re.search(
        r"(?:DETAILED DAY-WISE ITINERARY|YOUR BESPOKE DAY-WISE ITINERARY|DAY WISE ITINERARY|"
        r"DAY-WISE ITINERARY|DAY-WISE CUSTOM(?: TRAVEL)? ITINERARY|DETAILED DAY-WISE ITINERARY)",
        text,
        re.IGNORECASE,
    )
    if start:
        section = text[start.end():]
    else:
        day_one = re.search(r"^DAY\s*0?1\s+(?:\||–|-|\w)", text, re.MULTILINE | re.IGNORECASE)
        if not day_one:
            return []
        section = text[day_one.start():]
    end = re.search(
        r"(?m)^(?:ACCOMMODATION OPTIONS|HANDPICKED (?:LUXURY )?(?:PREMIUM )?(?:ACCOMMODATION|HOTEL)|"
        r"PREMIUM ACCOMMODATION|PREMIUM HOTEL SELECTION|HOTEL OPTIONS SECTION|"
        r"HANDPICKED PREMIUM ACCOMMODATION|HANDPICKED ACCOMMODATION|"
        r"HANDPICKED PREMIUM HOTEL|PREMIUM HOTEL OPTIONS|CURATED HOTEL ACCOMMODATIONS|"
        r"HANDPICKED PREMIUM ACCOMMODATIONS|PREMIUM ACCOMMODATION SELECTIONS)",
        section,
    )
    if end:
        section = section[: end.start()]
    section = _jh.FOOTER_RE.sub("", section)
    section = _jh.PAGE_RE.sub("", section)
    return _jh.parse_day_blocks(f"DETAILED DAY-WISE ITINERARY\n{section}")


def build_package_highlights(meta: dict, text: str) -> list[str]:
    serial = meta["serial"]
    tour_code = meta["tour_code"]
    category = extract_category(text)
    destinations = extract_destinations(text)
    ideal_for = extract_ideal_for(text)
    best_season = extract_best_season(text)
    starting_price = extract_starting_price(text)
    vehicle_meals = extract_vehicle_meals(text)
    route = extract_route(text)
    highlights = [
        f"Serial code {serial} | TRAGUIN tour code {tour_code}",
        f"State / Country: Kerala / India | Category: {category}",
        f"Destinations: {destinations}",
        f"Ideal for: {ideal_for}",
        f"Best season: {best_season}",
        f"Starting price: {starting_price}",
        f"Vehicle / Meals: {vehicle_meals}",
    ]
    if route:
        highlights.append(f"Route: {route}")
    for sig in parse_signature_highlights(text)[:4]:
        if sig.strip():
            highlights.append(sig)
    for shop in parse_shopping_notes(text)[:2]:
        if shop.strip():
            highlights.append(shop)
    return [h for h in highlights if h.strip()][:14]


def build_itinerary_highlights(days: list[dict], text: str) -> list[str]:
    sig = parse_signature_highlights(text)
    out = []
    for day in days[:10]:
        short = day["title"].split("|")[0].strip() if "|" in day["title"] else day["title"]
        out.append(f"Day {day['day_number']:02d}: {short}")
    for s in sig[:3]:
        if s.strip() and s not in out:
            out.append(s)
    return [h for h in out if h.strip()][:10]


def emit_hotel(hotel: dict, duration: str) -> str:
    nights = hotel.get("nights_label") or _infer_nights_from_duration(duration)
    desc = hotel.get("description") or (
        f"OPTION {hotel['sort_order']:02d} – {hotel['category'].upper()}: "
        f"{hotel['name']} ({hotel.get('location', 'Kerala')}) | {hotel['meal_plan']}"
    )
    name = hotel["name"][:128]
    location = (hotel.get("location") or "Kerala")[:128]
    room_type = hotel["room_type"][:128]
    meal_plan = hotel["meal_plan"][:128]
    desc = desc[:240]
    return f"""            _hotel(
                {py_str(name)},
                {py_str(location)},
                {py_str(nights)},
                {py_str(hotel['category'])},
                {py_str(room_type)},
                {py_str(meal_plan)},
                {hotel['stars']},
                {hotel['sort_order']},
                description={py_str(desc)},
            )"""


def emit_builder(serial: str, meta: dict, text: str, raw_text: str) -> str:
    num = serial.split("-")[1]
    func = f"build_kl_{num}"
    duration = re.sub(r"\s+", " ", extract_duration(text))
    slug = meta["slug"]
    itin_slug = f"{slug}-itinerary"
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = parse_day_blocks(text)
    hotels = meta.get("hotels") or _jh.parse_hotel_options(text)
    included = meta.get("included") or parse_inclusions_exclusions(raw_text)[0]
    excluded = meta.get("excluded")
    if excluded is None:
        _, excluded = parse_inclusions_exclusions(raw_text)
    overview = extract_overview_sections(text)
    meta_with_serial = {**meta, "serial": serial}
    pkg_highlights = build_package_highlights(meta_with_serial, text)
    itin_highlights = build_itinerary_highlights(days, text)
    starting_price = extract_starting_price(text)
    tagline = title.split("•")[0].strip() if "•" in title else title

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
        f"Premium {duration} Kerala package ({serial} / {tour_code}): "
        f"{extract_destinations(text)[:100]} with 4-tier handpicked accommodation."
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
        price_note={py_str(starting_price)},
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
    header = '''"""Builder functions for KL-001 through KL-010 Kerala domestic packages."""

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

'''
    builders = []
    for serial in BUILDER_ORDER:
        path = PDF_DIR / f"{serial}.txt"
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = clean_raw(raw)
        meta = PACKAGE_META[serial]
        builders.append(emit_builder(serial, meta, text, raw))

    builder_names = [f"build_kl_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nKERALA_KL_001_010_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
