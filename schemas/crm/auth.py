from pydantic import BaseModel, EmailStr, Field

from schemas.auth import TokenResponse
from schemas.crm.agency import AgencyRead
from schemas.crm.user import UserRead


class CrmLoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1)


class CrmTokenResponse(TokenResponse):
    pass


class CrmTokenClaims(BaseModel):
    user_id: str
    email: str
    agency_id: str | None
    token_type: str


class CrmSessionRead(BaseModel):
    user: UserRead
    agency: AgencyRead
