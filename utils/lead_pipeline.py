"""Lead pipeline stages — Travel CRM Lead Flow Guide v4.2."""

from __future__ import annotations

LEAD_PIPELINE_STATUSES: tuple[str, ...] = (
    "NEW",
    "ASSIGNED",
    "ACCEPTED",
    "CONTACTED",
    "ITINERARY_SENT",
    "APPROVED",
    "QUOTE_SENT",
    "BOOKED",
    "PAID",
    "READY",
    "CLOSED",
    "DUMP_LEAD",
)

ACTIVE_PIPELINE_STATUSES: frozenset[str] = frozenset(
    {
        "NEW",
        "ASSIGNED",
        "ACCEPTED",
        "CONTACTED",
        "ITINERARY_SENT",
        "APPROVED",
        "QUOTE_SENT",
    }
)

LEGACY_STATUS_MAP: dict[str, str] = {
    "PROPOSAL_SENT": "ITINERARY_SENT",
    "NEGOTIATION": "QUOTE_SENT",
    "CONFIRMED": "BOOKED",
    "LOST": "DUMP_LEAD",
}

PIPELINE_STATUS_LABELS: dict[str, str] = {
    "NEW": "New",
    "ASSIGNED": "Assigned",
    "ACCEPTED": "Accepted",
    "CONTACTED": "Contacted",
    "ITINERARY_SENT": "Itinerary Sent",
    "APPROVED": "Customer Approved",
    "QUOTE_SENT": "Quote Sent",
    "BOOKED": "Booked",
    "PAID": "Paid",
    "READY": "Operations",
    "CLOSED": "Closed",
    "DUMP_LEAD": "Dump Lead",
    # Legacy labels (notifications for unmigrated rows)
    "PROPOSAL_SENT": "Itinerary Sent",
    "NEGOTIATION": "Quote Sent",
    "CONFIRMED": "Booked",
    "LOST": "Dump Lead",
}


def resolve_pipeline_stage(status: str | None) -> str:
    raw = (status or "").strip().upper()
    if not raw:
        return "NEW"
    if raw in LEAD_PIPELINE_STATUSES:
        return raw
    return LEGACY_STATUS_MAP.get(raw, "NEW")


def pipeline_status_label(status: str | None) -> str:
    raw = (status or "").strip().upper()
    if not raw:
        return "New"
    return PIPELINE_STATUS_LABELS.get(raw) or PIPELINE_STATUS_LABELS.get(
        resolve_pipeline_stage(raw), raw
    )


PIPELINE_STAGE_INDEX: dict[str, int] = {
    stage: index for index, stage in enumerate(LEAD_PIPELINE_STATUSES)
}

TERMINAL_PIPELINE_STAGES: frozenset[str] = frozenset({"CLOSED", "DUMP_LEAD"})


def pipeline_stage_index(status: str | None) -> int:
    return PIPELINE_STAGE_INDEX.get(resolve_pipeline_stage(status), 0)


def is_pipeline_stage_before(left: str | None, right: str | None) -> bool:
    return pipeline_stage_index(left) < pipeline_stage_index(right)


def max_pipeline_stage(*statuses: str | None) -> str:
    best = "NEW"
    best_index = 0
    for status in statuses:
        if not status:
            continue
        resolved = resolve_pipeline_stage(status)
        index = pipeline_stage_index(resolved)
        if index > best_index:
            best_index = index
            best = resolved
    return best
