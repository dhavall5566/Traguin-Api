from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead
from schemas.media import MediaSummary

INDIA_REGION_PATTERN = "^(north|east|south|west|central|islands|northeast|north-east)$"


class DestinationCategoryBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    sort_order: int = 0


class DestinationCategoryCreate(DestinationCategoryBase):
    pass


class DestinationCategoryUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    sort_order: int | None = None


class DestinationCategoryRead(TimestampRead, DestinationCategoryBase):
    pass


class DestinationCategorySummary(BaseModel):
    id: UUID
    slug: str
    title: str
    sort_order: int | None = None


class DestinationBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    name: str = Field(..., min_length=1, max_length=255)
    country: str | None = Field(default=None, max_length=255)
    region: str = Field(..., pattern="^(domestic|international)$")
    india_region: str | None = Field(default=None, pattern=INDIA_REGION_PATTERN)
    description: str = Field(..., min_length=1)
    starting_price: int = Field(..., ge=0)
    hero_media_id: UUID | None = None
    lat: Decimal | None = None
    lng: Decimal | None = None
    moods: list[str] = Field(default_factory=list)
    package_count: int | None = Field(default=None, ge=0)
    hotel_count: int | None = Field(default=None, ge=0)
    is_featured: bool = False
    featured_sort_order: int | None = None
    is_published: bool = True
    meta_title: str | None = Field(default=None, max_length=255)
    meta_description: str | None = None


class DestinationCreate(DestinationBase):
    category_ids: list[UUID] = Field(default_factory=list)
    gallery_media_ids: list[UUID] = Field(default_factory=list)


class DestinationUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    name: str | None = Field(default=None, min_length=1, max_length=255)
    country: str | None = Field(default=None, max_length=255)
    region: str | None = Field(default=None, pattern="^(domestic|international)$")
    india_region: str | None = Field(default=None, pattern=INDIA_REGION_PATTERN)
    description: str | None = Field(default=None, min_length=1)
    starting_price: int | None = Field(default=None, ge=0)
    hero_media_id: UUID | None = None
    lat: Decimal | None = None
    lng: Decimal | None = None
    moods: list[str] | None = None
    package_count: int | None = Field(default=None, ge=0)
    hotel_count: int | None = Field(default=None, ge=0)
    is_featured: bool | None = None
    featured_sort_order: int | None = None
    is_published: bool | None = None
    meta_title: str | None = Field(default=None, max_length=255)
    meta_description: str | None = None
    category_ids: list[UUID] | None = None
    gallery_media_ids: list[UUID] | None = None


class DestinationRead(TimestampRead, DestinationBase):
    categories: list[DestinationCategorySummary] = Field(default_factory=list)
    gallery_media: list[MediaSummary] = Field(default_factory=list)
