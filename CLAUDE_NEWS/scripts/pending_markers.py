#!/usr/bin/env python3
"""懸置標記的共用解析庫 — audit / scan / check 三支腳本的單一事實來源。

語法規格見 `.claude/rules/wiki-ingest-format.md`「懸置標記語法」節。**規格與本檔
的 regex 必須一致**，改一邊要改另一邊。

設計的關鍵決定：**識別錨點不是「待查證」這個詞，而是散文裡不可能出現的 metadata
區塊 `（標 YYYY-MM-DD｜查 探針…）`。** 拿自然語言詞彙當錨點會踩到四種假陽性，
而它們全都不帶 metadata 區塊，所以新語法天生免疫：

  語意反轉  「本頁解除待核實」「✅ 待查證結案」「狀態自待查證轉為 ✅ 已修復」
            ——把已收斂的成功案例算成未結負債，指標永遠不降，比漏抓更糟
  符號圖例  「…／⛔ 官方拒修 / ❓ 待查證。」
  計數標頭  「### 🛡️ 安全與隱私（5 條未修復、6 條待查證）」——一行代表 6 條
  目錄 anchor「[第 7 段](#7-…社群面待補)」——coding-workflow-guide 17 筆全是這類

另外「（推論）」314 筆是永久認識論標籤不是待辦，且會與懸置**同句共現**
（「皆推論，未經官方確認」），所以排除必須作用在 match 層而非行層——這也是本檔
一律以 `finditer` 逐 match 處理、不切行的原因（巨型儲存格一格 1200+ 字含 3–5 個
標記，行與儲存格都不是合法單位）。

本檔只用標準庫，無 I/O 副作用（除 `page_domain()` 讀檔），可安全 import。
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "wiki"

# ── 語法 regex（與 wiki-ingest-format.md 規格逐字對應）────────────────────

PENDING_RE = re.compile(
    r"(?P<sym>[❓🔎])[ 　]*"
    r"\*{2}(?P<kind>待查證|查無官方)\*{2}[ 　]*"
    r"（標[ ]?(?P<marked>\d{4}-\d{2}-\d{2})"
    r"｜查[ ]?(?P<probes>[^）｜]+)"
    r"(?:｜複[ ]?(?P<review>\d{4}-\d{2}-\d{2}))?"
    r"(?:｜訊[ ]?(?P<signal>\d{4}-\d{2}-\d{2}))?"
    r"）"
)

SHORT_RE = re.compile(
    r"(?P<sym>[❓🔎])[ 　]*(?P<kind>待查證|查無官方)[ 　]*⟨(?P<qid>Q-\d{2})⟩"
)

QDEF_RE = re.compile(
    r"^[ \t]*[-*][ ]+⟨(?P<qid>Q-\d{2})⟩[ ]+(?=[❓🔎])", re.MULTILINE
)

# 存量掃描用。**只有 audit 腳本可以用它做判定**——scan 與 check 一律只認新語法，
# 否則舊字樣的假陽性會流進每日流程。
#
# 刻意不含「待補」：它的語意是「資料不全、去補就好」，與「事實未確認、要等外部證據」
# 是兩種處置。而且它誤命中極高——coding-workflow-guide 的「社群面待補」目錄 anchor
# 就吃掉 17 筆。要追蹤資料缺口該用別的機制，不是混進懸置。
LEGACY_RE = re.compile(
    r"待查證|待核實|待確認|待驗證|存疑|未經官方確認|未證實|官方未載|單方指控|無官方證實"
)

PROBE_SPLIT_RE = re.compile(r"[、,，]")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)")

SYM_TO_KIND = {"❓": "待查證", "🔎": "查無官方"}

# ── 探針品質門檻（checker 據此 FAIL；規格見 format 規則「探針怎麼寫」）──────

PROBE_MIN_ASCII = 4
PROBE_MIN_CJK = 3

# 天天出現的詞當探針＝每日命中、把真訊號淹掉。原型實測 `Cowork` 一個詞就在 16 筆
# 命中裡貢獻 4 筆雜訊。
#
# 平台/來源名 `[加入: 2026-08-10]`：這些詞是來源固有標記（每則 Reddit/HN 條目
# 必帶），不是內容訊號——`Reddit`、`ClaudeCode`（subreddit 名）雖然長度過門檻，
# 天天出現的性質與模型名/專有名詞無異，同樣會把真訊號淹掉。
PROBE_STOPLIST = {
    "claude", "anthropic", "ai", "code", "api", "agent", "model",
    "opus", "sonnet", "haiku", "fable", "cowork", "claude code",
    "reddit", "github", "hacker news", "hackernews", "claudecode",
    "show hn", "dev.to", "devto", "lobsters", "google news",
}

# 單探針放行門檻（scanner 的「單一具偵測力探針可放行」與 checker 的「探針過短」
# WARN 共用此地板）。與 `probe_too_weak()` 的 PROBE_MIN_ASCII/CJK 不同——那是
# 「探針合不合法」的最低地板，這裡是「單獨一個探針夠不夠格自己扛命中」的更高地板。
PROBE_DETECTIVE_LEN_FLOOR = 6

DOMAIN_TO_REPORTER = {
    "🤖 模型": "wiki-reporter-models",
    "🛠️ 工具/功能": "wiki-reporter-features",
    "💼 商業": "wiki-reporter-commercial",
    "🏛️ 政策/安全": "wiki-reporter-safety-policy",
    "🌐 社群": "wiki-reporter-community",
    "👤 人物": "wiki-reporter-people",
}

# ── 分類線索（僅 audit 使用）──────────────────────────────────────────────

# 「解除」出現在標記之前（如「解除 08-08 媒體報導階段『未經官方確認』狀態」，
# 距離達 14 字元，故窗口開到 24）。
PRE_CUES = ("解除", "撤下", "移除", "不再")
PRE_WINDOW = 24
POST_CUES = (
    "已解除", "結案", "轉為", "收斂", "已確認", "已證實",
    "已修復", "已澄清", "經官方確認", "改為事實",
)
POST_WINDOW = 16

# 線索詞被否定時語意翻回來：「❓ 待查證（尚待官方受理，非已修復或拒絕）」是**真懸置**，
# 卻含「已修復」。首輪盤點實測誤殺 claude-code.md:129/130 兩筆。
NEG_PREFIXES = ("非", "不", "未", "無", "尚")
NEG_LOOKBACK = 2

FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
FENCE_RE = re.compile(r"^[ \t]*(```|~~~).*?^[ \t]*\1", re.DOTALL | re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
LINK_TARGET_RE = re.compile(r"\]\(([^)]*)\)")

# 「N 條待查證」是狀態計數摘要（一行代表 N 筆，元層級）；「12 條內容…，待查證原文補全」
# 的 12 條講的是內容數量，該筆是真懸置。差別在**標記是否緊接在「N 條」之後**——首輪
# 盤點用「括號內有 N 條」判定，誤殺了 community-tech-patterns 兩筆。
COUNT_PREFIX_RE = re.compile(r"\d+\s*條$")

# 圖例偵測：同一行列舉多個狀態符號。清單須涵蓋各頁自訂的採用度符號，否則
# community-tech-tools 的「✅ 廣泛採用 / ⚡ 小圈子使用 / ⏳ 觀望中 / ⚠️ 效果存疑」
# 會被誤判為已解除敘述。
STATUS_SYMS = ("🔴", "✅", "⛔", "❓", "🟡", "🔎", "⚡", "⏳", "⚠️", "❌", "🧪", "🔄")

# PRE 線索與標記之間隔著句讀，代表那個動詞的受詞是別的東西：
# 「移除逾 80% 系統提示詞，列為待查證傳聞」的「移除」講的是提示詞不是標記。
CLAUSE_BREAKS = "，,、。；;：:"


@dataclass
class Marker:
    """一筆新語法標記。"""
    sym: str
    kind: str
    marked: str
    probes_raw: str
    review: str | None
    signal: str | None
    start: int
    end: int
    line: int
    qid: str | None = None

    @property
    def probes(self) -> list[str]:
        return split_probes(self.probes_raw)


@dataclass
class LegacyHit:
    """一筆舊字樣命中（含分類結果）。"""
    word: str
    start: int
    end: int
    line: int
    cls: str = ""
    reason: str = ""
    shape: str = ""
    segment: str = ""
    in_table_cell: bool = False
    cell_len: int | None = None
    event_dates: list[str] = field(default_factory=list)
    wikilinks: list[str] = field(default_factory=list)


def split_probes(raw: str) -> list[str]:
    return [p.strip() for p in PROBE_SPLIT_RE.split(raw) if p.strip()]


def normalize_probe(text: str) -> str:
    """NFKC + casefold，讓全半形與大小寫差異不影響比對。"""
    return unicodedata.normalize("NFKC", text).casefold().strip()


def _stoplist_key(text: str) -> str:
    """比對 PROBE_STOPLIST 專用的正規化：連字號/底線視同空白。

    `wiki-ingest.claude-code` 展開出的 slug 別名是 `claude-code`（連字號），
    `normalize_probe()` 不動連字號，若直接比對會與 STOPLIST 的 `claude code`
    （空白）錯開，讓同一個詞換個寫法就繞過封鎖——這正是 2026-08-09 樞紐頁
    wikilink 誤放行事件的根因之一。
    """
    norm = normalize_probe(text)
    norm = re.sub(r"[-_]+", " ", norm)
    return re.sub(r"\s+", " ", norm).strip()


def probe_is_wikilink(probe: str) -> bool:
    return bool(WIKILINK_RE.match(probe.strip()))


def wikilink_target(probe: str) -> str | None:
    m = WIKILINK_RE.match(probe.strip())
    return m.group(1).strip() if m else None


def probe_too_weak(probe: str) -> str | None:
    """回傳違規理由，合格則 None。checker 據此 FAIL。"""
    if probe_is_wikilink(probe):
        return None
    norm = normalize_probe(probe)
    if not norm:
        return "空探針"
    if _stoplist_key(probe) in PROBE_STOPLIST:
        return f"「{probe}」屬過寬詞（天天出現，會把真訊號淹掉）"
    has_cjk = any("一" <= c <= "鿿" for c in norm)
    if has_cjk:
        if len(norm) < PROBE_MIN_CJK:
            return f"「{probe}」中文探針需 ≥ {PROBE_MIN_CJK} 字元"
    elif len(norm) < PROBE_MIN_ASCII:
        return f"「{probe}」英數探針需 ≥ {PROBE_MIN_ASCII} 字元"
    return None


def wikilink_aliases(target: str, wiki_dir: Path | None = None) -> list[str]:
    """wikilink 探針展開的別名：slug 末段 + 目標頁 H1 標題文字。

    讀不到目標頁（不存在或非 utf-8）時只回傳 slug 末段。scanner／checker 共用
    此函式，確保兩邊對「這個 wikilink 展開成什麼」永遠是同一份答案。
    """
    wiki_dir = wiki_dir or WIKI_DIR
    aliases = [target.rstrip("/").split("/")[-1]]
    path = wiki_dir / f"{target}.md"
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError:
        return aliases
    m = re.search(r"^#\s+(.+)\s*$", text, re.MULTILINE)
    if m:
        aliases.append(m.group(1).strip())
    return aliases


def detective_aliases(probe: str, wiki_dir: Path | None = None) -> list[str]:
    """回傳這個探針實際具偵測力的別名集合；空集合＝這個探針偵測不到任何東西。

    scanner（比對日報）與 checker（判定探針組是否合格）共用此函式，讓兩邊對
    「這個探針到底偵測得到什麼」永遠是同一份答案——這是 2026-08-09 事件的
    核心修復：舊版 scanner 對 wikilink 展開別名後沒有複檢 STOPLIST，導致
    `[[entities/claude-code]]` 這類樞紐頁連結展開出「claude-code」「Claude Code」
    後，後者精準落在 STOPLIST 卻仍被拿去比對，任何標題含「Claude Code」的條目
    都命中，且 wikilink 探針享有單探針放行特權，等於一根萬用鑰匙。

    注意這裡判斷的是「這個探針能不能參與 AND 比對」，用的是 `probe_too_weak()`
    的合法門檻（ASCII ≥4／CJK ≥3 + 不落在 STOPLIST）——不是 scanner 另外用的
    「單一探針能不能自己扛命中」的更高地板（`PROBE_DETECTIVE_LEN_FLOOR`／
    `SINGLE_PROBE_LEN_FLOOR` = 6）。兩者是不同問題：一個 4 字元的合法探針
    （如「出口管制」）仍能貢獻一次 AND 命中，只是不能單獨扛命中。

      - **plain 探針**：`probe_too_weak(probe)` 合格才回傳 `[normalize_probe(probe)]`；
        否則回傳 `[]`。
      - **wikilink 探針**：展開為「slug 末段 + 目標頁 H1」，逐一剔除落在
        STOPLIST 的別名（比對走 `_stoplist_key()`，連字號視同空白），回傳
        剩餘別名；全數落在 STOPLIST（樞紐頁的典型情況）則回傳 `[]`。
    """
    if probe_is_wikilink(probe):
        target = wikilink_target(probe)
        if not target:
            return []
        aliases = wikilink_aliases(target, wiki_dir)
        return [a for a in aliases if _stoplist_key(a) not in PROBE_STOPLIST]
    return [] if probe_too_weak(probe) else [normalize_probe(probe)]


class Doc:
    """一份 markdown 的預算結構，讓逐 match 分類不必每次重掃全文。"""

    def __init__(self, text: str, path: Path | None = None):
        self.text = text
        self.path = path
        self.body_offset = 0
        m = FRONTMATTER_RE.match(text)
        if m:
            self.body_offset = m.end()
        self._line_starts = [0] + [i + 1 for i, c in enumerate(text) if c == "\n"]
        self._skip_spans = [mm.span() for mm in FENCE_RE.finditer(text)]
        self._skip_spans += [mm.span() for mm in INLINE_CODE_RE.finditer(text)]
        self._link_spans = [mm.span(1) for mm in LINK_TARGET_RE.finditer(text)]

    def line_of(self, pos: int) -> int:
        lo, hi = 0, len(self._line_starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self._line_starts[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1

    def line_text(self, pos: int) -> str:
        start = self.text.rfind("\n", 0, pos) + 1
        end = self.text.find("\n", pos)
        return self.text[start: end if end != -1 else len(self.text)]

    def in_code(self, pos: int) -> bool:
        return any(a <= pos < b for a, b in self._skip_spans)

    def in_link_target(self, pos: int) -> bool:
        return any(a <= pos < b for a, b in self._link_spans)

    def in_frontmatter(self, pos: int) -> bool:
        return pos < self.body_offset

    def table_cell(self, pos: int) -> str | None:
        """回傳 match 所在的表格儲存格內容；不在表格內則 None。"""
        line = self.line_text(pos)
        if not line.lstrip().startswith("|"):
            return None
        line_start = self.text.rfind("\n", 0, pos) + 1
        rel = pos - line_start
        bounds = [i for i, c in enumerate(line) if c == "|"]
        for a, b in zip(bounds, bounds[1:]):
            if a < rel < b:
                return line[a + 1: b]
        return line

    def segment(self, pos: int, span: int = 60) -> str:
        """取 match 前後最近的斷句符號之間那段，供語意分類與人工過目。"""
        breaks = "。；｜|\n"
        lo = pos
        while lo > 0 and pos - lo < span and self.text[lo - 1] not in breaks:
            lo -= 1
        hi = pos
        while hi < len(self.text) and hi - pos < span and self.text[hi] not in breaks:
            hi += 1
        return self.text[lo:hi].strip()


def iter_pending(text: str, path: Path | None = None) -> list[Marker]:
    """解析新語法標記（含表格細節區的 ⟨Q-nn⟩ 定義）。"""
    doc = Doc(text, path)
    out: list[Marker] = []
    for m in PENDING_RE.finditer(text):
        if doc.in_code(m.start()) or doc.in_frontmatter(m.start()):
            continue
        line_start = text.rfind("\n", 0, m.start()) + 1
        prefix = text[line_start:m.start()]
        qm = re.search(r"⟨(Q-\d{2})⟩", prefix)
        out.append(Marker(
            sym=m.group("sym"), kind=m.group("kind"), marked=m.group("marked"),
            probes_raw=m.group("probes"), review=m.group("review"),
            signal=m.group("signal"), start=m.start(), end=m.end(),
            line=doc.line_of(m.start()), qid=qm.group(1) if qm else None,
        ))
    return out


def _negated(text: str, cue_pos: int) -> bool:
    return any(n in text[max(0, cue_pos - NEG_LOOKBACK):cue_pos] for n in NEG_PREFIXES)


def _classify(doc: Doc, m: re.Match) -> tuple[str, str]:
    pos = m.start()
    line = doc.line_text(pos)

    # ── M 元層級：純結構判斷，不猜語意，可靠度最高 ──
    if doc.in_link_target(pos):
        return "M", "目錄 anchor"
    if doc.in_code(pos):
        return "M", "code span"
    if doc.in_frontmatter(pos):
        return "M", "frontmatter"
    # 標記緊接在「N 條」之後 → 狀態計數摘要（一行代表 N 筆）。
    # **不可因為身在標頭就判元層級**：小節標題裡的「（2026-07-28 新增，待查證）」
    # 是真懸置，首輪盤點誤殺了 ai-agent-safety 5 筆與 feature-radar 1 筆。
    line_start = doc.text.rfind("\n", 0, pos) + 1
    if COUNT_PREFIX_RE.search(line[: pos - line_start]):
        return "M", "狀態計數摘要"
    if "狀態標記" in line or "每條開頭" in line:
        return "M", "符號圖例"
    if sum(1 for s in STATUS_SYMS if s in line) >= 3:
        return "M", "符號圖例（多狀態符號同行）"

    seg = doc.segment(pos)
    word = m.group(0)
    idx = seg.find(word)
    before = seg[max(0, idx - PRE_WINDOW):idx] if idx >= 0 else ""
    after = seg[idx + len(word): idx + len(word) + POST_WINDOW] if idx >= 0 else ""

    # ── R 已解除敘述：唯一需要語意猜測的一類，故輸出一律附原文供人工過目 ──
    for cue in PRE_CUES:
        i = before.find(cue)
        if i == -1 or _negated(before, i):
            continue
        # 中間隔著句讀 → 該動詞的受詞不是這個標記
        if any(b in before[i + len(cue):] for b in CLAUSE_BREAKS):
            continue
        return "R", f"PRE「{cue}」"
    for cue in POST_CUES:
        i = after.find(cue)
        if i != -1 and not _negated(after, i):
            return "R", f"POST「{cue}」"
    if "✅" in seg and "已" in seg:
        return "R", "✅ 且鄰近「已」"

    # ── U 偵測不了：交人工，不硬猜 ──
    cell = doc.table_cell(pos)
    if cell is not None:
        if len(cell) > 400 and len(LEGACY_RE.findall(cell)) >= 3:
            return "U", f"巨型儲存格（{len(cell)} 字元，含多筆）"
        if not re.search(r"\d{4}-\d{2}-\d{2}", line) and not WIKILINK_RE.search(line):
            return "U", "表格列無日期且無 wikilink，無從推探針"
    if len(seg) < 12:
        return "U", f"脈絡過短（{len(seg)} 字元）"

    return "P", ""


def _shape(doc: Doc, pos: int) -> str:
    line = doc.line_text(pos)
    stripped = line.lstrip()
    if stripped.startswith("|"):
        return "table"
    if stripped.startswith(">"):
        return "callout"
    if re.match(r"^[-*]\s", stripped):
        return "list"
    if re.match(r"^#{1,6}\s", stripped):
        return "heading"
    return "prose"


def iter_legacy(text: str, path: Path | None = None) -> list[LegacyHit]:
    """掃描舊字樣並分類。已是新語法者不重複計入。"""
    doc = Doc(text, path)
    new_spans = [(mk.start, mk.end) for mk in iter_pending(text, path)]
    new_spans += [
        mm.span() for mm in SHORT_RE.finditer(text)
        if not doc.in_code(mm.start()) and not doc.in_frontmatter(mm.start())
    ]
    out: list[LegacyHit] = []
    for m in LEGACY_RE.finditer(text):
        if any(a <= m.start() < b for a, b in new_spans):
            continue
        cls, reason = _classify(doc, m)
        seg = doc.segment(m.start())
        cell = doc.table_cell(m.start())
        line = doc.line_text(m.start())
        out.append(LegacyHit(
            word=m.group(0), start=m.start(), end=m.end(),
            line=doc.line_of(m.start()), cls=cls, reason=reason,
            shape=_shape(doc, m.start()), segment=seg,
            in_table_cell=cell is not None,
            cell_len=len(cell) if cell is not None else None,
            event_dates=re.findall(r"\d{4}-\d{2}-\d{2}", line),
            wikilinks=WIKILINK_RE.findall(line),
        ))
    return out


def page_domain(path: Path) -> str | None:
    """三段 fallback 取領域：frontmatter → 正文粗體標頭 → None。"""
    try:
        text = path.read_text(encoding="utf-8-sig")
    except Exception:
        return None
    m = re.search(r'^domain:\s*"?([^"\n]+)"?\s*$', text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^\*\*領域[：:]\*\*\s*(.+?)\s*$", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def reporter_of(path: Path) -> str | None:
    domain = page_domain(path)
    return DOMAIN_TO_REPORTER.get(domain) if domain else None


def page_slug(path: Path) -> str:
    try:
        return path.relative_to(WIKI_DIR).as_posix()[:-3]
    except ValueError:
        return path.stem


def wiki_pages(wiki_dir: Path | None = None) -> list[Path]:
    """掃描對象：wiki 的內容頁。

    排除四類非內容檔——它們含「待查證」字樣但都不是待辦：
      log.md      歷史流水帳，一旦寫入就不再改
      CLAUDE.md   規則檔（「收留…未收錄決策、品質備註、待確認事項」是規則本文）
      *-archive-* 已歸檔的歷史快照
      _views/     Obsidian dataview 視圖，不存資料
    """
    base = wiki_dir or WIKI_DIR
    return [
        p for p in sorted(base.rglob("*.md"))
        if p.name not in ("log.md", "CLAUDE.md")
        and "-archive-" not in p.name
        and "_views" not in p.parts
    ]
