#!/usr/bin/env python3
"""
Merge duplicate CRM leads that share the same phone (last 10 digits) within an agency.

Keeps the oldest lead as canonical, merges sources/messages/child rows, soft-deletes dupes.

Run from api/:
  python scripts/dedupe_crm_lead_duplicates.py --dry-run
  python scripts/dedupe_crm_lead_duplicates.py --apply
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from decimal import Decimal
from pathlib import Path
from uuid import UUID

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select
from sqlalchemy.orm import Session

from config import settings
from database import SessionLocal
from models.crm.leads import Lead, LeadActivity, LeadFollowup, LeadNote
from models.crm.tenancy import User
from services.lead_assignee import apply_returning_customer_assignee
from services.lead_phone_dedup import merge_lead_sources
from utils.lead_codes import normalize_phone_digits

DETAIL_FIELDS = (
    "travel_date",
    "address_line1",
    "address_line2",
    "city",
    "pincode",
    "state",
    "country",
    "adults_count",
    "children_count",
    "children_ages",
    "travel_type",
    "arrival_date",
    "hotel_category",
    "meal_category",
    "travel_destination",
    "occasion",
    "flight_type",
    "extra_baggage",
    "wheelchair_assistance",
    "visa_assistance",
    "travel_insurance",
    "transportation",
    "package_mode",
    "cms_form_submission_id",
    "cms_package_id",
)


def resolve_actor_user_id(db: Session, agency_id: UUID) -> UUID:
    if settings.traguin_system_user_id is not None:
        return settings.traguin_system_user_id
    user = db.scalar(
        select(User)
        .where(User.agency_id == agency_id)
        .order_by(User.created_at.asc())
        .limit(1)
    )
    if user is None:
        raise RuntimeError(f"No CRM user found for agency {agency_id}")
    return user.id


def group_duplicate_leads(db: Session) -> dict[tuple[UUID, str], list[Lead]]:
    leads = db.scalars(
        select(Lead)
        .where(Lead.is_deleted.is_(False), Lead.phone.isnot(None))
        .order_by(Lead.agency_id, Lead.created_at.asc())
    ).all()

    groups: dict[tuple[UUID, str], list[Lead]] = defaultdict(list)
    for lead in leads:
        phone_key = normalize_phone_digits(lead.phone)
        if not phone_key:
            continue
        groups[(lead.agency_id, phone_key)].append(lead)

    return {key: rows for key, rows in groups.items() if len(rows) > 1}


def merge_scalar_fields(canonical: Lead, duplicate: Lead) -> None:
    canonical.source = merge_lead_sources(canonical.source, duplicate.source)

    dup_message = (duplicate.message or "").strip()
    if dup_message:
        cur = (canonical.message or "").strip()
        if dup_message != cur:
            canonical.message = f"{cur}\n\n---\n{dup_message}" if cur else dup_message

    if duplicate.email and not (canonical.email or "").strip():
        canonical.email = duplicate.email.strip().lower()

    if duplicate.value and duplicate.value > canonical.value:
        canonical.value = duplicate.value

    if duplicate.proposal_sent_at and (
        canonical.proposal_sent_at is None
        or duplicate.proposal_sent_at < canonical.proposal_sent_at
    ):
        canonical.proposal_sent_at = duplicate.proposal_sent_at

    if duplicate.customer_id and canonical.customer_id is None:
        canonical.customer_id = duplicate.customer_id

    for field in DETAIL_FIELDS:
        if getattr(canonical, field) in (None, "", []):
            value = getattr(duplicate, field)
            if value not in (None, "", []):
                setattr(canonical, field, value)


def reassign_children(db: Session, *, canonical_id: UUID, duplicate_id: UUID) -> tuple[int, int, int]:
    notes = db.scalars(select(LeadNote).where(LeadNote.lead_id == duplicate_id)).all()
    activities = db.scalars(select(LeadActivity).where(LeadActivity.lead_id == duplicate_id)).all()
    followups = db.scalars(select(LeadFollowup).where(LeadFollowup.lead_id == duplicate_id)).all()

    for row in notes:
        row.lead_id = canonical_id
    for row in activities:
        row.lead_id = canonical_id
    for row in followups:
        row.lead_id = canonical_id

    return len(notes), len(activities), len(followups)


def merge_group(
    db: Session,
    rows: list[Lead],
    *,
    actor_user_id: UUID,
    dry_run: bool,
) -> dict[str, object]:
    canonical = rows[0]
    duplicates = rows[1:]
    summary: dict[str, object] = {
        "canonical": canonical.lead_code or str(canonical.id),
        "canonical_id": str(canonical.id),
        "duplicates": [],
        "merged_count": len(duplicates),
    }

    for duplicate in duplicates:
        dup_label = duplicate.lead_code or str(duplicate.id)
        summary["duplicates"].append(dup_label)

        if dry_run:
            continue

        merge_scalar_fields(canonical, duplicate)
        notes_moved, activities_moved, followups_moved = reassign_children(
            db,
            canonical_id=canonical.id,
            duplicate_id=duplicate.id,
        )

        db.add(
            LeadActivity(
                lead_id=canonical.id,
                type="NOTE",
                description=(
                    f"Historical duplicate lead {dup_label} merged into "
                    f"{canonical.lead_code or canonical.id} (same phone). "
                    f"Moved {notes_moved} note(s), {activities_moved} activity/activities, "
                    f"{followups_moved} follow-up(s)."
                ),
                created_by_id=actor_user_id,
            )
        )

        duplicate.is_deleted = True

    if not dry_run and duplicates:
        apply_returning_customer_assignee(
            db,
            canonical,
            agency_id=canonical.agency_id,
            customer_id=canonical.customer_id,
            prefer_original_handler=True,
        )

    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge duplicate CRM leads by phone.")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Persist merges (default is dry-run only).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be merged without writing (default).",
    )
    args = parser.parse_args()
    dry_run = not args.apply or args.dry_run

    with SessionLocal() as db:
        groups = group_duplicate_leads(db)
        if not groups:
            print("No duplicate lead groups found (active leads with same phone).")
            return

        print(f"Found {len(groups)} duplicate phone group(s).\n")
        actor_cache: dict[UUID, UUID] = {}
        merged_groups = 0
        merged_leads = 0

        for (agency_id, phone_key), rows in sorted(
            groups.items(),
            key=lambda item: (str(item[0][0]), item[0][1]),
        ):
            if agency_id not in actor_cache:
                actor_cache[agency_id] = resolve_actor_user_id(db, agency_id)
            summary = merge_group(
                db,
                rows,
                actor_user_id=actor_cache[agency_id],
                dry_run=dry_run,
            )
            merged_groups += 1
            merged_leads += int(summary["merged_count"])
            print(
                f"  phone={phone_key} agency={agency_id}\n"
                f"    keep: {summary['canonical']}\n"
                f"    merge: {', '.join(summary['duplicates'])}"
            )

        if dry_run:
            print(
                f"\nDry run complete — would merge {merged_leads} duplicate lead(s) "
                f"across {merged_groups} group(s)."
            )
            print("Re-run with --apply to persist changes.")
            return

        db.commit()
        print(
            f"\nApplied — merged {merged_leads} duplicate lead(s) "
            f"across {merged_groups} group(s)."
        )


if __name__ == "__main__":
    main()
