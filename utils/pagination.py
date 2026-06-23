from collections.abc import Callable
from typing import TypeVar

from sqlalchemy.orm import Query

from schemas.pagination import PaginatedResponse

T = TypeVar("T")
R = TypeVar("R")


def paginate(
    query: Query,
    limit: int,
    offset: int,
    *,
    transform: Callable[[T], R] | None = None,
) -> PaginatedResponse[R]:
    total = query.order_by(None).count()
    rows = query.offset(offset).limit(limit).all()
    if transform is None:
        items = rows  # type: ignore[assignment]
    else:
        items = [transform(row) for row in rows]
    return PaginatedResponse(items=items, total=total, limit=limit, offset=offset)
