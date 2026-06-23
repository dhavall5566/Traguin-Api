from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.config import SiteSettings
from schemas.site_settings import SiteSettingsRead

router = APIRouter()


@router.get("", response_model=SiteSettingsRead)
def get_site_settings(db: Session = Depends(get_db)):
    settings = db.get(SiteSettings, 1)
    if settings is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site settings not found.")
    return settings
