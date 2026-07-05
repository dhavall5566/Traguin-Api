#!/usr/bin/env python3
"""
Bootstrap the unified Traguin database (CMS + CRM in one PostgreSQL instance).

Creates both schemas and missing tables, then runs incremental migrations.
Safe to re-run on an existing database — does not drop cms data.

Run from api/:  python scripts/init_unified_database.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from database import CRM_SCHEMA, CMS_SCHEMA, check_unified_database, get_unified_database_summary

from scripts.create_crm_tables import create_crm_tables
from scripts.create_tables import ensure_cms_tables
from scripts.run_migrations import run_all_migrations


def main() -> None:
    print("Initializing unified Traguin database (cms + crm schemas)...")
    print()

    before = get_unified_database_summary()
    print(f"Before — cms: {before[CMS_SCHEMA].table_count} tables, crm: {before[CRM_SCHEMA].table_count} tables")
    print()

    print("Ensuring CMS tables (schema: cms)...")
    ensure_cms_tables()

    print("Ensuring CRM tables (schema: crm)...")
    create_crm_tables()

    print()
    print("Running incremental migrations...")
    run_all_migrations()

    print()
    summary = check_unified_database()
    cms_count = summary["schemas"][CMS_SCHEMA]["table_count"]
    crm_count = summary["schemas"][CRM_SCHEMA]["table_count"]
    print(f"Unified database ready — cms: {cms_count} tables, crm: {crm_count} tables")


if __name__ == "__main__":
    main()
