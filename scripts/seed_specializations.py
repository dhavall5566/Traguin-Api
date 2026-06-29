#!/usr/bin/env python3
"""Replace placeholder specializations with real TRAGUIN content."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from database import SessionLocal
from models.content import Specialization

PLACEHOLDER_TITLE = re.compile(r"^specialization\s*\d+$", re.IGNORECASE)

SPECIALIZATIONS = [
    {
        "slug": "bespoke-leisure",
        "title": "Bespoke Leisure",
        "description": (
            "Custom holidays across India and abroad with handpicked stays, unhurried routes, "
            "and the details that match how you travel."
        ),
        "icon_key": "compass",
        "sort_order": 0,
    },
    {
        "slug": "honeymoons-celebrations",
        "title": "Honeymoons & Celebrations",
        "description": (
            "Romantic escapes and milestone journeys with private transfers, curated dining, "
            "and moments worth remembering."
        ),
        "icon_key": "sparkles",
        "sort_order": 1,
    },
    {
        "slug": "family-group-travel",
        "title": "Family & Group Travel",
        "description": (
            "Multi-generational trips planned with comfort, safety, and activities that work "
            "for every age in your group."
        ),
        "icon_key": "users",
        "sort_order": 2,
    },
    {
        "slug": "corporate-mice",
        "title": "Corporate & MICE",
        "description": (
            "Leadership retreats, incentive travel, and offsites coordinated end to end, "
            "including venues, logistics, and on-ground support."
        ),
        "icon_key": "briefcase",
        "sort_order": 3,
    },
    {
        "slug": "visa-documentation",
        "title": "Visa & Documentation",
        "description": (
            "Visa applications, insurance guidance, and travel paperwork handled before you "
            "pack, so there are fewer surprises at departure."
        ),
        "icon_key": "file-check",
        "sort_order": 4,
    },
]


def main() -> None:
    db = SessionLocal()
    try:
        removed = 0
        for item in db.query(Specialization).all():
            if PLACEHOLDER_TITLE.match(item.title.strip()):
                db.delete(item)
                removed += 1

        upserted = 0
        for spec in SPECIALIZATIONS:
            row = db.query(Specialization).filter(Specialization.slug == spec["slug"]).one_or_none()
            if row is None:
                db.add(Specialization(**spec))
                upserted += 1
                continue
            row.title = spec["title"]
            row.description = spec["description"]
            row.icon_key = spec["icon_key"]
            row.sort_order = spec["sort_order"]

        db.commit()
        total = db.query(Specialization).count()
        print(f"Removed {removed} placeholder specialization(s).")
        print(f"Upserted {upserted} new specialization(s).")
        print(f"Total specializations in database: {total}.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
