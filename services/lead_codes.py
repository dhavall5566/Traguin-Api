"""Assign sequential TEMP lead inquiry codes."""

from __future__ import annotations

from datetime import date, datetime, timezone
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crm.leads import Lead
from utils.lead_codes import TEMP_CODE_RE, format_temp_lead_code


def _lead_created_day(lead: Lead) -> date:
    created = lead.created_at
    if created is None:
        return datetime.now(timezone.utc).date()
    if created.tzinfo is None:
        created = created.replace(tzinfo=timezone.utc)
    return created.date()


def next_temp_sequence(db: Session, agency_id: UUID, day: date) -> int:
    """Next 4-digit daily sequence for TEMP{YYYYMMDD}####-XX codes."""
    day_key = day.strftime("%Y%m%d")
    prefix = f"TEMP{day_key}"
    codes = db.scalars(
        select(Lead.lead_code).where(
            Lead.agency_id == agency_id,
            Lead.lead_code.isnot(None),
            Lead.lead_code.like(f"{prefix}%"),
        )
    ).all()
    max_seq = 0
    for code in codes:
        match = TEMP_CODE_RE.match(code or "")
        if match and match.group(1) == day_key:
            max_seq = max(max_seq, int(match.group(2)))
    return max_seq + 1


def assign_lead_code(db: Session, lead: Lead) -> str:
    if lead.lead_code:
        return lead.lead_code
    day = _lead_created_day(lead)
    sequence = next_temp_sequence(db, lead.agency_id, day)
    lead.lead_code = format_temp_lead_code(day, sequence, lead.source)
    db.flush()
    return lead.lead_code


def ensure_lead_code(db: Session, lead: Lead) -> str:
    """Assign a TEMP inquiry code when missing."""
    if lead.lead_code:
        return lead.lead_code
    code = assign_lead_code(db, lead)
    db.flush()
    return code
