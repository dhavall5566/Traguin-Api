from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope
from dependencies.pagination import get_pagination
from models.crm.audit import AuditLog
from schemas.crm.audit import AuditLogRead
from schemas.pagination import PaginatedResponse
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[AuditLogRead])
def list_audit_logs(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    user_id: Annotated[UUID | None, Query()] = None,
    entity_type: Annotated[str | None, Query(max_length=64)] = None,
    action: Annotated[str | None, Query(max_length=32)] = None,
):
    limit, offset = pagination
    query = db.query(AuditLog).filter(AuditLog.agency_id == agency_id).order_by(AuditLog.created_at.desc())
    if user_id is not None:
        query = query.filter(AuditLog.user_id == user_id)
    if entity_type is not None:
        query = query.filter(AuditLog.entity_type == entity_type)
    if action is not None:
        query = query.filter(AuditLog.action == action)
    return paginate(query, limit, offset, transform=AuditLogRead.model_validate)


@router.get("/{audit_log_id}", response_model=AuditLogRead)
def get_audit_log(
    audit_log_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    entry = (
        db.query(AuditLog)
        .filter(AuditLog.id == audit_log_id, AuditLog.agency_id == agency_id)
        .one_or_none()
    )
    if entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Audit log not found.")
    return entry
