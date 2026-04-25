import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

SEARCH_TERMS = ["Claude Code", "claude-code", "Anthropic"]
LOOKBACK_HOURS = 26

REPO_ROOT = Path(__file__).parent.parent
NEWS_DIR = REPO_ROOT / "news"
LOG_DIR = REPO_ROOT / "logs"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")

REQUEST_TIMEOUT = 15
MAX_ITEMS_PER_SOURCE = 20

SEEN_CACHE_FILE = REPO_ROOT / "news_aggregator" / "seen_urls.json"
