from fastapi import APIRouter, Depends

from dependencies.crm_auth import require_crm_user
from routers.crm.agencies import router as agencies_router
from routers.crm.audit_logs import router as audit_logs_router
from routers.crm.auth import router as auth_router
from routers.crm.bookings import router as bookings_router
from routers.crm.customers import router as customers_router
from routers.crm.finance import router as finance_router
from routers.crm.itineraries import router as itineraries_router
from routers.crm.leads import router as leads_router
from routers.crm.packages import router as packages_router
from routers.crm.rbac import router as rbac_router
from routers.crm.users import router as users_router
from routers.crm.vendors import router as vendors_router
from routers.crm.settings import router as settings_router

router = APIRouter()

protected = [Depends(require_crm_user)]

router.include_router(auth_router, prefix="/auth", tags=["CRM · Auth"])
router.include_router(agencies_router, prefix="/agencies", tags=["CRM · Agencies"], dependencies=protected)
router.include_router(leads_router, prefix="/leads", tags=["CRM · Leads"], dependencies=protected)
router.include_router(users_router, prefix="/users", tags=["CRM · Users"], dependencies=protected)
router.include_router(customers_router, prefix="/customers", tags=["CRM · Customers"], dependencies=protected)
router.include_router(itineraries_router, prefix="/itineraries", tags=["CRM · Itineraries"], dependencies=protected)
router.include_router(packages_router, prefix="/packages", tags=["CRM · Packages"], dependencies=protected)
router.include_router(vendors_router, prefix="/vendors", tags=["CRM · Vendors"], dependencies=protected)
router.include_router(bookings_router, prefix="/bookings", tags=["CRM · Bookings"], dependencies=protected)
router.include_router(finance_router, prefix="/finance", tags=["CRM · Finance"], dependencies=protected)
router.include_router(rbac_router, prefix="/rbac", tags=["CRM · RBAC"], dependencies=protected)
router.include_router(audit_logs_router, prefix="/audit-logs", tags=["CRM · Audit Logs"], dependencies=protected)
router.include_router(settings_router, prefix="/settings", tags=["CRM · Settings"], dependencies=protected)
