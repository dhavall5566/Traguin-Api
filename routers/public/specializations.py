from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.content import Specialization
from schemas.pagination import PaginatedResponse
from schemas.specialization import SpecializationRead
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[SpecializationRead])
def list_specializations(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Specialization).order_by(Specialization.sort_order, Specialization.title)
    return paginate(query, limit, offset, transform=SpecializationRead.model_validate)


@router.get("/{specialization_id}", response_model=SpecializationRead)
def get_specialization(specialization_id: UUID, db: Session = Depends(get_db)):
    item = db.get(Specialization, specialization_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specialization not found.")
    return item
