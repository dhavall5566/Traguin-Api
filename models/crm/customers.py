from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any, Optional

from sqlalchemy import Boolean, ForeignKey, Index, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, TimestampMixin, UUIDPrimaryKeyMixin


class Customer(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "customers"
    __table_args__ = (
        Index("ix_customers_agency_id", "agency_id"),
        Index(
            "uq_customers_agency_id_email",
            "agency_id",
            "email",
            unique=True,
            postgresql_where=text("is_deleted = false"),
        ),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    first_name: Mapped[str] = mapped_column(String(128), nullable=False)
    last_name: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    passport_number: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    passport_expiry: Mapped[Optional[datetime]] = mapped_column(nullable=True)
    travel_history: Mapped[Optional[Any]] = mapped_column(JSONB, nullable=True)
    documents: Mapped[Optional[Any]] = mapped_column(JSONB, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    agency: Mapped[Agency] = relationship(back_populates="customers")
    leads: Mapped[list[Lead]] = relationship(back_populates="customer")
    itineraries: Mapped[list[Itinerary]] = relationship(back_populates="customer")
    bookings: Mapped[list[Booking]] = relationship(back_populates="customer")
