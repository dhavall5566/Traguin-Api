from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session, selectinload

from models.destinations import Destination
from models.hotels import Hotel, HotelMedia, HotelNearbyAttraction
from models.media import MediaAsset
from schemas.hotels import HotelListRead, HotelNearbyAttractionRead, HotelRead
from schemas.media import MediaSummary
from utils.orm_read import orm_read_with_nested


def hotel_query_with_nested(db: Session):
    return db.query(Hotel).options(
        selectinload(Hotel.nearby_attractions),
        selectinload(Hotel.gallery_media).selectinload(HotelMedia.media),
    )


def hotel_list_query(db: Session):
    return (
        db.query(Hotel, Destination.name.label("destination_name"))
        .join(Destination, Hotel.destination_id == Destination.id)
    )


def hotel_to_list_read(row: tuple[Hotel, str]) -> HotelListRead:
    hotel, destination_name = row
    return HotelListRead(
        id=hotel.id,
        created_at=hotel.created_at,
        updated_at=hotel.updated_at,
        slug=hotel.slug,
        destination_id=hotel.destination_id,
        destination_name=destination_name,
        name=hotel.name,
        stars=hotel.stars,
        price=hotel.price,
        rating=hotel.rating,
        is_published=hotel.is_published,
    )


def sync_hotel_nearby_attractions(db: Session, hotel: Hotel, attractions: list) -> None:
    hotel.nearby_attractions.clear()
    for item in attractions:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        hotel.nearby_attractions.append(HotelNearbyAttraction(**data))


def sync_hotel_gallery(
    db: Session,
    hotel: Hotel,
    media_ids: list[UUID],
) -> None:
    if not media_ids:
        hotel.gallery_media.clear()
        return

    assets = db.query(MediaAsset).filter(MediaAsset.id.in_(media_ids)).all()
    found_ids = {asset.id for asset in assets}
    missing = [str(media_id) for media_id in media_ids if media_id not in found_ids]
    if missing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown gallery_media_ids: {', '.join(missing)}",
        )

    order_by_id = {media_id: index for index, media_id in enumerate(media_ids)}
    hotel.gallery_media.clear()
    for asset in assets:
        hotel.gallery_media.append(
            HotelMedia(media_id=asset.id, sort_order=order_by_id[asset.id])
        )


def hotel_to_read(hotel: Hotel) -> HotelRead:
    nearby_attractions = [
        HotelNearbyAttractionRead.model_validate(a)
        for a in sorted(hotel.nearby_attractions, key=lambda x: x.sort_order)
    ]
    gallery_media = [
        MediaSummary(
            id=link.media.id,
            url=link.media.url,
            alt_text=link.media.alt_text,
            sort_order=link.sort_order,
        )
        for link in sorted(hotel.gallery_media, key=lambda x: x.sort_order)
        if link.media is not None
    ]
    return orm_read_with_nested(
        HotelRead,
        hotel,
        nested={"nearby_attractions": nearby_attractions, "gallery_media": gallery_media},
    )
