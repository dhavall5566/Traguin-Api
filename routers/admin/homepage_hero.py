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
    get_or_create_company_stats,
    read_homepage_hero_settings,
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


def _normalize_visible_ids(
    db: Session,
    stats: CompanyStats,
    *,
    persist: bool = False,
) -> HomepageHeroSliderSettingsRead:
    settings = read_homepage_hero_settings(stats)
    featured = _featured_packages(db)
    featured_ids = {str(pkg.id) for pkg in featured}

    visible = [UUID(value) for value in settings["visible_package_ids"] if value in featured_ids]
    if not visible and featured:
        visible = [pkg.id for pkg in featured[: settings["hero_slider_max_items"]]]
        write_homepage_hero_settings(stats, visible_package_ids=visible)
        persist = True

    if persist:
        commit_or_raise(db)
        db.refresh(stats)

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
    featured = _featured_packages(db)
    featured_ids = {pkg.id for pkg in featured}

    update_data = payload.model_dump(exclude_unset=True)
    next_visible = update_data.get("visible_package_ids")
    if next_visible is not None:
        invalid = [pkg_id for pkg_id in next_visible if pkg_id not in featured_ids]
        if invalid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only featured packages can be marked visible on the homepage hero slider.",
            )

    current = read_homepage_hero_settings(stats)
    next_max = update_data.get("hero_slider_max_items", current["hero_slider_max_items"])
    if next_visible is None:
        next_visible = [
            UUID(value)
            for value in current["visible_package_ids"]
            if value in {str(item) for item in featured_ids}
        ]

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
