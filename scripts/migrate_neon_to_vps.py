#!/usr/bin/env python3
"""
Copy cms + crm schemas from Neon/source to split VPS databases (public schema on each).

Run from api/:
  SOURCE_DATABASE_URL='postgresql://...neon...' python scripts/migrate_neon_to_vps.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import MetaData, create_engine, inspect, text
from sqlalchemy.dialects.postgresql import insert

SOURCE_URL = os.environ.get("SOURCE_DATABASE_URL", "")
CMS_TARGET_URL = os.environ.get(
    "CMS_TARGET_URL",
    "postgresql://traguincms:WszAYrrwkGhRKrNP@195.35.7.208:5432/traguincms",
)
CRM_TARGET_URL = os.environ.get(
    "CRM_TARGET_URL",
    "postgresql://traguincrm:TS88DmHrL4ekZnSX@195.35.7.208:5432/traguincrm",
)

BATCH_SIZE = 500


def normalize_url(url: str) -> str:
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    if url.startswith("postgresql://") and "+psycopg2" not in url:
        url = url.replace("postgresql://", "postgresql+psycopg2://", 1)
    return url


def load_source_url() -> str:
    if SOURCE_URL:
        return normalize_url(SOURCE_URL)
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.is_file():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("DATABASE_URL=") and "neon" in line.lower():
                return normalize_url(line.split("=", 1)[1].strip().strip('"'))
    raise SystemExit("Set SOURCE_DATABASE_URL to the Neon unified database URL.")


def wipe_public_schema(target_engine) -> None:
    with target_engine.begin() as conn:
        conn.execute(
            text(
                """
                DO $$ DECLARE r RECORD;
                BEGIN
                  FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
                    EXECUTE 'DROP TABLE IF EXISTS public.' || quote_ident(r.tablename) || ' CASCADE';
                  END LOOP;
                END $$;
                """
            )
        )


def copy_schema(source_engine, target_engine, source_schema: str) -> None:
    from sqlalchemy.schema import ForeignKeyConstraint

    print(f"  → logical schema {source_schema} → public on target")
    source_metadata = MetaData(schema=source_schema)
    source_metadata.reflect(bind=source_engine, schema=source_schema, views=False)
    source_tables = source_metadata.sorted_tables
    print(f"    tables: {len(source_tables)}")

    target_metadata = MetaData()
    for table in source_tables:
        copied = table.to_metadata(target_metadata, schema=None)
        for constraint in list(copied.constraints):
            if isinstance(constraint, ForeignKeyConstraint):
                copied.constraints.discard(constraint)

    wipe_public_schema(target_engine)
    target_metadata.create_all(bind=target_engine, checkfirst=True)

    with source_engine.connect() as source_conn:
        for source_table in source_tables:
            target_table = target_metadata.tables[source_table.name]
            total = source_conn.execute(
                text(f'SELECT COUNT(*) FROM "{source_schema}"."{source_table.name}"')
            ).scalar_one()
            if total == 0:
                print(f"    {source_table.name}: 0 rows")
                continue

            copied = 0
            offset = 0
            while offset < total:
                rows = (
                    source_conn.execute(source_table.select().limit(BATCH_SIZE).offset(offset))
                    .mappings()
                    .all()
                )
                if not rows:
                    break
                payload = [dict(row) for row in rows]
                with target_engine.begin() as target_conn:
                    target_conn.execute(insert(target_table), payload)
                copied += len(rows)
                offset += BATCH_SIZE
            print(f"    {source_table.name}: {copied} rows")


def verify(target_engine) -> int:
    return len(inspect(target_engine).get_table_names(schema=None))


def main() -> None:
    source_url = load_source_url()
    cms_url = normalize_url(CMS_TARGET_URL)
    crm_url = normalize_url(CRM_TARGET_URL)

    print("Migrating Traguin database to VPS split instances...")
    print(f"  source: {source_url.split('@')[-1]}")
    print(f"  cms:    {cms_url.split('@')[-1]}")
    print(f"  crm:    {crm_url.split('@')[-1]}")
    print()

    source_engine = create_engine(source_url, pool_pre_ping=True)
    cms_engine = create_engine(cms_url, pool_pre_ping=True)
    crm_engine = create_engine(crm_url, pool_pre_ping=True)

    copy_schema(source_engine, cms_engine, "cms")
    copy_schema(source_engine, crm_engine, "crm")

    cms_tables = verify(cms_engine)
    crm_tables = verify(crm_engine)
    print()
    print(f"Done — traguincms public: {cms_tables} tables, traguincrm public: {crm_tables} tables")


if __name__ == "__main__":
    main()
