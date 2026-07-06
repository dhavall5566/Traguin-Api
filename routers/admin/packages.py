from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.packages import Package
from schemas.packages import PackageCreate, PackageListRead, PackageRead, PackageUpdate
from schemas.pagination import PaginatedResponse
from services.packages import (
    apply_package_codes,
    package_list_query,
    package_query_with_nested,
    package_to_list_read,
    package_to_read,
    sync_package_highlights,
    sync_package_moods,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


@router.get("", response_model=PaginatedResponse[PackageListRead])
def list_packages(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = package_list_query(db).order_by(Package.title)
    return paginate(query, limit, offset, transform=package_to_list_read)


@router.get("/{package_id}", response_model=PackageRead)
def get_package(package_id: UUID, db: Session = Depends(get_db)):
    package = package_query_with_nested(db).filter_by(id=package_id).one_or_none()
    if package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found.")
    return package_to_read(package)


@router.post("", response_model=PackageRead, status_code=status.HTTP_201_CREATED)
def create_package(payload: PackageCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    highlights = data.pop("highlights")
    moods = data.pop("moods")
    package = Package(**data)
    highlight_texts = [h["text"] if isinstance(h, dict) else h.text for h in highlights]
    apply_package_codes(package, highlight_texts=highlight_texts)
    db.add(package)
    db.flush()
    sync_package_highlights(db, package, highlights)
    sync_package_moods(db, package, moods)
    commit_or_raise(db)
    package = package_query_with_nested(db).filter_by(id=package.id).one()
    return package_to_read(package)


@router.patch("/{package_id}", response_model=PackageRead)
def update_package(
    package_id: UUID,
    payload: PackageUpdate,
    db: Session = Depends(get_db),
):
    package = package_query_with_nested(db).filter_by(id=package_id).one_or_none()
    if package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found.")
    data = payload.model_dump(exclude_unset=True)
    highlights = data.pop("highlights", None)
    moods = data.pop("moods", None)
    apply_partial_update(package, data)
    if highlights is not None:
        sync_package_highlights(db, package, highlights)
    if moods is not None:
        sync_package_moods(db, package, moods)
    commit_or_raise(db)
    package = package_query_with_nested(db).filter_by(id=package.id).one()
    return package_to_read(package)


@router.delete("/{package_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_package(package_id: UUID, db: Session = Depends(get_db)):
    package = db.get(Package, package_id)
    if package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found.")
    db.delete(package)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
