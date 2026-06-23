from __future__ import annotations

import uuid
from typing import Optional

from sqlalchemy import ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, CreatedAtMixin, UUIDPrimaryKeyMixin


class AuditLog(CrmBase, UUIDPrimaryKeyMixin, CreatedAtMixin):
    __tablename__ = "audit_logs"
    __table_args__ = (
        Index("ix_audit_logs_agency_id", "agency_id"),
        Index("ix_audit_logs_user_id", "user_id"),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    action: Mapped[str] = mapped_column(String(32), nullable=False)
    entity_type: Mapped[str] = mapped_column(String(64), nullable=False)
    entity_id: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    details: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    agency: Mapped[Agency] = relationship(back_populates="audit_logs")
    user: Mapped[User] = relationship(back_populates="audit_logs")
