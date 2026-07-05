from pathlib import Path

from fastapi import Depends, FastAPI, File, Form, HTTPException, Request, Response, UploadFile, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from config import settings
from database import check_unified_database
from dependencies.auth import require_admin
from routers.admin import router as admin_router
from routers.auth import router as auth_router
from routers.crm import router as crm_router
from routers.cms_public import router as public_router

app = FastAPI(title="Traguin API")

app.add_middleware(GZipMiddleware, minimum_size=1024)

uploads_root = Path(settings.media_upload_dir).parent
uploads_root.mkdir(parents=True, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=str(uploads_root)), name="uploads")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(public_router, prefix="/api/cms/public")
app.include_router(auth_router, prefix="/api/cms/auth")
app.include_router(admin_router, prefix="/api/cms/admin", dependencies=[Depends(require_admin)])
app.include_router(crm_router, prefix="/api/crm")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Validation error.", "errors": exc.errors()},
    )


@app.exception_handler(IntegrityError)
async def integrity_exception_handler(_request: Request, exc: IntegrityError):
    message = str(exc.orig) if exc.orig else str(exc)
    if "slug" in message.lower():
        detail = (
            "A record with this slug already exists. "
            "For additional packages in the same state, the import should reuse the destination "
            "and assign a unique package slug automatically — restart the API server and try again."
        )
        code = status.HTTP_409_CONFLICT
    else:
        detail = "Database constraint violation."
        code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(status_code=code, content={"detail": detail})


@app.get("/health/db")
def health_db():
    try:
        summary = check_unified_database()
        return {
            "status": "ok",
            "message": "Unified CMS + CRM database connection successful",
            **summary,
        }
    except SQLAlchemyError as exc:
        return JSONResponse(
            status_code=503,
            content={
                "status": "error",
                "message": f"Database connection failed: {exc.orig if exc.orig else exc}",
            },
        )
    except Exception as exc:
        return JSONResponse(
            status_code=503,
            content={
                "status": "error",
                "message": f"Database connection failed: {exc}",
            },
        )
