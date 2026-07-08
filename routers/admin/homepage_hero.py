from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.config import CompanyStats
from models.packages import Package
from schemas.homepage_hero import (
    HomepageHeroSliderOrderUpdate,
    HomepageHeroSliderSettingsRead,
    HomepageHeroSliderSettingsUpdate,
)
from services.homepage_hero_settings import (
    _meta_entry,
    get_or_create_company_stats,
    read_homepage_hero_settings,
    repair_homepage_package_visibility,
    write_homepage_hero_settings,
)
from utils.db import commit_or_raise

router = APIRouter()


def _featured_packages(db: Session) -> list[Package]:
    return (
        db.query(Package)
        .filter(Package.is_featured.is_(True))
        .order_by(Package.featured_sort_order.asc().nullslast(), Package.title.asc())
        .all()
    )


def _sync_feature_flags_for_visibility(
    db: Session,
    *,
    previous_visible_ids: list[str],
    next_visible_ids: list[UUID],
) -> None:
    previous = set(previous_visible_ids)
    next_visible = {str(item) for item in next_visible_ids}
    removed = previous - next_visible
    added = next_visible - previous

    if removed:
        removed_uuids = [UUID(value) for value in removed]
        for pkg in db.query(Package).filter(Package.id.in_(removed_uuids)).all():
            pkg.is_featured = False
            pkg.featured_sort_order = None

    if added:
        featured_count = db.query(Package).filter(Package.is_featured.is_(True)).count()
        for index, package_id in enumerate(
            [value for value in next_visible_ids if str(value) in added],
            start=1,
        ):
            pkg = db.get(Package, package_id)
            if pkg is None:
                continue
            pkg.is_featured = True
            if pkg.featured_sort_order is None:
                pkg.featured_sort_order = featured_count + index


def _normalize_visible_ids(
    db: Session,
    stats: CompanyStats,
    *,
    persist: bool = False,
) -> HomepageHeroSliderSettingsRead:
    settings = read_homepage_hero_settings(stats)
    featured = _featured_packages(db)
    featured_ids = {str(pkg.id) for pkg in featured}
    meta = _meta_entry(stats.homepage_stats)

    if meta is None:
        visible = (
            [pkg.id for pkg in featured[: settings["hero_slider_max_items"]]]
            if featured
            else []
        )
        write_homepage_hero_settings(stats, visible_package_ids=visible)
        persist = True
    else:
        visible = [UUID(value) for value in settings["visible_package_ids"]]
        featured_visible = [item for item in visible if str(item) in featured_ids]
        if persist and featured_visible != visible:
            write_homepage_hero_settings(stats, visible_package_ids=featured_visible)
            visible = featured_visible

    if persist:
        repair_homepage_package_visibility(db, stats)
        commit_or_raise(db)
        db.refresh(stats)
        current_settings = read_homepage_hero_settings(stats)
        visible = [UUID(value) for value in current_settings["visible_package_ids"]]
    else:
        current_settings = read_homepage_hero_settings(stats)

    return HomepageHeroSliderSettingsRead(
        hero_slider_max_items=current_settings["hero_slider_max_items"],
        visible_package_ids=visible,
    )


@router.get("/settings", response_model=HomepageHeroSliderSettingsRead)
def get_homepage_hero_slider_settings(db: Session = Depends(get_db)):
    stats = get_or_create_company_stats(db)
    return _normalize_visible_ids(db, stats, persist=True)


@router.patch("/settings", response_model=HomepageHeroSliderSettingsRead)
def update_homepage_hero_slider_settings(
    payload: HomepageHeroSliderSettingsUpdate,
    db: Session = Depends(get_db),
):
    stats = get_or_create_company_stats(db)
    current = read_homepage_hero_settings(stats)

    update_data = payload.model_dump(exclude_unset=True)
    next_visible = update_data.get("visible_package_ids")
    next_max = update_data.get("hero_slider_max_items", current["hero_slider_max_items"])

    if next_visible is None:
        featured_ids = {str(pkg.id) for pkg in _featured_packages(db)}
        next_visible = [
            UUID(value)
            for value in current["visible_package_ids"]
            if value in featured_ids
        ]
    else:
        _sync_feature_flags_for_visibility(
            db,
            previous_visible_ids=current["visible_package_ids"],
            next_visible_ids=next_visible,
        )
        db.flush()

    featured_ids = {pkg.id for pkg in _featured_packages(db)}
    invalid = [pkg_id for pkg_id in next_visible if pkg_id not in featured_ids]
    if invalid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="One or more packages could not be marked visible on the homepage hero slider.",
        )

    if len(next_visible) > next_max:
        if update_data.get("visible_package_ids") is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"You can only show up to {next_max} packages on the homepage hero slider.",
            )
        next_visible = next_visible[:next_max]

    write_homepage_hero_settings(
        stats,
        hero_slider_max_items=update_data.get("hero_slider_max_items"),
        visible_package_ids=next_visible,
    )
    commit_or_raise(db)
    db.refresh(stats)
    return _normalize_visible_ids(db, stats)


@router.put("/order", response_model=HomepageHeroSliderSettingsRead)
def update_homepage_hero_slider_order(
    payload: HomepageHeroSliderOrderUpdate,
    db: Session = Depends(get_db),
):
    package_ids = list(dict.fromkeys(payload.package_ids))
    packages = db.query(Package).filter(Package.id.in_(package_ids)).all()
    packages_by_id = {pkg.id: pkg for pkg in packages}

    if len(packages_by_id) != len(package_ids):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="One or more packages were not found.",
        )

    for index, package_id in enumerate(package_ids):
        package = packages_by_id[package_id]
        package.is_featured = True
        package.featured_sort_order = index + 1

    commit_or_raise(db)
    stats = get_or_create_company_stats(db)
    return _normalize_visible_ids(db, stats)
