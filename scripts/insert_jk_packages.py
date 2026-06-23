#!/usr/bin/env python3
"""Insert JK-001, JK-002, JK-003, JK-004, JK-006, JK-007, and JK-010 Kashmir packages."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from jk_batch_package_defs import (
    build_jk_001,
    build_jk_002,
    build_jk_003,
    build_jk_004,
    build_jk_006,
    build_jk_007,
    build_jk_010,
)
from models.destinations import Destination
from services.package_insert import run_gujarat_package_inserts
from utils.db import commit_or_raise

KASHMIR_SLUG = "kashmir"


def get_or_create_kashmir_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == KASHMIR_SLUG))
        if destination is None:
            destination = Destination(
                slug=KASHMIR_SLUG,
                name="Jammu & Kashmir",
                country="India",
                region="domestic",
                india_region="north",
                description=(
                    "Dal Lake houseboats, Gulmarg alpine meadows, Pahalgam pine valleys, "
                    "Sonamarg glaciers, and the legendary Kashmir Great Lakes trek."
                ),
                starting_price=0,
                moods=["Family", "Romantic", "Nature", "Adventure"],
                is_published=True,
            )
            db.add(destination)
            db.flush()
            commit_or_raise(db)
            print(f"Created destination: {destination.slug} ({destination.id})")
        else:
            print(f"Using destination: {destination.slug} ({destination.id})")
        return str(destination.id)


def main() -> None:
    dest_id = get_or_create_kashmir_destination_id()
    builders = [
        build_jk_001,
        build_jk_002,
        build_jk_003,
        build_jk_004,
        build_jk_006,
        build_jk_007,
        build_jk_010,
    ]
    packages = [builder(dest_id) for builder in builders]
    run_gujarat_package_inserts(destination_id=dest_id, packages=packages)


if __name__ == "__main__":
    main()
