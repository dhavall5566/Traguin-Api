#!/usr/bin/env python3
"""
Refresh lead_code suffixes to 2-letter abbreviations from source.

Run: python scripts/refresh_crm_lead_code_abbrevs.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import engine
from utils.lead_codes import format_lead_code

_SEQ_RE = re.compile(r"^TRG(\d+)-", re.IGNORECASE)


def main() -> None:
    updated = 0
    with engine.begin() as connection:
        rows = connection.execute(
            text(
                """
                SELECT id, source, lead_code
                FROM crm.leads
                ORDER BY created_at ASC, id ASC
                """
            )
        ).fetchall()

        for row_id, source, lead_code in rows:
            seq = None
            if lead_code:
                match = _SEQ_RE.match(str(lead_code))
                if match:
                    seq = int(match.group(1))
            if seq is None:
                continue

            new_code = format_lead_code(seq, source)
            if str(lead_code) == new_code:
                continue

            connection.execute(
                text("UPDATE crm.leads SET lead_code = :code WHERE id = :id"),
                {"code": new_code, "id": row_id},
            )
            print(f"  {lead_code} → {new_code} ({source!r})")
            updated += 1

    print(f"Refreshed {updated} lead code(s).")


if __name__ == "__main__":
    main()
