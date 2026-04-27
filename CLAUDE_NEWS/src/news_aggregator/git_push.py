import logging
import subprocess
from pathlib import Path

from news_aggregator.config import REPO_ROOT

logger = logging.getLogger(__name__)


class GitError(Exception):
    pass


def commit_and_push(digest_path: Path) -> None:
    rel_path = digest_path.relative_to(REPO_ROOT).as_posix()
    date_str = digest_path.stem

    _run(["git", "add", rel_path], "git add")
    # Also commit seen_urls.json so dedup state persists across runs
    seen_urls_path = REPO_ROOT / "src" / "news_aggregator" / "seen_urls.json"
    if seen_urls_path.exists():
        seen_urls = seen_urls_path.relative_to(REPO_ROOT).as_posix()
        _run(["git", "add", seen_urls], "git add seen_urls")
    _run(["git", "commit", "-m", f"news: daily digest {date_str}"], "git commit", allow_nothing=True)
    _run(["git", "push"], "git push")
    logger.info("Git: pushed %s", rel_path)


def _run(cmd: list[str], label: str, allow_nothing: bool = False) -> None:
    result = subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        if allow_nothing and "nothing to commit" in stderr:
            logger.info("%s: nothing to commit (idempotent)", label)
            return
        raise GitError(f"{label} failed (rc={result.returncode}): {stderr}")
