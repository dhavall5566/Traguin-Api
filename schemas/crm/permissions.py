from pydantic import BaseModel

class PermissionEntry(BaseModel):
    module: str
    action: str

class UserPermissionsRead(BaseModel):
    is_admin: bool
    permissions: list[PermissionEntry]

class PermissionsMatrixUpdate(BaseModel):
    permissions: dict[str, dict[str, bool]]
