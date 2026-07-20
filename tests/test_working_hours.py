"""Tests for IST working-hours calculations."""

from __future__ import annotations

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from utils.working_hours import is_working_moment, working_minutes_between

IST = ZoneInfo("Asia/Kolkata")


def _ist(y, m, d, h, mi=0) -> datetime:
    return datetime(y, m, d, h, mi, tzinfo=IST).astimezone(timezone.utc)


def test_sunday_does_not_count() -> None:
    start = _ist(2026, 7, 12, 10)  # Sunday
    end = _ist(2026, 7, 12, 12)
    assert working_minutes_between(start, end) == 0
    assert not is_working_moment(start)


def test_weekday_window_counts_minutes() -> None:
    start = _ist(2026, 7, 10, 10, 0)  # Friday
    end = _ist(2026, 7, 10, 10, 30)
    assert working_minutes_between(start, end) == 30


def test_pauses_outside_business_hours() -> None:
    start = _ist(2026, 7, 10, 18, 30)  # Friday evening
    end = _ist(2026, 7, 11, 10, 0)  # Saturday morning
    # 30 min Fri + 60 min Sat
    assert working_minutes_between(start, end) == 90


if __name__ == "__main__":
    test_sunday_does_not_count()
    test_weekday_window_counts_minutes()
    test_pauses_outside_business_hours()
    print("working_hours tests passed")
