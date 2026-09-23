from daily_news_agent.models import NewsItem
from daily_news_agent.render import render_markdown


def test_render_markdown_includes_source_and_link():
    item = NewsItem(
        title="Long COVID study finds new marker",
        link="https://example.com/story",
        source="Example Feed",
        category="research",
        score=7,
        matched_terms=("long covid",),
    )

    output = render_markdown([item])

    assert "Long COVID study finds new marker" in output
    assert "Example Feed" in output
    assert "https://example.com/story" in output
