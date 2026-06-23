import re


def slugify(value: str, *, max_length: int = 128) -> str:
    text = value.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    if not text:
        return "item"
    return text[:max_length]
