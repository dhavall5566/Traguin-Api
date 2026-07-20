"""Lead pipeline status side effects (structured markers, not free-text parsing)."""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.orm import Session

from models.crm.leads import Lead, LeadActivity

ITINERARY_SENT_STATUS = "ITINERARY_SENT"
PROPOSAL_SENT_STATUS = "PROPOSAL_SENT"  # legacy alias
ENTERED_PROPOSAL_SENT_ACTIVITY = "ENTERED_PROPOSAL_SENT"
_ITINERARY_SENT_STATUSES = frozenset({ITINERARY_SENT_STATUS, PROPOSAL_SENT_STATUS})


def _is_itinerary_sent_status(status: str | None) -> bool:
    return (status or "").upper() in _ITINERARY_SENT_STATUSES


def apply_lead_status_transition(
    db: Session,
    lead: Lead,
    previous_status: str | None,
    *,
    created_by_id: UUID,
    entered_at: datetime | None = None,
) -> None:
    """
    When status enters itinerary-sent (ITINERARY_SENT or legacy PROPOSAL_SENT), set
    lead.proposal_sent_at and append ENTERED_PROPOSAL_SENT. Clears when leaving that stage.
    """
    prev = (previous_status or "").upper()
    curr = lead.status.upper()
    if curr == prev:
        return

    entering = _is_itinerary_sent_status(curr) and not _is_itinerary_sent_status(prev)
    leaving = _is_itinerary_sent_status(prev) and not _is_itinerary_sent_status(curr)

    if entering:
        when = entered_at or datetime.now(timezone.utc)
        lead.proposal_sent_at = when
        db.add(
            LeadActivity(
                lead_id=lead.id,
                type=ENTERED_PROPOSAL_SENT_ACTIVITY,
                description=f"Entered {curr} stage",
                created_by_id=created_by_id,
            )
        )
    elif leaving:
        lead.proposal_sent_at = None
