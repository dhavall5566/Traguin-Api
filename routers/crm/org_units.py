from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from models.crm.org_units import OrgUnit
from models.crm.tenancy import User
from schemas.crm.org_unit import OrgUnitCreate, OrgUnitRead, OrgUnitTreeNode, OrgUnitUpdate
from utils.db import apply_partial_update, commit_or_raise

router = APIRouter()

def _get_unit(db: Session, unit_id: UUID, agency_id: UUID) -> OrgUnit | None:
    return (
        db.query(OrgUnit)
        .filter(OrgUnit.id == unit_id, OrgUnit.agency_id == agency_id, OrgUnit.is_deleted.is_(False))
        .one_or_none()
    )

def _build_tree(units: list[OrgUnit], parent_id: UUID | None = None) -> list[OrgUnitTreeNode]:
    nodes: list[OrgUnitTreeNode] = []
    for unit in sorted([u for u in units if u.parent_id == parent_id], key=lambda u: u.name):
        children = _build_tree(units, unit.id)
        nodes.append(OrgUnitTreeNode.model_validate(unit).model_copy(update={"children": children}))
    return nodes

@router.get("", response_model=list[OrgUnitRead])
def list_org_units(agency_id: UUID = Depends(require_agency_scope), db: Session = Depends(get_db)):
    rows = (
        db.query(OrgUnit)
        .filter(OrgUnit.agency_id == agency_id, OrgUnit.is_deleted.is_(False))
        .order_by(OrgUnit.name)
        .all()
    )
    return rows

@router.get("/tree", response_model=list[OrgUnitTreeNode])
def list_org_units_tree(agency_id: UUID = Depends(require_agency_scope), db: Session = Depends(get_db)):
    rows = (
        db.query(OrgUnit)
        .filter(OrgUnit.agency_id == agency_id, OrgUnit.is_deleted.is_(False))
        .all()
    )
    return _build_tree(rows)

@router.get("/{unit_id}", response_model=OrgUnitRead)
def get_org_unit(
    unit_id: UUID, agency_id: UUID = Depends(require_agency_scope), db: Session = Depends(get_db)
):
    unit = _get_unit(db, unit_id, agency_id)
    if unit is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Org unit not found.")
    return unit

@router.post("", response_model=OrgUnitRead, status_code=status.HTTP_201_CREATED)
def create_org_unit(
    payload: OrgUnitCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    if payload.parent_id is not None:
        parent = _get_unit(db, payload.parent_id, agency_id)
        if parent is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Parent org unit not found.")
    unit = OrgUnit(**payload.model_dump(), agency_id=agency_id)
    db.add(unit)
    commit_or_raise(db)
    db.refresh(unit)
    return unit

@router.patch("/{unit_id}", response_model=OrgUnitRead)
def update_org_unit(
    unit_id: UUID,
    payload: OrgUnitUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    unit = _get_unit(db, unit_id, agency_id)
    if unit is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Org unit not found.")
    data = payload.model_dump(exclude_unset=True)
    if "parent_id" in data and data["parent_id"] is not None:
        if data["parent_id"] == unit_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unit cannot be its own parent.")
        parent = _get_unit(db, data["parent_id"], agency_id)
        if parent is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Parent org unit not found.")
    apply_partial_update(unit, data)
    commit_or_raise(db)
    db.refresh(unit)
    return unit

@router.delete("/{unit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_org_unit(
    unit_id: UUID, agency_id: UUID = Depends(require_agency_scope), db: Session = Depends(get_db)
):
    unit = _get_unit(db, unit_id, agency_id)
    if unit is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Org unit not found.")
    unit.is_deleted = True
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
