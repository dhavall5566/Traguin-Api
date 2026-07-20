from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Index, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.crm.base import CrmBase, CreatedAtMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from models.crm.customers import Customer
    from models.crm.tenancy import User


class CustomerFlag(CrmBase, UUIDPrimaryKeyMixin, CreatedAtMixin):
    __tablename__ = "customer_flags"
    __table_args__ = (Index("ix_customer_flags_customer_id", "customer_id"),)

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("customers.id", ondelete="CASCADE"), nullable=False
    )
    remark: Mapped[str] = mapped_column(Text, nullable=False)
    created_by_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    customer: Mapped[Customer] = relationship(back_populates="flags")
    created_by: Mapped[User] = relationship(back_populates="created_customer_flags")
