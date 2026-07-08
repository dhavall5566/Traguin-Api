#!/usr/bin/env python3
"""Generate telangana_domestic_batch_defs.py from tmp_tg_pdfs text sources."""

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

PDF_DIR = _SCRIPTS.parent / "tmp_tg_pdfs"
OUT_PATH = _SCRIPTS / "telangana_domestic_batch_defs.py"
PRICE_NOTE = "On Request (Premium Customised)"
BUILDER_ORDER = [f"TG-{i:03d}" for i in range(1, 11)]

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


def extract_destinations_telangana(text: str) -> str:
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
                r"^(IDEAL FOR|BEST SEASON|STARTING PRICE|TRAGUIN TOUR|VEHICLE|TOUR OVERVIEW|DURATION|CATEGORY|TRAVEL MONTH):",
                stripped,
                re.I,
            ):
                break
            parts.append(stripped)
    if parts:
        raw = re.sub(r"\s+", " ", " ".join(parts))
        return raw.replace(",", " • ")
    m = re.search(r"DESTINATIONS:\s*([^\n]+)", text, re.I)
    return re.sub(r"\s+", " ", m.group(1).strip()) if m else "Hyderabad • Telangana"


def extract_tour_code(text: str) -> str:
    flat = re.sub(r"\s+", " ", text)
    m = re.search(r"TRAGUIN TOUR\s*CODE:\s*([A-Z0-9\-]+)", flat, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"(TRG-[A-Z0-9\-]+)", flat)
    return m.group(1) if m else "TRG-TEL-000"


def extract_title_telangana(text: str) -> str:
    patterns = [
        r"TRAGUIN PREMIUM TELANGANA TOUR\s*\nPACKAGE\s*\n(.+?)(?:\nTRAGUIN Premium|\nTRAGUIN Corporate|\nWelcome|\nTOUR OVERVIEW)",
        r"TRAGUIN PREMIUM TELANGANA TOUR PACKAGE\s*\n(.+?)(?:\nTRAGUIN Premium|\nTRAGUIN Corporate|\nWelcome|\nTOUR OVERVIEW)",
        r"TRAGUIN PREMIUM TELANGANA TOUR\s*\nPACKAGE\s*\n(.+)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.DOTALL | re.IGNORECASE)
        if m:
            title = re.sub(r"\s+", " ", m.group(1).strip())
            title = re.sub(r"\s*TRAGUIN.*$", "", title, flags=re.I).strip()
            title = re.sub(r"\s+\d{2}\s+NIGHTS\s*/\s*\d{2}\s+DAYS.*$", "", title, flags=re.I).strip()
            if len(title) > 12:
                return title
    return "Telangana Premium Luxury Tour"


def extract_vehicle_meals_telangana(text: str) -> str:
    flat = re.sub(r"\s+", " ", text)
    for label in (
        "VEHICLE / MEALS:",
        "VEHICLE & MEALS:",
        "VEHICLE & MEAL PLAN:",
        "VEHICLE:",
    ):
        m = re.search(rf"{re.escape(label)}\s*(.+?)(?:TRAGUIN PREMIUM|TOUR OVERVIEW|DETAILED)", flat, re.I)
        if m:
            return m.group(1).strip()[:200]
    return "Private Luxury SUV / MAPAI"


def make_slug(serial: str, title: str) -> str:
    num = serial.split("-")[1]
    base = title.lower()
    base = base.replace("•", " ").replace("—", " ").replace("/", " ")
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return f"tg-{num}-{base}"[:118].rstrip("-")


def infer_moods(text: str) -> list[str]:
    blob = f"{extract_ideal_for(text)} {extract_category_telangana(text)} {extract_title_telangana(text)}".lower()
    candidates = [
        ("Family", ("family", "group")),
        ("Luxury", ("luxury", "premium", "bespoke")),
        ("Honeymoon", ("honeymoon", "romantic", "couple", "love")),
        ("Culture", ("culture", "heritage", "nizam", "royal", "fort")),
        ("Leisure", ("leisure", "senior")),
        ("Corporate", ("corporate", "mice", "conference", "delegate", "executive")),
        ("Educational", ("educational", "school", "student", "academic")),
        ("Adventure", ("adventure", "expedition", "thrill")),
        ("Nature", ("nature", "lake", "valley")),
    ]
    moods: list[str] = []
    for mood, keys in candidates:
        if any(k in blob for k in keys):
            moods.append(mood)
    if not moods:
        moods = ["Family", "Luxury", "Nature"]
    return moods[:3]


def parse_day_blocks_telangana(text: str) -> list[dict]:
    start = re.search(
        r"(?:DETAILED DAY-WISE ITINERARY|DAY-WISE ITINERARY|DAY WISE ITINERARY)",
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
        r"(?m)^(?:HANDPICKED (?:LUXURY )?(?:PREMIUM )?(?:ACCOMMODATION|HOTEL)|"
        r"PREMIUM ACCOMMODATION|HOTEL OPTIONS|HOTEL SELECTION|ACCOMMODATION OPTIONS|"
        r"HANDPICKED PREMIUM HOTEL|PREMIUM HOTEL OPTIONS|CURATED HOTEL|"
        r"CORPORATE ACCOMMODATION OPTIONS)",
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


def extract_category_telangana(text: str) -> str:
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


def parse_telangana_inclusions_exclusions(text: str) -> tuple[list[str], list[str]]:
    cleaned = _jh.PAGE_RE.sub(" ", text)
    cleaned = re.sub(
        r"TRAGUIN (?:Premium Luxury Itinerary|Corporate Luxury Proposal) — [A-Z]{2}-\d{3}\s*\d+",
        " ",
        cleaned,
        flags=re.IGNORECASE,
    )
    included, excluded = parse_inclusions_exclusions(cleaned)
    exc_m = re.search(
        r"PACKAGE EXCLUSIONS\s*(.+?)(?=\nSPECIAL TRAGUIN|\nSHOPPING &|\nIMPORTANT|\Z)",
        cleaned,
        re.DOTALL | re.IGNORECASE,
    )
    if exc_m:
        alt_exc = _parse_exclusion_markers(exc_m.group(1))
        if len(alt_exc) >= len(excluded):
            excluded = alt_exc
    included = [
        re.sub(r"^✔\s*", "", re.sub(r"\s+", " ", item).strip())
        for item in included
        if item and "TRAGUIN Premium Luxury Itinerary" not in item and len(item) > 10
    ]
    excluded = [re.sub(r"\s+", " ", item).strip() for item in excluded if item and len(item) > 10]
    return included, excluded


def parse_telangana_hotel_options(text: str) -> list[dict]:
    """Parse Telangana PDF table-style hotel option blocks (4 tiers)."""
    section_m = re.search(
        r"(?:HANDPICKED (?:PREMIUM )?(?:CORPORATE )?(?:HOTEL|ACCOMMODATION)(?: OPTIONS)?|"
        r"PREMIUM HOTEL OPTIONS|ACCOMMODATION OPTIONS)\s*(.+?)"
        r"(?:PACKAGE INCLUSIONS|PACKAGE INCLUSION)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_m:
        return []
    section = section_m.group(1)
    options: list[dict] = []
    pattern = re.compile(
        r"OPTION\s*0?(\d+)\s*[–-]\s*((?:DELUXE|PREMIUM|LUXURY|ULTRA\s*\n?\s*LUXURY|ULTRA))\s*(.+?)"
        r"(?=OPTION\s*0?\d+\s*[–-]|PACKAGE INCLUSIONS|\Z)",
        re.DOTALL | re.IGNORECASE,
    )
    for m in pattern.finditer(section):
        num = int(m.group(1))
        category = re.sub(r"\s+", " ", m.group(2).strip()).title()
        if category.upper().startswith("ULTRA"):
            category = "Ultra Luxury"
        block = re.sub(r"\s+", " ", m.group(3).strip())
        block = re.sub(
            r"^(Category|Hyderabad|Gangtok|Lachung|Lachen|Room Category|CATEGORY TIER|SELECTED LUXURY).*$",
            "",
            block,
            flags=re.I,
        )
        block = block.strip(" /")
        if not block or len(block) < 6:
            continue
        # Split multi-property rows on " / " when present
        parts = [p.strip() for p in re.split(r"\s*/\s*", block) if p.strip() and "similar" not in p.lower()]
        name = " / ".join(parts[:3]) if parts else block[:128]
        options.append(
            {
                "sort_order": num,
                "category": category,
                "name": name[:128],
                "location": "Telangana",
                "nights_label": _jh._infer_nights(text),
                "room_type": "Deluxe Room" if "deluxe" in category.lower() else "Premium Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 5 if "ultra" in category.lower() or category == "Luxury" else 4,
                "description": f"OPTION {num:02d} – {category.upper()}: {name[:100]}",
            }
        )
    return sorted(options, key=lambda x: x["sort_order"])[:4]


def build_meta(serial: str, text: str, raw: str) -> dict:
    title = extract_title_telangana(text)
    tour_code = extract_tour_code(raw)
    destinations = extract_destinations_telangana(text)
    hotels = parse_hotel_options(text)
    if len(hotels) < 4:
        alt = parse_telangana_hotel_options(text)
        if len(alt) > len(hotels):
            hotels = alt
    if not hotels:
        nights = _jh._infer_nights(text)
        hotels = [
            {
                "sort_order": i,
                "category": cat,
                "name": f"TRAGUIN Handpicked {cat} Property",
                "location": destinations.split("•")[0].strip() or "Telangana",
                "nights_label": nights,
                "room_type": "Deluxe Room",
                "meal_plan": "MAPAI (Breakfast & Dinner)",
                "stars": 5 if "ultra" in cat.lower() else 4,
                "description": f"OPTION {i:02d} – {cat.upper()}: TRAGUIN Handpicked {cat} Property",
            }
            for i, cat in enumerate(["Deluxe", "Premium", "Luxury", "Ultra Luxury"], 1)
        ]
    primary_loc = destinations.split("•")[0].strip() or "Telangana"
    for hotel in hotels:
        if hotel.get("location") in ("Jharkhand", "", "Haryana"):
            hotel["location"] = primary_loc
        hotel["nights_label"] = _compact_nights_label(hotel.get("nights_label") or _jh._infer_nights(text))
    included, excluded = parse_telangana_inclusions_exclusions(raw)
    return {
        "serial": serial,
        "tour_code": tour_code,
        "slug": make_slug(serial, title),
        "title": title,
        "destinations": destinations,
        "moods": infer_moods(text),
        "hotels": hotels,
        "included": included,
        "excluded": excluded,
    }


def build_package_highlights(meta: dict, text: str) -> list[str]:
    serial = meta["serial"]
    tour_code = meta["tour_code"]
    category = extract_category_telangana(text)
    destinations = meta.get("destinations") or extract_destinations_telangana(text)
    highlights = [
        f"Serial code {serial} | TRAGUIN tour code {tour_code}",
        f"State / Country: Telangana / India | Category: {category}",
        f"Destinations: {destinations}",
        f"Ideal for: {extract_ideal_for(text)}",
        f"Best season: {extract_best_season(text)}",
        f"Starting price: {extract_starting_price(text)}",
        f"Vehicle / Meals: {extract_vehicle_meals_telangana(text)}",
    ]
    for sig in parse_signature_highlights(text)[:4]:
        sig = re.sub(r"\s+", " ", sig).strip()
        if sig:
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
    func = f"build_tg_{num}"
    duration = re.sub(r"\s+", " ", extract_duration(text))
    slug = meta["slug"]
    itin_slug = f"{slug}-itinerary"
    title = meta["title"]
    tour_code = meta["tour_code"]
    moods = meta["moods"]
    days = _clean_day_descriptions(parse_day_blocks_telangana(text))
    hotels = meta["hotels"]
    included = _clean_items(meta.get("included") or parse_telangana_inclusions_exclusions(raw_text)[0])
    excluded = meta.get("excluded")
    if excluded is None:
        _, excluded = parse_telangana_inclusions_exclusions(raw_text)
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
    destinations = meta.get("destinations") or extract_destinations_telangana(text)
    seo_desc = (
        f"Premium {duration} Telangana package ({serial} / {tour_code}): "
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
    header = '''"""Builder functions for TG-001 through TG-010 Telangana domestic packages."""

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

TELANGANA_SLUG = "telangana"


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
        meta = build_meta(serial, text, raw)
        builders.append(emit_builder(serial, meta, text, raw))
        print(f"{serial}: {meta['title'][:60]} | days hotels={len(meta['hotels'])}")

    builder_names = [f"build_tg_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nTELANGANA_DOMESTIC_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
