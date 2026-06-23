from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from models.crm.tenancy import Agency, User
from schemas.crm.auth import CrmLoginRequest, CrmSessionRead, CrmTokenResponse
from utils.crm_jwt_tokens import create_crm_access_token
from utils.passwords import verify_password

router = APIRouter()


@router.post("/login", response_model=CrmTokenResponse)
def login(payload: CrmLoginRequest, db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == payload.email.lower()))
    if (
        user is None
        or user.is_deleted
        or not user.password_hash
        or not verify_password(payload.password, user.password_hash)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    access_token, expires_in = create_crm_access_token(
        user_id=user.id,
        email=user.email,
        agency_id=user.agency_id,
    )
    return CrmTokenResponse(access_token=access_token, expires_in=expires_in)


@router.get("/me", response_model=CrmSessionRead)
def get_me(
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    agency = (
        db.query(Agency)
        .filter(Agency.id == agency_id, Agency.is_deleted.is_(False))
        .one_or_none()
    )
    if agency is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agency not found.")
    return CrmSessionRead(user=current_user, agency=agency)
