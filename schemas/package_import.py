"""JSON import format for bulk package + itinerary inserts (no images)."""

from __future__ import annotations

from decimal import Decimal

from pydantic import BaseModel, Field

from schemas.itineraries import (
    ItineraryDayNested,
    ItineraryHighlightNested,
    ItineraryHotelNested,
    ItineraryInclusionNested,
)
from schemas.packages import PackageHighlightNested


class PackageImportData(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    serial_code: str | None = Field(default=None, min_length=1, max_length=16)
    traguin_tour_code: str | None = Field(default=None, min_length=1, max_length=128)
    title: str = Field(..., min_length=1, max_length=255)
    duration_label: str = Field(..., min_length=1, max_length=64)
    price: int = Field(default=0, ge=0)
    sold_last_month: int = Field(default=0, ge=0)
    rating: Decimal | None = Field(default=Decimal("4.9"))
    is_featured: bool = False
    featured_sort_order: int | None = None
    is_published: bool = False
    highlights: list[PackageHighlightNested] = Field(default_factory=list)
    moods: list[str] = Field(default_factory=list)


class ItineraryImportData(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    title: str = Field(..., min_length=1, max_length=255)
    duration_label: str = Field(..., min_length=1, max_length=64)
    duration_days: int = Field(..., ge=1)
    starting_price: int = Field(default=0, ge=0)
    price_note: str | None = None
    rating: Decimal | None = Field(default=Decimal("4.9"))
    review_count: int = Field(default=0, ge=0)
    tagline: str = Field(..., min_length=1)
    overview: str = Field(..., min_length=1)
    is_featured: bool = False
    featured_sort_order: int | None = None
    seo_title: str | None = Field(default=None, max_length=255)
    seo_description: str | None = None
    is_published: bool = False
    highlights: list[ItineraryHighlightNested] = Field(default_factory=list)
    days: list[ItineraryDayNested] = Field(default_factory=list)
    hotels: list[ItineraryHotelNested] = Field(default_factory=list)
    inclusions: list[ItineraryInclusionNested] = Field(default_factory=list)


class PackageImportFile(BaseModel):
    """One JSON file = one package + nested itinerary."""

    destination_slug: str = Field(..., min_length=1, max_length=128)
    package: PackageImportData
    itinerary: ItineraryImportData
