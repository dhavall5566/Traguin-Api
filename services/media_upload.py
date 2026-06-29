from __future__ import annotations

import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile, status

from config import settings
from utils.slugify import slugify

ALLOWED_IMAGE_TYPES: dict[str, str] = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
}


def ensure_media_upload_dir() -> Path:
    upload_dir = Path(settings.media_upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)
    return upload_dir


def _slug_from_filename(filename: str | None) -> str | None:
    if not filename:
        return None
    stem = Path(filename).stem.strip()
    if not stem:
        return None
    return slugify(stem)[:255] or None


def save_uploaded_image(file: UploadFile) -> tuple[str, str, str | None]:
    content_type = (file.content_type or "").split(";", 1)[0].strip().lower()
    extension = ALLOWED_IMAGE_TYPES.get(content_type)
    if extension is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported image type. Use JPEG, PNG, WebP, or GIF.",
        )

    raw = file.file.read()
    if not raw:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty.",
        )
    if len(raw) > settings.media_upload_max_bytes:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Image exceeds {settings.media_upload_max_bytes // (1024 * 1024)}MB limit.",
        )

    upload_dir = ensure_media_upload_dir()
    stored_name = f"{uuid.uuid4()}{extension}"
    target = upload_dir / stored_name
    target.write_bytes(raw)

    slug = _slug_from_filename(file.filename)
    return stored_name, content_type, slug


def public_upload_url(request_base_url: str, stored_name: str) -> str:
    base = request_base_url.rstrip("/")
    return f"{base}/uploads/media/{stored_name}"
