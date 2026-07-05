from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.destinations import Destination
from models.packages import Package
from schemas.packages import PackageListRead, PackageRead
from schemas.pagination import PaginatedResponse
from services.packages import package_list_query, package_query_with_nested, package_to_list_read, package_to_read
from utils.pagination import paginate

router = APIRouter()


def _apply_package_filters(
    query,
    *,
    q: str | None,
    published: bool | None,
    destination_id: UUID | None,
    duration: str | None,
    min_price: int | None,
    max_price: int | None,
):
    if published is not None:
        query = query.filter(Package.is_published.is_(published))
    if destination_id is not None:
        query = query.filter(Package.destination_id == destination_id)
    if duration:
        query = query.filter(Package.duration_label == duration.strip())
    if min_price is not None:
        query = query.filter(Package.price >= min_price)
    if max_price is not None:
        query = query.filter(Package.price <= max_price)
    if q:
        term = f"%{q.strip()}%"
        query = query.filter(
            or_(
                Package.title.ilike(term),
                Package.slug.ilike(term),
                Destination.name.ilike(term),
            )
        )
    return query


@router.get("/filters")
def list_package_filters(db: Session = Depends(get_db)):
    """Distinct filter values for the CRM packages catalog."""
    destination_rows = (
        db.query(Destination.id, Destination.name, func.count(Package.id))
        .join(Package, Package.destination_id == Destination.id)
        .group_by(Destination.id, Destination.name)
        .order_by(Destination.name)
        .all()
    )
    duration_rows = (
        db.query(Package.duration_label)
        .distinct()
        .order_by(Package.duration_label)
        .all()
    )
    return {
        "destinations": [
            {"id": str(row[0]), "name": row[1], "count": int(row[2])} for row in destination_rows
        ],
        "durations": [row[0] for row in duration_rows if row[0]],
    }


@router.get("", response_model=PaginatedResponse[PackageListRead])
def list_cms_packages(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    q: str | None = Query(default=None, max_length=128, description="Search title, slug, or destination."),
    published: bool | None = Query(
        default=None,
        description="When set, filter by website publish flag. Omit to return all packages.",
    ),
    destination_id: UUID | None = Query(default=None, description="Filter by CMS destination id."),
    duration: str | None = Query(default=None, max_length=64, description="Exact duration label match."),
    min_price: int | None = Query(default=None, ge=0, description="Minimum package price (INR)."),
    max_price: int | None = Query(default=None, ge=0, description="Maximum package price (INR)."),
):
    """Full CMS catalog for CRM — includes unpublished/internal packages."""
    limit, offset = pagination
    query = package_list_query(db)
    query = _apply_package_filters(
        query,
        q=q,
        published=published,
        destination_id=destination_id,
        duration=duration,
        min_price=min_price,
        max_price=max_price,
    )
    query = query.order_by(Package.title)
    return paginate(query, limit, offset, transform=package_to_list_read)


@router.get("/{package_id}", response_model=PackageRead)
def get_cms_package(package_id: UUID, db: Session = Depends(get_db)):
    package = package_query_with_nested(db).filter_by(id=package_id).one_or_none()
    if package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found.")
    return package_to_read(package)
