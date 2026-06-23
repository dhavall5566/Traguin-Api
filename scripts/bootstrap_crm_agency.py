#!/usr/bin/env python3
"""Bootstrap the first CRM agency and admin user (chicken-and-egg setup)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select

from database import SessionLocal
from models.crm.tenancy import Agency, User
from utils.passwords import hash_password


def bootstrap_crm_agency(
    *,
    agency_name: str,
    subdomain: str,
    user_email: str,
    user_password: str,
    user_name: str,
    subscription_plan: str = "PRO",
) -> tuple[Agency, User]:
    normalized_email = user_email.strip().lower()
    normalized_subdomain = subdomain.strip().lower()

    with SessionLocal() as db:
        if db.scalar(select(User).where(User.email == normalized_email)):
            print(f"CRM user already exists: {normalized_email}", file=sys.stderr)
            sys.exit(1)
        if db.scalar(select(Agency).where(Agency.subdomain == normalized_subdomain)):
            print(f"Agency subdomain already exists: {normalized_subdomain}", file=sys.stderr)
            sys.exit(1)

        agency = Agency(
            name=agency_name.strip(),
            subdomain=normalized_subdomain,
            subscription_plan=subscription_plan,
        )
        db.add(agency)
        db.flush()

        user = User(
            email=normalized_email,
            name=user_name.strip(),
            password_hash=hash_password(user_password),
            agency_id=agency.id,
        )
        db.add(user)
        db.commit()
        db.refresh(agency)
        db.refresh(user)
        return agency, user


def main() -> None:
    parser = argparse.ArgumentParser(description="Bootstrap a CRM agency and its first user.")
    parser.add_argument("--agency-name", required=True)
    parser.add_argument("--subdomain", required=True)
    parser.add_argument("--email", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--name", required=True, help="Display name for the first user")
    parser.add_argument("--subscription-plan", default="PRO")
    args = parser.parse_args()

    agency, user = bootstrap_crm_agency(
        agency_name=args.agency_name,
        subdomain=args.subdomain,
        user_email=args.email,
        user_password=args.password,
        user_name=args.name,
        subscription_plan=args.subscription_plan,
    )
    print(f"Created agency {agency.name} (id={agency.id}, subdomain={agency.subdomain})")
    print(f"Created user {user.email} (id={user.id}, agency_id={user.agency_id})")


if __name__ == "__main__":
    main()
