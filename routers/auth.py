from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from dependencies.auth import require_admin
from models.admin_users import AdminUser
from schemas.auth import AdminUserRead, LoginRequest, TokenResponse
from utils.jwt_tokens import create_access_token
from utils.passwords import verify_password

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.scalar(select(AdminUser).where(AdminUser.email == payload.email.lower()))
    if user is None or not user.is_active or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    access_token, expires_in = create_access_token(
        user_id=user.id,
        email=user.email,
        role=user.role,
    )
    return TokenResponse(access_token=access_token, expires_in=expires_in)


@router.get("/me", response_model=AdminUserRead)
def read_current_user(current_user: AdminUser = Depends(require_admin)):
    return current_user
