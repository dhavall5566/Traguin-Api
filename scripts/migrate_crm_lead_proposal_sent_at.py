#!/usr/bin/env python3
"""
Add leads.proposal_sent_at and backfill from structured/historical activity data.

Run: python scripts/migrate_crm_lead_proposal_sent_at.py
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select, text

from database import SessionLocal, engine
from models.crm.leads import Lead, LeadActivity
from services.lead_status import ENTERED_PROPOSAL_SENT_ACTIVITY, PROPOSAL_SENT_STATUS

LEGACY_STAGE_CHANGE_PATTERN = re.compile(r"\bto\s+PROPOSAL_SENT\b", re.IGNORECASE)


def legacy_proposal_entered_at(activities: list[LeadActivity]) -> datetime | None:
    stage_changes = [
        a
        for a in activities
        if a.type == "STAGE_CHANGE" and LEGACY_STAGE_CHANGE_PATTERN.search(a.description or "")
    ]
    if not stage_changes:
        return None
    stage_changes.sort(key=lambda a: a.created_at)
    return stage_changes[0].created_at


def structured_proposal_entered_at(activities: list[LeadActivity]) -> datetime | None:
    markers = [a for a in activities if a.type == ENTERED_PROPOSAL_SENT_ACTIVITY]
    if not markers:
        return None
    markers.sort(key=lambda a: a.created_at)
    return markers[0].created_at


def main() -> None:
    with engine.begin() as connection:
        connection.execute(
            text(
                """
                ALTER TABLE crm.leads
                ADD COLUMN IF NOT EXISTS proposal_sent_at TIMESTAMPTZ NULL
                """
            )
        )
        connection.execute(
            text(
                """
                CREATE INDEX IF NOT EXISTS ix_leads_proposal_sent_at
                ON crm.leads (proposal_sent_at)
                WHERE proposal_sent_at IS NOT NULL
                """
            )
        )
    print("Added crm.leads.proposal_sent_at (if missing).")

    db = SessionLocal()
    try:
        leads = db.scalars(select(Lead)).all()
        backfilled = 0
        for lead in db.scalars(
            select(Lead).where(Lead.proposal_sent_at.is_(None), Lead.status == PROPOSAL_SENT_STATUS)
        ).all():
            activities = list(
                db.scalars(select(LeadActivity).where(LeadActivity.lead_id == lead.id)).all()
            )
            anchor = structured_proposal_entered_at(activities) or legacy_proposal_entered_at(
                activities
            )
            if anchor is None:
                anchor = lead.updated_at or lead.created_at or datetime.now(timezone.utc)
            lead.proposal_sent_at = anchor
            backfilled += 1
        db.commit()
        print(f"Backfilled proposal_sent_at on {backfilled} active PROPOSAL_SENT lead(s).")
        print(f"Total leads in DB: {len(leads)}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
