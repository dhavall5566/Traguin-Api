from __future__ import annotations

import uuid
from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import ForeignKey, Index, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, TimestampMixin, UUIDPrimaryKeyMixin


class Vendor(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "vendors"
    __table_args__ = (Index("ix_vendors_agency_id", "agency_id"),)

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[str] = mapped_column(String(32), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ledger_balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))

    agency: Mapped[Agency] = relationship(back_populates="vendors")
    services: Mapped[list[VendorService]] = relationship(back_populates="vendor", cascade="all, delete-orphan")
    packages: Mapped[list[VendorPackage]] = relationship(back_populates="vendor", cascade="all, delete-orphan")
    vendor_payouts: Mapped[list[VendorPayout]] = relationship(back_populates="vendor")


class VendorService(CrmBase, UUIDPrimaryKeyMixin):
    __tablename__ = "vendor_services"
    __table_args__ = (Index("ix_vendor_services_vendor_id", "vendor_id"),)

    vendor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("vendors.id", ondelete="CASCADE"), nullable=False
    )
    type: Mapped[str] = mapped_column(String(32), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    base_rate: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))

    vendor: Mapped[Vendor] = relationship(back_populates="services")
    rates: Mapped[list[VendorRate]] = relationship(back_populates="vendor_service", cascade="all, delete-orphan")


class VendorPackage(CrmBase, UUIDPrimaryKeyMixin):
    __tablename__ = "vendor_packages"
    __table_args__ = (Index("ix_vendor_packages_vendor_id", "vendor_id"),)

    vendor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("vendors.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))

    vendor: Mapped[Vendor] = relationship(back_populates="packages")
    rates: Mapped[list[VendorRate]] = relationship(back_populates="vendor_package", cascade="all, delete-orphan")


class VendorRate(CrmBase, UUIDPrimaryKeyMixin):
    __tablename__ = "vendor_rates"
    __table_args__ = (
        Index("ix_vendor_rates_vendor_service_id", "vendor_service_id"),
        Index("ix_vendor_rates_vendor_package_id", "vendor_package_id"),
    )

    vendor_service_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("vendor_services.id", ondelete="CASCADE"), nullable=True
    )
    vendor_package_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("vendor_packages.id", ondelete="CASCADE"), nullable=True
    )
    rate: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    season_start: Mapped[datetime] = mapped_column(nullable=False)
    season_end: Mapped[datetime] = mapped_column(nullable=False)

    vendor_service: Mapped[Optional[VendorService]] = relationship(back_populates="rates")
    vendor_package: Mapped[Optional[VendorPackage]] = relationship(back_populates="rates")
