from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import TimestampRead
from schemas.media import MediaSummary


class GalleryCategorySummary(BaseModel):
    id: UUID
    slug: str
    label: str


class GalleryCategoryBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=64)
    label: str = Field(..., min_length=1, max_length=128)
    sort_order: int = 0


class GalleryCategoryCreate(GalleryCategoryBase):
    pass


class GalleryCategoryUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=64)
    label: str | None = Field(default=None, min_length=1, max_length=128)
    sort_order: int | None = None


class GalleryCategoryRead(TimestampRead, GalleryCategoryBase):
    pass


class GalleryItemBase(BaseModel):
    slug: str = Field(..., min_length=1, max_length=128)
    place: str = Field(..., min_length=1, max_length=255)
    region_label: str = Field(..., min_length=1, max_length=255)
    layout: str = Field(..., min_length=1, max_length=16)
    label_style: str = Field(..., min_length=1, max_length=16)
    sort_order: int | None = None
    is_published: bool = True


class GalleryItemCreate(GalleryItemBase):
    category_ids: list[UUID] = Field(default_factory=list)
    media_ids: list[UUID] = Field(..., min_length=1)


class GalleryItemUpdate(BaseModel):
    slug: str | None = Field(default=None, min_length=1, max_length=128)
    place: str | None = Field(default=None, min_length=1, max_length=255)
    region_label: str | None = Field(default=None, min_length=1, max_length=255)
    layout: str | None = Field(default=None, min_length=1, max_length=16)
    label_style: str | None = Field(default=None, min_length=1, max_length=16)
    sort_order: int | None = None
    is_published: bool | None = None
    category_ids: list[UUID] | None = None
    media_ids: list[UUID] | None = Field(default=None, min_length=1)


class GalleryItemRead(TimestampRead, GalleryItemBase):
    media_id: UUID | None = None
    media: list[MediaSummary] = Field(default_factory=list)
    categories: list[GalleryCategorySummary] = Field(default_factory=list)


class ClientStoryBase(BaseModel):
    client_name: str = Field(..., min_length=1, max_length=255)
    destination_id: UUID | None = None
    quote: str | None = None
    portrait_media_id: UUID | None = None
    show_on_home: bool = False
    show_in_gallery: bool = False
    is_featured_in_gallery: bool = False
    home_sort_order: int | None = None
    gallery_sort_order: int | None = None
    is_published: bool = False


class ClientStoryCreate(ClientStoryBase):
    pass


class ClientStoryUpdate(BaseModel):
    client_name: str | None = Field(default=None, min_length=1, max_length=255)
    destination_id: UUID | None = None
    quote: str | None = None
    portrait_media_id: UUID | None = None
    show_on_home: bool | None = None
    show_in_gallery: bool | None = None
    is_featured_in_gallery: bool | None = None
    home_sort_order: int | None = None
    gallery_sort_order: int | None = None
    is_published: bool | None = None


class ClientStoryRead(TimestampRead, ClientStoryBase):
    destination_name: str | None = None
