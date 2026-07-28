from uuid import UUID

from pydantic import BaseModel

class LeadStageCount(BaseModel):
    status: str
    count: int

class AgentPerformanceRow(BaseModel):
    user_id: UUID
    name: str
    leads_assigned: int
    leads_won: int
    conversion_rate: float

class BranchMetricRow(BaseModel):
    org_unit_id: UUID | None
    name: str
    unit_type: str | None
    lead_count: int
    user_count: int

class ReportsOverview(BaseModel):
    leads_by_stage: list[LeadStageCount]
    agent_performance: list[AgentPerformanceRow]
    branch_metrics: list[BranchMetricRow]

class SlaSummary(BaseModel):
    overdue_lead_responses: int
    overdue_followups: int
    overdue_proposals: int
    lead_response_minutes: int
    followup_reminder_minutes: int
    proposal_sla_hours: int
