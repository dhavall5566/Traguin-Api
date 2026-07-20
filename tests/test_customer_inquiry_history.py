"""Tests for customer inquiry history aggregation."""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from utils.lead_pipeline import resolve_pipeline_stage

ACTIVE = {"NEW", "ASSIGNED", "ACCEPTED", "CONTACTED", "ITINERARY_SENT", "APPROVED", "QUOTE_SENT"}


class _FakeLead:
    def __init__(self, status: str) -> None:
        self.id = uuid4()
        self.lead_code = "TEMP202607100001-WEB"
        self.title = "Kerala trip"
        self.status = status
        self.source = "Website"
        self.travel_destination = "Kerala"
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        self.customer_id = None
        self.phone = "919999999999"
        self.email = "guest@example.com"


def test_active_and_not_converted_classification() -> None:
    active = _FakeLead("CONTACTED")
    dumped = _FakeLead("DUMP_LEAD")
    assert resolve_pipeline_stage(active.status) in ACTIVE
    assert resolve_pipeline_stage(dumped.status) == "DUMP_LEAD"


if __name__ == "__main__":
    test_active_and_not_converted_classification()
    print("customer_inquiry_history tests passed")
