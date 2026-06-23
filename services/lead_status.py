"""Lead pipeline status side effects (structured markers, not free-text parsing)."""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.orm import Session

from models.crm.leads import Lead, LeadActivity

PROPOSAL_SENT_STATUS = "PROPOSAL_SENT"
ENTERED_PROPOSAL_SENT_ACTIVITY = "ENTERED_PROPOSAL_SENT"


def apply_lead_status_transition(
    db: Session,
    lead: Lead,
    previous_status: str | None,
    *,
    created_by_id: UUID,
    entered_at: datetime | None = None,
) -> None:
    """
    When status enters PROPOSAL_SENT, set lead.proposal_sent_at and append a structured
    ENTERED_PROPOSAL_SENT activity. Clears proposal_sent_at when leaving that stage.
    """
    prev = (previous_status or "").upper()
    curr = lead.status.upper()
    if curr == prev:
        return

    if curr == PROPOSAL_SENT_STATUS and prev != PROPOSAL_SENT_STATUS:
        when = entered_at or datetime.now(timezone.utc)
        lead.proposal_sent_at = when
        db.add(
            LeadActivity(
                lead_id=lead.id,
                type=ENTERED_PROPOSAL_SENT_ACTIVITY,
                description=f"Entered {PROPOSAL_SENT_STATUS} stage",
                created_by_id=created_by_id,
            )
        )
    elif prev == PROPOSAL_SENT_STATUS and curr != PROPOSAL_SENT_STATUS:
        lead.proposal_sent_at = None
