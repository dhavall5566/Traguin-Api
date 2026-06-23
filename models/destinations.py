import uuid
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class DestinationCategory(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "destination_categories"
    __table_args__ = (Index("ix_destination_categories_slug", "slug", unique=True),)

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    assignments: Mapped[list["DestinationCategoryAssignment"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<DestinationCategory slug={self.slug!r}>"


class Destination(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "destinations"
    __table_args__ = (
        Index("ix_destinations_slug", "slug", unique=True),
        Index("ix_destinations_is_featured", "is_featured"),
        Index("ix_destinations_is_published", "is_published"),
        Index("ix_destinations_region", "region"),
    )

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    country: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    region: Mapped[str] = mapped_column(String(32), nullable=False)
    india_region: Mapped[Optional[str]] = mapped_column(String(16), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    starting_price: Mapped[int] = mapped_column(Integer, nullable=False)
    hero_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    lat: Mapped[Optional[Decimal]] = mapped_column(Numeric(9, 6), nullable=True)
    lng: Mapped[Optional[Decimal]] = mapped_column(Numeric(9, 6), nullable=True)
    moods: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False, default=list)
    package_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    hotel_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_featured: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    featured_sort_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    meta_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    meta_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    category_assignments: Mapped[list["DestinationCategoryAssignment"]] = relationship(
        back_populates="destination",
        cascade="all, delete-orphan",
    )
    gallery_media: Mapped[list["DestinationMedia"]] = relationship(
        back_populates="destination",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Destination slug={self.slug!r}>"


class DestinationCategoryAssignment(Base, TimestampMixin):
    __tablename__ = "destination_category_assignments"
    __table_args__ = (
        Index("ix_destination_category_assignments_destination", "destination_id"),
        Index("ix_destination_category_assignments_category", "category_id"),
    )

    destination_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("destinations.id", ondelete="CASCADE"),
        primary_key=True,
    )
    category_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("destination_categories.id", ondelete="CASCADE"),
        primary_key=True,
    )
    sort_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    destination: Mapped["Destination"] = relationship(back_populates="category_assignments")
    category: Mapped["DestinationCategory"] = relationship(back_populates="assignments")

    def __repr__(self) -> str:
        return f"<DestinationCategoryAssignment dest={self.destination_id} cat={self.category_id}>"


class DestinationMedia(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "destination_media"
    __table_args__ = (
        Index("ix_destination_media_destination_id", "destination_id"),
        Index("ix_destination_media_sort", "destination_id", "sort_order"),
    )

    destination_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("destinations.id", ondelete="CASCADE"), nullable=False
    )
    media_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="CASCADE"), nullable=False
    )
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    destination: Mapped["Destination"] = relationship(back_populates="gallery_media")
    media: Mapped["MediaAsset"] = relationship()

    def __repr__(self) -> str:
        return f"<DestinationMedia destination={self.destination_id} sort={self.sort_order}>"
