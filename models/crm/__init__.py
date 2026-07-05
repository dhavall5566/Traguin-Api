"""Import all CRM models so SQLAlchemy metadata is fully populated."""

import models.crm.audit  # noqa: F401
import models.crm.bookings  # noqa: F401
import models.crm.customers  # noqa: F401
import models.crm.finance  # noqa: F401
import models.crm.itineraries  # noqa: F401
import models.crm.leads  # noqa: F401
import models.crm.smtp_settings  # noqa: F401
import models.crm.tenancy  # noqa: F401
import models.crm.vendors  # noqa: F401
from models.crm.audit import AuditLog
from models.crm.base import CrmBase, CreatedAtMixin, TimestampMixin, UUIDPrimaryKeyMixin
from models.crm.bookings import Booking
from models.crm.customers import Customer
from models.crm.finance import Expense, Invoice, Payment, Quotation, VendorPayout
from models.crm.itineraries import Itinerary, ItineraryDay, ItineraryItem
from models.crm.leads import Lead, LeadActivity, LeadFollowup, LeadNote
from models.crm.smtp_settings import AgencySmtpSettings
from models.crm.tenancy import Agency, Permission, Role, RolePermission, User, UserRole
from models.crm.vendors import Vendor, VendorPackage, VendorRate, VendorService

__all__ = [
    "CrmBase",
    "CreatedAtMixin",
    "TimestampMixin",
    "UUIDPrimaryKeyMixin",
    "AgencySmtpSettings",
    "Agency",
    "User",
    "Role",
    "Permission",
    "RolePermission",
    "UserRole",
    "Lead",
    "LeadNote",
    "LeadActivity",
    "LeadFollowup",
    "Customer",
    "Itinerary",
    "ItineraryDay",
    "ItineraryItem",
    "Vendor",
    "VendorService",
    "VendorPackage",
    "VendorRate",
    "Booking",
    "Quotation",
    "Invoice",
    "Payment",
    "Expense",
    "VendorPayout",
    "AuditLog",
]
