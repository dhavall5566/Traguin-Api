from datetime import datetime, timedelta, timezone
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope
from models.crm.leads import Lead, LeadFollowup
from models.crm.org_units import OrgUnit
from models.crm.sla_settings import AgencySlaSettings
from models.crm.tenancy import User
from schemas.crm.reports import (
    AgentPerformanceRow,
    BranchMetricRow,
    LeadStageCount,
    ReportsOverview,
    SlaSummary,
)

router = APIRouter()

WON_STATUSES = frozenset({"WON", "CONVERTED", "BOOKED", "CLOSED_WON"})

def _sla_settings(db: Session, agency_id: UUID) -> AgencySlaSettings:
    row = db.get(AgencySlaSettings, agency_id)
    if row is None:
        return AgencySlaSettings(agency_id=agency_id)
    return row

@router.get("/overview", response_model=ReportsOverview)
def reports_overview(agency_id: UUID = Depends(require_agency_scope), db: Session = Depends(get_db)):
    stage_rows = (
        db.query(Lead.status, func.count(Lead.id))
        .filter(Lead.agency_id == agency_id, Lead.is_deleted.is_(False))
        .group_by(Lead.status)
        .all()
    )
    leads_by_stage = [LeadStageCount(status=s, count=c) for s, c in stage_rows]

    agent_rows = (
        db.query(User.id, User.name)
        .filter(User.agency_id == agency_id, User.is_deleted.is_(False))
        .all()
    )
    agent_performance: list[AgentPerformanceRow] = []
    for user_id, name in agent_rows:
        assigned_n = (
            db.query(func.count(Lead.id))
            .filter(
                Lead.agency_id == agency_id,
                Lead.assigned_to_id == user_id,
                Lead.is_deleted.is_(False),
            )
            .scalar()
            or 0
        )
        won_n = (
            db.query(func.count(Lead.id))
            .filter(
                Lead.agency_id == agency_id,
                Lead.assigned_to_id == user_id,
                Lead.is_deleted.is_(False),
                Lead.status.in_(list(WON_STATUSES)),
            )
            .scalar()
            or 0
        )
        rate = round((won_n / assigned_n) * 100, 1) if assigned_n else 0.0
        agent_performance.append(
            AgentPerformanceRow(
                user_id=user_id,
                name=name,
                leads_assigned=assigned_n,
                leads_won=int(won_n),
                conversion_rate=rate,
            )
        )

    units = (
        db.query(OrgUnit)
        .filter(OrgUnit.agency_id == agency_id, OrgUnit.is_deleted.is_(False))
        .all()
    )
    branch_metrics: list[BranchMetricRow] = []
    for unit in units:
        lead_count = (
            db.query(func.count(Lead.id))
            .filter(Lead.agency_id == agency_id, Lead.org_unit_id == unit.id, Lead.is_deleted.is_(False))
            .scalar()
            or 0
        )
        user_count = (
            db.query(func.count(User.id))
            .filter(User.agency_id == agency_id, User.org_unit_id == unit.id, User.is_deleted.is_(False))
            .scalar()
            or 0
        )
        branch_metrics.append(
            BranchMetricRow(
                org_unit_id=unit.id,
                name=unit.name,
                unit_type=unit.unit_type,
                lead_count=int(lead_count),
                user_count=int(user_count),
            )
        )
    unassigned_leads = (
        db.query(func.count(Lead.id))
        .filter(Lead.agency_id == agency_id, Lead.org_unit_id.is_(None), Lead.is_deleted.is_(False))
        .scalar()
        or 0
    )
    if unassigned_leads:
        branch_metrics.append(
            BranchMetricRow(
                org_unit_id=None,
                name="Unassigned",
                unit_type=None,
                lead_count=int(unassigned_leads),
                user_count=0,
            )
        )

    return ReportsOverview(
        leads_by_stage=leads_by_stage,
        agent_performance=agent_performance,
        branch_metrics=branch_metrics,
    )

@router.get("/sla-summary", response_model=SlaSummary)
def reports_sla_summary(agency_id: UUID = Depends(require_agency_scope), db: Session = Depends(get_db)):
    sla = _sla_settings(db, agency_id)
    now = datetime.now(timezone.utc)
    lead_cutoff = now - timedelta(minutes=sla.lead_response_minutes)
    followup_cutoff = now - timedelta(minutes=sla.followup_reminder_minutes)
    proposal_cutoff = now - timedelta(hours=sla.proposal_sla_hours)

    overdue_lead_responses = (
        db.query(func.count(Lead.id))
        .filter(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.status == "NEW",
            Lead.created_at < lead_cutoff,
        )
        .scalar()
        or 0
    )
    overdue_followups = (
        db.query(func.count(LeadFollowup.id))
        .join(Lead, Lead.id == LeadFollowup.lead_id)
        .filter(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            LeadFollowup.status == "PENDING",
            LeadFollowup.scheduled_at < followup_cutoff,
        )
        .scalar()
        or 0
    )
    overdue_proposals = (
        db.query(func.count(Lead.id))
        .filter(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.proposal_sent_at.isnot(None),
            Lead.proposal_sent_at < proposal_cutoff,
            ~Lead.status.in_(list(WON_STATUSES)),
        )
        .scalar()
        or 0
    )

    return SlaSummary(
        overdue_lead_responses=int(overdue_lead_responses),
        overdue_followups=int(overdue_followups),
        overdue_proposals=int(overdue_proposals),
        lead_response_minutes=sla.lead_response_minutes,
        followup_reminder_minutes=sla.followup_reminder_minutes,
        proposal_sla_hours=sla.proposal_sla_hours,
    )
