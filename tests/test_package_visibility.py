"""Tests for package ↔ itinerary publish visibility alignment."""

from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import uuid4

from services.packages import sync_linked_itinerary_visibility


def test_sync_linked_itinerary_visibility_publishes_with_package():
    db = MagicMock()
    itinerary = SimpleNamespace(is_published=False)
    db.scalars.return_value.all.return_value = [itinerary]
    package = SimpleNamespace(id=uuid4(), is_published=True)

    sync_linked_itinerary_visibility(db, package)

    assert itinerary.is_published is True


def test_sync_linked_itinerary_visibility_unpublishes_with_package():
    db = MagicMock()
    itinerary = SimpleNamespace(is_published=True)
    db.scalars.return_value.all.return_value = [itinerary]
    package = SimpleNamespace(id=uuid4(), is_published=False)

    sync_linked_itinerary_visibility(db, package)

    assert itinerary.is_published is False


def test_sync_linked_itinerary_visibility_updates_all_linked_itineraries():
    db = MagicMock()
    first = SimpleNamespace(is_published=False)
    second = SimpleNamespace(is_published=False)
    db.scalars.return_value.all.return_value = [first, second]
    package = SimpleNamespace(id=uuid4(), is_published=True)

    sync_linked_itinerary_visibility(db, package)

    assert first.is_published is True
    assert second.is_published is True
