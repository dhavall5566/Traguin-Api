
"""Org unit hierarchy helpers for CRM data scoping."""
from __future__ import annotations
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.crm.org_units import OrgUnit

def collect_descendant_org_unit_ids(db: Session, agency_id: UUID, root_id: UUID) -> list[UUID]:
    units = db.scalars(
        select(OrgUnit).where(OrgUnit.agency_id == agency_id, OrgUnit.is_deleted.is_(False))
    ).all()
    children: dict[UUID | None, list[UUID]] = {}
    for unit in units:
        children.setdefault(unit.parent_id, []).append(unit.id)
    out: list[UUID] = []
    stack = [root_id]
    seen: set[UUID] = set()
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        out.append(cur)
        stack.extend(children.get(cur, []))
    return out

def lead_org_unit_filter_ids(db: Session, agency_id: UUID, org_unit_id: UUID) -> list[UUID]:
    return collect_descendant_org_unit_ids(db, agency_id, org_unit_id)

def default_org_unit_for_user(db: Session, user) -> UUID | None:
    if getattr(user, "org_unit_id", None):
        return user.org_unit_id
    branch = db.scalar(
        select(OrgUnit.id).where(
            OrgUnit.agency_id == user.agency_id,
            OrgUnit.unit_type == "BRANCH",
            OrgUnit.is_deleted.is_(False),
        ).limit(1)
    )
    return branch
