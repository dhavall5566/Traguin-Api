"""Backfill missing crm.leads.lead_code values."""

from __future__ import annotations

from sqlalchemy import select

from database import SessionLocal
from models.crm.leads import Lead
from services.lead_codes import assign_lead_code
from utils.db import commit_or_raise


def main() -> None:
    db = SessionLocal()
    try:
        rows = db.scalars(select(Lead).where(Lead.lead_code.is_(None)).order_by(Lead.created_at)).all()
        if not rows:
            print("All leads already have lead_code.")
            return

        for lead in rows:
            code = assign_lead_code(db, lead)
            db.flush()
            print(f"  {lead.id} -> {code} ({lead.source!r})")

        commit_or_raise(db)
        print(f"Backfilled {len(rows)} lead(s).")
    finally:
        db.close()


if __name__ == "__main__":
    main()
