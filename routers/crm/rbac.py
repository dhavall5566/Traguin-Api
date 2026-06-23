from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope
from dependencies.pagination import get_pagination
from models.crm.tenancy import Permission, Role, RolePermission, UserRole
from schemas.crm.rbac import (
    PermissionCreate,
    PermissionRead,
    PermissionUpdate,
    RoleCreate,
    RolePermissionCreate,
    RolePermissionRead,
    RoleRead,
    RoleUpdate,
    UserRoleCreate,
    UserRoleRead,
)
from schemas.pagination import PaginatedResponse
from services.crm_scope import (
    get_role_for_agency,
    require_permission,
    require_role_for_agency,
    require_user_for_agency,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


# --- Roles (agency-scoped) ---


@router.get("/roles", response_model=PaginatedResponse[RoleRead])
def list_roles(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Role).filter(Role.agency_id == agency_id).order_by(Role.name)
    return paginate(query, limit, offset, transform=RoleRead.model_validate)


@router.get("/roles/{role_id}", response_model=RoleRead)
def get_role(
    role_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    role = get_role_for_agency(db, role_id, agency_id)
    if role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found.")
    return role


@router.post("/roles", response_model=RoleRead, status_code=status.HTTP_201_CREATED)
def create_role(
    payload: RoleCreate,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    role = Role(**payload.model_dump(), agency_id=agency_id)
    db.add(role)
    commit_or_raise(db, unique_fields=("name",))
    db.refresh(role)
    return role


@router.patch("/roles/{role_id}", response_model=RoleRead)
def update_role(
    role_id: UUID,
    payload: RoleUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    role = get_role_for_agency(db, role_id, agency_id)
    if role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found.")
    apply_partial_update(role, payload.model_dump(exclude_unset=True))
    commit_or_raise(db, unique_fields=("name",))
    db.refresh(role)
    return role


@router.delete("/roles/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(
    role_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    role = get_role_for_agency(db, role_id, agency_id)
    if role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found.")
    db.delete(role)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- Permissions (global catalog) ---


@router.get("/permissions", response_model=PaginatedResponse[PermissionRead])
def list_permissions(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Permission).order_by(Permission.module, Permission.name)
    return paginate(query, limit, offset, transform=PermissionRead.model_validate)


@router.get("/permissions/{permission_id}", response_model=PermissionRead)
def get_permission(permission_id: UUID, db: Session = Depends(get_db)):
    return require_permission(db, permission_id)


@router.post("/permissions", response_model=PermissionRead, status_code=status.HTTP_201_CREATED)
def create_permission(payload: PermissionCreate, db: Session = Depends(get_db)):
    permission = Permission(**payload.model_dump())
    db.add(permission)
    commit_or_raise(db, unique_fields=("name",))
    db.refresh(permission)
    return permission


@router.patch("/permissions/{permission_id}", response_model=PermissionRead)
def update_permission(
    permission_id: UUID,
    payload: PermissionUpdate,
    db: Session = Depends(get_db),
):
    permission = require_permission(db, permission_id)
    apply_partial_update(permission, payload.model_dump(exclude_unset=True))
    commit_or_raise(db, unique_fields=("name",))
    db.refresh(permission)
    return permission


@router.delete("/permissions/{permission_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_permission(permission_id: UUID, db: Session = Depends(get_db)):
    permission = require_permission(db, permission_id)
    db.delete(permission)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- RolePermission junction ---


@router.get("/roles/{role_id}/permissions", response_model=list[RolePermissionRead])
def list_role_permissions(
    role_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    require_role_for_agency(db, role_id, agency_id)
    rows = db.query(RolePermission).filter(RolePermission.role_id == role_id).all()
    return [RolePermissionRead(role_id=r.role_id, permission_id=r.permission_id) for r in rows]


@router.post("/roles/{role_id}/permissions", response_model=RolePermissionRead, status_code=status.HTTP_201_CREATED)
def assign_role_permission(
    role_id: UUID,
    payload: RolePermissionCreate,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    require_role_for_agency(db, role_id, agency_id)
    require_permission(db, payload.permission_id)
    existing = db.get(RolePermission, {"role_id": role_id, "permission_id": payload.permission_id})
    if existing is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Permission already assigned to role.")
    link = RolePermission(role_id=role_id, permission_id=payload.permission_id)
    db.add(link)
    commit_or_raise(db)
    return RolePermissionRead(role_id=role_id, permission_id=payload.permission_id)


@router.delete("/roles/{role_id}/permissions/{permission_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_role_permission(
    role_id: UUID,
    permission_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    require_role_for_agency(db, role_id, agency_id)
    link = db.get(RolePermission, {"role_id": role_id, "permission_id": permission_id})
    if link is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role permission not found.")
    db.delete(link)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- UserRole junction ---


@router.get("/users/{user_id}/roles", response_model=list[UserRoleRead])
def list_user_roles(
    user_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    require_user_for_agency(db, user_id, agency_id)
    rows = db.query(UserRole).filter(UserRole.user_id == user_id).all()
    return [UserRoleRead(user_id=r.user_id, role_id=r.role_id) for r in rows]


@router.post("/users/{user_id}/roles", response_model=UserRoleRead, status_code=status.HTTP_201_CREATED)
def assign_user_role(
    user_id: UUID,
    payload: UserRoleCreate,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    require_user_for_agency(db, user_id, agency_id)
    require_role_for_agency(db, payload.role_id, agency_id)
    existing = db.get(UserRole, {"user_id": user_id, "role_id": payload.role_id})
    if existing is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Role already assigned to user.")
    link = UserRole(user_id=user_id, role_id=payload.role_id)
    db.add(link)
    commit_or_raise(db)
    return UserRoleRead(user_id=user_id, role_id=payload.role_id)


@router.delete("/users/{user_id}/roles/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_user_role(
    user_id: UUID,
    role_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    require_user_for_agency(db, user_id, agency_id)
    require_role_for_agency(db, role_id, agency_id)
    link = db.get(UserRole, {"user_id": user_id, "role_id": role_id})
    if link is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User role not found.")
    db.delete(link)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
