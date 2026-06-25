# 官方功能熱度雷達

追蹤 Anthropic 官方發布的 Claude / Claude Code 功能熱度、試用價值與快速上手方式。
僅收錄官方 changelog、release note 或官方公告來源；社群工具見 [[topics/community-tech-tools]]。
每次 ingest 後由 LLM 維護：新增功能、更新熱度、補充社群回饋。

**最後更新：** 2026-06-25

---

## ⭐ 本週推薦

- **/goal 指令**（熱度 🔥🔥🔥🔥🔥）：設定持久目標讓 Claude Code 多輪保持方向，適合需要長期任務追蹤的開發者
- **Claude Code Artifacts**（熱度 🔥🔥🔥🔥🔥）：工作階段即時輸出可共享互動網頁，適合需要向非工程師成員展示進度的開發者
- **破壞性 Git 指令自動封鎖**（熱度 🔥🔥🔥）：防止 Claude Code 執行 `git reset --hard` 等危險指令，適合重視倉庫安全的所有開發者

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
| **`/rewind` 指令**（Claude Code，從 `/clear` 前節點恢復 context） | 2026-06-25 | 🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **SDK `client.system.message`**（TypeScript v0.106.0 / Python v0.112.0） | 2026-06-25 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Claude Tag**（Slack-native AI 協作工具，65% Anthropic 程式碼由其生成） | 2026-06-24 | 🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **sandbox.credentials + 組織模型限制**（Claude Code v2.1.187） | 2026-06-24 | 🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **MCP CLI 認證指令**（`claude mcp login/logout`，v2.1.186） | 2026-06-22 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **MCP Enterprise Authorization**（Okta / VS Code 零設定 SSO） | 2026-06-19 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **破壞性 Git 指令自動封鎖**（Claude Code v2.1.183） | 2026-06-19 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| **Claude Code Artifacts**（工作階段即時輸出可共享互動網頁） | 2026-06-18 | 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Tool(param:value) permission 語法 + 巢狀 Skills**（v2.1.178） | 2026-06-15 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **enforceAvailableModels 企業管控**（Claude Code v2.1.175） | 2026-06-12 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **Claude Fable 5**（Mythos 架構公開版，$10/$50 per M token） | 2026-06-09 | 🔥🔥🔥🔥🔥 | ❌ 暫不可用 | 出口管制停用 |
| **`--safe-mode` 旗標**（v2.1.169） | 2026-06-08 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **Google Colab CLI 整合 Claude Code / Codex** | 2026-06-08 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **Claude Opus 4.1 SDK 棄用**（Python SDK v0.106.0） | 2026-06-06 | 🔥 | ✅ 推薦 | 正式發布 |
| **`waitingFor` 可見性 + `--tools` 目錄遍歷**（v2.1.162） | 2026-06-04 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **OTEL metrics + claude agents 改善**（v2.1.161） | 2026-06-03 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **workflow → ultracode 重命名**（⚠️ Breaking Change, v2.1.160） | 2026-06-02 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| **Claude Code v2.1.158**（Auto mode on Bedrock/Vertex/Foundry） | 2026-05-30 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **Claude Opus 4.8**（SWE-bench Pro 69.2%、1M context、Fast Mode 1/3 費用） | 2026-05-28 | 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Dynamic Workflows**（最多 1,000 平行子代理，UltraCode 1.7M token bug 無退款） | 2026-05-28 | 🔥🔥🔥🔥 | ❌ 暫不推薦 | Research Preview |
| **`skipLfs` 選項 + npm 版本通知**（v2.1.153） | 2026-05-28 | 🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Coordinator 模式 + `/code-review --fix`**（v2.1.152） | 2026-05-27 | 🔥🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| **小企業 Skills**（31 個官方 Skills） | 2026-05-24 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| **`/code-review`**（原 `/simplify`，v2.1.146） | 2026-05-21 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **`claude agents --json`**（v2.1.145） | 2026-05-20 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **自架沙箱 + MCP 隧道**（完整文件） | 2026-05-22 | 🔥🔥🔥🔥 | ⚡ 有條件推薦 | 公開測試 |
| **`/resume` 背景 session 擴展**（v2.1.144） | 2026-05-19 | 🔥 | ✅ 推薦 | 正式發布 |
| **Proactive Workflows** | 2026-05-18 | 🔥🔥🔥 | ⏳ 觀望 | 公開測試 |
| **Capability Curve** | 2026-05-18 | 🔥🔥 | ⏳ 觀望 | 公開測試 |
| **Plugin 依賴關係強制執行**（v2.1.143） | 2026-05-16 | 🔥 | ✅ 推薦 | 正式發布 |
| **`claude agents` 細粒度旗標**（v2.1.142） | 2026-05-14 | 🔥🔥 | ⚡ 有條件 | 正式發布 |
| **`/loop`・`/batch`・`/background`** | 2026-05-14 | 🔥🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| **`/goal` 指令** | 2026-05-12 | 🔥🔥🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| **Agent View** | 2026-05-12 | 🔥🔥🔥 | ⚡ 有條件 | Research Preview |
| **Managed Agents**（全套） | 2026-05-11 | 🔥🔥🔥🔥🔥 | ⚡ 有條件 | 正式發布 |
| **macOS Computer Use** | 2026-05-03 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| **Claude Code Sandboxing** | 2026-05-10 | 🔥🔥🔥 | ⚡ 有條件 | 正式發布 |
| **操作安全 + `hard_deny`** | 2026-05-09 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| **Claude Security**（公開 Beta） | 2026-05-06 | 🔥🔥🔥 | ⚡ 有條件推薦 | 公開測試 |
| **Claude Connectors 創意工作** | 2026-05-04 | 🔥🔥 | ⚡ 有條件 | 正式發布 |
| **MCP `alwaysLoad`** | 2026-04-28 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **`worktree.baseRef` 設定** | 2026-05-08 | 🔥 | ⚡ 有條件 | 正式發布 |
| **Claude Design** | 2026-04-27 | 🔥🔥 | ❌ 暫不推薦 | 正式發布 |
| **Dreaming 記憶整合** | 2026-05-07 | 🔥🔥🔥🔥 | ⏳ 觀望 | Research Preview |
| **Outcomes 規格驗證** | 2026-05-07 | 🔥🔥🔥🔥 | ⚡ 有條件 | 公開測試 |

---

## 🆕 最新功能（2026-06）

### /rewind 指令（Claude Code）
**發布：** 2026-06-25（v2.1.191）| **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** 在 Claude Code session 中，從 `/clear` 執行前的任一對話節點恢復 context，無需重新描述需求。

**為何熱：** 解決「誤下 `/clear` 失去所有對話背景」的常見痛點，讓長工作階段的上下文管理更具容錯性。

**快速上手：**
```
/rewind
```
選擇要恢復的歷史節點後，對話 context 回到該時間點。

**注意事項：** 僅能回溯至同一 session 內的歷史節點，不跨 session。

---

### SDK client.system.message（TypeScript / Python）
**發布：** 2026-06-25（TS v0.106.0 / Python v0.112.0）| **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** Anthropic SDK 的 `client` 物件新增 `system.message` 支援，開發者可在 client 層統一注入系統訊息，無需每次呼叫時手動傳遞。

**為何熱：** 簡化多輪對話或 agentic loop 中系統提示的管理，TS 與 Python 雙 SDK 同步發布，減少重複程式碼。

**快速上手：**
```python
# Python v0.112.0 / TypeScript v0.106.0
client = anthropic.Anthropic()
# 透過 client.system.message 統一注入系統訊息
```

**注意事項：** TS v0.106.0 與 Python v0.112.0 同日發布，功能對齊；具體 API 介面細節見官方 changelog。

---

### Claude Tag（Slack-native AI 隊友）
**發布：** 2026-06-24（正式發布）| **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** Anthropic 推出 Slack-native AI 協作工具，讓 Claude 以隊友身份加入頻道，可讀取頻道上下文、跨 session 記憶、主動規劃並在未來時間點完成任務，並可連接程式碼庫、工具與資料。

**為何熱：** Anthropic 官方公告揭露內部已有 65% 產品程式碼由 Claude Tag 生成；進入 HN 今日熱門討論（情緒 😊）；定位為 Claude Code 向 Slack 生態的延伸，代表 Anthropic 正式進入 AI 常駐協作工具賽道。

**快速上手：**
```
申請頁面：https://www.anthropic.com/news/introducing-claude-tag
將 Claude Tag 加入 Slack workspace → 邀請至頻道 → @Claude Tag 開始指派任務
```

**注意事項：** 需要 Slack workspace 管理員授權安裝；Claude 可讀取頻道歷史訊息，使用前需評估組織資料隱私政策。

---

### Claude Code v2.1.187 — sandbox.credentials + 組織模型限制
**發布：** 2026-06-24（v2.1.187）| **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** 新增 `sandbox.credentials` 設定可阻止沙盒指令讀取憑證檔案與機密環境變數；同時加入組織層級的模型限制功能，企業管理員可統一管控可用模型清單。

**為何熱：** 兩項功能均直指企業安全管控痛點——沙盒憑證隔離回應社群長期對 AI agent 洩漏 API 金鑰的疑慮；組織模型限制補強了 v2.1.175 引入的 `enforceAvailableModels`。

**快速上手：**
```json
{
  "sandbox": {
    "credentials": false
  }
}
```

**注意事項：** 設為 `false` 後沙盒內指令無法存取任何憑證環境變數，需確認沙盒工作流不依賴憑證傳遞；組織模型限制需企業管理員帳號設定。

---

### MCP CLI 認證指令（mcp login / logout）
**發布：** 2026-06-22（v2.1.186）| **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** 新增 `claude mcp login <name>` 與 `claude mcp logout <name>` 兩個 CLI 指令，讓使用者可從命令列直接完成 MCP Server 認證，無需進入互動式 `/mcp` 選單。支援 `--no-browser` 旗標，可透過 stdin 重導向進行認證，適合 headless / CI 環境。

**為何熱：** 解決 headless 環境中無法透過互動選單認證 MCP 的痛點，對自動化部署與 CI 工作流有直接幫助。

**快速上手：**
```
claude mcp login <server-name>
# headless 環境
claude mcp login <server-name> --no-browser
claude mcp logout <server-name>
```

**注意事項：** 僅適用 v2.1.186 以上版本；適合 headless 環境、CI/CD 管線的 MCP 認證場景。

---

### MCP Enterprise Authorization（企業 SSO 正式版）
**發布：** 2026-06-19 | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** GA（stable）

**是什麼：** MCP Enterprise Authorization 升為 stable，讓企業可透過 Okta、Anthropic 或 VS Code 整合啟用零設定 SSO，統一管理 Claude Code 的授權登入流程，無需個別設定每個開發者的認證憑證。

**為何熱：** 解決企業內多人共用 Claude Code 時，授權管理分散的痛點；VS Code 零設定整合降低了企業 IT 部署門檻。Tech Times 於 2026-06-19 報導確認升為 stable。

**快速上手：**
```
# 透過 VS Code 整合（零設定）：開啟 VS Code Claude Code 擴充套件，依 SSO 登入流程授權
# Okta 整合：在企業 Okta 儀表板設定 MCP 應用，員工透過 SSO 登入即可取得存取權
```

**注意事項：** 企業場景優先，適合需要集中管理 Claude Code 授權的 IT 管理員；個人開發者仍使用 Anthropic 帳號直接登入。

---

### Claude Code Artifacts（工作階段即時共享頁面）
**發布：** 2026-06-18 | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** Claude Code 可將工作階段進度即時輸出為可共享的互動網頁（Artifacts）。支援類型：PR 走查頁面、系統說明文件、儀表板、釋出清單。Artifact 隨工作階段進行自動更新，任何人可直接在瀏覽器開啟，無需安裝工具。

**為何熱：** 解決了「Claude 在本地端工作，但結果難以與非工程師成員共享」的痛點。初日即有多家科技媒體（VentureBeat、The Decoder、Crypto Briefing 等）同步報導；2026-06-19 SD Times、Tech Times、DevOps.com 再次同日跟進確認，企業文件協作場景接受度高。

**快速上手：**
在 Claude Code 工作階段中，執行工作後觸發 Artifacts 輸出——具體指令見官方部落格：
```
# 官方說明
https://claude.com/blog/artifacts-in-claude-code
```

**注意事項：** 目前仍為早期功能，適合企業知識共享與專案進度報告場景；個人日常編碼工作流程受益有限。

---

### Tool(param:value) permission rules 語法
**發布：** 2026-06-15（v2.1.178） | **熱度：** 🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** 新增 `Tool(param:value)` 語法用於 permission rules，允許比對工具的輸入參數（支援 `*` 萬用字元）。例如 `Agent(model:opus)` 可封鎖使用 Opus 模型的子 Agent 啟動。Skills 現在可在巢狀子 Agent 環境中正常運作。

**為何熱：** 解決多 Agent 環境中精細化權限控管的缺口——過去只能針對整個工具，現在可以針對工具的特定參數值設置允許/封鎖規則，大幅提升 Agent 安全管控粒度。

**快速上手：**
```
# 在 settings.json 的 permissions 中使用
# 封鎖使用 Opus 的子 Agent（避免費用過高）
"deny": ["Agent(model:opus)"]

# 只允許特定工具執行特定參數
"allow": ["Bash(command:git*)"]
```

**注意事項：** `*` 為萬用字元，可比對任意值；此功能主要適用於有多 Agent 編排或費用控管需求的開發者。

---

### `enforceAvailableModels` 企業管控
**發布：** 2026-06-12（v2.1.175） | **熱度：** 🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** 新增 `enforceAvailableModels` 管理設定——啟用後，`availableModels` 白名單同時限制預設模型的解析，避免管理員設定的模型限制被繞過。針對企業管理場景，確保組織控管政策的完整性。

**為何熱：** 解決企業部署 Claude Code 時的治理缺口：管理員設定了模型白名單，但預設模型解析仍可能繞過限制。對有合規需求的金融、醫療、政府機構部署場景尤其重要。

**快速上手：**
```json
// .claude/config.json（企業管理員設定）
{
  "availableModels": ["claude-fable-5-20260609", "claude-opus-4-8-20260528"],
  "enforceAvailableModels": true
}
```

**注意事項：** 僅影響企業管理員設定的 `availableModels` 白名單；個人開發者無需關注此設定。

---

### Claude Fable 5（Mythos 架構公開版）
**發布：** 2026-06-09 | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ❌ 暫不可用 | **狀態：** ⚠️ 出口管制停用

> **2026-06-13 更新：** 美國政府出口管制指令，Anthropic 於當日 5:21pm ET 對全體用戶停用 Fable 5 與 Mythos 5。其他模型（Opus 4.8、Sonnet 4.6 等）不受影響。復原時程未公告。詳見 [[entities/fable-5]] 與 [[topics/anthropic-government-policy]]。

**是什麼：** Anthropic 首款向大眾開放的 Mythos 級模型。Fable 5 = Mythos 5 模型權重 + 安全分類器護欄，觸發時靜默 fallback 至 Opus 4.8（< 5% session）。定價 $10/$50 per million token，context 1M，max output 128K。

**為何熱：** HN 2,448 分，近 2,000 評論。幾乎所有 benchmark SOTA，任務越長期越複雜優勢越大。首次讓開發者在一般工作流中使用 Mythos 等級推理能力。

**注意事項：** 目前無法使用。復原後請參考 [[entities/fable-5]] 確認最新狀態再切換。

---

> 2026-05 功能詳細條目已封存，見 [[feature-radar-archive-2026-05]]

