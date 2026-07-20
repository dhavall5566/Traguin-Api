"""Mumbai HQ working-hours helpers (IST, Mon–Sat 09:00–19:00)."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")
WORKDAY_START_HOUR = 9
WORKDAY_END_HOUR = 19  # exclusive — window is [09:00, 19:00)

ACCEPT_WINDOW_WORKING_MINUTES = 15


def _to_ist(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(IST)


def _is_working_weekday(local: datetime) -> bool:
    return local.weekday() != 6  # Sunday off


def _minutes_into_day(local: datetime) -> int:
    return local.hour * 60 + local.minute


def is_working_moment(dt: datetime) -> bool:
    local = _to_ist(dt)
    if not _is_working_weekday(local):
        return False
    mins = _minutes_into_day(local)
    return WORKDAY_START_HOUR * 60 <= mins < WORKDAY_END_HOUR * 60


def working_minutes_between(start: datetime, end: datetime) -> int:
    """
    Count elapsed working minutes between two instants.
    The clock pauses outside Mon–Sat 09:00–19:00 IST.
    """
    if end <= start:
        return 0

    start_ist = _to_ist(start)
    end_ist = _to_ist(end)
    total = 0
    cursor = start_ist

    while cursor < end_ist:
        if not _is_working_weekday(cursor):
            cursor = (cursor + timedelta(days=1)).replace(
                hour=WORKDAY_START_HOUR, minute=0, second=0, microsecond=0
            )
            continue

        day_start = cursor.replace(
            hour=WORKDAY_START_HOUR, minute=0, second=0, microsecond=0
        )
        day_end = cursor.replace(
            hour=WORKDAY_END_HOUR, minute=0, second=0, microsecond=0
        )

        if cursor < day_start:
            cursor = day_start

        if cursor >= day_end:
            cursor = (cursor + timedelta(days=1)).replace(
                hour=WORKDAY_START_HOUR, minute=0, second=0, microsecond=0
            )
            continue

        segment_end = min(end_ist, day_end)
        if segment_end > cursor:
            total += int((segment_end - cursor).total_seconds() // 60)
        cursor = segment_end

        if cursor >= end_ist:
            break

        cursor = (cursor + timedelta(days=1)).replace(
            hour=WORKDAY_START_HOUR, minute=0, second=0, microsecond=0
        )

    return total


def working_minutes_remaining(anchor: datetime, *, limit: int, now: datetime | None = None) -> int:
    when = now or datetime.now(timezone.utc)
    elapsed = working_minutes_between(anchor, when)
    return max(0, limit - elapsed)
