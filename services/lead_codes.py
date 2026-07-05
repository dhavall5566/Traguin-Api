"""Assign sequential TRG lead codes."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from models.crm.leads import Lead
from utils.lead_codes import format_lead_code


def next_lead_sequence(db: Session, agency_id: UUID) -> int:
    value = db.execute(
        text(
            """
            SELECT COALESCE(MAX(
                CAST(SUBSTRING(lead_code FROM '^TRG([0-9]+)') AS INTEGER)
            ), 0) + 1
            FROM crm.leads
            WHERE agency_id = :agency_id
              AND lead_code IS NOT NULL
            """
        ),
        {"agency_id": agency_id},
    ).scalar_one()
    return int(value or 1)


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
