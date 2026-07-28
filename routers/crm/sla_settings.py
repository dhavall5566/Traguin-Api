from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from models.crm.sla_settings import AgencySlaSettings
from models.crm.tenancy import User
from schemas.crm.sla_settings import AgencySlaSettingsRead, AgencySlaSettingsUpdate
from utils.db import apply_partial_update, commit_or_raise

router = APIRouter()

def _get_or_create(db: Session, agency_id: UUID) -> AgencySlaSettings:
    row = db.get(AgencySlaSettings, agency_id)
    if row is None:
        row = AgencySlaSettings(agency_id=agency_id)
        db.add(row)
        db.flush()
    return row

@router.get("", response_model=AgencySlaSettingsRead)
def get_sla_settings(agency_id: UUID = Depends(require_agency_scope), db: Session = Depends(get_db)):
    return _get_or_create(db, agency_id)

@router.patch("", response_model=AgencySlaSettingsRead)
def update_sla_settings(
    payload: AgencySlaSettingsUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    row = _get_or_create(db, agency_id)
    apply_partial_update(row, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(row)
    return row
