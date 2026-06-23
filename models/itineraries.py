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
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class Itinerary(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "itineraries"
    __table_args__ = (
        Index("ix_itineraries_slug", "slug", unique=True),
        Index("ix_itineraries_destination_id", "destination_id"),
        Index("ix_itineraries_package_id", "package_id"),
        Index("ix_itineraries_is_featured", "is_featured"),
        Index("ix_itineraries_is_published", "is_published"),
    )

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    package_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("packages.id", ondelete="SET NULL"), nullable=True
    )
    destination_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("destinations.id", ondelete="RESTRICT"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    duration_label: Mapped[str] = mapped_column(String(64), nullable=False)
    duration_days: Mapped[int] = mapped_column(Integer, nullable=False)
    starting_price: Mapped[int] = mapped_column(Integer, nullable=False)
    price_note: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    rating: Mapped[Optional[Decimal]] = mapped_column(Numeric(2, 1), nullable=True)
    review_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    hero_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    tagline: Mapped[str] = mapped_column(Text, nullable=False)
    overview: Mapped[str] = mapped_column(Text, nullable=False)
    is_featured: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    featured_sort_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    seo_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    seo_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    highlights: Mapped[list["ItineraryHighlight"]] = relationship(
        back_populates="itinerary", cascade="all, delete-orphan", order_by="ItineraryHighlight.sort_order"
    )
    days: Mapped[list["ItineraryDay"]] = relationship(
        back_populates="itinerary", cascade="all, delete-orphan", order_by="ItineraryDay.sort_order"
    )
    hotels: Mapped[list["ItineraryHotel"]] = relationship(
        back_populates="itinerary", cascade="all, delete-orphan", order_by="ItineraryHotel.sort_order"
    )
    inclusions: Mapped[list["ItineraryInclusion"]] = relationship(
        back_populates="itinerary", cascade="all, delete-orphan", order_by="ItineraryInclusion.sort_order"
    )
    gallery_media: Mapped[list["ItineraryMedia"]] = relationship(
        back_populates="itinerary", cascade="all, delete-orphan", order_by="ItineraryMedia.sort_order"
    )

    def __repr__(self) -> str:
        return f"<Itinerary slug={self.slug!r}>"


class ItineraryHighlight(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "itinerary_highlights"
    __table_args__ = (Index("ix_itinerary_highlights_itinerary_id", "itinerary_id"),)

    itinerary_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=False
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    itinerary: Mapped["Itinerary"] = relationship(back_populates="highlights")

    def __repr__(self) -> str:
        return f"<ItineraryHighlight itinerary={self.itinerary_id} sort={self.sort_order}>"


class ItineraryDay(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "itinerary_days"
    __table_args__ = (
        Index("ix_itinerary_days_itinerary_id", "itinerary_id"),
        UniqueConstraint("itinerary_id", "day_number", name="uq_itinerary_days_day_number"),
    )

    itinerary_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=False
    )
    day_number: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    activities: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False, default=list)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    itinerary: Mapped["Itinerary"] = relationship(back_populates="days")

    def __repr__(self) -> str:
        return f"<ItineraryDay itinerary={self.itinerary_id} day={self.day_number}>"


class ItineraryHotel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "itinerary_hotels"
    __table_args__ = (Index("ix_itinerary_hotels_itinerary_id", "itinerary_id"),)

    itinerary_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=False
    )
    hotel_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("hotels.id", ondelete="SET NULL"), nullable=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    nights_label: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    stars: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    category_label: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    room_type: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    meal_plan: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    image_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    itinerary: Mapped["Itinerary"] = relationship(back_populates="hotels")

    def __repr__(self) -> str:
        return f"<ItineraryHotel itinerary={self.itinerary_id} name={self.name!r}>"


class ItineraryInclusion(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "itinerary_inclusions"
    __table_args__ = (Index("ix_itinerary_inclusions_itinerary_id", "itinerary_id"),)

    itinerary_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=False
    )
    kind: Mapped[str] = mapped_column(String(16), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    itinerary: Mapped["Itinerary"] = relationship(back_populates="inclusions")

    def __repr__(self) -> str:
        return f"<ItineraryInclusion itinerary={self.itinerary_id} kind={self.kind!r}>"


class ItineraryMedia(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "itinerary_media"
    __table_args__ = (
        Index("ix_itinerary_media_itinerary_id", "itinerary_id"),
        Index("ix_itinerary_media_sort", "itinerary_id", "sort_order"),
    )

    itinerary_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=False
    )
    media_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="CASCADE"), nullable=False
    )
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    itinerary: Mapped["Itinerary"] = relationship(back_populates="gallery_media")
    media: Mapped["MediaAsset"] = relationship()

    def __repr__(self) -> str:
        return f"<ItineraryMedia itinerary={self.itinerary_id} sort={self.sort_order}>"
