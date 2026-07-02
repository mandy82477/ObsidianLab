---
description: 每週執行 wiki 品質檢查，修正矛盾/孤立/過期頁面，更新 overview。
---

# Wiki Lint

每週執行，檢查 wiki 品質並修正問題。建議在週末或週一執行。

## 步驟

### 1. 載入 wiki 全貌

同時讀取：
- `wiki/CLAUDE.md` — wiki 目錄結構與基本限制
- `.claude/rules/wiki-ingest.md` — 分類標準與派工流程（主編指南）
- `.claude/rules/wiki-ingest-format.md` — 頁面格式模板、欄位規則、品質標準
- `wiki/index.md` — 取得所有頁面清單
- `wiki/log.md` — 了解最近的 ingest 紀錄與活動

### 2. 並行派工（六位記者同時執行）

對每個類別呼叫 Agent tool，在**同一訊息中並行發出全部六個呼叫**。

| 類別 | subagent_type | 負責頁面範圍 |
|------|--------------|------------|
| 模型 | `wiki-reporter-models` | `wiki/entities/fable-5.md`, `opus-4-8.md`, `opus-4-7.md`, `mythos.md`, `pricing.md` |
| 功能 | `wiki-reporter-features` | `wiki/entities/claude-code.md`, `bugcrawl.md`, `managed-agents.md`, `openclaw.md`, `claude-design.md`, `claude-security.md`, `wiki/topics/official-community-gap.md`, `wiki/feature-radar.md` |
| 商業 | `wiki-reporter-commercial` | `wiki/topics/anthropic-business.md`, `enterprise-tool-tracker.md`, `enterprise-cost-management.md`, `competitor-landscape.md`, `wiki/entities/pricing.md` |
| 安全政策 | `wiki-reporter-safety-policy` | `wiki/topics/anthropic-government-policy.md`, `ai-agent-safety.md`, `recursive-self-improvement.md` |
| 社群 | `wiki-reporter-community` | `wiki/topics/community-tech-tools.md`, `community-tech-patterns.md`, `community-tech-discussions.md`, `community-tech-timeline.md`, `code-quality-decline.md` |
| 人物 | `wiki-reporter-people` | `wiki/entities/boris-cherny.md`, `cat-wu.md`, `andrej-karpathy.md`, `dario-amodei.md`, `chris-olah.md` 及其他人物頁 |

> **社群記者額外任務：** `community-tech-tools.md` 已脫離每日 ingest，是 **lint 專用策展頁**。除 3a–3f 品質檢查外，須額外依 `.claude/rules/wiki-ingest-community-lint.md` 的「策展規則」與「精選層提拔規則」執行：讀取近 7–14 天 `news/*.md` 萃取達標新工具、汰除過氣條目、提拔精選層、同步痛點洞察。派工 prompt 須附上「今日日期」供記者計算 news/ 範圍。

每個 Agent 呼叫的 prompt：

```
今日日期：[YYYY-MM-DD]
任務：對你負責的頁面執行 wiki lint 檢查並修正問題。

讀取 `.claude/rules/wiki-ingest-format.md`，然後對每個頁面依序執行：

**3a 矛盾偵測**
同一事件的描述若與其他已知頁面矛盾（日期不同、結論相反）→ 以日報原文為準修正，兩頁互加 wikilink。

**3b 孤立頁面**
用 Grep 搜尋此頁面 slug 是否在 wiki/ 目錄其他檔案中有 wikilink 引用。
若完全孤立（無任何頁面以 `[[...]]` 連結到它）→ 在語意相關的頁面補上 wikilink。

**3c 過期議題**
topics/ 頁面狀態為 `ongoing`，且「最後更新」距今超過 14 天，且 log.md 近期無相關更新。
→ 議題確已結束：狀態改 `resolved`，填寫「目前結論」
→ 仍在進行但無新消息：狀態改 `monitoring`

**3d 已解決議題遷移**
topics/ 狀態為 `resolved` → 移動至 `wiki/entities/`（類型標 `event`），更新內容，並在原 topics/ 路徑留一行重定向提示。

**3e 呈現品質審查**
依 `.claude/rules/wiki-ingest-format.md`「Wiki 頁面呈現品質標準」掃描：
必須修復：摘要可獨立閱讀、關鍵資訊前置、無 LLM 專屬指令
警示觸發：頁面 > 200 行、連續 8+ 個無分組日期條目、方案比較未用表格

**3f 超長頁面回報（> 500 行）**
自行分析：內容性質分佈、建議拆分邊界與新頁面命名。
**不自行拆分**——將分析結果回報給主 session，由主 session 詢問使用者確認。

完成後依標準格式回報。
```

記者回報格式（標準化）：

```
## [類別] Lint 回報
修正矛盾：[list or 無]
補孤立連結：[list or 無]
狀態更新：[page: ongoing→monitoring/resolved or 無]
遷移至 entities：[list or 無]
呈現品質：[每頁 ✅/⚠️已修復/📋待辦]
超長頁面（> 500 行）：[頁面名稱 + 行數 + 建議方案 or 無]
index.md 狀態變更：[page: 舊狀態→新狀態 or 無]
```

### 3. 處理超長頁面（需使用者確認）

收齊所有記者回報後，彙整 3f 的超長頁面清單。若有任何頁面需拆分，以下列格式呈現並**等待使用者確認**：

```
📄 [頁面名稱]（XXX 行）需要拆分評估

記者分析：
- 內容 A（約 XX 行）：[描述]
- 內容 B（約 XX 行）：[描述]

建議方案：
- [新頁面 A]：entities/xxx.md 或 topics/xxx.md
- [新頁面 B]：entities/yyy.md 或 topics/yyy.md

❓ 請確認：是否同意拆分？分類是否正確？命名是否OK？
```

根據使用者回應執行拆分或記錄為待辦。

### 4. 建議並建立新實體頁

掃描所有頁面（可用 Grep），找出被提及 3 次以上但尚無專頁的名稱（模型、功能、人物、產品）。
→ 建立對應的 entities/ 頁面，填入目前已知資訊。
→ 在來源頁面補上 wikilink。

### 5. 更新 wiki/overview.md

重寫 `wiki/overview.md` 的內容，反映當前局勢：
- 目前最活躍的議題（ongoing topics）
- 近兩週的重大事件摘要
- 值得持續關注的趨勢

### 6. CLAUDE.md 健檢

讀取 `wiki/CLAUDE.md`、`.claude/rules/wiki-ingest.md`、`.claude/rules/wiki-ingest-format.md`（已在 Step 1 載入，可直接檢查），依序執行五項檢查：

#### 6a. 規則矛盾偵測

逐段掃描，找出同一行為在不同章節有相反指示、同一情境觸發條件衝突、新舊規則語意重疊或互相否定。

→ 輸出：
```
⚠️ 矛盾：[規則 A 位置] vs [規則 B 位置]
  A 說：「…」
  B 說：「…」
  建議：保留 [A/B]，理由：…
```
→ **向使用者確認後再修改**，不自行決定保留哪條規則。

#### 6b. 規則引用驗證

逐一 grep 以下錨點，確認仍存在於對應檔案中：

| 規則描述中的引用 | 應存在於 | 驗證方式 |
|---------------|---------|---------|
| `首次出現` 欄 | `topics/community-tech-tools.md` | grep `\| 首次出現 \|` |
| `## 痛點洞察` 區塊 | `topics/community-tech-tools.md` | grep `## 痛點洞察` |
| `近期工具` 欄 | `topics/community-tech-tools.md` | grep `近期工具` |
| `## 技術彙整` 區塊 | `topics/community-tech-discussions.md` | grep `## 技術彙整` |
| `熱門討論` 表格 | `topics/community-tech-discussions.md` | grep `熱門討論` |
| `衍生` 欄 | `topics/community-tech-discussions.md` | grep `衍生` |
| `全覽表` 區塊 | `wiki/feature-radar.md` | grep `全覽表` |

輸出：
```
📎 引用驗證：
  ✅ `首次出現` 欄確認存在
  ⚠️ `XXX` 未找到 → 規則可能過時
```
→ 發現 ⚠️ 時向使用者說明，**不自行刪除規則**。

#### 6c. 規則遵守率抽樣

讀取 `wiki/log.md` 最近 3 筆 Ingest 條目，對照：

| 規則 | 合格標準 |
|------|---------|
| 每次 ingest 執行呈現品質審查 | log 含 ✅/⚠️/📋 標記，3/3 |
| 每次 ingest 更新 feature-radar.md | log 提及 feature-radar，3/3 |
| 新工具加入時更新痛點洞察近期工具欄 | 出現工具的 ingest 須提及 |
| log.md 格式正確（來源日報、更新頁面、摘要欄位） | 3/3 |

輸出：
```
🔍 遵守率抽樣（近 3 次 ingest）：
  ✅ 呈現品質審查 — 3/3
  ⚠️ 近期工具更新 — 1/3
```
→ 遵守率 < 2/3 的規則：說明原因，**向使用者確認是否調整規則**。

#### 6d. 規則年齡審查

`.claude/rules/wiki-ingest-format.md` 及各記者規則檔（`wiki-ingest-*.md`）中帶有 `[加入: YYYY-MM-DD]` 標記的 `##` 區塊，計算距今天數。

- **距今 > 60 天**：逐一確認規則描述的行為是否仍與現狀吻合
- **距今 ≤ 60 天**：記錄「在閾值內，無需審查」

輸出：
```
📅 規則年齡審查（今日 YYYY-MM-DD，閾值 60 天）：
  ⚠️ [規則名稱] [加入: YYYY-MM-DD]（距今 XX 天）→ 確認格式仍正確
  ✅ [規則名稱]（距今 XX 天）→ 在閾值內
```
→ ⚠️ 規則列出後**向使用者確認是否需要修訂**，不自行修改。

#### 6e. 長度與簡化評估

分別統計 `wiki/CLAUDE.md`、`.claude/rules/wiki-ingest.md`、`.claude/rules/wiki-ingest-format.md` 及各記者規則檔（`wiki-ingest-*.md`）總行數。

- **`wiki/CLAUDE.md` 若超過 80 行**：提出簡化建議
- **`.claude/rules/wiki-ingest.md` 若超過 80 行**：提出簡化建議（主編指南應保持精簡）
- **`.claude/rules/wiki-ingest-format.md` 若超過 200 行**：提出簡化建議
- **各記者規則檔若超過 100 行**：提出簡化建議

輸出：
```
📋 規則檔健檢：
  wiki/CLAUDE.md：XX 行（閾值 80 行）→ ✅ / ⚠️
  .claude/rules/wiki-ingest.md：XX 行（閾值 80 行）→ ✅ / ⚠️
  .claude/rules/wiki-ingest-format.md：XX 行（閾值 200 行）→ ✅ / ⚠️
  .claude/rules/wiki-ingest-[category].md：各 XX 行（閾值 100 行）→ ✅ / ⚠️
❓ 是否執行簡化？（是 / 否 / 指定段落）
```

### 7. 讀者模擬驗收 `[加入: 2026-07-02]`

站在三種目標讀者（根目錄 `CLAUDE.md`「目標讀者」）的角度各出一題**本週真實會問的問題**（從近 7 天日報事件取材），模擬讀者從 `wiki/index.md` 出發：

| 讀者 | 問題類型範例 |
|------|------------|
| Claude Code 重度使用者 | 「現在該不該升版？」「X 功能壞了嗎？」 |
| AI 系統開發者 | 「Y 模式社群驗證結果如何？」「Z 的替代方案是什麼？」 |
| Anthropic 生態追蹤者 | 「W 政策事件現在進展到哪？」 |

**驗收標準：** 從 index.md 出發，**3 跳內**（index → 頁面 → 區塊）能否得到答案。

- ✅ 3 跳內找到 → 通過
- ⚠️ 找得到但超過 3 跳或散在多頁 → 修復：在最相關頁面補 callout / wikilink，或補 index.md 摘要欄
- ❌ 找不到 → 記錄至 log.md 待辦，回報使用者是否為結構性缺口

### 8. 記錄本次 lint

在 `wiki/log.md` 末尾 append：

```
## YYYY-MM-DD Lint

- 修正矛盾：（列出，若無則寫「無」）
- 補連結：（列出孤立頁面，若無則寫「無」）
- 狀態更新：（列出議題狀態變更）
- 遷移至 entities：（列出，若無則寫「無」）
- 新增 entities：（列出，若無則寫「無」）
- 呈現品質：（列出修復或待辦的頁面，若全數通過則寫「全部通過」）
- 超長頁面（> 500 行）：（列出頁面名稱與行數，及處理結果：已拆分 / 使用者稍後處理 / 無）
- 規則檔健檢：
  - wiki/CLAUDE.md：XX 行（閾值 80 行）
  - .claude/rules/wiki-ingest.md：XX 行（閾值 80 行）
  - .claude/rules/wiki-ingest-format.md：XX 行（閾值 200 行）
  - 各記者規則檔：各 XX 行（閾值 100 行）
  - 矛盾：（列出，若無則寫「無」）
  - 引用驗證：（列出失效引用，若無則寫「全部通過」）
  - 遵守率：（列出 < 2/3 的規則，若全部通過則寫「全部通過」）
  - 過期規則（> 60 天）：（列出，若無則寫「無」）
  - 簡化：（是否執行 / 跳過）
- 讀者模擬：（3 題結果：✅/⚠️ 已修復/❌ 待辦，各附一句說明）
- overview.md：已更新
```

### 9. 更新 wiki/index.md

同步所有因本次 lint 造成的頁面新增、移動、狀態變更。

## 注意事項

- 繁體中文為主，英文術語保留英文
- 每次修改頁面都必須更新「最後更新」欄位
- `log.md` 只能 append，不可修改既有條目
- `news/` 目錄唯讀，不可修改
- 遷移頁面時保留原始 topics/ 路徑的重定向提示，避免 broken links
- 步驟 3f 超長頁面拆分：**必須等待使用者確認才能執行**，記者只負責回報分析
