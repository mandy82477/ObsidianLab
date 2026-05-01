import argparse
import logging
import logging.handlers
import math
import time
from datetime import date, datetime, time as dt_time, timedelta, timezone

import news_aggregator.config as _cfg
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


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Claude/Anthropic news aggregator")
    p.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        help="Backfill date: fetch news for exactly this day (default: today)",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    setup_logging()
    logger = logging.getLogger(__name__)
    start = time.time()

    # ── Date / lookback setup ─────────────────────────────────────────────────
    until_dt: datetime | None = None
    if args.date:
        target_date = date.fromisoformat(args.date)
        since_dt = datetime.combine(target_date, dt_time.min, tzinfo=timezone.utc)
        until_dt = since_dt + timedelta(days=1)
        now_utc = datetime.now(tz=timezone.utc)
        lookback = math.ceil((now_utc - since_dt).total_seconds() / 3600) + 1
        _cfg.LOOKBACK_HOURS = lookback
        logger.info(
            "=== News aggregator run started (backfill %s, lookback=%dh) ===",
            args.date, lookback,
        )
    else:
        target_date = date.today()
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

    # Backfill: drop articles published AFTER the target day ends
    if until_dt is not None:
        before_clip = len(deduped)
        deduped = [it for it in deduped if it.published is None or it.published < until_dt]
        logger.info("Clipped to %s window: %d → %d items", args.date, before_clip, len(deduped))

    enriched = enrich(deduped)
    logger.info("Enrichment done: %d items", len(enriched))

    filtered = filter_relevant(enriched)
    logger.info("After relevance filter: %d items", len(filtered))

    digest_path, is_fallback = render(filtered, target_date, source_status)
    logger.info("Digest written: %s", digest_path)

    if is_fallback:
        logger.warning("Digest is fallback (plain list) — skipping git push")
    else:
        try:
            commit_and_push(digest_path)
        except GitError as e:
            logger.warning("Git push skipped: %s", e)

    elapsed = time.time() - start
    logger.info("=== Run complete: %d items / %d sources / %.1fs ===", len(deduped), len(sources), elapsed)


if __name__ == "__main__":
    main()
