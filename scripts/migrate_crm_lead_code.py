#!/usr/bin/env python3
"""
Add human-readable lead codes (TRG001-ITN) and backfill existing rows.

Run: python scripts/migrate_crm_lead_code.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import engine
from utils.lead_codes import format_lead_code


def main() -> None:
    with engine.begin() as connection:
        connection.execute(
            text(
                """
                ALTER TABLE crm.leads
                ADD COLUMN IF NOT EXISTS lead_code VARCHAR(32) NULL
                """
            )
        )
        print("  crm.leads.lead_code column")

        agencies = connection.execute(
            text("SELECT DISTINCT agency_id FROM crm.leads ORDER BY agency_id")
        ).fetchall()

        for (agency_id,) in agencies:
            rows = connection.execute(
                text(
                    """
                    SELECT id, source, lead_code
                    FROM crm.leads
                    WHERE agency_id = :agency_id
                    ORDER BY created_at ASC, id ASC
                    """
                ),
                {"agency_id": agency_id},
            ).fetchall()

            seq = 0
            used: set[str] = set()
            for row_id, source, existing_code in rows:
                if existing_code:
                    used.add(str(existing_code))
                    try:
                        head = str(existing_code).split("-", 1)[0]
                        num = int(head[3:])
                        seq = max(seq, num)
                    except (TypeError, ValueError):
                        pass
                    continue

                while True:
                    seq += 1
                    code = format_lead_code(seq, source)
                    if code not in used:
                        break

                connection.execute(
                    text(
                        """
                        UPDATE crm.leads
                        SET lead_code = :code
                        WHERE id = :id
                        """
                    ),
                    {"code": code, "id": row_id},
                )
                used.add(code)

            print(f"  backfilled agency {agency_id} ({len(rows)} leads)")

        connection.execute(
            text(
                """
                CREATE UNIQUE INDEX IF NOT EXISTS uq_leads_agency_lead_code
                ON crm.leads (agency_id, lead_code)
                WHERE lead_code IS NOT NULL
                """
            )
        )
        print("  unique index uq_leads_agency_lead_code")

    print("Migration complete.")


if __name__ == "__main__":
    main()
