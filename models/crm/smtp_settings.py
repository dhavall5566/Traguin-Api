from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Index, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from models.crm.tenancy import Agency


class AgencySmtpSettings(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    """Per-agency outbound email (SMTP) configuration for CRM notifications."""

    __tablename__ = "agency_smtp_settings"
    __table_args__ = (Index("ix_agency_smtp_settings_agency_id", "agency_id", unique=True),)

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    host: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    port: Mapped[int] = mapped_column(Integer, nullable=False, default=587)
    use_tls: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    use_ssl: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    password: Mapped[str | None] = mapped_column(String(512), nullable=True)
    from_email: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    from_name: Mapped[str] = mapped_column(String(255), nullable=False, default="")

    agency: Mapped["Agency"] = relationship(back_populates="smtp_settings")
