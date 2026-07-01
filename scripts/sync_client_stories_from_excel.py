#!/usr/bin/env python3
"""
Upsert client stories from Excel: update quote for existing names, insert new ones.

Excel format (Sheet1):
  - Column "Client Testimonials": name on first line(s), blank line, then review text.

Usage:
  python scripts/sync_client_stories_from_excel.py --dry-run
  python scripts/sync_client_stories_from_excel.py --excel "/path/to/Client Stories.xlsx"
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
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select

from database import SessionLocal
from models.gallery import ClientStory
from utils.db import commit_or_raise

DEFAULT_EXCEL = Path.home() / "Downloads/Client Stories.xlsx"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
TESTIMONIAL_COLUMN = "Client Testimonials"


@dataclass
class StoryRow:
    client_name: str
    quote: str


def _col_letters(cell_ref: str) -> str:
    match = re.match(r"([A-Z]+)", cell_ref)
    return match.group(1) if match else ""


def _col_index(letters: str) -> int:
    index = 0
    for char in letters:
        index = index * 26 + (ord(char) - 64)
    return index


def parse_testimonial_cell(raw: str) -> StoryRow | None:
    text = raw.strip()
    if not text:
        return None

    parts = re.split(r"\n\s*\n", text, maxsplit=1)
    if len(parts) == 2:
        client_name, quote = parts[0].strip(), parts[1].strip()
    else:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        if len(lines) < 2:
            return None
        client_name, quote = lines[0], "\n\n".join(lines[1:])

    if not client_name or not quote:
        return None

    return StoryRow(client_name=client_name, quote=quote)


def load_excel_rows(path: Path) -> list[StoryRow]:
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
    testimonial_col = header.get(TESTIMONIAL_COLUMN)
    if not testimonial_col:
        raise ValueError(f'Column "{TESTIMONIAL_COLUMN}" not found in Excel sheet.')

    rows: list[StoryRow] = []
    for raw in parsed_rows[1:]:
        parsed = parse_testimonial_cell(raw.get(testimonial_col, ""))
        if parsed:
            rows.append(parsed)
    return rows


def match_key(name: str) -> str:
    normalized = re.sub(r"[,\.]", "", name.strip().lower())
    return re.sub(r"\s+", " ", normalized)


def core_key(name: str) -> str:
    normalized = match_key(name)
    normalized = re.sub(r"^(mr|mrs|ms|dr)\s+", "", normalized)
    normalized = re.sub(r"\bsir\b", "", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def name_tokens(name: str) -> list[str]:
    return [token for token in core_key(name).split() if token]


def find_existing_story(
    excel_name: str,
    stories: list[ClientStory],
) -> ClientStory | None:
    excel_full = match_key(excel_name)
    excel_core = core_key(excel_name)
    excel_token_list = name_tokens(excel_name)

    candidates: list[ClientStory] = []
    for story in stories:
        db_full = match_key(story.client_name)
        db_core = core_key(story.client_name)
        db_token_list = name_tokens(story.client_name)

        if excel_full == db_full or excel_core == db_core:
            candidates.append(story)
            continue

        if excel_token_list and db_token_list:
            if excel_token_list[0] == db_token_list[0] and excel_token_list[-1] == db_token_list[-1]:
                candidates.append(story)
                continue

            if len(excel_token_list) >= 2 and len(db_token_list) >= 2:
                if excel_token_list[:2] == db_token_list[:2]:
                    candidates.append(story)
                    continue

        if not excel_core or not db_core:
            continue

        shorter, longer = (
            (excel_core, db_core) if len(excel_core) <= len(db_core) else (db_core, excel_core)
        )
        if len(shorter) >= 4 and longer.startswith(shorter):
            if longer == shorter or longer[len(shorter)] == " ":
                candidates.append(story)

    unique = {story.id: story for story in candidates}
    if len(unique) == 1:
        return next(iter(unique.values()))
    return None


def sync_stories(*, excel_path: Path, dry_run: bool) -> int:
    rows = load_excel_rows(excel_path)
    print(f"Loaded {len(rows)} client stories from {excel_path}")

    stats: dict[str, int] = defaultdict(int)

    with SessionLocal() as db:
        existing_stories = list(db.scalars(select(ClientStory)).all())
        pending_inserts: dict[str, ClientStory] = {}

        for row in rows:
            row_key = match_key(row.client_name)
            matched = find_existing_story(row.client_name, existing_stories)
            if matched is None:
                matched = pending_inserts.get(row_key)
            if matched is None:
                for story in existing_stories:
                    if match_key(story.client_name) == row_key:
                        matched = story
                        break

            if matched is not None:
                previous_quote = (matched.quote or "").strip()
                if previous_quote == row.quote.strip():
                    stats["skipped_unchanged"] += 1
                    print(f"{'[dry-run] ' if dry_run else ''}SKIP unchanged: {matched.client_name}")
                    continue

                print(
                    f"{'[dry-run] ' if dry_run else ''}UPDATE {matched.client_name}: "
                    f"quote ({len(previous_quote)} -> {len(row.quote)} chars)"
                )
                if not dry_run:
                    matched.quote = row.quote.strip()
                stats["updated"] += 1
                continue

            print(
                f"{'[dry-run] ' if dry_run else ''}INSERT {row.client_name}: "
                f"quote ({len(row.quote)} chars)"
            )
            if dry_run:
                pending = SimpleNamespace(
                    id=row_key,
                    client_name=row.client_name,
                    quote=row.quote.strip(),
                )
                existing_stories.append(pending)
                pending_inserts[row_key] = pending
            else:
                story = ClientStory(
                    client_name=row.client_name.strip(),
                    quote=row.quote.strip(),
                    is_published=True,
                )
                db.add(story)
                db.flush()
                existing_stories.append(story)
                pending_inserts[row_key] = story
            stats["inserted"] += 1

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
    parser = argparse.ArgumentParser(description="Upsert client stories from Excel.")
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

    sys.exit(sync_stories(excel_path=args.excel, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
