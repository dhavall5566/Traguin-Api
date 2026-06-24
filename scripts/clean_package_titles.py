#!/usr/bin/env python3
"""Strip decorative dash separators from package and itinerary marketing titles."""

from __future__ import annotations

import sys
from pathlib import Path

_API_ROOT = Path(__file__).resolve().parents[1]
if str(_API_ROOT) not in sys.path:
    sys.path.insert(0, str(_API_ROOT))

from database import SessionLocal
from models.itineraries import Itinerary
from models.packages import Package
from utils.db import commit_or_raise
from utils.package_title import clean_package_title


def main() -> None:
    updated_packages = 0
    updated_itineraries = 0

    with SessionLocal() as db:
        for package in db.query(Package).all():
            cleaned = clean_package_title(package.title)
            if cleaned and cleaned != package.title:
                print(f"package: {package.title!r} -> {cleaned!r}")
                package.title = cleaned
                updated_packages += 1

        for itinerary in db.query(Itinerary).all():
            cleaned = clean_package_title(itinerary.title)
            if cleaned and cleaned != itinerary.title:
                print(f"itinerary: {itinerary.title!r} -> {cleaned!r}")
                itinerary.title = cleaned
                updated_itineraries += 1

        if updated_packages or updated_itineraries:
            commit_or_raise(db)
        else:
            print("No titles needed updating.")

    print(
        f"Done. Updated {updated_packages} package(s) and {updated_itineraries} itinerary title(s)."
    )


if __name__ == "__main__":
    main()
