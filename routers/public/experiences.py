from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.experiences import Experience
from schemas.experiences import ExperienceRead
from schemas.pagination import PaginatedResponse
from services.experiences import experience_query_with_nested, experience_to_read
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[ExperienceRead])
def list_experiences(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = (
        experience_query_with_nested(db)
        .filter(Experience.is_published.is_(True))
        .order_by(Experience.headline)
    )
    return paginate(query, limit, offset, transform=experience_to_read)


@router.get("/slug/{slug}", response_model=ExperienceRead)
def get_experience_by_slug(slug: str, db: Session = Depends(get_db)):
    experience = (
        experience_query_with_nested(db)
        .filter_by(slug=slug, is_published=True)
        .one_or_none()
    )
    if experience is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found.")
    return experience_to_read(experience)
