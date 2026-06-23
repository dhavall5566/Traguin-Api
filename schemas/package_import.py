from uuid import UUID

from pydantic import BaseModel, Field

from schemas.destination import DestinationCreate
from schemas.itineraries import ItineraryCreate
from schemas.packages import PackageCreate


class ExtractedDestinationDraft(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    slug: str | None = Field(default=None, max_length=128)
    country: str | None = Field(default=None, max_length=255)
    region: str = Field(default="domestic", pattern="^(domestic|international)$")
    india_region: str | None = Field(default=None, pattern="^(north|east|south|west)$")
    description: str = Field(..., min_length=1)
    starting_price: int | None = Field(default=None, ge=0)
    moods: list[str] = Field(default_factory=list)
    is_domestic: bool | None = None


class ExtractedPackageDraft(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    slug: str | None = Field(default=None, max_length=128)
    tagline: str | None = None
    duration_label: str = Field(..., min_length=1, max_length=64)
    duration_days: int | None = Field(default=None, ge=1)
    starting_price: int | None = Field(default=None, ge=0)
    price_on_request: bool = False
    highlights: list[str] = Field(default_factory=list)
    moods: list[str] = Field(default_factory=list)


class ExtractedItineraryDayDraft(BaseModel):
    day_number: int = Field(..., ge=1)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    activities: list[str] = Field(default_factory=list)
    sort_order: int = 0


class ExtractedItineraryHotelDraft(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    location: str = Field(..., min_length=1, max_length=255)
    nights_label: str = Field(..., min_length=1, max_length=64)
    description: str | None = None
    category_label: str | None = Field(
        default=None,
        max_length=128,
        description="Hotel tier/option when PDF lists Standard/Deluxe/Premium rows.",
    )
    sort_order: int = 0


class ExtractedItineraryInclusionDraft(BaseModel):
    kind: str = Field(..., pattern="^(included|excluded)$")
    text: str = Field(..., min_length=1)
    sort_order: int = 0


class ExtractedItineraryHighlightDraft(BaseModel):
    text: str = Field(..., min_length=1)
    sort_order: int = 0


class ExtractedItineraryDraft(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    slug: str | None = Field(default=None, max_length=128)
    tagline: str = Field(..., min_length=1)
    overview: str = Field(..., min_length=1)
    duration_label: str = Field(..., min_length=1, max_length=64)
    duration_days: int = Field(..., ge=1)
    starting_price: int | None = Field(default=None, ge=0)
    price_on_request: bool = False
    price_note: str | None = None
    days: list[ExtractedItineraryDayDraft] = Field(default_factory=list)
    hotels: list[ExtractedItineraryHotelDraft] = Field(default_factory=list)
    inclusions: list[ExtractedItineraryInclusionDraft] = Field(default_factory=list)
    highlights: list[ExtractedItineraryHighlightDraft] = Field(default_factory=list)


class ExtractedPackageBundle(BaseModel):
    destination: ExtractedDestinationDraft
    package: ExtractedPackageDraft
    itinerary: ExtractedItineraryDraft
    places_mentioned: list[str] = Field(default_factory=list)


class SourcedPlaceImage(BaseModel):
    place: str
    search_query: str
    url: str | None = None
    preview_url: str | None = None
    photographer: str | None = None
    width: int | None = None
    height: int | None = None
    media_asset_id: UUID | None = None
    error: str | None = None


class PackageImportExtractResponse(BaseModel):
    filename: str
    raw_text: str
    raw_text_char_count: int
    extracted: ExtractedPackageBundle
    llm_raw_json: dict
    images: list[SourcedPlaceImage] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class PackageImportCommitRequest(BaseModel):
    destination: DestinationCreate
    package: PackageCreate
    itinerary: ItineraryCreate


class PackageImportReviewCommit(BaseModel):
    destination: ExtractedDestinationDraft
    package: ExtractedPackageDraft
    itinerary: ExtractedItineraryDraft
    category_ids: list[UUID] = Field(default_factory=list)
    hero_media_id: UUID | None = None
    package_hero_media_id: UUID | None = None
    itinerary_hero_media_id: UUID | None = None
    gallery_media_ids: list[UUID] = Field(default_factory=list)


class PackageImportCommitResponse(BaseModel):
    destination_id: UUID
    package_id: UUID
    itinerary_id: UUID
    destination_slug: str
    package_slug: str
    itinerary_slug: str
