from uuid import UUID

from sqlalchemy.orm import Session, selectinload

from models.destinations import Destination
from models.packages import Package, PackageHighlight, PackageMood
from schemas.packages import PackageHighlightRead, PackageListRead, PackageRead
from utils.orm_read import orm_read_with_nested


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
        destination_id=package.destination_id,
        destination_name=destination_name,
        title=package.title,
        duration_label=package.duration_label,
        price=package.price,
        hero_media_id=package.hero_media_id,
        rating=package.rating,
        is_featured=package.is_featured,
        featured_sort_order=package.featured_sort_order,
        is_published=package.is_published,
    )


def sync_package_highlights(db: Session, package: Package, highlights: list) -> None:
    package.highlights.clear()
    for item in highlights:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        package.highlights.append(PackageHighlight(**data))


def sync_package_moods(db: Session, package: Package, moods: list[str]) -> None:
    package.moods.clear()
    for mood in moods:
        package.moods.append(PackageMood(mood=mood))


def package_to_read(package: Package) -> PackageRead:
    highlights = [
        PackageHighlightRead.model_validate(h)
        for h in sorted(package.highlights, key=lambda x: x.sort_order)
    ]
    moods = [m.mood for m in package.moods]
    return orm_read_with_nested(
        PackageRead,
        package,
        nested={"highlights": highlights, "moods": moods},
    )
