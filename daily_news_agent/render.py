from __future__ import annotations

from datetime import timezone

from .models import NewsItem


def render_markdown(items: list[NewsItem], title: str = "Daily News Briefing") -> str:
    lines = [f"# {title}", ""]
    if not items:
        return "# Daily News Briefing\n\nNo matching stories found."

    for index, item in enumerate(items, start=1):
        date = ""
        if item.published:
            date = item.published.astimezone(timezone.utc).strftime("%Y-%m-%d")
        terms = ", ".join(item.matched_terms) if item.matched_terms else "general relevance"
        lines.extend(
            [
                f"## {index}. {item.title}",
                f"- Source: {item.source} ({item.category})",
                f"- Date: {date or 'unknown'}",
                f"- Relevance score: {item.score}",
                f"- Matched terms: {terms}",
                f"- Link: {item.link}",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"
