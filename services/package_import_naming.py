from __future__ import annotations

import re

from schemas.package_import import ExtractedPackageBundle
from utils.slugify import slugify

BROCHURE_TITLE_PATTERN = re.compile(
    r"\b(traguin|premium|luxury|signature|handpicked|exclusive|bespoke|package|itinerary|tour|escape|journey|experience|nights?|days?|d/|n)\b",
    re.IGNORECASE,
)

DAY_CITY_PATTERNS = (
    re.compile(
        r"\b(?:arrival in|drive to|reach|departure from|stay in|overnight in|return to)\s+"
        r"([A-Za-z][A-Za-z\s]{1,28}?)(?:\s+(?:and|via|with|for|by|to)\b|[,|]|$)",
        re.IGNORECASE,
    ),
    re.compile(r"^([A-Za-z][A-Za-z\s]{1,28}?)\s+sightseeing\b", re.IGNORECASE),
    re.compile(r"^([A-Za-z][A-Za-z\s]{1,28}?)\s+local\b", re.IGNORECASE),
)

NIGHTS_PATTERN = re.compile(r"(\d+)", re.IGNORECASE)

THEME_KEYWORDS: dict[str, tuple[str, ...]] = {
    "Pilgrimage": (
        "pilgrim",
        "temple",
        "shrine",
        "aarti",
        "jyotirlinga",
        "darshan",
        "spiritual",
        "holy",
        "somnath",
        "dwarka",
        "tirth",
    ),
    "Heritage": (
        "heritage",
        "unesco",
        "fort",
        "stepwell",
        "ashram",
        "historic",
        "cultural",
        "old city",
        "monument",
    ),
    "Wildlife Safari": ("safari", "wildlife", "lion", "national park", "gir"),
    "Desert Escape": ("rann", "desert", "white desert", "kutch"),
    "Coastal Retreat": ("beach", "coast", "marine", "island"),
}

STATE_BY_CITY: dict[str, str] = {
    "dwarka": "Gujarat",
    "somnath": "Gujarat",
    "ahmedabad": "Gujarat",
    "porbandar": "Gujarat",
    "rajkot": "Gujarat",
    "bhuj": "Gujarat",
    "kutch": "Gujarat",
    "gir": "Gujarat",
    "vadodara": "Gujarat",
    "surat": "Gujarat",
    "junagadh": "Gujarat",
    "diu": "Gujarat",
    "shimla": "Himachal Pradesh",
    "manali": "Himachal Pradesh",
    "dharamshala": "Himachal Pradesh",
    "kufri": "Himachal Pradesh",
    "mashobra": "Himachal Pradesh",
}


def _parse_nights(label: str) -> int:
    match = NIGHTS_PATTERN.search(label or "")
    return int(match.group(1)) if match else 1


def _clean_place_name(value: str) -> str:
    text = re.sub(r"\s+", " ", (value or "").strip(" ,|·"))
    text = re.sub(r"\b(and|via|the)\b$", "", text, flags=re.IGNORECASE).strip()
    if not text:
        return ""
    return " ".join(word[:1].upper() + word[1:] for word in text.split(" ") if word)


def _looks_like_brochure_title(value: str) -> bool:
    text = (value or "").strip()
    if not text:
        return True
    if BROCHURE_TITLE_PATTERN.search(text):
        return True
    return len(text.split()) > 4 and text.upper() == text


def _bundle_text(bundle: ExtractedPackageBundle) -> str:
    parts = [
        bundle.destination.name,
        bundle.destination.description,
        bundle.package.title,
        bundle.package.tagline or "",
        bundle.itinerary.title,
        bundle.itinerary.tagline,
        bundle.itinerary.overview,
        " ".join(bundle.package.highlights),
        " ".join(item.text for item in bundle.itinerary.highlights),
        " ".join(day.title for day in bundle.itinerary.days),
        " ".join(bundle.places_mentioned),
    ]
    return " ".join(part for part in parts if part).lower()


def infer_destination_name(bundle: ExtractedPackageBundle) -> str:
    current = (bundle.destination.name or "").strip()
    if current and not _looks_like_brochure_title(current):
        return current

    text = _bundle_text(bundle)
    for city, state in STATE_BY_CITY.items():
        if re.search(rf"\b{re.escape(city)}\b", text):
            return state

    if bundle.destination.india_region == "west" and "gujarat" in text:
        return "Gujarat"

    cleaned = BROCHURE_TITLE_PATTERN.sub("", current).strip(" -|,")
    if cleaned and not _looks_like_brochure_title(cleaned):
        return cleaned

    return current or "Destination"


def _places_from_hotels(bundle: ExtractedPackageBundle) -> list[tuple[str, int, int]]:
    rows: list[tuple[str, int, int]] = []
    for hotel in sorted(bundle.itinerary.hotels, key=lambda item: item.sort_order):
        place = _clean_place_name(hotel.location.split(",")[0])
        if place:
            rows.append((place, _parse_nights(hotel.nights_label), hotel.sort_order))
    return rows


def _places_from_days(bundle: ExtractedPackageBundle) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for day in sorted(bundle.itinerary.days, key=lambda item: item.sort_order):
        for pattern in DAY_CITY_PATTERNS:
            match = pattern.search(day.title)
            if not match:
                continue
            place = _clean_place_name(match.group(1))
            key = place.lower()
            if place and key not in seen:
                seen.add(key)
                found.append(place)
    return found


def extract_route_places(bundle: ExtractedPackageBundle) -> list[str]:
    hotel_rows = _places_from_hotels(bundle)
    anchors = [place for place, nights, _ in hotel_rows if nights >= 2]
    if len(anchors) >= 2:
        return _dedupe_places(anchors)[:3]

    if hotel_rows:
        return _dedupe_places([place for place, _, _ in hotel_rows])[:3]

    day_places = _places_from_days(bundle)
    if day_places:
        return day_places[:3]

    mentioned: list[str] = []
    for place in bundle.places_mentioned:
        cleaned = _clean_place_name(place.split(",")[0])
        if cleaned and cleaned.lower() not in {item.lower() for item in mentioned}:
            mentioned.append(cleaned)
        if len(mentioned) >= 3:
            break
    return mentioned


def _dedupe_places(places: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for place in places:
        key = place.lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(place)
    return ordered


def infer_journey_theme(bundle: ExtractedPackageBundle) -> str:
    text = _bundle_text(bundle)
    for theme, keywords in THEME_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return theme
    return "Tour"


def format_place_list(places: list[str], *, max_places: int = 3) -> str:
    selected = places[:max_places]
    if not selected:
        return ""
    if len(selected) == 1:
        return selected[0]
    if len(selected) == 2:
        return f"{selected[0]} & {selected[1]}"
    return f"{selected[0]}, {selected[1]} & {selected[2]}"


def generate_package_title(bundle: ExtractedPackageBundle) -> str:
    route = format_place_list(extract_route_places(bundle))
    theme = infer_journey_theme(bundle)
    destination = infer_destination_name(bundle)

    if route and theme:
        return f"{route} {theme}"
    if route:
        return f"{route} Journey"
    if not _looks_like_brochure_title(bundle.package.title):
        return bundle.package.title.strip()
    return f"{destination} {theme}"


def _build_slug(title: str, duration_label: str | None) -> str:
    base = slugify(title, max_length=96)
    if duration_label:
        suffix = slugify(duration_label, max_length=24)
        if suffix:
            return slugify(f"{base}-{suffix}", max_length=128)
    return base


def apply_generated_names(bundle: ExtractedPackageBundle) -> ExtractedPackageBundle:
    destination_name = infer_destination_name(bundle)
    destination_slug = slugify(destination_name, max_length=128)
    package_title = generate_package_title(bundle)[:255]
    duration_label = bundle.package.duration_label or bundle.itinerary.duration_label
    package_slug = _build_slug(package_title, duration_label)
    itinerary_slug = slugify(f"{package_slug}-itinerary", max_length=128)

    return bundle.model_copy(
        update={
            "destination": bundle.destination.model_copy(
                update={"name": destination_name, "slug": destination_slug}
            ),
            "package": bundle.package.model_copy(
                update={"title": package_title, "slug": package_slug}
            ),
            "itinerary": bundle.itinerary.model_copy(
                update={"title": package_title, "slug": itinerary_slug}
            ),
        }
    )
