from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def orm_read_with_nested(
    model_cls: type[T],
    orm_obj: object,
    *,
    nested: dict,
) -> T:
    """Build a read schema from an ORM object, replacing nested relationship fields."""
    excluded = set(nested)
    data = {
        name: getattr(orm_obj, name)
        for name in model_cls.model_fields
        if name not in excluded and hasattr(orm_obj, name)
    }
    return model_cls(**data, **nested)
