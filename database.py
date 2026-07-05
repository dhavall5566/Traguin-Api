from collections.abc import Generator
from dataclasses import dataclass

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from config import settings

CMS_SCHEMA = "cms"
CRM_SCHEMA = "crm"


def _normalize_database_url(value: str) -> str:
    if value.startswith("postgres://"):
        value = value.replace("postgres://", "postgresql://", 1)
    if value.startswith("postgresql://") and "+psycopg2" not in value:
        value = value.replace("postgresql://", "postgresql+psycopg2://", 1)
    return value


def _make_engine(url: str, logical_schema: str):
    engine = create_engine(_normalize_database_url(url), pool_pre_ping=True)
    if settings.is_split_database:
        return engine.execution_options(schema_translate_map={logical_schema: None})
    return engine


cms_engine = _make_engine(settings.resolved_cms_database_url, CMS_SCHEMA)
crm_engine = _make_engine(settings.resolved_crm_database_url, CRM_SCHEMA)


class RoutingSession(Session):
    """Route ORM operations to the CMS or CRM database when they are split."""

    def get_bind(self, mapper=None, clause=None, bind=None, **kwargs):
        if mapper is not None:
            schema = getattr(mapper.persist_selectable, "schema", None)
            if schema == CRM_SCHEMA:
                return crm_engine
        return cms_engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False, class_=RoutingSession)

engine = cms_engine


@dataclass(frozen=True)
class SchemaSummary:
    name: str
    table_count: int
    tables: tuple[str, ...]


def _physical_schema(logical_schema: str) -> str | None:
    if settings.is_split_database:
        return None
    return logical_schema


def get_schema_summary(schema: str) -> SchemaSummary:
    bind = crm_engine if schema == CRM_SCHEMA else cms_engine
    inspector = inspect(bind)
    physical = _physical_schema(schema)
    tables = tuple(sorted(inspector.get_table_names(schema=physical)))
    return SchemaSummary(name=schema, table_count=len(tables), tables=tables)


def get_unified_database_summary() -> dict[str, SchemaSummary]:
    return {
        CMS_SCHEMA: get_schema_summary(CMS_SCHEMA),
        CRM_SCHEMA: get_schema_summary(CRM_SCHEMA),
    }


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_database_connection() -> None:
    with cms_engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    if settings.is_split_database:
        with crm_engine.connect() as connection:
            connection.execute(text("SELECT 1"))


def check_unified_database() -> dict:
    """Verify connectivity and that both CMS and CRM schemas are present."""
    check_database_connection()
    summary = get_unified_database_summary()
    missing: list[str] = []
    for schema_name, info in summary.items():
        if info.table_count == 0:
            missing.append(schema_name)
    if missing:
        mode = "split" if settings.is_split_database else "unified"
        raise SQLAlchemyError(
            f"Database ({mode}) is connected but schema(s) missing or empty: {', '.join(missing)}. "
            "Run: python scripts/init_unified_database.py"
        )
    return {
        "database": "split" if settings.is_split_database else "unified",
        "schemas": {
            name: {"table_count": info.table_count, "tables": list(info.tables)}
            for name, info in summary.items()
        },
    }
