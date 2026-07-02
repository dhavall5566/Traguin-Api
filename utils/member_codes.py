"""Deterministic member / inquiry reference codes for website leads."""

from __future__ import annotations

from uuid import UUID


def member_code_from_phone(phone: str | None) -> str:
    digits = "".join(ch for ch in (phone or "") if ch.isdigit())
    if len(digits) >= 10:
        tail = digits[-10:]
    elif digits:
        tail = digits.zfill(10)
    else:
        return "TRG-0000000000"
    return f"TRG-{tail}"


def inquiry_code_from_submission(
    submission_id: UUID,
    *,
    has_itinerary: bool = False,
) -> str:
    prefix = "ITN" if has_itinerary else "INQ"
    short = str(submission_id).replace("-", "")[:8].upper()
    return f"{prefix}-{short}"
