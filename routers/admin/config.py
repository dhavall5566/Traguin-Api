from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
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
    CompanyStatsBase,
    CompanyStatsRead,
    CompanyStatsUpdate,
    GlobalPageCtaBase,
    GlobalPageCtaRead,
    GlobalPageCtaUpdate,
    NavigationLinkCreate,
    NavigationLinkRead,
    NavigationLinkUpdate,
    PageHeroCreate,
    PageHeroRead,
    PageHeroUpdate,
    PageMetadataCreate,
    PageMetadataRead,
    PageMetadataUpdate,
    RedirectCreate,
    RedirectRead,
    RedirectUpdate,
    SiteCtaCreate,
    SiteCtaRead,
    SiteCtaUpdate,
)
from schemas.pagination import PaginatedResponse
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate
from utils.singleton import get_singleton_for_admin, upsert_singleton

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
    query = db.query(NavigationLink).order_by(
        NavigationLink.menu_group, NavigationLink.sort_order, NavigationLink.label
    )
    return paginate(query, limit, offset, transform=NavigationLinkRead.model_validate)


@navigation_router.get("/{link_id}", response_model=NavigationLinkRead)
def get_navigation_link(link_id: UUID, db: Session = Depends(get_db)):
    item = db.get(NavigationLink, link_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Navigation link not found.")
    return item


@navigation_router.post("", response_model=NavigationLinkRead, status_code=status.HTTP_201_CREATED)
def create_navigation_link(payload: NavigationLinkCreate, db: Session = Depends(get_db)):
    item = NavigationLink(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@navigation_router.patch("/{link_id}", response_model=NavigationLinkRead)
def update_navigation_link(
    link_id: UUID,
    payload: NavigationLinkUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(NavigationLink, link_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Navigation link not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(item)
    return item


@navigation_router.delete("/{link_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_navigation_link(link_id: UUID, db: Session = Depends(get_db)):
    item = db.get(NavigationLink, link_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Navigation link not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@site_ctas_router.get("", response_model=PaginatedResponse[SiteCtaRead])
def list_site_ctas(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(SiteCta).order_by(SiteCta.sort_order.nulls_last(), SiteCta.key)
    return paginate(query, limit, offset, transform=SiteCtaRead.model_validate)


@site_ctas_router.get("/{cta_id}", response_model=SiteCtaRead)
def get_site_cta(cta_id: UUID, db: Session = Depends(get_db)):
    item = db.get(SiteCta, cta_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site CTA not found.")
    return item


@site_ctas_router.post("", response_model=SiteCtaRead, status_code=status.HTTP_201_CREATED)
def create_site_cta(payload: SiteCtaCreate, db: Session = Depends(get_db)):
    item = SiteCta(**payload.model_dump())
    db.add(item)
    commit_or_raise(db, slug_field="key")
    db.refresh(item)
    return item


@site_ctas_router.patch("/{cta_id}", response_model=SiteCtaRead)
def update_site_cta(cta_id: UUID, payload: SiteCtaUpdate, db: Session = Depends(get_db)):
    item = db.get(SiteCta, cta_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site CTA not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db, slug_field="key")
    db.refresh(item)
    return item


@site_ctas_router.delete("/{cta_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_site_cta(cta_id: UUID, db: Session = Depends(get_db)):
    item = db.get(SiteCta, cta_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site CTA not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@page_metadata_router.get("", response_model=PaginatedResponse[PageMetadataRead])
def list_page_metadata(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(PageMetadata).order_by(PageMetadata.page_key)
    return paginate(query, limit, offset, transform=PageMetadataRead.model_validate)


@page_metadata_router.get("/{metadata_id}", response_model=PageMetadataRead)
def get_page_metadata(metadata_id: UUID, db: Session = Depends(get_db)):
    item = db.get(PageMetadata, metadata_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page metadata not found.")
    return item


@page_metadata_router.post("", response_model=PageMetadataRead, status_code=status.HTTP_201_CREATED)
def create_page_metadata(payload: PageMetadataCreate, db: Session = Depends(get_db)):
    item = PageMetadata(**payload.model_dump())
    db.add(item)
    commit_or_raise(db, slug_field="page_key")
    db.refresh(item)
    return item


@page_metadata_router.patch("/{metadata_id}", response_model=PageMetadataRead)
def update_page_metadata(
    metadata_id: UUID,
    payload: PageMetadataUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(PageMetadata, metadata_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page metadata not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db, slug_field="page_key")
    db.refresh(item)
    return item


@page_metadata_router.delete("/{metadata_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_page_metadata(metadata_id: UUID, db: Session = Depends(get_db)):
    item = db.get(PageMetadata, metadata_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page metadata not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


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


@page_heroes_router.post("", response_model=PageHeroRead, status_code=status.HTTP_201_CREATED)
def create_page_hero(payload: PageHeroCreate, db: Session = Depends(get_db)):
    item = PageHero(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@page_heroes_router.patch("/{hero_id}", response_model=PageHeroRead)
def update_page_hero(hero_id: UUID, payload: PageHeroUpdate, db: Session = Depends(get_db)):
    item = db.get(PageHero, hero_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page hero not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(item)
    return item


@page_heroes_router.delete("/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_page_hero(hero_id: UUID, db: Session = Depends(get_db)):
    item = db.get(PageHero, hero_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page hero not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@redirects_router.get("", response_model=PaginatedResponse[RedirectRead])
def list_redirects(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Redirect).order_by(Redirect.old_path)
    return paginate(query, limit, offset, transform=RedirectRead.model_validate)


@redirects_router.get("/{redirect_id}", response_model=RedirectRead)
def get_redirect(redirect_id: UUID, db: Session = Depends(get_db)):
    item = db.get(Redirect, redirect_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Redirect not found.")
    return item


@redirects_router.post("", response_model=RedirectRead, status_code=status.HTTP_201_CREATED)
def create_redirect(payload: RedirectCreate, db: Session = Depends(get_db)):
    item = Redirect(**payload.model_dump())
    db.add(item)
    commit_or_raise(db, slug_field="old_path")
    db.refresh(item)
    return item


@redirects_router.patch("/{redirect_id}", response_model=RedirectRead)
def update_redirect(redirect_id: UUID, payload: RedirectUpdate, db: Session = Depends(get_db)):
    item = db.get(Redirect, redirect_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Redirect not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db, slug_field="old_path")
    db.refresh(item)
    return item


@redirects_router.delete("/{redirect_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_redirect(redirect_id: UUID, db: Session = Depends(get_db)):
    item = db.get(Redirect, redirect_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Redirect not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@company_stats_router.get("", response_model=CompanyStatsRead | None)
def get_company_stats(db: Session = Depends(get_db)):
    return get_singleton_for_admin(db, CompanyStats)


@company_stats_router.patch("", response_model=CompanyStatsRead)
def update_company_stats(payload: CompanyStatsUpdate, db: Session = Depends(get_db)):
    return upsert_singleton(
        db,
        CompanyStats,
        payload.model_dump(exclude_unset=True),
        CompanyStatsBase,
    )


@global_page_cta_router.get("", response_model=GlobalPageCtaRead | None)
def get_global_page_cta(db: Session = Depends(get_db)):
    return get_singleton_for_admin(db, GlobalPageCta)


@global_page_cta_router.patch("", response_model=GlobalPageCtaRead)
def update_global_page_cta(payload: GlobalPageCtaUpdate, db: Session = Depends(get_db)):
    return upsert_singleton(
        db,
        GlobalPageCta,
        payload.model_dump(exclude_unset=True),
        GlobalPageCtaBase,
    )
