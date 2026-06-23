#!/usr/bin/env python3
"""Create the admin_users table if missing, then create an admin account."""

from __future__ import annotations

import argparse
import sys

from sqlalchemy import select

from database import SessionLocal, engine
from models.admin_users import AdminUser
from models.base import Base
from utils.passwords import hash_password


def ensure_table() -> None:
    AdminUser.__table__.create(bind=engine, checkfirst=True)


def create_admin_user(*, email: str, password: str, name: str, role: str = "admin") -> AdminUser:
    ensure_table()
    normalized_email = email.strip().lower()
    with SessionLocal() as db:
        existing = db.scalar(select(AdminUser).where(AdminUser.email == normalized_email))
        if existing is not None:
            print(f"Admin user already exists: {normalized_email}", file=sys.stderr)
            sys.exit(1)

        user = AdminUser(
            email=normalized_email,
            hashed_password=hash_password(password),
            name=name.strip(),
            role=role,
            is_active=True,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a CMS admin user.")
    parser.add_argument("--email", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--role", default="admin")
    args = parser.parse_args()

    user = create_admin_user(
        email=args.email,
        password=args.password,
        name=args.name,
        role=args.role,
    )
    print(f"Created admin user {user.email} (id={user.id}, role={user.role})")


if __name__ == "__main__":
    main()
