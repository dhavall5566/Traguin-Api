#!/usr/bin/env python3
"""Generate goa_domestic_batch_defs.py from tmp_ga_pdfs text sources."""

from __future__ import annotations

import re
from pathlib import Path

from _goa_hotels_data import GOA_HOTELS

PDF_DIR = Path(__file__).resolve().parent.parent / "tmp_ga_pdfs"
OUT_PATH = Path(__file__).resolve().parent / "goa_domestic_batch_defs.py"

PACKAGE_META: dict[str, dict] = {
    "GA-001": {
        "tour_code": "TRAGUIN-GA-001",
        "slug": "ga-001-premium-romantic-goa-escape",
        "title": "TRAGUIN Premium Romantic Goa Escape",
        "moods": ["Romantic", "Beach", "Luxury"],
    },
    "GA-002": {
        "tour_code": "TRAGUIN-GA-002",
        "slug": "ga-002-goa-family-fun",
        "title": "TRAGUIN Premium Goa Family Tour Package",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-003": {
        "tour_code": "TRAGUIN-GA-003",
        "slug": "ga-003-girls-trip-goa-package",
        "title": "TRAGUIN Premium Girls Trip Goa Package",
        "moods": ["Beach", "Luxury", "Romantic"],
    },
    "GA-004": {
        "tour_code": "TRAGUIN-GA-004",
        "slug": "ga-004-luxury-south-goa-private-sanctuary",
        "title": "TRAGUIN Premium Goa Tour Package — Luxury South Goa Private Sanctuary",
        "moods": ["Luxury", "Beach", "Romantic", "Family"],
    },
    "GA-005": {
        "tour_code": "TRAGUIN-GA-005-LUX",
        "slug": "ga-005-leisure-goa-senior-citizens",
        "title": "TRAGUIN Premium Goa Tour Package — Leisure Goa for Senior Citizens",
        "moods": ["Family", "Luxury", "Beach"],
    },
    "GA-006": {
        "tour_code": "TRG-GOA-006",
        "slug": "ga-006-north-south-goa-highlights",
        "title": "TRAGUIN Premium Goa Tour Package — North & South Goa Highlights",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-007": {
        "tour_code": "TRG-GOA-007",
        "slug": "ga-007-complete-goa-explorer",
        "title": "TRAGUIN Premium Goa Tour Package — Complete Goa Explorer",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-008": {
        "tour_code": "TRG-GOA-008",
        "slug": "ga-008-sunny-goa-vacation",
        "title": "TRAGUIN Premium Goa Tour Package — Sunny Goa Vacation",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-009": {
        "tour_code": "TRG-GOA-009",
        "slug": "ga-009-beaches-and-heritage-special",
        "title": "TRAGUIN Premium Goa Tour Package — Beaches and Heritage Special",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-010": {
        "tour_code": "TRG-GOA-010",
        "slug": "ga-010-grand-goan-experience",
        "title": "TRAGUIN Premium Goa Tour Package — Grand Goan Experience",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-012": {
        "tour_code": "TRG-GOA-012",
        "slug": "ga-012-exotic-goa-honeymoon",
        "title": "TRAGUIN Premium Goa Tour Package — Exotic Goa Honeymoon",
        "moods": ["Romantic", "Beach", "Luxury"],
    },
    "GA-013": {
        "tour_code": "TRG-GOA-013",
        "slug": "ga-013-luxury-sunset-romance-honeymoon",
        "title": "TRAGUIN Premium Goa Tour Package — Luxury Sunset Romance Honeymoon Escape",
        "moods": ["Romantic", "Beach", "Luxury"],
    },
    "GA-014": {
        "tour_code": "TRG-GOA-014",
        "slug": "ga-014-girls-trip-to-goa",
        "title": "TRAGUIN Premium Goa Tour Package — Girls Trip to Goa",
        "moods": ["Beach", "Luxury", "Romantic"],
    },
    "GA-015": {
        "tour_code": "TRG-GOA-015",
        "slug": "ga-015-relaxed-old-goa-temples",
        "title": "TRAGUIN Premium Goa Tour Package — Relaxed Old Goa & Temples",
        "moods": ["Family", "Luxury", "Beach"],
    },
    "GA-016": {
        "tour_code": "TRG-GOA-016",
        "slug": "ga-016-water-sports-scuba-adventure",
        "title": "TRAGUIN Premium Goa Tour Package — Water Sports & Scuba Adventure",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-017": {
        "tour_code": "TRG-GOA-017",
        "slug": "ga-017-dudhsagar-trek-backwater-safari",
        "title": "TRAGUIN Premium Goa Tour Package — Dudhsagar Trek & Backwater Safari",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-018": {
        "tour_code": "TRG-GOA-018",
        "slug": "ga-018-taj-heritage-luxury-retreat",
        "title": "TRAGUIN Premium Goa Tour Package — Taj & Heritage Luxury Retreat",
        "moods": ["Luxury", "Romantic", "Family", "Beach"],
    },
    "GA-019": {
        "tour_code": "TRG-GOA-019",
        "slug": "ga-019-premium-villa-private-yacht",
        "title": "TRAGUIN Premium Goa Tour Package — Premium Villa & Private Yacht Experience",
        "moods": ["Luxury", "Romantic", "Family", "Beach"],
    },
    "GA-020": {
        "tour_code": "TRG-GOA-MICE-020",
        "slug": "ga-020-corporate-beach-meet-mice",
        "title": "TRAGUIN Premium Goa Tour Package — Corporate Beach Meet MICE",
        "moods": ["Luxury", "Beach", "Family"],
    },
    "GA-021": {
        "tour_code": "TRG-GOA-021",
        "slug": "ga-021-educational-history-science-tour",
        "title": "TRAGUIN Premium Goa Tour Package — Educational History & Science Tour",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-022": {
        "tour_code": "TRG-GA-022",
        "slug": "ga-022-south-goa-portuguese-heritage",
        "title": "TRAGUIN Premium Goa Tour Package — South Goa Portuguese Heritage",
        "moods": ["Family", "Luxury", "Beach"],
    },
    "GA-023": {
        "tour_code": "TRG-GOA-023",
        "slug": "ga-023-fun-sun-coastal-delight",
        "title": "TRAGUIN Premium Goa Tour Package — Fun & Sun Coastal Delight",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-024": {
        "tour_code": "TRG-GOA-024",
        "slug": "ga-024-dudhsagar-spice-plantation-family",
        "title": "TRAGUIN Premium Goa Tour Package — Dudhsagar Waterfalls & Spice Plantation Family Escape",
        "moods": ["Family", "Beach", "Luxury"],
    },
    "GA-025": {
        "tour_code": "TRG-GOA-025",
        "slug": "ga-025-ultimate-goa-panorama",
        "title": "TRAGUIN Ultimate Goa Panorama — Best Goa Tour Package",
        "moods": ["Family", "Beach", "Luxury", "Romantic"],
    },
}

BUILDER_ORDER = [
    "GA-001", "GA-002", "GA-003", "GA-004", "GA-005", "GA-006", "GA-007", "GA-008",
    "GA-009", "GA-010", "GA-012", "GA-013", "GA-014", "GA-015", "GA-016", "GA-017",
    "GA-018", "GA-019", "GA-020", "GA-021", "GA-022", "GA-023", "GA-024", "GA-025",
]

FOOTER_RE = re.compile(
    r"TRAGUIN(?: Premium Luxury(?: Holidays| Itinerary| Family Vacations|MICE| Proposal)?|"
    r" Grand Goan Experience| Ultimate Goa Panorama| Educational Luxury Proposal| Luxury Proposal)"
    r"[^\n]*\n\d+\s*\n?",
    re.IGNORECASE,
)
PAGE_RE = re.compile(r"Page \d+ of \d+\s*\n?", re.IGNORECASE)
TAGLINE_RE = re.compile(
    r"PREMIUM TRAVEL \| LUXURY HOLIDAYS \| CORPORATE MICE \| HONEYMOON EXPERTS \| FAMILY\s*VACATIONS\s*",
    re.IGNORECASE,
)
QUOTE_RE = re.compile(r'"Creating Memories Beyond Destinations"\s*', re.IGNORECASE)
BULLET_ONLY_RE = re.compile(r"^[\s•✔✘]+$", re.MULTILINE)


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
    m = re.search(r"CATEGORY:\s*\n(.+?)(?:\nTRAGUIN|\nDURATION|\nBEST|\nIDEAL|\nSTARTING|\nDESTINATIONS|\nVEHICLE|\nTOUR|\n[A-Z]{2,})", text, re.DOTALL | re.IGNORECASE)
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return "Premium Goa Tour"


def extract_destinations(text: str) -> str:
    for pat in [
        r"DESTINATIONS(?: COVERED)?:\s*\n(.+?)(?:\nIDEAL|\nBEST|\nSTARTING|\nTRAGUIN TOUR|\nVEHICLE|\nTOUR OVERVIEW|\n[A-Z]{2,} )",
        r"DESTINATIONS:\s*\n(.+?)(?:\nIDEAL|\nBEST|\nSTARTING|\nTRAGUIN TOUR|\nVEHICLE|\nTOUR OVERVIEW)",
    ]:
        m = re.search(pat, text, re.DOTALL | re.IGNORECASE)
        if m:
            return re.sub(r"\s+", " ", m.group(1).strip())
    return "North Goa • South Goa"


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
    return "October to April"


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
    for pat in [
        r"VEHICLE(?: PLAN| & MEALS| / MEALS)?:\s*\n(.+?)(?:\nTRAGUIN PREMIUM|\nTRAGUIN TOUR|\nTOUR OVERVIEW|\nBEST GOA|\n[A-Z]{2,} )",
        r"VEHICLE / MEALS:\s*\n(.+?)(?:\nTRAGUIN|\nTOUR OVERVIEW)",
    ]:
        m = re.search(pat, text, re.DOTALL | re.IGNORECASE)
        if m:
            return re.sub(r"\s+", " ", m.group(1).strip())
    return "Private Luxury AC Vehicle / CP or MAPAI"


def extract_route(text: str) -> str:
    m = re.search(r"ROUTE(?: MAP)?:\s*\n(.+?)(?:\nTHE ULTIMATE|\nWHY CHOOSE|\nBESPOKE|\nDETAILED|\nDAY-WISE|\nDAY 0|\n[A-Z]{2,} )", text, re.DOTALL | re.IGNORECASE)
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return ""


def extract_overview_sections(text: str) -> str:
    parts: list[str] = []
    welcome = re.search(
        r"(?:TRAGUIN PREMIUM[^\n]+\n[^\n]+\n|BEST GOA TOUR PACKAGE\n[^\n]+\n|Welcome(?: Note)?:[^\n]+\n)(.+?)(?:\nTOUR OVERVIEW|\nTRAVEL DATES|\nWHY CHOOSE|\nDETAILED|\nBESPOKE|\nDAY-WISE|\nDAY 0)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if welcome:
        parts.append(re.sub(r"\s+", " ", welcome.group(1).strip()))

    tour_overview = re.search(
        r"TOUR OVERVIEW\s*\n(.+?)(?:\nTRAVEL DATES|\nWHY CHOOSE|\nTHE ESSENCE|\nTHE ULTIMATE|\nDESTINATION SEO|\nDETAILED|\nBESPOKE|\nDAY-WISE|\nDAY 0)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if tour_overview:
        body = re.sub(r"\s+", " ", tour_overview.group(1).strip())
        parts.append(f"TOUR OVERVIEW\n{body}")

    for heading in ["WHY CHOOSE THE BEST GOA TOUR PACKAGE?", "WHY CHOOSE THE PREMIUM GOA EXPERIENCE?", "WHY CHOOSE A PREMIUM GOA EXPERIENCE?", "WHY CHOOSE THE BEST GOA TOUR PACKAGE FOR SENIORS?", "THE ESSENCE OF A PREMIUM GOA EXPERIENCE", "THE ULTIMATE PREMIUM GOA EXPERIENCE", "DESTINATION SEO CONTENT & INSIGHTS"]:
        m = re.search(rf"{re.escape(heading)}\s*\n(.+?)(?:\nDETAILED|\nBESPOKE|\nDAY-WISE|\nDAY 0|\nHANDPICKED|\nPREMIUM HOTEL)", text, re.DOTALL | re.IGNORECASE)
        if m:
            body = re.sub(r"\s+", " ", m.group(1).strip())
            parts.append(f"{heading}\n{body}")
            break

    return "\n\n".join(parts)


def parse_day_blocks(text: str) -> list[dict]:
    start = re.search(
        r"(?:BESPOKE DAY-WISE ITINERARY|DETAILED DAY-WISE ITINERARY|DAY-WISE DETAILED ITINERARY|THE DAY-WISE ITINERARY)",
        text,
        re.IGNORECASE,
    )
    if not start:
        return []
    section = text[start.end():]
    end = re.search(
        r"(?m)^HANDPICKED (?:LUXURY )?(?:ACCOMMODATION|PREMIUM)|"
        r"^PREMIUM HOTEL OPTIONS|^HOTEL & VILLA OPTIONS|^HANDPICKED PREMIUM ACCOMMODATION|^HANDPICKED ACCOMMODATION PORTFOLIOS",
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
            "Optional Activities",
            "Evening Experience",
            "Overnight Stay",
            "Meals Included",
            "Transfers Included",
            "Food Suggestions",
            "Local Experiences",
            "Complimentary Experience",
            "Photography Points",
        )
        while i < len(lines):
            line = lines[i]
            label_match = re.match(rf"^({'|'.join(activity_labels)}):?\s*(.*)$", line, re.IGNORECASE)
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


def parse_hotel_options(text: str) -> list[dict]:
    section_m = re.search(
        r"(?:HANDPICKED(?: PREMIUM)?(?: & )?(?:ULTRA-)?LUXURY )?(?:ACCOMMODATION OPTIONS|ACCOMMODATION PORTFOLIOS|PREMIUM HOTEL OPTIONS|LUXURY ACCOMMODATIONS)(.+?)(?:PACKAGE INCLUSIONS|PACKAGE INCLUSION)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_m:
        return []
    section = section_m.group(1)

    options: list[dict] = []
    option_patterns = [
        r"Option\s*0?(\d+)\s*[–-]\s*(Deluxe|Premium|Luxury|Ultra\s*Luxury|ULTRA\s*LUXURY)\s*\n(.+?)(?=Option\s*0?\d+\s*[–-]|PACKAGE INCLUSIONS|\Z)",
        r"OPTION\s*0?(\d+)\s*[–-]\s*(DELUXE|PREMIUM|LUXURY|ULTRA\s*LUXURY)\s*\n(.+?)(?=OPTION\s*0?\d+\s*[–-]|PACKAGE INCLUSIONS|\Z)",
    ]
    for pat in option_patterns:
        for m in re.finditer(pat, section, re.DOTALL | re.IGNORECASE):
            num = int(m.group(1))
            category = m.group(2).strip().title().replace("Ultra Luxury", "Ultra Luxury")
            block = m.group(3).strip()
            lines = [ln.strip() for ln in block.splitlines() if ln.strip() and not re.match(r"^(OPTION|Category|North Goa|South Goa|ROOM|MEAL|Category)$", ln, re.I)]
            if not lines:
                continue
            name_parts = []
            room_type = "Deluxe Room"
            meal_plan = "CP (Breakfast)"
            location = "Goa"
            nights = ""
            for ln in lines:
                low = ln.lower()
                if "night" in low and ("goa" in low or "/" in ln):
                    location = ln
                elif any(x in low for x in ["cp ", "mapai", "breakfast", "dinner", "meal", "plan", "dining", "bespoke", "vvip", "custom"]):
                    meal_plan = ln
                elif any(x in low for x in ["room", "suite", "villa", "cottage", "chalet", "view"]):
                    room_type = ln
                else:
                    name_parts.append(ln)
            name = " / ".join(name_parts[:3]) if name_parts else lines[0]
            if len(name_parts) >= 2 and ("North Goa" in section or "South Goa" in section or "NIGHTS" in section.upper()):
                if len(name_parts) >= 2:
                    name = " / ".join(name_parts[:4])
            options.append({
                "sort_order": num,
                "category": category.replace("Deluxe", "Deluxe").replace("Premium", "Premium"),
                "name": name,
                "location": location if location != "Goa" else "Goa",
                "nights_label": nights or _infer_nights(text),
                "room_type": room_type,
                "meal_plan": meal_plan,
                "stars": 5 if "ultra" in category.lower() else 4,
            })

    if options:
        return sorted(options, key=lambda x: x["sort_order"])[:4]

    # Table-style fallback: lines after OPTION 01 – DELUXE header rows
    table_m = re.findall(
        r"OPTION\s*0?(\d+)\s*[–-]\s*(DELUXE|PREMIUM|LUXURY|ULTRA\s*LUXURY)\s*\n(.+?)(?=OPTION\s*0?\d+\s*[–-]|PACKAGE INCLUSIONS|\Z)",
        section,
        re.DOTALL | re.IGNORECASE,
    )
    for num_s, cat, block in table_m:
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        filtered = [ln for ln in lines if not re.match(r"^(Category|North Goa|South Goa|Meal Plan|ROOM|OPTION)$", ln, re.I)]
        if len(filtered) >= 2:
            name = filtered[0]
            if len(filtered) >= 3 and not re.search(r"room|suite|villa|cp|mapai|breakfast", filtered[1], re.I):
                name = f"{filtered[0]} / {filtered[1]}"
                room_type = filtered[2] if len(filtered) > 2 else "Deluxe Room"
                meal_plan = filtered[3] if len(filtered) > 3 else "CP (Breakfast)"
            else:
                room_type = filtered[1] if len(filtered) > 1 else "Deluxe Room"
                meal_plan = filtered[2] if len(filtered) > 2 else "CP (Breakfast)"
            options.append({
                "sort_order": int(num_s),
                "category": cat.strip().title(),
                "name": name,
                "location": "Goa",
                "nights_label": _infer_nights(text),
                "room_type": room_type,
                "meal_plan": meal_plan,
                "stars": 5 if "ultra" in cat.lower() else 4,
            })
    return sorted(options, key=lambda x: x["sort_order"])[:4]


def _infer_nights(text: str) -> str:
    duration = extract_duration(text)
    m = re.search(r"(\d+)\s*Nights?", duration, re.I)
    return f"{m.group(1)} Nights" if m else "03 Nights"


def parse_inclusions_exclusions(text: str) -> tuple[list[str], list[str]]:
    section_m = re.search(r"PACKAGE INCLUSIONS(?: & EXCLUSIONS)?(.+?)(?:SPECIAL TRAGUIN|EXCLUSIVE TRAGUIN|SHOPPING|IMPORTANT)", text, re.DOTALL | re.IGNORECASE)
    if not section_m:
        return [], []
    section = section_m.group(1)
    included: list[str] = []
    excluded: list[str] = []

    lines = section.splitlines()
    mode = None
    for raw in lines:
        line = raw.strip()
        if not line or line in {"✔", "✘", "•"}:
            continue
        if "PACKAGE INCLUSIONS" in line.upper() and "EXCLUSIONS" not in line.upper():
            mode = "inc"
            continue
        if "PACKAGE EXCLUSIONS" in line.upper():
            mode = "exc"
            continue
        if line.startswith("✔"):
            included.append(re.sub(r"^✔\s*", "", line).strip())
        elif line.startswith("✘"):
            excluded.append(re.sub(r"^✘\s*", "", line).strip())
        elif mode == "inc" and not line.startswith("✘"):
            if line and not re.match(r"^(Premium|Luxury|Meals|Taxes|Airfare|Insurance|Optional|Additional|Personal|Monument|Domestic|Water|Travel|Any|Food|Surcharges|Peak|Mandatory|Entry|Guide|Camera|Club|Peak|Holiday|Services|Items|Meals Plan|Complimentary|Heritage|Exclusive|24/7|Taxes:|Airfare:|Insurance:|Additional Meals:)", line):
                continue
            included.append(line)
        elif mode == "exc":
            excluded.append(line)

    # dedupe while preserving order
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
        r"(?:SPECIAL TRAGUIN HIGHLIGHTS|EXCLUSIVE TRAGUIN SIGNATURE(?: HIGHLIGHTS| FAMILY HIGHLIGHTS| HIGHLIGHTS)?)(.+?)(?:SHOPPING|IMPORTANT NOTES|IMPORTANT TRAVEL|LOCAL SHOPPING)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_m:
        return []
    section = section_m.group(1)
    highlights = []
    for line in section.splitlines():
        line = line.strip().lstrip("•").strip()
        if line.startswith("TRAGUIN") or line.startswith("Curated by") or line.startswith("Premium Handpicked") or line.startswith("Personalized") or line.startswith("Luxury Transportation") or line.startswith("Exclusive Recommendations") or line.startswith("Shopping"):
            highlights.append(line)
    return highlights[:6]


def parse_shopping_notes(text: str) -> list[str]:
    parts = []
    shopping = re.search(r"(?:SHOPPING & LOCAL EXPERIENCES(?: INSIGHTS| GUIDE|)?|LOCAL SHOPPING & FAMILY DINING GUIDE|LOCAL EXPERIENCES & SHOPPING INSIGHTS)(.+?)(?:IMPORTANT NOTES|IMPORTANT TRAVEL|IMPORTANT NOTES FOR)", text, re.DOTALL | re.IGNORECASE)
    if shopping:
        body = re.sub(r"\s+", " ", shopping.group(1).strip())
        parts.append(body)
    notes = re.search(r"IMPORTANT NOTES(?: & TRAVEL INFORMATION| FOR YOUR JOURNEY| FOR AN IDEAL STAY| FOR COMFORT & SAFETY| & TRAVEL INFORMATION| FOR TRAVELERS| FOR SENIORS| FOR COMFORT| FOR AN IDEAL STAY| FOR YOUR JOURNEY| & TRAVEL INFORMATION)?(.+?)(?:TRAGUIN\s*$|PREMIUM TRAVEL|\Z)", text, re.DOTALL | re.IGNORECASE)
    if notes:
        body = notes.group(1).strip()
        for ln in body.splitlines():
            ln = ln.strip().lstrip("•").strip()
            if ln and not ln.startswith("TRAGUIN") and "PREMIUM TRAVEL" not in ln:
                parts.append(ln)
    return parts[:8]


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
        f"State / Country: Goa / India | Category: {category}",
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


def build_itinerary_highlights(days: list[dict]) -> list[str]:
    out = []
    for i, day in enumerate(days[:10], 1):
        short = day["title"].split("|")[0].strip() if "|" in day["title"] else day["title"]
        out.append(f"Day {day['day_number']:02d}: {short}")
    return out


def emit_hotel(hotel: dict, duration: str) -> str:
    nights = hotel.get("nights_label") or _infer_nights_from_duration(duration)
    desc = hotel.get("description") or (
        f"OPTION {hotel['sort_order']:02d} – {hotel['category'].upper()}: "
        f"{hotel['name']} ({hotel.get('location', 'Goa')}) | {hotel['meal_plan']}"
    )
    return f"""            _hotel(
                {py_str(hotel['name'])},
                {py_str(hotel.get('location') or 'Goa')},
                {py_str(nights)},
                {py_str(hotel['category'])},
                {py_str(hotel['room_type'])},
                {py_str(hotel['meal_plan'])},
                {hotel['stars']},
                {hotel['sort_order']},
                description={py_str(desc)},
            )"""


def _infer_nights_from_duration(duration: str) -> str:
    m = re.search(r"(\d+)\s*Nights?", duration, re.I)
    return f"{m.group(1)} Nights" if m else "03 Nights"


def emit_builder(serial: str, meta: dict, text: str) -> str:
    num = serial.split("-")[1]
    func = f"build_ga_{num}"
    duration = extract_duration(text)
    slug = meta["slug"]
    itin_slug = f"{slug}-itinerary"
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = parse_day_blocks(text)
    hotels = GOA_HOTELS.get(serial, [])
    included, excluded = parse_inclusions_exclusions(text)
    overview = extract_overview_sections(text)
    pkg_highlights = build_package_highlights({**meta, "serial": serial}, text)
    itin_highlights = build_itinerary_highlights(days)
    starting_price = extract_starting_price(text)
    tagline = title.split("—")[-1].strip() if "—" in title else title.replace("TRAGUIN Premium Goa Tour Package", "").strip(" —")

    if not hotels:
        hotels = [
            {"sort_order": 1, "category": "Deluxe", "name": "Handpicked Premium Goa Resort / Similar", "location": "Goa", "nights_label": _infer_nights_from_duration(duration), "room_type": "Superior Room", "meal_plan": "CP (Breakfast)", "stars": 4},
            {"sort_order": 2, "category": "Premium", "name": "Novotel Goa Resort & Spa / Similar", "location": "Goa", "nights_label": _infer_nights_from_duration(duration), "room_type": "Premium Room", "meal_plan": "CP (Breakfast)", "stars": 4},
            {"sort_order": 3, "category": "Luxury", "name": "Taj Holiday Village / W Goa", "location": "Goa", "nights_label": _infer_nights_from_duration(duration), "room_type": "Luxury Suite", "meal_plan": "CP (Breakfast)", "stars": 5},
            {"sort_order": 4, "category": "Ultra Luxury", "name": "The Leela Goa / Taj Exotica Resort & Spa", "location": "Goa", "nights_label": _infer_nights_from_duration(duration), "room_type": "Private Villa Suite", "meal_plan": "Bespoke Dining Plan", "stars": 5},
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
            '            _inc_included("Premium accommodation at handpicked Goa resorts.", 1),',
            '            _inc_included("Private luxury vehicle for all transfers and sightseeing.", 2),',
            '            _inc_excluded("Airfare and personal expenses.", 3),',
        ]

    ph_lines = ",\n".join(f"            _ph({py_str(h)}, {i})" for i, h in enumerate(pkg_highlights, 1))
    ih_lines = ",\n".join(f"            _ih({py_str(h)}, {i})" for i, h in enumerate(itin_highlights, 1))
    mood_lines = ", ".join(py_str(m) for m in moods)
    seo_title = f"{serial} | {title.split('—')[0].replace('TRAGUIN Premium Goa Tour Package', 'Goa').strip(' —')} | TRAGUIN"
    seo_desc = f"Premium {duration} Goa package ({serial} / {tour_code}): {extract_destinations(text)[:120]}."

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
    header = '''"""Builder functions for GA-001 through GA-025 Goa packages (excluding GA-011)."""

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

GOA_SLUG = "goa"


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
        builders.append(emit_builder(serial, meta, text))

    builder_names = [f"build_ga_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nGOA_DOMESTIC_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
