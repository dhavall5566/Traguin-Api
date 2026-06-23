import re

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
