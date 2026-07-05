from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

from schemas.crm.common import CrmCreatedAtRead, CrmTimestampRead


class LeadDetailsFields(BaseModel):
    travel_date: date | None = None
    address_line1: str | None = Field(default=None, max_length=255)
    address_line2: str | None = Field(default=None, max_length=255)
    city: str | None = Field(default=None, max_length=128)
    pincode: str | None = Field(default=None, max_length=32)
    state: str | None = Field(default=None, max_length=128)
    country: str | None = Field(default=None, max_length=128)
    adults_count: int | None = Field(default=None, ge=0, le=99)
    children_count: int | None = Field(default=None, ge=0, le=20)
    children_ages: list[int] | None = None
    travel_type: str | None = Field(default=None, max_length=32)
    arrival_date: date | None = None
    hotel_category: str | None = Field(default=None, max_length=32)
    meal_category: str | None = Field(default=None, max_length=32)
    travel_destination: str | None = Field(default=None, max_length=255)
    occasion: str | None = Field(default=None, max_length=32)
    flight_type: str | None = Field(default=None, max_length=32)
    extra_baggage: str | None = Field(default=None, max_length=8)
    wheelchair_assistance: str | None = Field(default=None, max_length=8)
    visa_assistance: str | None = Field(default=None, max_length=8)
    travel_insurance: str | None = Field(default=None, max_length=8)
    transportation: str | None = Field(default=None, max_length=16)
    package_mode: str | None = Field(default=None, max_length=16)

    @field_validator("children_ages", mode="before")
    @classmethod
    def normalize_children_ages(cls, value):
        if value is None:
            return None
        if not isinstance(value, list):
            return value
        cleaned: list[int] = []
        for item in value:
            if item is None or item == "":
                continue
            cleaned.append(int(item))
        return cleaned or None


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
    message: str | None = None
    cms_package_id: UUID | None = None


class LeadCreate(LeadBase, LeadDetailsFields):
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
    message: str | None = None
    cms_package_id: UUID | None = None
    travel_date: date | None = None
    address_line1: str | None = Field(default=None, max_length=255)
    address_line2: str | None = Field(default=None, max_length=255)
    city: str | None = Field(default=None, max_length=128)
    pincode: str | None = Field(default=None, max_length=32)
    state: str | None = Field(default=None, max_length=128)
    country: str | None = Field(default=None, max_length=128)
    adults_count: int | None = Field(default=None, ge=0, le=99)
    children_count: int | None = Field(default=None, ge=0, le=20)
    children_ages: list[int] | None = None
    travel_type: str | None = Field(default=None, max_length=32)
    arrival_date: date | None = None
    hotel_category: str | None = Field(default=None, max_length=32)
    meal_category: str | None = Field(default=None, max_length=32)
    travel_destination: str | None = Field(default=None, max_length=255)
    occasion: str | None = Field(default=None, max_length=32)
    flight_type: str | None = Field(default=None, max_length=32)
    extra_baggage: str | None = Field(default=None, max_length=8)
    wheelchair_assistance: str | None = Field(default=None, max_length=8)
    visa_assistance: str | None = Field(default=None, max_length=8)
    travel_insurance: str | None = Field(default=None, max_length=8)
    transportation: str | None = Field(default=None, max_length=16)
    package_mode: str | None = Field(default=None, max_length=16)
    append_notes: list[LeadNoteCreateNested] | None = None
    append_activities: list[LeadActivityCreateNested] | None = None
    append_followups: list[LeadFollowupCreateNested] | None = None

    @field_validator("children_ages", mode="before")
    @classmethod
    def normalize_children_ages_update(cls, value):
        return LeadDetailsFields.normalize_children_ages(value)


class LeadRead(CrmTimestampRead, LeadBase, LeadDetailsFields):
    agency_id: UUID
    lead_code: str | None = None
    proposal_sent_at: datetime | None = None
    cms_form_submission_id: UUID | None = None
    cms_package_id: UUID | None = None
    is_deleted: bool
    notes: list[LeadNoteRead] = Field(default_factory=list)
    activities: list[LeadActivityRead] = Field(default_factory=list)
    followups: list[LeadFollowupRead] = Field(default_factory=list)


class LeadListRead(CrmTimestampRead, LeadBase, LeadDetailsFields):
    """Lightweight row for CRM tables — omits notes, activities, and followups."""

    agency_id: UUID
    lead_code: str | None = None
    proposal_sent_at: datetime | None = None
    cms_form_submission_id: UUID | None = None
    cms_package_id: UUID | None = None
    is_deleted: bool


class LeadRecentEventRead(BaseModel):
    """Lightweight payload for realtime CRM lead notifications."""

    id: UUID
    lead_code: str | None = None
    title: str
    first_name: str
    last_name: str
    source: str | None = None
    created_at: datetime
    updated_at: datetime
    kind: str = Field(description="new | returning")
