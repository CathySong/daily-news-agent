from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class FeedSource:
    category: str
    name: str
    url: str


@dataclass(frozen=True)
class NewsItem:
    title: str
    link: str
    source: str
    category: str
    summary: str = ""
    published: datetime | None = None
    matched_terms: tuple[str, ...] = field(default_factory=tuple)
    score: int = 0

    @property
    def published_sort_key(self) -> datetime:
        return self.published or datetime.fromtimestamp(0, tz=timezone.utc)
