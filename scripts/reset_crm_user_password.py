#!/usr/bin/env python3
"""Reset password for an existing CRM agency user."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select

from database import SessionLocal
from models.crm.tenancy import User
from utils.passwords import hash_password


def reset_crm_user_password(*, email: str, password: str) -> User:
    normalized_email = email.strip().lower()
    with SessionLocal() as db:
        user = db.scalar(select(User).where(User.email == normalized_email, User.is_deleted.is_(False)))
        if user is None:
            print(f"No CRM user found: {normalized_email}", file=sys.stderr)
            sys.exit(1)

        user.password_hash = hash_password(password)
        db.commit()
        db.refresh(user)
        return user


def main() -> None:
    parser = argparse.ArgumentParser(description="Reset a CRM user's password.")
    parser.add_argument("--email", required=True)
    parser.add_argument("--new-password", required=True, dest="new_password")
    args = parser.parse_args()

    user = reset_crm_user_password(email=args.email, password=args.new_password)
    print(f"Reset password for {user.email} (id={user.id}, agency_id={user.agency_id})")


if __name__ == "__main__":
    main()
