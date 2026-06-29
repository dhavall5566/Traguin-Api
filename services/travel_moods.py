"""Canonical travel moods for packages and destinations (CMS filter values)."""

from __future__ import annotations

CANONICAL_TRAVEL_MOODS: frozenset[str] = frozenset(
    {
        "luxury",
        "adventure",
        "romantic",
        "family",
        "solo",
        "cultural",
        "wildlife",
        "beach",
        "nature",
        "spiritual",
    }
)

MOOD_ALIASES: dict[str, str] = {
    "family": "family",
    "luxury": "luxury",
    "romantic": "romantic",
    "honeymoon": "romantic",
    "nature": "nature",
    "adventure": "adventure",
    "beach": "beach",
    "wildlife": "wildlife",
    "wellness": "spiritual",
    "spiritual": "spiritual",
    "culture": "cultural",
    "cultural": "cultural",
    "pilgrimage": "spiritual",
    "heritage": "cultural",
    "corporate": "luxury",
    "mice": "luxury",
    "solo": "solo",
    "senior": "family",
    "girls-trip": "adventure",
    "girls trip": "adventure",
}

# Curated from brochure / PDF package descriptions at insert time.
PACKAGE_TRAVEL_MOODS: dict[str, list[str]] = {
    # Kashmir (JK)
    "jk-001-kashmir-paradise-family": ["family", "luxury", "nature"],
    "jk-002-srinagar-gulmarg-premium-family": ["family", "luxury", "nature"],
    "jk-003-srinagar-pahalgam-gulmarg-dal-lake": ["family", "luxury", "nature", "cultural"],
    "jk-004-romantic-kashmir-honeymoon": ["romantic", "luxury"],
    "jk-006-luxury-kashmir-escape": ["luxury", "romantic", "nature"],
    "jk-007-kashmir-great-lakes-trek": ["adventure", "nature"],
    "jk-010-kashmir-complete": ["family", "luxury", "nature", "cultural"],
    # Himachal (HP)
    "hp-003-shimla-manali-classic-alpine-luxury": ["family", "romantic", "luxury", "nature"],
    "hp-004-shimla-manali-dharamshala-explorer": ["family", "adventure", "nature", "cultural"],
    "hp-006-romantic-himachal-honeymoon": ["romantic", "luxury"],
    "hp-007-snow-romance-manali-honeymoon": ["romantic", "luxury", "adventure"],
    "hp-009-girls-trip-manali": ["adventure", "nature"],
    "hp-010-relaxed-shimla-escape": ["family", "luxury", "cultural"],
    "hp-011-spiti-valley-explorer": ["adventure", "nature"],
    "hp-012-premium-kaza-expedition": ["adventure", "luxury", "nature"],
    "hp-013-luxury-himachal-retreat": ["family", "luxury", "nature", "spiritual"],
    "hp-014-oberoi-himachal-experience": ["luxury", "romantic"],
    "hp-015-corporate-himachal-mice": ["luxury", "cultural"],
    "hp-017-dharamshala-escape": ["family", "spiritual", "cultural", "nature"],
    "hp-018-shimla-kasol-delight": ["family", "adventure", "cultural"],
    "hp-019-manali-dharamshala-family": ["family", "luxury", "nature"],
    "hp-020-himachal-panorama": ["family", "luxury", "nature"],
    # Gujarat (GJ)
    "gj-003-sasan-gir-wildlife-safari": ["wildlife", "luxury", "family", "nature"],
    "gj-004-rann-of-kutch-luxury-extravaganza": ["cultural", "luxury", "nature"],
    "gj-005-divine-statue-of-unity-circuit": ["cultural", "spiritual", "family"],
    # Kerala (KL)
    "kl-001-munnar-thekkady-alleppey-family": ["family", "nature", "luxury"],
    "kl-002-cochin-munnar-kovalam-grand-family": ["family", "beach", "nature", "luxury"],
    "kl-003-munnar-kochi-family": ["family", "cultural", "nature"],
    "kl-005-romantic-honeymoon-munnar-alleppey": ["romantic", "nature", "luxury"],
    "kl-006-honeymoon-romance-munnar-kovalam": ["romantic", "beach", "luxury"],
    "kl-009-senior-citizen-kumarakom-relaxed": ["family", "spiritual", "nature"],
    "kl-010-wayanad-adventure-escape": ["adventure", "nature", "wildlife"],
}


def normalize_travel_mood(raw: str) -> str | None:
    key = raw.strip().lower()
    if key in CANONICAL_TRAVEL_MOODS:
        return key
    return MOOD_ALIASES.get(key)


def normalize_travel_moods(raw: list[str] | None) -> list[str]:
    if not raw:
        return []
    seen: set[str] = set()
    result: list[str] = []
    for item in raw:
        mood = normalize_travel_mood(item)
        if mood and mood not in seen:
            seen.add(mood)
            result.append(mood)
    return result


def infer_travel_moods_from_slug(slug: str) -> list[str]:
    slug_lower = slug.lower()
    inferred: list[str] = []

    def add(*moods: str) -> None:
        for mood in moods:
            if mood not in inferred:
                inferred.append(mood)

    if any(k in slug_lower for k in ("honeymoon", "romantic", "romance")):
        add("romantic", "luxury")
    if "family" in slug_lower or "senior" in slug_lower:
        add("family")
    if any(k in slug_lower for k in ("trek", "spiti", "adventure", "girls-trip", "wayanad")):
        add("adventure")
    if any(k in slug_lower for k in ("wildlife", "gir", "safari")):
        add("wildlife")
    if any(k in slug_lower for k in ("kutch", "statue", "unity", "heritage", "dharamshala", "shimla")):
        add("cultural")
    if "unity" in slug_lower or "divine" in slug_lower or "senior" in slug_lower:
        add("spiritual")
    if "kovalam" in slug_lower or "beach" in slug_lower:
        add("beach")
    if "luxury" in slug_lower or "oberoi" in slug_lower or "premium" in slug_lower:
        add("luxury")
    if any(
        k in slug_lower
        for k in ("munnar", "manali", "shimla", "kashmir", "kerala", "valley", "alpine", "panorama")
    ):
        add("nature")

    return inferred or ["luxury"]


def travel_moods_for_package(slug: str, fallback: list[str] | None = None) -> list[str]:
    if slug in PACKAGE_TRAVEL_MOODS:
        return list(PACKAGE_TRAVEL_MOODS[slug])
    normalized = normalize_travel_moods(fallback)
    if normalized:
        return normalized
    return infer_travel_moods_from_slug(slug)


def aggregate_destination_moods(package_mood_lists: list[list[str]]) -> list[str]:
    seen: set[str] = set()
    aggregated: list[str] = []
    for moods in package_mood_lists:
        for mood in moods:
            if mood not in seen:
                seen.add(mood)
                aggregated.append(mood)
    return aggregated
