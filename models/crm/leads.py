from __future__ import annotations

import uuid
from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, Index, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, CreatedAtMixin, TimestampMixin, UUIDPrimaryKeyMixin


class Lead(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "leads"
    __table_args__ = (
        Index("ix_leads_agency_id", "agency_id"),
        Index("ix_leads_assigned_to_id", "assigned_to_id"),
        Index("ix_leads_customer_id", "customer_id"),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(128), nullable=False)
    last_name: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="NEW")
    value: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    source: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    assigned_to_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    customer_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customers.id", ondelete="SET NULL"), nullable=True
    )
    proposal_sent_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    agency: Mapped[Agency] = relationship(back_populates="leads")
    customer: Mapped[Optional[Customer]] = relationship(back_populates="leads")
    assigned_to: Mapped[Optional[User]] = relationship(
        back_populates="assigned_leads", foreign_keys=[assigned_to_id]
    )
    notes: Mapped[list[LeadNote]] = relationship(back_populates="lead", cascade="all, delete-orphan")
    activities: Mapped[list[LeadActivity]] = relationship(
        back_populates="lead", cascade="all, delete-orphan"
    )
    followups: Mapped[list[LeadFollowup]] = relationship(
        back_populates="lead", cascade="all, delete-orphan"
    )


class LeadNote(CrmBase, UUIDPrimaryKeyMixin, CreatedAtMixin):
    __tablename__ = "lead_notes"
    __table_args__ = (Index("ix_lead_notes_lead_id", "lead_id"),)

    lead_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("leads.id", ondelete="CASCADE"), nullable=False
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_by_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    lead: Mapped[Lead] = relationship(back_populates="notes")
    created_by: Mapped[User] = relationship(back_populates="created_notes")


class LeadActivity(CrmBase, UUIDPrimaryKeyMixin, CreatedAtMixin):
    __tablename__ = "lead_activities"
    __table_args__ = (Index("ix_lead_activities_lead_id", "lead_id"),)

    lead_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("leads.id", ondelete="CASCADE"), nullable=False
    )
    type: Mapped[str] = mapped_column(String(32), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    created_by_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    lead: Mapped[Lead] = relationship(back_populates="activities")
    created_by: Mapped[User] = relationship(back_populates="created_activities")


class LeadFollowup(CrmBase, UUIDPrimaryKeyMixin, CreatedAtMixin):
    __tablename__ = "lead_followups"
    __table_args__ = (Index("ix_lead_followups_lead_id", "lead_id"),)

    lead_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("leads.id", ondelete="CASCADE"), nullable=False
    )
    scheduled_at: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="PENDING")
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_by_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    lead: Mapped[Lead] = relationship(back_populates="followups")
    created_by: Mapped[User] = relationship(back_populates="created_followups")
