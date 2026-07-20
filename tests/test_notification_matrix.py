"""Tests for notification matrix routing."""

from __future__ import annotations

from services.notification_matrix import (
    MATRIX_EVENT_AUDIENCES,
    STATUS_TO_MATRIX_EVENT,
    matrix_catalog,
    matrix_event_for_status,
)


def test_matrix_catalog_matches_spec_events() -> None:
    events = {row["event"] for row in matrix_catalog()}
    assert "new_lead" in events
    assert "assigned_to_rm" in events
    assert "payment_overdue" in events


def test_new_lead_notifies_customer_admin_and_ops() -> None:
    audiences = MATRIX_EVENT_AUDIENCES["new_lead"]
    assert audiences == ("customer", "admin", "ops_head")


def test_pipeline_status_mapping() -> None:
    assert matrix_event_for_status("ITINERARY_SENT") == "itinerary_sent"
    assert matrix_event_for_status("APPROVED") == "quote_approved"
    assert matrix_event_for_status("BOOKED") == "booking_confirmed"
    assert matrix_event_for_status("CLOSED") == "booking_closed"
    assert matrix_event_for_status("CONTACTED") is None
    assert STATUS_TO_MATRIX_EVENT["PROPOSAL_SENT"] == "itinerary_sent"


if __name__ == "__main__":
    test_matrix_catalog_matches_spec_events()
    test_new_lead_notifies_customer_admin_and_ops()
    test_pipeline_status_mapping()
    print("notification_matrix tests passed")
