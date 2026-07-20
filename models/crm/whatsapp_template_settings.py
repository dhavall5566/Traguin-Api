from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy import ForeignKey, Index, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from models.crm.tenancy import Agency


class AgencyWhatsAppTemplateSettings(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    """Per-agency WhatsApp template IDs/names for CRM notifications."""

    __tablename__ = "agency_whatsapp_template_settings"
    __table_args__ = (
        Index("ix_agency_whatsapp_template_settings_agency_id", "agency_id", unique=True),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    default_template_id: Mapped[str] = mapped_column(String(128), nullable=False, default="")
    default_template_name: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    template_language: Mapped[str] = mapped_column(String(16), nullable=False, default="en")
    template_overrides: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, default=dict)

    agency: Mapped["Agency"] = relationship(back_populates="whatsapp_template_settings")
