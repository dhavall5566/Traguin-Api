from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field

LeadMailEventType = Literal["website_lead", "crm_lead", "status_change"]


class LeadMailRecipientRead(BaseModel):
    user_id: UUID
    name: str
    email: str


class LeadMailEventRead(BaseModel):
    event_type: LeadMailEventType
    enabled: bool = True
    recipient_user_ids: list[UUID] = Field(default_factory=list)
    recipients: list[LeadMailRecipientRead] = Field(default_factory=list)


class AgencyLeadMailSettingsRead(BaseModel):
    events: list[LeadMailEventRead] = Field(default_factory=list)


class LeadMailEventUpdate(BaseModel):
    event_type: LeadMailEventType
    enabled: bool | None = None
    recipient_user_ids: list[UUID] | None = None


class AgencyLeadMailSettingsUpdate(BaseModel):
    events: list[LeadMailEventUpdate] | None = None
