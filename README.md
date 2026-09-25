# Daily News Agent

Configurable AI research agent for monitoring sources, filtering noisy feeds, and producing concise daily briefings.

The project is intentionally small: it shows the core pieces of an automated intelligence workflow without hiding the logic behind a large app shell.

## What It Does

- Pulls from configurable RSS source groups
- Applies topic-specific keyword filters
- Supports focused monitoring for health, policy, research, and emerging technology themes
- Produces briefing-ready inputs for an AI summarization layer
- Keeps source and filter configuration in editable YAML files

## Repo Structure

```text
daily-news-agent/
├── config/
│   ├── rss_sources.yaml        # Source groups and feed URLs
│   └── long_covid_filter.yaml  # Example topic filter
├── requirements.txt
└── README.md
```

## Quick Start

```bash
git clone https://github.com/CathySong/daily-news-agent.git
cd daily-news-agent

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Customize the source list in `config/rss_sources.yaml` and topic rules in `config/long_covid_filter.yaml`.

## Example Configuration Pattern

```yaml
rss_sources:
  research_journals:
    description: "Research and journal feeds"
    feeds:
      - name: Example Journal
        url: https://example.com/feed.xml
```

```yaml
topic_filter:
  primary_keywords:
    - target topic
  exclude_keywords:
    - opinion
    - unverified
```

## Why This Is Useful

Daily briefings are a strong applied-AI pattern: the system needs source selection, retrieval, filtering, ranking, summarization, and delivery. This repo captures the configuration layer for that workflow and can be extended into a scheduled agent with evaluation for relevance, novelty, and source quality.

## Portfolio Signal

For AI Engineer and Staff Data Scientist roles, this project demonstrates:

- practical agent workflow design;
- signal extraction from noisy sources;
- configuration-driven data products;
- explainable filtering rules;
- a foundation for scheduled research automation.

## Next Improvements

- Add a CLI entry point for fetching and scoring feed items
- Add tests for filter matching and source validation
- Add a GitHub Actions schedule for daily runs
- Add structured output for downstream LLM summarization
