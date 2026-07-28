from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.crm.common import CrmCreatedAtRead

APPROVAL_TYPES = frozenset({"DISCOUNT", "VENDOR_PAYOUT", "REFUND"})

class ApprovalCreate(BaseModel):
    request_type: str = Field(..., pattern="^(DISCOUNT|VENDOR_PAYOUT|REFUND)$")
    entity_type: str = Field(..., min_length=1, max_length=64)
    entity_id: UUID
    title: str = Field(..., min_length=1, max_length=512)
    payload: dict[str, Any] = Field(default_factory=dict)

class ApprovalRead(CrmCreatedAtRead):
    agency_id: UUID
    request_type: str
    entity_type: str
    entity_id: UUID
    title: str
    payload: dict[str, Any]
    status: str
    requested_by_id: UUID
    reviewed_by_id: UUID | None
    review_note: str | None
    reviewed_at: datetime | None

class ApprovalReview(BaseModel):
    review_note: str | None = None
