#!/usr/bin/env python3
"""Create crm.agency_lead_mail_settings and agency_lead_mail_recipients tables."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import models.crm.lead_mail_settings  # noqa: F401
from database import crm_engine
from models.crm.lead_mail_settings import AgencyLeadMailRecipient, AgencyLeadMailSettings


def main() -> None:
    AgencyLeadMailSettings.__table__.create(bind=crm_engine, checkfirst=True)
    AgencyLeadMailRecipient.__table__.create(bind=crm_engine, checkfirst=True)
    print("  crm.agency_lead_mail_settings + agency_lead_mail_recipients tables ready")


if __name__ == "__main__":
    main()
