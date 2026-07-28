from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

class AgencySlaSettingsRead(BaseModel):
    agency_id: UUID
    lead_response_minutes: int = 15
    followup_reminder_minutes: int = 30
    proposal_sla_hours: int = 48
    escalation_enabled: bool = True
    updated_at: datetime | None = None

class AgencySlaSettingsUpdate(BaseModel):
    lead_response_minutes: int | None = Field(default=None, ge=1, le=10080)
    followup_reminder_minutes: int | None = Field(default=None, ge=1, le=10080)
    proposal_sla_hours: int | None = Field(default=None, ge=1, le=720)
    escalation_enabled: bool | None = None
