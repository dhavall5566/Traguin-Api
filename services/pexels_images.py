from __future__ import annotations

from typing import Any

import httpx

from config import settings

PEXELS_SEARCH_URL = "https://api.pexels.com/v1/search"

# Mis-tagged or off-theme photos that Pexels search may surface for Kashmir queries.
BLOCKED_PEXELS_IDS: frozenset[int] = frozenset({35030068})


class PexelsError(RuntimeError):
    pass


def get_pexels_api_key() -> str | None:
    return settings.pexels_api_key


def search_pexels_photo(
    query: str,
    *,
    page: int = 1,
    per_page: int = 15,
    exclude_urls: set[str] | None = None,
    exclude_pexels_ids: set[int] | None = None,
) -> dict[str, Any] | None:
    api_key = get_pexels_api_key()
    if not api_key:
        raise PexelsError("PEXELS_API_KEY is not configured in api/.env.")

    blocked_urls = exclude_urls or set()
    blocked_ids = BLOCKED_PEXELS_IDS | (exclude_pexels_ids or set())

    for current_page in range(page, page + 5):
        response = httpx.get(
            PEXELS_SEARCH_URL,
            params={
                "query": query,
                "page": current_page,
                "per_page": per_page,
                "orientation": "landscape",
            },
            headers={"Authorization": api_key},
            timeout=30.0,
        )
        response.raise_for_status()
        photos = response.json().get("photos") or []
        if not photos:
            break

        for photo in photos:
            pexels_id = photo.get("id")
            if pexels_id is not None and pexels_id in blocked_ids:
                continue

            src = photo.get("src") or {}
            url = src.get("original") or src.get("large2x") or src.get("large")
            if not url or url in blocked_urls:
                continue

            photographer = photo.get("photographer") or "Pexels contributor"
            return {
                "url": url,
                "alt_text": f"{query} — photo by {photographer} on Pexels",
                "width": photo.get("width"),
                "height": photo.get("height"),
                "photographer": photographer,
                "pexels_id": pexels_id,
            }

    return None
