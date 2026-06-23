from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from models.config import CompanyStats

HERO_SLIDER_META_ID = "__hero_slider_settings"
DEFAULT_HERO_SLIDER_MAX_ITEMS = 8
MIN_HERO_SLIDER_MAX_ITEMS = 1
MAX_HERO_SLIDER_MAX_ITEMS = 20


def clamp_hero_slider_max_items(value: int | None) -> int:
    if value is None:
        return DEFAULT_HERO_SLIDER_MAX_ITEMS
    return max(MIN_HERO_SLIDER_MAX_ITEMS, min(MAX_HERO_SLIDER_MAX_ITEMS, int(value)))


def _meta_entry(homepage_stats: list | None) -> dict | None:
    for item in homepage_stats or []:
        if isinstance(item, dict) and item.get("id") == HERO_SLIDER_META_ID:
            return item
    return None


def _strip_meta(homepage_stats: list | None) -> list:
    return [
        item
        for item in (homepage_stats or [])
        if not (isinstance(item, dict) and item.get("id") == HERO_SLIDER_META_ID)
    ]


def read_homepage_hero_settings(stats: CompanyStats | None) -> dict:
    meta = _meta_entry(getattr(stats, "homepage_stats", None) if stats else None)
    max_items = clamp_hero_slider_max_items(
        meta.get("hero_slider_max_items") if meta else None
    )
    raw_visible = meta.get("visible_package_ids") if meta else []
    visible_package_ids: list[str] = []
    if isinstance(raw_visible, list):
        visible_package_ids = [str(item) for item in raw_visible if item]
    return {
        "hero_slider_max_items": max_items,
        "visible_package_ids": visible_package_ids,
    }


def write_homepage_hero_settings(
    stats: CompanyStats,
    *,
    hero_slider_max_items: int | None = None,
    visible_package_ids: list[UUID | str] | None = None,
) -> dict:
    current = read_homepage_hero_settings(stats)
    next_max = clamp_hero_slider_max_items(
        hero_slider_max_items if hero_slider_max_items is not None else current["hero_slider_max_items"]
    )
    next_visible = (
        [str(item) for item in visible_package_ids]
        if visible_package_ids is not None
        else current["visible_package_ids"]
    )
    next_visible = next_visible[:next_max]

    stats.homepage_stats = [
        {
            "id": HERO_SLIDER_META_ID,
            "hero_slider_max_items": next_max,
            "visible_package_ids": next_visible,
        },
        *_strip_meta(stats.homepage_stats),
    ]
    return read_homepage_hero_settings(stats)


def get_or_create_company_stats(db: Session) -> CompanyStats:
    stats = db.get(CompanyStats, 1)
    if stats is None:
        stats = CompanyStats(id=1, homepage_stats=[], trust_bar_stats=[], gallery_stats=[])
        db.add(stats)
        db.flush()
    return stats
