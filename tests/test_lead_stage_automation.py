from types import SimpleNamespace
from uuid import uuid4

from services.lead_stage_automation import (
    infer_pipeline_stage_from_signals,
    target_stage_for_activity_type,
)


def _lead(**kwargs):
    defaults = {
        "status": "NEW",
        "assigned_to_id": None,
        "assignment_status": None,
        "proposal_sent_at": None,
        "activities": [],
        "followups": [],
    }
    defaults.update(kwargs)
    return SimpleNamespace(**defaults)


def test_contact_activity_targets_contacted():
    assert target_stage_for_activity_type("PHONE") == "CONTACTED"
    assert target_stage_for_activity_type("EMAIL") == "CONTACTED"


def test_infer_stage_from_contact_activity():
    lead = _lead(
        activities=[SimpleNamespace(type="PHONE", description="Called customer")],
    )
    assert infer_pipeline_stage_from_signals(lead) == "CONTACTED"


def test_infer_stage_from_assignment_acceptance():
    user_id = uuid4()
    lead = _lead(
        assigned_to_id=user_id,
        assignment_status="ACCEPTED",
    )
    assert infer_pipeline_stage_from_signals(lead) == "ACCEPTED"


def test_infer_stage_from_stage_change_history():
    lead = _lead(
        status="NEW",
        activities=[
            SimpleNamespace(
                type="STAGE_CHANGE",
                description="Moved stage from NEW to ITINERARY_SENT",
            )
        ],
    )
    assert infer_pipeline_stage_from_signals(lead) == "ITINERARY_SENT"


def test_infer_stage_keeps_furthest_signal():
    user_id = uuid4()
    lead = _lead(
        assigned_to_id=user_id,
        assignment_status="ACCEPTED",
        activities=[SimpleNamespace(type="PHONE", description="Called customer")],
    )
    assert infer_pipeline_stage_from_signals(lead) == "CONTACTED"
