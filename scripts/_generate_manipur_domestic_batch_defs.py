#!/usr/bin/env python3
"""Generate manipur_domestic_batch_defs.py from tmp_mn_pdfs text sources."""

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

PDF_DIR = _SCRIPTS.parent / "tmp_mn_pdfs"
OUT_PATH = _SCRIPTS / "manipur_domestic_batch_defs.py"
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


def _mn_hotel(
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


def extract_destinations_manipur(text: str) -> str:
    m = re.search(
        r"DESTINATIONS(?:\s*COVERED)?:\s*\n(.+?)(?:\nIDEAL FOR|\nBEST SEASON|\nSTARTING|\nTRAGUIN TOUR|\nVEHICLE|\nTOUR OVERVIEW|\nHOTEL|\nMEAL PLAN|\n[A-Z]{2,}-\d{3})",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        raw = re.sub(r"\s+", " ", m.group(1).strip())
        raw = raw.replace(",", " • ")
        return raw
    return extract_destinations(text)


def extract_vehicle_meals_manipur(text: str) -> str:
    for label in (
        "VEHICLE & MEAL PLAN:",
        "VEHICLE & MEALS:",
        "VEHICLE & PLAN:",
        "VEHICLE TYPE:",
        "VEHICLE / MEALS:",
        "VEHICLE:",
    ):
        idx = text.upper().find(label.upper())
        if idx == -1:
            continue
        lines: list[str] = []
        for ln in text[idx + len(label) :].splitlines():
            stripped = ln.strip()
            if not stripped:
                if lines:
                    break
                continue
            if re.match(
                r"^(TRAGUIN|TOUR OVERVIEW|DURATION|DESTINATIONS|IDEAL FOR|BEST SEASON|STARTING|TRAGUIN TOUR|DETAILED|DAY-WISE|DAY 0|ROUTE|MEAL PLAN|HOTEL|WELCOME)",
                stripped,
                re.I,
            ):
                break
            lines.append(stripped)
        if lines:
            return re.sub(r"\s+", " ", " ".join(lines))[:200]
    return extract_vehicle_meals(text)


PACKAGE_META: dict[str, dict] = {
    "MN-001": {
        "tour_code": "TRG-MAN-FAM-001",
        "slug": "mn-001-imphal-discovery-floating-lake-luxury-family-vacation",
        "title": "Imphal Discovery & Floating Lake Luxury Family Vacation",
        "destinations": "Imphal • Loktak Lake • Moirang • Andro • Sendra Island",
        "moods": ["Family", "Heritage", "Nature"],
        "hotels": [
            _mn_hotel(1, "Deluxe", imphal="Hotel Classic / Similar (Deluxe Room)", loktak="Sendra Park Resort (Standard Cottage)", nights_label="3N Imphal + 1N Loktak/Sendra", meal_plan="CP (Breakfast Only)"),
            _mn_hotel(2, "Premium", imphal="The Classic Grande / Equivalent (Executive)", loktak="Sendra Park by Classic (Premium Villa)", nights_label="3N Imphal + 1N Loktak/Sendra", meal_plan="MAP (Breakfast & Dinner)"),
            _mn_hotel(3, "Luxury", imphal="The Classic Grande (Suite Category)", loktak="Sendra Resort Villas (Lake View Front)", nights_label="3N Imphal + 1N Loktak/Sendra", room_type="Suite Category | Lake View Front", meal_plan="All Inclusive Managed"),
            _mn_hotel(4, "Ultra Luxury", imphal="Signature Royal Palace Suite Collections", loktak="VIP Custom Overwater Luxury Eco Domes", nights_label="3N Imphal + 1N Loktak/Sendra", room_type="Royal Palace Suite | Overwater Eco Dome", meal_plan="Bespoke Private Culinary Host", stars=5),
        ],
    },
    "MN-002": {
        "tour_code": "TRG-MAN-FAM-002",
        "slug": "mn-002-loktak-lake-special-cultural-heritage-family-tour",
        "title": "Loktak Lake Special & Cultural Heritage Family Tour",
        "destinations": "Imphal • Loktak Lake • Moirang • Sendra Island • Keibul Lamjao",
        "moods": ["Family", "Nature", "Culture"],
        "hotels": [
            _mn_hotel(1, "Deluxe", imphal="Classic Hotel / Hotel Imphal (Deluxe)", loktak="Sendra Park & Resort (Standard Room)", nights_label="2N Imphal + 2N Loktak Lake", meal_plan="MAP Plan (Breakfast + Dinner)"),
            _mn_hotel(2, "Premium", imphal="The Classic Grande (Executive Room)", loktak="Classic Resort Sendra (Lakeview Room)", nights_label="2N Imphal + 2N Loktak Lake", meal_plan="AP Plan (All Meals Included)"),
            _mn_hotel(3, "Luxury", imphal="The Classic Grande (Suite Haven)", loktak="Sendra Hills Luxury Lakeview Cottage", nights_label="2N Imphal + 2N Loktak Lake", room_type="Suite Haven | Lakeview Cottage", meal_plan="Full Board Culinary Hosting", stars=5),
            _mn_hotel(4, "Ultra Luxury", imphal="Imphal Heritage Palace / Elite VIP Villa", loktak="Sendra Presidential Waterfront Cottage", nights_label="2N Imphal + 2N Loktak Lake", room_type="Elite VIP Villa | Presidential Waterfront", meal_plan="Bespoke Royal Meitei Culinary Experiences", stars=5),
        ],
    },
    "MN-003": {
        "tour_code": "TRG-MAN-EXPLORER-003",
        "slug": "mn-003-manipur-explorer-luxury-expedition",
        "title": "Manipur Explorer Luxury Expedition",
        "destinations": "Imphal • Loktak Lake • Moirang • Khangkhui Caves • Ukhrul",
        "moods": ["Adventure", "Wildlife", "Luxury"],
        "hotels": [
            _mn_hotel(1, "Deluxe", imphal="Classic Hotel / Hotel Imphal", loktak="Sendra Park Resort (Standard)", ukhrul="Shalom Eco Lodge (Standard)", nights_label="2N Imphal + 1N Loktak + 2N Ukhrul", meal_plan="MAPAI (Breakfast + Dinner)"),
            _mn_hotel(2, "Premium", imphal="The Classic Grande (Executive)", loktak="Loktak Floating Cottages (Premium)", ukhrul="Shirui Eco Lodge (Premium Cabin)", nights_label="2N Imphal + 1N Loktak + 2N Ukhrul", meal_plan="APAI (All Meals Included)"),
            _mn_hotel(3, "Luxury", imphal="The Classic Grande (Suite Tier)", loktak="TRAGUIN Private Luxury Floating Villa", ukhrul="Ukhrul Heritage Retreat (Luxury Villa)", nights_label="2N Imphal + 1N Loktak + 2N Ukhrul", room_type="Suite Tier | Luxury Villa", meal_plan="All Inclusive Gourmet", stars=5),
            _mn_hotel(4, "Ultra Luxury", imphal="Radisson Blu Imphal / Elite Signature Suite", loktak="TRAGUIN Bespoke VIP Overwater Geodesic Dome", ukhrul="The Cloud Estate (Bespoke Private Chalet)", nights_label="2N Imphal + 1N Loktak + 2N Ukhrul", room_type="Elite Signature Suite | Private Chalet", meal_plan="Royal Custom Dining", stars=5),
        ],
    },
    "MN-004": {
        "tour_code": "TRG-MAN-LUX-004",
        "slug": "mn-004-bespoke-loktak-floating-paradise-royal-tribal-heritage",
        "title": "Bespoke Loktak Floating Paradise & Royal Tribal Heritage",
        "destinations": "Imphal • Loktak Lake • Moirang • Andro Cultural Outpost • Moreh Border",
        "moods": ["Luxury", "Heritage", "Honeymoon"],
        "hotels": [
            _mn_hotel(1, "Deluxe", imphal="The Classic Hotel, Imphal (Executive Room)", loktak="Sendra Park Resort by Classic (Standard Villa)", nights_label="4N Imphal + 1N Loktak Lake", meal_plan="MAPAI (Breakfast & Dinner)"),
            _mn_hotel(2, "Premium", imphal="Classic Grande, Imphal (Club Elite Room)", loktak="Sendra Park Heritage Resort (Deluxe Water-View)", nights_label="4N Imphal + 1N Loktak Lake", meal_plan="APAI (All Daily Meals Included)"),
            _mn_hotel(3, "Luxury", imphal="Radisson Choice / Classic Grande (Luxury Suite)", loktak="Loktak Floating Luxury Over-Water Cottages", nights_label="4N Imphal + 1N Loktak Lake", room_type="Luxury Suite | Over-Water Cottage", meal_plan="TRAGUIN Private Culinary Plan", stars=5),
            _mn_hotel(4, "Ultra Luxury", imphal="Royal Palace Suite Portfolio / Private Elite", loktak="TRAGUIN VIP Custom Floating Geodesic Eco-Dome", nights_label="4N Imphal + 1N Loktak Lake", room_type="Royal Palace Suite | Geodesic Eco-Dome", meal_plan="Bespoke Royal In-Dome Dining", stars=5),
        ],
    },
    "MN-005": {
        "tour_code": "TRG-MN-LEI-05",
        "slug": "mn-005-senior-citizen-leisure-imphal-loktak-khongjom",
        "title": "Senior Citizen Leisure — Imphal • Loktak Lake • Moirang • Khongjom",
        "destinations": "Imphal • Loktak Lake • Moirang • Khongjom",
        "moods": ["Leisure", "Family", "Heritage"],
        "hotels": [
            _mn_hotel(1, "Deluxe", imphal="Hotel Classic / Similar (Executive Room)", nights_label="5N Imphal", room_type="Executive Room", meal_plan="MAPAI (Breakfast & Dinner)"),
            _mn_hotel(2, "Premium", imphal="The Classic Grande / Similar (Superior Room)", nights_label="5N Imphal", room_type="Superior Room", meal_plan="MAPAI (Breakfast & Dinner)"),
            _mn_hotel(3, "Luxury", imphal="Classic Grande - A Member of Radisson Individuals (Deluxe Club Room)", nights_label="5N Imphal", room_type="Deluxe Club Room", meal_plan="MAPAI (Breakfast & Dinner)", stars=5),
            _mn_hotel(4, "Ultra Luxury", imphal="Classic Grande - Premium Suite Experience (Executive Luxury Suite)", nights_label="5N Imphal", room_type="Executive Luxury Suite", meal_plan="MAPAI (Breakfast & Dinner)", stars=5),
        ],
    },
    "MN-006": {
        "tour_code": "TRAGUIN-MAN-006",
        "slug": "mn-006-imphal-loktak-moirang-andro-moreh-family-holiday",
        "title": "Imphal • Loktak Lake • Moirang • Andro • Moreh Border Family Holiday",
        "destinations": "Imphal • Moirang • Loktak Lake • Andro • Moreh",
        "moods": ["Family", "Culture", "Nature"],
        "hotels": [
            _mn_hotel(1, "Deluxe", imphal="Hotel Classic / Similar", loktak_moirang="Sendra Park Resort (Deluxe Room)", nights_label="5N Imphal + 1N Loktak/Moirang", room_type="Executive Room", meal_plan="MAPAI"),
            _mn_hotel(2, "Premium", imphal="The Classic Grande / Similar", loktak_moirang="Sendra Park Resort (Cottage)", nights_label="5N Imphal + 1N Loktak/Moirang", room_type="Superior Room", meal_plan="MAPAI"),
            _mn_hotel(3, "Luxury", imphal="Classic Grande - Member of Radisson Individuals", loktak_moirang="Sendra Luxury Lake Resort (Suite)", nights_label="5N Imphal + 1N Loktak/Moirang", room_type="Deluxe Suite Room", meal_plan="MAPAI", stars=5),
            _mn_hotel(4, "Ultra Luxury", imphal="Elite Premium Royal Suites Selection", loktak_moirang="Premium Overwater Villa Tier Selection", nights_label="5N Imphal + 1N Loktak/Moirang", room_type="Ultra Premium Elite Package", meal_plan="Ultra Premium Elite Package", stars=5),
        ],
    },
    "MN-007": {
        "tour_code": "TG-MAN-EDU-007",
        "slug": "mn-007-manipur-educational-tour",
        "title": "Manipur Educational Tour — Imphal • Loktak Lake • Moirang • Khongjom",
        "destinations": "Imphal • Moirang • Loktak Lake • Khongjom • Moreh Border",
        "moods": ["Educational", "Culture", "Nature"],
        "hotels": [
            _mn_hotel(1, "Deluxe", imphal="Classic Hotel / Hotel Imphal", nights_label="4N Imphal", room_type="Executive Twin Bed / Triple Bed Options", meal_plan="Breakfast & Dinner (MAPAI)"),
            _mn_hotel(2, "Premium", imphal="The Classic Grande (A Member of Radisson Individuals)", nights_label="4N Imphal", room_type="Superior Deluxe Twin Rooms", meal_plan="All Meals Curated (APAI)"),
            _mn_hotel(3, "Luxury", imphal="Premium Heritage Palace / Elite Suites", nights_label="4N Imphal", room_type="Luxury Club Rooms", meal_plan="All Meals Curated + High Tea", stars=5),
            _mn_hotel(4, "Ultra Luxury", imphal="Exclusive Boutique Eco-Resorts / Royal Palace Wings", nights_label="4N Imphal", room_type="Signature Executive Suites", meal_plan="Gourmet Customized Institutional Catering", stars=5),
        ],
    },
    "MN-008": {
        "tour_code": "TRAGUIN-MN-008",
        "slug": "mn-008-imphal-heritage-tour",
        "title": "Imphal Heritage Tour",
        "destinations": "Imphal • Moirang • Loktak Lake • Andro",
        "moods": ["Family", "Heritage", "Culture"],
        "hotels": [
            _mn_hotel(1, "Deluxe", imphal="Hotel Imphal by The Classic (Heritage Wing)", nights_label="4N Imphal", room_type="Executive Deluxe Room", meal_plan="CP / MAP AI"),
            _mn_hotel(2, "Premium", imphal="The Classic Grand (Premium Business Address)", nights_label="4N Imphal", room_type="Grand Deluxe Room", meal_plan="MAP Plan"),
            _mn_hotel(3, "Luxury", imphal="Classic Grand / Premium Boutique Suites", nights_label="4N Imphal", room_type="Executive Suite Comfort", meal_plan="MAP Plan", stars=5),
            _mn_hotel(4, "Ultra Luxury", imphal="Handpicked Elite Corporate Suites / Classic Luxury", nights_label="4N Imphal", room_type="Presidential / Royal Suite", meal_plan="Custom Luxury Plan", stars=5),
        ],
    },
    "MN-009": {
        "tour_code": "TRAGUIN-MN-009-ROMANTIC",
        "slug": "mn-009-romantic-loktak-lake-escapade-imphal-luxury",
        "title": "Romantic Loktak Lake Escapade • Imphal Luxury",
        "destinations": "Imphal • Loktak Lake • Sendra Hills • Moirang",
        "moods": ["Honeymoon", "Romance", "Luxury"],
        "hotels": [
            _mn_hotel(1, "Deluxe", lakeside="Sendra Park Resort (Standard)", imphal="The Classic Hotel", nights_label="2N Lakeside + 2N Imphal", room_type="Standard | Classic Hotel", meal_plan="Welcome Drink & Cake"),
            _mn_hotel(2, "Premium", lakeside="Sendra Resort (Lake View Cottage)", imphal="Classic Grande (Superior)", nights_label="2N Lakeside + 2N Imphal", room_type="Lake View Cottage | Superior", meal_plan="Bed Decoration + Fruit Basket"),
            _mn_hotel(3, "Luxury", lakeside="Loktak Floating Luxury Cabins", imphal="Radisson Suite Properties", nights_label="2N Lakeside + 2N Imphal", room_type="Floating Luxury Cabin | Radisson Suite", meal_plan="Candlelight Dinner + Floral Decor", stars=5),
            _mn_hotel(4, "Ultra Luxury", lakeside="The Sangai Premium Floating Villa", imphal="The Sangai Luxury City Suites", nights_label="2N Lakeside + 2N Imphal", room_type="Premium Floating Villa | Luxury City Suite", meal_plan="Spa Voucher + Poolside Dinner", stars=5),
        ],
    },
    "MN-010": {
        "tour_code": "TRG-MAN-010",
        "slug": "mn-010-manipur-panorama-family-luxury-tour",
        "title": "Manipur Panorama Family Luxury Tour — Imphal • Loktak • Moreh • Ukhrul",
        "destinations": "Imphal • Loktak • Moirang • Moreh • Ukhrul",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _mn_hotel(1, "Deluxe", imphal="Classic Hotel / Similar", ukhrul="Shalom Lodge / Similar", nights_label="5N Imphal + 1N Ukhrul", room_type="Executive Room", meal_plan="MAPAI"),
            _mn_hotel(2, "Premium", imphal="The Classic Grande / Similar", ukhrul="The Hills Hotel / Similar", nights_label="5N Imphal + 1N Ukhrul", room_type="Deluxe Suite Room", meal_plan="MAPAI"),
            _mn_hotel(3, "Luxury", imphal="Classic Grande - Premium Wing", ukhrul="Luxury Eco Retreat Ukhrul", nights_label="5N Imphal + 1N Ukhrul", room_type="Club Luxury Room", meal_plan="MAPAI", stars=5),
            _mn_hotel(4, "Ultra Luxury", imphal="Hotel Imphal Radisson / Elite Villa", ukhrul="Bespoke Elite Highland Cabin", nights_label="5N Imphal + 1N Ukhrul", room_type="Presidential / Royal Suite", meal_plan="MAPAI", stars=5),
        ],
    },
}

BUILDER_ORDER = [f"MN-{i:03d}" for i in range(1, 11)]


def parse_day_blocks(text: str) -> list[dict]:
    start = re.search(
        r"(?:DETAILED DAY-WISE ITINERARY|YOUR BESPOKE DAY-WISE ITINERARY|DAY WISE DETAILED ITINERARY|"
        r"DAY WISE ITINERARY|DAY-WISE DETAILED ITINERARY|DAY-WISE ITINERARY|DAY-WISE CUSTOM(?: TRAVEL)? ITINERARY)",
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
        r"(?m)^(?:BOUTIQUE PREMIUM STAY|ACCOMMODATION OPTIONS|HANDPICKED (?:LUXURY )?(?:PREMIUM )?(?:ACCOMMODATION|HOTEL|STAYS)|"
        r"PREMIUM ACCOMMODATION|PREMIUM HOTEL SELECTION|HOTEL OPTIONS SECTION|HOTEL SELECTION OPTIONS|"
        r"LUXURY ACCOMMODATION OPTIONS|EXCLUSIVE PREMIUM HOTEL OPTIONS|EXCLUSIVE LUXURY HOTEL OPTIONS|"
        r"HANDPICKED PREMIUM ACCOMMODATION OPTIONS|HANDPICKED PREMIUM ACCOMMODATION|HANDPICKED ACCOMMODATION|"
        r"HANDPICKED PREMIUM HOTEL|PREMIUM HOTEL OPTIONS|PREMIUM HANDPICKED HOTEL TIERS|CURATED HOTEL ACCOMMODATIONS|"
        r"HANDPICKED PREMIUM ACCOMMODATIONS|PREMIUM ACCOMMODATION SELECTIONS|EXCLUSIVE HOTEL SELECTIONS|"
        r"HANDPICKED PREMIUM ACCOMMODATIONS|ACCOMMODATION OPTIONS)",
        section,
    )
    if end:
        section = section[: end.start()]
    section = _jh.FOOTER_RE.sub("", section)
    section = _jh.PAGE_RE.sub("", section)
    section = re.sub(
        r"TRAGUIN Premium (?:Family|Luxury|Travel) (?:Expeditions|Holidays|Experience)[^\n]*\n\d+\s*\n?",
        "",
        section,
        flags=re.IGNORECASE,
    )
    return _jh.parse_day_blocks(f"DETAILED DAY-WISE ITINERARY\n{section}")


def _clean_day_descriptions(days: list[dict]) -> list[dict]:
    stop_markers = (
        "HANDPICKED PREMIUM STAYS",
        "PACKAGE INCLUSIONS",
        "EXCLUSIVE PREMIUM HOTEL",
        "HOTEL SELECTION OPTIONS",
        "LUXURY ACCOMMODATION OPTIONS",
        "TRAGUIN Premium Family Expeditions",
        "TRAGUIN Premium Luxury Expeditions",
        "TRAGUIN Premium Travel Experience",
    )
    cleaned: list[dict] = []
    for day in days:
        desc = day["description"]
        for marker in stop_markers:
            idx = desc.find(marker)
            if idx != -1:
                desc = desc[:idx].strip()
        desc = re.sub(r"\s+", " ", desc).strip()
        cleaned.append({**day, "description": desc})
    return cleaned


def _clean_items(items: list[str]) -> list[str]:
    out = []
    for item in items:
        item = re.sub(r"\s+", " ", item).strip()
        if not item or len(item) < 8:
            continue
        if re.search(r"TRAGUIN Premium (?:Family|Luxury|Travel)", item, re.I):
            continue
        if item.startswith("& TRAVEL INFORMATION") or item.startswith("IMPORTANT NOTES"):
            continue
        out.append(item)
    return out


def build_package_highlights(meta: dict, text: str) -> list[str]:
    serial = meta["serial"]
    tour_code = meta["tour_code"]
    category = extract_category(text)
    destinations = meta.get("destinations") or extract_destinations_manipur(text)
    ideal_for = extract_ideal_for(text)
    best_season = extract_best_season(text)
    starting_price = extract_starting_price(text)
    vehicle_meals = extract_vehicle_meals_manipur(text)
    route = extract_route(text)
    if route and len(route) > 180:
        route = route[:177].rsplit(" ", 1)[0] + "..."
    highlights = [
        f"Serial code {serial} | TRAGUIN tour code {tour_code}",
        f"State / Country: Manipur / India | Category: {category}",
        f"Destinations: {destinations}",
        f"Ideal for: {ideal_for}",
        f"Best season: {best_season}",
        f"Starting price: {starting_price}",
        f"Vehicle / Meals: {vehicle_meals}",
    ]
    if route:
        highlights.append(f"Route: {route}")
    skip_prefixes = ("RECOMMENDATIONS", "SHOPPING", "IMPORTANT", "& POLICIES", "POLICIES")
    for sig in parse_signature_highlights(text)[:4]:
        sig = re.sub(r"\s+", " ", sig).strip()
        if sig and not sig.startswith(skip_prefixes):
            highlights.append(sig)
    for shop in parse_shopping_notes(text)[:2]:
        shop = re.sub(r"\s+", " ", shop).strip()
        if shop and not shop.startswith(skip_prefixes) and "TRAVEL INFORMATION" not in shop:
            if not shop.upper().startswith("LOCAL MARKETS"):
                highlights.append(shop)
    cleaned = []
    for h in highlights:
        h = re.sub(r"\s+", " ", h).strip()
        if h and "TRAVEL INFORMATION" not in h and not h.startswith(skip_prefixes):
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
        f"{hotel['name']} ({hotel.get('location', 'Manipur')}) | {hotel['meal_plan']}"
    )
    extra = hotel.get("description_extra")
    if extra:
        desc = f"{desc} | {extra}"
    name = hotel["name"][:128]
    location = (hotel.get("location") or "Manipur")[:128]
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
    func = f"build_mn_{num}"
    duration = re.sub(r"\s+", " ", extract_duration(text))
    slug = meta["slug"]
    itin_slug = f"{slug}-itinerary"
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = _clean_day_descriptions(parse_day_blocks(text))
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
    tagline = tagline.split("—")[0].strip() if "—" in tagline else tagline

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
    seo_title = f"{serial} | {title.split('•')[0].split('—')[0].strip()} | TRAGUIN"
    destinations = meta.get("destinations") or extract_destinations_manipur(text)
    seo_desc = (
        f"Premium {duration} Manipur package ({serial} / {tour_code}): "
        f"{destinations[:100]} with 4-tier handpicked accommodation."
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
    header = '''"""Builder functions for MN-001 through MN-010 Manipur domestic packages."""

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

MANIPUR_SLUG = "manipur"


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

    builder_names = [f"build_mn_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nMANIPUR_DOMESTIC_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
