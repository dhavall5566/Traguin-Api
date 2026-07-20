#!/usr/bin/env python3
"""Create agency_whatsapp_template_settings for per-agency WhatsApp template configuration."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import models.crm.whatsapp_template_settings  # noqa: F401
from database import crm_engine
from models.crm.whatsapp_template_settings import AgencyWhatsAppTemplateSettings


def main() -> None:
    AgencyWhatsAppTemplateSettings.__table__.create(bind=crm_engine, checkfirst=True)
    print("  agency_whatsapp_template_settings table ready")


if __name__ == "__main__":
    main()
