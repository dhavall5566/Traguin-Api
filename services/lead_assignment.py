"""Lead assignment accept/reject workflow for CRM sales handoff."""

from __future__ import annotations

from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crm.leads import Lead, LeadActivity
from models.crm.tenancy import User
from schemas.crm.lead import LeadAssignmentPendingRead
from services.lead_assignee import user_is_active_staff

ASSIGNMENT_PENDING = "PENDING"
ASSIGNMENT_ACCEPTED = "ACCEPTED"
ASSIGNMENT_REJECTED = "REJECTED"


def _lead_label(lead: Lead) -> str:
    name = f"{lead.first_name} {lead.last_name}".strip()
    return f'"{lead.title}" ({name})'


def apply_assignment_on_assign(
    db: Session,
    lead: Lead,
    *,
    assignee_id: UUID | None,
    actor_id: UUID,
    agency_id: UUID,
) -> bool:
    """
    Update assignment fields when assignee changes.
    Self-assignments are auto-accepted; assignments to others require acceptance.
    """
    if assignee_id is not None and not user_is_active_staff(db, assignee_id, agency_id):
        return False

    if assignee_id is None:
        changed = (
            lead.assigned_to_id is not None
            or lead.assignment_status is not None
            or lead.assigned_by_id is not None
        )
        lead.assigned_to_id = None
        lead.assignment_status = None
        lead.assigned_by_id = None
        return changed

    next_status = ASSIGNMENT_ACCEPTED if assignee_id == actor_id else ASSIGNMENT_PENDING
    changed = lead.assigned_to_id != assignee_id or lead.assignment_status != next_status
    lead.assigned_to_id = assignee_id
    lead.assigned_by_id = actor_id
    lead.assignment_status = next_status
    return changed


def list_pending_assignments_for_user(
    db: Session,
    *,
    agency_id: UUID,
    user_id: UUID,
) -> list[LeadAssignmentPendingRead]:
    rows = db.scalars(
        select(Lead)
        .where(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.assigned_to_id == user_id,
            Lead.assignment_status == ASSIGNMENT_PENDING,
        )
        .order_by(Lead.updated_at.desc())
        .limit(50)
    ).all()

    results: list[LeadAssignmentPendingRead] = []
    for lead in rows:
        assigner_name = None
        if lead.assigned_by_id:
            assigner = db.get(User, lead.assigned_by_id)
            assigner_name = assigner.name if assigner else None
        results.append(
            LeadAssignmentPendingRead(
                id=lead.id,
                lead_code=lead.lead_code,
                title=lead.title,
                first_name=lead.first_name,
                last_name=lead.last_name,
                source=lead.source,
                phone=lead.phone,
                assigned_by_id=lead.assigned_by_id,
                assigned_by_name=assigner_name,
                updated_at=lead.updated_at,
            )
        )
    return results


def accept_lead_assignment(
    db: Session,
    lead: Lead,
    *,
    user_id: UUID,
) -> Lead:
    if lead.assigned_to_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not the assignee for this lead.")
    if lead.assignment_status != ASSIGNMENT_PENDING:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This assignment is not awaiting acceptance.",
        )

    lead.assignment_status = ASSIGNMENT_ACCEPTED
    db.add(
        LeadActivity(
            lead_id=lead.id,
            type="NOTE",
            description=f"Accepted lead assignment for {_lead_label(lead)}",
            created_by_id=user_id,
        )
    )
    return lead


def reject_lead_assignment(
    db: Session,
    lead: Lead,
    *,
    user_id: UUID,
) -> tuple[Lead, UUID | None]:
    if lead.assigned_to_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not the assignee for this lead.")
    if lead.assignment_status != ASSIGNMENT_PENDING:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This assignment is not awaiting acceptance.",
        )

    assigner_id = lead.assigned_by_id
    db.add(
        LeadActivity(
            lead_id=lead.id,
            type="NOTE",
            description=f"Rejected lead assignment for {_lead_label(lead)}",
            created_by_id=user_id,
        )
    )
    lead.assigned_to_id = None
    lead.assignment_status = None
    lead.assigned_by_id = None
    return lead, assigner_id


def assignment_requires_acceptance(lead: Lead) -> bool:
    return lead.assignment_status == ASSIGNMENT_PENDING and lead.assigned_to_id is not None
