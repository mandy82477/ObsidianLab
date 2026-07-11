import argparse
import json
import logging
import logging.handlers
import math
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, time as dt_time, timedelta, timezone
from pathlib import Path

import news_aggregator.config as _cfg
from news_aggregator.config import LOG_DIR, NEWS_DIR
from news_aggregator.dedup import deduplicate
from news_aggregator.digest import render
from news_aggregator.emitted_cache import (
    filter_new_or_reignited, load_cache, prune_expired, save_cache,
)
from news_aggregator.enricher import enrich
from news_aggregator.filter import filter_relevant
from news_aggregator.git_push import GitError, commit_and_push
from news_aggregator.sources.anthropic_blog import AnthropicBlog
from news_aggregator.sources.anthropic_status import AnthropicStatus
from news_aggregator.sources.api_docs import ApiDocs
from news_aggregator.sources.blogroll import Blogroll
from news_aggregator.sources.devto import DevTo
from news_aggregator.sources.github_releases import GitHubReleases
from news_aggregator.sources.github_issues import GitHubIssues
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
    p.add_argument(
        "--gather-only",
        action="store_true",
        help="Fetch, dedup, enrich, filter — then write gathered_items.json and exit (no LLM digest)",
    )
    return p.parse_args()


# score_unit values that denote a real engagement metric (vs "" = n/a). If a
# source returns items but ALL of them score 0 while claiming one of these units,
# the metric is silently broken (e.g. Reddit RSS has no vote count → always 0),
# which lets the whole source slip past downstream interaction gates unnoticed.
_REAL_SCORE_UNITS = {"分", "讚", "留言"}


def _warn_if_scores_all_zero(name: str, items: list, logger) -> None:
    if not items or any(getattr(it, "score", 0) for it in items):
        return
    claimed = {getattr(it, "score_unit", "") for it in items} & _REAL_SCORE_UNITS
    if claimed:
        logger.warning(
            "資料品質告警：來源 %s 回傳 %d 筆但 score 全為 0，score_unit 宣稱為真實指標 %s"
            "（疑似靜默劣化，該來源將被下游互動門檻全數擋掉）",
            name, len(items), "/".join(sorted(claimed)),
        )


def _count_by_prefix(items) -> dict[str, int]:
    """Group items by the leading part of their source label.

    "Hacker News / Show HN" → "Hacker News"; "Reddit / r/X · 週熱門" → "Reddit".
    """
    counts: dict[str, int] = {}
    for it in items:
        prefix = (getattr(it, "source", "") or "").split(" / ")[0].split(" · ")[0].strip()
        counts[prefix] = counts.get(prefix, 0) + 1
    return counts


def _map_prefix_to_registered(prefix: str, registered: list[str]) -> str | None:
    """Best-effort map a source-label prefix back to a registered source name."""
    if not prefix:
        return None
    for name in registered:
        if prefix == name:
            return name
    for name in registered:
        if prefix.startswith(name) or name.startswith(prefix):
            return name
    return None


def write_funnel_record(path, date, mode, lookback_hours, source_status,
                        filtered_items, emitted_items) -> None:
    """Append one JSON line of per-source funnel stats to `path`.

    Best-effort: any failure is logged as a warning and never interrupts the
    main pipeline.
    """
    logger = logging.getLogger(__name__)
    try:
        registered = list(source_status.keys())
        sources = {
            name: {
                "ok": bool(status.get("ok", False)),
                "gathered": int(status.get("count", 0)),
                "filtered": 0,
                "emitted": 0,
            }
            for name, status in source_status.items()
        }
        for stage, items in (("filtered", filtered_items), ("emitted", emitted_items)):
            for prefix, n in _count_by_prefix(items).items():
                name = _map_prefix_to_registered(prefix, registered)
                if name is None:
                    bucket = sources.setdefault(
                        "_unmapped",
                        {"ok": None, "gathered": 0, "filtered": 0, "emitted": 0},
                    )
                    bucket[stage] += n
                else:
                    sources[name][stage] += n
        record = {
            "date": date if isinstance(date, str) else date.isoformat(),
            "run_ts": datetime.now(tz=timezone.utc).isoformat(),
            "mode": mode,
            "lookback_hours": lookback_hours,
            "sources": sources,
            "totals": {
                "gathered": sum(s.get("gathered", 0) for s in sources.values()),
                "filtered": len(filtered_items),
                "emitted": len(emitted_items),
            },
        }
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception as e:
        logger.warning("source funnel 統計寫入失敗（不影響主流程）: %s", e)


def check_gap_lookback(target_date: date, news_dir=NEWS_DIR) -> str | None:
    """Return reason string if yesterday's digest is missing/empty (gap to cover),
    else None. Used to auto-extend LOOKBACK_HOURS to 50 on gather-only runs."""
    yesterday_file = news_dir / f"{(target_date - timedelta(days=1)).isoformat()}.md"
    if not yesterday_file.exists():
        return f"昨日日報 {yesterday_file.name} 不存在"
    try:
        if "今日無新增資訊" in yesterday_file.read_text(encoding="utf-8"):
            return f"昨日日報 {yesterday_file.name} 為空（今日無新增資訊）"
    except Exception:
        pass
    return None


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
        if args.gather_only:
            # Gap recovery: if yesterday's digest is missing or empty, extend the
            # lookback window to cover the hole left by a failed previous run.
            gap_reason = check_gap_lookback(target_date)
            if gap_reason and _cfg.LOOKBACK_HOURS < 50:
                _cfg.LOOKBACK_HOURS = 50
                logger.info("失敗補撈：%s → LOOKBACK_HOURS 延長為 50h", gap_reason)

    NEWS_DIR.mkdir(parents=True, exist_ok=True)

    sources = [
        ("Anthropic Blog", AnthropicBlog()),
        ("Anthropic Status", AnthropicStatus()),
        ("GitHub", GitHubReleases()),
        ("GitHub Issues", GitHubIssues()),
        ("Hacker News", HackerNews()),
        ("Reddit", Reddit()),
        ("Google News", GoogleNews()),
        ("dev.to", DevTo()),
        ("Claude API Release Notes", ApiDocs()),
        ("Blogroll", Blogroll()),
    ]

    all_items = []
    source_status: dict[str, dict] = {}

    def _fetch_source(name_source: tuple) -> tuple[str, list]:
        name, source = name_source
        return name, source.fetch()

    with ThreadPoolExecutor(max_workers=len(sources)) as pool:
        futures = {pool.submit(_fetch_source, ns): ns[0] for ns in sources}
        for fut in as_completed(futures):
            name = futures[fut]
            try:
                _, items = fut.result()
                all_items.extend(items)
                source_status[name] = {"ok": True, "count": len(items)}
                logger.info("%s: %d item(s)", name, len(items))
                _warn_if_scores_all_zero(name, items, logger)
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
    relevance_filtered = filtered  # snapshot for funnel stats (pre emitted-cache)

    if args.gather_only:
        # Cross-run dedup: drop items already emitted in a previous digest,
        # unless their score re-ignited (>= 2x and +10 since last emit).
        # Backfill runs (--date) must NOT touch the cache: they'd wrongly
        # drop items against a cache built from today's dates, and would
        # pollute the cache with the backfilled (past) date on save.
        updated_cache = None
        if args.gather_only and not args.date:
            emitted = prune_expired(load_cache(), today=target_date)
            before_cache = len(filtered)
            filtered, updated_cache = filter_new_or_reignited(filtered, emitted, today=target_date)
            logger.info("Emitted-cache filter: %d → %d items", before_cache, len(filtered))
        else:
            logger.info("Emitted-cache filter: skipped for backfill (--date %s)", args.date)

        # Write gathered items to JSON for Claude session to analyse
        out = {
            "date": target_date.isoformat(),
            "article_count": len(filtered),
            "source_status": source_status,
            "items": [
                {
                    "title":     it.title,
                    "url":       it.url,
                    "source":    it.source,
                    "published": it.published.strftime("%m/%d %H:%M UTC") if it.published else "",
                    "score":     it.score,
                    "score_unit": it.score_unit,
                    "source_count": it.source_count,
                    "summary":   it.summary or "",
                    "category":  it.category,
                }
                for it in filtered
            ],
        }
        gather_path = LOG_DIR.parent / "gathered_items.json"
        gather_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
        logger.info("--gather-only: wrote %d items to %s", len(filtered), gather_path)
        # Persist emitted cache only after the output JSON was written successfully.
        # Skipped entirely for backfill runs — see cache-skip comment above.
        if updated_cache is not None:
            save_cache(updated_cache)
        write_funnel_record(
            _cfg.FUNNEL_FILE, target_date,
            "backfill" if args.date else "gather",
            _cfg.LOOKBACK_HOURS, source_status,
            relevance_filtered, filtered,
        )
        elapsed = time.time() - start
        logger.info("=== Gather complete: %d items / %d sources / %.1fs ===", len(filtered), len(sources), elapsed)
        return

    write_funnel_record(
        _cfg.FUNNEL_FILE, target_date,
        "backfill" if args.date else "render",
        _cfg.LOOKBACK_HOURS, source_status,
        relevance_filtered, filtered,
    )

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
