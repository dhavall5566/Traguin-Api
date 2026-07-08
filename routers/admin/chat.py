from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.admin_list_filters import AdminListFilters, apply_admin_list_filters, get_admin_list_filters
from dependencies.pagination import get_pagination
from models.chat import ChatAgentQuickReply, ChatAgentSettings, ChatAgentWelcomeMessage
from schemas.chat import (
    ChatAgentQuickReplyCreate,
    ChatAgentQuickReplyRead,
    ChatAgentQuickReplyUpdate,
    ChatAgentSettingsBase,
    ChatAgentSettingsRead,
    ChatAgentSettingsUpdate,
    ChatAgentWelcomeMessageCreate,
    ChatAgentWelcomeMessageRead,
    ChatAgentWelcomeMessageUpdate,
)
from schemas.pagination import PaginatedResponse
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate
from utils.singleton import get_singleton_for_admin, upsert_singleton

settings_router = APIRouter()
welcome_messages_router = APIRouter()
quick_replies_router = APIRouter()


@settings_router.get("", response_model=ChatAgentSettingsRead | None)
def get_chat_agent_settings(db: Session = Depends(get_db)):
    return get_singleton_for_admin(db, ChatAgentSettings)


@settings_router.patch("", response_model=ChatAgentSettingsRead)
def update_chat_agent_settings(
    payload: ChatAgentSettingsUpdate,
    db: Session = Depends(get_db),
):
    return upsert_singleton(
        db,
        ChatAgentSettings,
        payload.model_dump(exclude_unset=True),
        ChatAgentSettingsBase,
    )


@welcome_messages_router.get("", response_model=PaginatedResponse[ChatAgentWelcomeMessageRead])
def list_welcome_messages(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    filters: AdminListFilters = Depends(get_admin_list_filters),
):
    limit, offset = pagination
    query = db.query(ChatAgentWelcomeMessage)
    query = apply_admin_list_filters(
        query,
        ChatAgentWelcomeMessage,
        filters,
        search_fields=("message",),
    )
    query = query.order_by(ChatAgentWelcomeMessage.sort_order, ChatAgentWelcomeMessage.message)
    return paginate(query, limit, offset, transform=ChatAgentWelcomeMessageRead.model_validate)


@welcome_messages_router.get("/{message_id}", response_model=ChatAgentWelcomeMessageRead)
def get_welcome_message(message_id: UUID, db: Session = Depends(get_db)):
    item = db.get(ChatAgentWelcomeMessage, message_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat agent welcome message not found.",
        )
    return item


@welcome_messages_router.post(
    "",
    response_model=ChatAgentWelcomeMessageRead,
    status_code=status.HTTP_201_CREATED,
)
def create_welcome_message(payload: ChatAgentWelcomeMessageCreate, db: Session = Depends(get_db)):
    item = ChatAgentWelcomeMessage(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@welcome_messages_router.patch("/{message_id}", response_model=ChatAgentWelcomeMessageRead)
def update_welcome_message(
    message_id: UUID,
    payload: ChatAgentWelcomeMessageUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(ChatAgentWelcomeMessage, message_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat agent welcome message not found.",
        )
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(item)
    return item


@welcome_messages_router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_welcome_message(message_id: UUID, db: Session = Depends(get_db)):
    item = db.get(ChatAgentWelcomeMessage, message_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat agent welcome message not found.",
        )
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@quick_replies_router.get("", response_model=PaginatedResponse[ChatAgentQuickReplyRead])
def list_quick_replies(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    filters: AdminListFilters = Depends(get_admin_list_filters),
):
    limit, offset = pagination
    query = db.query(ChatAgentQuickReply)
    query = apply_admin_list_filters(
        query,
        ChatAgentQuickReply,
        filters,
        search_fields=("key", "label", "response", "href"),
    )
    query = query.order_by(ChatAgentQuickReply.sort_order, ChatAgentQuickReply.label)
    return paginate(query, limit, offset, transform=ChatAgentQuickReplyRead.model_validate)


@quick_replies_router.get("/{reply_id}", response_model=ChatAgentQuickReplyRead)
def get_quick_reply(reply_id: UUID, db: Session = Depends(get_db)):
    item = db.get(ChatAgentQuickReply, reply_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat agent quick reply not found.",
        )
    return item


@quick_replies_router.post("", response_model=ChatAgentQuickReplyRead, status_code=status.HTTP_201_CREATED)
def create_quick_reply(payload: ChatAgentQuickReplyCreate, db: Session = Depends(get_db)):
    item = ChatAgentQuickReply(**payload.model_dump())
    db.add(item)
    commit_or_raise(db, slug_field="key")
    db.refresh(item)
    return item


@quick_replies_router.patch("/{reply_id}", response_model=ChatAgentQuickReplyRead)
def update_quick_reply(
    reply_id: UUID,
    payload: ChatAgentQuickReplyUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(ChatAgentQuickReply, reply_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat agent quick reply not found.",
        )
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db, slug_field="key")
    db.refresh(item)
    return item


@quick_replies_router.delete("/{reply_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quick_reply(reply_id: UUID, db: Session = Depends(get_db)):
    item = db.get(ChatAgentQuickReply, reply_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chat agent quick reply not found.",
        )
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
#This is comment added by Nikunj