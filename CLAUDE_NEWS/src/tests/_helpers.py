"""Shared test helpers: load scripts/*.py as modules without touching sys.path
permanently, and locate the repo root / fixtures dir.

scripts/build_web.py and scripts/check_links.py are plain scripts (no package
__init__.py in scripts/), so we load them via importlib from their absolute
path. This avoids any reliance on cwd or PYTHONPATH.
"""
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def load_script_module(name: str):
    """Import scripts/{name}.py as a standalone module named 'script_{name}'.

    Cached in sys.modules so repeated calls in the same test run reuse the
    same module object instead of re-executing top-level code every time.
    """
    mod_name = f"script_{name}"
    if mod_name in sys.modules:
        return sys.modules[mod_name]
    path = SCRIPTS_DIR / f"{name}.py"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = module
    spec.loader.exec_module(module)
    return module
