"""Resolve CRM users for assignment escalation notifications."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from models.crm.tenancy import Role, User, UserRole

ADMIN_ROLE_NAME = "Agency Admin"
SALES_AGENT_ROLE_NAME = "Sales Agent"
OPERATIONS_ROLE_NAME = "Operations"
FINANCE_ROLE_NAME = "Finance"

OPS_HEAD_NAME_HINTS = ("nisha",)
CEO_NAME_HINTS = ("ceo",)


def _active_agency_users(db: Session, agency_id: UUID) -> list[User]:
    return list(
        db.scalars(
            select(User)
            .where(
                User.agency_id == agency_id,
                User.is_deleted.is_(False),
            )
            .order_by(User.name)
        ).all()
    )


def users_with_role_name(db: Session, *, agency_id: UUID, role_name: str) -> list[User]:
    return list(
        db.scalars(
            select(User)
            .join(UserRole, UserRole.user_id == User.id)
            .join(Role, Role.id == UserRole.role_id)
            .where(
                User.agency_id == agency_id,
                User.is_deleted.is_(False),
                Role.agency_id == agency_id,
                Role.name == role_name,
            )
            .order_by(User.name)
        ).all()
    )


def users_matching_name_hints(
    db: Session,
    *,
    agency_id: UUID,
    hints: tuple[str, ...],
) -> list[User]:
    if not hints:
        return []
    clauses = [User.name.ilike(f"%{hint}%") for hint in hints]
    return list(
        db.scalars(
            select(User).where(
                User.agency_id == agency_id,
                User.is_deleted.is_(False),
                or_(*clauses),
            )
        ).all()
    )


def resolve_admin_users(db: Session, agency_id: UUID) -> list[User]:
    admins = users_with_role_name(db, agency_id=agency_id, role_name=ADMIN_ROLE_NAME)
    if admins:
        return admins
    return _active_agency_users(db, agency_id)[:1]


def resolve_ops_head_users(db: Session, agency_id: UUID) -> list[User]:
    by_name = users_matching_name_hints(db, agency_id=agency_id, hints=OPS_HEAD_NAME_HINTS)
    if by_name:
        return by_name
    ops = users_with_role_name(db, agency_id=agency_id, role_name=OPERATIONS_ROLE_NAME)
    return ops[:1]


def resolve_ceo_users(db: Session, agency_id: UUID) -> list[User]:
    by_name = users_matching_name_hints(db, agency_id=agency_id, hints=CEO_NAME_HINTS)
    if by_name:
        return by_name
    return resolve_admin_users(db, agency_id)[:1]


def resolve_account_users(db: Session, agency_id: UUID) -> list[User]:
    finance = users_with_role_name(db, agency_id=agency_id, role_name=FINANCE_ROLE_NAME)
    if finance:
        return finance
    return resolve_admin_users(db, agency_id)[:1]


def resolve_rm_user(db: Session, lead) -> User | None:
    assignee_id = getattr(lead, "assigned_to_id", None)
    if assignee_id is None:
        return None
    user = db.get(User, assignee_id)
    if user is None or user.is_deleted:
        return None
    return user


def dedupe_users(users: list[User]) -> list[User]:
    seen: set[UUID] = set()
    out: list[User] = []
    for user in users:
        if user.id in seen:
            continue
        seen.add(user.id)
        out.append(user)
    return out


def find_alternate_sales_agent(
    db: Session,
    *,
    agency_id: UUID,
    exclude_user_id: UUID | None,
) -> User | None:
    agents = users_with_role_name(db, agency_id=agency_id, role_name=SALES_AGENT_ROLE_NAME)
    for agent in agents:
        if exclude_user_id is not None and agent.id == exclude_user_id:
            continue
        return agent
    for user in _active_agency_users(db, agency_id):
        if exclude_user_id is not None and user.id == exclude_user_id:
            continue
        return user
    return None
