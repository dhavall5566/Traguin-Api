#!/usr/bin/env python3
"""Import packages from JSON files (no images, skip if serial_code/slug exists).

Examples:
  python scripts/import_packages_from_json.py --dir data/packages/domestic
  python scripts/import_packages_from_json.py --glob "data/packages/domestic/AP-*.json"
  python scripts/import_packages_from_json.py data/packages/domestic/AP-001.json
  python scripts/import_packages_from_json.py --dir data/packages/domestic --dry-run
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from sqlalchemy import select

_SCRIPTS_DIR = Path(__file__).resolve().parent
_API_DIR = _SCRIPTS_DIR.parent
if str(_API_DIR) not in sys.path:
    sys.path.insert(0, str(_API_DIR))
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from database import SessionLocal
from models.destinations import Destination
from package_json_io import load_package_import_file, package_import_to_models
from services.package_insert import insert_package_if_missing


def _collect_paths(args: argparse.Namespace) -> list[Path]:
    paths: set[Path] = set()
    for raw in args.files:
        path = Path(raw)
        if not path.is_absolute():
            path = (_API_DIR / path).resolve()
        paths.add(path)

    if args.glob:
        for match in sorted(_API_DIR.glob(args.glob)):
            if match.suffix.lower() == ".json" and match.is_file():
                paths.add(match.resolve())

    if args.dir:
        dir_path = Path(args.dir)
        if not dir_path.is_absolute():
            dir_path = (_API_DIR / dir_path).resolve()
        if not dir_path.is_dir():
            raise SystemExit(f"Directory not found: {dir_path}")
        for match in sorted(dir_path.rglob("*.json")):
            paths.add(match.resolve())

    return sorted(paths)


def _resolve_destination_id(db, slug: str) -> str:
    destination = db.scalar(select(Destination).where(Destination.slug == slug))
    if destination is None:
        raise RuntimeError(
            f"Destination not found for slug {slug!r}. "
            "Create the destination first or fix destination_slug in the JSON file."
        )
    return str(destination.id)


def main() -> None:
    parser = argparse.ArgumentParser(description="Import CMS packages from JSON files.")
    parser.add_argument("files", nargs="*", help="Explicit JSON file paths")
    parser.add_argument("--dir", help="Import all *.json files under this directory (recursive)")
    parser.add_argument("--glob", help='Glob pattern relative to api/, e.g. "data/packages/domestic/AP-*.json"')
    parser.add_argument("--dry-run", action="store_true", help="Validate JSON only; do not write to DB")
    args = parser.parse_args()

    paths = _collect_paths(args)
    if not paths:
        parser.error("Provide file paths, --dir, or --glob")

    print(f"Found {len(paths)} JSON file(s)")
    if args.dry_run:
        for path in paths:
            payload = load_package_import_file(path)
            serial = payload.package.serial_code or payload.package.slug
            print(
                f"  OK {path.name}: {serial} | {payload.destination_slug} | "
                f"days={len(payload.itinerary.days)} hotels={len(payload.itinerary.hotels)}"
            )
        print("Dry run complete — no database changes.")
        return

    inserted = 0
    skipped = 0
    failed = 0

    with SessionLocal() as db:
        destination_cache: dict[str, str] = {}

        for path in paths:
            print(f"\n--- {path.name} ---")
            try:
                payload = load_package_import_file(path)
                slug = payload.destination_slug
                if slug not in destination_cache:
                    destination_cache[slug] = _resolve_destination_id(db, slug)
                    print(f"Using destination: {slug} ({destination_cache[slug]})")

                package, itinerary = package_import_to_models(payload, destination_cache[slug])
                result = insert_package_if_missing(
                    db,
                    destination_id=destination_cache[slug],
                    package=package,
                    itinerary=itinerary,
                )
                if result is None:
                    skipped += 1
                else:
                    inserted += 1
            except Exception as exc:
                failed += 1
                print(f"Failed {path.name}: {exc}", file=sys.stderr)

    print(f"\nDone. Inserted: {inserted}, Skipped: {skipped}, Failed: {failed}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
