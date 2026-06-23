from uuid import UUID

from pydantic import BaseModel, Field


class HomepageHeroSliderSettingsRead(BaseModel):
    hero_slider_max_items: int = Field(..., ge=1, le=20)
    visible_package_ids: list[UUID] = Field(default_factory=list)


class HomepageHeroSliderSettingsUpdate(BaseModel):
    hero_slider_max_items: int | None = Field(default=None, ge=1, le=20)
    visible_package_ids: list[UUID] | None = None


class HomepageHeroSliderOrderUpdate(BaseModel):
    package_ids: list[UUID] = Field(..., min_length=1)
