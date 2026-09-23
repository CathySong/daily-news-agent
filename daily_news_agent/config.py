from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .models import FeedSource


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected YAML object in {path}")
    return data


def load_sources(path: str | Path) -> list[FeedSource]:
    data = load_yaml(path)
    groups = data.get("rss_sources", {})
    sources: list[FeedSource] = []
    for category, payload in groups.items():
        for feed in payload.get("feeds", []):
            sources.append(
                FeedSource(
                    category=category,
                    name=feed["name"],
                    url=feed["url"],
                )
            )
    return sources


def load_filter_terms(path: str | Path, filter_name: str = "long_covid") -> dict[str, list[str]]:
    data = load_yaml(path)
    filters = data.get(filter_name)
    if not isinstance(filters, dict):
        raise ValueError(f"Missing filter group: {filter_name}")
    return {key: list(value or []) for key, value in filters.items()}
