from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.crm_tenancy import get_include_deleted
from dependencies.pagination import get_pagination
from models.crm.leads import Lead
from models.crm.tenancy import User
from schemas.crm.lead import LeadActivityCreateNested, LeadCreate, LeadFollowupRead, LeadListRead, LeadRead, LeadUpdate
from schemas.pagination import PaginatedResponse
from services.lead_customers import link_or_create_customer_for_lead
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
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


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
    return paginate(query, limit, offset, transform=lead_to_list_read)


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
    return lead_to_read(lead)


@router.post("", response_model=LeadRead, status_code=status.HTTP_201_CREATED)
def create_lead(
    payload: LeadCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    data = payload.model_dump(exclude={"notes", "activities", "followups"})
    if data.get("email"):
        data["email"] = str(data["email"]).strip().lower()
    lead = Lead(**data, agency_id=agency_id)
    db.add(lead)
    db.flush()

    customer, _customer_created = link_or_create_customer_for_lead(
        db,
        agency_id=agency_id,
        lead_id=lead.id,
        first_name=lead.first_name,
        last_name=lead.last_name,
        email=lead.email,
        phone=lead.phone,
    )
    lead.customer_id = customer.id

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
        details=f'Created lead "{lead.title}" ({lead.first_name} {lead.last_name})',
    )
    commit_or_raise(db)
    lead = get_lead_for_agency(db, lead.id, agency_id, include_deleted=True)
    assert lead is not None
    return lead_to_read(lead)


@router.patch("/{lead_id}", response_model=LeadRead)
def update_lead(
    lead_id: UUID,
    payload: LeadUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    lead = get_lead_for_agency(db, lead_id, agency_id)
    if lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found.")

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
    lead = get_lead_for_agency(db, lead.id, agency_id, include_deleted=True)
    assert lead is not None
    return lead_to_read(lead)


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
