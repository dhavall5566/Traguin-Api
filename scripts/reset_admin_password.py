#!/usr/bin/env python3
"""Reset password for an existing CMS admin user."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sqlalchemy import select

from database import SessionLocal
from models.admin_users import AdminUser
from utils.passwords import hash_password


def reset_admin_password(*, email: str, password: str) -> AdminUser:
    normalized_email = email.strip().lower()
    with SessionLocal() as db:
        user = db.scalar(select(AdminUser).where(AdminUser.email == normalized_email))
        if user is None:
            print(f"No admin user found: {normalized_email}", file=sys.stderr)
            sys.exit(1)

        user.hashed_password = hash_password(password)
        user.is_active = True
        db.commit()
        db.refresh(user)
        return user


def main() -> None:
    parser = argparse.ArgumentParser(description="Reset a CMS admin user's password.")
    parser.add_argument("--email", required=True)
    parser.add_argument("--new-password", required=True, dest="new_password")
    args = parser.parse_args()

    user = reset_admin_password(email=args.email, password=args.new_password)
    print(f"Reset password for {user.email} (id={user.id}, role={user.role})")


if __name__ == "__main__":
    main()
