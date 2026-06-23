from __future__ import annotations

from uuid import UUID

from schemas.destination import DestinationCreate
from schemas.itineraries import (
    ItineraryCreate,
    ItineraryDayNested,
    ItineraryHighlightNested,
    ItineraryHotelNested,
    ItineraryInclusionNested,
)
from schemas.package_import import (
    ExtractedDestinationDraft,
    ExtractedItineraryDraft,
    ExtractedPackageDraft,
    PackageImportReviewCommit,
)
from schemas.packages import PackageCreate, PackageHighlightNested
from utils.slugify import slugify


def _price(value: int | None, *, on_request: bool = False) -> int:
    if on_request or value is None or value <= 0:
        return 0
    return value


def review_to_creates(
    review: PackageImportReviewCommit,
) -> tuple[DestinationCreate, PackageCreate, ItineraryCreate]:
    dest = review.destination
    pkg = review.package
    itin = review.itinerary

    dest_slug = dest.slug or slugify(dest.name)
    pkg_slug = pkg.slug or slugify(pkg.title)
    itin_slug = itin.slug or slugify(itin.title)

    destination = DestinationCreate(
        slug=dest_slug,
        name=dest.name,
        country=dest.country,
        region=dest.region,
        india_region=dest.india_region,
        description=dest.description,
        starting_price=_price(dest.starting_price),
        hero_media_id=review.hero_media_id,
        moods=dest.moods,
        is_published=True,
        category_ids=review.category_ids,
        gallery_media_ids=review.gallery_media_ids,
    )

    package = PackageCreate(
        slug=pkg_slug,
        destination_id=UUID("00000000-0000-0000-0000-000000000001"),
        title=pkg.title,
        duration_label=pkg.duration_label,
        price=_price(pkg.starting_price, on_request=pkg.price_on_request),
        hero_media_id=review.package_hero_media_id or review.hero_media_id,
        is_published=True,
        highlights=[
            PackageHighlightNested(text=text, sort_order=index)
            for index, text in enumerate(pkg.highlights)
            if text.strip()
        ],
        moods=pkg.moods,
    )

    itinerary = ItineraryCreate(
        slug=itin_slug,
        package_id=None,
        destination_id=UUID("00000000-0000-0000-0000-000000000001"),
        title=itin.title,
        duration_label=itin.duration_label,
        duration_days=itin.duration_days,
        starting_price=_price(itin.starting_price, on_request=itin.price_on_request),
        price_note=itin.price_note or None,
        hero_media_id=review.itinerary_hero_media_id or review.hero_media_id,
        tagline=itin.tagline,
        overview=itin.overview,
        is_published=True,
        highlights=[
            ItineraryHighlightNested(text=item.text, sort_order=item.sort_order)
            for item in itin.highlights
        ],
        days=[
            ItineraryDayNested(
                day_number=day.day_number,
                title=day.title,
                description=day.description,
                activities=day.activities,
                sort_order=day.sort_order,
            )
            for day in itin.days
        ],
        hotels=[
            ItineraryHotelNested(
                name=hotel.name,
                location=hotel.location,
                nights_label=hotel.nights_label,
                description=hotel.description,
                category_label=hotel.category_label,
                sort_order=hotel.sort_order,
            )
            for hotel in itin.hotels
        ],
        inclusions=[
            ItineraryInclusionNested(kind=inc.kind, text=inc.text, sort_order=inc.sort_order)
            for inc in itin.inclusions
        ],
        gallery_media_ids=review.gallery_media_ids,
    )

    return destination, package, itinerary
