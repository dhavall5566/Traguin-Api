"""WhatsApp Cloud API webhooks — log delivery status (sent/delivered/failed)."""

from __future__ import annotations

import logging

from fastapi import APIRouter, HTTPException, Query, Request, Response

from config import settings

logger = logging.getLogger(__name__)

router = APIRouter(tags=["webhooks"])


@router.get("/api/webhooks/whatsapp")
async def verify_whatsapp_webhook(
    hub_mode: str | None = Query(None, alias="hub.mode"),
    hub_verify_token: str | None = Query(None, alias="hub.verify_token"),
    hub_challenge: str | None = Query(None, alias="hub.challenge"),
):
    verify_token = (settings.whatsapp_webhook_verify_token or "").strip()
    if not verify_token:
        raise HTTPException(status_code=503, detail="WhatsApp webhook verify token not configured")
    if hub_mode == "subscribe" and hub_verify_token == verify_token and hub_challenge:
        return Response(content=hub_challenge, media_type="text/plain")
    raise HTTPException(status_code=403, detail="Webhook verification failed")


@router.post("/api/webhooks/whatsapp")
async def receive_whatsapp_webhook(request: Request):
    payload = await request.json()
    for entry in payload.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            for status in value.get("statuses", []):
                errors = status.get("errors") or []
                error_detail = errors[0] if errors else {}
                logger.warning(
                    "WhatsApp delivery status=%s recipient=%s message_id=%s error=%s",
                    status.get("status"),
                    status.get("recipient_id"),
                    status.get("id"),
                    error_detail,
                )
            for message in value.get("messages", []):
                logger.info(
                    "WhatsApp inbound from=%s type=%s",
                    message.get("from"),
                    message.get("type"),
                )
    return {"status": "ok"}
