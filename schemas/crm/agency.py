from pydantic import BaseModel, Field

from schemas.crm.common import CrmTimestampRead


class AgencyBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    subdomain: str = Field(..., min_length=1, max_length=255)
    logo_url: str | None = Field(default=None, max_length=2048)
    primary_color: str = Field(default="#3b82f6", max_length=32)
    secondary_color: str = Field(default="#1e293b", max_length=32)
    subscription_plan: str = Field(default="FREE", max_length=64)


class AgencyCreate(AgencyBase):
    pass


class AgencyUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    subdomain: str | None = Field(default=None, min_length=1, max_length=255)
    logo_url: str | None = Field(default=None, max_length=2048)
    primary_color: str | None = Field(default=None, max_length=32)
    secondary_color: str | None = Field(default=None, max_length=32)
    subscription_plan: str | None = Field(default=None, max_length=64)


class AgencyRead(CrmTimestampRead, AgencyBase):
    is_deleted: bool
