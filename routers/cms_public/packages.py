from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.packages import Package
from schemas.packages import PackageRead
from schemas.pagination import PaginatedResponse
from services.packages import package_query_with_nested, package_to_read
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[PackageRead])
def list_packages(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = (
        package_query_with_nested(db)
        .filter(Package.is_published.is_(True))
        .order_by(Package.title)
    )
    return paginate(query, limit, offset, transform=package_to_read)


@router.get("/slug/{slug}", response_model=PackageRead)
def get_package_by_slug(slug: str, db: Session = Depends(get_db)):
    package = (
        package_query_with_nested(db)
        .filter_by(slug=slug, is_published=True)
        .one_or_none()
    )
    if package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found.")
    return package_to_read(package)
