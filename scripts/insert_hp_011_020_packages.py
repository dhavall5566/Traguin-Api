#!/usr/bin/env python3
"""Insert HP-011 through HP-020 Himachal packages (excluding HP-016)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from hp_batch_package_defs_011_020 import (
    build_hp_011,
    build_hp_012,
    build_hp_013,
    build_hp_014,
    build_hp_015,
    build_hp_017,
    build_hp_018,
    build_hp_019,
    build_hp_020,
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
    builders = [
        build_hp_011,
        build_hp_012,
        build_hp_013,
        build_hp_014,
        build_hp_015,
        build_hp_017,
        build_hp_018,
        build_hp_019,
        build_hp_020,
    ]
    packages = [builder(dest_id) for builder in builders]
    run_gujarat_package_inserts(destination_id=dest_id, packages=packages)


if __name__ == "__main__":
    main()
