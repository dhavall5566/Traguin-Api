from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.admin_list_filters import AdminListFilters, apply_admin_list_filters, get_admin_list_filters
from dependencies.pagination import get_pagination
from models.content import (
    AboutClientLogo,
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
    AboutClientLogoCreate,
    AboutClientLogoRead,
    AboutClientLogoUpdate,
    AboutPageHeaderBase,
    AboutPageHeaderRead,
    AboutPageHeaderUpdate,
    AboutStorySectionCreate,
    AboutStorySectionRead,
    AboutStorySectionUpdate,
    CareersPageExtrasBase,
    CareersPageExtrasRead,
    CareersPageExtrasUpdate,
    ConciergeServiceCreate,
    ConciergeServiceRead,
    ConciergeServiceUpdate,
    HomepagePromoBase,
    HomepagePromoRead,
    HomepagePromoUpdate,
    HomepageRegionPanelCreate,
    HomepageRegionPanelRead,
    HomepageRegionPanelUpdate,
    JobOpeningCreate,
    JobOpeningRead,
    JobOpeningUpdate,
    JourneyProcessStepCreate,
    JourneyProcessStepRead,
    JourneyProcessStepUpdate,
    TravelExpertSettingsBase,
    TravelExpertSettingsRead,
    TravelExpertSettingsUpdate,
    ValuePropositionCreate,
    ValuePropositionRead,
    ValuePropositionUpdate,
)
from schemas.pagination import PaginatedResponse
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate
from utils.singleton import get_singleton_for_admin, upsert_singleton

journey_process_steps_router = APIRouter()
value_propositions_router = APIRouter()
concierge_services_router = APIRouter()
homepage_region_panels_router = APIRouter()
about_story_sections_router = APIRouter()
about_client_logos_router = APIRouter()
job_openings_router = APIRouter()
homepage_promo_router = APIRouter()
travel_expert_settings_router = APIRouter()
about_page_header_router = APIRouter()
careers_page_extras_router = APIRouter()


def _simple_crud(
    router,
    model,
    create_schema,
    read_schema,
    update_schema,
    order_by,
    not_found: str,
    search_fields: tuple[str, ...],
):
    @router.get("", response_model=PaginatedResponse[read_schema])
    def list_items(
        db: Session = Depends(get_db),
        pagination: tuple[int, int] = Depends(get_pagination),
        filters: AdminListFilters = Depends(get_admin_list_filters),
    ):
        limit, offset = pagination
        query = db.query(model)
        query = apply_admin_list_filters(query, model, filters, search_fields=search_fields)
        query = query.order_by(*order_by)
        return paginate(query, limit, offset, transform=read_schema.model_validate)

    @router.get("/{item_id}", response_model=read_schema)
    def get_item(item_id: UUID, db: Session = Depends(get_db)):
        item = db.get(model, item_id)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=not_found)
        return item

    @router.post("", response_model=read_schema, status_code=status.HTTP_201_CREATED)
    def create_item(payload: create_schema, db: Session = Depends(get_db)):
        item = model(**payload.model_dump())
        db.add(item)
        commit_or_raise(db)
        db.refresh(item)
        return item

    @router.patch("/{item_id}", response_model=read_schema)
    def update_item(item_id: UUID, payload: update_schema, db: Session = Depends(get_db)):
        item = db.get(model, item_id)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=not_found)
        apply_partial_update(item, payload.model_dump(exclude_unset=True))
        commit_or_raise(db)
        db.refresh(item)
        return item

    @router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_item(item_id: UUID, db: Session = Depends(get_db)):
        item = db.get(model, item_id)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=not_found)
        db.delete(item)
        commit_or_raise(db)
        return Response(status_code=status.HTTP_204_NO_CONTENT)


_simple_crud(
    journey_process_steps_router,
    JourneyProcessStep,
    JourneyProcessStepCreate,
    JourneyProcessStepRead,
    JourneyProcessStepUpdate,
    (JourneyProcessStep.sort_order, JourneyProcessStep.title),
    "Journey process step not found.",
    ("title", "step_label", "description", "detail", "icon_key"),
)
_simple_crud(
    value_propositions_router,
    ValueProposition,
    ValuePropositionCreate,
    ValuePropositionRead,
    ValuePropositionUpdate,
    (ValueProposition.sort_order, ValueProposition.title),
    "Value proposition not found.",
    ("title", "step_label", "description", "highlight", "icon_key"),
)
_simple_crud(
    concierge_services_router,
    ConciergeService,
    ConciergeServiceCreate,
    ConciergeServiceRead,
    ConciergeServiceUpdate,
    (ConciergeService.sort_order, ConciergeService.title),
    "Concierge service not found.",
    ("slug", "title", "description", "number_label", "icon_key"),
)
_simple_crud(
    homepage_region_panels_router,
    HomepageRegionPanel,
    HomepageRegionPanelCreate,
    HomepageRegionPanelRead,
    HomepageRegionPanelUpdate,
    (HomepageRegionPanel.sort_order, HomepageRegionPanel.key),
    "Homepage region panel not found.",
    ("key", "label", "title", "description", "stat_text", "href", "mood"),
)
_simple_crud(
    about_story_sections_router,
    AboutStorySection,
    AboutStorySectionCreate,
    AboutStorySectionRead,
    AboutStorySectionUpdate,
    (AboutStorySection.sort_order, AboutStorySection.title),
    "About story section not found.",
    ("title", "body"),
)
_simple_crud(
    about_client_logos_router,
    AboutClientLogo,
    AboutClientLogoCreate,
    AboutClientLogoRead,
    AboutClientLogoUpdate,
    (AboutClientLogo.sort_order, AboutClientLogo.name),
    "About client logo not found.",
    ("slug", "name"),
)


@job_openings_router.get("", response_model=PaginatedResponse[JobOpeningRead])
def list_job_openings(
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
    filters: AdminListFilters = Depends(get_admin_list_filters),
):
    limit, offset = pagination
    query = db.query(JobOpening)
    query = apply_admin_list_filters(
        query,
        JobOpening,
        filters,
        search_fields=("slug", "title", "location", "employment_type", "description"),
    )
    query = query.order_by(JobOpening.sort_order, JobOpening.title)
    return paginate(query, limit, offset, transform=JobOpeningRead.model_validate)


@job_openings_router.get("/{opening_id}", response_model=JobOpeningRead)
def get_job_opening(opening_id: UUID, db: Session = Depends(get_db)):
    item = db.get(JobOpening, opening_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job opening not found.")
    return item


@job_openings_router.post("", response_model=JobOpeningRead, status_code=status.HTTP_201_CREATED)
def create_job_opening(payload: JobOpeningCreate, db: Session = Depends(get_db)):
    item = JobOpening(**payload.model_dump())
    db.add(item)
    commit_or_raise(db)
    db.refresh(item)
    return item


@job_openings_router.patch("/{opening_id}", response_model=JobOpeningRead)
def update_job_opening(
    opening_id: UUID,
    payload: JobOpeningUpdate,
    db: Session = Depends(get_db),
):
    item = db.get(JobOpening, opening_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job opening not found.")
    apply_partial_update(item, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(item)
    return item


@job_openings_router.delete("/{opening_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job_opening(opening_id: UUID, db: Session = Depends(get_db)):
    item = db.get(JobOpening, opening_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job opening not found.")
    db.delete(item)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@homepage_promo_router.get("", response_model=HomepagePromoRead | None)
def get_homepage_promo(db: Session = Depends(get_db)):
    return get_singleton_for_admin(db, HomepagePromo)


@homepage_promo_router.patch("", response_model=HomepagePromoRead)
def update_homepage_promo(payload: HomepagePromoUpdate, db: Session = Depends(get_db)):
    return upsert_singleton(
        db,
        HomepagePromo,
        payload.model_dump(exclude_unset=True),
        HomepagePromoBase,
    )


@travel_expert_settings_router.get("", response_model=TravelExpertSettingsRead | None)
def get_travel_expert_settings(db: Session = Depends(get_db)):
    return get_singleton_for_admin(db, TravelExpertSettings)


@travel_expert_settings_router.patch("", response_model=TravelExpertSettingsRead)
def update_travel_expert_settings(
    payload: TravelExpertSettingsUpdate,
    db: Session = Depends(get_db),
):
    return upsert_singleton(
        db,
        TravelExpertSettings,
        payload.model_dump(exclude_unset=True),
        TravelExpertSettingsBase,
    )


@about_page_header_router.get("", response_model=AboutPageHeaderRead | None)
def get_about_page_header(db: Session = Depends(get_db)):
    return get_singleton_for_admin(db, AboutPageHeader)


@about_page_header_router.patch("", response_model=AboutPageHeaderRead)
def update_about_page_header(payload: AboutPageHeaderUpdate, db: Session = Depends(get_db)):
    return upsert_singleton(
        db,
        AboutPageHeader,
        payload.model_dump(exclude_unset=True),
        AboutPageHeaderBase,
    )


@careers_page_extras_router.get("", response_model=CareersPageExtrasRead | None)
def get_careers_page_extras(db: Session = Depends(get_db)):
    return get_singleton_for_admin(db, CareersPageExtras)


@careers_page_extras_router.patch("", response_model=CareersPageExtrasRead)
def update_careers_page_extras(payload: CareersPageExtrasUpdate, db: Session = Depends(get_db)):
    return upsert_singleton(
        db,
        CareersPageExtras,
        payload.model_dump(exclude_unset=True),
        CareersPageExtrasBase,
    )
