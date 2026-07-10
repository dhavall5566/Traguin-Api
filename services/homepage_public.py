"""Assemble scoped CMS data for the public homepage in one request."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from models.config import CompanyStats
from models.content import (
    HomepagePromo,
    HomepageRegionPanel,
    JourneyProcessStep,
    Specialization,
    ValueProposition,
)
from models.destinations import Destination
from models.experiences import Experience
from models.gallery import ClientStory
from models.itineraries import Itinerary
from models.media import MediaAsset
from models.packages import Package
from schemas.config import CompanyStatsRead
from schemas.destination import DestinationRead
from schemas.experiences import ExperienceRead
from schemas.gallery import ClientStoryRead
from schemas.homepage import HomepageBundleRead
from schemas.itineraries import ItineraryRead
from schemas.marketing import (
    HomepagePromoRead,
    HomepageRegionPanelRead,
    JourneyProcessStepRead,
    ValuePropositionRead,
)
from schemas.specialization import SpecializationRead
from schemas.media import MediaSummary
from schemas.packages import PackageRead
from services.destinations import destination_query_with_categories, destination_to_read
from services.experiences import experience_query_with_nested, experience_to_read
from services.gallery import client_story_query, client_story_to_read
from services.homepage_hero_settings import (
    has_homepage_hero_visibility_configured,
    read_homepage_hero_settings,
    select_homepage_hero_packages,
)
from services.itineraries import (
    itinerary_query_with_nested,
    itinerary_to_read,
    public_itinerary_visibility_filters,
)
from services.packages import package_query_with_nested, package_to_read
from utils.singleton import get_singleton_or_404

HOME_CLIENT_STORIES_LIMIT = 6


def _add_media_id(ids: set[UUID], value: UUID | None) -> None:
    if value is not None:
        ids.add(value)


def _collect_media_ids(
    *,
    packages: list[Package],
    destinations: list[Destination],
    itineraries: list[Itinerary],
    region_panels: list[HomepageRegionPanel],
    experiences: list[Experience],
    client_stories: list[ClientStory],
    destination_ids: set[UUID] | None = None,
) -> set[UUID]:
    ids: set[UUID] = set()
    scoped_destinations = (
        [dest for dest in destinations if dest.id in destination_ids]
        if destination_ids
        else destinations
    )

    for pkg in packages:
        _add_media_id(ids, pkg.hero_media_id)

    for dest in scoped_destinations:
        _add_media_id(ids, dest.hero_media_id)
        for link in dest.gallery_media:
            if link.media_id is not None:
                ids.add(link.media_id)

    for itinerary in itineraries:
        _add_media_id(ids, itinerary.hero_media_id)
        for link in itinerary.gallery_media:
            if link.media_id is not None:
                ids.add(link.media_id)

    for panel in region_panels:
        _add_media_id(ids, panel.hero_media_id)

    for exp in experiences:
        _add_media_id(ids, exp.hero_media_id)

    for story in client_stories:
        _add_media_id(ids, story.portrait_media_id)

    return ids


def build_homepage_bundle(db: Session) -> HomepageBundleRead:
    company_stats = get_singleton_or_404(db, CompanyStats)
    hero_settings = read_homepage_hero_settings(company_stats)

    packages = (
        package_query_with_nested(db)
        .filter(Package.is_published.is_(True))
        .order_by(Package.featured_sort_order.nulls_last(), Package.title)
        .all()
    )

    destinations = (
        destination_query_with_categories(db)
        .filter(Destination.is_published.is_(True))
        .order_by(Destination.featured_sort_order.nulls_last(), Destination.name)
        .all()
    )

    featured_packages = select_homepage_hero_packages(packages, company_stats)
    if featured_packages:
        hero_package_ids = {p.id for p in featured_packages}
    elif has_homepage_hero_visibility_configured(company_stats):
        hero_package_ids = set()
    else:
        hero_package_ids = {p.id for p in packages[: hero_settings["hero_slider_max_items"]]}
    featured_dest_ids = {d.id for d in destinations if d.is_featured}
    hero_dest_ids = {p.destination_id for p in packages if p.id in hero_package_ids and p.destination_id}
    itinerary_dest_ids = featured_dest_ids | hero_dest_ids
    media_package_ids = hero_package_ids
    media_packages = [p for p in packages if p.id in media_package_ids]

    itinerary_filters = [*public_itinerary_visibility_filters()]
    scope_filters = []
    if hero_package_ids:
        scope_filters.append(Itinerary.package_id.in_(hero_package_ids))
    if itinerary_dest_ids:
        scope_filters.append(Itinerary.destination_id.in_(itinerary_dest_ids))
    if scope_filters:
        itinerary_filters.append(or_(*scope_filters))

    itineraries = (
        itinerary_query_with_nested(db)
        .filter(*itinerary_filters)
        .order_by(Itinerary.title)
        .limit(40)
        .all()
    )

    region_panels = (
        db.query(HomepageRegionPanel)
        .filter(HomepageRegionPanel.is_active.is_(True))
        .order_by(HomepageRegionPanel.sort_order)
        .limit(20)
        .all()
    )

    homepage_promo = db.query(HomepagePromo).one_or_none()

    experiences = (
        experience_query_with_nested(db)
        .filter(
            Experience.is_published.is_(True),
            Experience.show_on_homepage.is_(True),
        )
        .order_by(Experience.homepage_sort_order.nulls_last(), Experience.headline)
        .limit(20)
        .all()
    )

    journey_steps = (
        db.query(JourneyProcessStep)
        .order_by(JourneyProcessStep.sort_order)
        .limit(20)
        .all()
    )

    specializations = (
        db.query(Specialization).order_by(Specialization.sort_order).limit(20).all()
    )

    value_propositions = (
        db.query(ValueProposition)
        .order_by(ValueProposition.sort_order)
        .limit(20)
        .all()
    )

    client_stories = (
        client_story_query(db)
        .filter(
            ClientStory.is_published.is_(True),
            ClientStory.quote.isnot(None),
            ClientStory.quote != "",
        )
        .order_by(
            func.coalesce(ClientStory.gallery_sort_order, ClientStory.home_sort_order, 999),
            ClientStory.client_name,
        )
        .limit(HOME_CLIENT_STORIES_LIMIT)
        .all()
    )

    media_ids = _collect_media_ids(
        packages=media_packages,
        destinations=destinations,
        itineraries=itineraries,
        region_panels=region_panels,
        experiences=experiences,
        client_stories=client_stories,
        destination_ids=itinerary_dest_ids,
    )

    media_assets: list[MediaAsset] = []
    if media_ids:
        media_assets = db.query(MediaAsset).filter(MediaAsset.id.in_(media_ids)).all()

    return HomepageBundleRead(
        packages=[package_to_read(p) for p in packages],
        destinations=[destination_to_read(d) for d in destinations],
        itineraries=[itinerary_to_read(i) for i in itineraries],
        media=[
            MediaSummary(
                id=asset.id,
                url=asset.url,
                alt_text=asset.alt_text,
            )
            for asset in media_assets
        ],
        company_stats=CompanyStatsRead.model_validate(company_stats),
        region_panels=[HomepageRegionPanelRead.model_validate(p) for p in region_panels],
        homepage_promo=(
            HomepagePromoRead.model_validate(homepage_promo) if homepage_promo else None
        ),
        experiences=[experience_to_read(e) for e in experiences],
        journey_process_steps=[JourneyProcessStepRead.model_validate(s) for s in journey_steps],
        specializations=[SpecializationRead.model_validate(s) for s in specializations],
        value_propositions=[ValuePropositionRead.model_validate(v) for v in value_propositions],
        client_stories=[client_story_to_read(s) for s in client_stories],
    )
