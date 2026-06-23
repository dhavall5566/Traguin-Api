from __future__ import annotations

import uuid
from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import ForeignKey, Index, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, CreatedAtMixin, UUIDPrimaryKeyMixin


class Quotation(CrmBase, UUIDPrimaryKeyMixin, CreatedAtMixin):
    __tablename__ = "quotations"
    __table_args__ = (Index("ix_quotations_agency_id", "agency_id"),)

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    itinerary_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="DRAFT")

    agency: Mapped[Agency] = relationship(back_populates="quotations")
    itinerary: Mapped[Itinerary] = relationship(back_populates="quotations")


class Invoice(CrmBase, UUIDPrimaryKeyMixin, CreatedAtMixin):
    __tablename__ = "invoices"
    __table_args__ = (
        Index("ix_invoices_invoice_number", "invoice_number", unique=True),
        Index("ix_invoices_agency_id", "agency_id"),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    booking_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("bookings.id", ondelete="CASCADE"), nullable=False
    )
    invoice_number: Mapped[str] = mapped_column(String(64), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    due_date: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="UNPAID")

    agency: Mapped[Agency] = relationship(back_populates="invoices")
    booking: Mapped[Booking] = relationship(back_populates="invoices")
    payments: Mapped[list[Payment]] = relationship(back_populates="invoice", cascade="all, delete-orphan")


class Payment(CrmBase, UUIDPrimaryKeyMixin):
    __tablename__ = "payments"
    __table_args__ = (
        Index("ix_payments_agency_id", "agency_id"),
        Index("ix_payments_invoice_id", "invoice_id"),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    invoice_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    payment_method: Mapped[str] = mapped_column(String(32), nullable=False)
    transaction_reference: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    payment_date: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())

    agency: Mapped[Agency] = relationship(back_populates="payments")
    invoice: Mapped[Invoice] = relationship(back_populates="payments")


class Expense(CrmBase, UUIDPrimaryKeyMixin):
    __tablename__ = "expenses"
    __table_args__ = (Index("ix_expenses_agency_id", "agency_id"),)

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    booking_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("bookings.id", ondelete="SET NULL"), nullable=True
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    category: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    expense_date: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())

    agency: Mapped[Agency] = relationship(back_populates="expenses")
    booking: Mapped[Optional[Booking]] = relationship(back_populates="expenses")


class VendorPayout(CrmBase, UUIDPrimaryKeyMixin):
    __tablename__ = "vendor_payouts"
    __table_args__ = (
        Index("ix_vendor_payouts_agency_id", "agency_id"),
        Index("ix_vendor_payouts_vendor_id", "vendor_id"),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    vendor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("vendors.id", ondelete="CASCADE"), nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    payment_date: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="PAID")

    agency: Mapped[Agency] = relationship(back_populates="vendor_payouts")
    vendor: Mapped[Vendor] = relationship(back_populates="vendor_payouts")
