from datetime import datetime, timedelta, timezone
from uuid import UUID

import jwt
from jwt.exceptions import InvalidTokenError

from config import settings


def create_access_token(*, user_id: UUID, email: str, role: str) -> tuple[str, int]:
    expires_in = settings.jwt_expire_hours * 3600
    expire = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
    payload = {
        "sub": str(user_id),
        "email": email,
        "role": role,
        "exp": expire,
    }
    token = jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return token, expires_in


def decode_access_token(token: str) -> dict:
    return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])


class TokenValidationError(Exception):
    pass


def get_token_subject(token: str) -> UUID:
    try:
        payload = decode_access_token(token)
    except InvalidTokenError as exc:
        raise TokenValidationError("Invalid or expired token.") from exc
    subject = payload.get("sub")
    if not subject:
        raise TokenValidationError("Invalid token payload.")
    return UUID(subject)
