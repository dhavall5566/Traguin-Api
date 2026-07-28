from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from models.crm.base import CrmBase

class AgencySlaSettings(CrmBase):
    __tablename__ = "agency_sla_settings"

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), primary_key=True
    )
    lead_response_minutes: Mapped[int] = mapped_column(Integer, nullable=False, default=15)
    followup_reminder_minutes: Mapped[int] = mapped_column(Integer, nullable=False, default=30)
    proposal_sla_hours: Mapped[int] = mapped_column(Integer, nullable=False, default=48)
    escalation_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
