from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import ORMModel


class SiteSettingsBase(BaseModel):
    phone: str = Field(..., min_length=1, max_length=32)
    phone_href: str = Field(..., min_length=1, max_length=64)
    whatsapp: str = Field(..., min_length=1, max_length=32)
    whatsapp_href: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1, max_length=255)
    email_href: str = Field(..., min_length=1, max_length=255)
    inquiry_email: str = Field(..., min_length=1, max_length=255)
    instagram_url: str | None = None
    address: str = Field(..., min_length=1)
    hours: str = Field(..., min_length=1, max_length=255)
    footer_tagline: str = Field(..., min_length=1)
    copyright_text: str = Field(..., min_length=1)
    default_meta_title: str = Field(..., min_length=1, max_length=255)
    default_meta_description: str = Field(..., min_length=1)
    default_meta_keywords: list[str] | None = None
    og_title: str | None = Field(default=None, max_length=255)
    og_description: str | None = None
    favicon_media_id: UUID | None = None
    icon_media_id: UUID | None = None
    apple_icon_media_id: UUID | None = None
    logo_media_id: UUID | None = None


class SiteSettingsUpdate(BaseModel):
    phone: str | None = Field(default=None, min_length=1, max_length=32)
    phone_href: str | None = Field(default=None, min_length=1, max_length=64)
    whatsapp: str | None = Field(default=None, min_length=1, max_length=32)
    whatsapp_href: str | None = Field(default=None, min_length=1)
    email: str | None = Field(default=None, min_length=1, max_length=255)
    email_href: str | None = Field(default=None, min_length=1, max_length=255)
    inquiry_email: str | None = Field(default=None, min_length=1, max_length=255)
    instagram_url: str | None = None
    address: str | None = Field(default=None, min_length=1)
    hours: str | None = Field(default=None, min_length=1, max_length=255)
    footer_tagline: str | None = Field(default=None, min_length=1)
    copyright_text: str | None = Field(default=None, min_length=1)
    default_meta_title: str | None = Field(default=None, min_length=1, max_length=255)
    default_meta_description: str | None = Field(default=None, min_length=1)
    default_meta_keywords: list[str] | None = None
    og_title: str | None = Field(default=None, max_length=255)
    og_description: str | None = None
    favicon_media_id: UUID | None = None
    icon_media_id: UUID | None = None
    apple_icon_media_id: UUID | None = None
    logo_media_id: UUID | None = None


class SiteSettingsRead(SiteSettingsBase, ORMModel):
    id: int
    created_at: datetime
    updated_at: datetime
