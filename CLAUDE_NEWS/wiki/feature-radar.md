# 官方功能熱度雷達

追蹤 Anthropic 官方發布的 Claude / Claude Code 功能熱度、試用價值與快速上手方式。
僅收錄官方 changelog、release note 或官方公告來源；社群工具見 [[topics/community-tech-tools]]。
每次 ingest 後由 LLM 維護：新增功能、更新熱度、補充社群回饋。

**最後更新：** 2026-06-11（新增 Claude Corps 公益計畫；v2.1.173 模型名稱正規化修復）

---

## 評分說明

| 指標 | 說明 |
|------|------|
| 🔥 熱度 | 1–5 格，依來源數量、討論量、持續天數、社群工具跟進情況綜合評分 |
| 試用價值 | ✅ 推薦 / ⚡ 有條件推薦 / ⏳ 觀望 / ❌ 暫不推薦 |
| 狀態 | 正式發布 / Research Preview / 公開測試 / 限制存取 |

**熱度計分基準：**
- 🔥 — 單次提及，討論有限
- 🔥🔥 — 2–3 個來源，短期討論
- 🔥🔥🔥 — 多來源 + 持續 2 天以上，或有社群工具跟進
- 🔥🔥🔥🔥 — 廣泛討論 + 社群工具爆發 / 大會主角功能
- 🔥🔥🔥🔥🔥 — 里程碑事件，跨平台持續多日，改變開發者工作流

---

## 📋 功能全覽表（2026-04-25 起）

| 功能 | 發布日期 | 熱度 | 試用價值 | 狀態 |
|------|----------|------|----------|------|
| **Claude Corps**（非營利 AI 教育公益計畫） | 2026-06-11 | 🔥🔥 | ⏳ 觀望 | 公告（1,000 名 Fellows，一年全薪，派遣至美國非營利組織）|
| **Claude Code v2.1.173**（Fable 5 模型名稱修復） | 2026-06-11 | 🔥 | ✅ 推薦 | 正式發布（`[1m]` 後綴自動移除；誤報沙盒錯誤修正）|
| **Claude Fable 5**（Mythos 架構公開版，$10/$50 per M token） | 2026-06-09 | 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布（6/22 前訂閱包含；之後消費制；護欄 fallback 至 Opus 4.8 < 5% session；護欄政策 6/11 部分修改：LLM 研究限制改為可見；資安研究護欄仍過激）|
| Python SDK v0.109.1（`frontier_llm` refusal 類別） | 2026-06-09 | 🔥 | ✅ 推薦 | 正式發布（Fable 5 安全分類器相關 refusal API 補齊）|
| Claude Code v2.1.170（Fable 5 支援） | 2026-06-09 | 🔥🔥 | ✅ 推薦 | 正式發布（Claude Code terminal 可切換 Fable 5）|
| Claude Code v2.1.169 `--safe-mode` 旗標 | 2026-06-08 | 🔥🔥 | ✅ 推薦 | 正式發布（停用所有客製化設定，MCP/hooks/skills/CLAUDE.md；故障排除利器）|
| Agent SDK / `claude -p` 計費軌道切割（2026-06-15 生效） | 2026-06-15 | 🔥🔥🔥🔥🔥 | ⚠️ 必讀 | Breaking Change（Pro $20/Max 5x $100/Max 20x $200 程式化月預算；超額依 API 費率）|
| Google Colab CLI 整合 Claude Code / Codex | 2026-06-08 | 🔥🔥 | ✅ 推薦 | 正式發布（降低 Colab 使用 AI coding agent 門檻）|
| Python SDK v0.107.1（foundry x-api-key header 修復） | 2026-06-07 | 🔥 | ✅ 推薦 | 正式發布（Bedrock Foundry 使用者應升級）|
| Python SDK v0.106.0（Claude Opus 4.1 標記棄用） | 2026-06-06 | 🔥 | ✅ 推薦 | 正式發布（開發者應遷移至新版模型 ID）|
| Claude Code v2.1.162（`waitingFor` 可見性 + `--tools` Grep/Glob 目錄遍歷） | 2026-06-04 | 🔥🔥 | ✅ 推薦 | 正式發布（agent 監控可見性顯著改善）|
| Claude Code v2.1.161（OTEL metrics 標籤 + claude agents 改善） | 2026-06-03 | 🔥🔥 | ✅ 推薦 | 正式發布（企業可觀測性提升）|
| Claude Code v2.1.160（shell 安全修復 + `workflow`→`ultracode` rename） | 2026-06-02 | 🔥🔥🔥 | ✅ 推薦 | 正式發布（⚠️ Breaking: `workflow` 更名為 `ultracode`）|
| Claude Code v2.1.158（Auto mode on Bedrock/Vertex/Foundry） | 2026-05-30 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| Claude Opus 4.8（SWE-bench Pro 69.2%、1M context、Fast Mode 1/3 費用） | 2026-05-28 | 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| Dynamic Workflows（最多 1,000 平行子代理） | 2026-05-28 | 🔥🔥🔥🔥 | ❌ 暫不推薦 | Research Preview（UltraCode 1.7M token bug，無退款）|
| `skipLfs` 選項 + npm 版本通知（v2.1.153） | 2026-05-28 | 🔥 | ⚡ 有條件推薦 | 正式發布 |
| Coordinator 模式 + `/code-review --fix`（v2.1.152） | 2026-05-27 | 🔥🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| 小企業 Skills（31 個官方 Skills） | 2026-05-24 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| `/code-review`（原 `/simplify`，v2.1.146） | 2026-05-21 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| HTML 輸出格式（官方背書） | 2026-05-20 | 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦 | 官方建議（非新功能，策略轉向）|
| `claude agents --json`（v2.1.145） | 2026-05-20 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| 自架沙箱 + MCP 隧道（完整文件） | 2026-05-22 | 🔥🔥🔥🔥 | ⚡ 有條件推薦 | 公開測試（文件完整）|
| `/resume` 背景 session 擴展（v2.1.144） | 2026-05-19 | 🔥 | ✅ 推薦 | 正式發布 |
| Proactive Workflows | 2026-05-18 | 🔥🔥🔥 | ⏳ 觀望 | 公告（細節待確認）|
| Capability Curve | 2026-05-18 | 🔥🔥 | ⏳ 觀望 | 公告（細節待確認）|
| Plugin 依賴關係強制執行（v2.1.143） | 2026-05-16 | 🔥 | ✅ 推薦 | 正式發布 |
| `claude agents` 細粒度旗標（v2.1.142） | 2026-05-14 | 🔥🔥 | ⚡ 有條件 | 正式發布 |
| `/loop`・`/batch`・`/background` | 2026-05-14 | 🔥🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| `/goal` 指令 | 2026-05-12 | 🔥🔥🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| Agent View | 2026-05-12 | 🔥🔥🔥 | ⚡ 有條件 | Research Preview |
| Managed Agents（全套） | 2026-05-11 | 🔥🔥🔥🔥🔥 | ⚡ 有條件 | 正式發布 |
| macOS Computer Use | 2026-05-03 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| Claude Code Sandboxing | 2026-05-10 | 🔥🔥🔥 | ⚡ 有條件 | 正式發布 |
| 操作安全 + `hard_deny` | 2026-05-09 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| Claude Security（公開 Beta） | 2026-05-06 | 🔥🔥🔥 | ⚡ 有條件推薦 | 公開測試 |
| Claude Connectors 創意工作 | 2026-05-04 | 🔥🔥 | ⚡ 有條件 | 正式發布 |
| MCP `alwaysLoad` | 2026-04-28 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| `worktree.baseRef` 設定 | 2026-05-08 | 🔥 | ⚡ 有條件 | 正式發布 |
| Claude Design | 2026-04-27 | 🔥🔥 | ❌ 暫不推薦 | 初期（問題多）|
| Dreaming 記憶整合 | 2026-05-07 | 🔥🔥🔥🔥 | ⏳ 觀望 | Research Preview |
| Outcomes 規格驗證 | 2026-05-07 | 🔥🔥🔥🔥 | ⚡ 有條件 | 公開測試 |

---

## 🆕 最新功能（2026-06）

### Claude Fable 5（Mythos 架構公開版）
**發布：** 2026-06-09 | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** Anthropic 首款向大眾開放的 Mythos 級模型。Fable 5 = Mythos 5 模型權重 + 安全分類器護欄，觸發時靜默 fallback 至 Opus 4.8（< 5% session）。定價 $10/$50 per million token，context 1M，max output 128K。6/22 前含括於訂閱方案。

**為何熱：** HN 2,448 分，近 2,000 評論。幾乎所有 benchmark SOTA，任務越長期越複雜優勢越大。首次讓開發者在一般工作流中使用 Mythos 等級推理能力。

**快速上手：**
```bash
# Claude Code terminal 切換 Fable 5
claude --model claude-fable-5-20260609

# 或在 Claude Code 設定中選擇 Fable 5 模型
```

**注意事項：** 前沿 LLM 開發工作（訓練 pipeline、推論研究、ML 加速器設計）會觸發靜默護欄，輸出品質降低且不告知；6/22 後需消費制計費；30 天資料保留政策適用於所有平台。見 [[entities/fable-5]]、[[entities/mythos]]。

---

## 最新功能（2026-05）

### Claude Opus 4.8 + Dynamic Workflows + Fast Mode
**發布：** 2026-05-28 | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布（Dynamic Workflows 為 Research Preview）

**是什麼：** Anthropic 最大規模旗艦更新：① **Opus 4.8**：SWE-bench Pro 69.2%、1M token context window、同價格發售；② **Dynamic Workflows**：Claude Code 可動態撰寫 orchestration scripts，最多啟動 **1,000 個平行子代理**（Research Preview，限 Max 方案）；③ **Fast Mode 降價**：2.5× 速度的 Fast Mode 費用降至前代的 **1/3**；④ **使用者可控努力程度**：claude.ai 用戶可自行調節 Claude 任務投入強度。

**為何熱：** HN 1662 分——Opus 4.8 是 Anthropic 2026 年最受關注的發布。Dynamic Workflows 被視為 Claude Code 工作流的架構性突破：「Work you'd normally plan in quarters now finishes in days」（官方）。Fast Mode 降價解除了 Max 方案用戶的高速推論成本限制。

**快速上手：**
```bash
# Dynamic Workflows（Max 方案，Claude Code CLI）
claude code "Hunt all N+1 query bugs across the entire service"
# 系統自動生成並執行 orchestration script，啟動並行子代理

# Fast Mode：在 Claude Code settings 啟用 fast mode
# 或在 claude.ai 對話框選擇「快速」選項
```

**注意事項：** Dynamic Workflows 為 Research Preview，限 Max 方案；初期社群反映 Opus 4.8 有 "pecl scripts" 行為退步；thinking blocks 400 錯誤已由 v2.1.156 修復。見 [[entities/opus-4-8]]、[[topics/code-quality-decline]]。

---

### Coordinator 模式 + `/code-review --fix`（v2.1.152）
**發布：** 2026-05-27（v2.1.152） | **熱度：** 🔥🔥🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** Claude Code v2.1.152 帶來兩大架構性更新：① **`/code-review --fix`**：審查完成後直接將建議套用至工作樹（修正錯誤、優化可重用性與效率，自動跳過誤報）；② **Coordinator 模式**：全新多 worker 代理人協調層，支援任務委派、結果合成、lifecycle 管理、跨 session peer 協調與獨立驗證委派結果。社群分析顯示系統提示增加 +4,566 tokens，標誌 Claude Code 正式進入多代理人編排層。

**為何熱：** Coordinator 模式是 Claude Code 從「單一 agent」走向「代理人工廠（agent factory）」的關鍵里程碑；`/code-review --fix` 打通了「發現問題→修復問題」的最後一哩路，不再需要手動查看 review 結果。HN 社群社群詳細分析了 +4,566 tokens 的新增內容。

**快速上手：**
```bash
/code-review --fix         # 審查並直接套用修復建議至工作樹
/code-review --fix high    # 高強度審查後自動修復
# Coordinator 模式：在 CLAUDE.md 指定 coordinator-mode agent role
# 讓 Coordinator agent 委派任務至多個 worker agents 並彙整結果
```

**注意事項：** +4,566 tokens 的系統提示增加會提高每次呼叫成本；Coordinator 模式適合大型任務拆分，但需明確設計 worker 邊界以避免重工。

---

### 小企業 Skills（31 個官方 Skills）
**發布：** 2026-05-24（官方正式發布） | **熱度：** 🔥🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** Anthropic 官方發布 31 個針對小型企業設計的 Skills，涵蓋財務、客服、行銷、HR 等商業場景。首日下載量據報達 **38.2 萬次**，是 Anthropic Skills 生態向非工程師商業用戶擴張的重要里程碑。

**為何熱：** 此批 Skills 定位明確針對非技術用戶，代表 Claude 平台從「開發者工具」向「通用商業平台」延伸的策略轉向；38.2 萬次首日下載量顯示潛在用戶基礎遠超現有開發者社群。

**適合：** 小型企業負責人、非技術業務人員、需要 AI 輔助標準商業流程的場景。

**注意事項：** 官方 Skills 的具體功能與限制需逐一確認；建議先從最切近現有業務流程的 Skills 開始試用。

---

### `/code-review` 指令（原 `/simplify`，v2.1.146）
**發布：** 2026-05-21（v2.1.146） | **熱度：** 🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** Claude Code v2.1.146 將 `/simplify` 指令正式更名為 `/code-review`，並新增可選強度參數（如 `/code-review high`）。同時，auto mode 不再抑制 `AskUserQuestion`——當 user 或 skill 明確觸發時，auto mode 下仍可向使用者提問。

**為何熱：** 更名使指令語意更直觀；強度參數允許更精確控制 review 深度，適合快速掃描（預設）或嚴格審查（high）不同場景。

**快速上手：**
```
/code-review           # 標準程式碼審查（原 /simplify）
/code-review high      # 高強度審查，找出更深層問題
```

**注意事項：** 原 `/simplify` 已棄用，建議更新 CLAUDE.md 中引用此指令的自訂規則。

---

### HTML 輸出格式（官方策略轉向）
**發布：** 2026-05-20（Anthropic 官方 Blog） | **熱度：** 🔥🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 官方建議

**是什麼：** Anthropic 官方 Blog 由 Claude Code 團隊成員撰文（《Using Claude Code: The unreasonable effectiveness of HTML》），主張以 **HTML 取代 Markdown** 作為 AI agent 輸出格式。理由：HTML 表達能力更強（支援表格、折疊、互動元件）、可直接在瀏覽器分享，且 Claude 已能高品質生成 HTML；此文代表**官方對輸出格式的策略轉向**，非 Claude 新功能，但對工作流設計影響重大。

**為何熱：** 此主題在 2026-05-09 已在 HN 引發 187 則討論（社群自發），官方背書後社群熱度大幅提升（🌋重燃）；Claude Code 生成報告、data viz、工具輸出的開發者應優先考慮切換

**快速上手：**
```
# 在 prompt 中明確要求 HTML 輸出
"請用 HTML 格式輸出分析報告，要可以直接在瀏覽器開啟"
"生成一個 HTML dashboard，包含折疊區塊和互動表格"
# 搭配 Claude Code 的 Write 工具直接輸出 .html 檔案
```

**注意事項：** Markdown 仍適合人機協作的純文字場景（CLAUDE.md、PR 描述）；HTML 更適合最終輸出、儀表板、分享用報告；見 [[topics/community-tech-discussions]]（HTML vs Markdown 討論）

---

### `claude agents --json`（v2.1.145）
**發布：** 2026-05-20（v2.1.145） | **熱度：** 🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** `claude agents --json` 指令將目前所有存活的 Claude session 以 JSON 格式輸出，包含 `agent_id`（本 session ID）與 `parent_agent_id`（父 session ID，支援多層 agent 層級識別）。

**為何熱：** 直接解鎖 tmux-resurrect、status bar、session picker 等工具的整合需求；多層 agent 工作流的可觀察性大幅提升；對管理大量並行 agent 的工作流（如 Claude Squad、Harness）尤為實用。

**快速上手：**
```bash
claude agents --json          # 輸出所有 session 的 JSON 列表（含 agent_id）
claude agents --json | jq '.[] | .agent_id'   # 取得所有 agent ID
# 搭配 tmux-resurrect：在 session 恢復時用 agent_id 識別對應任務
```

**注意事項：** `parent_agent_id` 在非層級架構的 session 中為 null；建議搭配 v2.1.142 的細粒度 agent 旗標使用。

---

### 自架沙箱 + MCP 隧道（Self-hosted Sandboxes + MCP Tunnels）
**發布：** 2026-05-19（官方公告） | **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 公開測試

**是什麼：** Anthropic 在 Managed Agents 平台新增兩項企業功能。**自架沙箱**讓企業在自有基礎設施上執行 agent 工作流，資料不需送至 Anthropic 雲端。**MCP 隧道**讓私有部署的 MCP 伺服器能安全連接 Claude Code agent，無需將內部服務暴露公網。

**為何熱：** 直接解除大型企業採用 Managed Agents 的兩大障礙——資料主權與私有 MCP 存取。結合 Proactive Workflows，標誌 Anthropic 全面布局企業私有雲 agent 場景；對有資料合規需求（金融、醫療、政府）的企業而言試用價值高。

**快速上手：**
```
# 詳細配置文件待 Anthropic 正式發布
# 基本流程：在自有基礎設施部署 Anthropic agent runtime
# 再透過 MCP 隧道配置連接內部 MCP 伺服器
# 持續追蹤：https://anthropic.com/claude-code/managed-agents
```

**注意事項：** 自架沙箱需要自行管理基礎設施安全與更新；MCP 隧道的身份驗證機制與延遲影響需在 PoC 階段充分測試。

---

### `/resume` 背景 session 擴展（v2.1.144）
**發布：** 2026-05-19（v2.1.144） | **熱度：** 🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** `/resume` 本已存在，v2.1.144 將其擴展以支援背景 session。`claude --bg` 啟動的背景 session 現可在 `/resume` 列表與互動式 session 並列顯示（標記為 `bg`），並加入 elapsed duration 計時。

**為何熱：** 是 `/goal` fire-and-forget 工作流的重要補充——背景任務跑完後可直接 `/resume` 切回，不需重新開啟新 session；對大量使用背景自動化 agent 的開發者有直接效益。

**快速上手：**
```bash
# 啟動背景 session
claude --bg "執行測試套件並修復失敗的測試"

# 在互動式 session 中恢復背景 session
/resume
```

**注意事項：** 搭配 Agent View（`claude agents`，v2.1.139+）使用效果最佳。

---

### Proactive Workflows
**發布：** 2026-05-18（官方公告） | **熱度：** 🔥🔥🔥 | **試用價值：** ⏳ 觀望 | **狀態：** 公告（細節待確認）

**是什麼：** Anthropic 正式公告的主動式工作流程能力，讓 Agent 能夠自主排程並在適當時機主動觸發任務，而非等待用戶輸入觸發。是 Claude Code 從「被動回應工具」走向「主動 Agent 平台」的架構性升級，與 Cat Wu「AI 的下一步是主動性（proactivity）」論述直接對應；見 [[entities/cat-wu]]、[[entities/managed-agents]]。

**為何熱：** InfoQ 以頭條報導此公告，社群期待已久的「主動性」終於有官方框架支撐；MCP 語音整合（2026-05-15，Claude 主動發出語音提問）、agent-baton（速率上限前主動轉移工作）等社群工具均是此方向的先行探索。

**注意事項：** 官方文件細節尚待確認，建議觀望至 SDK 支援與文件正式發布後再評估；試用前確認計費模式（Proactive 觸發可能走 Agent SDK 費率）。

---

### Capability Curve
**發布：** 2026-05-18（官方公告） | **熱度：** 🔥🔥 | **試用價值：** ⏳ 觀望 | **狀態：** 公告（細節待確認）

**是什麼：** Agent 能力曲線追蹤機制，協助用戶和企業客戶評估 Claude Agent 在不同任務類型（程式碼生成、研究、規劃等）的能力進展隨時間的變化。

**為何熱：** 企業採購決策者長期缺乏系統化評估 AI Agent 能力進展的工具，此功能若有效實現，對企業 ROI 評估具有重要意義；與 CC-Canary（自動偵測效能漂移）的社群解決思路呼應。

**注意事項：** 僅有公告，尚無具體文件；標記觀望至正式文件發布。

---

### Plugin 依賴關係強制執行 — v2.1.143
**發布：** 2026-05-16（v2.1.143） | **熱度：** 🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** `claude plugin disable` 指令新增依賴關係強制執行機制——當目標 plugin 被其他已啟用 plugin 依賴時，指令將拒絕執行並提示完整的停用鏈建議指令，防止工具鏈因單一 plugin 被停用而損壞。

**快速上手：**
```bash
# 若 plugin-A 被 plugin-B 依賴，嘗試停用時 Claude Code 會提示：
claude plugin disable plugin-A
# → 拒絕執行，提示：先執行 claude plugin disable plugin-B，再執行 claude plugin disable plugin-A

# 按建議的停用鏈逐步執行即可安全停用
```

**注意事項：** 對維護複雜 plugin 組合（3 個以上互相依賴）的用戶尤為重要；升級後應測試現有停用腳本是否需要調整順序。

---

### `claude agents` 細粒度旗標 — v2.1.142
**發布：** 2026-05-14（v2.1.142） | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：**
`claude agents` 指令新增 8 個啟動旗標，開發者可直接在指令列指定：
- **`--model`** — 指定子代理使用的模型版本
- **`--add-dir`** — 指定額外工作目錄
- **`--settings`** — 指定設定檔路徑
- **`--mcp-config`** — 指定 MCP 配置路徑
- **`--plugin-dir`** — 指定插件目錄
- **`--permission-mode`** — 指定權限模式
- **`--effort`** — 指定任務努力等級
- **`--dangerously-skip-permissions`** — 跳過權限確認（謹慎使用）

**為何有用：** 過去啟動子代理需依賴設定檔，現可完全透過指令列完成細粒度配置，大幅降低多代理腳本化啟動的設定摩擦；與 Managed Agents 架構配合使用效果最佳。

**快速上手：**
```bash
# 指定模型 + MCP 配置啟動子代理
claude agents --model claude-opus-4-7 --mcp-config ./mcp-config.json

# 限制工作目錄 + 安全模式
claude agents --add-dir ./src --permission-mode cautious
```

**注意事項：** `--dangerously-skip-permissions` 會跳過所有確認提示，只在完全受控的 CI 環境中使用；建議搭配 `--permission-mode` 明確定義邊界。

---

### `/loop`、`/batch`、`/background` 指令 — 完整自主執行套件
**發布：** 2026-05-14（官方文件上線） | **熱度：** 🔥🔥🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：**
與 `/goal` 共同構成官方自主執行指令套件：
- **`/loop`** — 固定循環執行，不設完成條件，持續迴圈直到手動停止
- **`/batch`** — 批次任務，對一組輸入依序執行相同工作流
- **`/background`** — 背景執行，讓 Claude 在後台獨立運行不阻斷終端機

**為何熱：** 官方文件同日上線，與 `/goal` 相互呼應，形成完整自主執行指令集；Claude Code 負責人 Cat Wu 同日接受訪問指出「AI 下一步是主動性（proactivity）」，完全呼應此方向；標誌 Claude Code 產品定位正式從「每輪互動」轉向「設定目標、自主完成」的 agent 開發範式。

**快速上手：**
```
# 固定循環（直到手動 Ctrl+C 停止）
/loop 每隔 5 分鐘讀取 logs/app.log 並報告異常

# 批次任務（對一組檔案執行）
/batch src/components/*.tsx 為每個元件新增 JSDoc 型別定義

# 背景執行
/background 持續監控 build/output.log，偵測到 ERROR 時建立 GitHub issue
```

**注意事項：** `/loop` 不設自動終止條件，建議搭配費用監控工具（Ledger、Tokenyst）設定上限；`/batch` 的進度可透過 Agent View 追蹤；與 6/15 信用池制費用結構同步，自動化工作流的成本評估更為重要。

---

### `/goal` 指令 — Fire-and-Forget 自動化
**發布：** 2026-05-12（v2.1.139） | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：**
設定可驗證的完成條件後，每輪執行結束由一個小型快速模型自動判斷條件是否成立；未達成則自動開始下一輪，直到目標完成為止。適合有明確「終態」的長時間任務。

**為何熱：** Code with Claude 大會官方主角功能（2026-05-12）；Reddit 與 HN 廣泛討論；官方文件再度擴充（2026-05-14），搭配 `/loop`・`/batch`・`/background` 形成完整自主執行套件；持續跨日覆蓋，社群稱之為 Claude Code 進入「非同步工作流時代」的標誌性版本。

**最適合的場景：**
- 大批量重構（TypeScript 型別錯誤全部清零）
- 測試全通過（CI green）
- 模組遷移（某目錄下所有 `.js` 改為 `.ts`）

**快速上手：**
```
# 在 Claude Code 中輸入：
/goal 所有 TypeScript 型別錯誤歸零，執行 tsc --noEmit 零報錯

# 或：
/goal tests/unit/ 所有測試通過，npm test 零失敗

# 或：
/goal src/legacy/ 目錄內所有 require() 改為 ES Module import，且不破壞現有測試
```

**注意事項：** 目標條件必須是可機器驗證的（有指令可跑），不適合純主觀判斷的任務（如「優化程式碼可讀性」）。

---

### Agent View — 多 Session 統一管理面板
**發布：** 2026-05-12（v2.1.139） | **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** Research Preview

**是什麼：**
統一面板管理所有並行 Claude Code 工作階段的即時狀態（執行中 / 等待輸入 / 已完成），解決過去需要手動管理多個終端機視窗的痛點。

**為何熱：** 與 `/goal` 同一版本發布，是 Managed Agents 正式生產化的配套工具；多代理工作流的使用者首次有官方 UI 可用。

**適合：** 同時跑 3 個以上 Claude Code agent 的重度使用者；目前仍為 Research Preview，功能可能變動。

**快速上手：**
```bash
# 啟用 Agent View 面板
claude agents

# 或在現有 session 中執行
# 面板會顯示所有並行 session 的狀態與等待輸入提示
```

**社群反應：** 初步正面，但部分使用者仍偏好 mux0 / Nimbalyst 等社群工具提供的更細緻控制。

**v2.1.140 補充（2026-05-13）：** `subagent_type` 現在支援大小寫不敏感及分隔符號不敏感匹配（`"Code Reviewer"` → `code-reviewer`），進一步降低多代理配置摩擦。

---

### Managed Agents — 官方多代理托管框架
**發布：** 2026-05-11（正式發布，從 Research Preview 升格） | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：**
Anthropic 官方 Agent 框架，提供三項核心能力：
- **Dreaming**：Agent 在任務間隙自動鞏固記憶（仍為 Research Preview）
- **20 路子代理並行**：最高 20 個子代理同時執行
- **Outcomes 規格驗證**：Agent 完成後自我驗證是否符合預設規格

**為何熱：** 跨越 3 週持續覆蓋（4/28 → 5/11 → 5/12）；Code with Claude 大會主題；Reddit 70 天自建 multi-agent 開發者案例廣傳；Python/TypeScript SDK 同步支援。

**適合：** 需要長時間、跨 session、可驗證輸出的 Production-level Agent 工作流；**不適合**快速原型或一次性任務。

**快速上手：**
```python
# Python SDK v0.100.0+
import anthropic

client = anthropic.Anthropic()

# 建立 Managed Agent
agent = client.managed_agents.create(
    name="my-agent",
    model="claude-opus-4-20260501",
    instructions="你是一個專注於 Python 重構的工程師代理"
)

# 設定 Outcome 規格
task = client.managed_agents.tasks.create(
    agent_id=agent.id,
    prompt="重構 src/legacy/ 下所有函數至符合 type hints",
    outcomes=["所有函數有完整 type hints", "mypy 零錯誤"]
)
```

```typescript
// TypeScript SDK v0.95.0+
import Anthropic from '@anthropic-ai/sdk';
const client = new Anthropic();

const task = await client.managedAgents.tasks.create({
  agentId: agent.id,
  prompt: '...',
  outcomes: ['...']
});
```

**社群關鍵洞察：** 自建 multi-agent 開發者指出「任務簡報（brief）的撰寫品質才是系統成敗的核心」，非框架選擇。官方托管 vs 社群自組架構差距仍在社群持續比較中。

**2026-05-13 更新：** Boris Cherny 公開每晚讓**數千個 AI 子代理**執行「深度工作」的工作流（白天設框架 → 夜間數千子代理並行深入研究 → 早上整合），被 Business Insider 主流媒體報導。這是 Managed Agents 20 路並行能力的極端個人應用案例，也驗證了官方工具正在降低大規模子代理配置的摩擦（v2.1.140 的 `subagent_type` 不敏感匹配）。

**相關頁面：** [[entities/managed-agents]]

---

### macOS Computer Use — 全桌面自動化
**發布：** 2026-05-03 | **熱度：** 🔥🔥🔥 | **試用價值：** ✅ 推薦（macOS 用戶） | **狀態：** 正式發布

**是什麼：**
Claude Code / Claude Cowork 可直接控制 macOS 桌面滑鼠與鍵盤，從純程式碼助理升格為全桌面自動化代理，可操作任何 GUI 應用程式。

**快速上手：**
```
# 在 Claude Code 或 Claude Cowork 中直接描述桌面任務：
「打開 Figma，將 designs/ 資料夾中所有 frame 匯出為 PNG」
「在 Terminal 中執行 npm test，截圖結果後附上報告」
```

**注意事項：** 不可逆桌面操作（刪除檔案、送出表單）建議在描述中加上「操作前請先確認」；v2.1.136 的 `hard_deny` 機制可設定禁止操作邊界。

---

### Claude Code Sandboxing — 官方沙箱隔離
**發布：** 2026-05-10（官方文件正式發布） | **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：**
透過 OS 層級原語（primitives）對 bash 工具實施檔案系統與網路隔離。在 session 開始時預先定義操作邊界，讓 Claude Code 在邊界內自由執行並縮小意外破壞的半徑。

**為何熱：** 在 CVE-2026-39861 沙箱逃逸漏洞曝光（2026-05-08）的背景下，官方文件及時補位；安全意識高的團隊高度關注。

**快速上手：**
```json
// .claude/settings.json — 限制 bash 工具只能存取 src/ 和 tests/
{
  "sandbox": {
    "enabled": true,
    "allowedPaths": ["src/", "tests/", "package.json"],
    "networkAccess": false
  }
}
```

**適合：** 在生產環境或多人共用機器上執行 Claude Code；不適合需要廣泛系統存取的任務（如環境設定、安裝依賴）。

---

### v2.1.136 操作安全 + `hard_deny` 機制
**發布：** 2026-05-09 | **熱度：** 🔥🔥🔥 | **試用價值：** ✅ 推薦（所有使用者） | **狀態：** 正式發布

**是什麼：**
系統提示新增「操作安全與如實回報」機制（+525 tokens）：
- 不可逆或對外操作須先獲授權確認
- 刪除前需檢視目標
- 必須如實回報跳過的步驟與未通過的測試
- `hard_deny`：使用者可設定無條件安全邊界（不可被覆蓋）

**為何值得關注：** 所有依賴 Claude 自主授權的現有工作流都可能受影響；`hard_deny` 是目前唯一能在提示詞層面設定強制邊界的機制。

**快速上手：**
```json
// .claude/settings.json — 設定 hard_deny 規則
{
  "rules": [
    {
      "type": "hard_deny",
      "pattern": "rm -rf",
      "reason": "禁止強制刪除操作"
    },
    {
      "type": "hard_deny",
      "pattern": "git push --force",
      "reason": "禁止強制推送"
    }
  ]
}
```

---

## 🔍 熱度追蹤說明（給 LLM）

每次 ingest 後，請執行以下步驟更新此頁：

1. **新增功能**：若日報出現新的 Claude 功能（🔧 技術更新 或官方公告），在「最新功能」區塊新增條目，包含：
   - 發布日期、版本號
   - 初始熱度評分（依單日討論量給 🔥–🔥🔥🔥）
   - 試用價值初評（有足夠資訊才評，否則標「⏳ 觀望」）
   - 快速上手（若日報有具體指令或 API）

2. **更新熱度**：若已追蹤功能在新日報再次出現（社群討論、新工具跟進、問題回報），熱度 +1 格（上限 🔥🔥🔥🔥🔥）

3. **更新試用價值**：
   - 若出現多個正面使用案例 → 升級（⏳→⚡→✅）
   - 若出現重大 bug、負面評價集中 → 降級（✅→⚡→⏳→❌）
   - 若進入正式發布（從 Preview 升格）→ 考慮升為 ✅

4. **更新全覽表**：同步更新底部全覽表的熱度與狀態欄

5. **更新「最後更新」日期**
