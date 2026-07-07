#!/usr/bin/env python3
"""Generate kashmir_jk_001_010_domestic_batch_defs.py from tmp_jk_pdfs text sources."""

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

PDF_DIR = _SCRIPTS.parent / "tmp_jk_pdfs"
OUT_PATH = _SCRIPTS / "kashmir_jk_001_010_domestic_batch_defs.py"

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


def _jk_hotel(
    sort_order: int,
    category: str,
    *,
    srinagar: str = "",
    gulmarg: str = "",
    pahalgam: str = "",
    sonamarg: str = "",
    houseboat: str = "",
    trek: str = "",
    nights_label: str,
    room_type: str = "Deluxe Room",
    meal_plan: str = "MAPAI (Breakfast & Dinner)",
    stars: int | None = None,
) -> dict:
    cities: list[str] = []
    names: list[str] = []
    for label, value in (
        ("Srinagar", srinagar),
        ("Gulmarg", gulmarg),
        ("Pahalgam", pahalgam),
        ("Sonamarg", sonamarg),
        ("Dal Lake Houseboat", houseboat),
        ("Alpine Trek", trek),
    ):
        if value:
            cities.append(label)
            names.append(value)
    name = " | ".join(names)
    location = " | ".join(cities)
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
    "JK-001": {
        "tour_code": "TRG-KASH-001",
        "slug": "jk-001-kashmir-paradise-family",
        "title": "Kashmir Paradise — The Ultimate Family Luxury Escape",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _jk_hotel(1, "Deluxe", houseboat="Royal Houseboats / similar", pahalgam="Hotel Hilltop / similar", srinagar="Hotel Grand Mumtaz / similar", nights_label="1N Houseboat + 2N Pahalgam + 2N Srinagar", room_type="Deluxe Room"),
            _jk_hotel(2, "Premium", houseboat="Mascot Houseboats / similar", pahalgam="Hotel Heevan / Pine n Peak", srinagar="The Orchid Retreat / similar", nights_label="1N Houseboat + 2N Pahalgam + 2N Srinagar", room_type="Premium Room"),
            _jk_hotel(3, "Luxury", houseboat="Sukoon Luxury Houseboat", pahalgam="Welcomhotel by ITC Pine & Peak", srinagar="The Radisson Blu Srinagar", nights_label="1N Houseboat + 2N Pahalgam + 2N Srinagar", room_type="Luxury Suite", stars=5),
            _jk_hotel(4, "Ultra Luxury", houseboat="Signature Ultra Luxury Suite", pahalgam="The Grand Mumtaz Resorts VVIP", srinagar="The Taj Palace / The Lalit Grand Palace", nights_label="1N Houseboat + 2N Pahalgam + 2N Srinagar", room_type="Royal Suite", stars=5),
        ],
    },
    "JK-002": {
        "tour_code": "TRG-KASH-002",
        "slug": "jk-002-srinagar-gulmarg-premium-family",
        "title": "Srinagar • Gulmarg Premium Family Tour",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _jk_hotel(1, "Deluxe", srinagar="Hotel Rose Petal / similar", gulmarg="Hotel Green Heights / similar", houseboat="Deluxe Wooden Houseboat", nights_label="2N Srinagar + 1N Gulmarg + 1N Houseboat"),
            _jk_hotel(2, "Premium", srinagar="Fortune Resort Heevan / similar", gulmarg="The Vintage Gulmarg / similar", houseboat="Premium Group of Houseboats", nights_label="2N Srinagar + 1N Gulmarg + 1N Houseboat"),
            _jk_hotel(3, "Luxury", srinagar="Vivanta Dal View / Radisson Blu", gulmarg="The Khyber Himalayan Resort", houseboat="Luxury Royal Palace Houseboat", nights_label="2N Srinagar + 1N Gulmarg + 1N Houseboat", stars=5),
            _jk_hotel(4, "Ultra Luxury", srinagar="The Lalit Grand Palace (Suite)", gulmarg="The Khyber (Luxury Suite)", houseboat="Exclusive Ultra-Luxury Private Houseboat", nights_label="2N Srinagar + 1N Gulmarg + 1N Houseboat", stars=5),
        ],
    },
    "JK-003": {
        "tour_code": "TRG-KASH-003",
        "slug": "jk-003-srinagar-pahalgam-gulmarg-dal-lake",
        "title": "Srinagar • Pahalgam • Gulmarg • Dal Lake",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _jk_hotel(1, "Deluxe", houseboat="Royal Houseboat Group / similar", pahalgam="Hotel Hilltop / Resort Water View", srinagar="Hotel Heevan / Rose Petal / similar", nights_label="1N Houseboat + 2N Pahalgam + 2N Srinagar"),
            _jk_hotel(2, "Premium", houseboat="Meena Group Houseboats / similar", pahalgam="Pahalgam Hotel / Grand Mumtaz", srinagar="The Lemon Tree Hotel / similar", nights_label="1N Houseboat + 2N Pahalgam + 2N Srinagar"),
            _jk_hotel(3, "Luxury", houseboat="Sukoon Luxury Houseboat / Deluxe", pahalgam="Welcomhotel by ITC Pine & Peak", srinagar="The Radisson Blu Srinagar / Vivanta", nights_label="1N Houseboat + 2N Pahalgam + 2N Srinagar", stars=5),
            _jk_hotel(4, "Ultra Luxury", houseboat="Signature Super-Luxury Private Suite Houseboat", pahalgam="The Grand Mumtaz Royal Suite View", srinagar="The Lalit Grand Palace Srinagar", nights_label="1N Houseboat + 2N Pahalgam + 2N Srinagar", stars=5),
        ],
    },
    "JK-004": {
        "tour_code": "TRG-KASH-004",
        "slug": "jk-004-romantic-kashmir-honeymoon",
        "title": "Romantic Kashmir — An Ethereal Love Story in Paradise",
        "moods": ["Romantic", "Honeymoon", "Luxury"],
        "hotels": [
            _jk_hotel(1, "Deluxe", houseboat="Meena Group Houseboats / similar", srinagar="Hotel Grand Mumtaz", gulmarg="Hotel Royal Park / similar", pahalgam="Hotel Mountview / similar", nights_label="1N Houseboat + 1N Srinagar + 1N Gulmarg + 2N Pahalgam"),
            _jk_hotel(2, "Premium", houseboat="Wangnoo Luxury Houseboats / Fortune Heavan", srinagar="Hotel Hilltop / Grand Mumtaz", gulmarg="Hotel Hilltop / Grand Mumtaz", pahalgam="Pahalgam Hotel / Hotel Heavan", nights_label="1N Houseboat + 1N Srinagar + 1N Gulmarg + 2N Pahalgam"),
            _jk_hotel(3, "Luxury", houseboat="Mascot Luxury Houseboats / Vivanta by Taj Dal View", srinagar="Vivanta by Taj Dal View", gulmarg="The Vintage Gulmarg / The Rosewood", pahalgam="Welcomhotel by ITC Pine n Peak", nights_label="1N Houseboat + 1N Srinagar + 1N Gulmarg + 2N Pahalgam", stars=5),
            _jk_hotel(4, "Ultra Luxury", houseboat="Sukoon Luxury Houseboat / The Lalit Grand Palace", srinagar="The Lalit Grand Palace", gulmarg="The Khyber Himalayan Resort & Spa", pahalgam="The Grand Mumtaz Royal Suites / Private Villa", nights_label="1N Houseboat + 1N Srinagar + 1N Gulmarg + 2N Pahalgam", stars=5),
        ],
    },
    "JK-005": {
        "tour_code": "TRG-KASH-005",
        "slug": "jk-005-tulip-romance-kashmir-honeymoon",
        "title": "Tulip Romance — A Dreamy Luxury Kashmir Holiday",
        "moods": ["Romantic", "Honeymoon", "Luxury"],
        "hotels": [
            _jk_hotel(1, "Deluxe", houseboat="Royal Group Houseboats / similar", srinagar="Hotel Pine Spring / Orchard Retreat", nights_label="1N Houseboat + 3N Srinagar"),
            _jk_hotel(2, "Premium", houseboat="Kashmir Oasis Houseboat / similar", srinagar="Lemon Tree Hotel / Fortune Riviera", nights_label="1N Houseboat + 3N Srinagar"),
            _jk_hotel(3, "Luxury", houseboat="The Grand Palace Houseboat Group", srinagar="Radisson Collection / Vivanta Dal View", nights_label="1N Houseboat + 3N Srinagar", stars=5),
            _jk_hotel(4, "Ultra Luxury", houseboat="Sukoon Luxury Cruise Houseboat", srinagar="The Lalit Grand Palace (Heritage Suite)", nights_label="1N Houseboat + 3N Srinagar", stars=5),
        ],
    },
    "JK-006": {
        "tour_code": "TRG-KASH-006",
        "slug": "jk-006-luxury-kashmir-escape",
        "title": "Luxury Kashmir Escape — Paradise on Earth Reimagined",
        "moods": ["Luxury", "Family", "Honeymoon"],
        "hotels": [
            _jk_hotel(1, "Deluxe", srinagar="Fortune Resort Heevan / similar", gulmarg="Hotel Royal Park / similar", pahalgam="Hotel Heevan Pahalgam / similar", nights_label="3N Srinagar + 1N Gulmarg + 2N Pahalgam"),
            _jk_hotel(2, "Premium", srinagar="Radisson Collection Silk Route", gulmarg="Grand Mumtaz Resort / similar", pahalgam="Welcomhotel by ITC Pine N Peak", nights_label="3N Srinagar + 1N Gulmarg + 2N Pahalgam"),
            _jk_hotel(3, "Luxury", srinagar="Vivanta Dal View by Taj / Lalit", gulmarg="The Khyber Himalayan Resort", pahalgam="The Grand Mumtaz / Pahalgam Hotel", nights_label="3N Srinagar + 1N Gulmarg + 2N Pahalgam", stars=5),
            _jk_hotel(4, "Ultra Luxury", srinagar="The Lalit Grand Palace (Royal Suite)", gulmarg="The Khyber (Luxury Chalet)", pahalgam="Bespoke Private Luxury Villa Stay", nights_label="3N Srinagar + 1N Gulmarg + 2N Pahalgam", stars=5),
        ],
    },
    "JK-007": {
        "tour_code": "TRG-KASH-007",
        "slug": "jk-007-kashmir-great-lakes-trek",
        "title": "Kashmir Great Lakes Trek — The Ultimate Alpine Expedition",
        "moods": ["Adventure", "Nature", "Luxury"],
        "hotels": [
            _jk_hotel(1, "Deluxe", srinagar="Premium Deluxe Houseboat / Hotel Rose Petal", sonamarg="Hotel Village Walk / similar", trek="Standard Professional High-Altitude Camps", nights_label="2N Srinagar + 1N Sonamarg + 5N Trek", room_type="Deluxe Room | Standard Camp"),
            _jk_hotel(2, "Premium", srinagar="The Grand Kaisar / Lemon Tree Srinagar", sonamarg="Radisson Hotel Sonamarg", trek="Premium Dome Camps with Elevated Foam Beds", nights_label="2N Srinagar + 1N Sonamarg + 5N Trek", room_type="Premium Room | Dome Camp"),
            _jk_hotel(3, "Luxury", srinagar="Vivanta Dal View by Taj / Fortune Hevan", sonamarg="Hotel Glacier Heights Luxury Suite", trek="Luxury Camps with Cots, Pillow Sets & Heated Dining", nights_label="2N Srinagar + 1N Sonamarg + 5N Trek", room_type="Luxury Suite | Heated Camp", stars=5),
            _jk_hotel(4, "Ultra Luxury", srinagar="The Lalit Grand Palace (Royal Suite)", sonamarg="The Khyber style luxury villa transit", trek="VVIP Custom Camps with Private Toilet Tents & Personal Porter", nights_label="2N Srinagar + 1N Sonamarg + 5N Trek", room_type="Royal Suite | VVIP Camp", stars=5),
        ],
    },
    "JK-008": {
        "tour_code": "TRG-KSH-008",
        "slug": "jk-008-kashmir-ladies-escape",
        "title": "Kashmir Ladies Escape — Sisterhood Amidst Paradise",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _jk_hotel(1, "Deluxe", srinagar="Hotel Paradise / Fortune Heevan / similar", pahalgam="Hotel Heevan / Grand Mumtaz / similar", nights_label="3N Srinagar + 2N Pahalgam", room_type="Deluxe Room with Heating"),
            _jk_hotel(2, "Premium", srinagar="Radisson Srinagar / Lemon Tree / similar", pahalgam="Pine n Peak / Welcomhotel / similar", nights_label="3N Srinagar + 2N Pahalgam", room_type="Premium Balcony View Room"),
            _jk_hotel(3, "Luxury", srinagar="The Grand Lalit / Vivanta Dal View by Taj", pahalgam="The Kolahoi Green Resort / similar suites", nights_label="3N Srinagar + 2N Pahalgam", room_type="Luxury Valley View Suite", stars=5),
            _jk_hotel(4, "Ultra Luxury", srinagar="The Grand Lalit (Palace Heritage Suite)", pahalgam="The Khyber Resort / Private Luxury Villas", nights_label="3N Srinagar + 2N Pahalgam", room_type="VVIP Heritage Suite", stars=5),
        ],
    },
    "JK-009": {
        "tour_code": "TRG-KASH-009",
        "slug": "jk-009-leisure-kashmir-serenade",
        "title": "Leisure Kashmir — Serenade of Paradise",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _jk_hotel(1, "Deluxe", srinagar="Hotel Grand Mumtaz / Deluxe Houseboat", gulmarg="Hotel Royal Park / similar", pahalgam="Grand Mumtaz Resort / similar", nights_label="2N Srinagar + 1N Gulmarg + 2N Pahalgam"),
            _jk_hotel(2, "Premium", srinagar="Fortune Resort Heevan / similar", gulmarg="Hotel Vintage / similar", pahalgam="Heevan Resort / Hotel Pine N Peak", nights_label="2N Srinagar + 1N Gulmarg + 2N Pahalgam"),
            _jk_hotel(3, "Luxury", srinagar="The Orchid Retreat / Vivanta Dal View", gulmarg="The Khyber Himalayan Resort (Luxury Room)", pahalgam="Welcomhotel Pine N Peak (Superior Suite)", nights_label="2N Srinagar + 1N Gulmarg + 2N Pahalgam", stars=5),
            _jk_hotel(4, "Ultra Luxury", srinagar="The Lalit Grand Palace (Heritage Palace Suite)", gulmarg="The Khyber Himalayan Resort (Presidential)", pahalgam="The Grand Mumtaz Resorts Premium Chalet", nights_label="2N Srinagar + 1N Gulmarg + 2N Pahalgam", stars=5),
        ],
    },
    "JK-010": {
        "tour_code": "TRG-KASH-010",
        "slug": "jk-010-kashmir-complete",
        "title": "Kashmir Complete — Paradise on Earth Rediscovered",
        "moods": ["Family", "Luxury", "Nature"],
        "hotels": [
            _jk_hotel(1, "Deluxe", srinagar="Hotel Royal Milestone / Deluxe Houseboat", pahalgam="Hotel Foothills / similar", gulmarg="Hotel Pine Spring / similar", nights_label="3N Srinagar + 2N Pahalgam + 2N Gulmarg"),
            _jk_hotel(2, "Premium", srinagar="Fortune Resort Heevan / Premium Houseboat", pahalgam="Hotel Heevan / Pine N Peak", gulmarg="The Vintage Gulmarg / similar", nights_label="3N Srinagar + 2N Pahalgam + 2N Gulmarg"),
            _jk_hotel(3, "Luxury", srinagar="Vivanta Dal View Srinagar / The Lalit Grand", pahalgam="Welcomhotel Pine N Peak (Grand Suite)", gulmarg="The Khyber Himalayan Resort & Spa", nights_label="3N Srinagar + 2N Pahalgam + 2N Gulmarg", stars=5),
            _jk_hotel(4, "Ultra Luxury", srinagar="The Lalit Grand Palace (Royal Suite Stay)", pahalgam="Pahalgam Hotel (VVIP Premium Bungalow)", gulmarg="The Khyber Resort (Luxury Private Chalet)", nights_label="3N Srinagar + 2N Pahalgam + 2N Gulmarg", stars=5),
        ],
    },
}

BUILDER_ORDER = [f"JK-{i:03d}" for i in range(1, 11)]


def parse_day_blocks(text: str) -> list[dict]:
    start = re.search(
        r"(?:DETAILED DAY-WISE ITINERARY|DAY-WISE IMMERSIVE ITINERARY|DAY WISE ITINERARY|DAY-WISE CUSTOM (?:TRAVEL )?ITINERARY|DAY-WISE (?:DETAILED )?ITINERARY|THE MASTER ITINERARY|DAY-WISE ITINERARY)",
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
        r"(?m)^(?:ACCOMMODATION & CAMP TIERS|HANDPICKED (?:LUXURY )?(?:PREMIUM )?(?:MICE )?(?:CORPORATE )?(?:ACCOMMODATION|HOTEL)|"
        r"PREMIUM ACCOMMODATION|HANDPICKED PREMIUM ACCOMMODATION|HANDPICKED LUXURY ACCOMMODATION|"
        r"HANDPICKED ACCOMMODATION|HANDPICKED PREMIUM HOTEL|EXCLUSIVE HANDPICKED HOTEL|"
        r"PREMIUM HOTEL OPTIONS|CURATED HOTEL ACCOMMODATIONS|HOTEL OPTIONS SECTION)",
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
        f"State / Country: Jammu & Kashmir / India | Category: {category}",
        f"Destinations: {destinations}",
        f"Ideal for: {ideal_for}",
        f"Best season: {best_season}",
        f"Starting price: {starting_price}",
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
    for day in days[:10]:
        short = day["title"].split("|")[0].strip() if "|" in day["title"] else day["title"]
        out.append(f"Day {day['day_number']:02d}: {short}")
    for s in sig[:3]:
        if s not in out:
            out.append(s)
    return out[:10]


def emit_hotel(hotel: dict, duration: str) -> str:
    nights = hotel.get("nights_label") or _infer_nights_from_duration(duration)
    desc = hotel.get("description") or (
        f"OPTION {hotel['sort_order']:02d} – {hotel['category'].upper()}: "
        f"{hotel['name']} ({hotel.get('location', 'Kashmir')}) | {hotel['meal_plan']}"
    )
    name = hotel["name"][:128]
    location = (hotel.get("location") or "Kashmir")[:128]
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
    func = f"build_jk_{num}"
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
        f"Premium {duration} Kashmir package ({serial} / {tour_code}): "
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
    header = '''"""Builder functions for JK-001 through JK-010 Kashmir domestic packages."""

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

KASHMIR_SLUG = "kashmir"


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

    builder_names = [f"build_jk_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nKASHMIR_JK_001_010_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
