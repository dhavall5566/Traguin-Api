from uuid import UUID

from pydantic import BaseModel, Field

from schemas.crm.common import CrmCreatedAtRead, CrmTimestampRead


class RoleBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=128)


class RoleCreate(RoleBase):
    pass


class RoleUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=128)


class RoleRead(CrmTimestampRead, RoleBase):
    agency_id: UUID | None


class PermissionBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=64)
    module: str = Field(..., min_length=1, max_length=64)


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=64)
    module: str | None = Field(default=None, min_length=1, max_length=64)


class PermissionRead(CrmCreatedAtRead, PermissionBase):
    pass


class RolePermissionCreate(BaseModel):
    permission_id: UUID


class RolePermissionRead(BaseModel):
    role_id: UUID
    permission_id: UUID


class UserRoleCreate(BaseModel):
    role_id: UUID


class UserRoleRead(BaseModel):
    user_id: UUID
    role_id: UUID
