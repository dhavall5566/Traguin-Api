from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.auth import require_admin
from models.admin_users import AdminUser
from schemas.auth import ChangePasswordRequest, MessageResponse
from utils.db import commit_or_raise
from utils.passwords import hash_password, verify_password

router = APIRouter()


@router.post("/change-password", response_model=MessageResponse)
def change_password(
    payload: ChangePasswordRequest,
    db: Session = Depends(get_db),
    current_user: AdminUser = Depends(require_admin),
):
    if not verify_password(payload.current_password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect.",
        )

    if verify_password(payload.new_password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password must be different from the current password.",
        )

    current_user.hashed_password = hash_password(payload.new_password)
    commit_or_raise(db)
    return MessageResponse(message="Password updated successfully.")
