#!/usr/bin/env python3
"""
Audit and repair homepage hero visibility vs package is_featured flags.

Run:
  python scripts/repair_homepage_package_visibility.py
  python scripts/repair_homepage_package_visibility.py --check-only
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from database import SessionLocal
from services.homepage_hero_settings import (
    audit_homepage_package_visibility,
    get_or_create_company_stats,
    repair_homepage_package_visibility,
)
from utils.db import commit_or_raise


def _print_audit(audit) -> None:
    print(f"Published packages: {audit.published_count}")
    print(f"Featured packages: {audit.featured_count}")
    print(f"Homepage visible list: {audit.visible_count}")
    if audit.ok:
        print("OK — no homepage visibility mismatches found.")
        return

    print(f"Issues found: {len(audit.issues)}")
    for issue in audit.issues:
        code = issue.serial_code or issue.package_id
        print(f"  - [{issue.issue}] {code}: {issue.title}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Audit only; do not repair package flags or visible list.",
    )
    args = parser.parse_args()

    with SessionLocal() as db:
        stats = get_or_create_company_stats(db)
        if args.check_only:
            audit = audit_homepage_package_visibility(db, stats)
            _print_audit(audit)
            if not audit.ok:
                sys.exit(1)
            return

        before = audit_homepage_package_visibility(db, stats)
        if before.ok:
            _print_audit(before)
            return

        print("Before repair:")
        _print_audit(before)
        repair_homepage_package_visibility(db, stats)
        commit_or_raise(db)
        after = audit_homepage_package_visibility(db, stats)
        print("\nAfter repair:")
        _print_audit(after)
        if not after.ok:
            sys.exit(1)


if __name__ == "__main__":
    main()
