from __future__ import annotations

import uuid
from typing import Optional

from sqlalchemy import ForeignKey, Index, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, TimestampMixin, UUIDPrimaryKeyMixin


class Booking(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "bookings"
    __table_args__ = (
        Index("ix_bookings_agency_id", "agency_id"),
        Index("ix_bookings_customer_id", "customer_id"),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False
    )
    itinerary_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="SET NULL"), nullable=True
    )
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="PENDING")
    voucher_url: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    ticket_url: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    hotel_confirmation_code: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    driver_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    driver_phone: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    visa_status: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

    agency: Mapped[Agency] = relationship(back_populates="bookings")
    customer: Mapped[Customer] = relationship(back_populates="bookings")
    itinerary: Mapped[Optional[Itinerary]] = relationship(back_populates="bookings")
    invoices: Mapped[list[Invoice]] = relationship(back_populates="booking", cascade="all, delete-orphan")
    expenses: Mapped[list[Expense]] = relationship(back_populates="booking")
