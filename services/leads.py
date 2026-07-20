from uuid import UUID

from sqlalchemy.orm import Session, joinedload

from models.crm.leads import Lead, LeadActivity, LeadFollowup, LeadNote
from schemas.crm.lead import LeadFollowupRead, LeadListRead, LeadRead
from services.lead_codes import ensure_lead_code


def lead_query_with_nested(db: Session):
    return db.query(Lead).options(
        joinedload(Lead.notes),
        joinedload(Lead.activities),
        joinedload(Lead.followups),
    )


def lead_to_read(db: Session, lead: Lead) -> LeadRead:
    if not lead.lead_code:
        ensure_lead_code(db, lead)
    read = LeadRead.model_validate(lead)
    if not (read.last_name or "").strip():
        return read.model_copy(update={"last_name": "Visitor"})
    return read


def lead_to_list_read(_db: Session, lead: Lead) -> LeadListRead:
    """Read-only list row — never assign codes or flush here (list would be O(n) writes)."""
    read = LeadListRead.model_validate(lead)
    if not (read.last_name or "").strip():
        return read.model_copy(update={"last_name": "Visitor"})
    return read


def list_pending_followups_for_agency(db: Session, agency_id: UUID) -> list[LeadFollowupRead]:
    rows = (
        db.query(LeadFollowup)
        .join(Lead, LeadFollowup.lead_id == Lead.id)
        .filter(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            LeadFollowup.status == "PENDING",
        )
        .order_by(LeadFollowup.scheduled_at.asc())
        .limit(500)
        .all()
    )
    return [LeadFollowupRead.model_validate(row) for row in rows]


def add_lead_children(
    db: Session,
    lead: Lead,
    *,
    created_by_id: UUID,
    notes: list,
    activities: list,
    followups: list,
) -> None:
    for note in notes:
        db.add(
            LeadNote(
                lead_id=lead.id,
                content=note.content,
                created_by_id=created_by_id,
            )
        )
    for activity in activities:
        db.add(
            LeadActivity(
                lead_id=lead.id,
                type=activity.type,
                description=activity.description,
                created_by_id=created_by_id,
            )
        )
    for followup in followups:
        db.add(
            LeadFollowup(
                lead_id=lead.id,
                scheduled_at=followup.scheduled_at,
                status=followup.status,
                notes=followup.notes,
                created_by_id=created_by_id,
            )
        )


def get_lead_for_agency(
    db: Session,
    lead_id: UUID,
    agency_id: UUID,
    *,
    include_deleted: bool = False,
) -> Lead | None:
    query = lead_query_with_nested(db).filter(Lead.id == lead_id, Lead.agency_id == agency_id)
    if not include_deleted:
        query = query.filter(Lead.is_deleted.is_(False))
    return query.one_or_none()
