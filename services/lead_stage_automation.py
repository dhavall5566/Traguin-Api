"""Auto-advance lead pipeline stage from assignment signals and activity history."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from models.crm.leads import Lead, LeadActivity
from services.lead_assignment import ASSIGNMENT_ACCEPTED
from services.lead_status import apply_lead_status_transition
from utils.lead_pipeline import (
    LEGACY_STATUS_MAP,
    LEAD_PIPELINE_STATUSES,
    TERMINAL_PIPELINE_STAGES,
    is_pipeline_stage_before,
    max_pipeline_stage,
    pipeline_stage_index,
    pipeline_status_label,
    resolve_pipeline_stage,
)

_CONTACT_ACTIVITY_TYPES = frozenset({"PHONE", "EMAIL", "MEET"})


def _stage_from_stage_change_description(description: str | None) -> str | None:
    if not description:
        return None
    upper = description.upper()
    best: str | None = None
    best_index = -1
    for stage in LEAD_PIPELINE_STATUSES:
        if stage in upper:
            index = pipeline_stage_index(stage)
            if index > best_index:
                best_index = index
                best = stage
    for legacy, modern in LEGACY_STATUS_MAP.items():
        if legacy in upper:
            index = pipeline_stage_index(modern)
            if index > best_index:
                best_index = index
                best = modern
    return best


def target_stage_for_activity_type(activity_type: str | None) -> str | None:
    normalized = (activity_type or "").strip().upper()
    if normalized in _CONTACT_ACTIVITY_TYPES:
        return "CONTACTED"
    if normalized == "ENTERED_PROPOSAL_SENT":
        return "ITINERARY_SENT"
    return None


def target_stage_for_assignment(lead: Lead) -> str | None:
    if lead.assigned_to_id is None:
        return None
    if (lead.assignment_status or "").upper() == ASSIGNMENT_ACCEPTED:
        return "ACCEPTED"
    return "ASSIGNED"


def infer_pipeline_stage_from_signals(lead: Lead) -> str:
    """Infer the furthest pipeline stage supported by assignment + activity history."""
    candidates: list[str] = ["NEW"]

    assignment_target = target_stage_for_assignment(lead)
    if assignment_target:
        candidates.append(assignment_target)

    if lead.proposal_sent_at is not None:
        candidates.append("ITINERARY_SENT")

    for activity in lead.activities:
        activity_target = target_stage_for_activity_type(activity.type)
        if activity_target:
            candidates.append(activity_target)
        if (activity.type or "").upper() == "STAGE_CHANGE":
            stage_target = _stage_from_stage_change_description(activity.description)
            if stage_target:
                candidates.append(stage_target)

    for followup in lead.followups:
        if (followup.status or "").upper() == "COMPLETED":
            candidates.append("CONTACTED")
            break

    return max_pipeline_stage(*candidates)


def _resolve_actor_id(lead: Lead, actor_id: UUID | None) -> UUID | None:
    if actor_id is not None:
        return actor_id
    if lead.assigned_to_id is not None:
        return lead.assigned_to_id
    if lead.assigned_by_id is not None:
        return lead.assigned_by_id
    return None


def advance_lead_stage_if_behind(
    db: Session,
    lead: Lead,
    target_stage: str,
    *,
    actor_id: UUID | None,
    reason: str,
) -> bool:
    current = resolve_pipeline_stage(lead.status)
    target = resolve_pipeline_stage(target_stage)

    if current in TERMINAL_PIPELINE_STAGES:
        return False
    if not is_pipeline_stage_before(current, target):
        return False

    resolved_actor = _resolve_actor_id(lead, actor_id)
    if resolved_actor is None:
        return False

    previous = lead.status
    lead.status = target
    apply_lead_status_transition(
        db,
        lead,
        previous,
        created_by_id=resolved_actor,
    )
    db.add(
        LeadActivity(
            lead_id=lead.id,
            type="STAGE_CHANGE",
            description=(
                f"Stage auto-advanced from {pipeline_status_label(previous)} "
                f"to {pipeline_status_label(target)} ({reason})"
            ),
            created_by_id=resolved_actor,
        )
    )
    return True


def maybe_sync_lead_stage_from_signals(
    db: Session,
    lead: Lead,
    *,
    actor_id: UUID | None,
) -> bool:
    """Move lead status forward when activity/assignment history warrants it."""
    current = resolve_pipeline_stage(lead.status)
    if current in TERMINAL_PIPELINE_STAGES:
        return False

    inferred = infer_pipeline_stage_from_signals(lead)
    if not is_pipeline_stage_before(current, inferred):
        return False

    return advance_lead_stage_if_behind(
        db,
        lead,
        inferred,
        actor_id=actor_id,
        reason="based on lead activity",
    )
