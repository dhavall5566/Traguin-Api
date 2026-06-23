from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.config import (
    CompanyStats,
    GlobalPageCta,
    NavigationLink,
    PageHero,
    PageMetadata,
    Redirect,
    SiteCta,
)
from schemas.config import (
    CompanyStatsRead,
    GlobalPageCtaRead,
    NavigationLinkRead,
    PageHeroRead,
    PageMetadataRead,
    RedirectRead,
    SiteCtaRead,
)
from schemas.pagination import PaginatedResponse
from utils.pagination import paginate
from utils.singleton import get_singleton_or_404

navigation_router = APIRouter()
site_ctas_router = APIRouter()
page_metadata_router = APIRouter()
page_heroes_router = APIRouter()
redirects_router = APIRouter()
company_stats_router = APIRouter()
global_page_cta_router = APIRouter()


@navigation_router.get("", response_model=PaginatedResponse[NavigationLinkRead])
def list_navigation_links(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = (
        db.query(NavigationLink)
        .filter(NavigationLink.is_visible.is_(True))
        .order_by(NavigationLink.menu_group, NavigationLink.sort_order, NavigationLink.label)
    )
    return paginate(query, limit, offset, transform=NavigationLinkRead.model_validate)


@site_ctas_router.get("", response_model=PaginatedResponse[SiteCtaRead])
def list_site_ctas(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(SiteCta).order_by(SiteCta.sort_order.nulls_last(), SiteCta.key)
    return paginate(query, limit, offset, transform=SiteCtaRead.model_validate)


@page_metadata_router.get("", response_model=PaginatedResponse[PageMetadataRead])
def list_page_metadata(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(PageMetadata).order_by(PageMetadata.page_key)
    return paginate(query, limit, offset, transform=PageMetadataRead.model_validate)


@page_metadata_router.get("/key/{page_key}", response_model=PageMetadataRead)
def get_page_metadata_by_key(page_key: str, db: Session = Depends(get_db)):
    item = db.query(PageMetadata).filter_by(page_key=page_key).one_or_none()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page metadata not found.")
    return item


@page_heroes_router.get("", response_model=PaginatedResponse[PageHeroRead])
def list_page_heroes(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(PageHero).order_by(PageHero.page_key, PageHero.region_variant)
    return paginate(query, limit, offset, transform=PageHeroRead.model_validate)


@page_heroes_router.get("/{hero_id}", response_model=PageHeroRead)
def get_page_hero(hero_id: UUID, db: Session = Depends(get_db)):
    item = db.get(PageHero, hero_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page hero not found.")
    return item


@redirects_router.get("", response_model=PaginatedResponse[RedirectRead])
def list_redirects(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Redirect).order_by(Redirect.old_path)
    return paginate(query, limit, offset, transform=RedirectRead.model_validate)


@redirects_router.get("/path/{old_path:path}", response_model=RedirectRead)
def get_redirect_by_path(old_path: str, db: Session = Depends(get_db)):
    if not old_path.startswith("/"):
        old_path = f"/{old_path}"
    item = db.query(Redirect).filter_by(old_path=old_path).one_or_none()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Redirect not found.")
    return item


@company_stats_router.get("", response_model=CompanyStatsRead)
def get_company_stats(db: Session = Depends(get_db)):
    return get_singleton_or_404(db, CompanyStats)


@global_page_cta_router.get("", response_model=GlobalPageCtaRead)
def get_global_page_cta(db: Session = Depends(get_db)):
    return get_singleton_or_404(db, GlobalPageCta)
