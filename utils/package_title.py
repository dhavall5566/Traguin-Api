"""Normalize marketing package / journey titles for display."""

from __future__ import annotations

import re

# Em dash, en dash, or spaced hyphen used as a title separator (not slug hyphens).
_TITLE_SEPARATOR = re.compile(r"\s*[—–]\s*|\s+-\s+")


def clean_package_title(title: str | None) -> str | None:
    if not title:
        return title
    cleaned = _TITLE_SEPARATOR.sub(" ", title)
    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
    return cleaned
