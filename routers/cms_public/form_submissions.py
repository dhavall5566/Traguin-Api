from fastapi import APIRouter, BackgroundTasks, Depends, Request, status
from sqlalchemy.orm import Session

from database import get_db
from models.submissions import FormSubmission
from schemas.form_submissions import FormSubmissionCreate, FormSubmissionRead
from services.form_submission_jobs import run_form_submission_intake
from services.form_submission_intake import LEAD_ELIGIBLE_FORM_TYPES
from utils.db import commit_or_raise
from utils.request import client_ip_or_none

router = APIRouter()


@router.post("", response_model=FormSubmissionRead, status_code=status.HTTP_201_CREATED)
def create_form_submission(
    payload: FormSubmissionCreate,
    request: Request,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    data = payload.model_dump()
    if data.get("email"):
        data["email"] = str(data["email"]).strip().lower()
    item = FormSubmission(
        **data,
        ip_address=client_ip_or_none(request),
        user_agent=request.headers.get("user-agent"),
    )
    db.add(item)
    db.flush()
    submission_id = item.id
    commit_or_raise(db)

    if payload.form_type in LEAD_ELIGIBLE_FORM_TYPES:
        background_tasks.add_task(run_form_submission_intake, submission_id)

    return item
