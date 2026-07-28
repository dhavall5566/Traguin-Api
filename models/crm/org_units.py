from __future__ import annotations

import uuid
from typing import Optional

from sqlalchemy import Boolean, ForeignKey, Index, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, TimestampMixin, UUIDPrimaryKeyMixin

class OrgUnit(CrmBase, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "org_units"
    __table_args__ = (
        Index("ix_org_units_agency_id", "agency_id"),
        Index("ix_org_units_parent_id", "parent_id"),
    )

    agency_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("agencies.id", ondelete="CASCADE"), nullable=False
    )
    parent_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("org_units.id", ondelete="SET NULL"), nullable=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    unit_type: Mapped[str] = mapped_column(String(32), nullable=False, default="BRANCH")
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    parent: Mapped[Optional["OrgUnit"]] = relationship(
        remote_side="OrgUnit.id", back_populates="children", foreign_keys=[parent_id]
    )
    children: Mapped[list["OrgUnit"]] = relationship(back_populates="parent", foreign_keys=[parent_id])
