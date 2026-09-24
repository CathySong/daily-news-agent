from daily_news_agent.models import NewsItem
from daily_news_agent.scoring import rank_items, score_text


FILTERS = {
    "primary_keywords": ["long covid", "post-covid"],
    "medical_terms": ["brain fog", "POTS"],
    "policy_terms": ["disability"],
    "exclude_keywords": ["opinion"],
}


def test_score_text_weights_primary_and_secondary_terms():
    score, terms = score_text(
        "New long covid research links brain fog and disability policy",
        FILTERS,
    )

    assert score == 9
    assert terms == ("long covid", "brain fog", "disability")


def test_score_text_penalizes_excluded_terms():
    score, terms = score_text("Opinion: long covid policy debate", FILTERS)

    assert score == 0
    assert terms == ("long covid", "exclude:opinion")


def test_rank_items_orders_by_score():
    items = [
        NewsItem(title="low", link="https://example.com/1", source="A", category="test", score=1),
        NewsItem(title="high", link="https://example.com/2", source="A", category="test", score=5),
    ]

    assert [item.title for item in rank_items(items)] == ["high", "low"]
