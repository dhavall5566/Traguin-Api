"""CRM route-level permission enforcement."""
from __future__ import annotations

from uuid import UUID

from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_crm_user
from models.crm.tenancy import User
from services.crm_permissions import user_has_permission

METHOD_ACTION = {
    "GET": "view",
    "HEAD": "view",
    "POST": "create",
    "PUT": "edit",
    "PATCH": "edit",
    "DELETE": "delete",
}

RESOURCE_MODULE = {
    "leads": "leads",
    "customers": "customers",
    "bookings": "customers",
    "itineraries": "itinerary",
    "packages": "itinerary",
    "vendors": "vendors",
    "finance": "finance",
    "users": "staff_control",
    "rbac": "staff_control",
    "audit-logs": "staff_control",
    "settings": "workspace_settings",
    "agencies": "workspace_settings",
    "org-units": "workspace_settings",
    "approvals": "finance",
    "reports": "analytics",
    "sla-settings": "workspace_settings",
}

SKIP_PREFIXES = ("/api/crm/auth",)

def _resolve_module(path: str) -> str | None:
    if any(path.startswith(p) for p in SKIP_PREFIXES):
        return None
    parts = path.strip("/").split("/")
    if len(parts) < 3 or parts[0] != "api" or parts[1] != "crm":
        return None
    return RESOURCE_MODULE.get(parts[2])

def enforce_crm_permissions(
    request: Request,
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
) -> User:
    module = _resolve_module(request.url.path)
    if module is None:
        return current_user
    action = METHOD_ACTION.get(request.method.upper(), "view")
    agency_id: UUID | None = current_user.agency_id
    if not user_has_permission(db, current_user.id, agency_id, module, action):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Missing permission: {module}.{action}",
        )
    return current_user
