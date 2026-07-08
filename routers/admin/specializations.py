from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.admin_list_filters import AdminListFilters, apply_admin_list_filters, get_admin_list_filters
from dependencies.pagination import get_pagination
from models.content import Specialization
from schemas.pagination import PaginatedResponse
from schemas.specialization import SpecializationCreate, SpecializationRead, SpecializationUpdate
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[SpecializationRead])
def list_specializations(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    filters: AdminListFilters = Depends(get_admin_list_filters),
):
    limit, offset = pagination
    query = db.query(Specialization)
    query = apply_admin_list_filters(
        query,
        Specialization,
        filters,
        search_fields=("title", "slug", "description", "icon_key"),
    )
    query = query.order_by(Specialization.sort_order, Specialization.title)
    return paginate(query, limit, offset, transform=SpecializationRead.model_validate)


@router.get("/{specialization_id}", response_model=SpecializationRead)
def get_specialization(specialization_id: UUID, db: Session = Depends(get_db)):
    item = db.get(Specialization, specialization_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specialization not found.")
    return item


@router.post("", response_model=SpecializationRead, status_code=status.HTTP_201_CREATED)
def create_specialization(payload: SpecializationCreate, db: Session = Depends(get_db)):
    item = Specialization(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.patch("/{specialization_id}", response_model=SpecializationRead)
def update_specialization(
    specialization_id: UUID,
    payload: SpecializationUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(Specialization, specialization_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specialization not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.delete("/{specialization_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_specialization(specialization_id: UUID, db: Session = Depends(get_db)):
    item = db.get(Specialization, specialization_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specialization not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
