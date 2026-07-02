from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, Request, status
from sqlalchemy.orm import Session

from database import get_db
from models.submissions import FormSubmission
from schemas.form_submissions import FormSubmissionCreate, FormSubmissionCreateResponse
from services.form_submission_jobs import run_form_submission_intake
from services.form_submission_intake import (
    LEAD_ELIGIBLE_FORM_TYPES,
    process_form_submission_intake,
)
from utils.db import commit_or_raise
from utils.request import client_ip_or_none

router = APIRouter()

SYNC_INTAKE_FORM_TYPES = frozenset({"plan_my_journey"})


def _to_response(
    item: FormSubmission,
    *,
    lead_id: UUID | None = None,
    customer_id: UUID | None = None,
    member_code: str | None = None,
    inquiry_code: str | None = None,
) -> FormSubmissionCreateResponse:
    return FormSubmissionCreateResponse(
        id=item.id,
        created_at=item.created_at,
        updated_at=item.updated_at,
        form_type=item.form_type,
        payload=item.payload or {},
        name=item.name,
        email=item.email,
        phone=item.phone,
        status=item.status,
        related_itinerary_id=item.related_itinerary_id,
        related_hotel_id=item.related_hotel_id,
        related_destination_id=item.related_destination_id,
        ip_address=item.ip_address,
        user_agent=item.user_agent,
        lead_id=lead_id,
        customer_id=customer_id,
        member_code=member_code,
        inquiry_code=inquiry_code,
    )


@router.post("", response_model=FormSubmissionCreateResponse, status_code=status.HTTP_201_CREATED)
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

    lead_id: UUID | None = None
    customer_id: UUID | None = None
    member_code: str | None = None
    inquiry_code: str | None = None

    if payload.form_type in SYNC_INTAKE_FORM_TYPES:
        lead = process_form_submission_intake(db, item)
        if lead is not None:
            lead_id = lead.id
            customer_id = lead.customer_id
            intake_payload = item.payload or {}
            member_code = intake_payload.get("member_code")
            inquiry_code = intake_payload.get("inquiry_code")
        commit_or_raise(db)
    elif payload.form_type in LEAD_ELIGIBLE_FORM_TYPES:
        submission_id = item.id
        commit_or_raise(db)
        background_tasks.add_task(run_form_submission_intake, submission_id)
    else:
        commit_or_raise(db)

    return _to_response(
        item,
        lead_id=lead_id,
        customer_id=customer_id,
        member_code=member_code,
        inquiry_code=inquiry_code,
    )
