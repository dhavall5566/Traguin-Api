from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.crm.common import CrmCreatedAtRead, CrmTimestampRead


class LeadNoteCreateNested(BaseModel):
    content: str = Field(..., min_length=1)


class LeadActivityCreateNested(BaseModel):
    type: str = Field(..., min_length=1, max_length=32)
    description: str = Field(..., min_length=1)


class LeadFollowupCreateNested(BaseModel):
    scheduled_at: datetime
    status: str = Field(default="PENDING", max_length=32)
    notes: str | None = None


class LeadNoteRead(CrmCreatedAtRead):
    lead_id: UUID
    content: str
    created_by_id: UUID


class LeadActivityRead(CrmCreatedAtRead):
    lead_id: UUID
    type: str
    description: str
    created_by_id: UUID


class LeadFollowupRead(CrmCreatedAtRead):
    lead_id: UUID
    scheduled_at: datetime
    status: str
    notes: str | None
    created_by_id: UUID


class LeadBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    first_name: str = Field(..., min_length=1, max_length=128)
    last_name: str = Field(..., min_length=1, max_length=128)
    email: str | None = Field(default=None, max_length=255)
    phone: str | None = Field(default=None, max_length=64)
    status: str = Field(default="NEW", max_length=32)
    value: Decimal = Field(default=Decimal("0.00"), ge=0)
    source: str | None = Field(default=None, max_length=128)
    assigned_to_id: UUID | None = None
    customer_id: UUID | None = None


class LeadCreate(LeadBase):
    notes: list[LeadNoteCreateNested] = Field(default_factory=list)
    activities: list[LeadActivityCreateNested] = Field(default_factory=list)
    followups: list[LeadFollowupCreateNested] = Field(default_factory=list)


class LeadUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    first_name: str | None = Field(default=None, min_length=1, max_length=128)
    last_name: str | None = Field(default=None, min_length=1, max_length=128)
    email: str | None = Field(default=None, max_length=255)
    phone: str | None = Field(default=None, max_length=64)
    status: str | None = Field(default=None, max_length=32)
    value: Decimal | None = Field(default=None, ge=0)
    source: str | None = Field(default=None, max_length=128)
    assigned_to_id: UUID | None = None
    customer_id: UUID | None = None
    append_notes: list[LeadNoteCreateNested] | None = None
    append_activities: list[LeadActivityCreateNested] | None = None
    append_followups: list[LeadFollowupCreateNested] | None = None


class LeadRead(CrmTimestampRead, LeadBase):
    agency_id: UUID
    proposal_sent_at: datetime | None = None
    is_deleted: bool
    notes: list[LeadNoteRead] = Field(default_factory=list)
    activities: list[LeadActivityRead] = Field(default_factory=list)
    followups: list[LeadFollowupRead] = Field(default_factory=list)


class LeadListRead(CrmTimestampRead, LeadBase):
    """Lightweight row for CRM tables — omits notes, activities, and followups."""

    agency_id: UUID
    proposal_sent_at: datetime | None = None
    is_deleted: bool
