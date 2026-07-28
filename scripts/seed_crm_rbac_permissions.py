#!/usr/bin/env python3
"""Seed CRM permissions + role_permissions for all agencies."""
from __future__ import annotations

import sys
from pathlib import Path
from uuid import UUID

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select
from database import SessionLocal
from models.crm.tenancy import Agency, Permission, Role, RolePermission

MODULES = [
    "analytics", "leads", "customers", "itinerary", "vendors",
    "finance", "staff_control", "workspace_settings",
]
ACTIONS = ("view", "create", "edit", "delete")

ROLE_PRESETS: dict[str, dict[str, set[str]]] = {
    "Agency Admin": {m: set(ACTIONS) for m in MODULES},
    "Sales Agent": {
        "analytics": {"view"},
        "leads": {"view", "create", "edit"},
        "customers": {"view", "create", "edit"},
        "itinerary": {"view", "create", "edit"},
        "workspace_settings": {"view"},
    },
    "Operations": {
        "analytics": {"view"},
        "customers": {"view", "create", "edit"},
        "itinerary": {"view", "create", "edit"},
        "vendors": {"view", "create", "edit"},
        "workspace_settings": {"view"},
    },
    "Finance": {
        "analytics": {"view"},
        "vendors": {"view"},
        "finance": {"view", "create", "edit"},
        "workspace_settings": {"view"},
    },
    "Operational Manager": {
        "analytics": {"view"},
        "leads": {"view", "create", "edit"},
        "customers": {"view", "create", "edit"},
        "itinerary": {"view", "create", "edit"},
        "vendors": {"view", "create", "edit"},
        "finance": {"view"},
        "staff_control": {"view"},
        "workspace_settings": {"view"},
    },
    "Vendor": {"vendors": {"view"}},
    "Customer": {},
}

def _key(module: str, action: str) -> str:
    return f"{module}.{action}"

def main() -> None:
    with SessionLocal() as db:
        catalog: dict[str, Permission] = {}
        for module in MODULES:
            for action in ACTIONS:
                row = db.scalar(
                    select(Permission).where(Permission.module == module, Permission.name == action)
                )
                if row is None:
                    row = Permission(name=action, module=module)
                    db.add(row)
                    db.flush()
                catalog[_key(module, action)] = row

        agencies = db.scalars(select(Agency).where(Agency.is_deleted.is_(False))).all()
        for agency in agencies:
            for role_name, preset in ROLE_PRESETS.items():
                role = db.scalar(
                    select(Role).where(Role.agency_id == agency.id, Role.name == role_name)
                )
                if role is None:
                    role = Role(name=role_name, agency_id=agency.id)
                    db.add(role)
                    db.flush()
                existing = {
                    rp.permission_id
                    for rp in db.query(RolePermission).filter(RolePermission.role_id == role.id)
                }
                desired: set[UUID] = set()
                for module, actions in preset.items():
                    for action in actions:
                        perm = catalog.get(_key(module, action))
                        if perm:
                            desired.add(perm.id)
                for pid in desired - existing:
                    db.add(RolePermission(role_id=role.id, permission_id=pid))
                for pid in existing - desired:
                    db.query(RolePermission).filter(
                        RolePermission.role_id == role.id,
                        RolePermission.permission_id == pid,
                    ).delete()
        db.commit()
    print("seed_crm_rbac_permissions complete.")

if __name__ == "__main__":
    main()
