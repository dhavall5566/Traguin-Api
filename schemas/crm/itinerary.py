from datetime import datetime
from decimal import Decimal
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.crm.common import CrmORMModel, CrmTimestampRead


class ItineraryItemNested(BaseModel):
    type: str = Field(..., min_length=1, max_length=32)
    title: str = Field(..., min_length=1, max_length=255)
    details: Any | None = None
    cost_price: Decimal = Field(default=Decimal("0.00"), ge=0)
    selling_price: Decimal = Field(default=Decimal("0.00"), ge=0)
    order: int = Field(default=0, ge=0)


class ItineraryDayNested(BaseModel):
    day_number: int = Field(..., ge=1)
    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    items: list[ItineraryItemNested] = Field(default_factory=list)


class ItineraryItemRead(CrmORMModel):
    id: UUID
    itinerary_day_id: UUID
    type: str
    title: str
    details: Any | None
    cost_price: Decimal
    selling_price: Decimal
    order: int


class ItineraryDayRead(CrmORMModel):
    id: UUID
    itinerary_id: UUID
    day_number: int
    title: str
    description: str | None
    items: list[ItineraryItemRead] = Field(default_factory=list)


class ItineraryBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    customer_id: UUID | None = None
    status: str = Field(default="DRAFT", max_length=32)
    total_price: Decimal = Field(default=Decimal("0.00"), ge=0)
    markup_margin: Decimal = Field(default=Decimal("0.00"), ge=0)
    tax_rate: Decimal = Field(default=Decimal("0.00"), ge=0)
    is_template: bool = False


class ItineraryCreate(ItineraryBase):
    days: list[ItineraryDayNested] = Field(default_factory=list)


class ItineraryFromCmsPackageCreate(BaseModel):
    cms_package_id: UUID
    customer_id: UUID | None = None


class ItineraryUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    customer_id: UUID | None = None
    status: str | None = Field(default=None, max_length=32)
    total_price: Decimal | None = Field(default=None, ge=0)
    markup_margin: Decimal | None = Field(default=None, ge=0)
    tax_rate: Decimal | None = Field(default=None, ge=0)
    is_template: bool | None = None
    days: list[ItineraryDayNested] | None = None


class ItineraryRead(CrmTimestampRead, ItineraryBase):
    agency_id: UUID
    days: list[ItineraryDayRead] = Field(default_factory=list)


class ItineraryListRead(CrmTimestampRead, ItineraryBase):
    """Lightweight row for CRM tables — omits nested day plans."""

    agency_id: UUID
