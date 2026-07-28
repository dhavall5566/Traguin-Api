from datetime import datetime, timezone
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from models.crm.approvals import ApprovalRequest
from models.crm.tenancy import User
from schemas.crm.approval import APPROVAL_TYPES, ApprovalCreate, ApprovalRead, ApprovalReview
from utils.db import commit_or_raise

router = APIRouter()

def _get_approval(db: Session, approval_id: UUID, agency_id: UUID) -> ApprovalRequest | None:
    return (
        db.query(ApprovalRequest)
        .filter(ApprovalRequest.id == approval_id, ApprovalRequest.agency_id == agency_id)
        .one_or_none()
    )

@router.get("", response_model=list[ApprovalRead])
def list_approvals(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    status_filter: str | None = Query(default=None, alias="status"),
    request_type: str | None = None,
):
    query = db.query(ApprovalRequest).filter(ApprovalRequest.agency_id == agency_id)
    if status_filter:
        query = query.filter(ApprovalRequest.status == status_filter.upper())
    if request_type:
        query = query.filter(ApprovalRequest.request_type == request_type.upper())
    return query.order_by(ApprovalRequest.created_at.desc()).limit(200).all()

@router.get("/pending-count")
def pending_approval_count(agency_id: UUID = Depends(require_agency_scope), db: Session = Depends(get_db)):
    count = (
        db.query(ApprovalRequest)
        .filter(ApprovalRequest.agency_id == agency_id, ApprovalRequest.status == "PENDING")
        .count()
    )
    return {"count": count}

@router.post("", response_model=ApprovalRead, status_code=status.HTTP_201_CREATED)
def create_approval(
    payload: ApprovalCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    if payload.request_type not in APPROVAL_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request type.")
    row = ApprovalRequest(
        **payload.model_dump(),
        agency_id=agency_id,
        requested_by_id=current_user.id,
        status="PENDING",
    )
    db.add(row)
    commit_or_raise(db)
    db.refresh(row)
    return row

@router.post("/{approval_id}/approve", response_model=ApprovalRead)
def approve_approval(
    approval_id: UUID,
    payload: ApprovalReview,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    row = _get_approval(db, approval_id, agency_id)
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Approval not found.")
    if row.status != "PENDING":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Approval already reviewed.")
    row.status = "APPROVED"
    row.reviewed_by_id = current_user.id
    row.review_note = payload.review_note
    row.reviewed_at = datetime.now(timezone.utc)
    commit_or_raise(db)
    db.refresh(row)
    return row

@router.post("/{approval_id}/reject", response_model=ApprovalRead)
def reject_approval(
    approval_id: UUID,
    payload: ApprovalReview,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    row = _get_approval(db, approval_id, agency_id)
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Approval not found.")
    if row.status != "PENDING":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Approval already reviewed.")
    row.status = "REJECTED"
    row.reviewed_by_id = current_user.id
    row.review_note = payload.review_note
    row.reviewed_at = datetime.now(timezone.utc)
    commit_or_raise(db)
    db.refresh(row)
    return row
