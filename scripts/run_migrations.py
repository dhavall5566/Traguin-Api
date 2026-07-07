#!/usr/bin/env python3
"""
Run all incremental CMS + CRM migrations against the unified database.

Run from api/:  python scripts/run_migrations.py
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

MIGRATION_MODULES: tuple[str, ...] = (
    "scripts.migrate_performance_indexes",
    "scripts.migrate_gallery_item_media",
    "scripts.migrate_client_stories_simplify",
    "scripts.migrate_remove_client_story_films",
    "scripts.migrate_homepage_region_panels_is_active",
    "scripts.migrate_packages_sold_last_month",
    "scripts.migrate_crm_lead_customer_and_email_uniqueness",
    "scripts.migrate_crm_lead_message",
    "scripts.migrate_crm_lead_proposal_sent_at",
    "scripts.migrate_crm_lead_details",
    "scripts.migrate_crm_lead_cms_form_submission_id",
    "scripts.migrate_cms_form_submission_package_id",
    "scripts.migrate_crm_lead_cms_package_id",
    "scripts.migrate_crm_lead_code",
    "scripts.migrate_crm_lead_package_mode",
    "scripts.migrate_crm_lead_priority_category",
    "scripts.migrate_crm_lead_assignment_status",
    "scripts.migrate_crm_agency_smtp_settings",
)


def run_all_migrations() -> None:
    for module_name in MIGRATION_MODULES:
        module = importlib.import_module(module_name)
        label = module_name.rsplit(".", 1)[-1]
        print(f"  → {label}")
        module.main()


def main() -> None:
    print("Running unified database migrations...")
    run_all_migrations()
    print("All migrations complete.")


if __name__ == "__main__":
    main()
