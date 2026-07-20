from datetime import datetime, timezone
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query, Response, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.crm_tenancy import get_include_deleted
from dependencies.pagination import get_pagination
from models.crm.customers import Customer
from models.crm.leads import Lead, LeadActivity
from models.crm.tenancy import User
from schemas.crm.customer_inquiry import CustomerInquiryHistoryRead
from schemas.crm.lead import (
    LeadActivityCreateNested,
    LeadAssignmentPendingRead,
    LeadCreate,
    LeadFollowupRead,
    LeadIntakeCheckRead,
    LeadIntakeCustomerRead,
    LeadIntakeDuplicateRead,
    LeadListRead,
    LeadRead,
    LeadRecentEventRead,
    LeadUpdate,
)
from schemas.pagination import PaginatedResponse
from services.customer_inquiry_history import build_customer_inquiry_history
from services.lead_assignee import apply_returning_customer_assignee
from services.lead_codes import assign_lead_code, ensure_lead_code
from services.customer_codes import ensure_customer_code_by_id
from services.lead_customers import find_customer_by_contact, link_or_create_customer_for_lead
from services.lead_intake_check import check_lead_intake
from services.lead_phone_dedup import merge_inquiry_into_existing_lead, resolve_canonical_lead_for_intake
from services.notification_matrix import maybe_notify_no_answer_calls_by_id
from services.lead_status import apply_lead_status_transition
from services.lead_stage_automation import maybe_sync_lead_stage_from_signals
from services.leads import (
    add_lead_children,
    get_lead_for_agency,
    lead_query_with_nested,
    lead_to_list_read,
    lead_to_read,
    list_pending_followups_for_agency,
)
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from services.email_notifications import (
    notify_lead_assignment_accepted_email_by_id,
    notify_lead_assignment_rejected_email_by_id,
)
from services.lead_assignment import (
    ASSIGNMENT_PENDING,
    accept_lead_assignment,
    apply_assignment_on_assign,
    list_pending_assignments_for_user,
    reject_lead_assignment,
)
from services.whatsapp_notifications import LeadUpdateNotice, notify_lead_update_by_id, notify_team_new_lead_by_id
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


def _finalize_lead_read(db: Session, lead: Lead) -> LeadRead:
    had_code = bool(lead.lead_code)
    result = lead_to_read(db, lead)
    if not had_code and lead.lead_code:
        commit_or_raise(db)
    return result


def _serialize_intake_check(
    db: Session,
    agency_id: UUID,
    email: str | None,
    phone: str | None,
    exclude_lead_id: UUID | None = None,
) -> LeadIntakeCheckRead:
    result = check_lead_intake(
        db,
        agency_id=agency_id,
        email=email,
        phone=phone,
        exclude_lead_id=exclude_lead_id,
    )
    customer_read = None
    if result.existing_customer is not None:
        customer = result.existing_customer
        customer_read = LeadIntakeCustomerRead(
            id=customer.id,
            first_name=customer.first_name,
            last_name=customer.last_name,
            email=customer.email,
            phone=customer.phone,
        )
    canonical_read = None
    if result.canonical_lead is not None:
        ensure_lead_code(db, result.canonical_lead)
        canonical_read = LeadIntakeDuplicateRead(
            id=result.canonical_lead.id,
            lead_code=result.canonical_lead.lead_code,
            title=result.canonical_lead.title,
            status=result.canonical_lead.status,
            email=result.canonical_lead.email,
            phone=result.canonical_lead.phone,
            created_at=result.canonical_lead.created_at,
        )
    duplicate_reads: list[LeadIntakeDuplicateRead] = []
    for duplicate in result.duplicate_leads:
        ensure_lead_code(db, duplicate)
        duplicate_reads.append(
            LeadIntakeDuplicateRead(
                id=duplicate.id,
                lead_code=duplicate.lead_code,
                title=duplicate.title,
                status=duplicate.status,
                email=duplicate.email,
                phone=duplicate.phone,
                created_at=duplicate.created_at,
            )
        )
    return LeadIntakeCheckRead(
        existing_customer=customer_read,
        canonical_lead=canonical_read,
        match_reason=result.match_reason,
        duplicate_leads=duplicate_reads,
        will_merge=result.canonical_lead is not None,
    )


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
    return result


def _serialize_inquiry_history(
    db: Session,
    *,
    agency_id: UUID,
    phone: str | None,
    email: str | None,
    customer_id: UUID | None = None,
    current_lead_id: UUID | None = None,
    include_interactions: bool = True,
    include_details: bool = True,
) -> CustomerInquiryHistoryRead:
    history = build_customer_inquiry_history(
        db,
        agency_id=agency_id,
        phone=phone,
        email=email,
        customer_id=customer_id,
        current_lead_id=current_lead_id,
        include_interactions=include_interactions,
        include_details=include_details,
    )
    return CustomerInquiryHistoryRead.model_validate(history.__dict__)


@router.get("/intake-check", response_model=LeadIntakeCheckRead)
def check_lead_intake_endpoint(
    email: str | None = Query(default=None),
    phone: str | None = Query(default=None),
    exclude_lead_id: UUID | None = Query(default=None),
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    normalized_email = email.strip().lower() if email and email.strip() else None
    normalized_phone = phone.strip() if phone and phone.strip() else None
    if not normalized_email and not normalized_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provide at least one of email or phone.",
        )
    result = _serialize_intake_check(
        db,
        agency_id,
        normalized_email,
        normalized_phone,
        exclude_lead_id=exclude_lead_id,
    )
    commit_or_raise(db)
    return result


@router.get("/recent", response_model=list[LeadRecentEventRead])
def list_recent_lead_events(
    since: datetime = Query(..., description="ISO timestamp — events after this instant"),
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    since_utc = since if since.tzinfo else since.replace(tzinfo=timezone.utc)
    if since_utc.tzinfo is not None:
        since_utc = since_utc.astimezone(timezone.utc)

    new_leads = (
        db.query(Lead)
        .filter(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.created_at > since_utc,
        )
        .order_by(Lead.created_at.desc())
        .limit(15)
        .all()
    )

    returning_lead_ids = db.scalars(
        select(LeadActivity.lead_id)
        .join(Lead, Lead.id == LeadActivity.lead_id)
        .where(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.created_at <= since_utc,
            LeadActivity.created_at > since_utc,
            or_(
                LeadActivity.description.ilike("%Returning contact%"),
                LeadActivity.description.ilike("%Merged inquiry%"),
                LeadActivity.description.ilike("%Website intake merged into%"),
            ),
        )
        .distinct()
        .limit(15)
    ).all()

    returning_leads: list[Lead] = []
    if returning_lead_ids:
        returning_leads = (
            db.query(Lead)
            .filter(Lead.id.in_(returning_lead_ids))
            .order_by(Lead.updated_at.desc())
            .all()
        )

    events: list[LeadRecentEventRead] = []
    seen: set[UUID] = set()

    for lead in new_leads:
        ensure_lead_code(db, lead)
        customer = find_customer_by_contact(
            db,
            agency_id=agency_id,
            email=lead.email,
            phone=lead.phone,
        )
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
                kind="new",
                existing_customer=customer is not None or lead.customer_id is not None,
                customer_id=lead.customer_id or (customer.id if customer else None),
            )
        )
        seen.add(lead.id)

    for lead in returning_leads:
        if lead.id in seen:
            continue
        ensure_lead_code(db, lead)
        customer = None
        if lead.customer_id:
            customer = db.get(Customer, lead.customer_id)
        if customer is None:
            customer = find_customer_by_contact(
                db,
                agency_id=agency_id,
                email=lead.email,
                phone=lead.phone,
            )
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
                kind="returning",
                existing_customer=True,
                customer_id=lead.customer_id or (customer.id if customer else None),
                merged_duplicate=True,
            )
        )
        seen.add(lead.id)

    events.sort(key=lambda event: event.updated_at, reverse=True)
    if events:
        commit_or_raise(db)
    return events[:15]


@router.get("/followups/pending", response_model=list[LeadFollowupRead])
def list_pending_lead_followups(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    return list_pending_followups_for_agency(db, agency_id)


@router.get("/assignments/pending", response_model=list[LeadAssignmentPendingRead])
def list_pending_lead_assignments(
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    return list_pending_assignments_for_user(db, agency_id=agency_id, user_id=current_user.id)


@router.post("/{lead_id}/assignment/accept", response_model=LeadRead)
def accept_lead_assignment_route(
    lead_id: UUID,
    background_tasks: BackgroundTasks,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    lead = get_lead_for_agency(db, lead_id, agency_id)
    if lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found.")

    accept_lead_assignment(db, lead, user_id=current_user.id)
    maybe_sync_lead_stage_from_signals(db, lead, actor_id=current_user.id)
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Lead",
        entity_id=lead.id,
        details=(
            f'Accepted lead assignment for "{lead.title}" '
            f"({lead.first_name} {lead.last_name}) — started working on it"
        ),
    )
    commit_or_raise(db)
    background_tasks.add_task(
        notify_lead_assignment_accepted_email_by_id,
        lead.id,
        assignee_user_id=current_user.id,
    )
    lead = get_lead_for_agency(db, lead.id, agency_id, include_deleted=True)
    assert lead is not None
    return _finalize_lead_read(db, lead)


@router.post("/{lead_id}/assignment/reject", response_model=LeadRead)
def reject_lead_assignment_route(
    lead_id: UUID,
    background_tasks: BackgroundTasks,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    lead = get_lead_for_agency(db, lead_id, agency_id)
    if lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found.")

    lead, assigner_id = reject_lead_assignment(db, lead, user_id=current_user.id)
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Lead",
        entity_id=lead.id,
        details=(
            f'Rejected lead assignment for "{lead.title}" '
            f"({lead.first_name} {lead.last_name})"
        ),
    )
    commit_or_raise(db)
    if assigner_id is not None:
        background_tasks.add_task(
            notify_lead_assignment_rejected_email_by_id,
            lead.id,
            assignee_user_id=current_user.id,
            assigner_user_id=assigner_id,
        )
    lead = get_lead_for_agency(db, lead.id, agency_id, include_deleted=True)
    assert lead is not None
    return _finalize_lead_read(db, lead)


@router.get("/{lead_id}/inquiry-history", response_model=CustomerInquiryHistoryRead)
def get_lead_inquiry_history(
    lead_id: UUID,
    include_interactions: bool = Query(default=True),
    include_details: bool = Query(default=True),
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    lead = (
        db.query(Lead)
        .filter(
            Lead.id == lead_id,
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
        )
        .one_or_none()
    )
    if lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found.")
    return _serialize_inquiry_history(
        db,
        agency_id=agency_id,
        phone=lead.phone,
        email=lead.email,
        customer_id=lead.customer_id,
        current_lead_id=lead.id,
        include_interactions=include_interactions,
        include_details=include_details,
    )


@router.get("/{lead_id}", response_model=LeadRead)
def get_lead(
    lead_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
    include_deleted: bool = Depends(get_include_deleted),
):
    lead = get_lead_for_agency(db, lead_id, agency_id, include_deleted=include_deleted)
    if lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found.")
    if maybe_sync_lead_stage_from_signals(db, lead, actor_id=current_user.id):
        commit_or_raise(db)
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

    existing, match_reason = resolve_canonical_lead_for_intake(
        db,
        agency_id=agency_id,
        phone=data.get("phone"),
    )
    if existing is not None:
        merge_detail = (
            f"Returning contact — new inquiry from {data.get('source') or 'Manual Input'}. "
            f"Merged into lead {existing.lead_code or existing.id} "
            f"(matched by {match_reason})."
        )
        merge_inquiry_into_existing_lead(
            db,
            existing,
            new_source=data.get("source"),
            created_by_id=current_user.id,
            message=data.get("message"),
            email=data.get("email"),
            cms_package_id=data.get("cms_package_id"),
            activity_detail=merge_detail,
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

    apply_returning_customer_assignee(
        db,
        lead,
        agency_id=agency_id,
        customer_id=lead.customer_id,
        requested_assignee_id=data.get("assigned_to_id"),
        prefer_original_handler=returning_customer,
    )
    if lead.assigned_to_id is not None:
        apply_assignment_on_assign(
            db,
            lead,
            assignee_id=lead.assigned_to_id,
            actor_id=current_user.id,
            agency_id=agency_id,
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
    background_tasks.add_task(notify_team_new_lead_by_id, lead.id, event_type="crm_lead")
    if lead.assigned_to_id is not None and lead.assignment_status == ASSIGNMENT_PENDING:
        assignee = db.get(User, lead.assigned_to_id)
        background_tasks.add_task(
            notify_lead_update_by_id,
            lead.id,
            LeadUpdateNotice(
                assigned_changed=True,
                assignee_name=assignee.name if assignee else "Team member",
            ),
        )
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
    if "assigned_to_id" in data:
        apply_assignment_on_assign(
            db,
            lead,
            assignee_id=lead.assigned_to_id,
            actor_id=current_user.id,
            agency_id=agency_id,
        )
    if "status" in data:
        apply_lead_status_transition(
            db,
            lead,
            previous_status,
            created_by_id=current_user.id,
        )
        if lead.status.upper() == "BOOKED" and lead.customer_id is not None:
            ensure_customer_code_by_id(db, lead.customer_id, agency_id)

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

    if maybe_sync_lead_stage_from_signals(db, lead, actor_id=current_user.id):
        if lead.status != previous_status:
            notice.status_changed = True
            notice.old_status = previous_status
            notice.new_status = lead.status

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
    if payload.append_activities:
        background_tasks.add_task(maybe_notify_no_answer_calls_by_id, lead.id)
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
