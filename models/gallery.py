import uuid
from typing import Optional

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class ClientStory(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "client_stories"
    __table_args__ = (
        Index("ix_client_stories_slug", "slug", unique=True),
        Index("ix_client_stories_show_on_home", "show_on_home"),
        Index("ix_client_stories_show_in_gallery", "show_in_gallery"),
        Index("ix_client_stories_is_published", "is_published"),
        Index("ix_client_stories_destination_id", "destination_id"),
    )

    slug: Mapped[Optional[str]] = mapped_column(String(128), unique=True, nullable=True)
    client_name: Mapped[str] = mapped_column(String(255), nullable=False)
    destination_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("destinations.id", ondelete="SET NULL"), nullable=True
    )
    destination_label: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    trip_type: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    quote: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    caption: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    portrait_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    show_on_home: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    show_in_gallery: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_featured_in_gallery: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    home_sort_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    gallery_sort_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<ClientStory client_name={self.client_name!r}>"


class GalleryCategory(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "gallery_categories"
    __table_args__ = (Index("ix_gallery_categories_slug", "slug", unique=True),)

    slug: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    label: Mapped[str] = mapped_column(String(128), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    item_links: Mapped[list["GalleryItemCategory"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<GalleryCategory slug={self.slug!r}>"


class GalleryItem(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "gallery_items"
    __table_args__ = (
        Index("ix_gallery_items_slug", "slug", unique=True),
        Index("ix_gallery_items_is_published", "is_published"),
    )

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    place: Mapped[str] = mapped_column(String(255), nullable=False)
    region_label: Mapped[str] = mapped_column(String(255), nullable=False)
    media_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="RESTRICT"), nullable=False
    )
    layout: Mapped[str] = mapped_column(String(16), nullable=False)
    label_style: Mapped[str] = mapped_column(String(16), nullable=False)
    sort_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    category_links: Mapped[list["GalleryItemCategory"]] = relationship(
        back_populates="gallery_item",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<GalleryItem slug={self.slug!r} place={self.place!r}>"


class GalleryItemCategory(Base, TimestampMixin):
    __tablename__ = "gallery_item_categories"
    __table_args__ = (
        Index("ix_gallery_item_categories_gallery_item_id", "gallery_item_id"),
        Index("ix_gallery_item_categories_category_id", "gallery_category_id"),
    )

    gallery_item_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("gallery_items.id", ondelete="CASCADE"), primary_key=True
    )
    gallery_category_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("gallery_categories.id", ondelete="CASCADE"), primary_key=True
    )

    gallery_item: Mapped["GalleryItem"] = relationship(back_populates="category_links")
    category: Mapped["GalleryCategory"] = relationship(back_populates="item_links")

    def __repr__(self) -> str:
        return f"<GalleryItemCategory item={self.gallery_item_id} category={self.gallery_category_id}>"
