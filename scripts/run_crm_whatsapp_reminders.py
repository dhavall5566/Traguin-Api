#!/usr/bin/env python3
"""Send CRM WhatsApp reminders (follow-ups due/overdue, stuck proposals). Run daily via cron."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.whatsapp_notifications import run_scheduled_reminders_job


if __name__ == "__main__":
    run_scheduled_reminders_job()
