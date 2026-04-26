import os
from pathlib import Path
from dotenv import load_dotenv

SRC_DIR = Path(__file__).parent.parent        # src/
REPO_ROOT = SRC_DIR.parent                    # CLAUDE_NEWS/

load_dotenv(REPO_ROOT / ".env")

SEARCH_TERMS = ["Claude Code", "claude-code", "Anthropic"]
LOOKBACK_HOURS = 26

NEWS_DIR = REPO_ROOT / "news"                 # CLAUDE_NEWS/news/
LOG_DIR = SRC_DIR / "logs"                    # src/logs/

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")

REQUEST_TIMEOUT = 15
MAX_ITEMS_PER_SOURCE = 20

SEEN_CACHE_FILE = Path(__file__).parent / "seen_urls.json"  # src/news_aggregator/seen_urls.json
