from __future__ import annotations

import uuid
from datetime import datetime
from decimal import Decimal
from typing import Any, Optional

from sqlalchemy import Boolean, ForeignKey, Index, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, TimestampMixin, UUIDPrimaryKeyMixin


class Itinerary(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "itineraries"
    __table_args__ = (
        Index("ix_itineraries_agency_id", "agency_id"),
        Index("ix_itineraries_customer_id", "customer_id"),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    start_date: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    end_date: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    customer_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customers.id", ondelete="SET NULL"), nullable=True
    )
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="DRAFT")
    total_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    markup_margin: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=Decimal("0.00"))
    tax_rate: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, default=Decimal("0.00"))
    is_template: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    agency: Mapped[Agency] = relationship(back_populates="itineraries")
    customer: Mapped[Optional[Customer]] = relationship(back_populates="itineraries")
    days: Mapped[list[ItineraryDay]] = relationship(back_populates="itinerary", cascade="all, delete-orphan")
    bookings: Mapped[list[Booking]] = relationship(back_populates="itinerary")
    quotations: Mapped[list[Quotation]] = relationship(back_populates="itinerary", cascade="all, delete-orphan")


class ItineraryDay(CrmBase, UUIDPrimaryKeyMixin):
    __tablename__ = "itinerary_days"
    __table_args__ = (Index("ix_itinerary_days_itinerary_id", "itinerary_id"),)

    itinerary_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=False
    )
    day_number: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    itinerary: Mapped[Itinerary] = relationship(back_populates="days")
    items: Mapped[list[ItineraryItem]] = relationship(back_populates="itinerary_day", cascade="all, delete-orphan")


class ItineraryItem(CrmBase, UUIDPrimaryKeyMixin):
    __tablename__ = "itinerary_items"
    __table_args__ = (Index("ix_itinerary_items_itinerary_day_id", "itinerary_day_id"),)

    itinerary_day_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itinerary_days.id", ondelete="CASCADE"), nullable=False
    )
    type: Mapped[str] = mapped_column(String(32), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    details: Mapped[Optional[Any]] = mapped_column(JSONB, nullable=True)
    cost_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    selling_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    order: Mapped[int] = mapped_column("order", Integer, nullable=False, default=0)

    itinerary_day: Mapped[ItineraryDay] = relationship(back_populates="items")
