import logging
import logging.handlers
import time
from datetime import date, datetime, timezone

from news_aggregator.config import LOG_DIR, NEWS_DIR
from news_aggregator.dedup import deduplicate
from news_aggregator.digest import render
from news_aggregator.enricher import enrich
from news_aggregator.filter import filter_relevant
from news_aggregator.git_push import GitError, commit_and_push
from news_aggregator.sources.anthropic_blog import AnthropicBlog
from news_aggregator.sources.github_releases import GitHubReleases
from news_aggregator.sources.google_news import GoogleNews
from news_aggregator.sources.hackernews import HackerNews
from news_aggregator.sources.reddit import Reddit


def setup_logging() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOG_DIR / "news_aggregator.log"
    handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[handler, logging.StreamHandler()],
    )


def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)
    start = time.time()
    logger.info("=== News aggregator run started ===")

    NEWS_DIR.mkdir(parents=True, exist_ok=True)

    sources = [
        ("Anthropic Blog", AnthropicBlog()),
        ("GitHub", GitHubReleases()),
        ("Hacker News", HackerNews()),
        ("Reddit", Reddit()),
        ("Google News", GoogleNews()),
    ]

    all_items = []
    source_status: dict[str, dict] = {}

    for name, source in sources:
        try:
            items = source.fetch()
            all_items.extend(items)
            source_status[name] = {"ok": True, "count": len(items)}
            logger.info("%s: %d item(s)", name, len(items))
        except Exception as e:
            source_status[name] = {"ok": False, "count": 0}
            logger.warning("%s: fetch raised unexpected exception: %s", name, e)

    deduped = deduplicate(all_items)
    logger.info("After dedup: %d items (was %d)", len(deduped), len(all_items))

    enriched = enrich(deduped)
    logger.info("Enrichment done: %d items", len(enriched))

    filtered = filter_relevant(enriched)
    logger.info("After relevance filter: %d items", len(filtered))

    today = date.today()
    digest_path = render(filtered, today, source_status)
    logger.info("Digest written: %s", digest_path)

    try:
        commit_and_push(digest_path)
    except GitError as e:
        logger.warning("Git push skipped: %s", e)

    elapsed = time.time() - start
    logger.info("=== Run complete: %d items / %d sources / %.1fs ===", len(deduped), len(sources), elapsed)


if __name__ == "__main__":
    main()
