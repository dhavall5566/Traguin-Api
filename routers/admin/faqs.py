from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.content import Faq
from schemas.faq import FaqCreate, FaqRead, FaqUpdate
from schemas.pagination import PaginatedResponse
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[FaqRead])
def list_faqs(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Faq).order_by(Faq.sort_order, Faq.question)
    return paginate(query, limit, offset, transform=FaqRead.model_validate)


@router.get("/{faq_id}", response_model=FaqRead)
def get_faq(faq_id: UUID, db: Session = Depends(get_db)):
    faq = db.get(Faq, faq_id)
    if faq is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FAQ not found.")
    return faq


@router.post("", response_model=FaqRead, status_code=status.HTTP_201_CREATED)
def create_faq(payload: FaqCreate, db: Session = Depends(get_db)):
    faq = Faq(**payload.model_dump())
    db.add(faq)
    commit_or_raise(db)
    db.refresh(faq)
    return faq


@router.patch("/{faq_id}", response_model=FaqRead)
def update_faq(faq_id: UUID, payload: FaqUpdate, db: Session = Depends(get_db)):
    faq = db.get(Faq, faq_id)
    if faq is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FAQ not found.")
    apply_partial_update(faq, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(faq)
    return faq


@router.delete("/{faq_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_faq(faq_id: UUID, db: Session = Depends(get_db)):
    faq = db.get(Faq, faq_id)
    if faq is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FAQ not found.")
    db.delete(faq)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
