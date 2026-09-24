from __future__ import annotations

import argparse
from pathlib import Path

from .config import load_filter_terms, load_sources
from .fetcher import fetch_source
from .render import render_markdown
from .scoring import rank_items


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a filtered RSS news briefing.")
    parser.add_argument("--sources", default="config/rss_sources.yaml", help="RSS source YAML path")
    parser.add_argument("--filters", default="config/long_covid_filter.yaml", help="Filter YAML path")
    parser.add_argument("--limit", type=int, default=8, help="Maximum stories to include")
    parser.add_argument("--min-score", type=int, default=1, help="Minimum relevance score")
    parser.add_argument("--output", help="Optional Markdown output path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    filters = load_filter_terms(args.filters)
    sources = load_sources(args.sources)

    items = []
    for source in sources:
        items.extend(fetch_source(source, filters))

    ranked = [item for item in rank_items(items) if item.score >= args.min_score]
    markdown = render_markdown(ranked[: args.limit], title="Long COVID Daily News Briefing")

    if args.output:
        Path(args.output).write_text(markdown, encoding="utf-8")
    else:
        print(markdown)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
