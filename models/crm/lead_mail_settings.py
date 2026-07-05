from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Index, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, CreatedAtMixin, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from models.crm.tenancy import Agency, User


class AgencyLeadMailSettings(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    """Per-agency toggle for outbound email when new CRM leads are created."""

    __tablename__ = "agency_lead_mail_settings"
    __table_args__ = (Index("ix_agency_lead_mail_settings_agency_id", "agency_id", unique=True),)

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    agency: Mapped["Agency"] = relationship(back_populates="lead_mail_settings")
    recipients: Mapped[list["AgencyLeadMailRecipient"]] = relationship(
        back_populates="settings",
        cascade="all, delete-orphan",
        order_by="AgencyLeadMailRecipient.created_at",
    )


class AgencyLeadMailRecipient(CrmBase, UUIDPrimaryKeyMixin, CreatedAtMixin):
    """Staff user selected to receive new-lead email alerts."""

    __tablename__ = "agency_lead_mail_recipients"
    __table_args__ = (
        UniqueConstraint("settings_id", "user_id", name="uq_lead_mail_recipient_settings_user"),
        Index("ix_agency_lead_mail_recipients_settings_id", "settings_id"),
    )

    settings_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("agency_lead_mail_settings.id", ondelete="CASCADE"),
        nullable=False,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    settings: Mapped["AgencyLeadMailSettings"] = relationship(back_populates="recipients")
    user: Mapped["User"] = relationship()
