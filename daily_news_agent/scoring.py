from __future__ import annotations

import re

from .models import NewsItem


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def score_text(text: str, filters: dict[str, list[str]]) -> tuple[int, tuple[str, ...]]:
    haystack = normalize(text)
    score = 0
    matched: list[str] = []

    weights = {
        "primary_keywords": 5,
        "medical_terms": 2,
        "policy_terms": 2,
    }

    for group, weight in weights.items():
        for term in filters.get(group, []):
            if normalize(term) in haystack:
                score += weight
                matched.append(term)

    for term in filters.get("exclude_keywords", []):
        if normalize(term) in haystack:
            score -= 5
            matched.append(f"exclude:{term}")

    return score, tuple(dict.fromkeys(matched))


def rank_items(items: list[NewsItem]) -> list[NewsItem]:
    return sorted(
        items,
        key=lambda item: (item.score, item.published_sort_key),
        reverse=True,
    )
