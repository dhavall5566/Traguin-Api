#!/usr/bin/env python3
"""
Seed client stories from the Traguin frontend static content (testimonials + gallery moments).

Run from api/: python scripts/seed_client_stories.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select

from database import SessionLocal
from models.gallery import ClientStory
from models.media import MediaAsset

TESTIMONIALS = [
    {
        "slug": "priya-arjun-sharma",
        "client_name": "Priya & Arjun Sharma",
        "destination_label": "Bali",
        "trip_type": "Luxury Honeymoon",
        "quote": "TRAGUIN transformed our honeymoon into a cinematic love story. Every moment felt personally orchestrated.",
        "portrait_url": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?ixlib=rb-4.1.0&auto=format&fit=crop&w=400&q=80",
        "show_on_home": True,
        "show_in_gallery": True,
        "home_sort_order": 1,
        "gallery_sort_order": 1,
    },
    {
        "slug": "rajesh-mehta",
        "client_name": "Rajesh Mehta",
        "destination_label": "Switzerland",
        "trip_type": "Alpine Escape",
        "quote": "The attention to detail was extraordinary. From private transfers to hidden alpine restaurants, flawless.",
        "portrait_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.1.0&auto=format&fit=crop&w=400&q=80",
        "show_on_home": True,
        "show_in_gallery": True,
        "home_sort_order": 2,
        "gallery_sort_order": 2,
    },
    {
        "slug": "ananya-desai",
        "client_name": "Ananya Desai",
        "destination_label": "Kerala",
        "trip_type": "Family Journey",
        "quote": "Our family backwater journey was magical. The kids still talk about the houseboat every day.",
        "portrait_url": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.1.0&auto=format&fit=crop&w=400&q=80",
        "show_on_home": True,
        "show_in_gallery": True,
        "home_sort_order": 3,
        "gallery_sort_order": 3,
    },
    {
        "slug": "vikram-neha-kapoor",
        "client_name": "Vikram & Neha Kapoor",
        "destination_label": "Dubai",
        "trip_type": "Corporate Retreat",
        "quote": "Corporate retreat turned luxury escape. TRAGUIN handled everything with white-glove precision.",
        "portrait_url": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.1.0&auto=format&fit=crop&w=400&q=80",
        "show_on_home": True,
        "show_in_gallery": True,
        "home_sort_order": 4,
        "gallery_sort_order": 4,
    },
    {
        "slug": "sofia-laurent",
        "client_name": "Sofia Laurent",
        "destination_label": "Maldives",
        "trip_type": "Wellness Retreat",
        "quote": "A week of complete serenity. Every detail anticipated before we even thought to ask.",
        "portrait_url": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.1.0&auto=format&fit=crop&w=400&q=80",
        "show_on_home": True,
        "show_in_gallery": True,
        "home_sort_order": 5,
        "gallery_sort_order": 5,
    },
    {
        "slug": "david-emma-wright",
        "client_name": "David & Emma Wright",
        "destination_label": "Japan",
        "trip_type": "Cultural Discovery",
        "quote": "Impossible restaurants, private guides, and a pace that felt entirely our own.",
        "portrait_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.1.0&auto=format&fit=crop&w=400&q=80",
        "show_on_home": True,
        "show_in_gallery": True,
        "home_sort_order": 6,
        "gallery_sort_order": 6,
    },
]

GALLERY_MOMENTS: list[dict] = []


def slugify_media(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:200] or "media"


def get_or_create_media(
    session,
    *,
    slug: str,
    url: str,
    alt_text: str,
    usage: str,
) -> MediaAsset:
    existing = session.scalar(select(MediaAsset).where(MediaAsset.slug == slug))
    if existing:
        return existing

    asset = MediaAsset(
        slug=slug,
        url=url,
        alt_text=alt_text,
        mime_type="image/jpeg",
        source="external",
        usage=usage,
    )
    session.add(asset)
    session.flush()
    return asset


def seed_story(session, payload: dict) -> str:
    slug = payload["slug"]
    existing = session.scalar(select(ClientStory).where(ClientStory.slug == slug))
    if existing:
        return f"skip {slug}"

    portrait_id = None

    if payload.get("portrait_url"):
        media = get_or_create_media(
            session,
            slug=f"client-story-{slug}-portrait",
            url=payload["portrait_url"],
            alt_text=payload.get("client_name", slug),
            usage="client-story",
        )
        portrait_id = media.id

    story = ClientStory(
        slug=slug,
        client_name=payload["client_name"],
        destination_label=payload.get("destination_label"),
        trip_type=payload.get("trip_type"),
        quote=payload.get("quote"),
        title=payload.get("title"),
        caption=payload.get("caption"),
        portrait_media_id=portrait_id,
        show_on_home=bool(payload.get("show_on_home", False)),
        show_in_gallery=bool(payload.get("show_in_gallery", False)),
        is_featured_in_gallery=bool(payload.get("is_featured_in_gallery", False)),
        home_sort_order=payload.get("home_sort_order"),
        gallery_sort_order=payload.get("gallery_sort_order"),
        is_published=bool(payload.get("is_published", False)),
    )
    session.add(story)
    session.flush()
    return f"created {slug}"


def main() -> None:
    results: list[str] = []
    with SessionLocal() as session:
        for item in TESTIMONIALS:
            results.append(seed_story(session, item))
        for item in GALLERY_MOMENTS:
            results.append(seed_story(session, item))
        session.commit()

    for line in results:
        print(line)
    print("client stories seed complete.")


if __name__ == "__main__":
    main()
