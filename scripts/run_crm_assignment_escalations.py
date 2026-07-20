#!/usr/bin/env python3
"""Process RM assignment accept timers and escalations. Run every 5–15 min via cron."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.lead_assignment_escalation import run_assignment_escalations_job


if __name__ == "__main__":
    run_assignment_escalations_job()
