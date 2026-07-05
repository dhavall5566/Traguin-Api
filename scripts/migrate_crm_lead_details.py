#!/usr/bin/env python3
"""
Add CRM lead detail columns (trip preferences / address block).

Run: python scripts/migrate_crm_lead_details.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text

from database import engine

COLUMNS = [
    ("travel_date", "DATE NULL"),
    ("address_line1", "VARCHAR(255) NULL"),
    ("address_line2", "VARCHAR(255) NULL"),
    ("city", "VARCHAR(128) NULL"),
    ("pincode", "VARCHAR(32) NULL"),
    ("state", "VARCHAR(128) NULL"),
    ("country", "VARCHAR(128) NULL"),
    ("adults_count", "INTEGER NULL"),
    ("children_count", "INTEGER NULL"),
    ("children_ages", "JSONB NULL"),
    ("travel_type", "VARCHAR(32) NULL"),
    ("arrival_date", "DATE NULL"),
    ("hotel_category", "VARCHAR(32) NULL"),
    ("meal_category", "VARCHAR(32) NULL"),
    ("travel_destination", "VARCHAR(255) NULL"),
    ("occasion", "VARCHAR(32) NULL"),
    ("flight_type", "VARCHAR(32) NULL"),
    ("extra_baggage", "VARCHAR(8) NULL"),
    ("wheelchair_assistance", "VARCHAR(8) NULL"),
    ("visa_assistance", "VARCHAR(8) NULL"),
    ("travel_insurance", "VARCHAR(8) NULL"),
    ("transportation", "VARCHAR(16) NULL"),
]


def main() -> None:
    with engine.begin() as connection:
        for name, col_type in COLUMNS:
            connection.execute(
                text(
                    f"""
                    ALTER TABLE crm.leads
                    ADD COLUMN IF NOT EXISTS {name} {col_type}
                    """
                )
            )
            print(f"  crm.leads.{name}")
    print("Migration complete.")


if __name__ == "__main__":
    main()
