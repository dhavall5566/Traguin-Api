from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead


class LegalPageBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    eyebrow: str = Field(..., min_length=1, max_length=255)
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    effective_date: str = Field(..., min_length=1, max_length=64)
    hero_media_id: UUID | None = None
    hero_image_alt: str | None = None
    sections: list = Field(default_factory=list)
    meta_title: str | None = Field(default=None, max_length=255)


class LegalPageCreate(LegalPageBase):
    pass


class LegalPageUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    eyebrow: str | None = Field(default=None, min_length=1, max_length=255)
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1)
    effective_date: str | None = Field(default=None, min_length=1, max_length=64)
    hero_media_id: UUID | None = None
    hero_image_alt: str | None = None
    sections: list | None = None
    meta_title: str | None = Field(default=None, max_length=255)


class LegalPageRead(TimestampRead, LegalPageBase):
    pass
