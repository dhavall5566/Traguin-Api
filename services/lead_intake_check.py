"""Preflight checks for CRM lead intake — duplicate leads and existing customers."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from sqlalchemy.orm import Session

from models.crm.customers import Customer
from models.crm.leads import Lead
from services.lead_customers import find_customer_by_contact
from services.lead_phone_dedup import (
    find_matching_leads,
    resolve_canonical_lead_for_intake,
)


@dataclass(frozen=True)
class LeadIntakeCheckResult:
    existing_customer: Customer | None
    canonical_lead: Lead | None
    match_reason: str | None
    duplicate_leads: list[Lead]


def check_lead_intake(
    db: Session,
    *,
    agency_id: UUID,
    email: str | None,
    phone: str | None,
    exclude_lead_id: UUID | None = None,
) -> LeadIntakeCheckResult:
    customer = find_customer_by_contact(
        db,
        agency_id=agency_id,
        email=email,
        phone=phone,
    )
    canonical, match_reason = resolve_canonical_lead_for_intake(
        db,
        agency_id=agency_id,
        phone=phone,
    )
    if (
        canonical is not None
        and exclude_lead_id is not None
        and canonical.id == exclude_lead_id
    ):
        canonical = None
        match_reason = None
    duplicates = find_matching_leads(
        db,
        agency_id=agency_id,
        phone=phone,
        exclude_lead_id=exclude_lead_id,
    )
    if canonical is not None:
        duplicates = [lead for lead in duplicates if lead.id != canonical.id]
    return LeadIntakeCheckResult(
        existing_customer=customer,
        canonical_lead=canonical,
        match_reason=match_reason,
        duplicate_leads=duplicates,
    )
