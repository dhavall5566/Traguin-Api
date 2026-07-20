from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field


class InquiryLeadSummaryRead(BaseModel):
    id: UUID
    lead_code: str | None = None
    title: str
    status: str
    status_label: str
    source: str | None = None
    travel_destination: str | None = None
    message: str | None = None
    value: Decimal | None = None
    priority: str | None = None
    assigned_to_name: str | None = None
    created_at: datetime
    updated_at: datetime


class BookingHistorySummaryRead(BaseModel):
    id: UUID
    status: str
    created_at: datetime
    itinerary_title: str | None = None


class CustomerFlagRead(BaseModel):
    id: UUID
    customer_id: UUID
    remark: str
    created_by_id: UUID
    created_by_name: str | None = None
    created_at: datetime


class CustomerFlagCreate(BaseModel):
    remark: str = Field(..., min_length=1, max_length=500)


class CustomerInteractionRead(BaseModel):
    id: str
    type: str
    at: datetime
    lead_id: UUID | None = None
    lead_code: str | None = None
    lead_title: str | None = None
    author_name: str | None = None
    title: str
    content: str | None = None
    activity_type: str | None = None
    status_label: str | None = None


class CustomerInquiryHistoryRead(BaseModel):
    customer_id: UUID | None = None
    customer_code: str | None = None
    inquiry_number: int | None = None
    total_inquiry_count: int = 0
    last_two_active_enquiries: list[InquiryLeadSummaryRead] = Field(default_factory=list)
    past_not_converted: list[InquiryLeadSummaryRead] = Field(default_factory=list)
    all_leads: list[InquiryLeadSummaryRead] = Field(default_factory=list)
    bookings: list[BookingHistorySummaryRead] = Field(default_factory=list)
    flags: list[CustomerFlagRead] = Field(default_factory=list)
    interactions: list[CustomerInteractionRead] = Field(default_factory=list)
    interaction_count: int = 0
    booking_count: int = 0
    flag_count: int = 0
