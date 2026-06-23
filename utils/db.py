from typing import Any

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def commit_or_raise(
    db: Session,
    *,
    slug_field: str = "slug",
    unique_fields: tuple[str, ...] = (),
    unique_field_messages: dict[str, str] | None = None,
) -> None:
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        message = str(exc.orig) if exc.orig else str(exc)
        lowered = message.lower()
        if "foreign key" in lowered or "23503" in message or "violates foreign key" in lowered:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Cannot complete operation: related records exist.",
            ) from exc
        candidates = unique_fields or (slug_field,)
        custom = unique_field_messages or {}
        for field in candidates:
            if (
                field.lower() in lowered
                or f"ix_{field}" in lowered
                or f"uq_{field}" in lowered
                or f"uq_customers_agency_id_{field}" in lowered
            ):
                detail = custom.get(field) or f"A record with this {field} already exists."
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=detail,
                ) from exc
        if "unique" in lowered or "duplicate key" in lowered:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A record with these values already exists.",
            ) from exc
        if "slug" in lowered or f"ix_{slug_field}" in lowered:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"A record with this {slug_field} already exists.",
            ) from exc
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database constraint violation.",
        ) from exc


def apply_partial_update(model: Any, data: dict[str, Any]) -> Any:
    for key, value in data.items():
        setattr(model, key, value)
    return model
