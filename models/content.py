import uuid
from typing import Optional

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    ForeignKey,
    Index,
    Integer,
    SmallInteger,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class Faq(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "faqs"
    __table_args__ = (
        Index("ix_faqs_itinerary_id", "itinerary_id"),
        Index("ix_faqs_is_published", "is_published"),
    )

    itinerary_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=True
    )
    question: Mapped[str] = mapped_column(Text, nullable=False)
    answer: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        scope = f"itinerary={self.itinerary_id}" if self.itinerary_id else "about"
        return f"<Faq {scope} question={self.question[:40]!r}>"


class HomepagePromo(Base, TimestampMixin):
    __tablename__ = "homepage_promo"
    __table_args__ = (CheckConstraint("id = 1", name="ck_homepage_promo_singleton"),)

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, default=1)
    eyebrow: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    assurances: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)

    def __repr__(self) -> str:
        return "<HomepagePromo id=1>"


class HomepageRegionPanel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "homepage_region_panels"
    __table_args__ = (Index("ix_homepage_region_panels_key", "key", unique=True),)

    key: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    label: Mapped[str] = mapped_column(String(64), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    highlights: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False, default=list)
    stat_text: Mapped[str] = mapped_column(String(64), nullable=False)
    href: Mapped[str] = mapped_column(Text, nullable=False)
    mood: Mapped[Optional[str]] = mapped_column(String(16), nullable=True)
    hero_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return f"<HomepageRegionPanel key={self.key!r}>"


class JourneyProcessStep(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "journey_process_steps"
    __table_args__ = (Index("ix_journey_process_steps_sort_order", "sort_order"),)

    step_label: Mapped[str] = mapped_column(String(16), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    detail: Mapped[str] = mapped_column(Text, nullable=False)
    icon_key: Mapped[str] = mapped_column(String(64), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<JourneyProcessStep step={self.step_label!r} title={self.title!r}>"


class ValueProposition(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "value_propositions"
    __table_args__ = (Index("ix_value_propositions_sort_order", "sort_order"),)

    step_label: Mapped[str] = mapped_column(String(16), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    highlight: Mapped[str] = mapped_column(String(255), nullable=False)
    icon_key: Mapped[str] = mapped_column(String(64), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<ValueProposition step={self.step_label!r} title={self.title!r}>"


class Specialization(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "specializations"
    __table_args__ = (Index("ix_specializations_slug", "slug", unique=True),)

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    icon_key: Mapped[str] = mapped_column(String(64), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<Specialization slug={self.slug!r}>"


class ConciergeService(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "concierge_services"
    __table_args__ = (Index("ix_concierge_services_slug", "slug", unique=True),)

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    number_label: Mapped[str] = mapped_column(String(16), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    icon_key: Mapped[str] = mapped_column(String(64), nullable=False)
    image_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    is_featured: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_wide: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<ConciergeService slug={self.slug!r}>"


class TravelExpertSettings(Base, TimestampMixin):
    __tablename__ = "travel_expert_settings"
    __table_args__ = (CheckConstraint("id = 1", name="ck_travel_expert_settings_singleton"),)

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, default=1)
    desk_headline: Mapped[str] = mapped_column(String(255), nullable=False)
    hours_label: Mapped[str] = mapped_column(String(64), nullable=False)
    hours_value: Mapped[str] = mapped_column(String(64), nullable=False)
    live_desk_label: Mapped[str] = mapped_column(String(64), nullable=False)
    live_desk_value: Mapped[str] = mapped_column(String(64), nullable=False)

    def __repr__(self) -> str:
        return "<TravelExpertSettings id=1>"


class AboutStorySection(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "about_story_sections"
    __table_args__ = (Index("ix_about_story_sections_sort_order", "sort_order"),)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<AboutStorySection title={self.title!r}>"


class AboutClientLogo(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "about_client_logos"
    __table_args__ = (
        Index("ix_about_client_logos_slug", "slug", unique=True),
        Index("ix_about_client_logos_is_published", "is_published"),
        Index("ix_about_client_logos_sort_order", "sort_order"),
    )

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    logo_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return f"<AboutClientLogo slug={self.slug!r} name={self.name!r}>"


class AboutPageHeader(Base, TimestampMixin):
    __tablename__ = "about_page_header"
    __table_args__ = (CheckConstraint("id = 1", name="ck_about_page_header_singleton"),)

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, default=1)
    eyebrow: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    def __repr__(self) -> str:
        return "<AboutPageHeader id=1>"


class JobOpening(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "job_openings"
    __table_args__ = (
        Index("ix_job_openings_slug", "slug", unique=True),
        Index("ix_job_openings_is_published", "is_published"),
    )

    slug: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    employment_type: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __repr__(self) -> str:
        return f"<JobOpening slug={self.slug!r} title={self.title!r}>"


class CareersPageExtras(Base, TimestampMixin):
    __tablename__ = "careers_page_extras"
    __table_args__ = (CheckConstraint("id = 1", name="ck_careers_page_extras_singleton"),)

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, default=1)
    culture_chips: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False, default=list)
    fallback_title: Mapped[str] = mapped_column(String(255), nullable=False)
    fallback_description: Mapped[str] = mapped_column(Text, nullable=False)

    def __repr__(self) -> str:
        return "<CareersPageExtras id=1>"
