from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead
from schemas.media import MediaSummary


class HotelNearbyAttractionNested(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    distance_label: str = Field(..., min_length=1, max_length=64)
    sort_order: int = 0


class HotelNearbyAttractionRead(TimestampRead, HotelNearbyAttractionNested):
    pass


class HotelBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    destination_id: UUID
    name: str = Field(..., min_length=1, max_length=255)
    stars: int = Field(..., ge=1, le=5)
    price: int = Field(..., ge=0)
    rating: Decimal | None = None
    review_count: int | None = Field(default=None, ge=0)
    description: str | None = None
    hero_media_id: UUID | None = None
    amenities: list[str] = Field(default_factory=list)
    is_published: bool = True


class HotelCreate(HotelBase):
    nearby_attractions: list[HotelNearbyAttractionNested] = Field(default_factory=list)
    gallery_media_ids: list[UUID] = Field(default_factory=list)


class HotelUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    destination_id: UUID | None = None
    name: str | None = Field(default=None, min_length=1, max_length=255)
    stars: int | None = Field(default=None, ge=1, le=5)
    price: int | None = Field(default=None, ge=0)
    rating: Decimal | None = None
    review_count: int | None = Field(default=None, ge=0)
    description: str | None = None
    hero_media_id: UUID | None = None
    amenities: list[str] | None = None
    is_published: bool | None = None
    nearby_attractions: list[HotelNearbyAttractionNested] | None = None
    gallery_media_ids: list[UUID] | None = None


class HotelRead(TimestampRead, HotelBase):
    nearby_attractions: list[HotelNearbyAttractionRead] = Field(default_factory=list)
    gallery_media: list[MediaSummary] = Field(default_factory=list)


class HotelListRead(TimestampRead):
    slug: str
    destination_id: UUID
    destination_name: str
    name: str
    stars: int = Field(..., ge=1, le=5)
    price: int = Field(..., ge=0)
    rating: Decimal | None = None
    is_published: bool = True
