from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.admin_list_filters import AdminListFilters, apply_admin_list_filters, get_admin_list_filters
from dependencies.pagination import get_pagination
from models.destinations import DestinationCategory
from schemas.destination import (
    DestinationCategoryCreate,
    DestinationCategoryRead,
    DestinationCategoryUpdate,
)
from schemas.pagination import PaginatedResponse
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[DestinationCategoryRead])
def list_destination_categories(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    filters: AdminListFilters = Depends(get_admin_list_filters),
):
    limit, offset = pagination
    query = db.query(DestinationCategory)
    query = apply_admin_list_filters(
        query,
        DestinationCategory,
        filters,
        search_fields=("title", "slug", "description"),
    )
    query = query.order_by(DestinationCategory.sort_order, DestinationCategory.title)
    return paginate(query, limit, offset, transform=DestinationCategoryRead.model_validate)


@router.get("/{category_id}", response_model=DestinationCategoryRead)
def get_destination_category(category_id: UUID, db: Session = Depends(get_db)):
    item = db.get(DestinationCategory, category_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Destination category not found.")
    return item


@router.post("", response_model=DestinationCategoryRead, status_code=status.HTTP_201_CREATED)
def create_destination_category(payload: DestinationCategoryCreate, db: Session = Depends(get_db)):
    item = DestinationCategory(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.patch("/{category_id}", response_model=DestinationCategoryRead)
def update_destination_category(
    category_id: UUID,
    payload: DestinationCategoryUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(DestinationCategory, category_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Destination category not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_destination_category(category_id: UUID, db: Session = Depends(get_db)):
    item = db.get(DestinationCategory, category_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Destination category not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
