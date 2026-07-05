"""Create all CMS tables defined in SQLAlchemy models."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import inspect, text

import models  # noqa: F401 — register all models with metadata
from database import engine
from models import Base


def create_tables() -> None:
    with engine.begin() as connection:
        # Replace any prior cms schema (e.g. legacy VARCHAR-id tables) with this model set.
        connection.execute(text("DROP SCHEMA IF EXISTS cms CASCADE"))
        connection.execute(text("CREATE SCHEMA cms"))
    Base.metadata.create_all(bind=engine)


def ensure_cms_tables() -> None:
    """Create cms schema and any missing CMS tables without dropping existing data."""
    with engine.begin() as connection:
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS cms"))
    Base.metadata.create_all(bind=engine)


def list_tables() -> list[str]:
    inspector = inspect(engine)
    return sorted(inspector.get_table_names(schema="cms"))


def main() -> None:
    print("Creating CMS tables...")
    create_tables()
    tables = list_tables()
    print(f"\n{len(tables)} tables in cms schema:\n")
    for name in tables:
        print(f"  - {name}")


if __name__ == "__main__":
    main()
