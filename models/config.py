import uuid
from typing import Optional

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    ForeignKey,
    Index,
    Integer,
    SmallInteger,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class SiteSettings(Base, TimestampMixin):
    __tablename__ = "site_settings"
    __table_args__ = (CheckConstraint("id = 1", name="ck_site_settings_singleton"),)

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, default=1)
    phone: Mapped[str] = mapped_column(String(32), nullable=False)
    phone_href: Mapped[str] = mapped_column(String(64), nullable=False)
    whatsapp: Mapped[str] = mapped_column(String(32), nullable=False)
    whatsapp_href: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    email_href: Mapped[str] = mapped_column(String(255), nullable=False)
    inquiry_email: Mapped[str] = mapped_column(String(255), nullable=False)
    instagram_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    address: Mapped[str] = mapped_column(Text, nullable=False)
    hours: Mapped[str] = mapped_column(String(255), nullable=False)
    footer_tagline: Mapped[str] = mapped_column(Text, nullable=False)
    copyright_text: Mapped[str] = mapped_column(Text, nullable=False)
    default_meta_title: Mapped[str] = mapped_column(String(255), nullable=False)
    default_meta_description: Mapped[str] = mapped_column(Text, nullable=False)
    default_meta_keywords: Mapped[Optional[list[str]]] = mapped_column(ARRAY(Text), nullable=True)
    og_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    og_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    favicon_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    icon_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    apple_icon_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    logo_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )

    def __repr__(self) -> str:
        return "<SiteSettings id=1>"


class NavigationLink(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "navigation_links"
    __table_args__ = (
        Index("ix_navigation_links_menu_group_sort", "menu_group", "sort_order"),
    )

    menu_group: Mapped[str] = mapped_column(String(32), nullable=False)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    href: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_visible: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return f"<NavigationLink {self.menu_group}:{self.label!r}>"


class SiteCta(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "site_ctas"
    __table_args__ = (Index("ix_site_ctas_key", "key", unique=True),)

    key: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    href: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    def __repr__(self) -> str:
        return f"<SiteCta key={self.key!r}>"


class CompanyStats(Base, TimestampMixin):
    __tablename__ = "company_stats"
    __table_args__ = (CheckConstraint("id = 1", name="ck_company_stats_singleton"),)

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, default=1)
    homepage_stats: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)
    trust_bar_stats: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)
    gallery_stats: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)

    def __repr__(self) -> str:
        return "<CompanyStats id=1>"


class GlobalPageCta(Base, TimestampMixin):
    __tablename__ = "global_page_cta"
    __table_args__ = (CheckConstraint("id = 1", name="ck_global_page_cta_singleton"),)

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, default=1)
    eyebrow: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    primary_cta_key: Mapped[str] = mapped_column(String(64), nullable=False)
    secondary_cta_key: Mapped[str] = mapped_column(String(64), nullable=False)

    def __repr__(self) -> str:
        return "<GlobalPageCta id=1>"


class PageMetadata(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "page_metadata"
    __table_args__ = (Index("ix_page_metadata_page_key", "page_key", unique=True),)

    page_key: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    og_image_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )

    def __repr__(self) -> str:
        return f"<PageMetadata page_key={self.page_key!r}>"


class PageHero(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "page_heroes"
    __table_args__ = (
        UniqueConstraint("page_key", "region_variant", name="uq_page_heroes_page_region"),
        Index("ix_page_heroes_page_key", "page_key"),
    )

    page_key: Mapped[str] = mapped_column(String(64), nullable=False)
    region_variant: Mapped[str] = mapped_column(String(32), nullable=False, default="all")
    eyebrow: Mapped[str] = mapped_column(String(255), nullable=False)
    badge: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    hero_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    hero_image_alt: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    primary_cta_key: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    primary_cta_label: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    primary_cta_href: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    secondary_cta_key: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    secondary_cta_label: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    secondary_cta_href: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<PageHero page_key={self.page_key!r} region={self.region_variant!r}>"


class Redirect(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "redirects"
    __table_args__ = (
        Index("ix_redirects_old_path", "old_path", unique=True),
        Index("ix_redirects_target_type", "target_type"),
        Index("ix_redirects_target_id", "target_id"),
    )

    old_path: Mapped[str] = mapped_column(String(512), unique=True, nullable=False)
    target_type: Mapped[str] = mapped_column(String(64), nullable=False)
    target_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), nullable=True)
    target_path: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    is_permanent: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return f"<Redirect {self.old_path!r} -> {self.target_type}:{self.target_id or self.target_path}>"
