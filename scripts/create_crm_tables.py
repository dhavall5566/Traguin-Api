"""Create CRM tables in the crm schema without modifying cms or public."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import inspect, text

import models.crm  # noqa: F401 — register all CRM models with metadata
from database import engine
from models.crm import CrmBase


def create_crm_tables() -> None:
    with engine.begin() as connection:
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS crm"))
    CrmBase.metadata.create_all(bind=engine)


def list_crm_tables() -> list[str]:
    inspector = inspect(engine)
    return sorted(inspector.get_table_names(schema="crm"))


def list_cms_tables() -> list[str]:
    inspector = inspect(engine)
    return sorted(inspector.get_table_names(schema="cms"))


def main() -> None:
    cms_before = list_cms_tables()
    print(f"CMS tables before: {len(cms_before)}")

    print("Creating CRM tables in crm schema...")
    create_crm_tables()

    crm_tables = list_crm_tables()
    cms_after = list_cms_tables()

    print(f"\n{len(crm_tables)} tables in crm schema:\n")
    for name in crm_tables:
        print(f"  - {name}")

    print(f"\nCMS tables after: {len(cms_after)} (unchanged: {cms_before == cms_after})")


if __name__ == "__main__":
    main()
