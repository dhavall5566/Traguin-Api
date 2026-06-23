from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead


class ExperienceOfferNested(BaseModel):
    icon_key: str = Field(..., min_length=1, max_length=64)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    sort_order: int = 0


class ExperienceOfferRead(TimestampRead, ExperienceOfferNested):
    pass


class ExperienceStatNested(BaseModel):
    value: str = Field(..., min_length=1, max_length=64)
    label: str = Field(..., min_length=1, max_length=255)
    sort_order: int = 0


class ExperienceStatRead(TimestampRead, ExperienceStatNested):
    pass


class ExperienceProcessStepNested(BaseModel):
    step_label: str = Field(..., min_length=1, max_length=16)
    title: str = Field(..., min_length=1, max_length=255)
    detail: str = Field(..., min_length=1)
    sort_order: int = 0


class ExperienceProcessStepRead(TimestampRead, ExperienceProcessStepNested):
    pass


class ExperienceBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    eyebrow: str = Field(..., min_length=1, max_length=255)
    headline: str = Field(..., min_length=1, max_length=255)
    intro: str = Field(..., min_length=1)
    hero_media_id: UUID | None = None
    card_number: str | None = Field(default=None, max_length=16)
    card_title: str | None = Field(default=None, max_length=255)
    card_description: str | None = None
    image_caption: str | None = None
    layout: str | None = Field(default=None, max_length=32)
    variant: str | None = Field(default=None, max_length=16)
    quote: str | None = None
    cta_title: str | None = Field(default=None, max_length=255)
    cta_description: str | None = None
    show_on_homepage: bool = True
    homepage_sort_order: int | None = None
    is_published: bool = True


class ExperienceCreate(ExperienceBase):
    offers: list[ExperienceOfferNested] = Field(default_factory=list)
    stats: list[ExperienceStatNested] = Field(default_factory=list)
    process_steps: list[ExperienceProcessStepNested] = Field(default_factory=list)


class ExperienceUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    eyebrow: str | None = Field(default=None, min_length=1, max_length=255)
    headline: str | None = Field(default=None, min_length=1, max_length=255)
    intro: str | None = Field(default=None, min_length=1)
    hero_media_id: UUID | None = None
    card_number: str | None = Field(default=None, max_length=16)
    card_title: str | None = Field(default=None, max_length=255)
    card_description: str | None = None
    image_caption: str | None = None
    layout: str | None = Field(default=None, max_length=32)
    variant: str | None = Field(default=None, max_length=16)
    quote: str | None = None
    cta_title: str | None = Field(default=None, max_length=255)
    cta_description: str | None = None
    show_on_homepage: bool | None = None
    homepage_sort_order: int | None = None
    is_published: bool | None = None
    offers: list[ExperienceOfferNested] | None = None
    stats: list[ExperienceStatNested] | None = None
    process_steps: list[ExperienceProcessStepNested] | None = None


class ExperienceRead(TimestampRead, ExperienceBase):
    offers: list[ExperienceOfferRead] = Field(default_factory=list)
    stats: list[ExperienceStatRead] = Field(default_factory=list)
    process_steps: list[ExperienceProcessStepRead] = Field(default_factory=list)
