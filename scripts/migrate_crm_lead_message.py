#!/usr/bin/env python3
"""
Add crm.leads.message and backfill from website intake notes.

Run: python scripts/migrate_crm_lead_message.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select, text

from database import SessionLocal, engine
from models.crm.leads import Lead, LeadNote


def _extract_message_from_note(content: str) -> str | None:
    for line in content.replace("\r\n", "\n").split("\n"):
        trimmed = line.strip()
        bullet = re.match(r"^[•\-*]\s*Message:\s*(.+)$", trimmed)
        if bullet:
            value = bullet.group(1).strip()
            return value if value and value != "—" else None
        field = re.match(r"^Message:\s*(.+)$", trimmed, re.IGNORECASE)
        if field:
            value = field.group(1).strip()
            return value if value and value != "—" else None
    return None


def main() -> None:
    with engine.begin() as connection:
        connection.execute(
            text(
                """
                ALTER TABLE crm.leads
                ADD COLUMN IF NOT EXISTS message TEXT NULL
                """
            )
        )
    print("Added crm.leads.message (if missing).")

    backfilled = 0
    with SessionLocal() as db:
        leads = db.scalars(
            select(Lead).where(Lead.message.is_(None), Lead.is_deleted.is_(False))
        ).all()
        for lead in leads:
            notes = db.scalars(
                select(LeadNote)
                .where(LeadNote.lead_id == lead.id)
                .order_by(LeadNote.created_at.asc())
            ).all()
            for note in notes:
                extracted = _extract_message_from_note(note.content)
                if extracted:
                    lead.message = extracted
                    backfilled += 1
                    break
        db.commit()

    print(f"Backfilled message on {backfilled} lead(s).")
    print("Migration complete.")


if __name__ == "__main__":
    main()
