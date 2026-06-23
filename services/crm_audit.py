from __future__ import annotations

from typing import Any
from uuid import UUID

from sqlalchemy.orm import Session

from services.audit import create_audit_log


def _entity_id_str(entity_id: UUID | str | None) -> str | None:
    if entity_id is None:
        return None
    return str(entity_id)


def changed_fields_from_payload(payload: Any, *, exclude: set[str] | None = None) -> list[str]:
    if not hasattr(payload, "model_dump"):
        return []
    data = payload.model_dump(exclude_unset=True)
    skip = exclude or set()
    return [key for key in data if key not in skip]


def _with_fields(summary: str, changed_fields: list[str] | None) -> str:
    if not changed_fields:
        return summary
    return f"{summary} (fields: {', '.join(changed_fields)})"


def audit_create(
    db: Session,
    *,
    agency_id: UUID,
    user_id: UUID,
    entity_type: str,
    entity_id: UUID | str | None,
    details: str,
) -> None:
    create_audit_log(
        db,
        agency_id=agency_id,
        user_id=user_id,
        action="CREATE",
        entity_type=entity_type,
        entity_id=_entity_id_str(entity_id),
        details=details,
    )


def audit_update(
    db: Session,
    *,
    agency_id: UUID,
    user_id: UUID,
    entity_type: str,
    entity_id: UUID | str | None,
    details: str,
    changed_fields: list[str] | None = None,
) -> None:
    create_audit_log(
        db,
        agency_id=agency_id,
        user_id=user_id,
        action="UPDATE",
        entity_type=entity_type,
        entity_id=_entity_id_str(entity_id),
        details=_with_fields(details, changed_fields),
    )


def audit_delete(
    db: Session,
    *,
    agency_id: UUID,
    user_id: UUID,
    entity_type: str,
    entity_id: UUID | str | None,
    details: str,
) -> None:
    create_audit_log(
        db,
        agency_id=agency_id,
        user_id=user_id,
        action="DELETE",
        entity_type=entity_type,
        entity_id=_entity_id_str(entity_id),
        details=details,
    )
