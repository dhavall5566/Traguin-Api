from fastapi import APIRouter

from routers.public.chat import (
    quick_replies_router as chat_quick_replies_router,
    settings_router as chat_settings_router,
    welcome_messages_router as chat_welcome_messages_router,
)
from routers.public.config import (
    company_stats_router,
    global_page_cta_router,
    navigation_router,
    page_heroes_router,
    page_metadata_router,
    redirects_router,
    site_ctas_router,
)
from routers.public.destinations import router as destinations_router
from routers.public.experiences import router as experiences_router
from routers.public.faqs import router as faqs_router
from routers.public.form_submissions import router as form_submissions_router
from routers.public.gallery import (
    client_stories_router,
    gallery_categories_router,
    gallery_items_router,
)
from routers.public.hotels import router as hotels_router
from routers.public.itineraries import router as itineraries_router
from routers.public.legal import router as legal_router
from routers.public.marketing import (
    about_page_header_router,
    about_story_sections_router,
    careers_page_extras_router,
    concierge_services_router,
    homepage_promo_router,
    homepage_region_panels_router,
    job_openings_router,
    journey_process_steps_router,
    travel_expert_settings_router,
    value_propositions_router,
)
from routers.public.media import router as media_router
from routers.public.packages import router as packages_router
from routers.public.site_settings import router as site_settings_router
from routers.public.specializations import router as specializations_router

router = APIRouter()

router.include_router(specializations_router, prefix="/specializations", tags=["Public · Specializations"])
router.include_router(destinations_router, prefix="/destinations", tags=["Public · Destinations"])
router.include_router(packages_router, prefix="/packages", tags=["Public · Packages"])
router.include_router(itineraries_router, prefix="/itineraries", tags=["Public · Itineraries"])
router.include_router(hotels_router, prefix="/hotels", tags=["Public · Hotels"])
router.include_router(experiences_router, prefix="/experiences", tags=["Public · Experiences"])
router.include_router(media_router, prefix="/media", tags=["Public · Media"])
router.include_router(client_stories_router, prefix="/client-stories", tags=["Public · Client Stories"])
router.include_router(
    gallery_categories_router,
    prefix="/gallery-categories",
    tags=["Public · Gallery Categories"],
)
router.include_router(gallery_items_router, prefix="/gallery-items", tags=["Public · Gallery Items"])
router.include_router(faqs_router, prefix="/faqs", tags=["Public · FAQs"])
router.include_router(site_settings_router, prefix="/site-settings", tags=["Public · Site Settings"])
router.include_router(navigation_router, prefix="/navigation-links", tags=["Public · Navigation Links"])
router.include_router(site_ctas_router, prefix="/site-ctas", tags=["Public · Site CTAs"])
router.include_router(company_stats_router, prefix="/company-stats", tags=["Public · Company Stats"])
router.include_router(global_page_cta_router, prefix="/global-page-cta", tags=["Public · Global Page CTA"])
router.include_router(page_metadata_router, prefix="/page-metadata", tags=["Public · Page Metadata"])
router.include_router(page_heroes_router, prefix="/page-heroes", tags=["Public · Page Heroes"])
router.include_router(redirects_router, prefix="/redirects", tags=["Public · Redirects"])
router.include_router(
    journey_process_steps_router,
    prefix="/journey-process-steps",
    tags=["Public · Journey Process Steps"],
)
router.include_router(
    value_propositions_router,
    prefix="/value-propositions",
    tags=["Public · Value Propositions"],
)
router.include_router(
    concierge_services_router,
    prefix="/concierge-services",
    tags=["Public · Concierge Services"],
)
router.include_router(
    homepage_region_panels_router,
    prefix="/homepage-region-panels",
    tags=["Public · Homepage Region Panels"],
)
router.include_router(
    about_story_sections_router,
    prefix="/about-story-sections",
    tags=["Public · About Story Sections"],
)
router.include_router(homepage_promo_router, prefix="/homepage-promo", tags=["Public · Homepage Promo"])
router.include_router(
    travel_expert_settings_router,
    prefix="/travel-expert-settings",
    tags=["Public · Travel Expert Settings"],
)
router.include_router(
    about_page_header_router,
    prefix="/about-page-header",
    tags=["Public · About Page Header"],
)
router.include_router(job_openings_router, prefix="/job-openings", tags=["Public · Job Openings"])
router.include_router(
    careers_page_extras_router,
    prefix="/careers-page-extras",
    tags=["Public · Careers Page Extras"],
)
router.include_router(legal_router, prefix="/legal-pages", tags=["Public · Legal Pages"])
router.include_router(chat_settings_router, prefix="/chat-agent-settings", tags=["Public · Chat Agent Settings"])
router.include_router(
    chat_welcome_messages_router,
    prefix="/chat-agent-welcome-messages",
    tags=["Public · Chat Agent Welcome Messages"],
)
router.include_router(
    chat_quick_replies_router,
    prefix="/chat-agent-quick-replies",
    tags=["Public · Chat Agent Quick Replies"],
)
router.include_router(form_submissions_router, prefix="/form-submissions", tags=["Public · Form Submissions"])
