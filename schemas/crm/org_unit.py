from uuid import UUID

from pydantic import BaseModel, Field

from schemas.crm.common import CrmTimestampRead

class OrgUnitBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    unit_type: str = Field(default="BRANCH", pattern="^(BRANCH|DEPARTMENT|TEAM)$")
    parent_id: UUID | None = None

class OrgUnitCreate(OrgUnitBase):
    pass

class OrgUnitUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    unit_type: str | None = Field(default=None, pattern="^(BRANCH|DEPARTMENT|TEAM)$")
    parent_id: UUID | None = None

class OrgUnitRead(CrmTimestampRead, OrgUnitBase):
    agency_id: UUID
    is_deleted: bool

class OrgUnitTreeNode(OrgUnitRead):
    children: list["OrgUnitTreeNode"] = []

OrgUnitTreeNode.model_rebuild()
