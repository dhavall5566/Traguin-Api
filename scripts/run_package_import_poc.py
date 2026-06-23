#!/usr/bin/env python3
"""Run package PDF import POC from CLI (extract only, or extract + commit).

Usage:
  ./venv/bin/python scripts/run_package_import_poc.py /path/to/brochure.pdf
  ./venv/bin/python scripts/run_package_import_poc.py /path/to/brochure.pdf --commit
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from database import SessionLocal
from services.package_import import run_package_import_extract
from services.package_import_commit import commit_package_import
from services.package_import_mapper import review_to_creates
from schemas.package_import import PackageImportCommitRequest, PackageImportReviewCommit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--commit", action="store_true", help="Write to CMS after extract")
    parser.add_argument("--no-images", action="store_true")
    args = parser.parse_args()

    if not args.pdf.is_file():
        print(f"PDF not found: {args.pdf}", file=sys.stderr)
        return 1

    pdf_bytes = args.pdf.read_bytes()
    db = SessionLocal()
    try:
        result = run_package_import_extract(
            db,
            filename=args.pdf.name,
            file_bytes=pdf_bytes,
            fetch_images=not args.no_images,
        )
        print("=== LLM JSON ===")
        print(json.dumps(result.llm_raw_json, indent=2, ensure_ascii=False))
        print("\n=== Images ===")
        for img in result.images:
            print(f"- {img.place}: {img.url or img.error}")
        if result.warnings:
            print("\n=== Warnings ===")
            for w in result.warnings:
                print(f"- {w}")

        if args.commit:
            review = PackageImportReviewCommit(
                destination=result.extracted.destination,
                package=result.extracted.package,
                itinerary=result.extracted.itinerary,
                gallery_media_ids=[i.media_asset_id for i in result.images if i.media_asset_id],
                hero_media_id=next((i.media_asset_id for i in result.images if i.media_asset_id), None),
            )
            dest, pkg, itin = review_to_creates(review)
            saved = commit_package_import(
                db,
                PackageImportCommitRequest(destination=dest, package=pkg, itinerary=itin),
            )
            print("\n=== Created ===")
            print(saved.model_dump_json(indent=2))
    finally:
        db.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
