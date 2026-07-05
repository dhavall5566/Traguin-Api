from datetime import datetime, timezone
from unittest.mock import MagicMock
from uuid import uuid4

from utils.member_codes import inquiry_code_from_submission


def test_inquiry_code_uses_ist_date_and_daily_sequence():
    submission = MagicMock()
    submission.created_at = datetime(2026, 7, 5, 18, 30, tzinfo=timezone.utc)
    submission.id = uuid4()

    db = MagicMock()
    db.scalar.return_value = 3

    code = inquiry_code_from_submission(db, submission)

    assert code == "INQ-060726-003"
    db.scalar.assert_called_once()
