#!/usr/bin/env python3
"""
Sync package price, review count, sold_last_month, and moods from Excel master sheet.

Matches rows by Code + State to packages.slug prefix + destination.
Only updates packages that exist in the database.

Usage:
  python scripts/sync_packages_from_excel.py --dry-run
  python scripts/sync_packages_from_excel.py --excel /path/to/file.xlsx
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import SessionLocal
from models.destinations import Destination
from models.itineraries import Itinerary
from models.packages import Package
from services.packages import merge_package_moods
from services.travel_moods import normalize_travel_mood
from utils.db import commit_or_raise

DEFAULT_EXCEL = Path.home() / "Downloads/Itinerary_Master_With_Traveller_Data_Revised.xlsx"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

STATE_SLUG_ALIASES: dict[str, str] = {
    "dubai": "uae",
    "u.a.e.": "uae",
    "uae": "uae",
    "united arab emirates": "uae",
    "usa": "usa",
    "united states": "usa",
    "united states of america": "usa",
    "south africa": "south-africa",
    "south korea": "south-korea",
    "korea": "south-korea",
    "new zealand": "new-zealand",
    "united kingdom": "united-kingdom",
    "uk": "united-kingdom",
    "bali": "bali",
    "indonesia": "bali",
    "thailand": "thailand",
    "turkey": "turkey",
    "switzerland": "switzerland",
    "singapore": "singapore",
    "malaysia": "malaysia",
    "vietnam": "vietnam",
    "france": "france",
    "italy": "italy",
    "japan": "japan",
    "australia": "australia",
    "himachal": "himachal",
    "himachal pradesh": "himachal",
    "rajasthan": "rajasthan",
    "kerala": "kerala",
    "kashmir": "kashmir",
    "jammu & kashmir": "kashmir",
    "jammu and kashmir": "kashmir",
    "uttarakhand": "uttarakhand",
    "uttaranchal": "uttarakhand",
    "gujarat": "gujarat",
    "maharashtra": "maharashtra",
    "chandigarh": "chandigarh",
    "tripura": "tripura",
}


@dataclass
class ExcelRow:
    code: str
    state: str
    category: str
    price_raw: str
    reviews_raw: str
    sold_raw: str


def _col_letters(cell_ref: str) -> str:
    match = re.match(r"([A-Z]+)", cell_ref)
    if not match:
        return ""
    return match.group(1)


def _col_index(letters: str) -> int:
    index = 0
    for char in letters:
        index = index * 26 + (ord(char) - 64)
    return index


def load_excel_rows(path: Path) -> list[ExcelRow]:
    with zipfile.ZipFile(path) as archive:
        shared_strings: list[str] = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for item in root.findall(".//m:si", NS):
                shared_strings.append("".join(t.text or "" for t in item.findall(".//m:t", NS)))

        sheet = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
        parsed_rows: list[dict[str, str]] = []
        for row in sheet.findall(".//m:sheetData/m:row", NS):
            cells: dict[str, str] = {}
            for cell in row.findall("m:c", NS):
                ref = cell.attrib.get("r", "")
                col = _col_letters(ref)
                if not col:
                    continue
                cell_type = cell.attrib.get("t")
                value_el = cell.find("m:v", NS)
                value = value_el.text if value_el is not None else ""
                if cell_type == "s" and value:
                    value = shared_strings[int(value)]
                cells[col] = str(value).strip()
            parsed_rows.append(cells)

    if not parsed_rows:
        return []

    all_cols = sorted({col for row in parsed_rows for col in row}, key=_col_index)
    header = {parsed_rows[0].get(col, ""): col for col in all_cols}

    rows: list[ExcelRow] = []
    for raw in parsed_rows[1:]:
        record = {name: raw.get(col, "").strip() for name, col in header.items()}
        code = record.get("Code", "").upper().replace(" ", "")
        if not code:
            continue
        rows.append(
            ExcelRow(
                code=code,
                state=record.get("State", ""),
                category=record.get("Category", ""),
                price_raw=record.get("Price", ""),
                reviews_raw=record.get("Reviews", ""),
                sold_raw=record.get("Last 3 Months Opted", ""),
            )
        )
    return rows


def normalize_state(value: str) -> str:
    return " ".join(value.strip().lower().split())


def state_to_slug_guess(state: str) -> str:
    normalized = normalize_state(state)
    return (
        normalized.replace(" & ", "-")
        .replace(" and ", "-")
        .replace(" ", "-")
    )


def resolve_destination(destinations: list[Destination], state: str) -> Destination | None:
    normalized = normalize_state(state)
    if not normalized:
        return None

    slug_guess = STATE_SLUG_ALIASES.get(normalized, state_to_slug_guess(state))

    for destination in destinations:
        if destination.slug == slug_guess:
            return destination

    for destination in destinations:
        if normalize_state(destination.name) == normalized:
            return destination

    for destination in destinations:
        if destination.country and normalize_state(destination.country) == normalized:
            return destination

    for destination in destinations:
        if normalized in normalize_state(destination.name):
            return destination

    return None


def parse_price(raw: str) -> int | None:
    digits = re.sub(r"[^\d]", "", raw or "")
    if not digits:
        return None
    return int(digits)


def parse_non_negative_int(raw: str) -> int | None:
    text = str(raw or "").strip()
    if not text:
        return None
    try:
        value = int(float(text))
    except ValueError:
        return None
    return max(value, 0)


def category_to_mood(category: str) -> str | None:
    return normalize_travel_mood(category)


def find_package(
    packages_by_dest: dict[str, list[Package]],
    *,
    code: str,
    destination_id: str,
) -> Package | None:
    slug_prefix = f"{code.lower()}-"
    candidates = [
        package
        for package in packages_by_dest.get(destination_id, [])
        if package.slug.lower().startswith(slug_prefix)
    ]
    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        return None
    return None


def sync_packages(*, excel_path: Path, dry_run: bool) -> int:
    rows = load_excel_rows(excel_path)
    print(f"Loaded {len(rows)} Excel rows from {excel_path}")

    stats = defaultdict(int)

    with SessionLocal() as db:
        destinations = list(db.scalars(select(Destination)).all())
        packages = list(
            db.scalars(
                select(Package).options(selectinload(Package.moods))
            ).all()
        )
        itineraries = list(db.scalars(select(Itinerary)).all())
        itinerary_by_package = {
            str(itinerary.package_id): itinerary
            for itinerary in itineraries
            if itinerary.package_id is not None
        }

        packages_by_dest: dict[str, list[Package]] = defaultdict(list)
        for package in packages:
            packages_by_dest[str(package.destination_id)].append(package)

        for row in rows:
            destination = resolve_destination(destinations, row.state)
            if destination is None:
                stats["skipped_no_destination"] += 1
                continue

            package = find_package(
                packages_by_dest,
                code=row.code,
                destination_id=str(destination.id),
            )
            if package is None:
                stats["skipped_no_package"] += 1
                continue

            itinerary = itinerary_by_package.get(str(package.id))
            if itinerary is None:
                stats["skipped_no_itinerary"] += 1
                continue

            price = parse_price(row.price_raw)
            reviews = parse_non_negative_int(row.reviews_raw)
            sold = parse_non_negative_int(row.sold_raw)
            mood = category_to_mood(row.category)

            if price is None:
                stats["skipped_bad_price"] += 1
                continue

            existing_moods = [m.mood for m in package.moods]
            merged_preview = existing_moods[:]
            if mood and mood not in merged_preview:
                merged_preview.append(mood)

            print(
                f"{'[dry-run] ' if dry_run else ''}UPDATE {row.code} @ {destination.slug} "
                f"({package.slug}): price={price}, reviews={reviews}, sold={sold}, "
                f"mood+={mood or '—'} -> {merged_preview}"
            )

            if not dry_run:
                package.price = price
                package.sold_last_month = sold if sold is not None else 0
                itinerary.starting_price = price
                if reviews is not None:
                    itinerary.review_count = reviews
                if mood:
                    merge_package_moods(db, package, [mood])

            stats["updated"] += 1

        if not dry_run:
            commit_or_raise(db)
            print("\nCommitted changes.")
        else:
            print("\nDry run — no changes written.")

    print("\nSummary:")
    for key in sorted(stats):
        print(f"  {key}: {stats[key]}")
    return 0 if stats["updated"] or stats["skipped_no_package"] else 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync package fields from Excel master sheet.")
    parser.add_argument(
        "--excel",
        type=Path,
        default=DEFAULT_EXCEL,
        help=f"Path to Excel file (default: {DEFAULT_EXCEL})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned updates without writing to the database",
    )
    args = parser.parse_args()

    if not args.excel.exists():
        print(f"Excel file not found: {args.excel}", file=sys.stderr)
        sys.exit(1)

    sys.exit(sync_packages(excel_path=args.excel, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
