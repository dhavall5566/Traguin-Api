from __future__ import annotations

import json
import re
from typing import Any

import httpx

from config import settings
from schemas.package_import import ExtractedItineraryDraft, ExtractedPackageBundle

GROQ_CHAT_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_MODEL = "llama-3.3-70b-versatile"

EXTRACTION_SYSTEM = """You extract structured travel package data from PDF brochure text.
Return ONLY a single valid JSON object matching the schema below. No markdown, no commentary.

Schema:
{
  "destination": {
    "name": string,
    "slug": string | null,
    "country": string | null,
    "region": "domestic" | "international",
    "india_region": "north" | "east" | "south" | "west" | null,
    "description": string,
    "starting_price": integer | null,
    "moods": string[],
    "is_domestic": boolean | null
  },
  "package": {
    "title": string,
    "slug": string | null,
    "tagline": string | null,
    "duration_label": string,
    "duration_days": integer | null,
    "starting_price": integer | null,
    "price_on_request": boolean,
    "highlights": string[],
    "moods": string[]
  },
  "itinerary": {
    "title": string,
    "slug": string | null,
    "tagline": string,
    "overview": string,
    "duration_label": string,
    "duration_days": integer,
    "starting_price": integer | null,
    "price_on_request": boolean,
    "price_note": string | null,
    "days": [
      {
        "day_number": integer,
        "title": string,
        "description": string,
        "activities": string[],
        "sort_order": integer
      }
    ],
    "hotels": [
      {
        "name": string,
        "location": string,
        "nights_label": string,
        "description": string | null,
        "category_label": string | null,
        "sort_order": integer
      }
    ],
    "inclusions": [
      { "kind": "included" | "excluded", "text": string, "sort_order": integer }
    ],
    "highlights": [
      { "text": string, "sort_order": integer }
    ]
  },
  "places_mentioned": string[]
}

Rules:
- Map ✔/included lists to kind "included" and ✘/excluded to kind "excluded".
- For hotel option tables with multiple tiers (Standard/Deluxe/Premium) per city, emit ONE row per tier with category_label set to the tier name.
- Parse duration like "7D/6N" into duration_label and duration_days (nights+1 or days from label).
- If price is "On Request" or non-numeric, set starting_price null and price_on_request true.
- Never use 0 as a placeholder price; use null with price_on_request true instead.
- places_mentioned: every named landmark/temple/city attraction worth a photo (be thorough).
- Infer india_region for Indian domestic destinations (Gujarat -> west).
- Use brochure title/overview for descriptions where appropriate.

Destination vs package naming (critical for states with many packages):
- destination.name must be the broad region only (state/country), e.g. "Gujarat", "Himachal Pradesh", "Bali" — never the brochure marketing trip name.
- destination.slug: short region slug, e.g. "gujarat".
- package.title and itinerary.title: descriptive route-based names from cities/places covered (e.g. "Dwarka & Somnath Pilgrimage"), not agency brochure titles like "TRAGUIN PREMIUM GUJARAT TOUR".
- Multiple PDFs for the same state share one destination; each PDF becomes a distinct package named after its route/places.

Itinerary day cards (critical):
- Each day "description" must be one evocative 1–2 sentence paragraph (not a bullet or fragment).
- Each "activities" entry MUST use "Category Label: descriptive details" with a colon separator.
- Prefer 2–5 categorized activities per day (not bare landmark names).
- Use these labels when applicable: Sightseeing Included, Evening Experience, Overnight Stay, Meals Included, Optional Activities, Transfer Included, Drop Location.
- Pull sightseeing, meals, and overnight stay from the PDF day block, hotel table, and inclusions list.

Example activities for one day:
[
  "Sightseeing Included: Himalayan Expressway Scenic Overlooks, Timber Trail Pass.",
  "Evening Experience: Leisurely resort settling followed by a custom multi-cuisine welcome buffet.",
  "Overnight Stay: Luxury Mountain Resort in Shimla.",
  "Meals Included: Gourmet Dinner."
]
"""

ENRICHMENT_SYSTEM = """You enrich travel itinerary day plans for a luxury travel CMS.
Return ONLY valid JSON: { "days": [ { "day_number", "title", "description", "activities" } ] }

Rules:
- Keep day_number and sort_order alignment with the input; one object per input day.
- "description": one evocative 1–2 sentence paragraph summarizing the day.
- Each activity string MUST be "Category Label: descriptive details" (exactly one colon).
- Labels: Sightseeing Included, Evening Experience, Overnight Stay, Meals Included, Optional Activities, Transfer Included, Drop Location.
- Group related sights into Sightseeing Included; add Overnight Stay from hotels when the day ends at a property; add Meals Included when breakfast/lunch/dinner apply.
- 2–5 activities per day typical; expand plain activity names into categorized lines with richer detail from PDF/context.
- Do not invent major destinations not supported by the source text or context.
"""


def _require_groq_key() -> str:
    key = settings.groq_api_key
    if not key:
        raise RuntimeError("GROQ_API_KEY is not configured.")
    return key


def _parse_json_response(content: str) -> dict[str, Any]:
    text = content.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def _chat(messages: list[dict[str, str]], *, temperature: float = 0.1) -> str:
    response = httpx.post(
        GROQ_CHAT_URL,
        headers={
            "Authorization": f"Bearer {_require_groq_key()}",
            "Content-Type": "application/json",
        },
        json={
            "model": DEFAULT_MODEL,
            "messages": messages,
            "temperature": temperature,
            "response_format": {"type": "json_object"},
        },
        timeout=120.0,
    )
    response.raise_for_status()
    payload = response.json()
    return payload["choices"][0]["message"]["content"]


def _activities_need_enrichment(itinerary: ExtractedItineraryDraft) -> bool:
    for day in itinerary.days:
        if not day.activities:
            continue
        if any(":" not in activity for activity in day.activities):
            return True
    return False


def enrich_itinerary_day_plans(
    itinerary: ExtractedItineraryDraft,
    *,
    pdf_text: str = "",
) -> ExtractedItineraryDraft:
    """Expand plain day activities into categorized plan lines for the itinerary UI."""
    if not itinerary.days or not _activities_need_enrichment(itinerary):
        return itinerary

    context = {
        "title": itinerary.title,
        "overview": itinerary.overview,
        "duration_label": itinerary.duration_label,
        "duration_days": itinerary.duration_days,
        "hotels": [hotel.model_dump() for hotel in itinerary.hotels],
        "inclusions": [inc.model_dump() for inc in itinerary.inclusions],
        "days": [day.model_dump() for day in itinerary.days],
    }
    user_prompt = (
        "Enrich these itinerary days into categorized plan cards.\n\n"
        f"CONTEXT JSON:\n{json.dumps(context, ensure_ascii=False, indent=2)}\n"
    )
    trimmed_pdf = pdf_text.strip()
    if trimmed_pdf:
        user_prompt += f"\n--- PDF TEXT (source) ---\n{trimmed_pdf[:50000]}\n--- END PDF ---\n"

    content = _chat(
        [
            {"role": "system", "content": ENRICHMENT_SYSTEM},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.1,
    )
    raw = _parse_json_response(content)
    enriched_by_day = {
        int(item["day_number"]): item
        for item in raw.get("days", [])
        if isinstance(item, dict) and "day_number" in item
    }

    updated_days = []
    for day in itinerary.days:
        enriched = enriched_by_day.get(day.day_number)
        if not enriched:
            updated_days.append(day)
            continue
        activities = enriched.get("activities") or day.activities
        if not isinstance(activities, list):
            activities = day.activities
        updated_days.append(
            day.model_copy(
                update={
                    "title": enriched.get("title") or day.title,
                    "description": enriched.get("description") or day.description,
                    "activities": [str(a) for a in activities if str(a).strip()],
                }
            )
        )

    return itinerary.model_copy(update={"days": updated_days})


def _normalize_pricing(bundle: ExtractedPackageBundle) -> ExtractedPackageBundle:
    """Treat missing/zero PDF prices as on-request instead of ₹0."""
    dest = bundle.destination
    pkg = bundle.package
    itin = bundle.itinerary

    dest_price = dest.starting_price
    if dest_price is None or dest_price <= 0:
        dest = dest.model_copy(update={"starting_price": None})

    pkg_on_request = pkg.price_on_request or pkg.starting_price is None or pkg.starting_price <= 0
    pkg = pkg.model_copy(
        update={
            "price_on_request": pkg_on_request,
            "starting_price": None if pkg_on_request else pkg.starting_price,
        }
    )

    itin_on_request = (
        itin.price_on_request or itin.starting_price is None or itin.starting_price <= 0
    )
    itin = itin.model_copy(
        update={
            "price_on_request": itin_on_request,
            "starting_price": None if itin_on_request else itin.starting_price,
        }
    )

    return bundle.model_copy(
        update={"destination": dest, "package": pkg, "itinerary": itin}
    )


def extract_package_from_text(pdf_text: str) -> tuple[ExtractedPackageBundle, dict[str, Any]]:
    user_prompt = (
        "Extract the complete travel package from this PDF text.\n\n"
        f"--- PDF TEXT START ---\n{pdf_text}\n--- PDF TEXT END ---"
    )
    messages = [
        {"role": "system", "content": EXTRACTION_SYSTEM},
        {"role": "user", "content": user_prompt},
    ]

    last_error: Exception | None = None
    for attempt in range(2):
        try:
            content = _chat(
                messages if attempt == 0 else messages + [
                    {
                        "role": "user",
                        "content": "Your previous reply was not valid JSON. Reply with ONLY the JSON object, no markdown.",
                    }
                ],
                temperature=0.0 if attempt else 0.1,
            )
            raw = _parse_json_response(content)
            bundle = ExtractedPackageBundle.model_validate(raw)
            bundle = _normalize_pricing(bundle)
            enriched_itinerary = enrich_itinerary_day_plans(bundle.itinerary, pdf_text=pdf_text)
            bundle = bundle.model_copy(update={"itinerary": enriched_itinerary})
            return bundle, raw
        except (json.JSONDecodeError, ValueError) as exc:
            last_error = exc
    raise ValueError(f"LLM returned invalid JSON after retry: {last_error}") from last_error
