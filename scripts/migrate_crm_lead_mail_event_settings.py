#!/usr/bin/env python3
"""Add per-event columns and recipient event_type for lead mail settings."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import inspect, text

import models.crm.lead_mail_settings  # noqa: F401
from database import CRM_SCHEMA, _physical_schema, crm_engine
from models.crm.lead_mail_settings import AgencyLeadMailRecipient, AgencyLeadMailSettings


def _physical() -> str | None:
    return _physical_schema(CRM_SCHEMA)


def _table_ref(table_name: str) -> str:
    physical = _physical()
    return f"{physical}.{table_name}" if physical else table_name


def _table_exists(table_name: str) -> bool:
    inspector = inspect(crm_engine)
    return table_name in inspector.get_table_names(schema=_physical())


def _column_names(table_name: str) -> set[str]:
    if not _table_exists(table_name):
        return set()
    inspector = inspect(crm_engine)
    return {column["name"] for column in inspector.get_columns(table_name, schema=_physical())}


def main() -> None:
    AgencyLeadMailSettings.__table__.create(bind=crm_engine, checkfirst=True)
    AgencyLeadMailRecipient.__table__.create(bind=crm_engine, checkfirst=True)

    settings_table = _table_ref("agency_lead_mail_settings")
    settings_columns = _column_names("agency_lead_mail_settings")
    with crm_engine.begin() as conn:
        if "website_lead_enabled" not in settings_columns:
            conn.execute(
                text(
                    f"ALTER TABLE {settings_table} "
                    "ADD COLUMN website_lead_enabled BOOLEAN NOT NULL DEFAULT TRUE"
                )
            )
        if "crm_lead_enabled" not in settings_columns:
            conn.execute(
                text(
                    f"ALTER TABLE {settings_table} "
                    "ADD COLUMN crm_lead_enabled BOOLEAN NOT NULL DEFAULT TRUE"
                )
            )
        if "status_change_enabled" not in settings_columns:
            conn.execute(
                text(
                    f"ALTER TABLE {settings_table} "
                    "ADD COLUMN status_change_enabled BOOLEAN NOT NULL DEFAULT FALSE"
                )
            )
        if _table_exists("agency_lead_mail_settings") and "enabled" in _column_names(
            "agency_lead_mail_settings"
        ):
            conn.execute(
                text(
                    f"UPDATE {settings_table} "
                    "SET website_lead_enabled = enabled, crm_lead_enabled = enabled "
                    "WHERE enabled = FALSE"
                )
            )

    recipients_table = _table_ref("agency_lead_mail_recipients")
    recipient_columns = _column_names("agency_lead_mail_recipients")
    with crm_engine.begin() as conn:
        if "event_type" not in recipient_columns:
            conn.execute(
                text(
                    f"ALTER TABLE {recipients_table} "
                    "ADD COLUMN event_type VARCHAR(32) NOT NULL DEFAULT 'website_lead'"
                )
            )
            conn.execute(
                text(
                    f"INSERT INTO {recipients_table} "
                    "(id, settings_id, user_id, event_type, created_at) "
                    "SELECT gen_random_uuid(), settings_id, user_id, 'crm_lead', created_at "
                    f"FROM {recipients_table} "
                    "WHERE event_type = 'website_lead'"
                )
            )

        conn.execute(
            text(
                f"ALTER TABLE {recipients_table} "
                "DROP CONSTRAINT IF EXISTS uq_lead_mail_recipient_settings_user"
            )
        )
        conn.execute(
            text(
                f"ALTER TABLE {recipients_table} "
                "DROP CONSTRAINT IF EXISTS uq_lead_mail_recipient_settings_user_event"
            )
        )
        conn.execute(
            text(
                f"ALTER TABLE {recipients_table} "
                "ADD CONSTRAINT uq_lead_mail_recipient_settings_user_event "
                "UNIQUE (settings_id, user_id, event_type)"
            )
        )

    print("  crm lead mail event settings migration complete")


if __name__ == "__main__":
    main()
