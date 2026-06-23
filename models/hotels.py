import uuid
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    SmallInteger,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class Hotel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "hotels"
    __table_args__ = (
        Index("ix_hotels_slug", "slug", unique=True),
        Index("ix_hotels_destination_id", "destination_id"),
        Index("ix_hotels_is_published", "is_published"),
    )

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    destination_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("destinations.id", ondelete="RESTRICT"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    stars: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[Optional[Decimal]] = mapped_column(Numeric(2, 1), nullable=True)
    review_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    hero_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    amenities: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False, default=list)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    nearby_attractions: Mapped[list["HotelNearbyAttraction"]] = relationship(
        back_populates="hotel", cascade="all, delete-orphan", order_by="HotelNearbyAttraction.sort_order"
    )
    gallery_media: Mapped[list["HotelMedia"]] = relationship(
        back_populates="hotel", cascade="all, delete-orphan", order_by="HotelMedia.sort_order"
    )

    def __repr__(self) -> str:
        return f"<Hotel slug={self.slug!r}>"


class HotelNearbyAttraction(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "hotel_nearby_attractions"
    __table_args__ = (Index("ix_hotel_nearby_attractions_hotel_id", "hotel_id"),)

    hotel_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("hotels.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    distance_label: Mapped[str] = mapped_column(String(64), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    hotel: Mapped["Hotel"] = relationship(back_populates="nearby_attractions")

    def __repr__(self) -> str:
        return f"<HotelNearbyAttraction hotel={self.hotel_id} name={self.name!r}>"


class HotelMedia(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "hotel_media"
    __table_args__ = (
        Index("ix_hotel_media_hotel_id", "hotel_id"),
        Index("ix_hotel_media_sort", "hotel_id", "sort_order"),
    )

    hotel_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("hotels.id", ondelete="CASCADE"), nullable=False
    )
    media_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="CASCADE"), nullable=False
    )
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    hotel: Mapped["Hotel"] = relationship(back_populates="gallery_media")
    media: Mapped["MediaAsset"] = relationship()

    def __repr__(self) -> str:
        return f"<HotelMedia hotel={self.hotel_id} sort={self.sort_order}>"
