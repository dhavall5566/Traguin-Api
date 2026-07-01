"""Fuzzy name matching between client stories and gallery item labels."""

from __future__ import annotations

import re
from difflib import SequenceMatcher
from typing import Protocol, TypeVar

T = TypeVar("T")


class Named(Protocol):
    @property
    def place(self) -> str: ...


def match_key(name: str) -> str:
    normalized = re.sub(r"[,\.]", "", name.strip().lower())
    return re.sub(r"\s+", " ", normalized)


def core_key(name: str) -> str:
    normalized = match_key(name)
    normalized = re.sub(r"^(mr|mrs|ms|dr)\s+", "", normalized)
    normalized = re.sub(r"\bsir\b", "", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def name_tokens(name: str) -> list[str]:
    return [token for token in core_key(name).split() if token]


def token_similarity(left: str, right: str) -> float:
    if left == right:
        return 1.0
    return SequenceMatcher(None, left, right).ratio()


def match_score(left_name: str, right_name: str) -> float:
    left_full = match_key(left_name)
    right_full = match_key(right_name)
    if left_full == right_full:
        return 1.0

    left_core = core_key(left_name)
    right_core = core_key(right_name)
    if left_core == right_core:
        return 0.98

    left_tokens = name_tokens(left_name)
    right_tokens = name_tokens(right_name)
    if not left_tokens or not right_tokens:
        return 0.0

    if left_tokens[0] == right_tokens[0] and left_tokens[-1] == right_tokens[-1]:
        return 0.95

    if len(left_tokens) >= 2 and len(right_tokens) >= 2 and left_tokens[:2] == right_tokens[:2]:
        return 0.9

    if left_tokens[0] == right_tokens[0] and token_similarity(left_tokens[-1], right_tokens[-1]) >= 0.8:
        return 0.88

    if len(left_tokens) == 1 and len(right_tokens) == 1:
        if token_similarity(left_tokens[0], right_tokens[0]) >= 0.85:
            return 0.86

    left_set = set(left_tokens)
    right_set = set(right_tokens)
    if left_set.issubset(right_set) or right_set.issubset(left_set):
        return 0.82

    if left_tokens[0] == right_tokens[0] and len(left_tokens) == 1:
        return 0.75

    return 0.0


def find_best_name_match(source_name: str, candidates: list[T], *, get_name) -> T | None:
    scored = [(match_score(source_name, get_name(item)), item) for item in candidates]
    scored = [(score, item) for score, item in scored if score >= 0.75]
    if not scored:
        source_tokens = name_tokens(source_name)
        if len(source_tokens) == 1:
            first = source_tokens[0]
            first_matches = [
                item
                for item in candidates
                if name_tokens(get_name(item)) and name_tokens(get_name(item))[0] == first
            ]
            if len(first_matches) == 1:
                return first_matches[0]
        return None

    scored.sort(key=lambda pair: pair[0], reverse=True)
    best_score = scored[0][0]
    best_items = [item for score, item in scored if score >= best_score - 0.02]
    if len(best_items) == 1:
        return best_items[0]
    return None
