#!/usr/bin/env python3
"""Generate france_fr_001_005_batch_defs.py from tmp_fr_pdfs text sources."""

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

PDF_DIR = _SCRIPTS.parent / "tmp_fr_pdfs"
OUT_PATH = _SCRIPTS / "france_fr_001_005_batch_defs.py"
PRICE_NOTE = "On Request (Premium France Experience)"
BUILDER_ORDER = [f"FR-{i:03d}" for i in range(1, 6)]

clean_raw = _jh.clean_raw
py_str = _jh.py_str
extract_duration = _jh.extract_duration
extract_category = _jh.extract_category
extract_ideal_for = _jh.extract_ideal_for
extract_best_season = _jh.extract_best_season
extract_starting_price = _jh.extract_starting_price
extract_overview_sections = _jh.extract_overview_sections
parse_signature_highlights = _jh.parse_signature_highlights
build_itinerary_highlights = _jh.build_itinerary_highlights
_compact_nights_label = _jh._compact_nights_label

TITLE_MAP = {
    "FR-001": "Paris Highlights Family Tour",
    "FR-002": "Romantic Paris Honeymoon",
    "FR-003": "Luxury France Tour",
    "FR-004": "Paris & Swiss Family Tour",
    "FR-005": "Grand France Tour",
}

SLUG_MAP = {
    "FR-001": "fr-001-paris-highlights-family-tour",
    "FR-002": "fr-002-romantic-paris-honeymoon",
    "FR-003": "fr-003-luxury-france-tour",
    "FR-004": "fr-004-paris-swiss-family-tour",
    "FR-005": "fr-005-grand-france-tour",
}

ITIN_SLUG_MAP = {
    "FR-001": "fr-001-paris-highlights-itinerary",
    "FR-002": "fr-002-romantic-paris-itinerary",
    "FR-003": "fr-003-luxury-france-itinerary",
    "FR-004": "fr-004-paris-swiss-family-itinerary",
    "FR-005": "fr-005-grand-france-itinerary",
}

_FR_FOOTER_LINE = re.compile(
    r"TRAGUIN (?:Family Vacations|Honeymoon Experts|Luxury Holidays|Premium Holidays)"
    r"(?: • FR-\d{3})?(?: • www\.traguin\.in)?(?: Page \d+ of \d+)?",
    re.IGNORECASE,
)
_FR_FOOTER_FRAGMENT = re.compile(
    r"(?:TRAGUIN )?(?:Family Vacations|Honeymoon Experts|Luxury Holidays)"
    r"(?: • www\.traguin\.in)?[^\n]*?(?=DAY\s*\d+)",
    re.IGNORECASE,
)


def pdf_serial_to_db_serial(pdf_serial: str) -> str:
    return pdf_serial


def normalize_fr_raw(raw: str) -> str:
    raw = re.sub(r"TRAGUIN TOUR\s*\n\s*CODE:\s*", "TRAGUIN TOUR CODE: ", raw, flags=re.I)
    raw = re.sub(
        r"(TRG-[A-Z]+-)\s*\n\s*([A-Z0-9\-]+)",
        r"\1\2",
        raw,
        flags=re.I,
    )
    raw = re.sub(r"SwitzerlandCATEGORY:", "Switzerland CATEGORY:", raw, flags=re.I)
    raw = re.sub(r"Lucerne/\s*\n\s*Interlaken", "Lucerne/Interlaken", raw, flags=re.I)
    return raw


def _normalize_day_headers(text: str) -> str:
    text = re.sub(r"(?:www\.)?traguin\.in\s*", "\n", text, flags=re.I)
    text = re.sub(r"(?<=[^\n])(DAY\s*\d+\s*[|–\-])", r"\n\1", text, flags=re.I)
    text = re.sub(r"^\s+(DAY\s*\d+)", r"\1", text, flags=re.MULTILINE)
    return text


def clean_fr_raw(raw: str) -> str:
    raw = normalize_fr_raw(raw)
    raw = _FR_FOOTER_LINE.sub("\n", raw)
    text = clean_raw(raw)
    text = re.sub(r"TRAGUIN TOUR\s*\n\s*CODE:", "TRAGUIN TOUR CODE:", text, flags=re.I)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = _FR_FOOTER_LINE.sub("\n", text)
    text = _FR_FOOTER_FRAGMENT.sub("\n", text)
    text = _normalize_day_headers(text)
    return text


def extract_tour_code(text: str) -> str:
    flat = re.sub(r"\s+", " ", normalize_fr_raw(text))
    m = re.search(r"TRAGUIN TOUR CODE:\s*(TRG-[A-Z0-9\-]+)", flat, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"(?:TRAGUIN TOUR )?CODE:\s*(TRG-[A-Z0-9\-]+)", flat, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"(TRG-[A-Z]{3}-[A-Z0-9\-]+)", flat)
    return m.group(1) if m else "TRG-FRA-000"


def extract_title_fr(text: str, serial: str = "") -> str:
    if serial in TITLE_MAP:
        return TITLE_MAP[serial]
    header = re.search(
        r"TRAGUIN PREMIUM\s+(.+?)(?:\n\n|\n\d+\s+Nights|\nSERIAL|\nSTATE|\nTOUR OVERVIEW)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if header:
        title = re.sub(r"\s+", " ", header.group(1).strip())
        title = re.sub(r"\s+\d{2}\s+Nights\s*/\s*\d{2}\s+Days.*$", "", title, flags=re.I).strip()
        if len(title) > 6:
            return title.title() if title.isupper() else title
    tagline = re.search(r"^(.{12,120}•.{8,120})$", text, re.MULTILINE)
    if tagline:
        return re.sub(r"\s+", " ", tagline.group(1).strip())
    return "France Premium Tour"


def extract_destinations_fr(text: str) -> str:
    m = re.search(
        r"DESTINATIONS:\s*(.+?)(?:CATEGORY:|DURATION:|TOUR OVERVIEW|STATE /)",
        re.sub(r"\s+", " ", text),
        re.I,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    tagline = re.search(r"^(.{12,120}•.{8,120})$", text, re.MULTILINE)
    if tagline:
        return re.sub(r"\s+", " ", tagline.group(1).strip())
    m = re.search(
        r"DURATION:\s*\d+\s*Nights\s*/\s*\d+\s*Days\s+(.+?)(?:TOUR OVERVIEW|$)",
        re.sub(r"\s+", " ", text),
        re.I,
    )
    if m:
        raw = m.group(1).strip()
        raw = re.sub(r"\s*\+\s*", " • ", raw)
        return raw
    return "France"


def extract_category_fr(text: str) -> str:
    m = re.search(
        r"CATEGORY:\s*(.+?)(?:\nDURATION|\nTOUR OVERVIEW|\nSTATE|\nZurich|\nLucerne)",
        text,
        re.DOTALL | re.I,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return extract_category(text)


def make_slug(serial: str, title: str) -> str:
    if serial in SLUG_MAP:
        return SLUG_MAP[serial]
    num = serial.split("-")[1]
    base = title.lower()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return f"fr-{num}-{base}"[:118].rstrip("-")


def infer_moods(text: str, serial: str = "") -> list[str]:
    blob = f"{extract_category_fr(text)} {extract_title_fr(text, serial)}".lower()
    candidates = [
        ("Family", ("family", "explorer")),
        ("Romantic", ("honeymoon", "romantic", "couple", "paris")),
        ("Luxury", ("luxury", "premium", "ultra", "grand", "michelin")),
        ("Culture", ("louvre", "versailles", "museum", "heritage", "art")),
        ("Nature", ("alps", "alpine", "lavender", "provence", "riviera")),
        ("Adventure", ("titlis", "swiss", "switzerland")),
    ]
    moods: list[str] = []
    for mood, keys in candidates:
        if any(k in blob for k in keys):
            moods.append(mood)
    return moods[:4] or ["Family", "Luxury", "Culture"]


def parse_day_blocks_fr(text: str) -> list[dict]:
    start = re.search(
        r"(?:THE IMMERSIVE DAY-WISE ITINERARY|THE DEFINITIVE DAY-WISE ITINERARY|"
        r"DETAILED DAY-WISE ITINERARY|DAY-WISE ITINERARY|DAY WISE ITINERARY)",
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
        r"(?m)^(?:HANDPICKED (?:PREMIUM )?(?:FAMILY )?(?:STAYS|ACCOMMODATIONS)|HANDPICKED ROMANTIC STAYS|"
        r"HANDPICKED PREMIUM LUXURY STAYS|HANDPICKED PREMIUM STAYS|HOTEL OPTIONS|"
        r"ACCOMMODATION OPTIONS)",
        section,
    )
    if end:
        section = section[: end.start()]
    section = _jh.FOOTER_RE.sub("", section)
    section = _jh.PAGE_RE.sub("", section)
    return _jh.parse_day_blocks(f"DETAILED DAY-WISE ITINERARY\n{section}")


def _clean_day_descriptions(days: list[dict]) -> list[dict]:
    stop_markers = (
        "HANDPICKED PREMIUM",
        "HANDPICKED ROMANTIC",
        "TRAGUIN Family Vacations",
        "TRAGUIN Luxury Holidays",
        "TRAGUIN Honeymoon Experts",
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


def _split_option_hotels(option_text: str, expected: int) -> list[str]:
    text = re.sub(r"^Option\s*\d+\s*:\s*", "", option_text.strip(), flags=re.I)
    if not text:
        return []
    if expected == 1:
        return [text]
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)
    known = [
        "Le Meurice",
        "The Peninsula Paris",
        "The Ritz Paris",
        "Shangri-La Paris",
        "Four Seasons George V",
        "Ritz Paris",
        "Grand-Hôtel du Cap-Ferrat",
        "Bürgenstock Resort",
        "Château de la Bourdaisière",
        "The Peninsula Paris",
    ]
    for name in known:
        text = text.replace(name, f"|{name}|")
    parts = [p.strip() for p in text.split("|") if p.strip()]
    if len(parts) >= expected:
        return parts[:expected]
    parts = re.findall(
        r"(?:Premium|Luxury|Ultra[\s-]?Luxury)?\s*[\w\s\-]+?(?:Hotel|Resort|Suites|Retreat|Grand|Palace|Omnia|Lac)",
        text,
        flags=re.I,
    )
    parts = [p.strip() for p in parts if p.strip()]
    if len(parts) >= expected:
        return parts[:expected]
    return parts or [text]


def parse_fr_hotel_options(text: str) -> list[dict]:
    section = re.search(
        r"(HANDPICKED (?:PREMIUM (?:FAMILY )?(?:STAYS|ACCOMMODATIONS)|ROMANTIC STAYS|PREMIUM LUXURY STAYS|PREMIUM STAYS))"
        r"[\s\S]+?(?:\"Creating Memories|PREMIUM TRAVEL|$)",
        text,
        re.I,
    )
    if not section:
        return []
    block = section.group(0)
    cat_parts: list[str] = []
    opt_parts: list[str] = []
    mode: str | None = None
    for ln in block.splitlines():
        ln = ln.strip()
        if not ln or ln.lower().startswith("handpicked"):
            continue
        if re.match(r"^Category", ln, re.I):
            mode = "cat"
            cat_parts.append(re.sub(r"^Category\s+", "", ln, flags=re.I))
        elif re.match(r"^Option", ln, re.I):
            mode = "opt"
            opt_parts.append(re.sub(r"^Option\s*\d+\s*:?\s*", "", ln, flags=re.I))
        elif mode == "cat":
            cat_parts.append(ln)
        elif mode == "opt":
            opt_parts.append(ln)
    category_line = re.sub(r"\s+", " ", " ".join(cat_parts)).strip()
    option_text = re.sub(r"\s+", " ", " ".join(opt_parts)).strip()
    if not category_line:
        return []
    locations = re.findall(r"([A-Za-z][A-Za-z\s\-]+?)\s*\((\d+)N\)", category_line)
    if not locations:
        return []
    tier_match = re.search(r"Option\s*(\d+)", block, re.I)
    tier_num = int(tier_match.group(1)) if tier_match else 1
    tier_labels = {1: "Premium", 2: "Premium", 3: "Luxury", 4: "Ultra Luxury"}
    category = tier_labels.get(tier_num, "Premium")
    if re.match(r"^Ultra\s+Luxury", option_text, re.I):
        option_text = re.sub(r"^Ultra\s+Luxury\s*", "", option_text, flags=re.I)
        category = "Ultra Luxury"
    hotel_names = _split_option_hotels(f"Option {tier_num}: {option_text}", len(locations))
    hotels: list[dict] = []
    for idx, (city, nights) in enumerate(locations, 1):
        name = hotel_names[idx - 1] if idx - 1 < len(hotel_names) else f"TRAGUIN Handpicked {category} Property"
        hotels.append(
            {
                "sort_order": idx,
                "category": category,
                "name": f"{name} / similar",
                "location": city.strip(),
                "nights_label": _compact_nights_label(f"{nights} Night{'s' if int(nights) != 1 else ''}"),
                "room_type": "Deluxe Room",
                "meal_plan": "Breakfast",
                "stars": 5 if "ultra" in category.lower() else 5,
                "description": f"OPTION {idx:02d} – {category.upper()}: {name}",
            }
        )
    return hotels


def default_inclusions(duration: str, destinations: str, text: str) -> tuple[list[str], list[str]]:
    blob = f"{text} {destinations}".lower()
    nights_part = duration.split("/")[0].strip() if "/" in duration else duration
    included = [
        f"{nights_part} in handpicked premium hotels across {destinations}",
        "Private executive chauffeur-driven luxury ground transfers throughout",
    ]
    if "eiffel" in blob or "louvre" in blob or "versailles" in blob:
        included.append("Private guided Paris sightseeing including Eiffel Tower, Louvre, and Versailles")
    if "seine" in blob:
        included.append("Scenic Seine River cruise experience")
    if "montmartre" in blob:
        included.append("Montmartre and Sacré-Cœur artistic quarter exploration")
    if "monaco" in blob or "riviera" in blob or "nice" in blob:
        included.append("French Riviera and Monaco elite coastal experiences")
    if "bordeaux" in blob or "loire" in blob or "provence" in blob:
        included.append("Curated wine country and heritage castle experiences")
    if "titlis" in blob or "switzerland" in blob:
        included.append("High-speed rail and alpine experiences in Switzerland")
    included.append("TRAGUIN 24/7 dedicated on-ground concierge support")
    excluded = [
        "International airfare and France/Schengen entry visa processing fees",
        "Personal expenses, laundry, room service, and mini-bar charges",
        "Optional sightseeing excursions not specified in the itinerary",
        "Tipping, porterage fees, and travel insurance",
    ]
    return included, excluded


def build_meta(serial: str, text: str, raw: str) -> dict:
    title = extract_title_fr(text, serial)
    tour_code = extract_tour_code(normalize_fr_raw(raw))
    destinations = extract_destinations_fr(text)
    hotels = parse_fr_hotel_options(text)
    if not hotels:
        nights = _jh._infer_nights(text)
        hotels = [
            {
                "sort_order": 1,
                "category": "Premium",
                "name": "TRAGUIN Handpicked Premium Property / similar",
                "location": destinations.split("•")[0].strip() or "France",
                "nights_label": nights,
                "room_type": "Deluxe Room",
                "meal_plan": "Breakfast",
                "stars": 5,
                "description": "OPTION 01 – PREMIUM: TRAGUIN Handpicked Premium Property",
            }
        ]
    included, excluded = default_inclusions(extract_duration(text), destinations, text)
    return {
        "serial": serial,
        "db_serial": pdf_serial_to_db_serial(serial),
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
    category = extract_category_fr(text)
    destinations = meta.get("destinations") or extract_destinations_fr(text)
    highlights = [
        f"Serial code {serial} | TRAGUIN tour code {tour_code}",
        f"Country: France | Category: {category}",
        f"Destinations: {destinations}",
        f"Best season: {extract_best_season(text) or 'April to October (Spring/Summer); December for festive Paris'}",
        f"Starting price: {extract_starting_price(text) or 'On Request'}",
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
    return cleaned[:12]


def emit_hotel(hotel: dict, duration: str) -> str:
    nights = hotel.get("nights_label") or _compact_nights_label(_jh._infer_nights(duration))
    room_type = hotel.get("room_type", "Deluxe Room")
    meal_plan = hotel.get("meal_plan", "Breakfast")
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


def emit_builder(serial: str, meta: dict, text: str) -> str:
    num = serial.split("-")[1]
    func = f"build_fr_{num}"
    duration = re.sub(r"\s+", " ", extract_duration(text))
    slug = meta["slug"]
    itin_slug = ITIN_SLUG_MAP.get(serial, f"{slug}-itinerary")
    title = meta["title"]
    tour_code = meta["tour_code"]
    db_serial = meta["db_serial"]
    moods = meta["moods"]
    days = _clean_day_descriptions(parse_day_blocks_fr(text))
    hotels = meta["hotels"]
    included = meta["included"]
    excluded = meta["excluded"]
    overview = extract_overview_sections(text)
    pkg_highlights = build_package_highlights(meta, text)
    itin_highlights = build_itinerary_highlights(days, text)
    tagline = meta["destinations"]

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
    inc_lines: list[str] = []
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
    seo_title = f"{serial} | {title[:80]} | TRAGUIN"
    destinations = meta.get("destinations") or extract_destinations_fr(text)
    seo_desc = (
        f"Premium {duration} France package ({serial} / {tour_code}): "
        f"{destinations[:120]}."
    )

    return f"""
def {func}(destination_id: str | UUID) -> tuple[PackageCreate, ItineraryCreate]:
    serial = {py_str(serial)}
    db_serial = {py_str(db_serial)}
    tour_code = {py_str(tour_code)}
    title = {py_str(title)}
    duration = {py_str(duration)}
    slug = {py_str(slug)}
    itin_slug = {py_str(itin_slug)}
    package = PackageCreate(
        slug=slug,
        serial_code=db_serial,
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
    header = '''"""Builder functions for FR-001 through FR-005 France international packages."""

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

FRANCE_SLUG = "france"


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
        text = clean_fr_raw(raw)
        meta = build_meta(serial, text, raw)
        days = _clean_day_descriptions(parse_day_blocks_fr(text))
        builders.append(emit_builder(serial, meta, text))
        print(
            f"{serial} -> {meta['db_serial']}: {meta['title'][:50]} | "
            f"days={len(days)} hotels={len(meta['hotels'])} tour={meta['tour_code']}"
        )

    builder_names = [f"build_fr_{serial.split('-')[1]}" for serial in BUILDER_ORDER]
    footer = "\nFRANCE_FR_001_005_BUILDERS = [\n    " + ",\n    ".join(builder_names) + ",\n]\n"
    OUT_PATH.write_text(header + "".join(builders) + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.read_text().count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()
