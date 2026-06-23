import uuid
from typing import Optional

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class Experience(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "experiences"
    __table_args__ = (
        Index("ix_experiences_slug", "slug", unique=True),
        Index("ix_experiences_show_on_homepage", "show_on_homepage"),
        Index("ix_experiences_is_published", "is_published"),
    )

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    eyebrow: Mapped[str] = mapped_column(String(255), nullable=False)
    headline: Mapped[str] = mapped_column(String(255), nullable=False)
    intro: Mapped[str] = mapped_column(Text, nullable=False)
    hero_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    card_number: Mapped[Optional[str]] = mapped_column(String(16), nullable=True)
    card_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    card_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    image_caption: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    layout: Mapped[Optional[str]] = mapped_column(String(32), nullable=True)
    variant: Mapped[Optional[str]] = mapped_column(String(16), nullable=True)
    quote: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    cta_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    cta_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    show_on_homepage: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    homepage_sort_order: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    offers: Mapped[list["ExperienceOffer"]] = relationship(
        back_populates="experience", cascade="all, delete-orphan", order_by="ExperienceOffer.sort_order"
    )
    stats: Mapped[list["ExperienceStat"]] = relationship(
        back_populates="experience", cascade="all, delete-orphan", order_by="ExperienceStat.sort_order"
    )
    process_steps: Mapped[list["ExperienceProcessStep"]] = relationship(
        back_populates="experience",
        cascade="all, delete-orphan",
        order_by="ExperienceProcessStep.sort_order",
    )

    def __repr__(self) -> str:
        return f"<Experience slug={self.slug!r}>"


class ExperienceOffer(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "experience_offers"
    __table_args__ = (Index("ix_experience_offers_experience_id", "experience_id"),)

    experience_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("experiences.id", ondelete="CASCADE"), nullable=False
    )
    icon_key: Mapped[str] = mapped_column(String(64), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    experience: Mapped["Experience"] = relationship(back_populates="offers")

    def __repr__(self) -> str:
        return f"<ExperienceOffer experience={self.experience_id} title={self.title!r}>"


class ExperienceStat(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "experience_stats"
    __table_args__ = (Index("ix_experience_stats_experience_id", "experience_id"),)

    experience_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("experiences.id", ondelete="CASCADE"), nullable=False
    )
    value: Mapped[str] = mapped_column(String(64), nullable=False)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    experience: Mapped["Experience"] = relationship(back_populates="stats")

    def __repr__(self) -> str:
        return f"<ExperienceStat experience={self.experience_id} value={self.value!r}>"


class ExperienceProcessStep(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "experience_process_steps"
    __table_args__ = (Index("ix_experience_process_steps_experience_id", "experience_id"),)

    experience_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("experiences.id", ondelete="CASCADE"), nullable=False
    )
    step_label: Mapped[str] = mapped_column(String(16), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    detail: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    experience: Mapped["Experience"] = relationship(back_populates="process_steps")

    def __repr__(self) -> str:
        return f"<ExperienceProcessStep experience={self.experience_id} step={self.step_label!r}>"
