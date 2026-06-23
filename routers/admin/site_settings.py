from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.config import SiteSettings
from schemas.site_settings import SiteSettingsBase, SiteSettingsRead, SiteSettingsUpdate
from utils.singleton import get_singleton_for_admin, upsert_singleton

router = APIRouter()


@router.get("", response_model=SiteSettingsRead | None)
def get_site_settings(db: Session = Depends(get_db)):
    return get_singleton_for_admin(db, SiteSettings)


@router.patch("", response_model=SiteSettingsRead)
def update_site_settings(payload: SiteSettingsUpdate, db: Session = Depends(get_db)):
    return upsert_singleton(
        db,
        SiteSettings,
        payload.model_dump(exclude_unset=True),
        SiteSettingsBase,
    )
