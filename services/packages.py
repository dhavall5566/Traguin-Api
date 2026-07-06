from uuid import UUID

from sqlalchemy.orm import Session, selectinload

from models.destinations import Destination
from models.packages import Package, PackageHighlight, PackageMood
from schemas.packages import PackageHighlightRead, PackageListRead, PackageRead
from services.travel_moods import normalize_travel_moods
from utils.orm_read import orm_read_with_nested
from utils.package_codes import resolve_package_codes
from utils.package_title import clean_package_title


def package_query_with_nested(db: Session):
    return db.query(Package).options(
        selectinload(Package.highlights),
        selectinload(Package.moods),
    )


def package_list_query(db: Session):
    return (
        db.query(Package, Destination.name.label("destination_name"))
        .join(Destination, Package.destination_id == Destination.id)
    )


def package_to_list_read(row: tuple[Package, str]) -> PackageListRead:
    package, destination_name = row
    return PackageListRead(
        id=package.id,
        created_at=package.created_at,
        updated_at=package.updated_at,
        slug=package.slug,
        serial_code=package.serial_code,
        traguin_tour_code=package.traguin_tour_code,
        destination_id=package.destination_id,
        destination_name=destination_name,
        title=clean_package_title(package.title) or package.title,
        duration_label=package.duration_label,
        price=package.price,
        sold_last_month=package.sold_last_month,
        hero_media_id=package.hero_media_id,
        rating=package.rating,
        is_featured=package.is_featured,
        featured_sort_order=package.featured_sort_order,
        is_published=package.is_published,
    )


def apply_package_codes(package: Package, *, highlight_texts: list[str] | None = None) -> None:
    if package.serial_code and package.traguin_tour_code:
        return
    texts = highlight_texts
    if texts is None:
        texts = [h.text for h in package.highlights]
    serial, tour = resolve_package_codes(package.slug, texts)
    if not package.serial_code:
        package.serial_code = serial
    if not package.traguin_tour_code:
        package.traguin_tour_code = tour


def sync_package_highlights(db: Session, package: Package, highlights: list) -> None:
    package.highlights.clear()
    for item in highlights:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        package.highlights.append(PackageHighlight(**data))


def sync_package_moods(db: Session, package: Package, moods: list[str]) -> None:
    package.moods.clear()
    for mood in moods:
        package.moods.append(PackageMood(mood=mood))


def merge_package_moods(db: Session, package: Package, new_moods: list[str]) -> None:
    existing = [m.mood for m in package.moods]
    merged = normalize_travel_moods(existing + new_moods)
    sync_package_moods(db, package, merged)


def package_to_read(package: Package) -> PackageRead:
    highlights = [
        PackageHighlightRead.model_validate(h)
        for h in sorted(package.highlights, key=lambda x: x.sort_order)
    ]
    moods = [m.mood for m in package.moods]
    read = orm_read_with_nested(
        PackageRead,
        package,
        nested={"highlights": highlights, "moods": moods},
    )
    if read.title:
        read.title = clean_package_title(read.title) or read.title
    return read
