#!/usr/bin/env python3
"""Insert KL-001, KL-002, KL-003, KL-005, KL-006, KL-009, and KL-010 Kerala packages."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from kl_batch_package_defs import (
    build_kl_001,
    build_kl_002,
    build_kl_003,
    build_kl_005,
    build_kl_006,
    build_kl_009,
    build_kl_010,
)
from models.destinations import Destination
from services.package_insert import run_gujarat_package_inserts
from utils.db import commit_or_raise

KERALA_SLUG = "kerala"


def get_or_create_kerala_destination_id() -> str:
    with SessionLocal() as db:
        destination = db.scalar(select(Destination).where(Destination.slug == KERALA_SLUG))
        if destination is None:
            destination = Destination(
                slug=KERALA_SLUG,
                name="Kerala",
                country="India",
                region="domestic",
                india_region="south",
                description=(
                    "Munnar tea hills, Alleppey backwaters, Thekkady spice forests, "
                    "Kumarakom lake retreats, Kovalam beaches, and Wayanad adventure trails."
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
    dest_id = get_or_create_kerala_destination_id()
    builders = [
        build_kl_001,
        build_kl_002,
        build_kl_003,
        build_kl_005,
        build_kl_006,
        build_kl_009,
        build_kl_010,
    ]
    packages = [builder(dest_id) for builder in builders]
    run_gujarat_package_inserts(destination_id=dest_id, packages=packages)


if __name__ == "__main__":
    main()
