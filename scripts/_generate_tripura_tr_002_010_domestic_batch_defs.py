#!/usr/bin/env python3
"""Generate tripura_tr_002_010_batch_defs.py from tmp_tr_pdfs text sources."""

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

PDF_DIR = _SCRIPTS.parent / "tmp_tr_pdfs"
OUT_PATH = _SCRIPTS / "tripura_tr_002_010_batch_defs.py"
PRICE_NOTE = "On Request (Premium Customised)"
BUILDER_ORDER = [f"TR-{i:03d}" for i in range(2, 11)]

clean_raw = _jh.clean_raw
py_str = _jh.py_str
extract_best_season = _jh.extract_best_season
extract_starting_price = _jh.extract_starting_price
parse_signature_highlights = _jh.parse_signature_highlights
parse_shopping_notes = _jh.parse_shopping_notes
build_itinerary_highlights = _jh.build_itinerary_highlights
_compact_nights_label = _jh._compact_nights_label

FOOTER_RE = re.compile(
    r"TRAGUIN[^\n]*?Page \d+ of \d+\s*",
    re.I,
)


def _strip_footers(text: str) -> str:
    text = FOOTER_RE.sub("\n", text)
    text = re.sub(r"Page \d+ of \d+\s*", "\n", text, flags=re.I)
    return text


def extract_duration_tripura(text: str) -> str:
    m = re.search(
        r"(?:DURATION|HOLIDAY DURATION|TOUR PACKAGE DURATION):\s*(\d+\s*Nights?\s*/\s*\d+\s*Days?)",
        text,
        re.I,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1))
    m = re.search(r"(\d+\s*Nights?\s*/\s*\d+\s*Days?)", text, re.I)
    return re.sub(r"\s+", " ", m.group(1)) if m else "03 Nights / 04 Days"


def extract_category_tripura(text: str) -> str:
    m = re.search(
        r"CATEGORY:\s*(.+?)(?:IDEAL FOR|DURATION|BEST SEASON|DESTINATIONS|STARTING|TRAGUIN)",
        text,
        re.DOTALL | re.I,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "Premium Tripura Tour"


def extract_ideal_for_tripura(text: str) -> str:
    m = re.search(
        r"IDEAL FOR:\s*(.+?)(?:BEST SEASON|STARTING|TRAGUIN TOUR|TRAGUIN PREMIUM|DURATION)",
        text,
        re.DOTALL | re.I,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return extract_category_tripura(text)


def extract_destinations_tripura(text: str) -> str:
    lines = text.splitlines()
    parts: list[str] = []
    collecting = False
    for i, ln in enumerate(lines):
        stripped = ln.strip()
        if re.match(r"^DESTINATIONS:?\s*$", stripped, re.I):
            collecting = True
            continue
        if collecting:
            if not stripped:
                if parts:
                    break
                continue
            if re.match(r"^(IDEAL FOR|BEST SEASON|STARTING|TRAGUIN|DURATION|CATEGORY)", stripped, re.I):
                break
            parts.append(stripped)
    if parts:
        return re.sub(r"\s+", " ", " ".join(parts)).replace(",", " • ")
    m = re.search(
        r"(?:TRAGUIN (?:PREMIUM |ROMANTIC )?TRIPURA[^\n]+\n)([A-Za-z0-9 •\-–/]+)",
        text,
        re.I,
    )
    if m:
        line = re.sub(r"\s+", " ", m.group(1).strip())
        if len(line) > 8 and "Welcome" not in line:
            return line
    return "Agartala • Tripura"


def extract_tour_code(text: str) -> str:
    flat = re.sub(r"\s+", " ", text)
    for pat in (
        r"TRAGUIN TOUR\s*CODE:\s*([A-Z0-9\-]+)",
        r"CODE:\s*(TG-TR-[A-Z0-9\-]+)",
        r"(TRAGUIN-TR-\d+)",
        r"(TG-TR-[A-Z0-9\-]+)",
    ):
        m = re.search(pat, flat, re.I)
        if m:
            return m.group(1).strip()
    return "TRG-TR-000"


def extract_title_tripura(text: str) -> str:
    patterns = [
        r"TRAGUIN COMPLETE TRIPURA GRAND\s*\nFAMILY TOUR PACKAGE\s*\n(.+?)(?:\nWelcome|\nTRAGUIN)",
        r"TRAGUIN PREMIUM LUXURY TRIPURA\s*\nPACKAGE\s*\n(.+?)(?:\nWelcome|\nTRAGUIN Premium)",
        r"TRAGUIN (?:PREMIUM |ROMANTIC )?TRIPURA[^\n]+\n(?:TOUR |HERITAGE |HONEYMOON |LEISURE )?(?:PACKAGE\s*\n)?(.+?)(?:\n(?:Immerse|Welcome|Step |TRAGUIN Premium|TOUR OVERVIEW))",
        r"TRAGUIN ROMANTIC TRIPURA PREMIUM\s*\nHONEYMOON PACKAGE\s*\n(.+?)(?:\nStep|\nTRAGUIN)",
        r"TRAGUIN PREMIUM TRIPURA[^\n]+\n(.+?)(?:\nImmerse|\nWelcome|\nTRAGUIN)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.DOTALL | re.I)
        if m:
            title = re.sub(r"\s+", " ", m.group(1).strip())
            title = re.sub(r"\s*TRAGUIN.*$", "", title, flags=re.I).strip()
            if len(title) > 10:
                return title[:200]
    return "Tripura Premium Luxury Tour"


def extract_vehicle_meals_tripura(text: str) -> str:
    flat = re.sub(r"\s+", " ", text)
    chunks: list[str] = []
    for label in (
        "Vehicle Layout:",
        "Vehicle Type:",
        "Vehicle:",
        "Meal Strategy:",
        "Meal Plan:",
    ):
        m = re.search(rf"{re.escape(label)}\s*(.+?)(?:Route|TRAGUIN Curated|TOUR OVERVIEW|DESTINATION)", flat, re.I)
        if m:
            chunks.append(m.group(1).strip()[:120])
    return " | ".join(chunks)[:200] if chunks else "Premium AC Luxury Vehicle / MAPAI"


def extract_overview_tripura(text: str) -> str:
    m = re.search(
        r"TOUR OVERVIEW\s*(.+?)(?:DESTINATION(?: SEO| HIGHLIGHTS)|DAY[- ]WISE|DAY-BY-DAY|WHY CHOOSE)",
        text,
        re.DOTALL | re.I,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())[:3000]
    return extract_title_tripura(text)


def make_slug(serial: str, title: str) -> str:
    num = serial.split("-")[1]
    base = title.lower().replace("•", " ").replace("—", " ").replace("/", " ")
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return f"tr-{num}-{base}"[:118].rstrip("-")


def infer_moods(text: str) -> list[str]:
    blob = f"{extract_ideal_for_tripura(text)} {extract_category_tripura(text)} {extract_title_tripura(text)}".lower()
    candidates = [
        ("Family", ("family", "group", "children")),
        ("Luxury", ("luxury", "premium", "bespoke")),
        ("Honeymoon", ("honeymoon", "romantic", "couple", "newlywed")),
        ("Culture", ("culture", "heritage", "history", "palace", "temple")),
        ("Leisure", ("leisure", "senior")),
        ("Educational", ("educational", "school", "student", "institutional")),
        ("Adventure", ("adventure", "hills", "jampui", "trek")),
        ("Nature", ("nature", "wildlife", "sanctuary", "eco")),
    ]
    moods = [mood for mood, keys in candidates if any(k in blob for k in keys)]
    return moods[:3] if moods else ["Family", "Luxury", "Culture"]


def _normalize_tripura_itinerary_section(section: str) -> str:
    section = re.sub(
        r"TRAGUIN[^\n]*?Page \d+ of \d+\s*",
        "\n",
        section,
        flags=re.I,
    )
    section = re.sub(r"Page \d+ of \d+\s*", "\n", section, flags=re.I)
    return section


def parse_day_blocks_tripura(text: str) -> list[dict]:
    start = re.search(
        r"(?:DAY[- ]BY[- ]DAY(?: DETAILED| SACRED)? ITINERARY|DAY[- ]WISE ITINERARY|DETAILED DAY-WISE ITINERARY)",
        text,
        re.I,
    )
    if start:
        section = text[start.end() :]
    else:
        day_one = re.search(r"^DAY\s*0?1\s+\|", text, re.MULTILINE | re.I)
        if not day_one:
            return []
        section = text[day_one.start() :]
    end = re.search(
        r"(?m)^(?:HOTEL OPTIONS|PREMIUM HOTEL|PREMIUM STAY|LUXURY HOTEL|PREMIUM HOTEL ACCOMMODATIONS)",
        section,
        re.I,
    )
    if end:
        section = section[: end.start()]
    section = _normalize_tripura_itinerary_section(_strip_footers(section))

    day_starts = list(re.finditer(r"^DAY\s*(\d+)\s*(?:\||–|-)\s*(.+)$", section, re.MULTILINE | re.I))
    activity_labels = (
        "Sightseeing Included",
        "Optional Activities",
        "Evening Experience",
        "Overnight Stay",
        "Meals Included",
        "Transfers Included",
        "Assistance",
        "Sightseeing",
        "Optional",
        "Evening",
        "Meals",
    )
    days: list[dict] = []
    for idx, match in enumerate(day_starts):
        day_num = int(match.group(1))
        title_line = re.sub(r"\s+", " ", match.group(2).strip()).upper()
        body_start = match.end()
        body_end = day_starts[idx + 1].start() if idx + 1 < len(day_starts) else len(section)
        body = section[body_start:body_end].strip()
        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        paragraphs: list[str] = []
        activities: list[str] = []
        current_para: list[str] = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if line in {"Sightseeing", "Optional", "Evening", "Meals", "Transfers"} and i + 1 < len(lines):
                nxt = lines[i + 1]
                if ":" in nxt or nxt in {"Included", "Activities", "Experience", "Stay", "Included:"}:
                    label = f"{line} {nxt.split(':')[0].strip()}"
                    val = nxt.split(":", 1)[1].strip() if ":" in nxt else ""
                    if not val and i + 2 < len(lines) and not lines[i + 2].startswith("DAY"):
                        i += 2
                        val = lines[i]
                    else:
                        i += 1
                    activities.append(f"{label}: {val}" if val else label)
                    i += 1
                    continue
            label_match = re.match(
                rf"^({'|'.join(re.escape(x) for x in activity_labels)}):?\s*(.*)$",
                line,
                re.I,
            )
            if label_match:
                label = label_match.group(1).strip()
                val = label_match.group(2).strip()
                if not val and i + 1 < len(lines):
                    i += 1
                    val = lines[i]
                activities.append(f"{label}: {val}" if val else label)
                i += 1
                continue
            current_para.append(line)
            if line.endswith(".") or line.endswith(")"):
                paragraphs.append(" ".join(current_para))
                current_para = []
            i += 1
        if current_para:
            paragraphs.append(" ".join(current_para))
        description = re.sub(r"\s+", " ", " ".join(paragraphs)).strip()
        if not description and activities:
            description = activities[0].split(":", 1)[-1].strip()
        days.append(
            {
                "day_number": day_num,
                "title": title_line,
                "description": description,
                "activities": activities,
            }
        )
    return days


def _clean_day_descriptions(days: list[dict]) -> list[dict]:
    stops = ("HOTEL OPTIONS", "PACKAGE INCLUSIONS", "PREMIUM HOTEL", "TRAGUIN Luxury")
    cleaned = []
    for day in days:
        desc = day["description"]
        for marker in stops:
            idx = desc.find(marker)
            if idx != -1:
                desc = desc[:idx].strip()
        cleaned.append({**day, "description": re.sub(r"\s+", " ", desc).strip()})
    return cleaned


def _normalize_hotel_category(raw: str) -> str:
    cat = re.sub(r"\s+", " ", raw.strip()).title()
    if "ultra" in cat.lower():
        return "Ultra Luxury"
    if cat.lower().startswith("premium"):
        return "Premium"
    if cat.lower().startswith("luxury"):
        return "Luxury"
    if cat.lower().startswith("deluxe"):
        return "Deluxe"
    return cat


def parse_tripura_inline_hotels(text: str) -> list[dict]:
    section_m = re.search(
        r"(?:HOTEL OPTIONS|PREMIUM HOTEL|PREMIUM STAY|LUXURY HOTEL|PREMIUM HOTEL ACCOMMODATIONS)[^\n]*\s*"
        r"(.+?)(?:PACKAGE INCLUSIONS)",
        text,
        re.DOTALL | re.I,
    )
    if not section_m:
        return []
    section = section_m.group(1)
    options: list[dict] = []
    pattern = re.compile(
        r"OPTION\s*0?(\d+)\s*[–-]\s*"
        r"((?:ULTRA\s*LUXURY|DELUXE|PREMIUM(?:\s*LUXURY)?|LUXURY)(?:\s*\([^)]+\))?)\s*:?\s*"
        r"(.+?)(?=OPTION\s*0?\d+\s*[–-]|PACKAGE INCLUSIONS|\Z)",
        re.DOTALL | re.I,
    )
    nights = _jh._infer_nights(text)
    for m in pattern.finditer(section):
        num = int(m.group(1))
        category = _normalize_hotel_category(re.sub(r"\s*\(.*\)\s*$", "", m.group(2)))
        name = re.sub(r"\s+", " ", m.group(3).strip()).strip(" :")
        if not name or len(name) < 5:
            continue
        options.append(
            {
                "sort_order": num,
                "category": category,
                "name": name[:128],
                "location": "Agartala",
                "nights_label": nights,
                "room_type": "Deluxe Room" if category == "Deluxe" else "Premium Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 5 if "ultra" in category.lower() or category == "Luxury" else 4,
                "description": f"OPTION {num:02d} – {category.upper()}: {name[:100]}",
            }
        )
    return sorted(options, key=lambda x: x["sort_order"])


def parse_tripura_table_hotels(text: str) -> list[dict]:
    section_m = re.search(
        r"(?:HOTEL OPTIONS SECTION|HANDPICKED PREMIUM ACCOMMODATION OPTIONS)\s*(.+?)(?:PACKAGE (?:INCLUSIONS|EXCLUSIONS))",
        text,
        re.DOTALL | re.I,
    )
    if not section_m:
        return []
    section = section_m.group(1)
    options: list[dict] = []
    pattern = re.compile(
        r"OPTION\s*0?(\d+)\s*[–-]\s*((?:DELUXE|PREMIUM|LUXURY|ULTRA\s*\n?\s*LUXURY|ULTRA))\s*([Hh]otel.+?)"
        r"(?=OPTION\s*0?\d+\s*[–-]|PACKAGE |\Z)",
        re.DOTALL,
    )
    nights = _jh._infer_nights(text)
    for m in pattern.finditer(section):
        num = int(m.group(1))
        category = _normalize_hotel_category(m.group(2))
        block = m.group(3)
        block = re.sub(r"\s+", " ", block)
        block = re.sub(r"(Superior|Premier|Executive|Royal|Presidential|Luxury|Deluxe|Premium|Club|Exclusive).*(Room|Suite|Meals|MAPAI).*$", "", block, flags=re.I)
        block = re.sub(r"MAPAI.*$", "", block, flags=re.I)
        name = re.sub(r"\s+", " ", block).strip(" /")
        if not name or len(name) < 4:
            continue
        options.append(
            {
                "sort_order": num,
                "category": category,
                "name": name[:128],
                "location": "Agartala",
                "nights_label": nights,
                "room_type": "Deluxe Room" if category == "Deluxe" else "Premium Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 5 if "ultra" in category.lower() or category == "Luxury" else 4,
                "description": f"OPTION {num:02d} – {category.upper()}: {name[:100]}",
            }
        )
    if not options:
        pattern2 = re.compile(
            r"OPTION\s*0?(\d+)\s*[–-]\s*((?:DELUXE|PREMIUM|LUXURY|ULTRA\s*LUXURY))\s*(.+?)"
            r"(?=OPTION\s*0?\d+\s*[–-]|PACKAGE |\Z)",
            re.DOTALL | re.I,
        )
        for m in pattern2.finditer(section):
            num = int(m.group(1))
            category = _normalize_hotel_category(m.group(2))
            block = re.sub(r"\s+", " ", m.group(3))
            block = re.sub(r"(Room|Suite|MAPAI|Meals|Premium Curated).*$", "", block, flags=re.I).strip()
            if len(block) < 4:
                continue
            options.append(
                {
                    "sort_order": num,
                    "category": category,
                    "name": block[:128],
                    "location": "Agartala",
                    "nights_label": nights,
                    "room_type": "Deluxe Room",
                    "meal_plan": "MAPAI (Breakfast & Dinner)",
                    "stars": 5 if "ultra" in category.lower() else 4,
                    "description": f"OPTION {num:02d} – {category.upper()}: {block[:100]}",
                }
            )
    return sorted(options, key=lambda x: x["sort_order"])


def parse_tripura_inclusions_exclusions(text: str) -> tuple[list[str], list[str]]:
    cleaned = _strip_footers(text)
    cleaned = _normalize_tripura_itinerary_section(cleaned)
    included: list[str] = []
    excluded: list[str] = []

    exc_keys = (
        "airfare",
        "flight",
        "rail ticket",
        "train ticket",
        "personal expense",
        "laundry",
        "minibar",
        "telephone",
        "camera",
        "insurance",
        "optional adventure",
        "water sport",
        "liquor",
        "gst outside",
    )

    section_m = re.search(
        r"PACKAGE INCLUSIONS[^S]*(?:& EXCLUSIONS)?\s*(.+?)(?:SPECIAL TRAGUIN|SHOPPING|IMPORTANT|TRAGUIN Premium|\Z)",
        cleaned,
        re.DOTALL | re.I,
    )
    if section_m:
        for line in section_m.group(1).splitlines():
            line = re.sub(r"^\s*•\s*", "", line).strip()
            if not line or line in {"✔", "✘"}:
                continue
            if re.match(r"✔\s*INCLUSIONS", line, re.I) or re.match(r"✘\s*EXCLUSIONS", line, re.I):
                continue
            item = re.sub(r"\s+", " ", line).strip()
            if len(item) < 12 or "Page " in item:
                continue
            if any(k in item.lower() for k in exc_keys):
                if item not in excluded:
                    excluded.append(item)
            elif item not in included:
                included.append(item)

    inc_block = re.search(
        r"✔\s*INCLUSIONS\s*(.+?)(?:✘\s*EXCLUSIONS|SPECIAL TRAGUIN|SHOPPING|IMPORTANT|\Z)",
        cleaned,
        re.DOTALL | re.I,
    )
    if inc_block:
        blob = re.sub(r"\s*•\s*", " ", inc_block.group(1))
        for chunk in re.split(r"\n\s*\n", blob):
            item = re.sub(r"\s+", " ", chunk).strip(" •")
            if item and len(item) > 12 and "Page " not in item:
                included.append(item)

    exc_block = re.search(
        r"✘\s*EXCLUSIONS\s*(.+?)(?:SPECIAL TRAGUIN|SHOPPING|IMPORTANT|TRAGUIN Premium|\Z)",
        cleaned,
        re.DOTALL | re.I,
    )
    if exc_block:
        blob = re.sub(r"\s*•\s*", " ", exc_block.group(1))
        for chunk in re.split(r"\n\s*\n", blob):
            item = re.sub(r"\s+", " ", chunk).strip(" •")
            if item and len(item) > 12:
                excluded.append(item)

  # Label: description with marker on same or next line
    for m in re.finditer(
        r"((?:Accommodation|Meals|Transfers|Sightseeing|Assistance|Welcome Amenities|Complimentary Experiences|Taxes|Flights|Entry Tickets|Personal Expenses|Activities|Insurance)[^✔✘\n]{4,}?)\s*✔",
        cleaned,
        re.I,
    ):
        item = re.sub(r"\s+", " ", m.group(1)).strip()
        if len(item) > 10 and item not in included:
            included.append(item)

    for m in re.finditer(
        r"((?:Flights|Entry Tickets|Personal Expenses|Activities|Insurance|Taxes)[^✔✘\n]{4,}?)\s*✘",
        cleaned,
        re.I,
    ):
        item = re.sub(r"\s+", " ", m.group(1)).strip()
        if len(item) > 10 and item not in excluded:
            excluded.append(item)

    for m in re.finditer(r"([A-Za-z][^✔✘\n]{8,}?)\s*✔", cleaned):
        item = re.sub(r"\s+", " ", m.group(1)).strip()
        if any(x in item.upper() for x in ("INCLUSIONS", "EXCLUSIONS", "PAGE ", "GST OUTSIDE")):
            continue
        if len(item) > 10 and item not in included:
            included.append(item)

    for m in re.finditer(r"([A-Za-z][^✔✘\n]{8,}?)\s*✘", cleaned):
        item = re.sub(r"\s+", " ", m.group(1)).strip()
        if any(x in item.upper() for x in ("INCLUSIONS", "EXCLUSIONS", "PAGE ")):
            continue
        if len(item) > 10 and item not in excluded:
            excluded.append(item)

    inc_clean: list[str] = []
    for item in included:
        for part in re.split(r"\s*✘\s*", item):
            part = part.strip()
            if part and len(part) > 10:
                inc_clean.append(part)
    exc_clean: list[str] = []
    for item in excluded:
        for part in re.split(r"\s*✔\s*", item):
            part = part.strip()
            if part and len(part) > 10:
                exc_clean.append(part)

    return inc_clean[:14], exc_clean[:10]


def _clean_items(items: list[str]) -> list[str]:
    out = []
    for item in items:
        item = re.sub(r"\s+", " ", item).strip()
        if not item or len(item) < 8:
            continue
        if "TRAGUIN Luxury Proposal" in item or "Premium Luxury Holidays Page" in item:
            continue
        if item.startswith("IMPORTANT NOTES"):
            continue
        out.append(item)
    return out


def build_meta(serial: str, text: str, raw: str) -> dict:
    src = raw
    title = extract_title_tripura(src)
    tour_code = extract_tour_code(src)
    destinations = extract_destinations_tripura(src)
    hotels = parse_tripura_inline_hotels(src)
    if len(hotels) < 2:
        table = parse_tripura_table_hotels(src)
        if len(table) > len(hotels):
            hotels = table
    if not hotels:
        nights = _jh._infer_nights(src)
        hotels = [
            {
                "sort_order": i,
                "category": cat,
                "name": f"TRAGUIN Handpicked {cat} Property — Agartala",
                "location": "Agartala",
                "nights_label": nights,
                "room_type": "Deluxe Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 5 if "ultra" in cat.lower() else 4,
                "description": f"OPTION {i:02d} – {cat.upper()}: TRAGUIN Handpicked {cat} Property",
            }
            for i, cat in enumerate(["Deluxe", "Premium", "Luxury", "Ultra Luxury"], 1)
        ]
    for hotel in hotels:
        hotel["nights_label"] = _compact_nights_label(hotel.get("nights_label") or _jh._infer_nights(src))
    included, excluded = parse_tripura_inclusions_exclusions(src)
    return {
        "serial": serial,
        "tour_code": tour_code,
        "slug": make_slug(serial, title),
        "title": title,
        "destinations": destinations,
        "moods": infer_moods(src),
        "hotels": hotels,
        "included": included,
        "excluded": excluded,
    }


def build_package_highlights(meta: dict, text: str) -> list[str]:
    highlights = [
        f"Serial code {meta['serial']} | TRAGUIN tour code {meta['tour_code']}",
        f"State / Country: Tripura / India | Category: {extract_category_tripura(text)}",
        f"Destinations: {meta.get('destinations') or extract_destinations_tripura(text)}",
        f"Ideal for: {extract_ideal_for_tripura(text)}",
        f"Best season: {extract_best_season(text) or 'October to March'}",
        f"Starting price: {extract_starting_price(text) or 'On Request'}",
        f"Vehicle / Meals: {extract_vehicle_meals_tripura(text)}",
    ]
    for sig in parse_signature_highlights(text)[:4]:
        sig = re.sub(r"\s+", " ", sig).strip()
        if sig:
            highlights.append(sig)
    return [h for h in highlights if h][:14]


def emit_hotel(hotel: dict, duration: str) -> str:
    nights = hotel.get("nights_label") or _compact_nights_label(_jh._infer_nights(duration))
    room_type = hotel.get("room_type", "Deluxe Room")
    meal_plan = hotel.get("meal_plan", "MAPAI (Breakfast & Dinner)")
    desc = hotel.get("description") or (
        f"OPTION {hotel['sort_order']:02d} – {hotel['category'].upper()}: {hotel['name']}"
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
    func = f"build_tr_{num}"
    duration = extract_duration_tripura(raw_text)
    slug = meta["slug"]
    itin_slug = f"{slug}-itinerary"
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = _clean_day_descriptions(parse_day_blocks_tripura(raw_text))
    hotels = meta["hotels"]
    included = _clean_items(meta.get("included") or parse_tripura_inclusions_exclusions(raw_text)[0])
    excluded = _clean_items(meta.get("excluded") or parse_tripura_inclusions_exclusions(raw_text)[1])
    overview = extract_overview_tripura(raw_text)
    pkg_highlights = build_package_highlights(meta, raw_text)
    itin_highlights = build_itinerary_highlights(days, text)
    tagline = title.split("•")[0].strip() if "•" in title else title
    destinations = meta.get("destinations") or extract_destinations_tripura(text)
    seo_desc = (
        f"Premium {duration} Tripura package ({serial} / {tour_code}): "
        f"{destinations[:100]} with handpicked accommodation."
    )

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
    header = '''"""Builder functions for TR-002 through TR-010 Tripura domestic packages."""

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

TRIPURA_SLUG = "tripura"


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
        meta = build_meta(serial, raw, raw)
        builders.append(emit_builder(serial, meta, raw, raw))
        print(
            f"{serial}: {meta['title'][:55]} | days={len(_clean_day_descriptions(parse_day_blocks_tripura(raw)))} "
            f"hotels={len(meta['hotels'])} inc={len(meta['included'])+len(meta['excluded'])}"
        )

    builder_names = [f"build_tr_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nTRIPURA_TR_002_010_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
