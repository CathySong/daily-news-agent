# Daily News Agent

RSS-based briefing agent that filters health and policy feeds for high-signal Long COVID stories. It loads feed sources from YAML, scores entries against configurable topic terms, ranks the results, and renders a Markdown briefing.

## Why This Project Exists

News feeds are noisy. This project shows a lightweight agent pipeline for turning broad RSS sources into a focused daily briefing that can be scheduled, emailed, or posted to a chat app.

## Features

- YAML-configured RSS source groups
- Topic filter with primary, medical, policy, and exclude terms
- Deterministic relevance scoring
- Markdown briefing renderer
- CLI for local or scheduled runs
- Unit tests and GitHub Actions CI

## Quick Start

```bash
git clone https://github.com/CathySong/daily-news-agent.git
cd daily-news-agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m daily_news_agent.cli --limit 5
```

Write the briefing to a file:

```bash
python -m daily_news_agent.cli --limit 8 --output briefing.md
```

## Configuration

RSS feeds live in `config/rss_sources.yaml`.

Filter terms live in `config/long_covid_filter.yaml`:

- `primary_keywords`: high-signal terms such as `long covid`
- `medical_terms`: symptoms and scientific terms
- `policy_terms`: public-health and workforce terms
- `exclude_keywords`: terms that reduce relevance

## Project Structure

```text
daily_news_agent/
  cli.py       Command-line entry point
  config.py    YAML loading
  fetcher.py   RSS fetching and parsing
  scoring.py   Relevance scoring and ranking
  render.py    Markdown output
config/        RSS sources and topic filters
tests/         Unit tests
```

## Tests

```bash
pytest
```

## Next Improvements

- Add date-window filtering
- Add source reliability weights
- Add duplicate clustering by title/link similarity
- Add delivery adapters for email, Telegram, or Slack
- Add LLM summarization as an optional post-processing step
