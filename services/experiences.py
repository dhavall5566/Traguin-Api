from sqlalchemy.orm import Session, selectinload

from models.experiences import Experience, ExperienceOffer, ExperienceProcessStep, ExperienceStat
from schemas.experiences import (
    ExperienceOfferRead,
    ExperienceProcessStepRead,
    ExperienceRead,
    ExperienceStatRead,
)
from utils.orm_read import orm_read_with_nested


def experience_query_with_nested(db: Session):
    return db.query(Experience).options(
        selectinload(Experience.offers),
        selectinload(Experience.stats),
        selectinload(Experience.process_steps),
    )


def sync_experience_offers(db: Session, experience: Experience, offers: list) -> None:
    experience.offers.clear()
    for item in offers:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        experience.offers.append(ExperienceOffer(**data))


def sync_experience_stats(db: Session, experience: Experience, stats: list) -> None:
    experience.stats.clear()
    for item in stats:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        experience.stats.append(ExperienceStat(**data))


def sync_experience_process_steps(db: Session, experience: Experience, steps: list) -> None:
    experience.process_steps.clear()
    for item in steps:
        data = item.model_dump() if hasattr(item, "model_dump") else item
        experience.process_steps.append(ExperienceProcessStep(**data))


def experience_to_read(experience: Experience) -> ExperienceRead:
    offers = [
        ExperienceOfferRead.model_validate(o)
        for o in sorted(experience.offers, key=lambda x: x.sort_order)
    ]
    stats = [
        ExperienceStatRead.model_validate(s)
        for s in sorted(experience.stats, key=lambda x: x.sort_order)
    ]
    process_steps = [
        ExperienceProcessStepRead.model_validate(p)
        for p in sorted(experience.process_steps, key=lambda x: x.sort_order)
    ]
    return orm_read_with_nested(
        ExperienceRead,
        experience,
        nested={"offers": offers, "stats": stats, "process_steps": process_steps},
    )
