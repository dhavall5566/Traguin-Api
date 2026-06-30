"""Password hashing via bcrypt directly (do not use passlib — breaks on bcrypt 4.1+)."""

import re

import bcrypt

PASSWORD_MIN_LENGTH = 8
_PASSWORD_HAS_LETTER = re.compile(r"[A-Za-z]")
_PASSWORD_HAS_NUMBER = re.compile(r"\d")
_PASSWORD_HAS_SYMBOL = re.compile(r"[^A-Za-z0-9]")


def validate_password_strength(password: str) -> None:
    if len(password) < PASSWORD_MIN_LENGTH:
        raise ValueError(f"Password must be at least {PASSWORD_MIN_LENGTH} characters.")
    if not _PASSWORD_HAS_LETTER.search(password):
        raise ValueError("Password must include at least one letter.")
    if not _PASSWORD_HAS_NUMBER.search(password):
        raise ValueError("Password must include at least one number.")
    if not _PASSWORD_HAS_SYMBOL.search(password):
        raise ValueError("Password must include at least one symbol.")


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str | None) -> bool:
    if not plain_password or not hashed_password:
        return False
    try:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError, AttributeError):
        return False
