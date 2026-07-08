from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.admin_list_filters import AdminListFilters, apply_admin_list_filters, get_admin_list_filters
from dependencies.pagination import get_pagination
from models.legal import LegalPage
from schemas.legal import LegalPageCreate, LegalPageRead, LegalPageUpdate
from schemas.pagination import PaginatedResponse
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[LegalPageRead])
def list_legal_pages(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    filters: AdminListFilters = Depends(get_admin_list_filters),
):
    limit, offset = pagination
    query = db.query(LegalPage)
    query = apply_admin_list_filters(
        query,
        LegalPage,
        filters,
        search_fields=("slug", "title", "eyebrow", "description"),
    )
    query = query.order_by(LegalPage.slug)
    return paginate(query, limit, offset, transform=LegalPageRead.model_validate)


@router.get("/{page_id}", response_model=LegalPageRead)
def get_legal_page(page_id: UUID, db: Session = Depends(get_db)):
    item = db.get(LegalPage, page_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Legal page not found.")
    return item


@router.post("", response_model=LegalPageRead, status_code=status.HTTP_201_CREATED)
def create_legal_page(payload: LegalPageCreate, db: Session = Depends(get_db)):
    item = LegalPage(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.patch("/{page_id}", response_model=LegalPageRead)
def update_legal_page(
    page_id: UUID,
    payload: LegalPageUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(LegalPage, page_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Legal page not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.delete("/{page_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_legal_page(page_id: UUID, db: Session = Depends(get_db)):
    item = db.get(LegalPage, page_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Legal page not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
