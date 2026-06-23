import uuid
from typing import Optional

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    ForeignKey,
    Index,
    Integer,
    SmallInteger,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class ChatAgentSettings(Base, TimestampMixin):
    __tablename__ = "chat_agent_settings"
    __table_args__ = (CheckConstraint("id = 1", name="ck_chat_agent_settings_singleton"),)

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, default=1)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[str] = mapped_column(String(128), nullable=False)
    greeting: Mapped[str] = mapped_column(String(255), nullable=False)
    status_text: Mapped[str] = mapped_column(String(128), nullable=False)
    avatar_media_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("media_assets.id", ondelete="SET NULL"), nullable=True
    )

    def __repr__(self) -> str:
        return "<ChatAgentSettings id=1>"


class ChatAgentWelcomeMessage(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "chat_agent_welcome_messages"
    __table_args__ = (Index("ix_chat_agent_welcome_messages_sort_order", "sort_order"),)

    message: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<ChatAgentWelcomeMessage sort={self.sort_order}>"


class ChatAgentQuickReply(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "chat_agent_quick_replies"
    __table_args__ = (Index("ix_chat_agent_quick_replies_key", "key", unique=True),)

    key: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    response: Mapped[str] = mapped_column(Text, nullable=False)
    href: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_external: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<ChatAgentQuickReply key={self.key!r}>"
