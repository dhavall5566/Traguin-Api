from __future__ import annotations

import mimetypes
import uuid
from pathlib import Path
from urllib.parse import urlparse

import httpx
from fastapi import HTTPException, UploadFile, status

from config import settings
from utils.slugify import slugify

ALLOWED_IMAGE_TYPES: dict[str, str] = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
}

LOCAL_UPLOAD_PATH_PREFIX = "/uploads/media/"


def ensure_media_upload_dir() -> Path:
    upload_dir = Path(settings.media_upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)
    return upload_dir


def resolve_public_base_url(request_base_url: str | None = None) -> str:
    if settings.api_public_base_url:
        return settings.api_public_base_url.rstrip("/")
    return (request_base_url or "http://127.0.0.1:8001").rstrip("/")


def public_upload_url(request_base_url: str | None, stored_name: str) -> str:
    base = resolve_public_base_url(request_base_url)
    return f"{base}{LOCAL_UPLOAD_PATH_PREFIX}{stored_name}"


def is_local_media_url(url: str) -> bool:
    raw = (url or "").strip()
    if not raw:
        return False
    if raw.startswith(LOCAL_UPLOAD_PATH_PREFIX):
        return True
    bases = [
        settings.api_public_base_url,
        "http://127.0.0.1:8001",
        "http://localhost:8001",
        "https://api.traguin.in",
        "http://api.traguin.in",
    ]
    for base in bases:
        if not base:
            continue
        prefix = f"{base.rstrip('/')}{LOCAL_UPLOAD_PATH_PREFIX}"
        if raw.startswith(prefix):
            return True
    return False


def _extension_for_content_type(content_type: str, url: str | None = None) -> str:
    normalized = (content_type or "").split(";", 1)[0].strip().lower()
    extension = ALLOWED_IMAGE_TYPES.get(normalized)
    if extension:
        return extension
    if url:
        guessed = mimetypes.guess_extension(normalized)
        if guessed in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
            return ".jpg" if guessed == ".jpeg" else guessed
        path_ext = Path(urlparse(url).path).suffix.lower()
        if path_ext in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
            return ".jpg" if path_ext == ".jpeg" else path_ext
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Unsupported image type. Use JPEG, PNG, WebP, or GIF.",
    )


def _validate_image_bytes(raw: bytes, content_type: str) -> None:
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
    _extension_for_content_type(content_type)


def save_image_bytes(raw: bytes, content_type: str) -> tuple[str, str]:
    normalized = (content_type or "").split(";", 1)[0].strip().lower()
    _validate_image_bytes(raw, normalized)
    extension = _extension_for_content_type(normalized)
    upload_dir = ensure_media_upload_dir()
    stored_name = f"{uuid.uuid4()}{extension}"
    target = upload_dir / stored_name
    target.write_bytes(raw)
    return stored_name, normalized


def _slug_from_filename(filename: str | None) -> str | None:
    if not filename:
        return None
    stem = Path(filename).stem.strip()
    if not stem:
        return None
    return slugify(stem)[:255] or None


def delete_local_media_file(url: str) -> bool:
    """Remove the on-disk upload for a local media URL. Returns True if a file was deleted."""
    raw = (url or "").strip()
    if not raw or not is_local_media_url(raw):
        return False

    stored_name = raw.split(LOCAL_UPLOAD_PATH_PREFIX, 1)[-1].split("?", 1)[0].strip()
    if not stored_name or ".." in stored_name or "/" in stored_name or "\\" in stored_name:
        return False

    path = Path(settings.media_upload_dir) / stored_name
    if path.is_file():
        path.unlink()
        return True
    return False


def save_uploaded_image(file: UploadFile) -> tuple[str, str, str | None]:
    content_type = (file.content_type or "").split(";", 1)[0].strip().lower()
    raw = file.file.read()
    stored_name, mime_type = save_image_bytes(raw, content_type)
    slug = _slug_from_filename(file.filename)
    return stored_name, mime_type, slug


def download_remote_image(url: str) -> tuple[bytes, str]:
    try:
        response = httpx.get(url, timeout=60.0, follow_redirects=True)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Could not download image: {exc}",
        ) from exc

    content_type = (response.headers.get("content-type") or "image/jpeg").split(";", 1)[0].strip().lower()
    raw = response.content
    _validate_image_bytes(raw, content_type)
    return raw, content_type


def ingest_remote_image_url(
    url: str,
    *,
    request_base_url: str | None = None,
) -> tuple[str, str, str]:
    """Download a remote image and store it on the API server."""
    if is_local_media_url(url):
        mime_type = mimetypes.guess_type(url)[0] or "image/jpeg"
        stored_name = url.split(LOCAL_UPLOAD_PATH_PREFIX, 1)[-1].split("?", 1)[0]
        return stored_name, mime_type, url

    raw, content_type = download_remote_image(url)
    stored_name, mime_type = save_image_bytes(raw, content_type)
    return stored_name, mime_type, public_upload_url(request_base_url, stored_name)
