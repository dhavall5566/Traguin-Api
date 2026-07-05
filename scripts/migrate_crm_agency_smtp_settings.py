#!/usr/bin/env python3
"""Create crm.agency_smtp_settings for per-agency outbound email configuration."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import models.crm.smtp_settings  # noqa: F401
from database import engine
from models.crm.smtp_settings import AgencySmtpSettings


def main() -> None:
    AgencySmtpSettings.__table__.create(bind=engine, checkfirst=True)
    print("  crm.agency_smtp_settings table ready")


if __name__ == "__main__":
    main()
