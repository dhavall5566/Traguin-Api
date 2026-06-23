from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.experiences import Experience
from schemas.experiences import ExperienceCreate, ExperienceRead, ExperienceUpdate
from schemas.pagination import PaginatedResponse
from services.experiences import (
    experience_query_with_nested,
    experience_to_read,
    sync_experience_offers,
    sync_experience_process_steps,
    sync_experience_stats,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[ExperienceRead])
def list_experiences(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = experience_query_with_nested(db).order_by(Experience.headline)
    return paginate(query, limit, offset, transform=experience_to_read)


@router.get("/{experience_id}", response_model=ExperienceRead)
def get_experience(experience_id: UUID, db: Session = Depends(get_db)):
    experience = experience_query_with_nested(db).filter_by(id=experience_id).one_or_none()
    if experience is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found.")
    return experience_to_read(experience)


@router.post("", response_model=ExperienceRead, status_code=status.HTTP_201_CREATED)
def create_experience(payload: ExperienceCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    offers = data.pop("offers")
    stats = data.pop("stats")
    process_steps = data.pop("process_steps")
    experience = Experience(**data)
    db.add(experience)
    db.flush()
    sync_experience_offers(db, experience, offers)
    sync_experience_stats(db, experience, stats)
    sync_experience_process_steps(db, experience, process_steps)
    commit_or_raise(db)
    experience = experience_query_with_nested(db).filter_by(id=experience.id).one()
    return experience_to_read(experience)


@router.patch("/{experience_id}", response_model=ExperienceRead)
def update_experience(
    experience_id: UUID,
    payload: ExperienceUpdate,
    db: Session = Depends(get_db),
):
    experience = experience_query_with_nested(db).filter_by(id=experience_id).one_or_none()
    if experience is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found.")
    data = payload.model_dump(exclude_unset=True)
    offers = data.pop("offers", None)
    stats = data.pop("stats", None)
    process_steps = data.pop("process_steps", None)
    apply_partial_update(experience, data)
    if offers is not None:
        sync_experience_offers(db, experience, offers)
    if stats is not None:
        sync_experience_stats(db, experience, stats)
    if process_steps is not None:
        sync_experience_process_steps(db, experience, process_steps)
    commit_or_raise(db)
    experience = experience_query_with_nested(db).filter_by(id=experience.id).one()
    return experience_to_read(experience)


@router.delete("/{experience_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_experience(experience_id: UUID, db: Session = Depends(get_db)):
    experience = db.get(Experience, experience_id)
    if experience is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found.")
    db.delete(experience)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
