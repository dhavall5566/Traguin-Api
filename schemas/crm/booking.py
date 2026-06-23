from uuid import UUID

from pydantic import BaseModel, Field

from schemas.crm.common import CrmTimestampRead


class BookingBase(BaseModel):
    customer_id: UUID
    itinerary_id: UUID | None = None
    status: str = Field(default="PENDING", max_length=32)
    voucher_url: str | None = Field(default=None, max_length=2048)
    ticket_url: str | None = Field(default=None, max_length=2048)
    hotel_confirmation_code: str | None = Field(default=None, max_length=128)
    driver_name: str | None = Field(default=None, max_length=255)
    driver_phone: str | None = Field(default=None, max_length=64)
    visa_status: str | None = Field(default=None, max_length=64)


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BaseModel):
    customer_id: UUID | None = None
    itinerary_id: UUID | None = None
    status: str | None = Field(default=None, max_length=32)
    voucher_url: str | None = Field(default=None, max_length=2048)
    ticket_url: str | None = Field(default=None, max_length=2048)
    hotel_confirmation_code: str | None = Field(default=None, max_length=128)
    driver_name: str | None = Field(default=None, max_length=255)
    driver_phone: str | None = Field(default=None, max_length=64)
    visa_status: str | None = Field(default=None, max_length=64)


class BookingRead(CrmTimestampRead, BookingBase):
    agency_id: UUID
