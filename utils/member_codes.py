"""Deterministic member / inquiry reference codes for website leads."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from models.submissions import FormSubmission

IST = ZoneInfo("Asia/Kolkata")


def member_code_from_phone(phone: str | None) -> str:
    digits = "".join(ch for ch in (phone or "") if ch.isdigit())
    if len(digits) >= 10:
        tail = digits[-10:]
    elif digits:
        tail = digits.zfill(10)
    else:
        return "TRG-0000000000"
    return f"TRG-{tail}"


def _submission_created_at(submission: FormSubmission) -> datetime:
    created = submission.created_at
    if created is None:
        return datetime.now(timezone.utc)
    if created.tzinfo is None:
        return created.replace(tzinfo=timezone.utc)
    return created


def _ist_day_bounds_utc(created: datetime) -> tuple[datetime, datetime]:
    local = created.astimezone(IST)
    day_start_local = local.replace(hour=0, minute=0, second=0, microsecond=0)
    day_end_local = day_start_local + timedelta(days=1)
    return (
        day_start_local.astimezone(timezone.utc),
        day_end_local.astimezone(timezone.utc),
    )


def inquiry_code_from_submission(db: Session, submission: FormSubmission) -> str:
    """Return a human-readable inquiry id, e.g. INQ-050726-001."""
    created = _submission_created_at(submission)
    date_part = created.astimezone(IST).strftime("%d%m%y")
    day_start_utc, day_end_utc = _ist_day_bounds_utc(created)

    sequence = db.scalar(
        select(func.count())
        .select_from(FormSubmission)
        .where(
            FormSubmission.created_at >= day_start_utc,
            FormSubmission.created_at < day_end_utc,
        )
    )
    return f"INQ-{date_part}-{max(sequence or 0, 1):03d}"


def assign_submission_inquiry_code(db: Session, submission: FormSubmission) -> str:
    payload = dict(submission.payload or {})
    inquiry_code = inquiry_code_from_submission(db, submission)
    payload["inquiry_code"] = inquiry_code
    submission.payload = payload
    return inquiry_code
