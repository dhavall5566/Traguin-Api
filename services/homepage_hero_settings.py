from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from sqlalchemy.orm import Session

from models.config import CompanyStats
from models.packages import Package

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


def has_homepage_hero_visibility_configured(stats: CompanyStats | None) -> bool:
    return _meta_entry(getattr(stats, "homepage_stats", None) if stats else None) is not None


def select_homepage_hero_packages(packages: list, stats: CompanyStats | None) -> list:
    settings = read_homepage_hero_settings(stats)
    published = [pkg for pkg in packages if getattr(pkg, "is_published", False)]

    if has_homepage_hero_visibility_configured(stats):
        visible = set(settings["visible_package_ids"])
        selected = [pkg for pkg in published if str(pkg.id) in visible]
        selected.sort(
            key=lambda pkg: (
                pkg.featured_sort_order if pkg.featured_sort_order is not None else 999,
                pkg.title,
            )
        )
        return selected

    featured = [pkg for pkg in published if getattr(pkg, "is_featured", False)]
    featured.sort(
        key=lambda pkg: (
            pkg.featured_sort_order if pkg.featured_sort_order is not None else 999,
            pkg.title,
        )
    )

    visible_ids = settings["visible_package_ids"]
    if visible_ids:
        visible = set(visible_ids)
        return [pkg for pkg in featured if str(pkg.id) in visible]
    return featured[: settings["hero_slider_max_items"]]


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


@dataclass
class HomepagePackageVisibilityIssue:
    package_id: str
    serial_code: str | None
    title: str
    issue: str


@dataclass
class HomepagePackageVisibilityAudit:
    visible_count: int
    featured_count: int
    published_count: int
    issues: list[HomepagePackageVisibilityIssue]

    @property
    def ok(self) -> bool:
        return not self.issues


def audit_homepage_package_visibility(db: Session, stats: CompanyStats) -> HomepagePackageVisibilityAudit:
    settings = read_homepage_hero_settings(stats)
    visible_ids = set(settings["visible_package_ids"])
    packages = db.query(Package).all()
    issues: list[HomepagePackageVisibilityIssue] = []

    for pkg in packages:
        pkg_id = str(pkg.id)
        if pkg.is_featured and pkg_id not in visible_ids:
            issues.append(
                HomepagePackageVisibilityIssue(
                    package_id=pkg_id,
                    serial_code=pkg.serial_code,
                    title=pkg.title,
                    issue="featured_not_visible",
                )
            )
        if pkg_id in visible_ids and not pkg.is_featured:
            issues.append(
                HomepagePackageVisibilityIssue(
                    package_id=pkg_id,
                    serial_code=pkg.serial_code,
                    title=pkg.title,
                    issue="visible_not_featured",
                )
            )
        if pkg_id in visible_ids and not pkg.is_published:
            issues.append(
                HomepagePackageVisibilityIssue(
                    package_id=pkg_id,
                    serial_code=pkg.serial_code,
                    title=pkg.title,
                    issue="visible_unpublished",
                )
            )

    return HomepagePackageVisibilityAudit(
        visible_count=len(visible_ids),
        featured_count=sum(1 for pkg in packages if pkg.is_featured),
        published_count=sum(1 for pkg in packages if pkg.is_published),
        issues=issues,
    )


def repair_homepage_package_visibility(db: Session, stats: CompanyStats) -> HomepagePackageVisibilityAudit:
    if not has_homepage_hero_visibility_configured(stats):
        return audit_homepage_package_visibility(db, stats)

    settings = read_homepage_hero_settings(stats)
    visible_ids = list(settings["visible_package_ids"])
    packages_by_id = {str(pkg.id): pkg for pkg in db.query(Package).all()}
    featured_count = sum(1 for pkg in packages_by_id.values() if pkg.is_featured)
    next_visible: list[str] = []
    changed = False

    for index, package_id in enumerate(visible_ids, start=1):
        pkg = packages_by_id.get(package_id)
        if pkg is None or not pkg.is_published:
            changed = True
            continue
        next_visible.append(package_id)
        if not pkg.is_featured:
            pkg.is_featured = True
            if pkg.featured_sort_order is None:
                pkg.featured_sort_order = featured_count + index
            featured_count += 1
            changed = True

    visible_set = set(next_visible)
    for pkg in packages_by_id.values():
        if pkg.is_featured and str(pkg.id) not in visible_set:
            pkg.is_featured = False
            pkg.featured_sort_order = None
            changed = True

    if next_visible != visible_ids:
        write_homepage_hero_settings(stats, visible_package_ids=next_visible)
        changed = True

    audit = audit_homepage_package_visibility(db, stats)
    if changed:
        db.flush()
    return audit
