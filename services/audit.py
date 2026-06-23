from uuid import UUID

from sqlalchemy.orm import Session

from models.crm.audit import AuditLog


def create_audit_log(
    db: Session,
    *,
    agency_id: UUID,
    user_id: UUID,
    action: str,
    entity_type: str,
    entity_id: str | None = None,
    details: str | None = None,
) -> AuditLog:
    entry = AuditLog(
        agency_id=agency_id,
        user_id=user_id,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        details=details,
    )
    db.add(entry)
    db.flush()
    return entry
