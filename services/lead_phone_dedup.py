"""Merge duplicate phone inquiries into a single canonical CRM lead."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.crm.leads import Lead, LeadActivity
from utils.lead_codes import normalize_phone_digits


def _parse_source_parts(source: str | None) -> list[str]:
    if not source or not source.strip():
        return []
    parts: list[str] = []
    for token in source.split(","):
        cleaned = token.strip()
        if cleaned and cleaned not in parts:
            parts.append(cleaned)
    return parts


def merge_lead_sources(existing: str | None, new: str | None) -> str | None:
    """Combine unique source labels into one comma-separated field."""
    parts = _parse_source_parts(existing)
    incoming = (new or "").strip()
    if incoming and incoming not in parts:
        parts.append(incoming)
    return ", ".join(parts) if parts else None


def find_canonical_lead_by_phone(
    db: Session,
    *,
    agency_id: UUID,
    phone: str | None,
) -> Lead | None:
    """Return the oldest active lead with this phone (canonical record)."""
    phone_key = normalize_phone_digits(phone)
    if not phone_key:
        return None

    candidates = db.scalars(
        select(Lead)
        .where(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.phone.isnot(None),
        )
        .order_by(Lead.created_at.asc())
        .limit(250)
    ).all()

    for candidate in candidates:
        if normalize_phone_digits(candidate.phone) == phone_key:
            return candidate
    return None


def resolve_canonical_lead_for_intake(
    db: Session,
    *,
    agency_id: UUID,
    phone: str | None,
) -> tuple[Lead | None, str | None]:
    """Return the oldest active lead with this phone — (lead, match_reason)."""
    by_phone = find_canonical_lead_by_phone(db, agency_id=agency_id, phone=phone)
    if by_phone is not None:
        return by_phone, "phone"
    return None, None


def find_matching_leads(
    db: Session,
    *,
    agency_id: UUID,
    phone: str | None,
    exclude_lead_id: UUID | None = None,
    limit: int = 5,
) -> list[Lead]:
    """Active leads with the same phone (newest first), for duplicate warnings."""
    phone_key = normalize_phone_digits(phone)
    if not phone_key:
        return []

    candidates = db.scalars(
        select(Lead)
        .where(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.phone.isnot(None),
        )
        .order_by(Lead.created_at.desc())
        .limit(250)
    ).all()

    matches: list[Lead] = []
    for candidate in candidates:
        if exclude_lead_id is not None and candidate.id == exclude_lead_id:
            continue
        if normalize_phone_digits(candidate.phone) != phone_key:
            continue
        matches.append(candidate)
        if len(matches) >= limit:
            break
    return matches


def find_prior_leads_by_phone(
    db: Session,
    *,
    agency_id: UUID,
    phone: str | None,
    exclude_lead_id: UUID | None = None,
    limit: int = 5,
) -> list[Lead]:
    """Other leads with the same phone (newest first), excluding one id."""
    phone_key = normalize_phone_digits(phone)
    if not phone_key:
        return []

    candidates = db.scalars(
        select(Lead)
        .where(
            Lead.agency_id == agency_id,
            Lead.is_deleted.is_(False),
            Lead.phone.isnot(None),
        )
        .order_by(Lead.created_at.desc())
        .limit(250)
    ).all()

    matches: list[Lead] = []
    for candidate in candidates:
        if exclude_lead_id is not None and candidate.id == exclude_lead_id:
            continue
        if normalize_phone_digits(candidate.phone) != phone_key:
            continue
        matches.append(candidate)
        if len(matches) >= limit:
            break
    return matches


def merge_inquiry_into_existing_lead(
    db: Session,
    existing: Lead,
    *,
    new_source: str | None,
    created_by_id: UUID,
    message: str | None = None,
    email: str | None = None,
    cms_package_id: UUID | None = None,
    activity_detail: str | None = None,
) -> Lead:
    """Append source and context to the canonical lead instead of creating a duplicate."""
    merged_source = merge_lead_sources(existing.source, new_source)
    if merged_source:
        existing.source = merged_source

    if email and not (existing.email or "").strip():
        existing.email = email.strip().lower()

    if message:
        incoming = message.strip()
        current = (existing.message or "").strip()
        if incoming and incoming != current:
            existing.message = f"{current}\n\n---\n{incoming}" if current else incoming

    if cms_package_id and existing.cms_package_id is None:
        existing.cms_package_id = cms_package_id

    detail = activity_detail or (
        f"Returning contact — new inquiry from {new_source or 'unknown source'}. "
        f"Merged into lead {existing.lead_code or existing.id}."
    )
    db.add(
        LeadActivity(
            lead_id=existing.id,
            type="NOTE",
            description=detail,
            created_by_id=created_by_id,
        )
    )
    return existing
