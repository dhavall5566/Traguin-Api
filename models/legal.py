import uuid
from typing import Optional

from sqlalchemy import ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class LegalPage(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "legal_pages"
    __table_args__ = (Index("ix_legal_pages_slug", "slug", unique=True),)

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    eyebrow: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    effective_date: Mapped[str] = mapped_column(String(64), nullable=False)
    hero_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    hero_image_alt: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    sections: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)
    meta_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    def __repr__(self) -> str:
        return f"<LegalPage slug={self.slug!r}>"
