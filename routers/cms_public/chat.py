from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.chat import ChatAgentQuickReply, ChatAgentSettings, ChatAgentWelcomeMessage
from schemas.chat import (
    ChatAgentQuickReplyRead,
    ChatAgentSettingsRead,
    ChatAgentWelcomeMessageRead,
)
from schemas.pagination import PaginatedResponse
from utils.pagination import paginate
from utils.singleton import get_singleton_or_404

settings_router = APIRouter()
welcome_messages_router = APIRouter()
quick_replies_router = APIRouter()


@settings_router.get("", response_model=ChatAgentSettingsRead)
def get_chat_agent_settings(db: Session = Depends(get_db)):
    return get_singleton_or_404(db, ChatAgentSettings)


@welcome_messages_router.get("", response_model=PaginatedResponse[ChatAgentWelcomeMessageRead])
def list_welcome_messages(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(ChatAgentWelcomeMessage).order_by(
        ChatAgentWelcomeMessage.sort_order, ChatAgentWelcomeMessage.message
    )
    return paginate(query, limit, offset, transform=ChatAgentWelcomeMessageRead.model_validate)


@quick_replies_router.get("", response_model=PaginatedResponse[ChatAgentQuickReplyRead])
def list_quick_replies(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(ChatAgentQuickReply).order_by(
        ChatAgentQuickReply.sort_order, ChatAgentQuickReply.label
    )
    return paginate(query, limit, offset, transform=ChatAgentQuickReplyRead.model_validate)
