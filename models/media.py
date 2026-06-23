import uuid
from typing import Optional

from sqlalchemy import Index, Integer, String, Text
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class MediaAsset(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "media_assets"
    __table_args__ = (
        Index("ix_media_assets_slug", "slug", unique=True),
        Index("ix_media_assets_usage", "usage"),
    )

    slug: Mapped[Optional[str]] = mapped_column(String(255), unique=True, nullable=True)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    alt_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    mime_type: Mapped[Optional[str]] = mapped_column(String(127), nullable=True)
    width: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    height: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    source: Mapped[str] = mapped_column(String(32), nullable=False, default="external")
    usage: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    tags: Mapped[Optional[list[str]]] = mapped_column(ARRAY(Text), nullable=True)

    def __repr__(self) -> str:
        return f"<MediaAsset id={self.id} slug={self.slug!r} usage={self.usage!r}>"
