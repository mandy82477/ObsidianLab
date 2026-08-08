"""Official skill / plugin repos — directory-membership diff.

Anthropic ships official Agent Skills from two repos, and *neither publishes
GitHub releases* (both `/releases` endpoints return an empty list), so the
existing GitHubReleases source is structurally blind to them:

  anthropics/skills                 the Skills format itself — spec, template,
                                    and the official skill library
  anthropics/knowledge-work-plugins per-role plugin bundles for Cowork
                                    (engineering, finance, legal, ...)

Watching commits would be pure noise — a typo fix in one skill's README is not
news. What *is* news is membership: a new skill directory appearing, or one
disappearing. So this source stores the set of known directory names per
watched path and emits only on set changes.

As with OfficialDocsWatch, a path seen for the first time is recorded silently
rather than emitted; otherwise adding a watch entry would announce every skill
that already existed as if it were new.
"""
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import requests

from news_aggregator.config import GITHUB_TOKEN, REQUEST_TIMEOUT
from news_aggregator.sources.base import BaseSource, FeedItem

logger = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).parent / "official_skills_repos.json"
STATE_PATH = Path(__file__).parent / "official_skills_repos_state.json"

API = "https://api.github.com/repos/{repo}/contents/{path}"

# Leave headroom for GitHubReleases, which shares the same hourly quota and
# runs its repo searches in the same pipeline pass.
RATE_LIMIT_FLOOR = 15


class OfficialSkillsRepos(BaseSource):
    def fetch(self) -> list[FeedItem]:
        try:
            watches = _load_watches()
        except Exception as e:
            logger.warning("Official skills repos config load failed: %s", e)
            return []

        if not watches:
            return []

        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "ClaudeNewsBot/1.0",
        }
        if GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

        state = _load_state()
        items: list[FeedItem] = []
        dirty = False

        for watch in watches:
            repo, path = watch.get("repo"), watch.get("path", "")
            if not repo:
                logger.warning("Official skills watch entry missing repo: %s", watch)
                continue
            key = f"{repo}/{path}"
            try:
                names, remaining = _list_dirs(repo, path, headers)
            except Exception as e:
                # Never take the pipeline down, and never overwrite the stored
                # set on failure — a half-read listing would read as deletions.
                logger.warning("Official skills watch '%s' failed: %s", key, e)
                continue

            prev = state.get(key)
            state[key] = sorted(names)
            dirty = True

            if prev is None:
                logger.info("Official skills watch '%s' baseline recorded (%d)", key, len(names))
            else:
                added = sorted(set(names) - set(prev))
                removed = sorted(set(prev) - set(names))
                if added or removed:
                    items.append(_item(watch, key, added, removed))

            if remaining is not None and remaining < RATE_LIMIT_FLOOR:
                logger.warning(
                    "GitHub rate limit low (%s remaining), stopping official skills watch",
                    remaining,
                )
                break

        if dirty:
            _save_state(state)

        return items


def _item(watch: dict, key: str, added: list[str], removed: list[str]) -> FeedItem:
    label = watch.get("label") or key
    parts = []
    if added:
        parts.append(f"新增 {len(added)} 項：{', '.join(added)}")
    if removed:
        parts.append(f"移除 {len(removed)} 項：{', '.join(removed)}")
    headline = "官方 Skills 異動" if added and not removed else "官方 Skills 目錄異動"
    return FeedItem(
        title=f"{headline}：{label}（{'／'.join(parts)}）",
        url=watch.get("url") or f"https://github.com/{watch['repo']}",
        source="Official Skills",
        published=datetime.now(tz=timezone.utc),
        score=0,
        summary=(
            f"{label} 的目錄成員有變動——{'；'.join(parts)}。"
            "此為官方 repo 的技能／外掛清單變更偵測（兩個 repo 皆不發 release，"
            "故以目錄成員差異取代版本追蹤），非新聞報導；細節需開啟連結確認。"
        ),
        category="official",
        score_unit="",
    )


def _load_watches() -> list[dict]:
    if not CONFIG_PATH.exists():
        logger.warning("Official skills repos config not found: %s", CONFIG_PATH)
        return []
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        logger.warning("Official skills repos config is invalid JSON: %s", e)
        return []
    return [w for w in (data.get("watches") or []) if w.get("status") != "retired"]


def _load_state() -> dict:
    if not STATE_PATH.exists():
        return {}
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        logger.warning("Official skills state unreadable, resetting: %s", e)
        return {}


def _save_state(state: dict) -> None:
    try:
        STATE_PATH.write_text(
            json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    except Exception as e:
        logger.warning("Official skills state write failed (non-fatal): %s", e)


def _list_dirs(repo: str, path: str, headers: dict) -> tuple[list[str], int | None]:
    """Return the directory names under `path`, plus remaining rate-limit budget."""
    resp = requests.get(
        API.format(repo=repo, path=path),
        headers=headers,
        timeout=REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    payload = resp.json()
    if not isinstance(payload, list):
        raise ValueError(f"unexpected contents payload for {repo}/{path}")

    try:
        remaining = int(resp.headers.get("X-RateLimit-Remaining", ""))
    except ValueError:
        remaining = None

    names = [e["name"] for e in payload if e.get("type") == "dir" and not e["name"].startswith(".")]
    return names, remaining
