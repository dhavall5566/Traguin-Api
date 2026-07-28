#!/usr/bin/env python3
"""P1: org hierarchy, approvals, SLA settings, user/lead org fields."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text
from database import CRM_SCHEMA, _physical_schema, crm_engine

def _ref(name: str) -> str:
    p = _physical_schema(CRM_SCHEMA)
    return f"{p}.{name}" if p else name

def main() -> None:
    agencies, users, leads = _ref("agencies"), _ref("users"), _ref("leads")
    org_units = _ref("org_units")
    approvals = _ref("approval_requests")
    sla = _ref("agency_sla_settings")

    with crm_engine.begin() as conn:
        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {org_units} (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                agency_id UUID NOT NULL REFERENCES {agencies}(id) ON DELETE CASCADE,
                parent_id UUID REFERENCES {org_units}(id) ON DELETE SET NULL,
                name VARCHAR(255) NOT NULL,
                unit_type VARCHAR(32) NOT NULL DEFAULT 'BRANCH',
                is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
                created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
                updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
            )"""))
        conn.execute(text(f"CREATE INDEX IF NOT EXISTS ix_org_units_agency_id ON {org_units}(agency_id)"))
        conn.execute(text(f"CREATE INDEX IF NOT EXISTS ix_org_units_parent_id ON {org_units}(parent_id)"))

        conn.execute(text(f"""
            ALTER TABLE {users}
            ADD COLUMN IF NOT EXISTS org_unit_id UUID REFERENCES {org_units}(id) ON DELETE SET NULL"""))
        conn.execute(text(f"""
            ALTER TABLE {users}
            ADD COLUMN IF NOT EXISTS manager_id UUID REFERENCES {users}(id) ON DELETE SET NULL"""))
        conn.execute(text(f"CREATE INDEX IF NOT EXISTS ix_users_org_unit_id ON {users}(org_unit_id)"))

        conn.execute(text(f"""
            ALTER TABLE {leads}
            ADD COLUMN IF NOT EXISTS org_unit_id UUID REFERENCES {org_units}(id) ON DELETE SET NULL"""))
        conn.execute(text(f"CREATE INDEX IF NOT EXISTS ix_leads_org_unit_id ON {leads}(org_unit_id)"))

        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {approvals} (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                agency_id UUID NOT NULL REFERENCES {agencies}(id) ON DELETE CASCADE,
                request_type VARCHAR(64) NOT NULL,
                entity_type VARCHAR(64) NOT NULL,
                entity_id UUID NOT NULL,
                title VARCHAR(512) NOT NULL,
                payload JSONB NOT NULL DEFAULT '{{}}'::jsonb,
                status VARCHAR(32) NOT NULL DEFAULT 'PENDING',
                requested_by_id UUID NOT NULL REFERENCES {users}(id) ON DELETE CASCADE,
                reviewed_by_id UUID REFERENCES {users}(id) ON DELETE SET NULL,
                review_note TEXT,
                created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
                reviewed_at TIMESTAMPTZ
            )"""))
        conn.execute(text(f"""
            CREATE INDEX IF NOT EXISTS ix_approval_requests_agency_status
            ON {approvals}(agency_id, status)"""))

        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {sla} (
                agency_id UUID PRIMARY KEY REFERENCES {agencies}(id) ON DELETE CASCADE,
                lead_response_minutes INTEGER NOT NULL DEFAULT 15,
                followup_reminder_minutes INTEGER NOT NULL DEFAULT 30,
                proposal_sla_hours INTEGER NOT NULL DEFAULT 48,
                escalation_enabled BOOLEAN NOT NULL DEFAULT TRUE,
                updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
            )"""))

    print("migrate_crm_enterprise_p1 complete.")

if __name__ == "__main__":
    main()
