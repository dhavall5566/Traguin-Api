from uuid import UUID

from pydantic import BaseModel, Field


class LeadMailRecipientRead(BaseModel):
    user_id: UUID
    name: str
    email: str


class AgencyLeadMailSettingsRead(BaseModel):
    enabled: bool = True
    recipient_user_ids: list[UUID] = Field(default_factory=list)
    recipients: list[LeadMailRecipientRead] = Field(default_factory=list)


class AgencyLeadMailSettingsUpdate(BaseModel):
    enabled: bool | None = None
    recipient_user_ids: list[UUID] | None = None
