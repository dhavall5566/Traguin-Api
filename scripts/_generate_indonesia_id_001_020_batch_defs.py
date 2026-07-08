#!/usr/bin/env python3
"""Generate indonesia_id_001_020_batch_defs.py from tmp_id_pdfs text sources."""

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

PDF_DIR = _SCRIPTS.parent / "tmp_id_pdfs"
OUT_PATH = _SCRIPTS / "indonesia_id_001_020_batch_defs.py"
PRICE_NOTE = "On Request (Premium Customised)"
BUILDER_ORDER = ["ID-001", "ID-002"] + [f"ID-{i:03d}" for i in range(5, 21)]

TITLE_MAP = {
    "ID-001": "Premium Bali Honeymoon",
    "ID-002": "Bali Ubud Love Escape",
    "ID-005": "Premium Bali Family Tour",
    "ID-006": "Bali Girls Escape",
    "ID-007": "Luxury Bali Retreat",
    "ID-008": "Luxury Bali Villa Retreat",
    "ID-009": "Senior Citizen Relax Bali Escape",
    "ID-010": "Premium Bali Adventure Tour",
    "ID-011": "Best Bali Beaches & Coastal Escape",
    "ID-012": "Bali Romantic Tour Package",
    "ID-013": "Bali Family Tour Package",
    "ID-014": "Luxury Yoga & Wellness Bali Retreat",
    "ID-015": "Ultimate Bali Luxury Escapes",
    "ID-016": "Bali Lombok Ultimate Family Vacation",
    "ID-017": "Luxury Couple Bali Package",
    "ID-018": "Bali Fixed Departure Group Package",
    "ID-019": "Ladies Bali Retreat",
    "ID-020": "Grand Bali Premium Tour",
}

SLUG_MAP = {
    "ID-001": "id-001-premium-bali-honeymoon",
    "ID-002": "id-002-bali-ubud-love-escape",
    "ID-005": "id-005-premium-bali-family-tour",
    "ID-006": "id-006-bali-girls-escape",
    "ID-007": "id-007-luxury-bali-retreat",
}

ITIN_SLUG_MAP = {
    "ID-001": "id-001-premium-bali-honeymoon-itinerary",
    "ID-002": "id-002-bali-ubud-love-escape-itinerary",
    "ID-005": "id-005-premium-bali-itinerary",
    "ID-006": "id-006-bali-girls-escape-itinerary",
    "ID-007": "id-007-luxury-bali-retreat-itinerary",
}

clean_raw = _jh.clean_raw
py_str = _jh.py_str
extract_duration = _jh.extract_duration
extract_category = _jh.extract_category
extract_ideal_for = _jh.extract_ideal_for
extract_best_season = _jh.extract_best_season
extract_starting_price = _jh.extract_starting_price
extract_overview_sections = _jh.extract_overview_sections
parse_inclusions_exclusions = _jh.parse_inclusions_exclusions
parse_signature_highlights = _jh.parse_signature_highlights
parse_shopping_notes = _jh.parse_shopping_notes
parse_hotel_options = _jh.parse_hotel_options
build_itinerary_highlights = _jh.build_itinerary_highlights
_compact_nights_label = _jh._compact_nights_label


_ID_FOOTER_LINE = re.compile(
    r"TRAGUIN (?:Premium Luxury Itinerary|Premium Holidays|Luxury Holidays|Luxury Proposals?|Luxury Proposal|Family Vacations|Honeymoon Experts)"
    r"(?: • ID-\d{3})?(?: • www\.traguin\.in)?(?: Page \d+ of \d+|\s+\d+)?(?:\s*—\s*[^\n]+)?\s*\d*",
    re.IGNORECASE,
)
_ID_FOOTER_FRAGMENT = re.compile(
    r"(?:TRAGUIN )?(?:Premium )?(?:Luxury )?(?:Holidays|Itinerary|Holiday Proposals?|Family Vacations|Honeymoon Experts)"
    r"(?: • ID-\d{3})?(?: • www\.traguin\.in)?[^\n]*?(?=DAY\s*\d+)",
    re.IGNORECASE,
)


def _normalize_day_headers(text: str) -> str:
    text = re.sub(r"(?:www\.)?traguin\.in\s*", "\n", text, flags=re.I)
    text = re.sub(r"(?<=[^\n])(DAY\s*\d+\s*[|–\-])", r"\n\1", text, flags=re.I)
    text = re.sub(r"^\s+(DAY\s*\d+)", r"\1", text, flags=re.MULTILINE)
    return text


def clean_id_raw(raw: str) -> str:
    raw = _ID_FOOTER_LINE.sub("\n", raw)
    text = clean_raw(raw)
    text = re.sub(r"TRAGUIN TOUR\s*\n\s*CODE:", "TRAGUIN TOUR CODE:", text, flags=re.I)
    text = re.sub(r"TRAGUIN CODE:\s*", "TRAGUIN TOUR CODE: ", text, flags=re.I)
    text = re.sub(r"DESTINATIONS\s*\n\s*COVERED:", "DESTINATIONS COVERED:", text, flags=re.I)
    text = re.sub(r"DESTINATIONS\s*\n\s*COVERED\s+", "DESTINATIONS COVERED: ", text, flags=re.I)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = _ID_FOOTER_LINE.sub("\n", text)
    text = _ID_FOOTER_FRAGMENT.sub("\n", text)
    text = _normalize_day_headers(text)
    text = re.sub(r"(DAY\s*\d+\s*\|\s*[^\n]+)\n\s*[—–-]\s*", r"\1 | ", text, flags=re.MULTILINE)
    return text


def extract_destinations_id(text: str) -> str:
    lines = text.splitlines()
    collecting = False
    parts: list[str] = []
    for ln in lines:
        if re.match(r"DESTINATIONS(?:\s*COVERED)?:\s*$", ln.strip(), re.I):
            collecting = True
            continue
        if collecting:
            stripped = ln.strip()
            if not stripped:
                if parts:
                    break
                continue
            if re.match(
                r"^(IDEAL FOR|BEST SEASON|STARTING PRICE|TRAGUIN TOUR|VEHICLE|VEHICLE TYPE|MEAL PLAN|TOUR OVERVIEW|DURATION|CATEGORY|TRAVEL MONTH|Create |Embark |Step |Welcome to):",
                stripped,
                re.I,
            ):
                break
            parts.append(stripped)
    if parts:
        raw = re.sub(r"\s+", " ", " ".join(parts))
        return raw.replace(",", " • ")
    m = re.search(r"DESTINATIONS(?:\s*COVERED)?:\s*([^\n]+)", text, re.I)
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    m = re.search(r"Destinations Covered:\s*([^\n|]+)", text, re.I)
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    tagline = re.search(r"^(.{8,120}•.{4,120})$", text, re.MULTILINE)
    if tagline:
        return re.sub(r"\s+", " ", tagline.group(1).strip())
    return "Bali, Indonesia"


def extract_tour_code(text: str) -> str:
    flat = re.sub(r"\s+", " ", text)
    for pat in (
        r"TRAGUIN TOUR CODE:\s*(TRAGUIN-[A-Z0-9\-]+)",
        r"TRAGUIN TOUR CODE:\s*(TRG-[A-Z0-9\-]+)",
        r"TRAGUIN CODE:\s*(TRAGUIN-[A-Z0-9\-]+)",
        r"(TRAGUIN-BALI-[A-Z0-9\-]+)",
    ):
        m = re.search(pat, flat, re.I)
        if m:
            return m.group(1).strip()
    m = re.search(r"Serial Code:\s*ID-\d{3}", flat, re.I)
    if m:
        return f"TRAGUIN-BALI-{m.group(0).split('-')[-1]}"
    return "TRAGUIN-BALI-000"


def extract_title_id(text: str, serial: str = "") -> str:
    if serial in TITLE_MAP:
        return TITLE_MAP[serial]
    normalized = re.sub(r"TRAGUIN\s*\n\s*PREMIUM\s+", "TRAGUIN PREMIUM ", text, flags=re.I)
    normalized = re.sub(r"TRAGUIN\s*\n\s*(BEST|GRAND|LUXURY)\s+", r"TRAGUIN \1 ", normalized, flags=re.I)
    header = re.search(
        r"TRAGUIN (?:PREMIUM|LUXURY|ULTIMATE|GRAND|BEST)\s+(.+?)(?:\n\n|\n\d+\s+N|\nSERIAL|\nSTATE|\nCreate |\nEmbark |\nStep |\nWelcome to|\nTOUR OVERVIEW|ITINERARY SUMMARY|ITINERARY CODE)",
        normalized,
        re.DOTALL | re.IGNORECASE,
    )
    if header:
        title = re.sub(r"\s+", " ", header.group(1).strip())
        title = re.sub(r"\s+\d{2}\s+Nights\s*/\s*\d{2}\s+Days.*$", "", title, flags=re.I).strip()
        title = re.sub(r"\s*•\s*.*$", "", title).strip()
        if len(title) > 8:
            return title
    short = re.search(
        r"^(?:TRAGUIN PREMIUM\s+)?([A-Z][A-Z\s&\-]+(?:HONEYMOON|TOUR|ESCAPE|PACKAGE|RETREAT|ADVENTURE)[A-Z\s&\-]*)\s*$",
        text,
        re.MULTILINE | re.I,
    )
    if short:
        return re.sub(r"\s+", " ", short.group(1).strip()).title()
    tagline = re.search(r"^(.{12,120}•.{8,120})$", text, re.MULTILINE)
    if tagline:
        return re.sub(r"\s+", " ", tagline.group(1).strip())
    return "Bali Premium Luxury Tour"


def extract_vehicle_meals_id(text: str) -> str:
    flat = re.sub(r"\s+", " ", text)
    vehicle = ""
    meals = ""
    m = re.search(r"VEHICLE TYPE:\s*(.+?)(?:MEAL PLAN:|TOUR OVERVIEW|Create |Embark |$)", flat, re.I)
    if m:
        vehicle = m.group(1).strip()
    m = re.search(r"MEAL PLAN:\s*(.+?)(?:Create |Embark |Step |Welcome|TOUR OVERVIEW|$)", flat, re.I)
    if m:
        meals = m.group(1).strip()
    if vehicle and meals:
        return f"{vehicle} / {meals}"[:200]
    for label in (
        "VEHICLE / MEALS:",
        "VEHICLE TYPE:",
        "MEAL PLAN:",
        "VEHICLE:",
    ):
        m = re.search(rf"{re.escape(label)}\s*(.+?)(?:TRAGUIN|TOUR OVERVIEW|Create |Embark )", flat, re.I)
        if m:
            return m.group(1).strip()[:200]
    return "Private Luxury MPV / Buffet Breakfast & Curated Dinners"


def make_slug(serial: str, title: str) -> str:
    if serial in SLUG_MAP:
        return SLUG_MAP[serial]
    num = serial.split("-")[1]
    base = title.lower()
    base = base.replace("•", " ").replace("—", " ").replace("/", " ")
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return f"id-{num}-{base}"[:118].rstrip("-")


def infer_moods(text: str, serial: str = "") -> list[str]:
    blob = f"{extract_ideal_for(text)} {extract_category_id(text)} {extract_title_id(text, serial)}".lower()
    candidates = [
        ("Family", ("family", "group", "multi-generational")),
        ("Luxury", ("luxury", "premium", "bespoke", "ultra")),
        ("Honeymoon", ("honeymoon", "romantic", "couple", "love")),
        ("Culture", ("culture", "heritage", "temple", "ubud", "kecak")),
        ("Beach", ("beach", "seminyak", "nusa", "penida", "coastal")),
        ("Adventure", ("adventure", "rafting", "swing", "volcano", "kintamani")),
        ("Nature", ("nature", "rice terrace", "waterfall", "jungle")),
        ("Leisure", ("leisure", "senior", "relax", "retreat", "spa")),
    ]
    moods: list[str] = []
    for mood, keys in candidates:
        if any(k in blob for k in keys):
            moods.append(mood)
    if not moods:
        moods = ["Family", "Luxury", "Nature"]
    return moods[:3]


def parse_day_blocks_id(text: str) -> list[dict]:
    start = re.search(
        r"(?:THE DEFINITIVE DAY-WISE ITINERARY|YOUR BESPOKE DAY-WISE ITINERARY|DETAILED DAY-WISE ITINERARY|"
        r"DAY-BY-DAY CURATED ITINERARY|DAY-WISE ITINERARY|DAY WISE ITINERARY)",
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
        r"(?m)^(?:HANDPICKED (?:LUXURY )?(?:PREMIUM )?(?:ACCOMMODATION|HOTEL|RESORT|VILLA)|"
        r"CURATED HOTEL|PREMIUM ACCOMMODATION|HOTEL OPTIONS|HOTEL SELECTION|ACCOMMODATION OPTIONS|"
        r"HANDPICKED PREMIUM HOTEL|PREMIUM HOTEL OPTIONS|"
        r"CORPORATE ACCOMMODATION OPTIONS|PACKAGE INCLUSIONS)",
        section,
    )
    if end:
        section = section[: end.start()]
    section = _jh.FOOTER_RE.sub("", section)
    section = _jh.PAGE_RE.sub("", section)
    section = re.sub(
        r"TRAGUIN Premium Luxury Itinerary[^\n]*\n\d+\s*\n?",
        "",
        section,
        flags=re.IGNORECASE,
    )
    return _jh.parse_day_blocks(f"DETAILED DAY-WISE ITINERARY\n{section}")


def _clean_day_descriptions(days: list[dict]) -> list[dict]:
    stop_markers = (
        "HANDPICKED PREMIUM",
        "PACKAGE INCLUSIONS",
        "HOTEL OPTIONS",
        "ACCOMMODATION OPTIONS",
        "TRAGUIN Premium Luxury Itinerary",
    )
    cleaned: list[dict] = []
    for day in days:
        desc = day["description"]
        for marker in stop_markers:
            idx = desc.find(marker)
            if idx != -1:
                desc = desc[:idx].strip()
        cleaned.append({**day, "description": re.sub(r"\s+", " ", desc).strip()})
    return cleaned


def _clean_items(items: list[str]) -> list[str]:
    out: list[str] = []
    for item in items:
        item = re.sub(r"\s+", " ", item).strip()
        if not item or len(item) < 8:
            continue
        if "TRAGUIN Premium Luxury Itinerary" in item:
            continue
        if item.startswith("IMPORTANT NOTES"):
            continue
        out.append(item)
    return out


def extract_category_id(text: str) -> str:
    m = re.search(
        r"CATEGORY:\s*(.+?)(?:\nDURATION|\nDESTINATIONS|\nIDEAL|\nBEST|\nSTARTING|\nTRAGUIN)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return extract_category(text)


def _parse_exclusion_markers(section: str) -> list[str]:
    items: list[str] = []
    current: list[str] = []
    for line in section.splitlines():
        line = line.strip()
        if not line:
            continue
        if line == "✘":
            if current:
                items.append(re.sub(r"\s+", " ", " ".join(current)).strip())
            current = []
            continue
        if line.startswith("✘"):
            if current:
                items.append(re.sub(r"\s+", " ", " ".join(current)).strip())
            current = [re.sub(r"^✘\s*", "", line).strip()]
            continue
        if current:
            current.append(line)
    if current:
        items.append(re.sub(r"\s+", " ", " ".join(current)).strip())
    return [item for item in items if item and len(item) > 5]


def _default_id_inclusions() -> tuple[list[str], list[str]]:
    return (
        [
            "Premium handpicked accommodation across Bali",
            "Private luxury airport transfers and dedicated chauffeur-driven MPV",
            "TRAGUIN 24/7 dedicated on-ground concierge support",
        ],
        [
            "International airfare and Indonesia visa on arrival fees",
            "Personal expenses, laundry, room service, and mini-bar charges",
            "Optional sightseeing excursions not specified in the itinerary",
            "Tipping, porterage fees, and travel insurance",
        ],
    )


def parse_short_inclusions(text: str) -> tuple[list[str], list[str]]:
    block = re.search(r"PACKAGE INCLUSIONS\s*(.+?)(?:TRAGUIN|Creating Memories|\Z)", text, re.DOTALL | re.I)
    included: list[str] = []
    if block:
        for ln in block.group(1).splitlines():
            ln = ln.strip()
            if ln.startswith("✔"):
                item = re.sub(r"^✔\s*", "", ln).strip()
                if item and len(item) > 5:
                    included.append(item)
    if included:
        _, excluded = _default_id_inclusions()
        return included, excluded
    return _default_id_inclusions()


def parse_id_inclusions_exclusions(text: str) -> tuple[list[str], list[str]]:
    cleaned = _jh.PAGE_RE.sub(" ", text)
    cleaned = re.sub(r"TRAGUIN Luxury Holidays • www\.traguin\.in Page \d+ of \d+", " ", cleaned, flags=re.I)
    included, excluded = parse_inclusions_exclusions(cleaned)
    inline_inc: list[str] = []
    inline_exc: list[str] = []
    for m in re.finditer(r"([^✔✘\n]{12,}?)✔", cleaned):
        item = re.sub(r"\s+", " ", m.group(1)).strip(" .")
        item = re.sub(r"^(Accommodation|Meals|Transfers|Sightseeing|Welcome Amenities|TRAGUIN Support):\s*", r"\1: ", item, flags=re.I)
        if item and len(item) > 12 and "PACKAGE INCLUSIONS" not in item:
            inline_inc.append(item)
    for m in re.finditer(r"([^✔✘\n]{12,}?)✘", cleaned):
        item = re.sub(r"\s+", " ", m.group(1)).strip(" .")
        if item and len(item) > 12 and "PACKAGE EXCLUSIONS" not in item:
            inline_exc.append(item)
    block = re.search(
        r"PACKAGE INCLUSIONS(?:\s*&\s*EXCLUSIONS)?\s*(.+?)(?:SPECIAL TRAGUIN|SHOPPING|IMPORTANT|Creating Memories|\Z)",
        cleaned,
        re.DOTALL | re.I,
    )
    if block:
        chunk = block.group(1)
        for side in re.split(r"✘\s*PACKAGE EXCLUSIONS", chunk, flags=re.I):
            for m in re.finditer(r"([^✔✘\n]{12,}?)✔", side):
                item = re.sub(r"\s+", " ", m.group(1)).strip(" .")
                if item and len(item) > 12:
                    inline_inc.append(item)
            for m in re.finditer(r"([^✔✘\n]{12,}?)✘", side):
                item = re.sub(r"\s+", " ", m.group(1)).strip(" .")
                if item and len(item) > 12:
                    inline_exc.append(item)
    if len(inline_inc) >= len(included):
        included = inline_inc
    if len(inline_exc) >= len(excluded):
        excluded = inline_exc
    included = [
        re.sub(r"^✔\s*", "", re.sub(r"\s+", " ", item).strip())
        for item in included
        if item and "TRAGUIN Luxury Holidays" not in item and len(item) > 10
    ]
    expanded_exc: list[str] = []
    for item in excluded:
        for part in re.split(r"✘\s*", item):
            part = re.sub(r"\s+", " ", part).strip()
            if part and len(part) > 8:
                expanded_exc.append(part)
    if expanded_exc:
        excluded = expanded_exc
    if not included and not excluded:
        return _default_id_inclusions()
    if not included:
        included = _default_id_inclusions()[0]
    if not excluded:
        excluded = _default_id_inclusions()[1]
    return included, excluded


def parse_id_hotel_options(text: str) -> list[dict]:
    """Parse Bali PDF hotel option blocks."""
    section_m = re.search(
        r"(?:HANDPICKED|CURATED)[^\n]*(?:HOTEL|ACCOMMODATION|RESORT|VILLA|STAYS)[^\n]*\s*(.+?)(?:\"Creating Memories|PACKAGE INCLUSIONS|PREMIUM TRAVEL|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_m:
        section_m = re.search(
            r"HANDPICKED PREMIUM (?:FAMILY )?ACCOMMODATIONS\s*(.+?)(?:\"Creating Memories|PACKAGE INCLUSIONS|PREMIUM TRAVEL|\Z)",
            text,
            re.DOTALL | re.IGNORECASE,
        )
    if not section_m:
        return parse_hotel_options(text)
    section = section_m.group(1)
    section = re.sub(
        r"(Option\s*0?(\d+)\s*[–\-]?\s*(Deluxe|Premium|Luxury|Ultra\s*Luxury))(?=[A-Z])",
        r"\1\n",
        section,
        flags=re.I,
    )
    options: list[dict] = []
    nights = _compact_nights_label(_jh._infer_nights(text))
    pattern = re.compile(
        r"Option\s*0?(\d+)\s*[–\-]?\s*(Deluxe|Premium|Luxury|Ultra\s*Luxury)\s*(.+?)"
        r"(?=Option\s*0?\d+\s*[–\-]?|OPTION\s*0?\d+|Category |\Z)",
        re.DOTALL | re.IGNORECASE,
    )
    for m in pattern.finditer(section):
        num = int(m.group(1))
        category = re.sub(r"\s+", " ", m.group(2).strip()).title()
        if category.upper().startswith("ULTRA"):
            category = "Ultra Luxury"
        name = re.sub(r"\s+", " ", m.group(3).strip())
        name = re.sub(r"Category .*", "", name, flags=re.I).strip()
        name = re.sub(r"Room:.*", "", name, flags=re.I).strip()
        if not name or len(name) < 4:
            continue
        loc = "Bali"
        if name.count(" ") > 4 or "/" in name:
            loc = "Multi-city Bali"
        options.append(
            {
                "sort_order": num,
                "category": category,
                "name": name[:220],
                "location": loc,
                "nights_label": nights,
                "room_type": "Deluxe Room",
                "meal_plan": "Buffet Breakfast (CP)",
                "stars": 5 if "ultra" in category.lower() else 4,
                "description": f"Option {num:02d}: {category} — {name[:120]}",
            }
        )
    if options:
        return sorted(options, key=lambda x: x["sort_order"])[:4]
    return parse_hotel_options(text)


def build_meta(serial: str, text: str, raw: str) -> dict:
    title = extract_title_id(text, serial)
    tour_code = extract_tour_code(clean_id_raw(raw))
    destinations = extract_destinations_id(text)
    hotels = parse_id_hotel_options(text)
    if len(hotels) < 4:
        alt = parse_hotel_options(text)
        if len(alt) > len(hotels):
            hotels = alt
    if not hotels:
        nights = _jh._infer_nights(text)
        hotels = [
            {
                "sort_order": i,
                "category": cat,
                "name": f"TRAGUIN Handpicked {cat} Property",
                "location": destinations.split("•")[0].strip() or "Bali",
                "nights_label": nights,
                "room_type": "Deluxe Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 5 if "ultra" in cat.lower() else 4,
                "description": f"OPTION {i:02d} – {cat.upper()}: TRAGUIN Handpicked {cat} Property",
            }
            for i, cat in enumerate(["Deluxe", "Premium", "Luxury", "Ultra Luxury"], 1)
        ]
    primary_loc = destinations.split("•")[0].strip() or "Bali"
    for hotel in hotels:
        if hotel.get("location") in ("Jharkhand", "", "Haryana", "Multi-city Jharkhand", "Thailand"):
            hotel["location"] = primary_loc
        hotel["nights_label"] = _compact_nights_label(hotel.get("nights_label") or _jh._infer_nights(text))
    if serial in {"ID-001", "ID-002"}:
        included, excluded = parse_short_inclusions(text)
    else:
        included, excluded = parse_id_inclusions_exclusions(raw)
    return {
        "serial": serial,
        "tour_code": tour_code,
        "slug": make_slug(serial, title),
        "title": title,
        "destinations": destinations,
        "moods": infer_moods(text, serial),
        "hotels": hotels,
        "included": included,
        "excluded": excluded,
    }


def build_package_highlights(meta: dict, text: str) -> list[str]:
    serial = meta["serial"]
    tour_code = meta["tour_code"]
    category = extract_category_id(text)
    destinations = meta.get("destinations") or extract_destinations_id(text)
    highlights = [
        f"Serial code {serial} | TRAGUIN tour code {tour_code}",
        f"Country: Bali, Indonesia | Category: {category}",
        f"Destinations: {destinations}",
        f"Ideal for: {extract_ideal_for(text)}",
        f"Best season: {extract_best_season(text)}",
        f"Starting price: {extract_starting_price(text)}",
        f"Vehicle / Meals: {extract_vehicle_meals_id(text)}",
    ]
    for sig in parse_signature_highlights(text)[:4]:
        sig = re.sub(r"\s+", " ", sig).strip()
        if sig and "TRAGUIN Luxury Proposal" not in sig and "TRAGUIN Premium Luxury Itinerary" not in sig:
            highlights.append(sig)
    cleaned = []
    for h in highlights:
        h = re.sub(r"\s+", " ", h).strip()
        if h:
            cleaned.append(h)
    return cleaned[:14]


def emit_hotel(hotel: dict, duration: str) -> str:
    nights = hotel.get("nights_label") or _compact_nights_label(_jh._infer_nights(duration))
    room_type = hotel.get("room_type", "Deluxe Room")
    meal_plan = hotel.get("meal_plan", "MAPAI (Breakfast & Dinner)")
    desc = hotel.get("description") or (
        f"OPTION {hotel['sort_order']:02d} – {hotel['category'].upper()}: "
        f"{hotel['name']} | {room_type} | {meal_plan}"
    )
    return f"""            _hotel(
                {py_str(hotel['name'])},
                {py_str(hotel['location'])},
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
    func = f"build_id_{num}"
    duration = re.sub(r"\s+", " ", extract_duration(text))
    slug = meta["slug"]
    itin_slug = ITIN_SLUG_MAP.get(serial, f"{slug}-itinerary")
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = _clean_day_descriptions(parse_day_blocks_id(text))
    hotels = meta["hotels"]
    included = _clean_items(meta.get("included") or parse_id_inclusions_exclusions(raw_text)[0])
    excluded = meta.get("excluded")
    if excluded is None:
        _, excluded = parse_id_inclusions_exclusions(raw_text)
    excluded = _clean_items(excluded)
    overview = extract_overview_sections(text)
    pkg_highlights = build_package_highlights(meta, text)
    itin_highlights = build_itinerary_highlights(days, text)
    tagline = title.split("•")[0].strip() if "•" in title else title
    tagline = tagline.split("—")[0].strip() if "—" in tagline else tagline

    day_lines = []
    for day in days:
        acts = ",\n".join(f"                    {py_str(a)}" for a in day["activities"]) or (
            f"                    {py_str('Full day as per curated TRAGUIN itinerary.')}"
        )
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
    seo_title = f"{serial} | {tagline[:80]} | TRAGUIN"
    destinations = meta.get("destinations") or extract_destinations_id(text)
    seo_desc = (
        f"Premium {duration} Bali package ({serial} / {tour_code}): "
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
    header = '''"""Builder functions for ID-001 through ID-020 Bali/Indonesia international packages."""

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

BALI_SLUG = "bali"


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
        if not path.exists():
            print(f"{serial}: SKIPPED (no PDF text)")
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = clean_id_raw(raw)
        meta = build_meta(serial, text, raw)
        days = _clean_day_descriptions(parse_day_blocks_id(text))
        builders.append(emit_builder(serial, meta, text, raw))
        print(f"{serial}: {meta['title'][:55]} | days={len(days)} hotels={len(meta['hotels'])}")

    builder_names = [f"build_id_{serial.split('-')[1]}" for serial in BUILDER_ORDER if (PDF_DIR / f"{serial}.txt").exists()]
    footer = "\nINDONESIA_ID_001_020_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
