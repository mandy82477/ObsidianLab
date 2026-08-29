# CLAUDE.md

---

## 專案目標

每日聚焦 Claude Code 與 Anthropic 核心動態，從官方更新到社群實測，一站掌握技術情報。所有條目經 LLM 評分過濾、繁中摘要、再沉澱進 wiki。

### 目標讀者

- **Claude Code 重度使用者**：想第一時間知道有什麼壞了、值不值得升版，不用自己刷 HN。
- **AI 系統開發者**：在建 agent 或工作流，想知道社群驗證了什麼、踩過哪些坑。
- **Anthropic 生態追蹤者**：關注政策、融資、合作動態，一站掌握生態走向。

### 蒐集範圍

| 類型 | 內容 |
|------|------|
| **官方核心** | GitHub Changelog、SDK / API 迭代、定價結構變化、Anthropic 公告 |
| **社群實測** | 工程師驗證過的工作流模式、agent 設計、Bug 回報與替代方案（HN / Reddit） |
| **生態動態** | 融資、大型企業合作（AWS / Google）、政策趨勢、周邊工具 |
| **專頁定向** | 為特定 wiki 專頁定向抓取的少量條目（`src/news_aggregator/sources/topic_watch.json`），判準是「對該專頁有無價值」而非標題是否提及 Claude／Anthropic |
| **存量盤點** | 已成名但本庫從未報導過的 GitHub repo，每日至多 2 則補進（`src/news_aggregator/sources/github_releases.py` C 窗）。含 Agent Skills 生態——SKILL.md 是 Anthropic originated 的格式，該生態整體屬 Claude 生態，但多數 repo 的描述不含 claude 字樣 |

### 不收錄

- X / Discord 即時訊號（社交平台秒級爆料；26–30 小時延遲是設計取捨，非缺陷）
- NDA 保護下的企業非公開資訊
- 與 Claude / Anthropic 無直接關聯的通用 AI 新聞（**例外**：wiki 專頁定向抓取，見上表「專頁定向」——該通道有數量上限且在日報獨立成區，不混入正文六區塊）
- Agent Skills 生態以外、與 Claude 無關的 agent 工具存量（存量盤點通道綁定四條 scope，不是通用 GitHub 熱門榜；scope 清單見 `src/news_aggregator/sources/github_releases.py` 的 `_INVENTORY_SCOPES`）
- 無技術內容的純行銷稿

**新增 source 或 command 時的判斷標準：**
> 這份資料能幫助**需要深度與穩定資訊的工程師**更了解 Claude / Anthropic 生態系嗎？若否，不收錄。

### Web Reader 目的

- **自用**：在瀏覽器閱讀日報與 wiki，不需開啟 Obsidian 或看 raw Markdown
- **分享**：部署後可將連結分享給他人，無需安裝任何工具即可瀏覽

---

## 專案架構

兩個獨立部分：

1. **`src/news_aggregator/`** — Python 爬蟲，每日抓取 Claude / Anthropic 新聞 → `news/YYYY-MM-DD.md`
   Pipeline：`sources/*.py → dedup.py → enricher.py → filter.py → analyzer.py → digest.py → git_push.py`
   新增來源：繼承 `BaseSource`，實作 `fetch() -> list[FeedItem]`，在 `main.py` 的 `sources` 列表加入即可。

2. **`wiki/`** — LLM 維護的知識庫，從日報萃取並整理為結構化頁面
   規則：`wiki/CLAUDE.md`（進入 wiki/ 自動載入）+ `.claude/rules/wiki-ingest.md`（ingest / lint 時載入）

執行日誌：`src/logs/` | 完整模組說明：`src/DesignDocument/`

---

## 環境限制（開發前必讀）

**此專案沒有 `ANTHROPIC_API_KEY`，開發時不得假設其存在。**

### 🚫 開發禁止使用 `claude -p`

**`claude -p` 完全禁止**，任何情境一律不得出現：

- Skills / Commands 中嚴禁出現 `claude -p`（含子程序呼叫、shell 執行、間接觸發）
- Skills / Commands 呼叫的 Python script，呼叫鏈中也不得觸發 `claude -p`
- 不可新增任何「有 API key 才能運作」的功能或 fallback

**合法的 LLM 呼叫路徑：**
1. Claude session 直接執行 — skills / commands 的唯一合法路徑

**新增功能或修改 pipeline 時的判斷標準：**
> 這個改動，在完全沒有 `ANTHROPIC_API_KEY` 的環境下也能正確運作嗎？若否，重新設計。

---

## 完工定義（Definition of Done）

**改動未閉迴路不算完成。** 實質改動（pipeline / 規則 / wiki / 腳本）的完工定義三者到齊：

1. **測試綠**：`python scripts/run_tests.py` 通過
2. **已 commit**：非 data 檔的改動已進 git（data 檔如 `gathered_items.json` / `emitted_items.json` / `seen_urls.json` 例外，不需為它們 commit）。**commit 必須指名路徑，任何情境一律不得 `git add -A` / `git add .`**——見下方「commit 範圍」
3. **依賴缺口已登記**：若改動依賴尚缺的憑證/服務/真解（而非真正解決），在 `docs/workaround-register.md` 登記 owner + 複查日，不可只留在對話裡

三者缺一，任務標「進行中」，不標「完成」。

> 判斷：這個改動的迴路閉了嗎？測試、commit、依賴缺口登記三者到齊了嗎？缺一 → 還沒完成。

### commit 範圍：只 add 你這次真的改了的路徑 `[加入: 2026-08-29]`

**任何 session、任何情境，一律不得 `git add -A` / `git add .`**，一律指名路徑（如 `git add wiki/ .claude/rules/`）。commit 訊息只描述你這次做的事——**訊息裡沒提到的檔案，就不該在這個 commit 裡**。

> 本條原本只寫在 `.claude/commands/news-pipeline-steps.md`「絕不要在補跑流程裡用 `git add -A`」，射程只到補跑流程；**臨時修復工作不在射程內**，於是 2026-08-29 出事：一個訊息為「fix: 目標日期取自耐久的 gathered_archive」的 commit，掃走了同時間另一份工作中的 `wiki/entities/pricing.md`（+43）、`wiki/topics/model-comparison.md`（+30）、`code-quality-decline.md`、`log.md`（+39）。
>
> 兩層傷害：(a) **commit 了半成品**——那批 wiki 改動當時尚未修完錨點、規則也還沒移到 lint 檔；(b) **殺掉可追溯性**——本專案的品質系統整個建立在「為什麼加這條」查得到（`log.md` 的 Query 條目、`[加入: YYYY-MM-DD]` 標記、幾乎每條規則都寫著「教訓來自 X 月 Y 日」），而這些考古全靠 `git log` / `git blame`。訊息錯置的 commit 會讓那條路斷掉，且**事後補不回來**。

**判斷式：** 這個 commit 的訊息，說得出裡面每一個檔案為什麼在嗎？說不出 → 你 add 太多了。

**開放迴路掃描：** 每週跑 `python scripts/open_loops.py`（列出未 commit 的實質改動、逾複查日的 workaround）；日常則由 SessionStart hook 在開啟專案時提醒未 commit 的實質改動。

---

## Skills

| 指令 | 用途 | 何時執行 | 詳細規格 |
|------|------|---------|---------|
| `/news-pipeline` | 完整 pipeline：抓新聞 → 生成日報 → wiki ingest → 建置 web → 全部 push | 🟢 每天（平常只跑這個；已含 `/wiki-ingest`）| `.claude/commands/news-pipeline.md` |
| `/wiki-ingest` | 讀取日報，更新 wiki entities / topics / feature-radar | 通常不單獨跑（pipeline 沒跑完、只想補 wiki 那段時）| `.claude/commands/wiki-ingest.md` |
| `/wiki-backfill` | 補跑一或多個過去日期的 wiki ingest，適用於排程失敗或日報重新抓取後 | 按需（排程失敗／日報重抓後）| `.claude/commands/wiki-backfill.md` |
| `/wiki-lint` | 每週品質檢查：矛盾頁面、孤立頁面、過期議題、規則檔健檢 | 🟡 每週 | `.claude/commands/wiki-lint.md` |
| `/wiki-weekly-review` | 每週判斷值得加碼追蹤的主題（建頁/加開子區塊/升熱度），經確認後執行 | 🟡 每週（每月首次含聚焦校準 30 天回看）| `.claude/commands/wiki-weekly-review.md` |
| `/weekly` | **每週總指揮**：依序跑 `/weekly-report`（對外交付）與 `/wiki-weekly-review`（對內策展），最後統一收尾單一 push | 🟡 每週（平常只跑這個；已含另兩者）| `.claude/commands/weekly.md` |
| `/weekly-report` | 產生本週深度週報（頭條敘事＋技術討論深挖＋下週看什麼＋檔尾數字），輸出 `weekly/YYYY-Wnn.md` | 通常不單獨跑（補跑或修正單一期週報時）| `.claude/commands/weekly-report.md` |
| `/wiki-readability` | 低成本可讀性掃描：單一 agent 取樣每頁開頭與結構，回報後經確認修復 | 按需 | `.claude/commands/wiki-readability.md` |
| `/pipeline-change-check` | 改版前後品質對照：baseline 記錄基線、compare 對照差異＋舊資料回歸 | 改 pipeline／日報格式／收錄門檻**前後**各一次 | `.claude/commands/pipeline-change-check.md` |
| `/review-commands` | 修改 commands/rules/CLAUDE.md 後強制執行，確認所有指令仍可正確運作 | 改完 commands/rules/CLAUDE.md **後** | `.claude/commands/review-commands.md` |

**新增 skill 時的判斷標準：**
> 這個任務是否需要跨多個步驟、值得重複執行，且有明確的輸入與完成條件？若否，用對話即可，不需要新 skill。

---

## Wiki 規則入口

- **`wiki/CLAUDE.md`**（進入 wiki/ 自動載入）：目錄結構、基本限制、搜尋策略
- **`.claude/rules/wiki-ingest.md`**（ingest / lint 時載入）：分類標準與派工流程（主編指南）
- **`.claude/rules/wiki-ingest-format.md`**（建立新頁面時載入）：頁面格式模板、欄位規則、品質標準
- **`.claude/rules/wiki-ingest-[category].md`**（各記者載入）：模型 / 功能 / 商業 / 安全政策 / 社群 / 人物 各類別的負責頁面與更新規則

### 🚫 Wiki 關鍵限制

- Wiki 檔案只能建立或修改在 `CLAUDE_NEWS/wiki/`，**不可**誤存至父層 `ObsidianLab/` 目錄
- `news/` 為唯讀原始資料，不可修改
- `log.md` 只能 append，不可修改既有條目
- 繁體中文為主；英文術語保留英文

**新增 wiki 頁面時的判斷標準：**
> 這個主題已有足夠的具體資訊（名稱 + 狀態 + 至少一個事件）嗎？若今日首見，先附記在相關頁面的歷史記錄，明天再評估是否建頁。

### 🔗 連結與嵌入語法

wiki 正文的連結寫法以 web reader 解析器（`web_reader/assets/app.js` 的 `parseWikilink()`）吃得下的為準——下表以外的 Obsidian 語法在 Obsidian 正常、在網站上壞掉，一律不得寫入 `wiki/`：

| 語法 | 用途 | 判斷 |
|------|------|------|
| `[[entities/x]]`、`[[topics/x]]` | 內部連結（含目錄前綴）| ✅ 預設寫法；網站自動顯示中文頁名，**不必為了好看手寫別名** |
| `[[feature-radar]]`、`[[news/YYYY-MM-DD]]` | 根頁面、日報連結 | ✅ |
| `[[頁面\|別名]]` | 別名顯示 | ✅ 只在句子需要特定措辭時用（如「取代 [[entities/opus-4-8\|Opus 4.8]] 成為次旗艦」）|
| `[[頁面#標題]]`、`[[#本頁標題]]` | 跳到該頁某段 | ✅ 錨點須為目標頁的 **h2–h4 標題原文**；建置的 `check_wikilink_anchors()` 會驗，打錯或標題改名會 WARN |
| `![[頁面]]`、`![[圖片.png\|300]]` | 嵌入 / 轉引 | ❌ 網站無嵌入渲染，原樣輸出 `![[...]]` |
| `[[頁面#^區塊id]]`、段落尾 `^區塊id` | 區塊引用 | ❌ 同上，解析器不支援 |

指向長頁面的特定段落時**優先用錨點**（`詳見 [[topics/model-comparison#快速選型表]]`），不要只寫頁名讓讀者自己在數百行裡找。

> 要改用嵌入或區塊 id → 先擴充 `parseWikilink()` / `wikilinkButtonHtml()` 與 `scripts/build_web.py` 的 `check_wikilinks()`，不可只改 wiki 內文。

### ✏️ 修改 rules 或 commands 時的注意事項

**修改任何 `CLAUDE.md`、`.claude/commands/`、`.claude/rules/` 中的檔案後，必須確保所有相關指令仍可正確執行，執行 `/review-commands` 直到零錯誤為止。**

規則一致性的機械檢查（裸露引用、路徑存在性、錨點、同步配對）已納入測試套件（`scripts/check_rules.py`，掛在 `python scripts/run_tests.py` 內一併執行）；`/review-commands` 只負責判讀失敗並修復。

詳細規則（路徑引用原則、反向查詢、設計原則、長度控制）：**`.claude/rules/claude-md-edit.md`**（修改前必須讀取此檔）
