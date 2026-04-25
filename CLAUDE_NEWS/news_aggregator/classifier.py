import re
from news_aggregator.sources.base import FeedItem

# Keywords for each topic bucket
_PRICING_KW = re.compile(
    r"pric|billing|subscri|plan|payment|tier|quota|cost|pro\b|max\b|free\b|paid|charge|invoice|limit|token.{0,20}cost",
    re.I,
)
_TECH_UPDATE_KW = re.compile(
    r"releas|launch|introduc|announc|update|upgrad|new.{0,15}model|new.{0,15}feature|sdk|api.{0,10}v\d|v\d+\.\d|changelog|deprecat|breaking.change|claude.opus|claude.sonnet|claude.haiku|claude.code.v|mcp\b",
    re.I,
)
_TECH_DISCUSS_KW = re.compile(
    r"how.to|benchmark|compar|vs\b|versus|trick|tip|workflow|agent|tool.use|prompt|context|performance|speed|latency|memory|token|integrat|plugin|extension|hook|review|experience|using|test|build|show.hn|ask.hn",
    re.I,
)

# Score threshold for an item to count as "significant discussion"
HIGH_SCORE = 50

# Topic labels
PRICING = "pricing"
TECH_UPDATE = "tech_update"
TECH_DISCUSS = "tech_discuss"
OTHER = "other"


def classify(item: FeedItem) -> str:
    text = f"{item.title} {item.summary}"
    if _PRICING_KW.search(text):
        return PRICING
    if item.category == "official" or _TECH_UPDATE_KW.search(text):
        return TECH_UPDATE
    if _TECH_DISCUSS_KW.search(text):
        return TECH_DISCUSS
    return TECH_DISCUSS  # default community items to discussion bucket


def find_highlights(items: list[FeedItem]) -> set[str]:
    """Return URLs of items that deserve a special highlight.

    An item is highlighted if:
    - It has a very high community score (>= HIGH_SCORE), OR
    - Its topic appears in BOTH official and community sources (cross-source buzz).
    """
    highlights: set[str] = set()

    # High-score items
    for item in items:
        if item.score >= HIGH_SCORE:
            highlights.add(item.url)

    # Cross-source buzz: same keyword cluster in official + community
    official_titles = " ".join(i.title for i in items if i.category == "official").lower()
    for item in items:
        if item.category == "community" and item.score > 0:
            # Check if any significant word from this title appears in official titles
            words = [w for w in re.findall(r"[a-z]{4,}", item.title.lower()) if w not in _STOPWORDS]
            if any(w in official_titles for w in words):
                highlights.add(item.url)

    return highlights


_STOPWORDS = {
    "this", "that", "with", "from", "have", "been", "will", "your", "their",
    "what", "when", "where", "which", "about", "just", "show", "using", "code",
    "claude", "anthropic", "model",
}
