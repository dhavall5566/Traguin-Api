#!/usr/bin/env python3
"""Generate himachal_domestic_batch_defs.py from tmp_hp_pdfs text sources."""

from __future__ import annotations

import re
from pathlib import Path

PDF_DIR = Path(__file__).resolve().parent.parent / "tmp_hp_pdfs"
OUT_PATH = Path(__file__).resolve().parent / "himachal_domestic_batch_defs.py"

PACKAGE_META: dict[str, dict] = {
    "HP-001": {
        "tour_code": "TRAGUIN-HP-SHIMLA-001",
        "slug": "hp-001-shimla-delight-family-getaway",
        "title": "Shimla Delight Family Getaway",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-002": {
        "tour_code": "TRG-HIM-002",
        "slug": "hp-002-shimla-extended-alpine-luxury-timeless-ridges",
        "title": "Shimla Extended • Alpine Luxury & Timeless Ridges",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-003": {
        "tour_code": "TRG-HP-003",
        "slug": "hp-003-shimla-manali-classic-alpine-luxury",
        "title": "Shimla Manali Classic • Alpine Luxury & Escapes",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-004": {
        "tour_code": "TRG-HIM-004",
        "slug": "hp-004-shimla-manali-dharamshala-explorer",
        "title": "Shimla • Manali • Dharamshala Explorer",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-005": {
        "tour_code": "TRG-HP-005",
        "slug": "hp-005-complete-himachal-grand-alpine-escape",
        "title": "Complete Himachal • Grand Alpine Escape",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-006": {
        "tour_code": "TRG-HIM-006",
        "slug": "hp-006-romantic-himachal-honeymoon",
        "title": "Romantic Himachal • Love Amidst the Snow-Capped Peaks",
        "moods": ["Romantic", "Luxury", "Nature"],
    },
    "HP-007": {
        "tour_code": "TRG-HP-HON-007",
        "slug": "hp-007-snow-romance-manali-honeymoon",
        "title": "Snow Romance Manali Honeymoon Special",
        "moods": ["Romantic", "Luxury", "Nature"],
    },
    "HP-008": {
        "tour_code": "TRG-HIM-008",
        "slug": "hp-008-luxury-manali-escape-romance-amidst-the-clouds",
        "title": "Luxury Manali Escape • Romance Amidst the Clouds",
        "moods": ["Romantic", "Luxury", "Nature"],
    },
    "HP-009": {
        "tour_code": "TRG-HIM-009",
        "slug": "hp-009-girls-trip-manali",
        "title": "Girls Trip Manali • Wanderlust, Luxury & Sisterhood",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-010": {
        "tour_code": "TRG-HIM-010",
        "slug": "hp-010-relaxed-shimla-escape",
        "title": "Relaxed Shimla Escape • Elegance & Leisure at a Gentle Pace",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-011": {
        "tour_code": "TRG-SPI-011",
        "slug": "hp-011-spiti-valley-explorer",
        "title": "Spiti Explorer • Journey to the Middle Land",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-012": {
        "tour_code": "TRG-KAZA-012",
        "slug": "hp-012-premium-kaza-expedition",
        "title": "Premium Kaza Expedition",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-013": {
        "tour_code": "TRG-HIM-013",
        "slug": "hp-013-luxury-himachal-retreat",
        "title": "Luxury Himachal Retreat • Grand Heritage & High Alpine Escape",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-014": {
        "tour_code": "TRG-OB-HP-014",
        "slug": "hp-014-oberoi-himachal-experience",
        "title": "The Oberoi Himachal Experience • Royalty Reimagined",
        "moods": ["Luxury", "Romantic", "Family"],
    },
    "HP-015": {
        "tour_code": "TRG-HIM-MICE-015",
        "slug": "hp-015-corporate-himachal-mice",
        "title": "Corporate Himachal • Elevation, Leadership & Synergy",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-016": {
        "tour_code": "TRG-HIM-ED016",
        "slug": "hp-016-educational-himachal-tour",
        "title": "Educational Himachal Tour",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-017": {
        "tour_code": "TRG-HP-017",
        "slug": "hp-017-dharamshala-escape",
        "title": "Dharamshala Escape • Serenity, Spirituality & Peaks",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-018": {
        "tour_code": "TRG-HP-018",
        "slug": "hp-018-shimla-kasol-delight",
        "title": "Shimla Kasol Delight • The Royal Ridge to the Mystic Valley",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-019": {
        "tour_code": "TRG-HIM-019",
        "slug": "hp-019-manali-dharamshala-family",
        "title": "Manali & Dharamshala Family Explorer",
        "moods": ["Family", "Luxury", "Nature"],
    },
    "HP-020": {
        "tour_code": "TRG-HIM-PAN-020",
        "slug": "hp-020-himachal-panorama",
        "title": "Himachal Panorama • The Ultimate Luxury Alpine Journey",
        "moods": ["Family", "Luxury", "Nature"],
    },
}

BUILDER_ORDER = [f"HP-{i:03d}" for i in range(1, 21)]

FOOTER_RE = re.compile(
    r"TRAGUIN(?: Premium Luxury(?: Holidays| Itinerary| Family Vacations|MICE| Proposal| Corporate Itinerary)?|"
    r" Luxury Proposal| Educational Luxury Proposal| Premium Romantic Himachal Itinerary|"
    r" Premium Luxury Family Itinerary| Premium Luxury Proposal| Premium Corporate Itinerary)"
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


def clean_raw(text: str) -> str:
    text = FOOTER_RE.sub("", text)
    text = PAGE_RE.sub("", text)
    text = TAGLINE_RE.sub("", text)
    text = QUOTE_RE.sub("", text)
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
    return m.group(1).strip() if m else "03 Nights / 04 Days"


def extract_category(text: str) -> str:
    m = re.search(
        r"CATEGORY:\s*\n(.+?)(?:\nTRAGUIN|\nDURATION|\nBEST|\nIDEAL|\nSTARTING|\nDESTINATIONS|\nVEHICLE|\nTOUR|\n[A-Z]{2,})",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "Premium Himachal Tour"


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
            if re.match(r"^(IDEAL FOR|BEST SEASON|STARTING PRICE|TRAGUIN TOUR|VEHICLE|TOUR OVERVIEW|DURATION|CATEGORY):", stripped, re.I):
                break
            parts.append(stripped)
    if parts:
        return re.sub(r"\s+", " ", " ".join(parts))
    return "Himachal Pradesh"


def extract_ideal_for(text: str) -> str:
    m = re.search(
        r"IDEAL FOR:\s*\n(.+?)(?:\nSTARTING|\nBEST|\nTRAGUIN TOUR|\nVEHICLE|\nTOUR|\nTRAGUIN PREMIUM|\n[A-Z]{3,}-\d{3})",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "Luxury Travelers"


def extract_best_season(text: str) -> str:
    m = re.search(
        r"BEST SEASON:\s*\n(.+?)(?:\nDESTINATIONS|\nIDEAL|\nSTARTING|\nTRAGUIN TOUR|\nVEHICLE|\nTOUR|\nTRAGUIN PREMIUM|\n[A-Z]{3,}-\d{3})",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "March to June"


def extract_starting_price(text: str) -> str:
    m = re.search(
        r"STARTING PRICE:\s*\n(.+?)(?:\nTRAGUIN TOUR|\nVEHICLE|\nTOUR OVERVIEW|\nTRAGUIN PREMIUM|\n[A-Z]{3,}-\d{3})",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "On Request"


def extract_vehicle_meals(text: str) -> str:
    for label in ("VEHICLE & MEALS:", "VEHICLE / MEALS:", "VEHICLE / MEAL PLAN:", "VEHICLE PLAN:"):
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
                r"^(TRAGUIN|TOUR OVERVIEW|DURATION|DESTINATIONS|IDEAL FOR|BEST SEASON|STARTING PRICE|TRAGUIN TOUR|DETAILED|DAY-WISE|DAY 0|ROUTE)",
                stripped,
                re.I,
            ):
                break
            lines.append(stripped)
        if lines:
            return re.sub(r"\s+", " ", " ".join(lines))
    return "Private Luxury SUV / MAPAI"


def extract_route(text: str) -> str:
    m = re.search(
        r"ROUTE(?: MAP| PLAN)?:\s*\n(.+?)(?:\nTRAGUIN|\nWHY CHOOSE|\nDETAILED|\nDAY-WISE|\nDAY 0)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return ""


def extract_overview_sections(text: str) -> str:
    parts: list[str] = []
    welcome = re.search(
        r"(?:TRAGUIN PREMIUM[^\n]+\n[^\n]+\n|Welcome(?: Note)?:[^\n]+\n|Dear Educators[^\n]+\n)(.+?)(?:\nTOUR OVERVIEW|\nWHY CHOOSE|\nWHY BOOK|\nWHY VISIT|\nDETAILED|\nDAY-WISE|\nDAY 0)",
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

    why_patterns = [
        "WHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE?",
        "WHY CHOOSE A LUXURY SHIMLA FAMILY TOUR?",
        "WHY BOOK A PREMIUM SHIMLA EXTENDED HOLIDAY?",
        "WHY BOOK THE BEST HIMACHAL TOUR PACKAGE?",
        "WHY CHOOSE THE BEST HIMACHAL HONEYMOON PACKAGE?",
        "WHY BOOK THE BEST HIMACHAL HONEYMOON PACKAGE?",
        "WHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE FOR A GIRLS' TRIP?",
        "WHY CHOOSE THE BEST SHIMLA TOUR PACKAGE?",
        "WHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE TO SPITI VALLEY?",
        "WHY BOOK A PREMIUM HIMACHAL EXPERIENCE?",
        "WHY VISIT HIMACHAL WITH THE BEST HIMACHAL TOUR PACKAGE?",
        "WHY CHOOSE CORPORATE HIMACHAL FOR YOUR NEXT MICE EVENT?",
        "WHY CHOOSE THE BEST HIMACHAL TOUR PACKAGE FOR SCHOOLS?",
        "WHY CHOOSE THE BEST DHARAMSHALA TOUR PACKAGE?",
        "WHY VISIT DESTINATION: THE PREMIUM HIMACHAL EXPERIENCE",
    ]
    for heading in why_patterns:
        m = re.search(
            rf"{re.escape(heading)}\s*\n(.+?)(?:\nDETAILED|\nDAY-WISE|\nDAY 0|\nHANDPICKED|\nPREMIUM ACCOMMODATION)",
            text,
            re.DOTALL | re.IGNORECASE,
        )
        if m:
            body = re.sub(r"\s+", " ", m.group(1).strip())
            parts.append(f"{heading}\n{body}")
            break

    seo = re.search(
        r"DESTINATION SEO CONTENT\s*\n(.+?)(?:\nDAY WISE|\nDAY-WISE|\nHANDPICKED)",
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
    if not start:
        return []
    section = text[start.end():]
    end = re.search(
        r"(?m)^HANDPICKED (?:LUXURY )?(?:PREMIUM )?(?:MICE )?(?:ACCOMMODATION|HOTEL)|"
        r"^PREMIUM ACCOMMODATION TIERS|^HANDPICKED PREMIUM ACCOMMODATION|^HANDPICKED ACCOMMODATION",
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


    return bool(
        re.match(
            r"^(Category|Option Level|OPTION|Option Tier|Meal Plan|Room Category|Key Included|Conference|Corporate Meal|Room Style|Senior-Friendly|HONEYMOON ADD-ONS|Shimla|Manali|Dharamshala|Dalhousie|Kasol|Kaza|Kalpa|Chandratal|Extended|Category)$",
            ln,
            re.I,
        )
        or re.match(r"^\(\d+N\)$", ln)
        or re.match(r"^\d+N\)$", ln)
    )


def parse_hotel_options(text: str) -> list[dict]:
    section_m = re.search(
        r"(?:HANDPICKED(?: PREMIUM)?(?: LUXURY)?(?: MICE)? )?(?:ACCOMMODATION OPTIONS|HOTEL ACCOMMODATIONS|ACCOMMODATION OPTIONS \(SCHOOL GROUP GRID\)|PREMIUM HOTEL TIERS|LUXURY ACCOMMODATION MATRIX)(.+?)(?:PACKAGE INCLUSIONS|PACKAGE INCLUSION)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_m:
        return []
    section = section_m.group(1)

    # Single-location Option 01 – Deluxe blocks (HP-001 style)
    options: list[dict] = []
    for m in re.finditer(
        r"Option\s*0?(\d+)\s*[–-]\s*(Deluxe|Premium|Luxury|Ultra\s*Luxury|ULTRA\s*LUXURY)\s*\n(.+?)(?=Option\s*0?\d+\s*[–-]|OPTION\s*0?\d+\s*[–-]|PACKAGE INCLUSIONS|\Z)",
        section,
        re.DOTALL | re.IGNORECASE,
    ):
        num = int(m.group(1))
        category = _normalize_category(m.group(2))
        block = m.group(3).strip()
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
                    "location": "Himachal Pradesh",
                    "nights_label": _infer_nights(text),
                    "room_type": room_type,
                    "meal_plan": meal_plan,
                    "stars": 5 if "ultra" in category.lower() else 4,
                    "description": f"OPTION {num:02d} – {category.upper()}: {name} | {room_type} | {meal_plan}",
                }
            )

    if options:
        return sorted(options, key=lambda x: x["sort_order"])[:4]

    # Table-style OPTION 01 – DELUXE with multi-city columns
    header_lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
    city_headers: list[str] = []
    for ln in header_lines[:8]:
        if re.search(r"\(\d+N\)|Stay \(|Nights\)|Resort \(|Hotels \(", ln, re.I) and not _is_skip_line(ln):
            city_headers.append(re.sub(r"\s+", " ", ln))

    feature_re = re.compile(
        r"(mountain-facing|balcony rooms|premium view|vvip|butler|wi-fi|health club|spa credit|guided walk|heated pool|conference hall|audio|broadband|meal layout|room style|honeymoon add|key included|corporate meal|meal framework|senior-friendly)",
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
            low = ln.lower()
            if feature_re.search(ln):
                feature_started = True
                extras.append(ln)
                continue
            if feature_started:
                extras.append(ln)
                continue
            if re.search(r"\bmapai\b", low) or "full board" in low or re.search(r"\bapai\b", low) or re.search(r"\bapex\b", low) or "bespoke signature" in low or "culinary plan" in low:
                meal_plan = ln
                continue
            if any(x in low for x in ["room", "suite", "villa", "chalet", "cottage", "layout", "wing", "chamber", "accommodation", "setup"]):
                room_type = ln
                continue
            hotel_parts.append(ln)

        if not hotel_parts:
            hotel_parts = [lines[0]]

        name = hotel_parts[0]
        pipe_desc = " | ".join(hotel_parts)
        location = " | ".join(city_headers[: len(hotel_parts)]) if city_headers else "Multi-city Himachal"
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

    return sorted(options, key=lambda x: x["sort_order"])[:4]


def parse_inclusions_exclusions(text: str) -> tuple[list[str], list[str]]:
    section_m = re.search(
        r"PACKAGE INCLUSIONS(?: & EXCLUSIONS)?(.+?)(?:SPECIAL TRAGUIN|EXCLUSIVE TRAGUIN|SHOPPING|IMPORTANT)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_m:
        return [], []
    section = section_m.group(1)
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
        if not line or line in {"✔", "✘", "•"}:
            if line in {"✔", "✘"}:
                pending_marker = line
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
        elif mode == "exc":
            current_item.append(line)

    if mode == "inc":
        flush_item(included)
    elif mode == "exc":
        flush_item(excluded)

    def dedupe(items: list[str]) -> list[str]:
        seen = set()
        out = []
        for item in items:
            item = re.sub(r"\s+", " ", item).strip()
            if item and item not in seen and len(item) > 5:
                seen.add(item)
                out.append(item)
        return out

    return dedupe(included), dedupe(excluded)


def parse_signature_highlights(text: str) -> list[str]:
    section_m = re.search(
        r"(?:SPECIAL TRAGUIN(?: CORPORATE)? HIGHLIGHTS|EXCLUSIVE TRAGUIN SIGNATURE HIGHLIGHTS)(.+?)(?:SHOPPING|IMPORTANT NOTES|IMPORTANT TRAVEL|LOCAL SHOPPING|LOCAL CORPORATE)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_m:
        return []
    section = section_m.group(1)
    highlights = []
    for line in section.splitlines():
        line = line.strip().lstrip("•").strip()
        if line.startswith(("TRAGUIN", "Curated by", "Premium Handpicked", "Personalized", "Luxury Transportation", "Exclusive Recommendations", "Shopping")):
            highlights.append(line)
    return highlights[:6]


def parse_shopping_notes(text: str) -> list[str]:
    parts = []
    shopping = re.search(
        r"(?:SHOPPING & LOCAL(?: EXPERIENCES| CULINARY| CORPORATE GIFTING)?|LOCAL MARKETS)(.+?)(?:IMPORTANT NOTES|IMPORTANT TRAVEL|IMPORTANT NOTES FOR)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if shopping:
        body = re.sub(r"\s+", " ", shopping.group(1).strip())
        if len(body) < 500:
            parts.append(body)
    notes = re.search(
        r"IMPORTANT NOTES(?: & TRAVEL INFORMATION| FOR YOUR JOURNEY| & TRAVEL CONDITIONS)?(.+?)(?:TRAGUIN\s*$|PREMIUM TRAVEL|\Z)",
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
        f"State / Country: Himachal Pradesh / India | Category: {category}",
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
    for i, day in enumerate(days[:8], 1):
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
        f"{hotel['name']} ({hotel.get('location', 'Himachal Pradesh')}) | {hotel['meal_plan']}"
    )
    return f"""            _hotel(
                {py_str(hotel['name'])},
                {py_str(hotel.get('location') or 'Himachal Pradesh')},
                {py_str(nights)},
                {py_str(hotel['category'])},
                {py_str(hotel['room_type'])},
                {py_str(hotel['meal_plan'])},
                {hotel['stars']},
                {hotel['sort_order']},
                description={py_str(desc)},
            )"""


def emit_builder(serial: str, meta: dict, text: str, raw_text: str) -> str:
    num = serial.split("-")[1]
    func = f"build_hp_{num}"
    duration = extract_duration(text)
    slug = meta["slug"]
    itin_slug = f"{slug}-itinerary"
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = parse_day_blocks(text)
    hotels = parse_hotel_options(text)
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
                "name": "Hotel Willow Banks / Similar",
                "location": "Himachal Pradesh",
                "nights_label": _infer_nights_from_duration(duration),
                "room_type": "Deluxe Valley View Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 4,
                "description": "OPTION 01 – DELUXE: Hotel Willow Banks / Similar | Deluxe Valley View Room | MAPAI",
            },
            {
                "sort_order": 2,
                "category": "Premium",
                "name": "Radisson Hotel Shimla / Similar",
                "location": "Himachal Pradesh",
                "nights_label": _infer_nights_from_duration(duration),
                "room_type": "Premium Balcony Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 4,
                "description": "OPTION 02 – PREMIUM: Radisson Hotel Shimla / Similar | Premium Balcony Room | MAPAI",
            },
            {
                "sort_order": 3,
                "category": "Luxury",
                "name": "The Oberoi Cecil / Similar",
                "location": "Himachal Pradesh",
                "nights_label": _infer_nights_from_duration(duration),
                "room_type": "Luxury Suite",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 5,
                "description": "OPTION 03 – LUXURY: The Oberoi Cecil / Similar | Luxury Suite | MAPAI",
            },
            {
                "sort_order": 4,
                "category": "Ultra Luxury",
                "name": "Wildflower Hall, An Oberoi Resort",
                "location": "Himachal Pradesh",
                "nights_label": _infer_nights_from_duration(duration),
                "room_type": "Premier Mountain View Suite",
                "meal_plan": "Bespoke Signature MAPAI",
                "stars": 5,
                "description": "OPTION 04 – ULTRA LUXURY: Wildflower Hall, An Oberoi Resort | Premier Mountain View Suite | Bespoke MAPAI",
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
            '            _inc_included("Premium accommodation at handpicked Himachal properties.", 1),',
            '            _inc_included("Private luxury vehicle for all transfers and sightseeing.", 2),',
            '            _inc_excluded("Airfare and personal expenses.", 3),',
        ]

    ph_lines = ",\n".join(f"            _ph({py_str(h)}, {i})" for i, h in enumerate(pkg_highlights, 1))
    ih_lines = ",\n".join(f"            _ih({py_str(h)}, {i})" for i, h in enumerate(itin_highlights, 1))
    mood_lines = ", ".join(py_str(m) for m in moods)
    seo_title = f"{serial} | {title.split('•')[0].strip()} | TRAGUIN"
    seo_desc = (
        f"Premium {duration} Himachal Pradesh package ({serial} / {tour_code}): "
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
{",".join(day_lines)}
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
    header = '''"""Builder functions for HP-001 through HP-020 Himachal Pradesh packages."""

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

HIMACHAL_SLUG = "himachal"


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

    builder_names = [f"build_hp_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nHIMACHAL_DOMESTIC_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
