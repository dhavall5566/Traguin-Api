#!/usr/bin/env python3
"""Fix Rajasthan region and ensure North India destinations exist (Punjab, Delhi, UP)."""

from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR.parent) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR.parent))

from database import SessionLocal
from models.destinations import Destination
from utils.db import commit_or_raise

NORTH_DESTINATIONS: list[tuple[str, str, str]] = [
    (
        "punjab",
        "Punjab",
        "Amritsar's Golden Temple, Chandigarh's planned boulevards, Patiala's royal heritage, "
        "and Punjab's vibrant culture with farm-fresh cuisine and warm hospitality.",
    ),
    (
        "delhi",
        "Delhi",
        "Old Delhi's Mughal lanes, Lutyens' monuments, curated heritage walks, and India's "
        "gateway capital for bespoke luxury journeys across the subcontinent.",
    ),
    (
        "uttar-pradesh",
        "Uttar Pradesh",
        "Agra's Taj Mahal, Varanasi's sacred ghats, Lucknow's culinary legacy, and the timeless "
        "heartland of India's royal and spiritual heritage.",
    ),
]


def upsert_north_destination(db, slug: str, name: str, description: str) -> None:
    destination = db.scalar(select(Destination).where(Destination.slug == slug))
    if destination is None:
        destination = Destination(
            slug=slug,
            name=name,
            country="India",
            region="domestic",
            india_region="north",
            description=description,
            starting_price=0,
            moods=["Cultural", "Family", "Luxury"],
            is_published=True,
        )
        db.add(destination)
        print(f"Created destination: {slug}")
        return

    destination.name = name
    destination.country = "India"
    destination.region = "domestic"
    destination.india_region = "north"
    destination.description = description
    destination.is_published = True
    print(f"Updated destination: {slug}")


def main() -> None:
    with SessionLocal() as db:
        rajasthan = db.scalar(select(Destination).where(Destination.slug == "rajasthan"))
        if rajasthan is not None and rajasthan.india_region != "west":
            rajasthan.india_region = "west"
            print("Updated rajasthan -> west")

        for slug, name, description in NORTH_DESTINATIONS:
            upsert_north_destination(db, slug, name, description)

        commit_or_raise(db)
    print("Done.")


if __name__ == "__main__":
    main()
