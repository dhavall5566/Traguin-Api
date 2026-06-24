from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import ORMModel, TimestampRead


class JourneyProcessStepBase(BaseModel):
    step_label: str = Field(..., min_length=1, max_length=16)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    detail: str = Field(..., min_length=1)
    icon_key: str = Field(..., min_length=1, max_length=64)
    sort_order: int = 0


class JourneyProcessStepCreate(JourneyProcessStepBase):
    pass


class JourneyProcessStepUpdate(BaseModel):
    step_label: str | None = Field(default=None, min_length=1, max_length=16)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    detail: str | None = Field(default=None, min_length=1)
    icon_key: str | None = Field(default=None, min_length=1, max_length=64)
    sort_order: int | None = None


class JourneyProcessStepRead(TimestampRead, JourneyProcessStepBase):
    pass


class ValuePropositionBase(BaseModel):
    step_label: str = Field(..., min_length=1, max_length=16)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    highlight: str = Field(..., min_length=1, max_length=255)
    icon_key: str = Field(..., min_length=1, max_length=64)
    sort_order: int = 0


class ValuePropositionCreate(ValuePropositionBase):
    pass


class ValuePropositionUpdate(BaseModel):
    step_label: str | None = Field(default=None, min_length=1, max_length=16)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    highlight: str | None = Field(default=None, min_length=1, max_length=255)
    icon_key: str | None = Field(default=None, min_length=1, max_length=64)
    sort_order: int | None = None


class ValuePropositionRead(TimestampRead, ValuePropositionBase):
    pass


class ConciergeServiceBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    number_label: str = Field(..., min_length=1, max_length=16)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    icon_key: str = Field(..., min_length=1, max_length=64)
    image_media_id: UUID | None = None
    is_featured: bool = False
    is_wide: bool = False
    sort_order: int = 0


class ConciergeServiceCreate(ConciergeServiceBase):
    pass


class ConciergeServiceUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    number_label: str | None = Field(default=None, min_length=1, max_length=16)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    icon_key: str | None = Field(default=None, min_length=1, max_length=64)
    image_media_id: UUID | None = None
    is_featured: bool | None = None
    is_wide: bool | None = None
    sort_order: int | None = None


class ConciergeServiceRead(TimestampRead, ConciergeServiceBase):
    pass


class HomepageRegionPanelBase(BaseModel):
    key: str = Field(..., min_length=1, max_length=32)
    label: str = Field(..., min_length=1, max_length=64)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    highlights: list[str] = Field(default_factory=list)
    stat_text: str = Field(..., min_length=1, max_length=64)
    href: str = Field(..., min_length=1)
    mood: str | None = Field(default=None, max_length=16)
    hero_media_id: UUID | None = None
    sort_order: int = 0
    is_active: bool = True


class HomepageRegionPanelCreate(HomepageRegionPanelBase):
    pass


class HomepageRegionPanelUpdate(BaseModel):
    key: str | None = Field(default=None, min_length=1, max_length=32)
    label: str | None = Field(default=None, min_length=1, max_length=64)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    highlights: list[str] | None = None
    stat_text: str | None = Field(default=None, min_length=1, max_length=64)
    href: str | None = Field(default=None, min_length=1)
    mood: str | None = Field(default=None, max_length=16)
    hero_media_id: UUID | None = None
    sort_order: int | None = None
    is_active: bool | None = None


class HomepageRegionPanelRead(TimestampRead, HomepageRegionPanelBase):
    pass


class AboutStorySectionBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    body: str = Field(..., min_length=1)
    sort_order: int = 0


class AboutStorySectionCreate(AboutStorySectionBase):
    pass


class AboutStorySectionUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    body: str | None = Field(default=None, min_length=1)
    sort_order: int | None = None


class AboutStorySectionRead(TimestampRead, AboutStorySectionBase):
    pass


class HomepagePromoBase(BaseModel):
    eyebrow: str = Field(..., min_length=1, max_length=255)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    assurances: list = Field(default_factory=list)


class HomepagePromoUpdate(BaseModel):
    eyebrow: str | None = Field(default=None, min_length=1, max_length=255)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    assurances: list | None = None


class HomepagePromoRead(HomepagePromoBase, ORMModel):
    id: int
    created_at: datetime
    updated_at: datetime


class TravelExpertSettingsBase(BaseModel):
    desk_headline: str = Field(..., min_length=1, max_length=255)
    hours_label: str = Field(..., min_length=1, max_length=64)
    hours_value: str = Field(..., min_length=1, max_length=64)
    live_desk_label: str = Field(..., min_length=1, max_length=64)
    live_desk_value: str = Field(..., min_length=1, max_length=64)


class TravelExpertSettingsUpdate(BaseModel):
    desk_headline: str | None = Field(default=None, min_length=1, max_length=255)
    hours_label: str | None = Field(default=None, min_length=1, max_length=64)
    hours_value: str | None = Field(default=None, min_length=1, max_length=64)
    live_desk_label: str | None = Field(default=None, min_length=1, max_length=64)
    live_desk_value: str | None = Field(default=None, min_length=1, max_length=64)


class TravelExpertSettingsRead(TravelExpertSettingsBase, ORMModel):
    id: int
    created_at: datetime
    updated_at: datetime


class AboutPageHeaderBase(BaseModel):
    eyebrow: str = Field(..., min_length=1, max_length=255)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)


class AboutPageHeaderUpdate(BaseModel):
    eyebrow: str | None = Field(default=None, min_length=1, max_length=255)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)


class AboutPageHeaderRead(AboutPageHeaderBase, ORMModel):
    id: int
    created_at: datetime
    updated_at: datetime


class JobOpeningBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    title: str = Field(..., min_length=1, max_length=255)
    location: str = Field(..., min_length=1, max_length=255)
    employment_type: str = Field(..., min_length=1, max_length=64)
    description: str = Field(..., min_length=1)
    sort_order: int = 0
    is_published: bool = True


class JobOpeningCreate(JobOpeningBase):
    pass


class JobOpeningUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    location: str | None = Field(default=None, min_length=1, max_length=255)
    employment_type: str | None = Field(default=None, min_length=1, max_length=64)
    description: str | None = Field(default=None, min_length=1)
    sort_order: int | None = None
    is_published: bool | None = None


class JobOpeningRead(TimestampRead, JobOpeningBase):
    pass


class CareersPageExtrasBase(BaseModel):
    culture_chips: list[str] = Field(default_factory=list)
    fallback_title: str = Field(..., min_length=1, max_length=255)
    fallback_description: str = Field(..., min_length=1)


class CareersPageExtrasUpdate(BaseModel):
    culture_chips: list[str] | None = None
    fallback_title: str | None = Field(default=None, min_length=1, max_length=255)
    fallback_description: str | None = Field(default=None, min_length=1)


class CareersPageExtrasRead(CareersPageExtrasBase, ORMModel):
    id: int
    created_at: datetime
    updated_at: datetime
