from pydantic import BaseModel, Field

from schemas.config import CompanyStatsRead
from schemas.destination import DestinationRead
from schemas.experiences import ExperienceRead
from schemas.gallery import ClientStoryRead
from schemas.itineraries import ItineraryRead
from schemas.marketing import (
    HomepagePromoRead,
    HomepageRegionPanelRead,
    JourneyProcessStepRead,
    ValuePropositionRead,
)
from schemas.media import MediaAssetRead
from schemas.packages import PackageRead
from schemas.specialization import SpecializationRead


class HomepageBundleRead(BaseModel):
    packages: list[PackageRead] = Field(default_factory=list)
    destinations: list[DestinationRead] = Field(default_factory=list)
    itineraries: list[ItineraryRead] = Field(default_factory=list)
    media: list[MediaAssetRead] = Field(default_factory=list)
    company_stats: CompanyStatsRead
    region_panels: list[HomepageRegionPanelRead] = Field(default_factory=list)
    homepage_promo: HomepagePromoRead | None = None
    experiences: list[ExperienceRead] = Field(default_factory=list)
    journey_process_steps: list[JourneyProcessStepRead] = Field(default_factory=list)
    specializations: list[SpecializationRead] = Field(default_factory=list)
    value_propositions: list[ValuePropositionRead] = Field(default_factory=list)
    client_stories: list[ClientStoryRead] = Field(default_factory=list)
