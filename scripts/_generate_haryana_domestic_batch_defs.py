#!/usr/bin/env python3
"""Generate haryana_domestic_batch_defs.py from tmp_hr_pdfs text sources."""

from __future__ import annotations

import re
from pathlib import Path

PDF_DIR = Path(__file__).resolve().parent.parent / "tmp_hr_pdfs"
OUT_PATH = Path(__file__).resolve().parent / "haryana_domestic_batch_defs.py"

PACKAGE_META: dict[str, dict] = {
    "HR-001": {
        "tour_code": "TRAGUIN-HAR-KUR-001",
        "slug": "hr-001-kurukshetra-heritage-trail",
        "title": "Dharmakshetra Kurukshetra Heritage Trail",
        "moods": ["Heritage", "Family", "Spiritual"],
    },
    "HR-002": {
        "tour_code": "TRAGUIN-HR-002",
        "slug": "hr-002-kurukshetra-spiritual-tour",
        "title": "Kurukshetra Spiritual Tour",
        "moods": ["Spiritual", "Heritage", "Luxury"],
        "hotels": [
            {
                "sort_order": 1,
                "category": "Luxury",
                "name": "The Divine Castle / Noormahal Palace Heritage variant",
                "location": "Kurukshetra",
                "nights_label": "03 Nights",
                "room_type": "Executive Suite / Club Room",
                "meal_plan": "Breakfast & Dinner (MAP)",
                "stars": 5,
                "description": "OPTION 01 – LUXURY: The Divine Castle / Noormahal Palace Heritage variant | Executive Suite / Club Room | Breakfast & Dinner (MAP)",
            },
            {
                "sort_order": 2,
                "category": "Deluxe",
                "name": "Hotel Kimaya / Golden Tulip Essence",
                "location": "Kurukshetra",
                "nights_label": "03 Nights",
                "room_type": "Super Deluxe King Room",
                "meal_plan": "Breakfast & Dinner (MAP)",
                "stars": 4,
                "description": "OPTION 02 – DELUXE: Hotel Kimaya / Golden Tulip Essence | Super Deluxe King Room | Breakfast & Dinner (MAP)",
            },
            {
                "sort_order": 3,
                "category": "Premium",
                "name": "Hotel Red Castle / Divine Clerks",
                "location": "Kurukshetra",
                "nights_label": "03 Nights",
                "room_type": "Super Deluxe Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 4,
                "description": "OPTION 03 – PREMIUM: Hotel Red Castle / Divine Clerks | Super Deluxe Room | MAPAI",
            },
            {
                "sort_order": 4,
                "category": "Ultra Luxury",
                "name": "Curated Heritage Boutique Farm & Wellness Villa",
                "location": "Kurukshetra",
                "nights_label": "03 Nights",
                "room_type": "Royal Club Villa",
                "meal_plan": "All Inclusive Premium Meals",
                "stars": 5,
                "description": "OPTION 04 – ULTRA LUXURY: Curated Heritage Boutique Farm & Wellness Villa | Royal Club Villa | All Inclusive Premium Meals",
            },
        ],
    },
    "HR-003": {
        "tour_code": "TRAGUIN-HR-003-2026",
        "slug": "hr-003-sultanpur-birding-gurugram-eco",
        "title": "Sultanpur Birding Tour • Gurugram Premium Escapes",
        "moods": ["Family", "Luxury", "Heritage"],
    },
    "HR-004": {
        "tour_code": "TRAGUIN-LUX-HR-004",
        "slug": "hr-004-luxury-haryana-retreat",
        "title": "Luxury Haryana Retreat",
        "moods": ["Luxury", "Family", "Heritage"],
    },
    "HR-005": {
        "tour_code": "TG-HAR-SR-005",
        "slug": "hr-005-royal-heritage-wellness-circuit",
        "title": "Royal Heritage & Wellness Leisure Circuit",
        "moods": ["Heritage", "Family", "Luxury"],
    },
    "HR-006": {
        "tour_code": "TG-HR-EDU-006",
        "slug": "hr-006-educational-kurukshetra-pinjore",
        "title": "Educational Tour Kurukshetra & Pinjore",
        "moods": ["Heritage", "Family", "Spiritual"],
    },
    "HR-007": {
        "tour_code": "TRG-HAR-007",
        "slug": "hr-007-haryana-explorer",
        "title": "Haryana Explorer",
        "moods": ["Family", "Heritage", "Luxury"],
    },
    "HR-008": {
        "tour_code": "TRG-GURG-MICE-008",
        "slug": "hr-008-gurgaon-mice-excellence",
        "title": "Gurgaon MICE Excellence",
        "moods": ["Luxury", "Family", "Heritage"],
    },
    "HR-009": {
        "tour_code": "TRG-HAR-009",
        "slug": "hr-009-heritage-haryana",
        "title": "Heritage Haryana",
        "moods": ["Heritage", "Family", "Spiritual"],
        "hotels": [
            {
                "sort_order": 1,
                "category": "Deluxe",
                "name": "Hotel Divine Clerks / similar",
                "location": "Kurukshetra | Narnaul",
                "nights_label": "02 Nights Kurukshetra + 02 Nights Narnaul",
                "room_type": "Deluxe Room | Heritage Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 4,
                "description": "OPTION 01 – DELUXE: Hotel Divine Clerks / similar | Shree Hari Heritage Hotel / similar | MAPAI",
            },
            {
                "sort_order": 2,
                "category": "Premium",
                "name": "The King's Sukham / similar",
                "location": "Kurukshetra | Narnaul",
                "nights_label": "02 Nights Kurukshetra + 02 Nights Narnaul",
                "room_type": "Premium Suite | Heritage Plaza Luxury Rooms",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 4,
                "description": "OPTION 02 – PREMIUM: The King's Sukham / similar | Hotel Heritage Plaza Luxury Rooms | MAPAI",
            },
            {
                "sort_order": 3,
                "category": "Luxury",
                "name": "Premium Heritage Haveli Suite",
                "location": "Kurukshetra | Narnaul",
                "nights_label": "02 Nights Kurukshetra + 02 Nights Narnaul",
                "room_type": "Heritage Haveli Suite | Restored Boutique Fort Mansion",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 5,
                "description": "OPTION 03 – LUXURY: Premium Heritage Haveli Suite | Restored Boutique Fort Mansion / Haveli Stay | MAPAI",
            },
            {
                "sort_order": 4,
                "category": "Ultra Luxury",
                "name": "VVIP Custom Private Villa Stay",
                "location": "Kurukshetra | Narnaul",
                "nights_label": "02 Nights Kurukshetra + 02 Nights Narnaul",
                "room_type": "Private Villa | The Neemrana Fort Palace Elite Wing",
                "meal_plan": "Bespoke Heritage Dining Plan",
                "stars": 5,
                "description": "OPTION 04 – ULTRA LUXURY: VVIP Custom Private Villa Stay | The Neemrana Fort Palace Elite Wing (Nearby) | Bespoke Plan",
            },
        ],
    },
    "HR-010": {
        "tour_code": "TRG-HAR-010",
        "slug": "hr-010-complete-haryana-premium-family-tour",
        "title": "Complete Haryana Premium Family Tour",
        "moods": ["Family", "Heritage", "Luxury"],
    },
}

BUILDER_ORDER = [f"HR-{i:03d}" for i in range(1, 11)]

FOOTER_RE = re.compile(
    r"TRAGUIN(?: Premium (?:Luxury )?(?:Holidays|Itinerary|Holiday Proposals|Travel & Luxury Holidays|"
    r"Luxury Itinerary|Corporate MICE Proposal)| Corporate MICE Proposal| Premium Holidays)"
    r"[^\n]*\n\d+\s*\n?",
    re.IGNORECASE,
)
PAGE_RE = re.compile(r"Page \d+ of \d+\s*\n?", re.IGNORECASE)
TAGLINE_RE = re.compile(
    r"PREMIUM TRAVEL \| LUXURY HOLIDAYS \| CORPORATE MICE \| HONEYMOON EXPERTS \| FAMILY\s*VACATIONS\s*",
    re.IGNORECASE,
)
QUOTE_RE = re.compile(r'"Creating Memories Beyond Destinations"\s*', re.IGNORECASE)
BULLET_ONLY_RE = re.compile(r"^[\s•]+$", re.MULTILINE)
PROPOSAL_ID_RE = re.compile(r"Proposal Document ID:.*\n?", re.IGNORECASE)


def clean_raw(text: str) -> str:
    text = FOOTER_RE.sub("", text)
    text = PAGE_RE.sub("", text)
    text = TAGLINE_RE.sub("", text)
    text = QUOTE_RE.sub("", text)
    text = PROPOSAL_ID_RE.sub("", text)
    text = BULLET_ONLY_RE.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def py_str(value: str) -> str:
    return repr(value)


def extract_duration(text: str) -> str:
    m = re.search(
        r"DURATION:\s*\n((?:\d+\s*Nights?\s*/\s*\d+\s*Days?)|(?:\d+\s*Nights?\s*/\s*\n\s*\d+\s*Days?))",
        text,
        re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    m = re.search(r"(\d+\s*Nights?\s*/\s*\d+\s*Days?)", text, re.IGNORECASE)
    return re.sub(r"\s+", " ", m.group(1).strip()) if m else "03 Nights / 04 Days"


def extract_category(text: str) -> str:
    m = re.search(
        r"CATEGORY:\s*\n(.+?)(?:\nTRAGUIN|\nDURATION|\nBEST|\nIDEAL|\nSTARTING|\nDESTINATIONS|\nVEHICLE|\nTOUR|\n[A-Z]{2,})",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "Premium Haryana Tour"


def extract_destinations(text: str) -> str:
    lines = text.splitlines()
    collecting = False
    parts: list[str] = []
    for ln in lines:
        if re.match(r"DESTINATIONS(?: COVERED)?:\s*$", ln.strip(), re.I):
            collecting = True
            continue
        if collecting:
            stripped = ln.strip()
            if not stripped:
                if parts:
                    break
                continue
            if re.match(
                r"^(IDEAL FOR|BEST SEASON|STARTING PRICE|TRAGUIN TOUR|VEHICLE|TOUR OVERVIEW|DURATION|CATEGORY|TRAVEL MONTH):",
                stripped,
                re.I,
            ):
                break
            parts.append(stripped)
    if parts:
        return re.sub(r"\s+", " ", " ".join(parts))
    return "Haryana"


def extract_ideal_for(text: str) -> str:
    m = re.search(
        r"IDEAL FOR:\s*\n(.+?)(?:\nSTARTING|\nBEST|\nTRAGUIN TOUR|\nVEHICLE|\nTOUR|\nTRAGUIN PREMIUM|\n[A-Z]{2,}-\d{3})",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "Luxury Travelers"


def extract_best_season(text: str) -> str:
    m = re.search(
        r"BEST SEASON:\s*\n(.+?)(?:\nDESTINATIONS|\nIDEAL|\nSTARTING|\nTRAGUIN TOUR|\nVEHICLE|\nTOUR|\nTRAGUIN PREMIUM|\n[A-Z]{2,}-\d{3})",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "October to March"


def extract_starting_price(text: str) -> str:
    m = re.search(
        r"STARTING PRICE:\s*\n(.+?)(?:\nTRAGUIN TOUR|\nTOUR CODE|\nVEHICLE|\nTOUR OVERVIEW|\nTRAGUIN PREMIUM|\n[A-Z]{2,}-\d{3}|TRAVEL MONTH)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "On Request"


def extract_vehicle_meals(text: str) -> str:
    for label in ("VEHICLE & MEALS:", "VEHICLE / MEALS:", "VEHICLE / MEAL PLAN:", "VEHICLE TYPE:", "VEHICLE STYLE:", "VEHICLE:"):
        idx = text.upper().find(label.upper())
        if idx == -1:
            continue
        lines = []
        for ln in text[idx + len(label) :].splitlines():
            stripped = ln.strip()
            if not stripped:
                if lines:
                    break
                continue
            if re.match(
                r"^(TRAGUIN|TOUR OVERVIEW|DURATION|DESTINATIONS|IDEAL FOR|BEST SEASON|STARTING PRICE|TRAGUIN TOUR|DETAILED|DAY-WISE|DAY 0|ROUTE|BEST HARYANA|TRAVEL MONTH)",
                stripped,
                re.I,
            ):
                break
            lines.append(stripped)
        if lines:
            return re.sub(r"\s+", " ", " ".join(lines))
    return "Private Luxury SUV / MAPAI"


def extract_route(text: str) -> str:
    for pattern in (
        r"ROUTE(?: MAP| PLAN| OUTLINE)?:\s*\n(.+?)(?:\nTRAGUIN|\nWHY CHOOSE|\nDETAILED|\nDAY-WISE|\nDAY 0)",
        r"Route:\s*(.+?)(?:\nVehicle|\nMeal|\nGuest|\nTRAGUIN Curated|\nWHY CHOOSE|\nDAY-WISE|\nDAY 0)",
        r"ROUTE:\s*(.+?)(?:\nVEHICLE|\nMEAL|\nTRAGUIN NOTE|\nWHY CHOOSE|\nDAY 0)",
    ):
        m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if m:
            route = re.sub(r"\s+", " ", m.group(1).strip())
            route = re.split(r"\bVEHICLE\b|\bMEAL\b|\bTRAGUIN NOTE\b", route, maxsplit=1, flags=re.I)[0].strip()
            return route
    return ""


def extract_overview_sections(text: str) -> str:
    parts: list[str] = []
    welcome = re.search(
        r"(?:TRAGUIN PREMIUM[^\n]+\n[^\n]+\n|Welcome(?: Note)?:[^\n]+\n|Embark on an? .+?)(.+?)(?:\nTOUR OVERVIEW|\nWHY CHOOSE|\nWHY BOOK|\nWHY VISIT|\nDETAILED|\nDAY-WISE|\nDAY 0)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if welcome:
        parts.append(re.sub(r"\s+", " ", welcome.group(1).strip()))

    tour_overview = re.search(
        r"TOUR OVERVIEW\s*\n(.+?)(?:\nWHY CHOOSE|\nWHY BOOK|\nWHY VISIT|\nDESTINATION SEO|\nDETAILED|\nDAY-WISE|\nDAY 0)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if tour_overview:
        body = re.sub(r"\s+", " ", tour_overview.group(1).strip())
        parts.append(f"TOUR OVERVIEW\n{body}")

    why_heading = re.search(
        r"(WHY (?:CHOOSE|VISIT|BOOK)[^\n]+\??)\s*\n(.+?)(?:\nDETAILED|\nDAY-WISE|\nDAY 0|\nHANDPICKED|\nPREMIUM ACCOMMODATION|\nHOTEL OPTIONS)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if why_heading:
        body = re.sub(r"\s+", " ", why_heading.group(2).strip())
        parts.append(f"{why_heading.group(1).strip()}\n{body}")

    seo = re.search(
        r"DESTINATION SEO CONTENT\s*\n(.+?)(?:\nDAY WISE|\nDAY-WISE|\nHANDPICKED|\nHOTEL OPTIONS)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if seo:
        body = re.sub(r"\s+", " ", seo.group(1).strip())
        parts.append(f"DESTINATION SEO CONTENT\n{body}")

    return "\n\n".join(parts)


def parse_day_blocks(text: str) -> list[dict]:
    start = re.search(
        r"(?:DETAILED DAY-WISE ITINERARY|DAY-WISE IMMERSIVE ITINERARY|DAY WISE ITINERARY|DAY-WISE CUSTOM ITINERARY|DAY-WISE ITINERARY)",
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
        r"(?m)^(?:HANDPICKED (?:LUXURY )?(?:PREMIUM )?(?:MICE )?(?:CORPORATE )?(?:ACCOMMODATION|HOTEL)|"
        r"PREMIUM ACCOMMODATION|PREMIUM CORPORATE HOTEL|HOTEL OPTIONS SECTION|"
        r"HANDPICKED PREMIUM ACCOMMODATION|HANDPICKED ACCOMMODATION|HANDPICKED PREMIUM HOTEL)",
        section,
    )
    if end:
        section = section[: end.start()]

    section = FOOTER_RE.sub("", section)
    section = PAGE_RE.sub("", section)

    day_starts = list(re.finditer(r"^DAY\s*(\d+)\s*(?:\||–|-)\s*(.+)$", section, re.MULTILINE | re.IGNORECASE))
    if not day_starts:
        day_starts = list(re.finditer(r"^DAY\s*(\d+)\s+(.+)$", section, re.MULTILINE | re.IGNORECASE))

    days: list[dict] = []
    for idx, match in enumerate(day_starts):
        day_num = int(match.group(1))
        title_line = re.sub(r"\s+", " ", match.group(2).strip()).upper()
        body_start = match.end()
        body_end = day_starts[idx + 1].start() if idx + 1 < len(day_starts) else len(section)
        body = section[body_start:body_end].strip()

        paragraphs: list[str] = []
        activities: list[str] = []
        current_para: list[str] = []

        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        i = 0
        activity_labels = (
            "Sightseeing Included",
            "Sightseeing En-route",
            "Optional Activities",
            "Evening Experience",
            "Overnight Stay",
            "Meals Included",
            "Meals",
            "Transfers Included",
            "Food Suggestions",
            "Local Experience",
            "Local Experiences",
            "Complimentary Experience",
            "Photography Points",
            "Shopping",
            "Welcome Note",
            "Sightseeing & Drop",
        )
        while i < len(lines):
            line = lines[i]
            label_match = re.match(rf"^({'|'.join(activity_labels)}):?\s*(.*)$", line, re.IGNORECASE)
            if label_match:
                label = label_match.group(1).strip()
                val = label_match.group(2).strip()
                if not val and i + 1 < len(lines) and not re.match(r"^DAY\s*\d+", lines[i + 1], re.I):
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


def _infer_nights(text: str) -> str:
    duration = extract_duration(text)
    m = re.search(r"(\d+)\s*Nights?", duration, re.I)
    return f"{m.group(1)} Nights" if m else "03 Nights"


def _infer_nights_from_duration(duration: str) -> str:
    m = re.search(r"(\d+)\s*Nights?", duration, re.I)
    return f"{m.group(1)} Nights" if m else "03 Nights"


def _normalize_category(cat: str) -> str:
    c = cat.strip().title()
    if "Ultra" in c:
        return "Ultra Luxury"
    return c


def _normalize_hotel_block_lines(lines: list[str]) -> list[str]:
    merged: list[str] = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.rstrip().endswith("/") and i + 1 < len(lines):
            merged.append(f"{ln.rstrip()} {lines[i + 1].strip()}")
            i += 2
            continue
        if ln.strip().startswith("/") and merged:
            merged[-1] = f"{merged[-1]} {ln.strip()}"
            i += 1
            continue
        merged.append(ln)
        i += 1
    return merged


def _is_skip_line(ln: str) -> bool:
    return bool(
        re.match(
            r"^(Category|Option Level|OPTION|Option Tier|Meal Plan|Room Category|Key Included|Conference|"
            r"Corporate Meal|Room Style|INCLUSIONS|GURUGRAM|KURUKSHETRA|PANCHKULA|HISAR|CHANDIGARH|"
            r"Manesar|Resort|Gurgaon|NIGHTS|Stay Nights|TIER|HOTEL & RESORT|HOTEL OPTIONS|CATEGORY)$",
            ln,
            re.I,
        )
        or re.match(r"^\(\d+N\)$", ln)
        or re.match(r"^\d+N\)$", ln)
        or re.match(r"^\d+\s*Nights?\s", ln, re.I)
    )


def _parse_multi_city_option(block: str, num: int, category: str, text: str) -> dict | None:
    lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
    city_hotels: list[str] = []
    city_locations: list[str] = []
    room_type = "Deluxe Room"
    meal_plan = "MAPAI (Breakfast & Dinner Included)"
    nights_label = _infer_nights(text)

    for ln in lines:
        low = ln.lower()
        if re.match(r"^meal plan:", ln, re.I):
            meal_plan = ln.split(":", 1)[-1].strip()
            continue
        if re.match(r"^stay nights:", ln, re.I):
            nights_label = ln.split(":", 1)[-1].strip()
            continue
        city_match = re.match(r"^([A-Za-z /]+):\s*(.+)$", ln)
        if city_match:
            city = city_match.group(1).strip()
            hotel_info = city_match.group(2).strip()
            city_locations.append(city)
            city_hotels.append(hotel_info)
            continue
        if re.search(r"\bmapai\b|\bapai\b|\bcpai\b|all inclusive|full board|bespoke", low):
            meal_plan = ln
            continue

    if not city_hotels:
        return None

    name = city_hotels[0].split("(")[0].strip()
    if len(city_hotels) > 1:
        name = " | ".join(h.split("(")[0].strip() for h in city_hotels)
    location = " | ".join(city_locations) if city_locations else "Multi-city Haryana"
    pipe_desc = " | ".join(city_hotels)
    desc = f"OPTION {num:02d} – {category.upper()}: {pipe_desc} | {meal_plan}"

    return {
        "sort_order": num,
        "category": category,
        "name": name,
        "location": location,
        "nights_label": nights_label,
        "room_type": room_type,
        "meal_plan": meal_plan,
        "stars": 5 if "ultra" in category.lower() else 4,
        "description": desc,
    }


def parse_hotel_options(text: str) -> list[dict]:
    section_m = re.search(
        r"(?:HANDPICKED(?: PREMIUM)?(?: LUXURY)?(?: MICE )?(?:CORPORATE )?\s+(?:ACCOMMODATION OPTIONS|ACCOMMODATIONS|"
        r"HOTEL OPTIONS|HOTEL ACCOMMODATIONS|PREMIUM HOTEL TIERS|LUXURY ACCOMMODATION MATRIX|"
        r"PREMIUM ACCOMMODATIONS & HANDPICKED HOTELS|PREMIUM CORPORATE HOTEL OPTIONS)|"
        r"HOTEL OPTIONS SECTION)\s*(.+?)(?:PACKAGE INCLUSIONS|PACKAGE INCLUSION|Package Inclusions|PACKAGE TERMS)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_m:
        return []
    section = section_m.group(1)

    options: list[dict] = []

    for m in re.finditer(
        r"Option\s*0?(\d+)\s*[–-]\s*((?:Deluxe|Premium|Luxury|Ultra\s*\n?\s*Luxury|ULTRA\s*\n?\s*LUXURY))\s*\n(.+?)(?=Option\s*0?\d+\s*[–-]|OPTION\s*0?\d+\s*[–-]|PACKAGE INCLUSIONS|Package Inclusions|\Z)",
        section,
        re.DOTALL | re.IGNORECASE,
    ):
        num = int(m.group(1))
        category = _normalize_category(m.group(2))
        block = m.group(3).strip()
        if re.search(r"^[A-Za-z /]+:\s*", block, re.MULTILINE):
            parsed = _parse_multi_city_option(block, num, category, text)
            if parsed:
                options.append(parsed)
                continue
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        if len(lines) >= 3:
            name = lines[0]
            room_type = lines[1]
            meal_plan = lines[2]
            options.append(
                {
                    "sort_order": num,
                    "category": category,
                    "name": name,
                    "location": "Kurukshetra",
                    "nights_label": _infer_nights(text),
                    "room_type": room_type,
                    "meal_plan": meal_plan,
                    "stars": 5 if "ultra" in category.lower() else 4,
                    "description": f"OPTION {num:02d} – {category.upper()}: {name} | {room_type} | {meal_plan}",
                }
            )

    if options:
        return sorted(options, key=lambda x: x["sort_order"])[:4]

    # HR-002 style stacked tier blocks after table headers
    if not options:
        raw_lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
        start_idx = 0
        for idx, ln in enumerate(raw_lines):
            if re.match(r"^MEAL (?:STRATEGY|PLAN)$", ln, re.I):
                start_idx = idx + 1
                break
        block_lines = [
            ln
            for ln in raw_lines[start_idx:]
            if not re.match(
                r"^(TIER|CATEGORY|HOTEL|ROOM|MEAL|OPTION|Option|CATEGORY$|HOTEL OPTIONS|MEAL PLAN|ROOM CATEGORY)",
                ln,
                re.I,
            )
            and "→" not in ln
            and not ln.upper().startswith(("DAY ", "SIGHTSEEING", "OVERNIGHT", "MEALS ", "ROUTE", "VEHICLE"))
        ]
        chunks: list[list[str]] = []
        current: list[str] = []
        for ln in block_lines:
            if re.match(r"^(Luxury|Deluxe|Premium|Ultra)", ln, re.I) and current:
                chunks.append(current)
                current = [ln]
            else:
                current.append(ln)
        if current:
            chunks.append(current)
        category_cycle = ["Luxury", "Deluxe", "Premium", "Ultra Luxury"]
        for idx, chunk in enumerate(chunks[:4], 1):
            if len(chunk) < 3:
                continue
            category = _normalize_category(chunk[0].replace("/", " ").split()[0] if chunk[0] else category_cycle[idx - 1])
            if "ultra" in " ".join(chunk).lower():
                category = "Ultra Luxury"
            elif "luxury" in chunk[0].lower():
                category = "Luxury"
            elif "deluxe" in chunk[0].lower():
                category = "Deluxe"
            name = next((ln for ln in chunk if "/" in ln or "Hotel" in ln or "Castle" in ln or "Resort" in ln), chunk[1] if len(chunk) > 1 else chunk[0])
            room_type = next((ln for ln in chunk if re.search(r"room|suite|villa", ln, re.I)), "Deluxe Room")
            meal_parts = [ln for ln in chunk if re.search(r"breakfast|dinner|map|apai|cpai|inclusive", ln, re.I)]
            meal_plan = re.sub(r"\s+", " ", " ".join(meal_parts)) if meal_parts else "MAPAI (Breakfast & Dinner)"
            meal_plan = meal_plan[:128]
            room_type = room_type[:128]
            name = name[:128]
            options.append(
                {
                    "sort_order": idx,
                    "category": category,
                    "name": name,
                    "location": "Kurukshetra",
                    "nights_label": _infer_nights(text),
                    "room_type": room_type,
                    "meal_plan": meal_plan,
                    "stars": 5 if "ultra" in category.lower() or category == "Luxury" else 4,
                    "description": f"OPTION {idx:02d} – {category.upper()}: {name} | {room_type} | {meal_plan}",
                }
            )

    if options:
        return sorted(options, key=lambda x: x["sort_order"])[:4]

    # HR-002 style tier rows with pipe separators
    tier_rows = []
    for ln in section.splitlines():
        ln = ln.strip()
        if not ln or ln.upper().startswith(("TIER", "CATEGORY", "HOTEL", "ROOM", "MEAL")):
            continue
        if "|" in ln:
            tier_rows.append(ln)
    if tier_rows:
        category_map = {
            1: "Luxury",
            2: "Deluxe",
            3: "Premium",
            4: "Ultra Luxury",
        }
        for idx, row in enumerate(tier_rows[:4], 1):
            parts = [p.strip() for p in row.split("|")]
            if len(parts) >= 4:
                tier_label, name, room_type, meal_plan = parts[0], parts[1], parts[2], parts[3]
                category = _normalize_category(tier_label.split("/")[0])
            elif len(parts) == 3:
                category = category_map.get(idx, "Premium")
                name, room_type, meal_plan = parts[0], parts[1], parts[2]
            else:
                continue
            options.append(
                {
                    "sort_order": idx,
                    "category": category,
                    "name": name,
                    "location": "Kurukshetra",
                    "nights_label": _infer_nights(text),
                    "room_type": room_type,
                    "meal_plan": meal_plan,
                    "stars": 5 if "ultra" in category.lower() or "luxury" in category.lower() else 4,
                    "description": f"OPTION {idx:02d} – {category.upper()}: {name} | {room_type} | {meal_plan}",
                }
            )
    if options:
        return sorted(options, key=lambda x: x["sort_order"])[:4]

    header_lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
    city_headers: list[str] = []
    for ln in header_lines[:12]:
        if (
            re.search(r"\(\d+N\)|Stay \(|Nights\)|NIGHTS \d|FOOTHILLS|GURUGRAM|KURUKSHETRA|CHANDIGARH|HISAR|Gurgaon|Resort", ln, re.I)
            and not _is_skip_line(ln)
        ):
            city_headers.append(re.sub(r"\s+", " ", ln))

    feature_re = re.compile(
        r"(mountain-facing|balcony|premium view|vvip|butler|wi-fi|health club|spa|conference|boardroom|mice|meal framework|senior-friendly|perks)",
        re.I,
    )

    for m in re.finditer(
        r"OPTION\s*0?(\d+)\s*[–-]\s*(DELUXE|PREMIUM|LUXURY|ULTRA\s*LUXURY)\s*\n(.+?)(?=OPTION\s*0?\d+\s*[–-]|PACKAGE INCLUSIONS|\Z)",
        section,
        re.DOTALL | re.IGNORECASE,
    ):
        num = int(m.group(1))
        category = _normalize_category(m.group(2))
        block = m.group(3).strip()
        if re.search(r"^[A-Za-z /]+:\s*", block, re.MULTILINE):
            parsed = _parse_multi_city_option(block, num, category, text)
            if parsed:
                options.append(parsed)
                continue
        lines = _normalize_hotel_block_lines(
            [ln.strip() for ln in block.splitlines() if ln.strip() and not _is_skip_line(ln)]
        )
        if not lines:
            continue

        hotel_parts: list[str] = []
        room_type = "Deluxe Room"
        meal_plan = "MAPAI (Breakfast & Dinner)"
        extras: list[str] = []
        feature_started = False

        for ln in lines:
            if feature_re.search(ln):
                feature_started = True
                extras.append(ln)
                continue
            if feature_started:
                extras.append(ln)
                continue
            low = ln.lower()
            if re.search(r"\bmapai\b|\bapai\b|\bcpai\b|full board|bespoke|all meals|gourmet all", low):
                meal_plan = ln
                continue
            if any(x in low for x in ["room", "suite", "villa", "wing", "chamber", "accommodation", "setup", "planner"]):
                room_type = ln
                continue
            hotel_parts.append(ln)

        if not hotel_parts:
            hotel_parts = [lines[0]]

        name = hotel_parts[0]
        pipe_desc = " | ".join(hotel_parts)
        location = " | ".join(city_headers[: len(hotel_parts)]) if city_headers else "Multi-city Haryana"
        desc = f"OPTION {num:02d} – {category.upper()}: {pipe_desc}"
        if extras:
            desc += f" | {' | '.join(extras[:2])}"

        options.append(
            {
                "sort_order": num,
                "category": category,
                "name": name,
                "location": location,
                "nights_label": _infer_nights(text),
                "room_type": room_type,
                "meal_plan": meal_plan,
                "stars": 5 if "ultra" in category.lower() else 4,
                "description": desc,
            }
        )

    if options:
        return sorted(options, key=lambda x: x["sort_order"])[:4]

    return []


def parse_inclusions_exclusions(text: str) -> tuple[list[str], list[str]]:
    section_m = re.search(
        r"PACKAGE (?:INCLUSIONS(?: & EXCLUSIONS)?|TERMS & PRACTICAL SPECIFICATIONS)(.+?)(?:SPECIAL TRAGUIN|EXCLUSIVE TRAGUIN|SHOPPING|IMPORTANT)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    included: list[str] = []
    excluded: list[str] = []

    if section_m:
        included, excluded = _parse_inclusion_section(section_m.group(1))

    if not included and not excluded:
        alt = re.search(
            r"Package Inclusions\s*\nPackage Exclusions\s*\n(?:SPECIAL TRAGUIN HIGHLIGHTS.+?\n)?(.+?)(?:IMPORTANT GENERAL NOTES|IMPORTANT NOTES|\Z)",
            text,
            re.DOTALL | re.IGNORECASE,
        )
        if alt:
            included, excluded = _parse_marker_lines(alt.group(1))

    if included and not excluded:
        marker_exc = re.search(
            r"✘\s*\n(.+?)(?:IMPORTANT GENERAL NOTES|IMPORTANT NOTES|IMPORTANT TOUR|\Z)",
            text,
            re.DOTALL,
        )
        if marker_exc:
            _, excluded = _parse_marker_lines(marker_exc.group(1))

    return included, excluded


def _parse_inclusion_section(section: str) -> tuple[list[str], list[str]]:
    included: list[str] = []
    excluded: list[str] = []
    lines = [ln.strip() for ln in section.splitlines()]
    mode: str | None = None
    pending_marker: str | None = None
    current_item: list[str] = []

    def flush_item(target: list[str]) -> None:
        nonlocal current_item
        if current_item:
            item = re.sub(r"\s+", " ", " ".join(current_item)).strip()
            if item and len(item) > 5:
                target.append(item)
        current_item = []

    for line in lines:
        if line in {"✔", "✘"}:
            if mode == "inc":
                flush_item(included)
            elif mode == "exc":
                flush_item(excluded)
            mode = "inc" if line == "✔" else "exc"
            pending_marker = None
            continue
        if not line or line in {"•"}:
            continue
        if line.endswith("✔") or line.endswith("✘"):
            marker = "✔" if line.endswith("✔") else "✘"
            line = line[:-1].strip()
            if marker == "✔":
                flush_item(included)
                mode = "inc"
                current_item = [line] if line else []
            else:
                flush_item(excluded)
                mode = "exc"
                current_item = [line] if line else []
            continue
        if "PACKAGE INCLUSIONS" in line.upper() and "EXCLUSIONS" not in line.upper():
            flush_item(included)
            flush_item(excluded)
            mode = "inc"
            pending_marker = None
            current_item = []
            continue
        if "PACKAGE EXCLUSIONS" in line.upper():
            flush_item(included)
            mode = "exc"
            pending_marker = None
            current_item = []
            continue
        if line.upper().startswith("EXCLUSIVE SIGNATURE") or line.upper().startswith("LOCAL CULTURE"):
            flush_item(excluded)
            mode = None
            current_item = []
            continue
        if line.startswith("✔"):
            flush_item(included)
            mode = "inc"
            pending_marker = None
            current_item = [re.sub(r"^✔\s*", "", line).strip()]
            continue
        if line.startswith("✘"):
            flush_item(excluded)
            mode = "exc"
            pending_marker = None
            current_item = [re.sub(r"^✘\s*", "", line).strip()]
            continue
        if pending_marker == "✔":
            flush_item(included)
            mode = "inc"
            current_item = [line]
            pending_marker = None
            continue
        if pending_marker == "✘":
            flush_item(excluded)
            mode = "exc"
            current_item = [line]
            pending_marker = None
            continue
        if mode == "inc":
            current_item.append(line)
            if line.endswith("."):
                flush_item(included)
        elif mode == "exc":
            current_item.append(line)
            if line.endswith("."):
                flush_item(excluded)

    return _dedupe_items(included), _dedupe_items(excluded)


def _dedupe_items(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        item = re.sub(r"\s+", " ", item).strip()
        if item and item not in seen and len(item) > 5:
            seen.add(item)
            out.append(item)
    return out


def _parse_marker_lines(section: str) -> tuple[list[str], list[str]]:
    included: list[str] = []
    excluded: list[str] = []
    lines = [ln.strip() for ln in section.splitlines()]
    mode: str | None = None
    current: list[str] = []

    def flush(target: list[str]) -> None:
        nonlocal current
        if current:
            item = re.sub(r"\s+", " ", " ".join(current)).strip()
            if item and len(item) > 5 and not item.startswith("TRAGUIN"):
                target.append(item)
        current = []

    for line in lines:
        if line in {"✔", "✘"}:
            if mode == "inc":
                flush(included)
            elif mode == "exc":
                flush(excluded)
            mode = "inc" if line == "✔" else "exc"
            continue
        if not line or line.startswith("⭐") or line.startswith("SHOPPING"):
            continue
        if mode == "inc":
            current.append(line)
        elif mode == "exc":
            current.append(line)
        elif not mode and line and not line.startswith("Package"):
            mode = "inc"
            current.append(line)

    if mode == "inc":
        flush(included)
    elif mode == "exc":
        flush(excluded)
    return _dedupe_items(included), _dedupe_items(excluded)


def parse_signature_highlights(text: str) -> list[str]:
    section_m = re.search(
        r"(?:SPECIAL TRAGUIN(?: CORPORATE)? HIGHLIGHTS|EXCLUSIVE (?:TRAGUIN )?(?:SIGNATURE )?HIGHLIGHTS)(.+?)(?:SHOPPING|IMPORTANT NOTES|IMPORTANT TRAVEL|LOCAL SHOPPING|LOCAL CORPORATE|LOCAL CULTURE)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_m:
        return []
    section = section_m.group(1)
    highlights = []
    for line in section.splitlines():
        line = line.strip().lstrip("•⭐").strip()
        if line.startswith(
            (
                "TRAGUIN",
                "Curated by",
                "Premium Handpicked",
                "Personalized",
                "Luxury Transportation",
                "Exclusive Recommendations",
                "Signature Experience",
                "Shopping",
            )
        ):
            highlights.append(line)
    return highlights[:6]


def parse_shopping_notes(text: str) -> list[str]:
    parts = []
    shopping = re.search(
        r"(?:SHOPPING & LOCAL(?: EXPERIENCES| CULINARY| LIFESTYLE| CORPORATE GIFTING)?|LOCAL MARKETS|LOCAL CULTURE)(.+?)(?:IMPORTANT NOTES|IMPORTANT TRAVEL|IMPORTANT GENERAL|IMPORTANT TOUR|IMPORTANT TOUR GUIDELINES|IMPORTANT NOTES FOR)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if shopping:
        body = re.sub(r"\s+", " ", shopping.group(1).strip())
        if len(body) < 500:
            parts.append(body)
    notes = re.search(
        r"IMPORTANT (?:NOTES|GENERAL NOTES|TOUR GUIDELINES|NOTES & TRAVEL INFORMATION|NOTES & CORPORATE TERMS|NOTES & BOOKING INFORMATION)(?: FOR YOUR JOURNEY| & TRAVEL CONDITIONS)?(.+?)(?:TRAGUIN\s*$|PREMIUM TRAVEL|\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if notes:
        body = notes.group(1).strip()
        for ln in body.splitlines():
            ln = ln.strip().lstrip("•").strip()
            if ln and len(ln) < 200 and not ln.startswith("TRAGUIN") and "PREMIUM TRAVEL" not in ln:
                parts.append(ln)
    return parts[:4]


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
        f"State / Country: Haryana / India | Category: {category}",
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
    for day in days[:8]:
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
        f"{hotel['name']} ({hotel.get('location', 'Haryana')}) | {hotel['meal_plan']}"
    )
    name = hotel["name"][:128]
    location = (hotel.get("location") or "Haryana")[:128]
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
    func = f"build_hr_{num}"
    duration = re.sub(r"\s+", " ", extract_duration(text))
    slug = meta["slug"]
    itin_slug = f"{slug}-itinerary"
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = parse_day_blocks(text)
    hotels = meta.get("hotels") or parse_hotel_options(text)
    included, excluded = parse_inclusions_exclusions(raw_text)
    overview = extract_overview_sections(text)
    pkg_highlights = build_package_highlights({**meta, "serial": serial}, text)
    itin_highlights = build_itinerary_highlights(days, text)
    starting_price = extract_starting_price(text)
    tagline = title.split("•")[0].strip() if "•" in title else title

    if not hotels:
        hotels = [
            {
                "sort_order": 1,
                "category": "Deluxe",
                "name": "Hotel Kimaya / Similar",
                "location": "Kurukshetra",
                "nights_label": _infer_nights_from_duration(duration),
                "room_type": "Executive Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 4,
                "description": "OPTION 01 – DELUXE: Hotel Kimaya / Similar | Executive Room | MAPAI",
            },
            {
                "sort_order": 2,
                "category": "Premium",
                "name": "Hotel Red Castle / Divine Clerks",
                "location": "Kurukshetra",
                "nights_label": _infer_nights_from_duration(duration),
                "room_type": "Super Deluxe Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 4,
                "description": "OPTION 02 – PREMIUM: Hotel Red Castle / Divine Clerks | Super Deluxe Room | MAPAI",
            },
            {
                "sort_order": 3,
                "category": "Luxury",
                "name": "The Pearl Resort & Spa / Similar",
                "location": "Kurukshetra",
                "nights_label": _infer_nights_from_duration(duration),
                "room_type": "Luxury Suite",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 5,
                "description": "OPTION 03 – LUXURY: The Pearl Resort & Spa / Similar | Luxury Suite | MAPAI",
            },
            {
                "sort_order": 4,
                "category": "Ultra Luxury",
                "name": "Curated Heritage Boutique Farm & Wellness Villa",
                "location": "Kurukshetra",
                "nights_label": _infer_nights_from_duration(duration),
                "room_type": "Royal Club Villa",
                "meal_plan": "All Inclusive Premium Meals",
                "stars": 5,
                "description": "OPTION 04 – ULTRA LUXURY: Curated Heritage Boutique Farm & Wellness Villa | Royal Club Villa | All Inclusive",
            },
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
    if not inc_lines:
        inc_lines = [
            '            _inc_included("Premium accommodation at handpicked Haryana properties.", 1),',
            '            _inc_included("Private luxury vehicle for all transfers and sightseeing.", 2),',
            '            _inc_excluded("Airfare and personal expenses.", 3),',
        ]

    ph_lines = ",\n".join(f"            _ph({py_str(h)}, {i})" for i, h in enumerate(pkg_highlights, 1))
    ih_lines = ",\n".join(f"            _ih({py_str(h)}, {i})" for i, h in enumerate(itin_highlights, 1))
    mood_lines = ", ".join(py_str(m) for m in moods)
    seo_title = f"{serial} | {title.split('•')[0].strip()} | TRAGUIN"
    seo_desc = (
        f"Premium {duration} Haryana package ({serial} / {tour_code}): "
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
    header = '''"""Builder functions for HR-001 through HR-010 Haryana packages."""

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

HARYANA_SLUG = "haryana"


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

    builder_names = [f"build_hr_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nHARYANA_DOMESTIC_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
