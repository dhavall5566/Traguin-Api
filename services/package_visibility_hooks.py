"""ORM hooks: linked itineraries and destination stats follow package publish state."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import event, inspect
from sqlalchemy.orm import Session

from models.itineraries import Itinerary
from models.packages import Package
from services.packages import sync_destination_package_stats, sync_linked_itinerary_visibility

_DESTINATION_SYNC_KEY = "_package_visibility_destination_ids"


def enforce_itinerary_publish_state_from_package(db: Session, itinerary: Itinerary) -> None:
    """Published packages must have a published linked itinerary on the public site."""
    if not itinerary.package_id:
        return
    package = db.get(Package, itinerary.package_id)
    if package is None:
        return
    itinerary.is_published = package.is_published


def _track_destination_sync(session: Session, destination_id: UUID) -> None:
    pending: set[UUID] = session.info.setdefault(_DESTINATION_SYNC_KEY, set())
    pending.add(destination_id)


def _field_changed(session: Session, obj, field: str) -> bool:
    if obj in session.new:
        return True
    return inspect(obj).attrs[field].history.has_changes()


@event.listens_for(Session, "before_flush")
def package_visibility_before_flush(session: Session, flush_context, instances) -> None:
    for obj in list(session.new) + list(session.dirty):
        if isinstance(obj, Package):
            if obj in session.new or _field_changed(session, obj, "is_published"):
                sync_linked_itinerary_visibility(session, obj)
                _track_destination_sync(session, obj.destination_id)
        elif isinstance(obj, Itinerary) and obj.package_id:
            if (
                obj in session.new
                or _field_changed(session, obj, "is_published")
                or _field_changed(session, obj, "package_id")
            ):
                enforce_itinerary_publish_state_from_package(session, obj)

    for obj in session.deleted:
        if isinstance(obj, Package):
            _track_destination_sync(session, obj.destination_id)


@event.listens_for(Session, "after_flush")
def package_visibility_after_flush(session: Session, flush_context) -> None:
    destination_ids: set[UUID] = session.info.pop(_DESTINATION_SYNC_KEY, set())
    for destination_id in destination_ids:
        sync_destination_package_stats(session, destination_id)
