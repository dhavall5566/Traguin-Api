#!/usr/bin/env python3
"""
Link client story portrait_media_id from gallery items matched by client name.

Usage:
  python scripts/link_client_story_portraits_from_gallery.py --dry-run
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from client_name_matching import find_best_name_match, match_key
from database import SessionLocal
from models.gallery import ClientStory, GalleryItem
from utils.db import commit_or_raise

# Story client_name -> exact gallery place label when fuzzy match is insufficient.
STORY_GALLERY_ALIASES: dict[str, str] = {
    match_key("Mrs. Yashvi Shah"): "Mrs. Yashvi Nishant Ranpara",
}


def gallery_media_id(item: GalleryItem):
    if item.media_id:
        return item.media_id
    if item.gallery_media:
        return item.gallery_media[0].media_id
    return None


def link_portraits(*, dry_run: bool) -> int:
    stats: dict[str, int] = defaultdict(int)

    with SessionLocal() as db:
        stories = list(db.scalars(select(ClientStory).order_by(ClientStory.client_name)).all())
        gallery_items = list(
            db.scalars(
                select(GalleryItem)
                .options(selectinload(GalleryItem.gallery_media))
                .where(GalleryItem.is_published.is_(True))
            ).all()
        )
        items_with_media = [item for item in gallery_items if gallery_media_id(item)]

        for story in stories:
            alias_place = STORY_GALLERY_ALIASES.get(match_key(story.client_name))
            match = None
            if alias_place:
                match = next((item for item in items_with_media if item.place == alias_place), None)

            if match is None:
                match = find_best_name_match(
                    story.client_name,
                    items_with_media,
                    get_name=lambda item: item.place,
                )
            if match is None:
                stats["skipped_no_gallery_match"] += 1
                print(f"{'[dry-run] ' if dry_run else ''}SKIP no gallery match: {story.client_name}")
                continue

            media_id = gallery_media_id(match)
            if media_id is None:
                stats["skipped_no_media"] += 1
                continue

            if story.portrait_media_id == media_id:
                stats["skipped_unchanged"] += 1
                continue

            print(
                f"{'[dry-run] ' if dry_run else ''}LINK {story.client_name} "
                f"<- {match.place} (media {media_id})"
            )
            if not dry_run:
                story.portrait_media_id = media_id
                story.show_in_gallery = True
            stats["linked"] += 1

        if not dry_run:
            commit_or_raise(db)
            print("\nCommitted changes.")
        else:
            print("\nDry run — no changes written.")

    print("\nSummary:")
    for key in sorted(stats):
        print(f"  {key}: {stats[key]}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Link client story portraits from gallery items.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    sys.exit(link_portraits(dry_run=args.dry_run))


if __name__ == "__main__":
    main()
