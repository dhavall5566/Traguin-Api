from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated, Sequence
from uuid import UUID

from fastapi import Query
from sqlalchemy import inspect, or_
from sqlalchemy.orm import Query as SqlQuery

BOOL_FILTER_FIELDS = (
    "is_published",
    "is_featured",
    "show_on_homepage",
    "show_on_home",
    "show_in_gallery",
    "is_visible",
    "is_permanent",
)

STRING_EQ_FILTER_FIELDS = (
    "region",
    "status",
    "form_type",
    "employment_type",
    "usage",
    "menu_group",
)

INT_EQ_FILTER_FIELDS = ("stars",)


@dataclass(frozen=True)
class AdminListFilters:
    search: str | None = None
    destination_id: UUID | None = None
    destination_name: str | None = None
    region: str | None = None
    is_published: bool | None = None
    is_featured: bool | None = None
    show_on_homepage: bool | None = None
    show_on_home: bool | None = None
    show_in_gallery: bool | None = None
    is_visible: bool | None = None
    is_permanent: bool | None = None
    status: str | None = None
    stars: int | None = None
    form_type: str | None = None
    employment_type: str | None = None
    usage: str | None = None
    menu_group: str | None = None


def _clean_str(value: str | None) -> str | None:
    if not value:
        return None
    cleaned = value.strip()
    return cleaned or None


def get_admin_list_filters(
    search: Annotated[str | None, Query(max_length=200, description="Free-text search.")] = None,
    destination_id: Annotated[UUID | None, Query(description="Filter by destination id.")] = None,
    destination_name: Annotated[
        str | None,
        Query(max_length=255, description="Filter by destination name."),
    ] = None,
    region: Annotated[str | None, Query(max_length=32, description="Filter by region.")] = None,
    is_published: Annotated[bool | None, Query(description="Filter by published status.")] = None,
    is_featured: Annotated[bool | None, Query(description="Filter by featured status.")] = None,
    show_on_homepage: Annotated[bool | None, Query(description="Filter by homepage visibility.")] = None,
    show_on_home: Annotated[bool | None, Query(description="Filter by home visibility.")] = None,
    show_in_gallery: Annotated[bool | None, Query(description="Filter by gallery visibility.")] = None,
    is_visible: Annotated[bool | None, Query(description="Filter by visibility.")] = None,
    is_permanent: Annotated[bool | None, Query(description="Filter by permanent redirect flag.")] = None,
    status: Annotated[str | None, Query(max_length=64, description="Filter by status.")] = None,
    stars: Annotated[int | None, Query(ge=1, le=5, description="Filter by star rating.")] = None,
    form_type: Annotated[str | None, Query(max_length=64, description="Filter by form type.")] = None,
    employment_type: Annotated[
        str | None,
        Query(max_length=64, description="Filter by employment type."),
    ] = None,
    usage: Annotated[str | None, Query(max_length=64, description="Filter by usage tag.")] = None,
    menu_group: Annotated[str | None, Query(max_length=64, description="Filter by menu group.")] = None,
) -> AdminListFilters:
    return AdminListFilters(
        search=_clean_str(search),
        destination_id=destination_id,
        destination_name=_clean_str(destination_name),
        region=_clean_str(region),
        is_published=is_published,
        is_featured=is_featured,
        show_on_homepage=show_on_homepage,
        show_on_home=show_on_home,
        show_in_gallery=show_in_gallery,
        is_visible=is_visible,
        is_permanent=is_permanent,
        status=_clean_str(status),
        stars=stars,
        form_type=_clean_str(form_type),
        employment_type=_clean_str(employment_type),
        usage=_clean_str(usage),
        menu_group=_clean_str(menu_group),
    )


def _model_columns(model) -> set[str]:
    return {column.key for column in inspect(model).columns}


def apply_admin_list_filters(
    query: SqlQuery,
    model,
    filters: AdminListFilters,
    *,
    search_fields: Sequence[str],
    destination_model=None,
) -> SqlQuery:
    columns = _model_columns(model)

    for field in BOOL_FILTER_FIELDS:
        value = getattr(filters, field)
        if value is not None and field in columns:
            query = query.filter(getattr(model, field).is_(value))

    for field in STRING_EQ_FILTER_FIELDS:
        value = getattr(filters, field)
        if value and field in columns:
            query = query.filter(getattr(model, field) == value)

    for field in INT_EQ_FILTER_FIELDS:
        value = getattr(filters, field)
        if value is not None and field in columns:
            query = query.filter(getattr(model, field) == value)

    if filters.destination_id is not None and "destination_id" in columns:
        query = query.filter(model.destination_id == filters.destination_id)

    if filters.destination_name and destination_model is not None:
        query = query.filter(destination_model.name.ilike(f"%{filters.destination_name}%"))

    if filters.search:
        usable_fields = [field for field in search_fields if field in columns]
        if usable_fields:
            pattern = f"%{filters.search}%"
            query = query.filter(
                or_(*[getattr(model, field).ilike(pattern) for field in usable_fields])
            )

    return query
