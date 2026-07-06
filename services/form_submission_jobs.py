"""Run CRM lead intake after a form submission is persisted."""

from __future__ import annotations

import logging
from uuid import UUID

from database import SessionLocal
from models.submissions import FormSubmission
from services.form_submission_intake import process_form_submission_intake
from services.whatsapp_notifications import notify_team_new_lead_by_id
from utils.db import commit_or_raise

logger = logging.getLogger(__name__)


def run_form_submission_intake(submission_id: UUID) -> None:
    db = SessionLocal()
    try:
        submission = db.get(FormSubmission, submission_id)
        if submission is None:
            logger.warning("form intake skipped: submission %s not found", submission_id)
            return
        lead = process_form_submission_intake(db, submission)
        commit_or_raise(db)
        if lead is not None:
            notify_team_new_lead_by_id(lead.id, event_type="website_lead")
    except Exception:
        db.rollback()
        logger.exception("form intake failed for submission %s", submission_id)
    finally:
        db.close()
