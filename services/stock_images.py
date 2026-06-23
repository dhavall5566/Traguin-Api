from __future__ import annotations

import httpx

from config import settings
from schemas.package_import import SourcedPlaceImage
from utils.slugify import slugify

PEXELS_SEARCH_URL = "https://api.pexels.com/v1/search"


def _require_pexels_key() -> str | None:
    return settings.pexels_api_key or None


def search_place_image(place: str) -> SourcedPlaceImage:
    query = f"{place} India landmark travel"
    key = _require_pexels_key()
    if not key:
        return SourcedPlaceImage(
            place=place,
            search_query=query,
            error="PEXELS_API_KEY is not configured.",
        )

    try:
        response = httpx.get(
            PEXELS_SEARCH_URL,
            params={"query": query, "per_page": 1, "orientation": "landscape"},
            headers={"Authorization": key},
            timeout=30.0,
        )
        response.raise_for_status()
        photos = response.json().get("photos") or []
        if not photos:
            return SourcedPlaceImage(
                place=place,
                search_query=query,
                error="No photos found.",
            )
        photo = photos[0]
        src = photo.get("src") or {}
        return SourcedPlaceImage(
            place=place,
            search_query=query,
            url=src.get("original") or src.get("large2x") or src.get("large"),
            preview_url=src.get("medium") or src.get("small"),
            photographer=(photo.get("photographer") or None),
            width=photo.get("width"),
            height=photo.get("height"),
        )
    except httpx.HTTPError as exc:
        return SourcedPlaceImage(
            place=place,
            search_query=query,
            error=f"Pexels request failed: {exc.__class__.__name__}",
        )


def place_media_slug(place: str) -> str:
    return slugify(f"package-{place}", max_length=255)
