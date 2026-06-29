"""Short-lived in-process cache for expensive read endpoints."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")

_cache: dict[str, tuple[float, object]] = {}


def get_cached_response(key: str, ttl_seconds: float, factory: Callable[[], T]) -> T:
    now = time.monotonic()
    cached = _cache.get(key)
    if cached is not None:
        expires_at, value = cached
        if now < expires_at:
            return value  # type: ignore[return-value]

    value = factory()
    _cache[key] = (now + ttl_seconds, value)
    return value


def invalidate_cached_response(key: str) -> None:
    _cache.pop(key, None)
