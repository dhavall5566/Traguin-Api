from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead


class MediaSummary(BaseModel):
    id: UUID
    url: str
    alt_text: str | None = None
    sort_order: int | None = None


class MediaAssetBase(BaseModel):
    slug: str | None = Field(default=None, max_length=255)
    url: str = Field(..., min_length=1)
    alt_text: str | None = None
    mime_type: str | None = Field(default=None, max_length=127)
    width: int | None = Field(default=None, ge=0)
    height: int | None = Field(default=None, ge=0)
    source: str = Field(default="external", max_length=32)
    usage: str | None = Field(default=None, max_length=64)
    tags: list[str] | None = None


class MediaAssetCreate(MediaAssetBase):
    pass


class MediaAssetUpdate(BaseModel):
    slug: str | None = Field(default=None, max_length=255)
    url: str | None = Field(default=None, min_length=1)
    alt_text: str | None = None
    mime_type: str | None = Field(default=None, max_length=127)
    width: int | None = Field(default=None, ge=0)
    height: int | None = Field(default=None, ge=0)
    source: str | None = Field(default=None, max_length=32)
    usage: str | None = Field(default=None, max_length=64)
    tags: list[str] | None = None


class MediaAssetRead(TimestampRead, MediaAssetBase):
    pass
