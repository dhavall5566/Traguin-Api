from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.common import ORMModel, TimestampRead


class ChatAgentSettingsBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=128)
    role: str = Field(..., min_length=1, max_length=128)
    greeting: str = Field(..., min_length=1, max_length=255)
    status_text: str = Field(..., min_length=1, max_length=128)
    avatar_media_id: UUID | None = None


class ChatAgentSettingsUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=128)
    role: str | None = Field(default=None, min_length=1, max_length=128)
    greeting: str | None = Field(default=None, min_length=1, max_length=255)
    status_text: str | None = Field(default=None, min_length=1, max_length=128)
    avatar_media_id: UUID | None = None


class ChatAgentSettingsRead(ChatAgentSettingsBase, ORMModel):
    id: int
    created_at: datetime
    updated_at: datetime


class ChatAgentWelcomeMessageBase(BaseModel):
    message: str = Field(..., min_length=1)
    sort_order: int = 0


class ChatAgentWelcomeMessageCreate(ChatAgentWelcomeMessageBase):
    pass


class ChatAgentWelcomeMessageUpdate(BaseModel):
    message: str | None = Field(default=None, min_length=1)
    sort_order: int | None = None


class ChatAgentWelcomeMessageRead(TimestampRead, ChatAgentWelcomeMessageBase):
    pass


class ChatAgentQuickReplyBase(BaseModel):
    key: str = Field(..., min_length=1, max_length=64)
    label: str = Field(..., min_length=1, max_length=255)
    response: str = Field(..., min_length=1)
    href: str | None = None
    is_external: bool = False
    sort_order: int = 0


class ChatAgentQuickReplyCreate(ChatAgentQuickReplyBase):
    pass


class ChatAgentQuickReplyUpdate(BaseModel):
    key: str | None = Field(default=None, min_length=1, max_length=64)
    label: str | None = Field(default=None, min_length=1, max_length=255)
    response: str | None = Field(default=None, min_length=1)
    href: str | None = None
    is_external: bool | None = None
    sort_order: int | None = None


class ChatAgentQuickReplyRead(TimestampRead, ChatAgentQuickReplyBase):
    pass
