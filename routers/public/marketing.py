from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.pagination import get_pagination
from models.content import (
    AboutPageHeader,
    AboutStorySection,
    CareersPageExtras,
    ConciergeService,
    HomepagePromo,
    HomepageRegionPanel,
    JobOpening,
    JourneyProcessStep,
    TravelExpertSettings,
    ValueProposition,
)
from schemas.marketing import (
    AboutPageHeaderRead,
    AboutStorySectionRead,
    CareersPageExtrasRead,
    ConciergeServiceRead,
    HomepagePromoRead,
    HomepageRegionPanelRead,
    JobOpeningRead,
    JourneyProcessStepRead,
    TravelExpertSettingsRead,
    ValuePropositionRead,
)
from schemas.pagination import PaginatedResponse
from utils.pagination import paginate
from utils.singleton import get_singleton_or_404

journey_process_steps_router = APIRouter()
value_propositions_router = APIRouter()
concierge_services_router = APIRouter()
homepage_region_panels_router = APIRouter()
about_story_sections_router = APIRouter()
job_openings_router = APIRouter()
homepage_promo_router = APIRouter()
travel_expert_settings_router = APIRouter()
about_page_header_router = APIRouter()
careers_page_extras_router = APIRouter()


@journey_process_steps_router.get("", response_model=PaginatedResponse[JourneyProcessStepRead])
def list_journey_process_steps(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(JourneyProcessStep).order_by(
        JourneyProcessStep.sort_order, JourneyProcessStep.title
    )
    return paginate(query, limit, offset, transform=JourneyProcessStepRead.model_validate)


@value_propositions_router.get("", response_model=PaginatedResponse[ValuePropositionRead])
def list_value_propositions(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(ValueProposition).order_by(
        ValueProposition.sort_order, ValueProposition.title
    )
    return paginate(query, limit, offset, transform=ValuePropositionRead.model_validate)


@concierge_services_router.get("", response_model=PaginatedResponse[ConciergeServiceRead])
def list_concierge_services(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(ConciergeService).order_by(
        ConciergeService.sort_order, ConciergeService.title
    )
    return paginate(query, limit, offset, transform=ConciergeServiceRead.model_validate)


@concierge_services_router.get("/slug/{slug}", response_model=ConciergeServiceRead)
def get_concierge_service_by_slug(slug: str, db: Session = Depends(get_db)):
    item = db.query(ConciergeService).filter_by(slug=slug).one_or_none()
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Concierge service not found.",
        )
    return item


@homepage_region_panels_router.get("", response_model=PaginatedResponse[HomepageRegionPanelRead])
def list_homepage_region_panels(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(HomepageRegionPanel).order_by(
        HomepageRegionPanel.sort_order, HomepageRegionPanel.key
    )
    return paginate(query, limit, offset, transform=HomepageRegionPanelRead.model_validate)


@about_story_sections_router.get("", response_model=PaginatedResponse[AboutStorySectionRead])
def list_about_story_sections(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(AboutStorySection).order_by(
        AboutStorySection.sort_order, AboutStorySection.title
    )
    return paginate(query, limit, offset, transform=AboutStorySectionRead.model_validate)


@job_openings_router.get("", response_model=PaginatedResponse[JobOpeningRead])
def list_job_openings(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = (
        db.query(JobOpening)
        .filter(JobOpening.is_published.is_(True))
        .order_by(JobOpening.sort_order, JobOpening.title)
    )
    return paginate(query, limit, offset, transform=JobOpeningRead.model_validate)


@job_openings_router.get("/slug/{slug}", response_model=JobOpeningRead)
def get_job_opening_by_slug(slug: str, db: Session = Depends(get_db)):
    item = db.query(JobOpening).filter_by(slug=slug, is_published=True).one_or_none()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job opening not found.")
    return item


@homepage_promo_router.get("", response_model=HomepagePromoRead)
def get_homepage_promo(db: Session = Depends(get_db)):
    return get_singleton_or_404(db, HomepagePromo)


@travel_expert_settings_router.get("", response_model=TravelExpertSettingsRead)
def get_travel_expert_settings(db: Session = Depends(get_db)):
    return get_singleton_or_404(db, TravelExpertSettings)


@about_page_header_router.get("", response_model=AboutPageHeaderRead)
def get_about_page_header(db: Session = Depends(get_db)):
    return get_singleton_or_404(db, AboutPageHeader)


@careers_page_extras_router.get("", response_model=CareersPageExtrasRead)
def get_careers_page_extras(db: Session = Depends(get_db)):
    return get_singleton_or_404(db, CareersPageExtras)
