from typing import Annotated

from fastapi import Query


def get_pagination(
    limit: Annotated[int, Query(ge=1, le=100, description="Page size (max 100).")] = 20,
    offset: Annotated[int, Query(ge=0, description="Number of records to skip.")] = 0,
) -> tuple[int, int]:
    return limit, offset
