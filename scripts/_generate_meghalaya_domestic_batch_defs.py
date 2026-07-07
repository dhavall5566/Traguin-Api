#!/usr/bin/env python3
"""Generate meghalaya_domestic_batch_defs.py from tmp_ml_pdfs text sources."""

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

PDF_DIR = _SCRIPTS.parent / "tmp_ml_pdfs"
OUT_PATH = _SCRIPTS / "meghalaya_domestic_batch_defs.py"
PRICE_NOTE = "On Request (Premium Class)"

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


def _ml_hotel(
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
    "ML-001": {
        "tour_code": "TRG-MEG-001",
        "slug": "ml-001-shillong-escape-journey-into-the-abode-of-clouds",
        "title": "Shillong Escape — Journey Into the Abode of Clouds",
        "moods": ["Family", "Nature", "Luxury"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Polo Towers / similar", cherrapunji="Sohra Plaza / similar", nights_label="2N Shillong + 1N Cherrapunji", meal_plan="MAPAI (Breakfast & Dinner)"),
            _ml_hotel(2, "Premium", shillong="M crown Hotel / MBL Luxury Stay", cherrapunji="Cherrapunji Holiday Resort / similar", nights_label="2N Shillong + 1N Cherrapunji", meal_plan="MAPAI (Breakfast & Dinner)"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai Resort / Vivanta Shillong", cherrapunji="Polo Orchid Resort (Jasmine Suite)", nights_label="2N Shillong + 1N Cherrapunji", room_type="Luxury Lake View | Orchid Suite", meal_plan="MAPAI Plan + Welcome Kit", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="Ri Kynjai (Premium Lake View Cottage)", cherrapunji="Jiva Resort Cherrapunji (Luxury Suite)", nights_label="2N Shillong + 1N Cherrapunji", room_type="Premium Lake View Cottage | Luxury Suite", meal_plan="Bespoke Signature MAPAI Plan", stars=5),
        ],
    },
    "ML-002": {
        "tour_code": "TRG-MEG-002",
        "slug": "ml-002-shillong-cherrapunji-mawlynnong-dawki",
        "title": "Shillong • Cherrapunji • Mawlynnong • Dawki",
        "moods": ["Family", "Nature", "Luxury"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Polo Towers / M-設計 Boutique", cherrapunji="Sohra Plaza Heritage / similar", nights_label="3N Shillong + 2N Cherrapunji", room_type="Executive Deluxe Room", meal_plan="MAPAI (Breakfast & Dinner)"),
            _ml_hotel(2, "Premium", shillong="The Heritage Club - Tripura Castle", cherrapunji="Cherrapunjee Holiday Resort", nights_label="3N Shillong + 2N Cherrapunji", room_type="Premium Balcony Room", meal_plan="MAPAI (Breakfast & Dinner)"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai Serene Lake Resort", cherrapunji="Polo Orchid Resort Cherrapunji", nights_label="3N Shillong + 2N Cherrapunji", room_type="Luxury Lake View Cottage / Orchid Suite", meal_plan="MAPAI (Breakfast & Dinner)", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="Ri Kynjai (Premium Presidential Suite)", cherrapunji="Jiva Resort Cherrapunji (Luxury Villa)", nights_label="3N Shillong + 2N Cherrapunji", room_type="Presidential Suite | Luxury Villa", meal_plan="VVIP Custom Handpicked Private Retreat", stars=5),
        ],
    },
    "ML-003": {
        "tour_code": "TRG-MEG-003",
        "slug": "ml-003-romantic-meghalaya-escape-romance-in-the-abode-of-clouds",
        "title": "Romantic Meghalaya Escape • Romance in the Abode of Clouds",
        "moods": ["Honeymoon", "Romance", "Luxury"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Centre Point / M crown", cherrapunjee="Sohra Plaza Resort / similar", shnongpdeng="Standard Riverside Tents", nights_label="2N Shillong + 2N Cherrapunjee + 1N Shnongpdeng"),
            _ml_hotel(2, "Premium", shillong="Polo Towers / Landmark Victoria", cherrapunjee="Cherrapunjee Holiday Resort", shnongpdeng="Premium Riverside Glamping", nights_label="2N Shillong + 2N Cherrapunjee + 1N Shnongpdeng"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai Resort / Orchid Lake", cherrapunjee="Polo Orchid Resort (Jungle Suite)", shnongpdeng="Luxury Wooden Eco Cottage", nights_label="2N Shillong + 2N Cherrapunjee + 1N Shnongpdeng", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="Ri Kynjai (Cottage Suite Suite)", cherrapunjee="Jiva Resort (VVIP Luxury Suite)", shnongpdeng="Bespoke Private Luxury Swiss Camp", nights_label="2N Shillong + 2N Cherrapunjee + 1N Shnongpdeng", stars=5),
        ],
    },
    "ML-004": {
        "tour_code": "TRG-MEG-004",
        "slug": "ml-004-living-route-bridges-wilderness-luxury-escape",
        "title": "Living Route Bridges & Wilderness Luxury Escape",
        "moods": ["Adventure", "Nature", "Luxury"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Polo Towers / M-Crown", cherrapunjee="Cherrapunjee Holiday Resort", dawki="Dawki Riverside Luxury Tents", nights_label="2N Shillong + 2N Cherrapunjee + 1N Dawki"),
            _ml_hotel(2, "Premium", shillong="Courtyard by Marriott Shillong", cherrapunjee="Polo Orchid Resort / similar", dawki="Betelnut Resort Shnongpdeng", nights_label="2N Shillong + 2N Cherrapunjee + 1N Dawki"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai Serene Lake Resort", cherrapunjee="Jiva Resort Cherrapunjee", dawki="Bespoke Private Riverside Glamp", nights_label="2N Shillong + 2N Cherrapunjee + 1N Dawki", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="Ri Kynjai (Cottage Suite)", cherrapunjee="Jiva Resort (Luxury Villa)", dawki="TRAGUIN VVIP Customized Elite Setup", nights_label="2N Shillong + 2N Cherrapunjee + 1N Dawki", stars=5),
        ],
    },
    "ML-005": {
        "tour_code": "TRG-MEG-005",
        "slug": "ml-005-meghalaya-discovery-journey-into-the-abode-of-clouds",
        "title": "Meghalaya Discovery • Journey Into the Abode of Clouds",
        "moods": ["Family", "Nature", "Luxury"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Polo Towers / M-Pratibha / similar", cherrapunji="Cherrapunji Holiday Resort / similar", nights_label="4N Shillong + 2N Cherrapunji", meal_plan="MAPAI Plan (Daily Breakfast & Dinner)"),
            _ml_hotel(2, "Premium", shillong="Rigal Heritage / Courtyard by Marriott", cherrapunji="Saimika Resort / Jiva Resort (Executive)", nights_label="4N Shillong + 2N Cherrapunji", meal_plan="MAPAI + Premium Room Upgrades"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai Serenity By The Lake / similar", cherrapunji="Polo Orchid Resort (Orchid Rooms)", nights_label="4N Shillong + 2N Cherrapunji", room_type="Private Balcony View Suites", meal_plan="MAPAI + Private Balcony View Suites", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="Ri Kynjai (Luxury Heritage Cottage)", cherrapunji="Polo Orchid Resort (Log Cabin With Private Plunge Pool)", nights_label="4N Shillong + 2N Cherrapunji", meal_plan="VVIP Custom Chef Curated Dining", stars=5),
        ],
    },
    "ML-006": {
        "tour_code": "TRG-MEG-ML-006",
        "slug": "ml-006-meghalaya-ladies-escape-abode-of-clouds-sisterhood",
        "title": "Meghalaya Ladies Escape • Abode of Clouds & Sisterhood",
        "moods": ["Wellness", "Adventure", "Luxury"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Polo Towers / M-Pratishtha", cherrapunjee="Cherrapunjee Holiday Resort", nights_label="3N Shillong + 2N Cherrapunjee", room_type="Deluxe Balcony Room"),
            _ml_hotel(2, "Premium", shillong="The Heritage Club - Tripura Castle", cherrapunjee="Jiva Resort / Polo Orchid Resort", nights_label="3N Shillong + 2N Cherrapunjee", room_type="Premium Executive Room"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai - Serenity By The Lake", cherrapunjee="Saimika Resort Luxury Chalet", nights_label="3N Shillong + 2N Cherrapunjee", room_type="Luxury Lakeview / Cliff Suite", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="Ri Kynjai (Cottage Suite)", cherrapunjee="Jiva Resort (Royal Presidential Suite)", nights_label="3N Shillong + 2N Cherrapunjee", room_type="VVIP Private Villa Signature Club", stars=5),
        ],
    },
    "ML-007": {
        "tour_code": "TRG-MEG-007",
        "slug": "ml-007-leisure-meghalaya-escape-the-abode-of-clouds",
        "title": "Leisure Meghalaya Escape • The Abode of Clouds",
        "moods": ["Leisure", "Family", "Luxury"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Polo Towers / similar", cherrapunji="Polo Orchid Resort (Deluxe)", nights_label="3N Shillong + 2N Cherrapunji", room_type="Deluxe Room", meal_plan="MAPAI (Breakfast & Dinner)", description_extra="Lift Access & Flat Walkways"),
            _ml_hotel(2, "Premium", shillong="M crown Hotel / Courtyard by Marriott", cherrapunji="Cherrapunjee Holiday Resort", nights_label="3N Shillong + 2N Cherrapunji", room_type="Premium Room", meal_plan="MAPAI (Breakfast & Dinner)", description_extra="Wheelchair assistance on request"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai Serene Lake Resort", cherrapunji="Jiva Resort Cherrapunji (Suite)", nights_label="3N Shillong + 2N Cherrapunji", room_type="Premium ground-floor valley view suites", meal_plan="MAPAI (Breakfast & Dinner)", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="The Heritage Club - Tripura Castle (VVIP)", cherrapunji="Jiva Resort (Royal Luxury Executive)", nights_label="3N Shillong + 2N Cherrapunji", room_type="VVIP Suite", meal_plan="Bespoke luxury customized priority support", stars=5),
        ],
    },
    "ML-008": {
        "tour_code": "TRG-MEG-008",
        "slug": "ml-008-luxury-meghalaya-escape-the-abode-of-clouds",
        "title": "Luxury Meghalaya Escape • The Abode of Clouds",
        "moods": ["Luxury", "Honeymoon", "Nature"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Polo Towers / M-Pratiba", cherrapunji="Sohra Plaza Resort / similar", dawki="Betelnut Resort Dawki / similar", nights_label="3N Shillong + 2N Cherrapunji + 1N Dawki"),
            _ml_hotel(2, "Premium", shillong="Courtyard by Marriott Shillong", cherrapunji="Cherrapunjee Holiday Resort", dawki="Dawki Exotic Glamping Tents", nights_label="3N Shillong + 2N Cherrapunji + 1N Dawki"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai Serene Lake Resort", cherrapunji="Polo Orchid Resort Cherrapunji", dawki="ShantiDawki Luxury Riverfront Cabins", nights_label="3N Shillong + 2N Cherrapunji + 1N Dawki", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="Ri Kynjai (Premium Heritage Cottage)", cherrapunji="Polo Orchid (Log Cabin with Private Pool)", dawki="VVIP Custom Private Luxury Eco-Retreat", nights_label="3N Shillong + 2N Cherrapunji + 1N Dawki", stars=5),
        ],
    },
    "ML-009": {
        "tour_code": "TRG-MEG-009",
        "slug": "ml-009-caving-meghalaya-the-subterranean-chronicles-mystic-hills",
        "title": "Caving Meghalaya • The Subterranean Chronicles & Mystic Hills",
        "moods": ["Adventure", "Nature", "Luxury"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Centre Point / similar", cherrapunjee="Sohra Plaza / similar", shnongpdeng="Standard Eco Comfort Lodge", nights_label="2N Shillong + 2N Cherrapunjee + 1N Shnongpdeng"),
            _ml_hotel(2, "Premium", shillong="Mawiandun Boutique / similar", cherrapunjee="Jiva Resort / similar", shnongpdeng="Premium Riverside Glamping Tents", nights_label="2N Shillong + 2N Cherrapunjee + 1N Shnongpdeng"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai Serenity By The Lake", cherrapunjee="Polo Orchid Resort (Log Cabin)", shnongpdeng="Bespoke Eco-Luxury Tented Suites", nights_label="2N Shillong + 2N Cherrapunjee + 1N Shnongpdeng", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="Ri Kynjai (Luxury Heritage Cottage)", cherrapunjee="Polo Orchid (Presidential Villa with Pool)", shnongpdeng="VIP Private Custom Riverside Cottage", nights_label="2N Shillong + 2N Cherrapunjee + 1N Shnongpdeng", stars=5),
        ],
    },
    "ML-010": {
        "tour_code": "TRG-MEG-010",
        "slug": "ml-010-complete-meghalaya-explorer-symphony-of-clouds-cascades",
        "title": "Complete Meghalaya Explorer • Symphony of Clouds & Cascades",
        "moods": ["Family", "Nature", "Luxury"],
        "hotels": [
            _ml_hotel(1, "Deluxe", shillong="Hotel Polo Towers / M-Crown / similar", cherrapunjee="Cherrapunjee Holiday Resort / similar", nights_label="5N Shillong + 2N Cherrapunjee", meal_plan="MAPAI (Daily Breakfast & Dinner)"),
            _ml_hotel(2, "Premium", shillong="Rigal Heritage / Pinewood Hotel / similar", cherrapunjee="Sohra Plaza Resort / Jiva Resort (Executive)", nights_label="5N Shillong + 2N Cherrapunjee", meal_plan="MAPAI (Premium Selected Dining)"),
            _ml_hotel(3, "Luxury", shillong="Ri Kynjai Serenity Lake Resort / Similar", cherrapunjee="Jiva Resort (Luxury Suite) / Polo Orchid Resort", nights_label="5N Shillong + 2N Cherrapunjee", meal_plan="MAPAI + Welcome Premium Amenities", stars=5),
            _ml_hotel(4, "Ultra Luxury", shillong="Ri Kynjai (Luxury Cottage Overlooking Lake)", cherrapunjee="Polo Orchid (Log Cabin With Plunge Pool)", nights_label="5N Shillong + 2N Cherrapunjee", meal_plan="Bespoke Custom Signature VVIP Dining", stars=5),
        ],
    },
}

BUILDER_ORDER = [f"ML-{i:03d}" for i in range(1, 11)]


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
        r"(?m)^(?:BOUTIQUE PREMIUM STAY|ACCOMMODATION OPTIONS|HANDPICKED (?:LUXURY )?(?:PREMIUM )?(?:ACCOMMODATION|HOTEL)|"
        r"PREMIUM ACCOMMODATION|PREMIUM HOTEL SELECTION|HOTEL OPTIONS SECTION|"
        r"HANDPICKED PREMIUM ACCOMMODATION OPTIONS|HANDPICKED PREMIUM ACCOMMODATION|HANDPICKED ACCOMMODATION|"
        r"HANDPICKED PREMIUM HOTEL|PREMIUM HOTEL OPTIONS|CURATED HOTEL ACCOMMODATIONS|"
        r"HANDPICKED PREMIUM ACCOMMODATIONS|PREMIUM ACCOMMODATION SELECTIONS)",
        section,
    )
    if end:
        section = section[: end.start()]
    section = _jh.FOOTER_RE.sub("", section)
    section = _jh.PAGE_RE.sub("", section)
    section = re.sub(
        r"TRAGUIN Premium Luxury (?:Itinerary|Proposal)[^\n]*\n\d+\s*\n?",
        "",
        section,
        flags=re.IGNORECASE,
    )
    return _jh.parse_day_blocks(f"DETAILED DAY-WISE ITINERARY\n{section}")


def _clean_items(items: list[str]) -> list[str]:
    out = []
    for item in items:
        item = re.sub(r"\s+", " ", item).strip()
        if not item or len(item) < 8:
            continue
        if re.search(r"TRAGUIN Premium Luxury (?:Itinerary|Proposal)", item, re.I):
            continue
        if item.startswith("& TRAVEL INFORMATION") or item.startswith("IMPORTANT NOTES"):
            continue
        out.append(item)
    return out


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
        f"State / Country: Meghalaya / India | Category: {category}",
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
        shop = shop.strip()
        if shop and not shop.startswith("IMPORTANT") and "TRAVEL INFORMATION" not in shop:
            highlights.append(shop)
    cleaned = []
    for h in highlights:
        h = re.sub(r"\s+", " ", h).strip()
        if h and "TRAVEL INFORMATION" not in h:
            cleaned.append(h)
    return cleaned[:14]


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
        f"{hotel['name']} ({hotel.get('location', 'Meghalaya')}) | {hotel['meal_plan']}"
    )
    extra = hotel.get("description_extra")
    if extra:
        desc = f"{desc} | {extra}"
    name = hotel["name"][:128]
    location = (hotel.get("location") or "Meghalaya")[:128]
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
    func = f"build_ml_{num}"
    duration = re.sub(r"\s+", " ", extract_duration(text))
    slug = meta["slug"]
    itin_slug = f"{slug}-itinerary"
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = parse_day_blocks(text)
    hotels = meta.get("hotels") or _jh.parse_hotel_options(text)
    included = _clean_items(meta.get("included") or parse_inclusions_exclusions(raw_text)[0])
    excluded = meta.get("excluded")
    if excluded is None:
        _, excluded = parse_inclusions_exclusions(raw_text)
    excluded = _clean_items(excluded)
    overview = extract_overview_sections(text)
    meta_with_serial = {**meta, "serial": serial}
    pkg_highlights = build_package_highlights(meta_with_serial, text)
    itin_highlights = build_itinerary_highlights(days, text)
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
        f"Premium {duration} Meghalaya package ({serial} / {tour_code}): "
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
    header = '''"""Builder functions for ML-001 through ML-010 Meghalaya domestic packages."""

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

MEGHALAYA_SLUG = "meghalaya"


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

    builder_names = [f"build_ml_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nMEGHALAYA_DOMESTIC_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
