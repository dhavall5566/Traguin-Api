from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from database import get_db
from schemas.homepage import HomepageBundleRead
from services.homepage_public import build_homepage_bundle
from utils.response_cache import get_cached_response

router = APIRouter()


@router.get("", response_model=HomepageBundleRead)
def get_homepage_bundle(response: Response, db: Session = Depends(get_db)):
    payload = get_cached_response(
        "homepage-bundle",
        ttl_seconds=30,
        factory=lambda: build_homepage_bundle(db),
    )
    response.headers["Cache-Control"] = "public, max-age=30, stale-while-revalidate=120"
    return payload
