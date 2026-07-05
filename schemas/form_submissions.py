from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead


class FormSubmissionCreate(BaseModel):
    form_type: str = Field(..., min_length=1, max_length=64)
    payload: dict
    name: str | None = Field(default=None, max_length=255)
    email: str | None = Field(default=None, max_length=255)
    phone: str | None = Field(default=None, max_length=64)
    related_itinerary_id: UUID | None = None
    related_hotel_id: UUID | None = None
    related_destination_id: UUID | None = None
    related_package_id: UUID | None = None


class FormSubmissionStatusUpdate(BaseModel):
    status: str = Field(..., min_length=1, max_length=32)


class FormSubmissionRead(TimestampRead):
    form_type: str
    payload: dict
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    status: str
    related_itinerary_id: UUID | None = None
    related_hotel_id: UUID | None = None
    related_destination_id: UUID | None = None
    related_package_id: UUID | None = None
    ip_address: str | None = None
    user_agent: str | None = None


class FormSubmissionCreateResponse(FormSubmissionRead):
    lead_id: UUID | None = None
    customer_id: UUID | None = None
    lead_code: str | None = None
    member_code: str | None = None
    inquiry_code: str | None = None
