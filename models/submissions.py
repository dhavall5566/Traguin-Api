import uuid
from typing import Optional

from sqlalchemy import ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import INET, JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class FormSubmission(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Single-table store for all public form submissions."""

    __tablename__ = "form_submissions"
    __table_args__ = (
        Index("ix_form_submissions_form_type_created_at", "form_type", "created_at"),
        Index("ix_form_submissions_email", "email"),
        Index("ix_form_submissions_phone", "phone"),
        Index("ix_form_submissions_status", "status"),
        Index("ix_form_submissions_related_itinerary_id", "related_itinerary_id"),
        Index("ix_form_submissions_related_hotel_id", "related_hotel_id"),
        Index("ix_form_submissions_related_destination_id", "related_destination_id"),
    )

    form_type: Mapped[str] = mapped_column(String(64), nullable=False)
    payload: Mapped[dict] = mapped_column(JSONB, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="new")
    related_itinerary_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("itineraries.id", ondelete="SET NULL"), nullable=True
    )
    related_hotel_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("hotels.id", ondelete="SET NULL"), nullable=True
    )
    related_destination_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("destinations.id", ondelete="SET NULL"), nullable=True
    )
    ip_address: Mapped[Optional[str]] = mapped_column(INET, nullable=True)
    user_agent: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<FormSubmission form_type={self.form_type!r} status={self.status!r}>"
