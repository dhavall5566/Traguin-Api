from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead
from schemas.media import MediaSummary


class ItineraryHighlightNested(BaseModel):
    text: str = Field(..., min_length=1)
    sort_order: int = 0


class ItineraryHighlightRead(TimestampRead, ItineraryHighlightNested):
    pass


class ItineraryDayNested(BaseModel):
    day_number: int = Field(..., ge=1)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    activities: list[str] = Field(default_factory=list)
    sort_order: int = 0


class ItineraryDayRead(TimestampRead, ItineraryDayNested):
    pass


class ItineraryHotelNested(BaseModel):
    hotel_id: UUID | None = None
    name: str = Field(..., min_length=1, max_length=255)
    location: str = Field(..., min_length=1, max_length=255)
    nights_label: str = Field(..., min_length=1, max_length=64)
    description: str | None = None
    stars: int | None = Field(default=None, ge=1, le=5)
    category_label: str | None = Field(default=None, max_length=128)
    room_type: str | None = Field(default=None, max_length=128)
    meal_plan: str | None = Field(default=None, max_length=128)
    image_media_id: UUID | None = None
    sort_order: int = 0


class ItineraryHotelRead(TimestampRead, ItineraryHotelNested):
    pass


class ItineraryInclusionNested(BaseModel):
    kind: str = Field(..., pattern="^(included|excluded)$")
    text: str = Field(..., min_length=1)
    sort_order: int = 0


class ItineraryInclusionRead(TimestampRead, ItineraryInclusionNested):
    pass


class ItineraryBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    package_id: UUID | None = None
    destination_id: UUID
    title: str = Field(..., min_length=1, max_length=255)
    duration_label: str = Field(..., min_length=1, max_length=64)
    duration_days: int = Field(..., ge=1)
    starting_price: int = Field(..., ge=0)
    price_note: str | None = None
    rating: Decimal | None = None
    review_count: int | None = Field(default=None, ge=0)
    hero_media_id: UUID | None = None
    tagline: str = Field(..., min_length=1)
    overview: str = Field(..., min_length=1)
    is_featured: bool = False
    featured_sort_order: int | None = None
    seo_title: str | None = Field(default=None, max_length=255)
    seo_description: str | None = None
    is_published: bool = True


class ItineraryCreate(ItineraryBase):
    highlights: list[ItineraryHighlightNested] = Field(default_factory=list)
    days: list[ItineraryDayNested] = Field(default_factory=list)
    hotels: list[ItineraryHotelNested] = Field(default_factory=list)
    inclusions: list[ItineraryInclusionNested] = Field(default_factory=list)
    gallery_media_ids: list[UUID] = Field(default_factory=list)


class ItineraryUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    package_id: UUID | None = None
    destination_id: UUID | None = None
    title: str | None = Field(default=None, min_length=1, max_length=255)
    duration_label: str | None = Field(default=None, min_length=1, max_length=64)
    duration_days: int | None = Field(default=None, ge=1)
    starting_price: int | None = Field(default=None, ge=0)
    price_note: str | None = None
    rating: Decimal | None = None
    review_count: int | None = Field(default=None, ge=0)
    hero_media_id: UUID | None = None
    tagline: str | None = Field(default=None, min_length=1)
    overview: str | None = Field(default=None, min_length=1)
    is_featured: bool | None = None
    featured_sort_order: int | None = None
    seo_title: str | None = Field(default=None, max_length=255)
    seo_description: str | None = None
    is_published: bool | None = None
    highlights: list[ItineraryHighlightNested] | None = None
    days: list[ItineraryDayNested] | None = None
    hotels: list[ItineraryHotelNested] | None = None
    inclusions: list[ItineraryInclusionNested] | None = None
    gallery_media_ids: list[UUID] | None = None


class ItineraryRead(TimestampRead, ItineraryBase):
    highlights: list[ItineraryHighlightRead] = Field(default_factory=list)
    days: list[ItineraryDayRead] = Field(default_factory=list)
    hotels: list[ItineraryHotelRead] = Field(default_factory=list)
    inclusions: list[ItineraryInclusionRead] = Field(default_factory=list)
    gallery_media: list[MediaSummary] = Field(default_factory=list)


class ItineraryListRead(TimestampRead):
    slug: str
    serial_code: str | None = None
    package_id: UUID | None = None
    package_title: str | None = None
    destination_id: UUID
    destination_name: str
    title: str
    duration_label: str
    duration_days: int = Field(..., ge=1)
    starting_price: int = Field(..., ge=0)
    price_note: str | None = None
    is_featured: bool = False
    featured_sort_order: int | None = None
    is_published: bool = True
