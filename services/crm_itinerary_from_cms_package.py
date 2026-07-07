"""Create a CRM trip planner itinerary from a CMS pre-built package."""

from __future__ import annotations

from decimal import Decimal
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session, selectinload

from models.itineraries import Itinerary as CmsItinerary
from models.packages import Package
from models.crm.itineraries import Itinerary as CrmItinerary
from schemas.crm.itinerary import ItineraryDayNested, ItineraryItemNested
from services.crm_itineraries import sync_itinerary_days
from utils.package_title import clean_package_title


def _cms_days_to_crm_nested(cms_itinerary: CmsItinerary) -> list[ItineraryDayNested]:
    days: list[ItineraryDayNested] = []
    for cms_day in sorted(cms_itinerary.days, key=lambda row: (row.sort_order, row.day_number)):
        items: list[ItineraryItemNested] = []
        for idx, activity in enumerate(cms_day.activities or []):
            label = (activity or "").strip()
            if not label:
                continue
            items.append(
                ItineraryItemNested(
                    type="ACTIVITY",
                    title=label[:255],
                    details=None,
                    cost_price=Decimal("0.00"),
                    selling_price=Decimal("0.00"),
                    order=idx,
                )
            )
        if not items:
            summary = (cms_day.description or "").strip()
            if summary:
                items.append(
                    ItineraryItemNested(
                        type="NOTE",
                        title=cms_day.title[:255],
                        details=summary,
                        cost_price=Decimal("0.00"),
                        selling_price=Decimal("0.00"),
                        order=0,
                    )
                )
        days.append(
            ItineraryDayNested(
                day_number=cms_day.day_number,
                title=cms_day.title,
                description=(cms_day.description or None),
                items=items,
            )
        )
    return days


def create_crm_itinerary_from_cms_package(
    db: Session,
    *,
    agency_id: UUID,
    cms_package_id: UUID,
    customer_id: UUID | None = None,
) -> CrmItinerary:
    package = db.get(Package, cms_package_id)
    if package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found.")

    cms_itinerary = (
        db.query(CmsItinerary)
        .options(selectinload(CmsItinerary.days))
        .filter(CmsItinerary.package_id == cms_package_id)
        .order_by(CmsItinerary.created_at.asc())
        .first()
    )

    title = clean_package_title(package.title) or package.title
    description = None
    days: list[ItineraryDayNested] = []
    if cms_itinerary is not None:
        title = clean_package_title(cms_itinerary.title) or title
        overview = (cms_itinerary.overview or "").strip()
        description = overview or None
        days = _cms_days_to_crm_nested(cms_itinerary)

    itinerary = CrmItinerary(
        agency_id=agency_id,
        title=title,
        description=description,
        customer_id=customer_id,
        status="DRAFT",
        total_price=Decimal(str(package.price)),
        markup_margin=Decimal("0.00"),
        tax_rate=Decimal("0.00"),
        is_template=False,
    )
    db.add(itinerary)
    db.flush()
    if days:
        sync_itinerary_days(db, itinerary, days)
    return itinerary
