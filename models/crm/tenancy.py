from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Boolean, ForeignKey, Index, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, CreatedAtMixin, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from models.crm.lead_mail_settings import AgencyLeadMailSettings
    from models.crm.smtp_settings import AgencySmtpSettings


class Agency(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "agencies"
    __table_args__ = (Index("ix_agencies_subdomain", "subdomain", unique=True),)

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    subdomain: Mapped[str] = mapped_column(String(255), nullable=False)
    logo_url: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    primary_color: Mapped[str] = mapped_column(String(32), nullable=False, default="#3b82f6")
    secondary_color: Mapped[str] = mapped_column(String(32), nullable=False, default="#1e293b")
    subscription_plan: Mapped[str] = mapped_column(String(64), nullable=False, default="FREE")
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    users: Mapped[list[User]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    roles: Mapped[list[Role]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    leads: Mapped[list[Lead]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    customers: Mapped[list[Customer]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    itineraries: Mapped[list[Itinerary]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    vendors: Mapped[list[Vendor]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    bookings: Mapped[list[Booking]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    quotations: Mapped[list[Quotation]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    invoices: Mapped[list[Invoice]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    payments: Mapped[list[Payment]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    expenses: Mapped[list[Expense]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    vendor_payouts: Mapped[list[VendorPayout]] = relationship(
        back_populates="agency", cascade="all, delete-orphan"
    )
    audit_logs: Mapped[list[AuditLog]] = relationship(back_populates="agency", cascade="all, delete-orphan")
    smtp_settings: Mapped[Optional["AgencySmtpSettings"]] = relationship(
        back_populates="agency", cascade="all, delete-orphan", uselist=False
    )
    lead_mail_settings: Mapped[Optional["AgencyLeadMailSettings"]] = relationship(
        back_populates="agency", cascade="all, delete-orphan", uselist=False
    )


class User(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "users"
    __table_args__ = (
        Index("ix_users_email", "email", unique=True),
        Index("ix_users_agency_id", "agency_id"),
    )

    email: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    agency_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=True
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    agency: Mapped[Optional[Agency]] = relationship(back_populates="users")
    assigned_leads: Mapped[list[Lead]] = relationship(
        back_populates="assigned_to", foreign_keys="Lead.assigned_to_id"
    )
    created_notes: Mapped[list[LeadNote]] = relationship(back_populates="created_by")
    created_activities: Mapped[list[LeadActivity]] = relationship(back_populates="created_by")
    created_followups: Mapped[list[LeadFollowup]] = relationship(back_populates="created_by")
    user_roles: Mapped[list[UserRole]] = relationship(back_populates="user", cascade="all, delete-orphan")
    audit_logs: Mapped[list[AuditLog]] = relationship(back_populates="user")


class Role(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "roles"
    __table_args__ = (
        UniqueConstraint("name", "agency_id", name="uq_roles_name_agency_id"),
        Index("ix_roles_agency_id", "agency_id"),
    )

    name: Mapped[str] = mapped_column(String(128), nullable=False)
    agency_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=True
    )

    agency: Mapped[Optional[Agency]] = relationship(back_populates="roles")
    role_permissions: Mapped[list[RolePermission]] = relationship(
        back_populates="role", cascade="all, delete-orphan"
    )
    user_roles: Mapped[list[UserRole]] = relationship(back_populates="role", cascade="all, delete-orphan")


class Permission(CrmBase, UUIDPrimaryKeyMixin, CreatedAtMixin):
    __tablename__ = "permissions"
    __table_args__ = (UniqueConstraint("name", "module", name="uq_permissions_name_module"),)

    name: Mapped[str] = mapped_column(String(64), nullable=False)
    module: Mapped[str] = mapped_column(String(64), nullable=False)

    role_permissions: Mapped[list[RolePermission]] = relationship(
        back_populates="permission", cascade="all, delete-orphan"
    )


class RolePermission(CrmBase):
    __tablename__ = "role_permissions"

    role_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True
    )
    permission_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True
    )

    role: Mapped[Role] = relationship(back_populates="role_permissions")
    permission: Mapped[Permission] = relationship(back_populates="role_permissions")


class UserRole(CrmBase):
    __tablename__ = "user_roles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    role_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True
    )

    user: Mapped[User] = relationship(back_populates="user_roles")
    role: Mapped[Role] = relationship(back_populates="user_roles")
