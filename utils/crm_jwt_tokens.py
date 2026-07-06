from datetime import datetime, timedelta, timezone
from uuid import UUID

import jwt
from jwt.exceptions import InvalidTokenError

from config import settings

CRM_TOKEN_TYPE = "crm"


def create_crm_access_token(
    *,
    user_id: UUID,
    email: str,
    agency_id: UUID | None,
) -> tuple[str, int]:
    expires_in = settings.jwt_expire_hours * 3600
    expire = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
    payload = {
        "sub": str(user_id),
        "email": email,
        "agency_id": str(agency_id) if agency_id else None,
        "type": CRM_TOKEN_TYPE,
        "exp": expire,
    }
    token = jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return token, expires_in


def decode_crm_access_token(token: str) -> dict:
    payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    if payload.get("type") != CRM_TOKEN_TYPE:
        raise TokenValidationError("Invalid token type.")
    return payload


class TokenValidationError(Exception):
    pass


def get_crm_token_subject(token: str) -> UUID:
    try:
        payload = decode_crm_access_token(token)
    except InvalidTokenError as exc:
        raise TokenValidationError("Invalid or expired token.") from exc
    subject = payload.get("sub")
    if not subject:
        raise TokenValidationError("Invalid token payload.")
    return UUID(subject)


def get_crm_token_claims(token: str) -> dict:
    try:
        return decode_crm_access_token(token)
    except InvalidTokenError as exc:
        raise TokenValidationError("Invalid or expired token.") from exc
