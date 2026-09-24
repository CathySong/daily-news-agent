from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

import feedparser

from .models import FeedSource, NewsItem
from .scoring import score_text


def parse_published(entry: object) -> datetime | None:
    published = getattr(entry, "published", None) or getattr(entry, "updated", None)
    if not published:
        return None
    try:
        value = parsedate_to_datetime(published)
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def item_from_entry(source: FeedSource, entry: object, filters: dict[str, list[str]]) -> NewsItem:
    title = getattr(entry, "title", "").strip()
    link = getattr(entry, "link", "").strip()
    summary = getattr(entry, "summary", "").strip()
    score, matched_terms = score_text(f"{title} {summary}", filters)
    return NewsItem(
        title=title,
        link=link,
        source=source.name,
        category=source.category,
        summary=summary,
        published=parse_published(entry),
        matched_terms=matched_terms,
        score=score,
    )


def fetch_source(source: FeedSource, filters: dict[str, list[str]]) -> list[NewsItem]:
    parsed = feedparser.parse(source.url)
    return [
        item_from_entry(source, entry, filters)
        for entry in parsed.entries
        if getattr(entry, "title", None) and getattr(entry, "link", None)
    ]
