from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.submissions import FormSubmission
from schemas.form_submissions import (
    FormSubmissionCreate,
    FormSubmissionRead,
    FormSubmissionStatusUpdate,
)
from schemas.pagination import PaginatedResponse
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[FormSubmissionRead])
def list_form_submissions(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(FormSubmission).order_by(FormSubmission.created_at.desc())
    return paginate(query, limit, offset, transform=FormSubmissionRead.model_validate)


@router.get("/{submission_id}", response_model=FormSubmissionRead)
def get_form_submission(submission_id: UUID, db: Session = Depends(get_db)):
    item = db.get(FormSubmission, submission_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Form submission not found.")
    return item


@router.patch("/{submission_id}", response_model=FormSubmissionRead)
def update_form_submission_status(
    submission_id: UUID,
    payload: FormSubmissionStatusUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(FormSubmission, submission_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Form submission not found.")
    apply_partial_update(item, payload.model_dump())
    commit_or_raise(db)
    db.refresh(item)
    return item


@router.delete("/{submission_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_form_submission(submission_id: UUID, db: Session = Depends(get_db)):
    item = db.get(FormSubmission, submission_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Form submission not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
