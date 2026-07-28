"""Server-side CRM RBAC permission checks."""
from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crm.tenancy import Permission, Role, RolePermission, UserRole

ADMIN_ROLE_NAMES = frozenset({"Agency Admin"})

def get_user_role_names(db: Session, user_id: UUID, agency_id: UUID | None) -> list[str]:
    rows = (
        db.query(Role.name)
        .join(UserRole, UserRole.role_id == Role.id)
        .filter(UserRole.user_id == user_id, Role.agency_id == agency_id)
        .all()
    )
    return [r[0] for r in rows]

def user_is_agency_admin(db: Session, user_id: UUID, agency_id: UUID | None) -> bool:
    return any(name in ADMIN_ROLE_NAMES for name in get_user_role_names(db, user_id, agency_id))

def user_has_permission(
    db: Session, user_id: UUID, agency_id: UUID | None, module: str, action: str
) -> bool:
    if agency_id is None:
        return False
    if user_is_agency_admin(db, user_id, agency_id):
        return True
    stmt = (
        select(Permission.id)
        .join(RolePermission, RolePermission.permission_id == Permission.id)
        .join(Role, Role.id == RolePermission.role_id)
        .join(UserRole, UserRole.role_id == Role.id)
        .where(
            UserRole.user_id == user_id,
            Role.agency_id == agency_id,
            Permission.module == module,
            Permission.name == action,
        )
        .limit(1)
    )
    return db.scalar(stmt) is not None

def list_user_permissions(db: Session, user_id: UUID, agency_id: UUID | None) -> list[dict[str, str]]:
    if agency_id is None:
        return []
    if user_is_agency_admin(db, user_id, agency_id):
        modules = [
            "analytics", "leads", "customers", "itinerary", "vendors",
            "finance", "staff_control", "workspace_settings",
        ]
        return [{"module": m, "action": a} for m in modules for a in ("view", "create", "edit", "delete")]
    rows = (
        db.query(Permission.module, Permission.name)
        .join(RolePermission, RolePermission.permission_id == Permission.id)
        .join(Role, Role.id == RolePermission.role_id)
        .join(UserRole, UserRole.role_id == Role.id)
        .filter(UserRole.user_id == user_id, Role.agency_id == agency_id)
        .distinct()
        .all()
    )
    return [{"module": m, "action": a} for m, a in rows]
