from uuid import UUID

from pydantic import BaseModel, Field

from schemas.crm.common import CrmCreatedAtRead


class AuditLogRead(CrmCreatedAtRead):
    agency_id: UUID
    user_id: UUID
    action: str
    entity_type: str
    entity_id: str | None
    details: str | None


class AuditLogFilter(BaseModel):
    user_id: UUID | None = None
    entity_type: str | None = Field(default=None, max_length=64)
    action: str | None = Field(default=None, max_length=32)
