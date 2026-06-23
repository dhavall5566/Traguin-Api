from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from schemas.crm.common import CrmTimestampRead


class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=255)
    phone: str | None = Field(default=None, max_length=64)


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)
    agency_id: UUID | None = None


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    name: str | None = Field(default=None, min_length=1, max_length=255)
    phone: str | None = Field(default=None, max_length=64)
    password: str | None = Field(default=None, min_length=8, max_length=128)
    agency_id: UUID | None = None


class UserRead(CrmTimestampRead, UserBase):
    agency_id: UUID | None
    is_deleted: bool
