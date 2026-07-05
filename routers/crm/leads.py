from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.crm_tenancy import get_include_deleted
from dependencies.pagination import get_pagination
from models.crm.customers import Customer
from models.crm.leads import Lead
from models.crm.tenancy import User
from schemas.crm.lead import (
    LeadActivityCreateNested,
    LeadCreate,
    LeadFollowupRead,
    LeadListRead,
    LeadRead,
    LeadRecentEventRead,
    LeadUpdate,
)
from schemas.pagination import PaginatedResponse
from services.lead_assignee import apply_returning_customer_assignee
from services.lead_codes import assign_lead_code, ensure_lead_code
from services.lead_customers import link_or_create_customer_for_lead
from services.lead_phone_dedup import find_canonical_lead_by_phone, merge_inquiry_into_existing_lead
from services.lead_status import apply_lead_status_transition
from services.leads import (
    add_lead_children,
    get_lead_for_agency,
    lead_query_with_nested,
    lead_to_list_read,
    lead_to_read,
    list_pending_followups_for_agency,
)
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from services.whatsapp_notifications import LeadUpdateNotice, notify_lead_update_by_id, notify_team_new_lead_by_id
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


def _finalize_lead_read(db: Session, lead: Lead) -> LeadRead:
    result = lead_to_read(db, lead)
    commit_or_raise(db)
    return result


@router.get("", response_model=PaginatedResponse[LeadListRead])
def list_leads(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    include_deleted: bool = Depends(get_include_deleted),
):
    limit, offset = pagination
    query = db.query(Lead).filter(Lead.agency_id == agency_id).order_by(Lead.created_at.desc())
    if not include_deleted:
        query = query.filter(Lead.is_deleted.is_(False))
    result = paginate(
        query,
        limit,
        offset,
        transform=lambda lead: lead_to_list_read(db, lead),
    )
    commit_or_raise(db)
    return result


@router.get("/recent", response_model=list[LeadRecentEventRead])
def list_recent_lead_events(
    since: datetime = Query(..., description="ISO timestamp — events after this instant"),
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    from datetime import timezone

    since_utc = since if since.tzinfo else since.replace(tzinfo=timezone.utc)
    if since_utc.tzinfo is not None:
        since_utc = since_utc.astimezone(timezone.utc)

    rows = (
        db.query(Lead)
        .filter(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.updated_at > since_utc,
        )
        .order_by(Lead.updated_at.desc())
        .limit(15)
        .all()
    )
    events: list[LeadRecentEventRead] = []
    for lead in rows:
        ensure_lead_code(db, lead)
        created = lead.created_at
        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)
        kind = "new" if created > since_utc else "returning"
        events.append(
            LeadRecentEventRead(
                id=lead.id,
                lead_code=lead.lead_code,
                title=lead.title,
                first_name=lead.first_name,
                last_name=lead.last_name,
                source=lead.source,
                created_at=lead.created_at,
                updated_at=lead.updated_at,
                kind=kind,
            )
        )
    if events:
        commit_or_raise(db)
    return events


@router.get("/followups/pending", response_model=list[LeadFollowupRead])
def list_pending_lead_followups(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    return list_pending_followups_for_agency(db, agency_id)


@router.get("/{lead_id}", response_model=LeadRead)
def get_lead(
    lead_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    include_deleted: bool = Depends(get_include_deleted),
):
    lead = get_lead_for_agency(db, lead_id, agency_id, include_deleted=include_deleted)
    if lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found.")
    return _finalize_lead_read(db, lead)


@router.post("", response_model=LeadRead)
def create_lead(
    payload: LeadCreate,
    background_tasks: BackgroundTasks,
    response: Response,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    data = payload.model_dump(exclude={"notes", "activities", "followups"})
    if data.get("email"):
        data["email"] = str(data["email"]).strip().lower()

    existing = find_canonical_lead_by_phone(db, agency_id=agency_id, phone=data.get("phone"))
    if existing is not None:
        merge_inquiry_into_existing_lead(
            db,
            existing,
            new_source=data.get("source"),
            created_by_id=current_user.id,
            message=data.get("message"),
            email=data.get("email"),
            cms_package_id=data.get("cms_package_id"),
            activity_detail=(
                f"Returning contact — new inquiry from {data.get('source') or 'Manual Input'}. "
                f"Merged into lead {existing.lead_code or existing.id}."
            ),
        )
        assignee_applied = apply_returning_customer_assignee(
            db,
            existing,
            agency_id=agency_id,
            customer_id=data.get("customer_id") or existing.customer_id,
            requested_assignee_id=data.get("assigned_to_id"),
            prefer_original_handler=True,
        )
        add_lead_children(
            db,
            existing,
            created_by_id=current_user.id,
            notes=payload.notes,
            activities=[
                a
                for a in payload.activities
                if "Lead created from source" not in a.description
            ],
            followups=payload.followups,
        )
        ensure_lead_code(db, existing)
        audit_update(
            db,
            agency_id=agency_id,
            user_id=current_user.id,
            entity_type="Lead",
            entity_id=existing.id,
            details=(
                f'Merged inquiry into lead "{existing.title}" '
                f"({existing.lead_code or existing.id})"
            ),
            changed_fields=["source"] + (["assigned_to_id"] if assignee_applied else []),
        )
        commit_or_raise(db)
        response.status_code = status.HTTP_200_OK
        lead = get_lead_for_agency(db, existing.id, agency_id, include_deleted=True)
        assert lead is not None
        return _finalize_lead_read(db, lead)

    lead = Lead(**data, agency_id=agency_id)
    db.add(lead)
    db.flush()

    assign_lead_code(db, lead)

    requested_customer_id = data.get("customer_id")
    returning_customer = requested_customer_id is not None
    if requested_customer_id is not None:
        customer = db.get(Customer, requested_customer_id)
        if (
            customer is None
            or customer.agency_id != agency_id
            or customer.is_deleted
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Customer not found for this agency.",
            )
        lead.customer_id = customer.id
    else:
        customer, customer_created = link_or_create_customer_for_lead(
            db,
            agency_id=agency_id,
            lead_id=lead.id,
            first_name=lead.first_name,
            last_name=lead.last_name,
            email=lead.email,
            phone=lead.phone,
        )
        lead.customer_id = customer.id
        returning_customer = not customer_created

        if not existing.lead_code:
            assign_lead_code(db, existing)

        apply_returning_customer_assignee(
        db,
        lead,
        agency_id=agency_id,
        customer_id=lead.customer_id,
        requested_assignee_id=data.get("assigned_to_id"),
        prefer_original_handler=returning_customer,
    )

    activities = list(payload.activities)
    if not any("Customer Directory profile linked" in a.description for a in activities):
        updated: list[LeadActivityCreateNested] = []
        appended = False
        for activity in activities:
            if (
                not appended
                and activity.type == "NOTE"
                and "Lead created from source" in activity.description
            ):
                updated.append(
                    LeadActivityCreateNested(
                        type=activity.type,
                        description=f"{activity.description} · Customer Directory profile linked",
                    )
                )
                appended = True
            else:
                updated.append(activity)
        if not appended:
            updated.insert(
                0,
                LeadActivityCreateNested(
                    type="NOTE",
                    description=(
                        f"Lead created from source: {lead.source or 'Manual Input'}"
                        f" · Customer Directory profile linked"
                    ),
                ),
            )
        activities = updated

    add_lead_children(
        db,
        lead,
        created_by_id=current_user.id,
        notes=payload.notes,
        activities=activities,
        followups=payload.followups,
    )
    apply_lead_status_transition(
        db,
        lead,
        None,
        created_by_id=current_user.id,
    )
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Lead",
        entity_id=lead.id,
        details=f'Created lead "{lead.title}" ({lead.lead_code or lead.id})',
    )
    commit_or_raise(db)
    background_tasks.add_task(notify_team_new_lead_by_id, lead.id)
    response.status_code = status.HTTP_201_CREATED
    lead = get_lead_for_agency(db, lead.id, agency_id, include_deleted=True)
    assert lead is not None
    return _finalize_lead_read(db, lead)


@router.patch("/{lead_id}", response_model=LeadRead)
def update_lead(
    lead_id: UUID,
    payload: LeadUpdate,
    background_tasks: BackgroundTasks,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    lead = get_lead_for_agency(db, lead_id, agency_id)
    if lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found.")

    previous_assigned_to_id = lead.assigned_to_id
    data = payload.model_dump(
        exclude_unset=True,
        exclude={"append_notes", "append_activities", "append_followups"},
    )
    previous_status = lead.status
    apply_partial_update(lead, data)
    if "status" in data:
        apply_lead_status_transition(
            db,
            lead,
            previous_status,
            created_by_id=current_user.id,
        )

    notice = LeadUpdateNotice()

    if "assigned_to_id" in data and lead.assigned_to_id != previous_assigned_to_id:
        notice.assigned_changed = True
        if lead.assigned_to_id is None:
            notice.assignee_name = "Unassigned"
        else:
            assignee = db.get(User, lead.assigned_to_id)
            notice.assignee_name = assignee.name if assignee else "Team member"

    if "status" in data and lead.status != previous_status:
        notice.status_changed = True
        notice.old_status = previous_status
        notice.new_status = lead.status

    if payload.append_followups:
        notice.followups_added = len(payload.append_followups)

    if payload.append_notes and lead.assigned_to_id is None:
        notice.note_on_unassigned = True

    if payload.append_notes:
        add_lead_children(
            db,
            lead,
            created_by_id=current_user.id,
            notes=payload.append_notes,
            activities=[],
            followups=[],
        )
    if payload.append_activities:
        add_lead_children(
            db,
            lead,
            created_by_id=current_user.id,
            notes=[],
            activities=payload.append_activities,
            followups=[],
        )
    if payload.append_followups:
        add_lead_children(
            db,
            lead,
            created_by_id=current_user.id,
            notes=[],
            activities=[],
            followups=payload.append_followups,
        )

    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Lead",
        entity_id=lead.id,
        details=f'Updated lead "{lead.title}" ({lead.first_name} {lead.last_name})',
        changed_fields=changed_fields_from_payload(
            payload,
            exclude={"append_notes", "append_activities", "append_followups"},
        ),
    )
    commit_or_raise(db)
    if (
        notice.assigned_changed
        or notice.status_changed
        or notice.followups_added > 0
        or notice.note_on_unassigned
    ):
        background_tasks.add_task(notify_lead_update_by_id, lead.id, notice)
    lead = get_lead_for_agency(db, lead.id, agency_id, include_deleted=True)
    assert lead is not None
    return _finalize_lead_read(db, lead)


@router.delete("/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lead(
    lead_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    lead = get_lead_for_agency(db, lead_id, agency_id)
    if lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found.")
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Lead",
        entity_id=lead.id,
        details=f'Soft-deleted lead "{lead.title}" ({lead.first_name} {lead.last_name})',
    )
    lead.is_deleted = True
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
