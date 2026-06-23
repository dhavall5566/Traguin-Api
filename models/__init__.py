"""Import all models so SQLAlchemy metadata is fully populated."""

from models.admin_users import AdminUser
from models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin
from models.chat import ChatAgentQuickReply, ChatAgentSettings, ChatAgentWelcomeMessage
from models.config import (
    CompanyStats,
    GlobalPageCta,
    NavigationLink,
    PageHero,
    PageMetadata,
    Redirect,
    SiteCta,
    SiteSettings,
)
from models.content import (
    AboutPageHeader,
    AboutStorySection,
    CareersPageExtras,
    ConciergeService,
    Faq,
    HomepagePromo,
    HomepageRegionPanel,
    JobOpening,
    JourneyProcessStep,
    Specialization,
    TravelExpertSettings,
    ValueProposition,
)
from models.destinations import (
    Destination,
    DestinationCategory,
    DestinationCategoryAssignment,
    DestinationMedia,
)
from models.experiences import (
    Experience,
    ExperienceOffer,
    ExperienceProcessStep,
    ExperienceStat,
)
from models.gallery import ClientStory, GalleryCategory, GalleryItem, GalleryItemCategory
from models.hotels import Hotel, HotelMedia, HotelNearbyAttraction
from models.itineraries import (
    Itinerary,
    ItineraryDay,
    ItineraryHighlight,
    ItineraryHotel,
    ItineraryInclusion,
    ItineraryMedia,
)
from models.legal import LegalPage
from models.media import MediaAsset
from models.packages import Package, PackageHighlight, PackageMood
from models.submissions import FormSubmission

__all__ = [
    "Base",
    "TimestampMixin",
    "UUIDPrimaryKeyMixin",
    "MediaAsset",
    "SiteSettings",
    "NavigationLink",
    "SiteCta",
    "CompanyStats",
    "GlobalPageCta",
    "PageMetadata",
    "PageHero",
    "Redirect",
    "DestinationCategory",
    "Destination",
    "DestinationCategoryAssignment",
    "DestinationMedia",
    "Package",
    "PackageHighlight",
    "PackageMood",
    "Itinerary",
    "ItineraryHighlight",
    "ItineraryDay",
    "ItineraryHotel",
    "ItineraryInclusion",
    "ItineraryMedia",
    "Hotel",
    "HotelNearbyAttraction",
    "HotelMedia",
    "Experience",
    "ExperienceOffer",
    "ExperienceStat",
    "ExperienceProcessStep",
    "ClientStory",
    "GalleryCategory",
    "GalleryItem",
    "GalleryItemCategory",
    "Faq",
    "HomepagePromo",
    "HomepageRegionPanel",
    "JourneyProcessStep",
    "ValueProposition",
    "Specialization",
    "ConciergeService",
    "TravelExpertSettings",
    "AboutStorySection",
    "AboutPageHeader",
    "JobOpening",
    "CareersPageExtras",
    "LegalPage",
    "ChatAgentSettings",
    "ChatAgentWelcomeMessage",
    "ChatAgentQuickReply",
    "FormSubmission",
    "AdminUser",
]
