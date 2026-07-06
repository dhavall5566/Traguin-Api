from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead


class PackageHighlightNested(BaseModel):
    text: str = Field(..., min_length=1)
    sort_order: int = 0


class PackageHighlightRead(TimestampRead, PackageHighlightNested):
    pass


class PackageBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    serial_code: str | None = Field(default=None, min_length=1, max_length=16)
    traguin_tour_code: str | None = Field(default=None, min_length=1, max_length=128)
    destination_id: UUID
    title: str = Field(..., min_length=1, max_length=255)
    duration_label: str = Field(..., min_length=1, max_length=64)
    price: int = Field(..., ge=0)
    sold_last_month: int = Field(default=0, ge=0)
    hero_media_id: UUID | None = None
    rating: Decimal | None = None
    is_featured: bool = False
    featured_sort_order: int | None = None
    is_published: bool = True


class PackageCreate(PackageBase):
    highlights: list[PackageHighlightNested] = Field(default_factory=list)
    moods: list[str] = Field(default_factory=list)


class PackageUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    serial_code: str | None = Field(default=None, min_length=1, max_length=16)
    traguin_tour_code: str | None = Field(default=None, min_length=1, max_length=128)
    destination_id: UUID | None = None
    title: str | None = Field(default=None, min_length=1, max_length=255)
    duration_label: str | None = Field(default=None, min_length=1, max_length=64)
    price: int | None = Field(default=None, ge=0)
    sold_last_month: int | None = Field(default=None, ge=0)
    hero_media_id: UUID | None = None
    rating: Decimal | None = None
    is_featured: bool | None = None
    featured_sort_order: int | None = None
    is_published: bool | None = None
    highlights: list[PackageHighlightNested] | None = None
    moods: list[str] | None = None


class PackageRead(TimestampRead, PackageBase):
    highlights: list[PackageHighlightRead] = Field(default_factory=list)
    moods: list[str] = Field(default_factory=list)


class PackageListRead(TimestampRead):
    slug: str
    serial_code: str | None = None
    traguin_tour_code: str | None = None
    destination_id: UUID
    destination_name: str
    title: str
    duration_label: str
    price: int = Field(..., ge=0)
    sold_last_month: int = Field(default=0, ge=0)
    hero_media_id: UUID | None = None
    rating: Decimal | None = None
    is_featured: bool = False
    featured_sort_order: int | None = None
    is_published: bool = True
