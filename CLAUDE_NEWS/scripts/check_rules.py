#!/usr/bin/env python3
"""
check_rules.py — 通用規則一致性檢查引擎（取代 /review-commands 手動機械檢查）。

只用標準庫（re / json / pathlib），不 subprocess 呼叫 grep（跨平台考量）。
讀取 REPO_ROOT/.claude/review-registry.json，對 .claude/commands/、.claude/rules/
（或 registry 指定的其他 glob）執行五類確定性檢查：

    1. bare_references   — 裸露引用（如無路徑前綴的 CLAUDE.md）
    2. path_existence     — backtick 路徑存在性
    3. anchors             — 錨點字串必須存在於指定檔案
    4. sync_pairs           — 同步配對斷言（all_contain / equal_values / min_count）
    5. coupling_hints（warn-only）— 高頻互相引用但未登記 sync_pair 的檔案對提示

用法：
    python scripts/check_rules.py

行為：
    全部通過（含 warn-only）→ exit 0，列印報告
    任何確定性檢查（1–4）失敗 → exit 1，列印報告與失敗明細
    coupling_hints 不影響 exit code，只在報告中列出

供 scripts/run_tests.py 呼叫，也供 .claude/commands/review-commands.md 呼叫。
"""
from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO_ROOT / ".claude" / "review-registry.json"


def _stdout():
    if hasattr(sys.stdout, "buffer"):
        return io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    return sys.stdout


class Report:
    """收集各檢查結果，最後統一輸出人類可讀報告。"""

    def __init__(self):
        self.sections: list[dict] = []
        self.ok = True

    def add(self, name: str, passed: bool, details: list[str], warn_only: bool = False):
        self.sections.append(
            {"name": name, "passed": passed, "details": details, "warn_only": warn_only}
        )
        if not passed and not warn_only:
            self.ok = False

    def render(self) -> str:
        lines = ["# check_rules.py 報告", ""]
        for sec in self.sections:
            icon = "✅" if sec["passed"] else ("⚠️" if sec["warn_only"] else "❌")
            lines.append(f"{icon} {sec['name']}")
            for d in sec["details"]:
                lines.append(f"    {d}")
            lines.append("")
        lines.append("=" * 40)
        if self.ok:
            lines.append("狀態：✅ 全部確定性檢查通過")
        else:
            lines.append("狀態：❌ 有確定性檢查失敗，exit 1")
        return "\n".join(lines)


def load_registry() -> dict:
    if not REGISTRY_PATH.exists():
        raise SystemExit(f"找不到 registry：{REGISTRY_PATH}")
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def resolve_glob(pattern: str) -> list[Path]:
    return sorted(REPO_ROOT.glob(pattern))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


# ---------------------------------------------------------------------------
# 檢查 1：裸露引用（bare_references）
# ---------------------------------------------------------------------------

def check_bare_references(cfg: dict, report: Report):
    if not cfg:
        return
    globs = cfg.get("globs", [])
    pattern = cfg.get("pattern", r"CLAUDE\.md")
    exempt_files = set(cfg.get("exempt_files", []))
    line_allowlist = cfg.get("line_allowlist", [])
    # 每個 allowlist 項目：{"file": "...", "pattern": "regex"}，僅套用於指定檔案
    allow_by_file: dict[str, list[re.Pattern]] = {}
    for item in line_allowlist:
        allow_by_file.setdefault(item["file"], []).append(re.compile(item["pattern"]))

    bare_re = re.compile(pattern)
    backtick_span_re = re.compile(r"`([^`]+)`")

    violations: list[str] = []
    files_checked = 0

    for g in globs:
        for path in resolve_glob(g):
            relpath = rel(path)
            if relpath in exempt_files:
                continue
            files_checked += 1
            text = read_text(path)
            for lineno, line in enumerate(text.splitlines(), start=1):
                if not bare_re.search(line):
                    continue
                # 先看此行是否被 allowlist 豁免
                exempt_patterns = allow_by_file.get(relpath, [])
                if any(p.search(line) for p in exempt_patterns):
                    continue

                # 找出所有 backtick span，判斷 span 內的 CLAUDE.md 是否有路徑前綴（含 /）
                spans = backtick_span_re.findall(line)
                line_without_backticks = backtick_span_re.sub("", line)

                bad_in_backtick = False
                for span in spans:
                    if bare_re.search(span):
                        if not re.search(r"[\w./-]+/" + pattern, span):
                            bad_in_backtick = True

                bad_bare_text = bool(bare_re.search(line_without_backticks))

                if bad_in_backtick or bad_bare_text:
                    violations.append(f"{relpath}:{lineno}: {line.strip()}")

    passed = not violations
    details = [f"掃描 {files_checked} 檔案"]
    if violations:
        details.append(f"發現 {len(violations)} 處裸露引用：")
        details.extend(f"  - {v}" for v in violations)
    else:
        details.append("無裸露引用")
    report.add("檢查 1：裸露引用（bare_references）", passed, details)


# ---------------------------------------------------------------------------
# 檢查 2：路徑存在性（path_existence）
# ---------------------------------------------------------------------------

def check_path_existence(cfg: dict, report: Report):
    if not cfg:
        return
    globs = cfg.get("globs", [])
    extensions = tuple(cfg.get("extensions", [".md", ".py", ".json", ".jsonl"]))
    allow_regexes = [re.compile(p) for p in cfg.get("allowlist_patterns", [])]
    bare_name_dirs = cfg.get("bare_name_search_dirs", {})  # {"filename.md": ["wiki/topics", ...]}

    path_re = re.compile(r"`([^`]+)`")
    slashy_path_re = re.compile(r"^[\w./\\-]+\.(?:%s)$" % "|".join(e.lstrip(".") for e in extensions))

    missing: list[str] = []
    checked = 0

    for g in globs:
        for path in resolve_glob(g):
            relpath = rel(path)
            text = read_text(path)
            for lineno, line in enumerate(text.splitlines(), start=1):
                for span in path_re.findall(line):
                    span = span.strip()
                    if not slashy_path_re.match(span):
                        continue
                    if "/" not in span and "\\" not in span:
                        # 裸檔名：只在 registry 有登記解析目錄時才檢查
                        candidates = bare_name_dirs.get(span)
                        if not candidates:
                            continue
                        checked += 1
                        if any((REPO_ROOT / d / span).exists() for d in candidates):
                            continue
                        if any(rx.search(span) for rx in allow_regexes):
                            continue
                        missing.append(
                            f"{relpath}:{lineno}: 裸檔名 `{span}` 於 {candidates} 皆找不到"
                        )
                        continue

                    if any(rx.search(span) for rx in allow_regexes):
                        continue

                    checked += 1
                    target = (REPO_ROOT / span).resolve()
                    if not target.exists():
                        missing.append(f"{relpath}:{lineno}: `{span}` 不存在")

    passed = not missing
    details = [f"驗證 {checked} 個路徑引用"]
    if missing:
        details.append(f"發現 {len(missing)} 個不存在的路徑：")
        details.extend(f"  - {m}" for m in missing)
    else:
        details.append("全部存在")
    report.add("檢查 2：路徑存在性（path_existence）", passed, details)


# ---------------------------------------------------------------------------
# 檢查 3：錨點（anchors）
# ---------------------------------------------------------------------------

def check_anchors(cfg: list, report: Report):
    if not cfg:
        return
    missing: list[str] = []
    checked = 0
    for item in cfg:
        pattern = item["pattern"]
        target = item["file"]
        target_path = REPO_ROOT / target
        checked += 1
        if not target_path.exists():
            missing.append(f"{item.get('label', pattern)} → 檔案不存在：{target}")
            continue
        text = read_text(target_path)
        if not re.search(pattern, text):
            missing.append(f"{item.get('label', pattern)} → 未在 {target} 中找到 `{pattern}`")

    passed = not missing
    details = [f"驗證 {checked} 個錨點"]
    if missing:
        details.extend(f"  - {m}" for m in missing)
    else:
        details.append("全部有效")
    report.add("檢查 3：錨點（anchors）", passed, details)


# ---------------------------------------------------------------------------
# 檢查 4：同步配對（sync_pairs）
# ---------------------------------------------------------------------------

def _assert_all_contain(pair: dict) -> list[str]:
    failures = []
    for f in pair["files"]:
        target = REPO_ROOT / f
        if not target.exists():
            failures.append(f"{f}：檔案不存在")
            continue
        text = read_text(target)
        for pattern in pair["patterns"]:
            if not re.search(pattern, text):
                failures.append(f"{f}：缺少 `{pattern}`")
    return failures


def _assert_min_count(pair: dict) -> list[str]:
    failures = []
    n = pair.get("min", 1)
    for f in pair["files"]:
        target = REPO_ROOT / f
        if not target.exists():
            failures.append(f"{f}：檔案不存在")
            continue
        text = read_text(target)
        for pattern in pair["patterns"]:
            count = len(re.findall(pattern, text))
            if count < n:
                failures.append(f"{f}：`{pattern}` 只出現 {count} 次（需 ≥ {n}）")
    return failures


def _assert_equal_values(pair: dict) -> list[str]:
    failures = []
    pattern = pair["pattern"]
    values_by_file: dict[str, list[str]] = {}
    for f in pair["files"]:
        target = REPO_ROOT / f
        if not target.exists():
            failures.append(f"{f}：檔案不存在")
            continue
        text = read_text(target)
        matches = re.findall(pattern, text)
        values_by_file[f] = [m.strip() if isinstance(m, str) else m for m in matches]

    all_values = set()
    for vals in values_by_file.values():
        all_values.update(vals)

    if len(all_values) > 1:
        detail = "; ".join(f"{f}={vals}" for f, vals in values_by_file.items())
        failures.append(f"數值不一致（pattern=`{pattern}`）：{detail}")
    elif not all_values:
        failures.append(f"pattern=`{pattern}` 在任何檔案中都沒有匹配到值")
    return failures


ASSERTION_HANDLERS = {
    "all_contain": _assert_all_contain,
    "min_count": _assert_min_count,
    "equal_values": _assert_equal_values,
}


def check_sync_pairs(cfg: list, report: Report):
    if not cfg:
        return
    total_failures = 0
    details = []
    for pair in cfg:
        name = pair["name"]
        assertion = pair["assertion"]
        handler = ASSERTION_HANDLERS.get(assertion)
        if handler is None:
            details.append(f"❌ {name}：未知斷言類型 `{assertion}`")
            total_failures += 1
            continue
        failures = handler(pair)
        if failures:
            details.append(f"❌ {name}：")
            details.extend(f"    - {f}" for f in failures)
            total_failures += len(failures)
        else:
            details.append(f"✅ {name}")

    passed = total_failures == 0
    report.add(f"檢查 4：同步配對（sync_pairs，共 {len(cfg)} 組）", passed, details)


# ---------------------------------------------------------------------------
# 檢查 5：coupling hints（warn-only）
# ---------------------------------------------------------------------------

def check_coupling_hints(cfg: dict, sync_pairs_cfg: list, report: Report):
    if not cfg or not cfg.get("enabled", True):
        return
    globs = cfg.get("globs", [])
    min_refs = cfg.get("min_mutual_references", 2)

    files = []
    for g in globs:
        files.extend(resolve_glob(g))
    files = sorted(set(files))

    texts = {f: read_text(f) for f in files}
    names = {f: f.name for f in files}

    # 已登記的 sync_pair 檔案組合
    registered_pairs = set()
    for pair in sync_pairs_cfg or []:
        fs = pair.get("files", [])
        for i in range(len(fs)):
            for j in range(i + 1, len(fs)):
                registered_pairs.add(frozenset([fs[i], fs[j]]))

    hints = []
    for f1 in files:
        for f2 in files:
            if f1 >= f2:
                continue
            n1 = names[f1]
            n2 = names[f2]
            count_1_to_2 = len(re.findall(re.escape(n2), texts[f1]))
            count_2_to_1 = len(re.findall(re.escape(n1), texts[f2]))
            total = count_1_to_2 + count_2_to_1
            if total >= min_refs:
                pair_key = frozenset([rel(f1), rel(f2)])
                if pair_key not in registered_pairs:
                    hints.append(f"{rel(f1)} <-> {rel(f2)}（互引 {total} 次，未登記 sync_pair）")

    details = []
    if hints:
        details.append(f"發現 {len(hints)} 組高頻互引但未登記的檔案對（僅提示，不阻塞）：")
        details.extend(f"  - {h}" for h in hints)
    else:
        details.append("無新的高頻互引提示")
    report.add("檢查 5：coupling hints（warn-only）", True, details, warn_only=True)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    stream = _stdout()
    registry = load_registry()
    report = Report()

    check_bare_references(registry.get("bare_references"), report)
    check_path_existence(registry.get("path_existence"), report)
    check_anchors(registry.get("anchors"), report)
    check_sync_pairs(registry.get("sync_pairs"), report)
    check_coupling_hints(registry.get("coupling_hints"), registry.get("sync_pairs"), report)

    stream.write(report.render() + "\n")
    stream.flush()
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
