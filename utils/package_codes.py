"""Parse and derive package serial / TRAGUIN tour codes."""

from __future__ import annotations

import re

SLUG_SERIAL_RE = re.compile(r"^([a-z]{2,3})-(\d{3})-")
SERIAL_HIGHLIGHT_RE = re.compile(r"Serial(?:\s+(?:code|ID))?\s+([A-Z]{2,3}-\d{3})", re.I)
TOUR_HIGHLIGHT_RE = re.compile(
    r"(?:TRAGUIN\s+tour\s+code|Tour\s+code)\s+(TRAGUIN[^\|]+?)(?:\s*\||\s*$)",
    re.I,
)


def serial_code_from_slug(slug: str) -> str | None:
    match = SLUG_SERIAL_RE.match(slug)
    if match is None:
        return None
    return f"{match.group(1).upper()}-{match.group(2)}"


def parse_codes_from_highlights(highlights: list[str]) -> tuple[str | None, str | None]:
    text = " | ".join(highlights)
    serial_match = SERIAL_HIGHLIGHT_RE.search(text)
    tour_match = TOUR_HIGHLIGHT_RE.search(text)
    serial = serial_match.group(1).upper() if serial_match else None
    tour = tour_match.group(1).strip() if tour_match else None
    return serial, tour


def resolve_package_codes(slug: str, highlight_texts: list[str] | None = None) -> tuple[str, str]:
    highlights = highlight_texts or []
    highlight_serial, highlight_tour = parse_codes_from_highlights(highlights)
    serial = highlight_serial or serial_code_from_slug(slug)
    if not serial:
        raise ValueError(f"Could not derive serial code for package slug {slug!r}")
    tour = highlight_tour or f"TRAGUIN-{serial}"
    return serial, tour
