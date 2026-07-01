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
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class Package(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "packages"
    __table_args__ = (
        Index("ix_packages_slug", "slug", unique=True),
        Index("ix_packages_destination_id", "destination_id"),
        Index("ix_packages_is_featured", "is_featured"),
        Index("ix_packages_is_published", "is_published"),
    )

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    destination_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("destinations.id", ondelete="RESTRICT"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    duration_label: Mapped[str] = mapped_column(String(64), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    sold_last_month: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    hero_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    rating: Mapped[Optional[Decimal]] = mapped_column(Numeric(2, 1), nullable=True)
    is_featured: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    featured_sort_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    highlights: Mapped[list["PackageHighlight"]] = relationship(
        back_populates="package",
        cascade="all, delete-orphan",
        order_by="PackageHighlight.sort_order",
    )
    moods: Mapped[list["PackageMood"]] = relationship(
        back_populates="package",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Package slug={self.slug!r}>"


class PackageHighlight(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "package_highlights"
    __table_args__ = (Index("ix_package_highlights_package_id", "package_id"),)

    package_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("packages.id", ondelete="CASCADE"), nullable=False
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    package: Mapped["Package"] = relationship(back_populates="highlights")

    def __repr__(self) -> str:
        return f"<PackageHighlight package={self.package_id} sort={self.sort_order}>"


class PackageMood(Base, TimestampMixin):
    __tablename__ = "package_moods"
    __table_args__ = (Index("ix_package_moods_package_id", "package_id"),)

    package_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("packages.id", ondelete="CASCADE"), primary_key=True
    )
    mood: Mapped[str] = mapped_column(String(32), primary_key=True)

    package: Mapped["Package"] = relationship(back_populates="moods")

    def __repr__(self) -> str:
        return f"<PackageMood package={self.package_id} mood={self.mood!r}>"
