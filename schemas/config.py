from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import ORMModel, TimestampRead


class NavigationLinkBase(BaseModel):
    menu_group: str = Field(..., min_length=1, max_length=32)
    label: str = Field(..., min_length=1, max_length=255)
    href: str = Field(..., min_length=1)
    sort_order: int = 0
    is_visible: bool = True


class NavigationLinkCreate(NavigationLinkBase):
    pass


class NavigationLinkUpdate(BaseModel):
    menu_group: str | None = Field(default=None, min_length=1, max_length=32)
    label: str | None = Field(default=None, min_length=1, max_length=255)
    href: str | None = Field(default=None, min_length=1)
    sort_order: int | None = None
    is_visible: bool | None = None


class NavigationLinkRead(TimestampRead, NavigationLinkBase):
    pass


class SiteCtaBase(BaseModel):
    key: str = Field(..., min_length=1, max_length=64)
    label: str = Field(..., min_length=1, max_length=255)
    href: str = Field(..., min_length=1)
    sort_order: int | None = None


class SiteCtaCreate(SiteCtaBase):
    pass


class SiteCtaUpdate(BaseModel):
    key: str | None = Field(default=None, min_length=1, max_length=64)
    label: str | None = Field(default=None, min_length=1, max_length=255)
    href: str | None = Field(default=None, min_length=1)
    sort_order: int | None = None


class SiteCtaRead(TimestampRead, SiteCtaBase):
    pass


class CompanyStatsBase(BaseModel):
    homepage_stats: list = Field(default_factory=list)
    trust_bar_stats: list = Field(default_factory=list)
    gallery_stats: list = Field(default_factory=list)


class CompanyStatsUpdate(BaseModel):
    homepage_stats: list | None = None
    trust_bar_stats: list | None = None
    gallery_stats: list | None = None


class CompanyStatsRead(CompanyStatsBase, ORMModel):
    id: int
    created_at: datetime
    updated_at: datetime


class GlobalPageCtaBase(BaseModel):
    eyebrow: str = Field(..., min_length=1, max_length=255)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    primary_cta_key: str = Field(..., min_length=1, max_length=64)
    secondary_cta_key: str = Field(..., min_length=1, max_length=64)


class GlobalPageCtaUpdate(BaseModel):
    eyebrow: str | None = Field(default=None, min_length=1, max_length=255)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    primary_cta_key: str | None = Field(default=None, min_length=1, max_length=64)
    secondary_cta_key: str | None = Field(default=None, min_length=1, max_length=64)


class GlobalPageCtaRead(GlobalPageCtaBase, ORMModel):
    id: int
    created_at: datetime
    updated_at: datetime


class PageMetadataBase(BaseModel):
    page_key: str = Field(..., min_length=1, max_length=64)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    og_image_media_id: UUID | None = None


class PageMetadataCreate(PageMetadataBase):
    pass


class PageMetadataUpdate(BaseModel):
    page_key: str | None = Field(default=None, min_length=1, max_length=64)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    og_image_media_id: UUID | None = None


class PageMetadataRead(TimestampRead, PageMetadataBase):
    pass


class PageHeroBase(BaseModel):
    page_key: str = Field(..., min_length=1, max_length=64)
    region_variant: str = Field(default="all", min_length=1, max_length=32)
    eyebrow: str = Field(..., min_length=1, max_length=255)
    badge: str | None = Field(default=None, max_length=255)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    hero_media_id: UUID | None = None
    hero_image_alt: str | None = None
    primary_cta_key: str | None = Field(default=None, max_length=64)
    primary_cta_label: str | None = Field(default=None, max_length=255)
    primary_cta_href: str | None = None
    secondary_cta_key: str | None = Field(default=None, max_length=64)
    secondary_cta_label: str | None = Field(default=None, max_length=255)
    secondary_cta_href: str | None = None


class PageHeroCreate(PageHeroBase):
    pass


class PageHeroUpdate(BaseModel):
    page_key: str | None = Field(default=None, min_length=1, max_length=64)
    region_variant: str | None = Field(default=None, min_length=1, max_length=32)
    eyebrow: str | None = Field(default=None, min_length=1, max_length=255)
    badge: str | None = Field(default=None, max_length=255)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    hero_media_id: UUID | None = None
    hero_image_alt: str | None = None
    primary_cta_key: str | None = Field(default=None, max_length=64)
    primary_cta_label: str | None = Field(default=None, max_length=255)
    primary_cta_href: str | None = None
    secondary_cta_key: str | None = Field(default=None, max_length=64)
    secondary_cta_label: str | None = Field(default=None, max_length=255)
    secondary_cta_href: str | None = None


class PageHeroRead(TimestampRead, PageHeroBase):
    pass


class RedirectBase(BaseModel):
    old_path: str = Field(..., min_length=1, max_length=512)
    target_type: str = Field(..., min_length=1, max_length=64)
    target_id: UUID | None = None
    target_path: str | None = Field(default=None, max_length=512)
    is_permanent: bool = True


class RedirectCreate(RedirectBase):
    pass


class RedirectUpdate(BaseModel):
    old_path: str | None = Field(default=None, min_length=1, max_length=512)
    target_type: str | None = Field(default=None, min_length=1, max_length=64)
    target_id: UUID | None = None
    target_path: str | None = Field(default=None, max_length=512)
    is_permanent: bool | None = None


class RedirectRead(TimestampRead, RedirectBase):
    pass
