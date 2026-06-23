#!/usr/bin/env python3
"""Insert HP-004, HP-006, HP-007, HP-009, and HP-010 Himachal packages."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from hp_batch_package_defs import (
    build_hp_004,
    build_hp_006,
    build_hp_007,
    build_hp_009,
    build_hp_010,
)
from models.destinations import Destination
from services.package_insert import run_gujarat_package_inserts

HIMACHAL_SLUG = "himachal"


def get_himachal_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == HIMACHAL_SLUG))
        if destination is None:
            print(f"Destination '{HIMACHAL_SLUG}' not found. Run insert_hp_003_package.py first.", file=sys.stderr)
            sys.exit(1)
        return str(destination.id)


def main() -> None:
    dest_id = get_himachal_destination_id()
    packages = [
        build_hp_004(dest_id),
        build_hp_006(dest_id),
        build_hp_007(dest_id),
        build_hp_009(dest_id),
        build_hp_010(dest_id),
    ]
    run_gujarat_package_inserts(destination_id=dest_id, packages=packages)


if __name__ == "__main__":
    main()
