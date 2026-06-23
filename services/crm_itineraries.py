from uuid import UUID

from sqlalchemy.orm import Session, selectinload

from models.crm.itineraries import Itinerary, ItineraryDay, ItineraryItem
from schemas.crm.itinerary import ItineraryListRead, ItineraryRead


def itinerary_query_with_nested(db: Session):
    return db.query(Itinerary).options(
        selectinload(Itinerary.days).selectinload(ItineraryDay.items),
    )


def get_itinerary_with_nested(db: Session, itinerary_id: UUID, agency_id: UUID) -> Itinerary | None:
    return (
        itinerary_query_with_nested(db)
        .filter(Itinerary.id == itinerary_id, Itinerary.agency_id == agency_id)
        .one_or_none()
    )


def sync_itinerary_days(db: Session, itinerary: Itinerary, days: list) -> None:
    itinerary.days.clear()
    db.flush()
    for day_data in days:
        items = day_data.items if hasattr(day_data, "items") else day_data.get("items", [])
        day_fields = (
            day_data.model_dump(exclude={"items"})
            if hasattr(day_data, "model_dump")
            else {k: v for k, v in day_data.items() if k != "items"}
        )
        day = ItineraryDay(itinerary_id=itinerary.id, **day_fields)
        db.add(day)
        db.flush()
        for item_data in items:
            item_fields = item_data.model_dump() if hasattr(item_data, "model_dump") else item_data
            db.add(ItineraryItem(itinerary_day_id=day.id, **item_fields))


def itinerary_to_read(itinerary: Itinerary) -> ItineraryRead:
    return ItineraryRead.model_validate(itinerary)


def itinerary_to_list_read(itinerary: Itinerary) -> ItineraryListRead:
    return ItineraryListRead.model_validate(itinerary)
