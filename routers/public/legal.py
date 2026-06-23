from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.legal import LegalPage
from schemas.legal import LegalPageRead
from schemas.pagination import PaginatedResponse
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[LegalPageRead])
def list_legal_pages(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(LegalPage).order_by(LegalPage.slug)
    return paginate(query, limit, offset, transform=LegalPageRead.model_validate)


@router.get("/slug/{slug}", response_model=LegalPageRead)
def get_legal_page_by_slug(slug: str, db: Session = Depends(get_db)):
    item = db.query(LegalPage).filter_by(slug=slug).one_or_none()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Legal page not found.")
    return item
