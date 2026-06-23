from fastapi import APIRouter

from routers.admin.auth import router as admin_auth_router
from routers.admin.chat import (
    quick_replies_router as chat_quick_replies_router,
    settings_router as chat_settings_router,
    welcome_messages_router as chat_welcome_messages_router,
)
from routers.admin.config import (
    company_stats_router,
    global_page_cta_router,
    navigation_router,
    page_heroes_router,
    page_metadata_router,
    redirects_router,
    site_ctas_router,
)
from routers.admin.destination_categories import router as destination_categories_router
from routers.admin.destinations import router as destinations_router
from routers.admin.experiences import router as experiences_router
from routers.admin.faqs import router as faqs_router
from routers.admin.form_submissions import router as form_submissions_router
from routers.admin.gallery import (
    client_stories_router,
    gallery_categories_router,
    gallery_items_router,
)
from routers.admin.hotels import router as hotels_router
from routers.admin.itineraries import router as itineraries_router
from routers.admin.legal import router as legal_router
from routers.admin.marketing import (
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
from routers.admin.media import router as media_router
from routers.admin.packages import router as packages_router
from routers.admin.package_import import router as package_import_router
from routers.admin.site_settings import router as site_settings_router
from routers.admin.specializations import router as specializations_router

router = APIRouter()

router.include_router(admin_auth_router, prefix="/auth", tags=["Admin · Auth"])
router.include_router(specializations_router, prefix="/specializations", tags=["Admin · Specializations"])
router.include_router(
    destination_categories_router,
    prefix="/destination-categories",
    tags=["Admin · Destination Categories"],
)
router.include_router(destinations_router, prefix="/destinations", tags=["Admin · Destinations"])
router.include_router(packages_router, prefix="/packages", tags=["Admin · Packages"])
router.include_router(package_import_router, prefix="/package-import", tags=["Admin · Package Import"])
router.include_router(itineraries_router, prefix="/itineraries", tags=["Admin · Itineraries"])
router.include_router(hotels_router, prefix="/hotels", tags=["Admin · Hotels"])
router.include_router(experiences_router, prefix="/experiences", tags=["Admin · Experiences"])
router.include_router(media_router, prefix="/media", tags=["Admin · Media"])
router.include_router(client_stories_router, prefix="/client-stories", tags=["Admin · Client Stories"])
router.include_router(
    gallery_categories_router,
    prefix="/gallery-categories",
    tags=["Admin · Gallery Categories"],
)
router.include_router(gallery_items_router, prefix="/gallery-items", tags=["Admin · Gallery Items"])
router.include_router(faqs_router, prefix="/faqs", tags=["Admin · FAQs"])
router.include_router(site_settings_router, prefix="/site-settings", tags=["Admin · Site Settings"])
router.include_router(navigation_router, prefix="/navigation-links", tags=["Admin · Navigation Links"])
router.include_router(site_ctas_router, prefix="/site-ctas", tags=["Admin · Site CTAs"])
router.include_router(company_stats_router, prefix="/company-stats", tags=["Admin · Company Stats"])
router.include_router(global_page_cta_router, prefix="/global-page-cta", tags=["Admin · Global Page CTA"])
router.include_router(page_metadata_router, prefix="/page-metadata", tags=["Admin · Page Metadata"])
router.include_router(page_heroes_router, prefix="/page-heroes", tags=["Admin · Page Heroes"])
router.include_router(redirects_router, prefix="/redirects", tags=["Admin · Redirects"])
router.include_router(
    journey_process_steps_router,
    prefix="/journey-process-steps",
    tags=["Admin · Journey Process Steps"],
)
router.include_router(
    value_propositions_router,
    prefix="/value-propositions",
    tags=["Admin · Value Propositions"],
)
router.include_router(
    concierge_services_router,
    prefix="/concierge-services",
    tags=["Admin · Concierge Services"],
)
router.include_router(
    homepage_region_panels_router,
    prefix="/homepage-region-panels",
    tags=["Admin · Homepage Region Panels"],
)
router.include_router(
    about_story_sections_router,
    prefix="/about-story-sections",
    tags=["Admin · About Story Sections"],
)
router.include_router(homepage_promo_router, prefix="/homepage-promo", tags=["Admin · Homepage Promo"])
router.include_router(
    travel_expert_settings_router,
    prefix="/travel-expert-settings",
    tags=["Admin · Travel Expert Settings"],
)
router.include_router(
    about_page_header_router,
    prefix="/about-page-header",
    tags=["Admin · About Page Header"],
)
router.include_router(job_openings_router, prefix="/job-openings", tags=["Admin · Job Openings"])
router.include_router(
    careers_page_extras_router,
    prefix="/careers-page-extras",
    tags=["Admin · Careers Page Extras"],
)
router.include_router(legal_router, prefix="/legal-pages", tags=["Admin · Legal Pages"])
router.include_router(chat_settings_router, prefix="/chat-agent-settings", tags=["Admin · Chat Agent Settings"])
router.include_router(
    chat_welcome_messages_router,
    prefix="/chat-agent-welcome-messages",
    tags=["Admin · Chat Agent Welcome Messages"],
)
router.include_router(
    chat_quick_replies_router,
    prefix="/chat-agent-quick-replies",
    tags=["Admin · Chat Agent Quick Replies"],
)
router.include_router(form_submissions_router, prefix="/form-submissions", tags=["Admin · Form Submissions"])
