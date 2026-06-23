from enum import Enum
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.content import Faq
from schemas.faq import FaqRead
from schemas.pagination import PaginatedResponse
from utils.pagination import paginate

router = APIRouter()


class FaqScope(str, Enum):
    about = "about"
    itinerary = "itinerary"
    all = "all"


@router.get("", response_model=PaginatedResponse[FaqRead])
def list_faqs(
    scope: FaqScope = Query(default=FaqScope.about),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Faq).filter(Faq.is_published.is_(True))
    if scope == FaqScope.about:
        query = query.filter(Faq.itinerary_id.is_(None))
    elif scope == FaqScope.itinerary:
        query = query.filter(Faq.itinerary_id.isnot(None))
    query = query.order_by(Faq.sort_order, Faq.question)
    return paginate(query, limit, offset, transform=FaqRead.model_validate)


@router.get("/{faq_id}", response_model=FaqRead)
def get_faq(faq_id: UUID, db: Session = Depends(get_db)):
    faq = db.get(Faq, faq_id)
    if faq is None or not faq.is_published:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="FAQ not found.")
    return faq
