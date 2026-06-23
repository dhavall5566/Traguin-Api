from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import get_db

from schemas.package_import import (
    PackageImportCommitResponse,
    PackageImportExtractResponse,
    PackageImportReviewCommit,
)
from services.package_import import run_package_import_extract
from services.package_import_commit import commit_package_import
from services.package_import_mapper import review_to_creates

router = APIRouter()


@router.post("/extract", response_model=PackageImportExtractResponse)
async def extract_package_pdf(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Upload a PDF file.")
    content = await file.read()
    if not content:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty file.")
    if len(content) > 15 * 1024 * 1024:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="PDF must be under 15 MB.")

    try:
        return run_package_import_extract(db, filename=file.filename, file_bytes=content)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc


@router.post("/commit", response_model=PackageImportCommitResponse, status_code=status.HTTP_201_CREATED)
def commit_package_import_route(
    payload: PackageImportReviewCommit,
    db: Session = Depends(get_db),
):
    try:
        destination, package, itinerary = review_to_creates(payload)
        from schemas.package_import import PackageImportCommitRequest

        return commit_package_import(
            db,
            PackageImportCommitRequest(
                destination=destination,
                package=package,
                itinerary=itinerary,
            ),
        )
    except IntegrityError:
        db.rollback()
        raise
    except Exception as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create records: {exc}",
        ) from exc
