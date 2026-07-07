"""Load/save package import JSON files."""

from __future__ import annotations

import json
from pathlib import Path
from uuid import UUID

from schemas.itineraries import ItineraryCreate
from schemas.package_import import PackageImportFile
from schemas.packages import PackageCreate

PLACEHOLDER_DESTINATION_ID = UUID("00000000-0000-0000-0000-000000000001")


def load_package_import_file(path: Path) -> PackageImportFile:
    data = json.loads(path.read_text(encoding="utf-8"))
    return PackageImportFile.model_validate(data)


def package_import_to_models(
    payload: PackageImportFile,
    destination_id: str | UUID,
) -> tuple[PackageCreate, ItineraryCreate]:
    dest_uuid = UUID(str(destination_id))
    package = PackageCreate(
        destination_id=dest_uuid,
        **payload.package.model_dump(),
    )
    itinerary = ItineraryCreate(
        destination_id=dest_uuid,
        **payload.itinerary.model_dump(),
    )
    return package, itinerary


def export_builder_to_dict(
    *,
    destination_slug: str,
    package: PackageCreate,
    itinerary: ItineraryCreate,
) -> dict:
    pkg = package.model_dump(mode="json")
    pkg.pop("destination_id", None)
    pkg.pop("hero_media_id", None)

    itin = itinerary.model_dump(mode="json")
    itin.pop("destination_id", None)
    itin.pop("package_id", None)
    itin.pop("hero_media_id", None)
    itin.pop("gallery_media_ids", None)

    return {
        "destination_slug": destination_slug,
        "package": pkg,
        "itinerary": itin,
    }


def write_package_import_file(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    validated = PackageImportFile.model_validate(payload)
    path.write_text(
        json.dumps(validated.model_dump(mode="json"), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
