from typing import TypeVar

from fastapi import HTTPException, status
from pydantic import BaseModel, ValidationError
from sqlalchemy.orm import Session

from utils.db import apply_partial_update, commit_or_raise

T = TypeVar("T")


def get_singleton_or_404(db: Session, model: type[T], singleton_id: int = 1) -> T:
    instance = db.get(model, singleton_id)
    if instance is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{model.__name__} not found.",
        )
    return instance


def get_singleton_for_admin(db: Session, model: type[T], singleton_id: int = 1) -> T | None:
    """Admin GET: return None when unseeded so the UI can show an empty form (no 404)."""
    return db.get(model, singleton_id)


def upsert_singleton(
    db: Session,
    model: type[T],
    update_data: dict,
    base_schema: type[BaseModel],
    *,
    singleton_id: int = 1,
) -> T:
    instance = db.get(model, singleton_id)
    if instance is None:
        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"{model.__name__} do not exist yet. Provide all required fields on first update.",
            )
        try:
            validated = base_schema.model_validate(update_data)
        except ValidationError as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "message": f"Missing or invalid fields for initial {model.__name__}.",
                    "errors": exc.errors(),
                },
            ) from exc
        instance = model(id=singleton_id, **validated.model_dump())  # type: ignore[call-arg]
        db.add(instance)
    else:
        apply_partial_update(instance, update_data)
    commit_or_raise(db)
    db.refresh(instance)
    return instance
