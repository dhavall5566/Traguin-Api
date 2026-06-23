from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead


class FaqBase(BaseModel):
    itinerary_id: UUID | None = None
    question: str = Field(..., min_length=1)
    answer: str = Field(..., min_length=1)
    sort_order: int = 0
    is_published: bool = True


class FaqCreate(FaqBase):
    pass


class FaqUpdate(BaseModel):
    itinerary_id: UUID | None = None
    question: str | None = Field(default=None, min_length=1)
    answer: str | None = Field(default=None, min_length=1)
    sort_order: int | None = None
    is_published: bool | None = None


class FaqRead(TimestampRead, FaqBase):
    pass
