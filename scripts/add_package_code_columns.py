#!/usr/bin/env python3
"""Add serial_code + traguin_tour_code columns to cms.packages and backfill all rows."""

from __future__ import annotations

import argparse

from sqlalchemy import text
from sqlalchemy.orm import selectinload

from database import CMS_SCHEMA, SessionLocal, _physical_schema, cms_engine
from models.packages import Package
from utils.db import commit_or_raise
from utils.package_codes import resolve_package_codes


def _packages_table_ref() -> str:
    physical = _physical_schema(CMS_SCHEMA)
    return f"{physical}.packages" if physical else "packages"


def ensure_columns() -> None:
    table = _packages_table_ref()
    with cms_engine.begin() as conn:
        conn.execute(
            text(
                f"""
                ALTER TABLE {table}
                ADD COLUMN IF NOT EXISTS serial_code VARCHAR(16),
                ADD COLUMN IF NOT EXISTS traguin_tour_code VARCHAR(128)
                """
            )
        )
        conn.execute(
            text(
                f"""
                CREATE UNIQUE INDEX IF NOT EXISTS ix_packages_serial_code
                ON {table} (serial_code)
                WHERE serial_code IS NOT NULL
                """
            )
        )


def backfill_packages(*, dry_run: bool = False) -> None:
    db = SessionLocal()
    try:
        packages = (
            db.query(Package)
            .options(selectinload(Package.highlights))
            .order_by(Package.slug)
            .all()
        )
        updated = 0
        for package in packages:
            highlight_texts = [h.text for h in package.highlights]
            serial, tour = resolve_package_codes(package.slug, highlight_texts)
            if package.serial_code == serial and package.traguin_tour_code == tour:
                continue
            print(f"{serial:8} | {tour:35} | {package.slug}")
            if not dry_run:
                package.serial_code = serial
                package.traguin_tour_code = tour
            updated += 1
        if dry_run:
            print(f"Dry run — would update {updated} of {len(packages)} packages.")
        else:
            commit_or_raise(db)
            print(f"Updated {updated} of {len(packages)} packages.")
    finally:
        db.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing.")
    args = parser.parse_args()
    ensure_columns()
    backfill_packages(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
