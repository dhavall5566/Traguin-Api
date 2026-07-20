from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from schemas.crm.common import CrmTimestampRead


class CustomerBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=128)
    last_name: str = Field(..., min_length=1, max_length=128)
    email: EmailStr
    phone: str | None = Field(default=None, max_length=64)
    customer_code: str | None = Field(default=None, max_length=32)
    passport_number: str | None = Field(default=None, max_length=64)
    passport_expiry: datetime | None = None
    travel_history: Any | None = None
    documents: Any | None = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    first_name: str | None = Field(default=None, min_length=1, max_length=128)
    last_name: str | None = Field(default=None, min_length=1, max_length=128)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=64)
    customer_code: str | None = Field(default=None, max_length=32)
    passport_number: str | None = Field(default=None, max_length=64)
    passport_expiry: datetime | None = None
    travel_history: Any | None = None
    documents: Any | None = None


class CustomerRead(CrmTimestampRead, CustomerBase):
    agency_id: UUID
    is_deleted: bool
