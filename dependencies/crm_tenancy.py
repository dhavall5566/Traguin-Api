from typing import Annotated

from fastapi import Depends, Query


def get_include_deleted(
    include_deleted: Annotated[
        bool,
        Query(description="Include soft-deleted records."),
    ] = False,
) -> bool:
    return include_deleted
