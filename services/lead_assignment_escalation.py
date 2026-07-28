"""RM assignment accept timers and escalation (working hours, IST)."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from config import settings
from models.crm.leads import Lead, LeadActivity, LeadNote
from models.crm.tenancy import User
from services.crm_escalation_targets import (
    resolve_admin_users,
    resolve_manager_or_ops_users,
    resolve_rm_user,
)
from services.lead_assignment import (
    ASSIGNMENT_ACCEPTED,
    ASSIGNMENT_PENDING,
    apply_assignment_on_assign,
)
from services.whatsapp_notifications import CrmAlertPayload, build_alert_fields, send_whatsapp_template
from utils.working_hours import (
    ACCEPT_WINDOW_WORKING_MINUTES,
    working_minutes_between,
)

logger = logging.getLogger(__name__)

POST_ACCEPT_INACTIVITY_MINUTES = 30
MAX_RM_REMINDERS = 5

# (working_minutes_threshold, escalation_level, event_title_suffix)
PENDING_ESCALATION_TIERS: tuple[tuple[int, int, str], ...] = (
    (15, 1, "RM reminder 1/5"),
    (30, 2, "RM reminder 2/5"),
    (45, 3, "RM reminder 3/5"),
    (60, 4, "RM reminder 4/5"),
    (75, 5, "RM reminder 5/5"),
)
PENDING_UNASSIGN_AFTER_MINUTES = 90

_EARLY_PIPELINE_STATUSES = frozenset({"NEW", "ASSIGNED", "ACCEPTED"})


@dataclass
class EscalationRunCounts:
    pending_escalations: int = 0
    accept_inactivity_reminders: int = 0
    reassignments: int = 0
    unassignments: int = 0


def _lead_subject(lead: Lead) -> str:
    name = f"{lead.first_name} {lead.last_name}".strip()
    code = lead.lead_code or str(lead.id)[:8]
    return f"{code} — {name}"


def _system_actor_id(db: Session, lead: Lead) -> UUID:
    if settings.traguin_system_user_id is not None:
        return settings.traguin_system_user_id
    if lead.assigned_by_id is not None:
        return lead.assigned_by_id
    admins = resolve_admin_users(db, lead.agency_id)
    if admins:
        return admins[0].id
    if lead.assigned_to_id is not None:
        return lead.assigned_to_id
    raise ValueError("No system actor available for assignment escalation")


def _notify_users(
    db: Session,
    *,
    agency_id: UUID,
    users: list[User],
    payload: CrmAlertPayload,
    lead: Lead | None = None,
    template_id: str | None = None,
    template_variables: dict[str, str] | None = None,
    elapsed_time: str | None = None,
    escalation_level: str | None = None,
    escalation_message: str | None = None,
) -> int:
    from services.email_notifications import _send_email_to_user
    from services.notification_templates.context import build_lead_context
    from services.notification_templates.delivery import (
        send_templated_email,
        send_templated_whatsapp,
        whatsapp_fields_for_template,
    )
    from services.notification_templates.renderer import render_email, render_plain

    if not users:
        return 0

    sent = 0
    if template_id and lead is not None:
        variables = build_lead_context(
            db,
            lead,
            elapsed_time=elapsed_time,
            escalation_level=escalation_level,
            escalation_message=escalation_message,
        )
        if template_variables:
            variables.update(template_variables)
        subject, _html_body = render_email(template_id, variables)
        body = render_plain(template_id, variables)
        wa_fields = whatsapp_fields_for_template(template_id, variables)
        for user in users:
            if user.phone and send_whatsapp_template(
                user.phone,
                wa_fields,
                db=db,
                agency_id=agency_id,
                notification_template_key=template_id,
            ):
                sent += 1
        for user in users:
            if (user.email or "").strip() and send_templated_email(
                db,
                agency_id=agency_id,
                to_email=user.email or "",
                template_id=template_id,
                variables=variables,
            ):
                sent += 1
        return sent

    fields = build_alert_fields(
        payload.event_title,
        payload.subject,
        payload.detail,
        payload.extra,
        payload.link,
    )
    subject = f"[TRAGUIN CRM] {payload.event_title}"
    body = "\n".join(
        [
            payload.event_title,
            "",
            payload.subject,
            payload.detail,
            payload.extra,
            "",
            payload.link or "Open TRAGUIN CRM",
        ]
    )
    for user in users:
        if user.phone:
            if send_whatsapp_template(
                user.phone,
                fields,
                db=db,
                agency_id=agency_id,
            ):
                sent += 1
    for user in users:
        if _send_email_to_user(
            db,
            agency_id=agency_id,
            to_user_id=user.id,
            subject=subject,
            body=body,
        ):
            sent += 1
    return sent


def _log_escalation_activity(
    db: Session,
    lead: Lead,
    *,
    description: str,
    actor_id: UUID,
) -> None:
    db.add(
        LeadActivity(
            lead_id=lead.id,
            type="ASSIGNMENT_ESCALATION",
            description=description,
            created_by_id=actor_id,
        )
    )


def _targets_for_tier(db: Session, lead: Lead, level: int) -> list[User]:
    assignee = resolve_rm_user(db, lead)
    if level in range(1, MAX_RM_REMINDERS + 1):
        return [assignee] if assignee is not None else []
    return []


def _notify_assigner_lead_unassigned_no_accept(
    db: Session,
    lead: Lead,
    *,
    previous_rm: User | None,
    assigner_id: UUID | None,
) -> None:
    if assigner_id is None:
        return
    assigner = db.get(User, assigner_id)
    if assigner is None or assigner.is_deleted:
        return

    rm_name = previous_rm.name if previous_rm is not None else "Assigned RM"
    subject = _lead_subject(lead)
    escalation_message = (
        f"Lead {lead.lead_code or lead.id} was unassigned because {rm_name} did not accept "
        f"the assignment after {MAX_RM_REMINDERS} reminders."
    )
    _notify_users(
        db,
        agency_id=lead.agency_id,
        users=[assigner],
        payload=CrmAlertPayload(
            agency_id=lead.agency_id,
            event_title="Lead unassigned — RM did not accept",
            subject=subject,
            detail=escalation_message,
            extra=f"Previous RM: {rm_name} · Status: {lead.status}",
        ),
        lead=lead,
        template_id="team_assigner_lead_unassigned",
        template_variables={
            "RM_Name": rm_name,
            "Escalation_Message": escalation_message,
            "Attempt_Count": str(MAX_RM_REMINDERS),
        },
        escalation_level="Unassigned",
        escalation_message=escalation_message,
    )


def _unassign_lead_for_rm_inactivity(
    db: Session,
    lead: Lead,
    *,
    previous_rm: User | None,
    reason: str,
    actor_id: UUID,
    notify_assigner_only: bool = False,
) -> None:
    rm_name = previous_rm.name if previous_rm is not None else "Assigned RM"
    assigner_id = lead.assigned_by_id

    apply_assignment_on_assign(
        db,
        lead,
        assignee_id=None,
        actor_id=actor_id,
        agency_id=lead.agency_id,
    )
    _log_escalation_activity(
        db,
        lead,
        description=(
            f"Lead unassigned after {MAX_RM_REMINDERS} reminders: {rm_name} had no activity "
            f"({reason})"
        ),
        actor_id=actor_id,
    )

    if notify_assigner_only:
        _notify_assigner_lead_unassigned_no_accept(
            db,
            lead,
            previous_rm=previous_rm,
            assigner_id=assigner_id,
        )
        return

    subject = _lead_subject(lead)
    managers = resolve_manager_or_ops_users(db, lead.agency_id, previous_rm)
    escalation_message = (
        f"Lead {lead.lead_code or lead.id} is now unassigned because {rm_name} performed no "
        f"activity after {MAX_RM_REMINDERS} reminders ({reason})."
    )
    _notify_users(
        db,
        agency_id=lead.agency_id,
        users=managers,
        payload=CrmAlertPayload(
            agency_id=lead.agency_id,
            event_title="Lead unassigned — RM inactivity",
            subject=subject,
            detail=escalation_message,
            extra=f"Previous RM: {rm_name} · Status: {lead.status}",
        ),
        lead=lead,
        template_id="team_manager_lead_unassigned",
        template_variables={
            "RM_Name": rm_name,
            "Escalation_Message": escalation_message,
            "Attempt_Count": str(MAX_RM_REMINDERS),
        },
        escalation_level="Manager alert",
        escalation_message=escalation_message,
    )


def _has_rm_progress_since_accept(db: Session, lead: Lead, since: datetime) -> bool:
    if lead.status.upper() not in _EARLY_PIPELINE_STATUSES:
        return True
    if lead.assigned_to_id is None:
        return True

    assignee_id = lead.assigned_to_id
    activities = db.scalars(
        select(LeadActivity).where(
            LeadActivity.lead_id == lead.id,
            LeadActivity.created_by_id == assignee_id,
            LeadActivity.created_at > since,
        )
    ).all()
    for activity in activities:
        if activity.type == "ASSIGNMENT_ESCALATION":
            continue
        if activity.type == "NOTE" and "Accepted lead assignment" in activity.description:
            continue
        return True

    note = db.scalar(
        select(LeadNote.id)
        .where(
            LeadNote.lead_id == lead.id,
            LeadNote.created_by_id == assignee_id,
            LeadNote.created_at > since,
        )
        .limit(1)
    )
    return note is not None


def process_pending_assignment_escalations(
    db: Session,
    *,
    now: datetime | None = None,
) -> EscalationRunCounts:
    when = now or datetime.now(timezone.utc)
    counts = EscalationRunCounts()

    pending_leads = db.scalars(
        select(Lead).where(
            Lead.is_deleted.is_(False),
            Lead.assignment_status == ASSIGNMENT_PENDING,
            Lead.assigned_to_id.is_not(None),
            Lead.assigned_at.is_not(None),
        )
    ).all()

    for lead in pending_leads:
        elapsed = working_minutes_between(lead.assigned_at, when)
        assignee = resolve_rm_user(db, lead)
        actor_id = _system_actor_id(db, lead)

        if (
            lead.assignment_escalation_level >= MAX_RM_REMINDERS
            and elapsed >= PENDING_UNASSIGN_AFTER_MINUTES
        ):
            _unassign_lead_for_rm_inactivity(
                db,
                lead,
                previous_rm=assignee,
                reason="no acceptance after assignment reminders",
                actor_id=actor_id,
                notify_assigner_only=True,
            )
            counts.pending_escalations += 1
            counts.unassignments += 1
            continue

        for threshold, level, label in PENDING_ESCALATION_TIERS:
            if elapsed < threshold or lead.assignment_escalation_level >= level:
                continue

            subject = _lead_subject(lead)
            elapsed_label = f"{elapsed} working minutes"
            _notify_users(
                db,
                agency_id=lead.agency_id,
                users=_targets_for_tier(db, lead, level),
                payload=CrmAlertPayload(
                    agency_id=lead.agency_id,
                    event_title=f"Assignment {label}",
                    subject=subject,
                    detail=(
                        f"Pending RM accept for {elapsed} working minutes "
                        f"(threshold {threshold} min)."
                    ),
                    extra=f"Accept within {ACCEPT_WINDOW_WORKING_MINUTES} min · Status: {lead.status}",
                ),
                lead=lead,
                template_id="team_rm_accept_reminder",
                elapsed_time=elapsed_label,
                escalation_level=f"Reminder {level}/{MAX_RM_REMINDERS}",
                escalation_message=(
                    f"Lead {lead.lead_code or lead.id} not accepted after {elapsed_label}. "
                    f"Reminder {level} of {MAX_RM_REMINDERS} sent to assigned RM."
                ),
                template_variables={"Attempt_Count": f"{level}/{MAX_RM_REMINDERS}"},
            )
            lead.assignment_escalation_level = level
            _log_escalation_activity(
                db,
                lead,
                description=f"Assignment reminder {level}/{MAX_RM_REMINDERS}: {label} ({threshold} working min)",
                actor_id=actor_id,
            )
            counts.pending_escalations += 1
            break

    return counts


def process_accept_inactivity_reminders(
    db: Session,
    *,
    now: datetime | None = None,
) -> tuple[int, int]:
    when = now or datetime.now(timezone.utc)
    sent = 0
    unassigned = 0

    accepted_leads = db.scalars(
        select(Lead).where(
            Lead.is_deleted.is_(False),
            Lead.assignment_status == ASSIGNMENT_ACCEPTED,
            Lead.assigned_to_id.is_not(None),
            Lead.assignment_accepted_at.is_not(None),
        )
    ).all()

    for lead in accepted_leads:
        if _has_rm_progress_since_accept(db, lead, lead.assignment_accepted_at):
            lead.assignment_escalation_level = 0
            lead.accept_inactivity_notified = False
            continue

        elapsed = working_minutes_between(lead.assignment_accepted_at, when)
        reminder_count = lead.assignment_escalation_level
        assignee = resolve_rm_user(db, lead)
        actor_id = _system_actor_id(db, lead)

        if reminder_count >= MAX_RM_REMINDERS:
            unassign_after = POST_ACCEPT_INACTIVITY_MINUTES * (MAX_RM_REMINDERS + 1)
            if elapsed < unassign_after:
                continue
            _unassign_lead_for_rm_inactivity(
                db,
                lead,
                previous_rm=assignee,
                reason="no customer contact after acceptance reminders",
                actor_id=actor_id,
                notify_assigner_only=False,
            )
            unassigned += 1
            continue

        next_threshold = POST_ACCEPT_INACTIVITY_MINUTES * (reminder_count + 1)
        if elapsed < next_threshold:
            continue

        if assignee is None:
            lead.accept_inactivity_notified = True
            continue

        next_reminder = reminder_count + 1
        subject = _lead_subject(lead)
        elapsed_label = f"{elapsed} working minutes"
        _notify_users(
            db,
            agency_id=lead.agency_id,
            users=[assignee],
            payload=CrmAlertPayload(
                agency_id=lead.agency_id,
                event_title=f"No action after accept ({next_reminder}/{MAX_RM_REMINDERS})",
                subject=subject,
                detail=(
                    f"No customer contact recorded {elapsed} working minutes after accepting "
                    f"this lead."
                ),
                extra=f"Reminder {next_reminder} of {MAX_RM_REMINDERS} · Status: {lead.status}",
            ),
            lead=lead,
            template_id="team_no_action_after_accept",
            elapsed_time=elapsed_label,
            escalation_level=f"Reminder {next_reminder}/{MAX_RM_REMINDERS}",
            escalation_message=(
                f"No call or note logged for lead {lead.lead_code or lead.id} after accept. "
                f"Reminder {next_reminder} of {MAX_RM_REMINDERS}."
            ),
            template_variables={"Attempt_Count": f"{next_reminder}/{MAX_RM_REMINDERS}"},
        )
        _log_escalation_activity(
            db,
            lead,
            description=(
                f"RM inactivity reminder {next_reminder}/{MAX_RM_REMINDERS}: no progress "
                f"{POST_ACCEPT_INACTIVITY_MINUTES}+ working minutes after accept"
            ),
            actor_id=actor_id,
        )
        lead.assignment_escalation_level = next_reminder
        lead.accept_inactivity_notified = next_reminder >= MAX_RM_REMINDERS
        sent += 1

    return sent, unassigned


def run_assignment_escalations(db: Session) -> dict[str, int]:
    pending = process_pending_assignment_escalations(db)
    inactivity_sent, inactivity_unassigned = process_accept_inactivity_reminders(db)
    db.commit()
    return {
        "pending_escalations": pending.pending_escalations,
        "reassignments": pending.reassignments,
        "accept_inactivity_reminders": inactivity_sent,
        "unassignments": pending.unassignments + inactivity_unassigned,
    }


def run_assignment_escalations_job() -> None:
    from database import SessionLocal

    db = SessionLocal()
    try:
        counts = run_assignment_escalations(db)
        logger.info("Assignment escalation job complete: %s", counts)
    except Exception:
        db.rollback()
        logger.exception("Assignment escalation job failed")
    finally:
        db.close()
