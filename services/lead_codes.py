"""Assign sequential TRG lead codes."""

from __future__ import annotations

import re
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crm.leads import Lead
from utils.lead_codes import format_lead_code

_LEAD_SEQUENCE_RE = re.compile(r"^TRG(\d+)")


def next_lead_sequence(db: Session, agency_id: UUID) -> int:
    codes = db.scalars(
        select(Lead.lead_code).where(
            Lead.agency_id == agency_id,
            Lead.lead_code.isnot(None),
        )
    ).all()
    max_seq = 0
    for code in codes:
        match = _LEAD_SEQUENCE_RE.match(code or "")
        if match:
            max_seq = max(max_seq, int(match.group(1)))
    return max_seq + 1


def assign_lead_code(db: Session, lead: Lead) -> str:
    if lead.lead_code:
        return lead.lead_code
    lead.lead_code = format_lead_code(next_lead_sequence(db, lead.agency_id), lead.source)
    db.flush()
    return lead.lead_code


def ensure_lead_code(db: Session, lead: Lead) -> str:
    """Assign a TRG code when missing so clients never see placeholder IDs."""
    if lead.lead_code:
        return lead.lead_code
    code = assign_lead_code(db, lead)
    db.flush()
    return code
