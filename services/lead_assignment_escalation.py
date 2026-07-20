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
    find_alternate_sales_agent,
    resolve_admin_users,
    resolve_ceo_users,
    resolve_ops_head_users,
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

# (working_minutes_threshold, escalation_level, event_title_suffix)
PENDING_ESCALATION_TIERS: tuple[tuple[int, int, str], ...] = (
    (15, 1, "RM reminder"),
    (30, 2, "RM second reminder"),
    (45, 3, "Admin alert"),
    (60, 4, "Ops head alert"),
    (90, 5, "Reassign RM"),
)

_EARLY_PIPELINE_STATUSES = frozenset({"NEW", "ASSIGNED", "ACCEPTED"})


@dataclass(frozen=True)
class EscalationRunCounts:
    pending_escalations: int = 0
    accept_inactivity_reminders: int = 0
    reassignments: int = 0


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
    assignee = db.get(User, lead.assigned_to_id) if lead.assigned_to_id else None
    if level in (1, 2):
        return [assignee] if assignee is not None else []
    if level == 3:
        return resolve_admin_users(db, lead.agency_id)
    if level == 4:
        return resolve_ops_head_users(db, lead.agency_id)
    if level == 5:
        ceo = resolve_ceo_users(db, lead.agency_id)
        ops = resolve_ops_head_users(db, lead.agency_id)
        seen: set[UUID] = set()
        out: list[User] = []
        for user in [*ceo, *ops]:
            if user.id in seen:
                continue
            seen.add(user.id)
            out.append(user)
        return out
    return []


def _reassign_lead(db: Session, lead: Lead, *, actor_id: UUID) -> bool:
    previous_id = lead.assigned_to_id
    alternate = find_alternate_sales_agent(
        db,
        agency_id=lead.agency_id,
        exclude_user_id=previous_id,
    )
    if alternate is None:
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
            description="Assignment escalated: no alternate RM — lead returned to pool",
            actor_id=actor_id,
        )
        return False

    apply_assignment_on_assign(
        db,
        lead,
        assignee_id=alternate.id,
        actor_id=actor_id,
        agency_id=lead.agency_id,
    )
    _log_escalation_activity(
        db,
        lead,
        description=(
            f"Assignment escalated: reassigned from previous RM to {alternate.name} "
            f"after 90 working minutes without acceptance"
        ),
        actor_id=actor_id,
    )
    return True


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
        for threshold, level, label in PENDING_ESCALATION_TIERS:
            if elapsed < threshold or lead.assignment_escalation_level >= level:
                continue

            actor_id = _system_actor_id(db, lead)
            subject = _lead_subject(lead)

            if level == 5:
                reassigned = _reassign_lead(db, lead, actor_id=actor_id)
                counts.pending_escalations += 1
                if reassigned:
                    counts.reassignments += 1
                _notify_users(
                    db,
                    agency_id=lead.agency_id,
                    users=_targets_for_tier(db, lead, level),
                    payload=CrmAlertPayload(
                        agency_id=lead.agency_id,
                        event_title="Lead reassigned (90 min)",
                        subject=subject,
                        detail=f"Lead reassigned after {threshold} working minutes without RM acceptance.",
                        extra=f"Previous assignee overdue · Status: {lead.status}",
                    ),
                    lead=lead,
                    template_id="team_escalation",
                    escalation_level=f"Tier {level}",
                    escalation_message=f"Lead reassigned after {threshold} working minutes without RM acceptance.",
                )
                break

            elapsed_label = f"{elapsed} working minutes"
            template_id = "team_rm_accept_reminder" if level in (1, 2) else "team_escalation"
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
                template_id=template_id,
                elapsed_time=elapsed_label,
                escalation_level=f"Tier {level} — {label}",
                escalation_message=(
                    f"Lead {lead.lead_code or lead.id} not accepted after {elapsed_label}. "
                    f"Assigned RM must accept or reject."
                ),
            )
            lead.assignment_escalation_level = level
            _log_escalation_activity(
                db,
                lead,
                description=f"Assignment escalation tier {level}: {label} ({threshold} working min)",
                actor_id=actor_id,
            )
            counts.pending_escalations += 1
            break

    return counts


def process_accept_inactivity_reminders(
    db: Session,
    *,
    now: datetime | None = None,
) -> int:
    when = now or datetime.now(timezone.utc)
    sent = 0

    accepted_leads = db.scalars(
        select(Lead).where(
            Lead.is_deleted.is_(False),
            Lead.assignment_status == ASSIGNMENT_ACCEPTED,
            Lead.assigned_to_id.is_not(None),
            Lead.assignment_accepted_at.is_not(None),
            Lead.accept_inactivity_notified.is_(False),
        )
    ).all()

    for lead in accepted_leads:
        if _has_rm_progress_since_accept(db, lead, lead.assignment_accepted_at):
            lead.accept_inactivity_notified = True
            continue

        elapsed = working_minutes_between(lead.assignment_accepted_at, when)
        if elapsed < POST_ACCEPT_INACTIVITY_MINUTES:
            continue

        assignee = db.get(User, lead.assigned_to_id) if lead.assigned_to_id else None
        if assignee is None:
            lead.accept_inactivity_notified = True
            continue

        subject = _lead_subject(lead)
        _notify_users(
            db,
            agency_id=lead.agency_id,
            users=[assignee],
            payload=CrmAlertPayload(
                agency_id=lead.agency_id,
                event_title="No action after accept",
                subject=subject,
                detail=(
                    f"No customer contact recorded {elapsed} working minutes after accepting "
                    f"this lead."
                ),
                extra=f"Move to Contacted when you reach the customer · Status: {lead.status}",
            ),
            lead=lead,
            template_id="team_no_action_after_accept",
        )
        actor_id = _system_actor_id(db, lead)
        _log_escalation_activity(
            db,
            lead,
            description=(
                f"RM inactivity reminder: no progress {POST_ACCEPT_INACTIVITY_MINUTES}+ "
                "working minutes after accept"
            ),
            actor_id=actor_id,
        )
        lead.accept_inactivity_notified = True
        sent += 1

    return sent


def run_assignment_escalations(db: Session) -> dict[str, int]:
    pending = process_pending_assignment_escalations(db)
    inactivity = process_accept_inactivity_reminders(db)
    db.commit()
    return {
        "pending_escalations": pending.pending_escalations,
        "reassignments": pending.reassignments,
        "accept_inactivity_reminders": inactivity,
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
