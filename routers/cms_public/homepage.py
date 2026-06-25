from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.homepage import HomepageBundleRead
from services.homepage_public import build_homepage_bundle

router = APIRouter()


@router.get("", response_model=HomepageBundleRead)
def get_homepage_bundle(db: Session = Depends(get_db)):
    return build_homepage_bundle(db)
