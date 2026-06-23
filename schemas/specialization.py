from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead


class SpecializationBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    icon_key: str = Field(..., min_length=1, max_length=64)
    sort_order: int = 0


class SpecializationCreate(SpecializationBase):
    pass


class SpecializationUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    icon_key: str | None = Field(default=None, min_length=1, max_length=64)
    sort_order: int | None = None


class SpecializationRead(TimestampRead, SpecializationBase):
    pass
