# 官方功能熱度雷達

追蹤 Anthropic 官方發布的 Claude / Claude Code 功能熱度、試用價值與快速上手方式。
僅收錄官方 changelog、release note 或官方公告來源；社群工具見 [[topics/community-tech-tools]]。
每次 ingest 後由 LLM 維護：新增功能、更新熱度、補充社群回饋。

**最後更新：** 2026-07-19

---

## ⭐ 本週推薦

- **Claude Fable 5（免費期限延至 7/19）**（熱度 🔥🔥🔥🔥🔥）：旗艦模型全球恢復，免費使用期限因 GPT-5.6 Sol 被視為同級競品再度延長至 7/19（原 7/12），到期後轉 usage-based billing，想試 Mythos 級推理者把握視窗
- **Claude Code Artifacts**（熱度 🔥🔥🔥🔥🔥）：工作階段可即時輸出互動式儀表板、圖表與可分享頁面，適合需要展示中間產出或建立輕量工具的開發者
- **Claude Cowork 行動版 / 網頁版**（熱度 🔥🔥🔥🔥）：任務可在雲端持續執行，闔上筆電或關閉裝置也不中斷，首波開放 Max 訂閱戶，適合需要行動場景交辦長時間背景任務者

> `/goal` 指令已連續推薦超過 7 天（自 07-09 起）且今日 ingest 未更新其熱度/試用價值，依防霸榜規則換下，改為 Claude Code Artifacts（上次在推薦榜為 07-07 之前）；詳細條目仍見下方全覽表。

---

## ⚠️ 升版風險（每次 ingest 更新）

**最新版本：** v2.1.215（2026-07-19，Claude 不再自動執行 `/verify` 與 `/code-review` 兩項技能，須手動呼叫 `/verify` 或 `/code-review` 指令觸發；無過渡期，升級後立即生效。前一異動為 v2.1.214（2026-07-18）純安全性修正）

| 風險 | 嚴重度 | 說明 |
|------|--------|------|
| Cowork 已知問題（VM bundle 效能劣化 + 檔案靜默截斷） | 🔴 | Cowork 功能會建立高達 10GB 的 VM bundle，導致啟動變慢、UI 延遲、效能隨時間持續劣化（#22543，76 留言）；Edit/Write 工具另因緩衝區容量上限（byte-conservation buffer cap）靜默截斷檔案，任何檔案大小皆可重現（#53940，累計 16 個讚同反應），屬資料完整性風險，非邊緣情況 |
| `/fork` 語意變更（⚠️ Breaking Change，無過渡期） | 🔴 | v2.1.212 起 `/fork` 不再於同一 session 內啟動子 agent，改為複製對話進新背景 session；依賴舊行為撰寫的 skill/hook/巨集需立即改用 `/subtask`，官方 release note 未附完整遷移指南 |
| `/verify` `/code-review` 不再自動觸發（⚠️ Breaking Change，無過渡期） | 🔴 | v2.1.215 起 Claude 不再於背景自動執行 `/verify` 與 `/code-review`，須使用者手動呼叫指令；依賴自動驗證/審查隱性保護的既有工作流（CI、hook、慣例流程）升級後會失去這層保護，官方未附遷移指南 |

**建議：** 升級前確認是否有依賴 `/fork` 舊行為（同 session 子 agent 委派）撰寫的 skill/hook/巨集，若有需立即改寫為 `/subtask`；同時確認既有流程是否依賴 Claude 自動觸發 `/verify` `/code-review`，若有須在 CI 或 hook 中新增顯式呼叫；**重度依賴 Cowork 的使用者近期應避免處理大型檔案或大量寫入操作**，Edit/Write 靜默截斷問題目前無官方修復時程。Fable 5 Defense in Depth 誤判問題持續存在，詳見 [[entities/fable-5]]，非版本升級可解決，本表暫不重複列出。

---

## ⏰ 倒數中（每次 ingest 更新）

| 截止日 | 事件 | 到期後 | 你該做的決定 |
|--------|------|--------|------------|
| **2026-07-19** | Fable 5 免費使用期限＋週配額 +50% 促銷到期日；同日另有兩則媒體報導方向不一致：Tech Times 稱 Max 方案轉永久、Pro 改 Credits-only，Dawn 稱 Fable 5 將以 50% 用量上限併入 Max/Team Premium | 兩篇報導均僅存標題、暫無官方公告可確認何者為準，詳見 [[entities/pricing]] | Pro/Max/Team 及舊制 Enterprise 用戶：留意官方是否於今明兩日發布正式公告，公告前不建議依單一媒體報導調整用量規劃 |
| **2026-08-31** | Sonnet 5 促銷價 $2/$10 per Mtok 結束 | 正式定價未公布，成本可能上升 | 依賴 Sonnet 5 的自動化流程：8 月底前關注正式定價公告 |

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
| **Claude Code v2.1.215**（Claude 不再自動執行 `/verify` 與 `/code-review` 兩項技能，須手動呼叫指令觸發；⚠️ Breaking change 無過渡期） | 2026-07-19 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Claude Code v2.1.212**（`/fork` 改為背景 session 化，原同 session 子 agent 功能改名 `/subtask`；⚠️ Breaking change 無過渡期） | 2026-07-17 | 🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Claude 1Password 整合**（透過已存 1Password 憑證登入網站免暴露密碼，官方一手公告未附） | 2026-07-17 | 🔥🔥 | ⏳ 觀望 | 官方新功能（狀態未明） |
| **Claude for Teachers**（美國通過認證 K-12 教師免費開放進階 Claude 功能與教學技能庫，對接全美 50 州學術標準） | 2026-07-15 | 🔥🔥🔥 | ⏳ 觀望 | 正式發布（限定對象） |
| **Claude Code v2.1.211**（`--forward-subagent-text` 旗標，stream-json 輸出含 subagent 文字與思考內容） | 2026-07-15 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Claude Code v2.1.210**（收合工具摘要列即時耗時計數器、`Write(path)` 啟動警告） | 2026-07-14 | 🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Claude Code v2.1.207**（Auto mode 在 Bedrock/Vertex/Foundry 改預設開啟、修復終端機凍結） | 2026-07-11 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Claude Code Desktop 內建瀏覽器**（AI 可在外部網站讀取/點擊/輸入文字，雙方媒體來源，官方版本號待確認） | 2026-07-11 | 🔥🔥 | ⏳ 待驗證 | 待確認（雙方媒體，官方版本號仍未公布） |
| **Claude Code v2.1.206**（`/cd` 目錄路徑建議、`/doctor` CLAUDE.md 精簡檢查） | 2026-07-10 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Reflect with Claude**（Settings 內使用模式儀表板，媒體廣泛報導但 HN 僅 29 分） | 2026-07-09 | 🔥🔥🔥🔥 | ⚡ 有條件推薦 | Preview |
| **Claude Cowork 行動版 / 網頁版**（雲端持續執行，闔上裝置任務不中斷，首波 Max 訂閱戶，涵蓋政府客戶） | 2026-07-07 | 🔥🔥🔥🔥 | ⚡ 有條件推薦 | Preview（限 Max） |
| **`/config` Dynamic workflow size**（v2.1.202，調整動態工作流 agent 規模 小/中/大，建議性引導值） | 2026-07-07 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Claude Sonnet 5**（Claude Code v2.1.197 新預設，1M context，$2/$10 per Mtok 促銷至 8/31） | 2026-07-01 | 🔥🔥🔥🔥🔥 | ✅ 強烈推薦 | 正式發布 |
| **Claude Science**（科學家專用 AI 工作台，整合研究工具套件、可稽核 artifact、彈性雲端運算） | 2026-07-01 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Org Default Model**（Claude Code v2.1.196，管理員設定組織預設模型，使用者 `/model` 顯示「Org default」） | 2026-06-29 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **`CLAUDE_CODE_DISABLE_MOUSE_CLICKS` 環境變數**（Claude Code v2.1.195，全螢幕模式停用滑鼠點擊/拖拉/懸停） | 2026-06-26 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **`autoMode.classifyAllShell` 設定**（Claude Code v2.1.193，所有 Bash/PowerShell 路由 auto-mode 分類器） | 2026-06-25 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **`/rewind` 指令**（Claude Code，從 `/clear` 前節點恢復 context） | 2026-06-25 | 🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **SDK `client.system.message`**（TypeScript v0.106.0 / Python v0.112.0） | 2026-06-25 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Claude Tag**（Slack-native AI 協作工具，65% Anthropic 程式碼由其生成） | 2026-06-24 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **sandbox.credentials + 組織模型限制**（Claude Code v2.1.187） | 2026-06-24 | 🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **MCP CLI 認證指令**（`claude mcp login/logout`，v2.1.186） | 2026-06-22 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **MCP Enterprise Authorization**（Okta / VS Code 零設定 SSO） | 2026-06-19 | 🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **破壞性 Git 指令自動封鎖**（Claude Code v2.1.183） | 2026-06-19 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| **Claude Code Artifacts**（工作階段即時輸出可共享互動網頁） | 2026-06-18 | 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| **Tool(param:value) permission 語法 + 巢狀 Skills**（v2.1.178） | 2026-06-15 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **enforceAvailableModels 企業管控**（Claude Code v2.1.175） | 2026-06-12 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| **Claude Fable 5**（Mythos 架構公開版，$10/$50 per M token） | 2026-06-09 | 🔥🔥🔥🔥🔥 | ✅ 推薦 | 正式發布（出口管制 2026-07-01 全面解除，Pro/Max/Team 7/7 前 50% 配額） |
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

## 🆕 最新功能（2026-07）

### `/fork` 背景 Session 化與 `/subtask` 語意拆分
**發布：** 2026-07-17（v2.1.212） | **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** `/fork` 不再於同一 session 內啟動子 agent，而是將目前對話複製進一個新的背景 session（在 `claude agents` 列表中自成一列），使用者可同時繼續原本工作；原本 `/fork` 提供的「同 session 子 agent」功能改由新指令 `/subtask` 承接。

**為何熱：** 對核心多 agent 工作流指令的行為重新定義，直接影響所有依賴 `/fork` 舊語意（同 session 子 agent 委派）撰寫的腳本、hotkey、自動化流程；⚠️ Breaking change，無過渡期，即刻生效。與既有 `--forward-subagent-text`（v2.1.211）、Agent View（`claude agents`）同屬 agent 可觀測性/協調基礎設施延伸，見 [[topics/official-community-gap]]「多平行 agent 即時可觀測性」與「Subagent 派工/編排」列。

**現在要試嗎：** 依賴 `/fork` 舊行為（同一 session 內快速委派子任務）的使用者，升版後應立即改用 `/subtask`；需要「複製對話到背景繼續跑、同時手邊繼續操作」的使用者可直接改用新版 `/fork`。

**快速上手：**
```
# 同一 session 內委派子任務（舊 /fork 行為，現改用）
/subtask 幫我檢查這段程式碼有沒有 race condition

# 複製目前對話到新背景 session，繼續在原 session 工作
/fork
# 之後可在 `claude agents` 看到新背景 session 的獨立列
```

**注意事項：** ⚠️ Breaking change，無棄用過渡期；舊版依賴 `/fork` 語意的 skill/hook/巨集需立即改寫為 `/subtask`；官方 release note 未附完整遷移指南，細節以 GitHub Release 為準。

---

### Claude 1Password 整合
**發布：** 2026-07-17（媒體報導，官方一手公告未附） | **熱度：** 🔥🔥 | **試用價值：** ⏳ 觀望（技術細節/適用範圍未知） | **狀態：** 官方新功能（正式/Preview 狀態未明）

**是什麼：** 使用者可透過已存的 1Password 憑證登入網站，過程不會將密碼暴露給 Claude 或 Anthropic，屬 Claude 代理瀏覽情境下的安全登入機制。

**為何熱：** The Verge、Engadget、SiliconANGLE、Help Net Security 四家媒體同步報導，回應「agent 幫你操作瀏覽器時密碼要不要交給 AI」的長期資安疑慮。

**現在要試嗎：** 僅有媒體報導層級資訊，官方文件、適用產品線（Claude.ai／Claude for Chrome／Cowork）、設定步驟均未確認，建議先觀望，待官方一手來源（changelog/部落格）確認後再評估導入。

**快速上手：**
```
（官方尚未公布具體設定步驟，待補）
```

**注意事項：** 本條目資訊完全來自媒體轉述，非官方一手來源；技術規格、支援平台範圍未知，下次 ingest 應追蹤官方來源補齊。

---

### Claude for Teachers
**發布：** 2026-07-15 | **熱度：** 🔥🔥🔥 | **試用價值：** ⏳ 觀望 | **狀態：** 正式發布（限定對象）

**是什麼：** Anthropic 面向美國通過認證的 K-12 教師，免費開放進階 Claude 功能、教學技能庫，並對接全美 50 州學術標準的實證課綱。

**為何熱：** Anthropic Blog 官方公告，另有 CBS News、The Hill、Forbes、9to5Mac、Central Oregon Daily 等至少六家獨立媒體同步報導，Google News 聚合本身標記三個獨立來源，教育產業關注度高。

**現在要試嗎：** 適合美國通過認證的 K-12 教師立即申請取用；非美國教師、非 K-12 教育者、一般開發者或企業使用者不適用（無公開一般存取管道）。

**快速上手：**
```
（原文摘要未提供教師身分驗證/註冊入口的具體網址與步驟，暫無可執行範例；請直接參考官方公告頁 https://www.anthropic.com/news/claude-for-teachers）
```

**注意事項：** 僅限美國通過認證的 K-12 教師；免費範圍與進階功能清單細節未於原文摘要中完整揭露，待後續追蹤補齊。

### Claude Code v2.1.210
**發布：** 2026-07-14（v2.1.210） | **熱度：** 🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** 為收合的工具摘要列加入即時耗時計數器，讓長時間執行的工具呼叫視覺上持續跳動而非看似卡住；並為 `Write(path)` 新增啟動警告。

**為何熱：** 日常使用體感改善（減少誤判「卡住」而中斷任務），純 UI/UX 微調非重大異動。

**快速上手：**
```
更新至 v2.1.210 即自動生效，無需額外設定
```

**注意事項：** 原始 release notes 摘要於來源處被截斷，僅可確認上述兩項變更，其餘變動內容待後續版本資訊補齊。

### Claude Code v2.1.207
**發布：** 2026-07-11（v2.1.207） | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** Auto mode 在 Bedrock、Vertex AI、Foundry 三個平台上不再需要 `CLAUDE_CODE_ENABLE_AUTO_MODE` 環境變數 opt-in 即可使用（可用 `disableAutoMode` 關閉）；同版修復終端機凍結問題。

**為何熱：** 將 2026-05-30 v2.1.158 首次引入的 Bedrock/Vertex/Foundry Auto mode 從 opt-in 改為預設開啟，屬使用門檻降低的升格事件；終端機凍結修復對日常穩定性有直接幫助。

**快速上手：**
```
# Bedrock / Vertex AI / Foundry 上，Auto mode 現為預設開啟
# 如需關閉：
claude config set disableAutoMode true
```

**注意事項：** 若原先依賴 opt-in 未啟用 Auto mode 的工作流，升版後行為會改變，需確認是否要用 `disableAutoMode` 關閉。

---

### Claude Code Desktop 內建瀏覽器（待確認）
**發布：** 2026-07-11（媒體報導，官方版本號待確認） | **熱度：** 🔥 | **試用價值：** ⏳ 待驗證 | **狀態：** 待確認（單一媒體來源）

**是什麼：** The Mac Observer 報導 Anthropic 為 Claude Code Desktop 新增內建瀏覽器功能，讓使用者無需切離桌面應用即可瀏覽網頁內容。

**為何熱：** 目前僅單一媒體來源，尚無官方 changelog / release notes 或社群討論佐證，熱度保守標記；下次 ingest 若未見官方或社群佐證，建議降級或移除。

**注意事項：** 功能存在與具體操作方式待官方確認。

---

### Claude Code v2.1.206
**發布：** 2026-07-10（v2.1.206） | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** `/cd` 新增目錄路徑建議（比照 `/add-dir`）；`/doctor` 新增檢查項目，建議精簡已 checked-in 的 CLAUDE.md 內容。

**為何熱：** 兩項均為日常操作體感改善，`/doctor` 的 CLAUDE.md 精簡建議屬維護性提醒，未直接解決 [[topics/official-community-gap]] 追蹤的 CLAUDE.md 遵循率缺口，僅屬引導層級。

**快速上手：**
```
claude
/cd   # 輸入路徑時出現目錄建議
/doctor   # 檢查項目含 CLAUDE.md 精簡建議
```

**注意事項：** `/doctor` 的建議僅是提醒，不會自動修改 CLAUDE.md 內容。

---

### Reflect with Claude
**發布：** 2026-07-09（測試版） | **熱度：** 🔥🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** Preview

**是什麼：** Settings 內新增使用模式儀表板，讓使用者檢視自己如何使用 Claude（提問類型、時段、模式等）。

**為何熱：** 官方部落格首發，TechCrunch、Mashable、CNET、Axios、The Verge 等多家媒體同步報導，多數類比為「AI 版 Spotify Wrapped」或「螢幕使用時間」統計；TechCrunch 提出質疑角度，認為此舉實質是包裝成「自我反思」的使用引導設計；HN 獲 29 分，屬媒體廣度大於社群深度的訊號組合。2026-07-10 Axios、The Verge 再度跟進報導，媒體延燒持續第二天，熱度升至 🔥🔥🔥🔥。

**現在要試嗎：** 適合想了解自己 Claude 使用習慣、對隱私/資料分析無疑慮的使用者可直接在 Settings 打開看看；對「產品是否藉此變相鼓勵更多使用」有疑慮者，可留意 TechCrunch 的批評角度再決定是否啟用。

**快速上手：**
```
Claude → Settings → Reflect with Claude（測試版儀表板）
```

**注意事項：** 測試版功能，範圍與資料呈現方式可能調整；目前無社群實測回饋佐證儀表板數據準確性或洞察深度。

---

### Claude Cowork 行動版 / 網頁版擴展（雲端持續執行）
**發布：** 2026-07-07（Max 訂閱用戶首波開放）| **熱度：** 🔥🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** Preview（限 Max 訂閱，逐步擴大）

**是什麼：** Claude Cowork 從桌面擴展至行動裝置與網頁版，任務可在雲端持續執行，即使闔上筆電或關閉裝置也不中斷；此次擴展也涵蓋政府機構客戶。

**為何熱：** The Verge、TechCrunch（兩篇）、WIRED、NBC News、The New Stack、Let's Data Science 等 7+ 家媒體同步報導，跨媒體覆蓋密度高，但 HN 討論僅 16 分，屬「媒體先行、社群尚未大量驗證」的早期擴散階段。

**現在要試嗎：** 適合已是 Max 訂閱戶、需要行動場景交辦任務或長時間背景任務的使用者可立即試用；官方明言「完整體驗」仍在桌面版，重度工作流建議暫留桌面。

**快速上手：**
```
於行動裝置或瀏覽器開啟 Claude app → 選擇 Cowork → 指派任務
（Max 訂閱用戶可用；任務可在闔上裝置後於雲端持續執行）
```

**注意事項：** 首波僅開放 Max 訂閱用戶；官方表示完整體驗仍限桌面版，行動/網頁版功能可能有落差；Cowork 既有已知問題（Linux 沙箱啟動失敗、virtiofs FUSE 檔案過期未同步、Windows 11 desktop app tab 消失、RTL 排版未支援）尚未修復，擴展至行動裝置後這些平台相容性問題是否延伸尚待觀察。

---

### Claude Code v2.1.202——/config 新增「Dynamic workflow size」設定
**發布：** 2026-07-07（v2.1.202） | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** `/config` 新增「Dynamic workflow size」設定，可調整 Dynamic Workflows（`ultracode`）動態工作流的 agent 數量規模（小/中/大），屬建議性引導值而非硬上限。

**為何熱：** Dynamic Workflows 本身（2026-05-28 Research Preview，最多 1,000 平行子代理）因 UltraCode 1.7M token bug 無退款而被標「❌ 暫不推薦」；此次更新讓使用者可自行控制規模以降低失控成本風險，但未解決核心退款爭議，故熱度中等。

**快速上手：**
```
claude
/config
# 選擇 Dynamic workflow size → 小 / 中 / 大
```

**注意事項：** 為建議性引導值，非硬性上限，實際 agent 數量仍可能超出設定；核心的 token 消耗與退款爭議尚未解決，大規模場景建議先參考本頁 Dynamic Workflows 條目的既有風險說明。

---

### Claude Sonnet 5 — Claude Code 新預設模型（1M context）
**發布：** 2026-07-01（v2.1.197）| **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ✅ 強烈推薦 | **狀態：** 正式發布

**是什麼：** Claude Code v2.1.197 將 Claude Sonnet 5 設為預設模型，原生支援 1M token context window，促銷定價 $2/$10 per Mtok 至 2026-08-31，agentic 效能接近 Opus 4.8。

**為何熱：** 影響所有新 session，無需手動切換即享 1M context；社群多篇評測確認 agentic 任務、coding、tool use 已接近 Opus 4.8 水準，而成本僅 60%。

**現在要試嗎：** 升級至最新版本即自動生效，所有使用者均適合立即採用。

**快速上手：**
```bash
npm install -g @anthropic-ai/claude-code@latest
# 新 session 自動使用 Sonnet 5 + 1M context；/model 可確認
```

**注意事項：** 促銷定價至 2026-08-31，之後定價待官方公告；1M context 仍需注意 token 成本控制。

---

### Claude Science — 科學家專用 AI 工作台
**發布：** 2026-07-01 | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** 科學家專用 AI app，整合研究常用工具套件、可稽核 artifact（支援研究可重現性）與彈性雲端運算資源。

**為何熱：** Anthropic 首次針對科研場景推出獨立 app，並宣布將自行開發藥物，是 AI 進入學術研究工作流的明確訊號。

**現在要試嗎：** 適合學術研究者、生命科學領域；工程開發場景不受直接影響。

**注意事項：** 今日首報，社群反應待觀察；詳見 [[entities/claude-science]]。

---

## 🆕 最新功能（2026-06）

### Org Default Model
**發布：** 2026-06-29（v2.1.196） | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** 企業管理員在 org console 設定組織預設模型後，使用者在 `/model` 選單看到「Org default」（或角色層級的「Role default」）選項，實現組織內模型版本統一管控。

**為何熱：** 解決企業規模部署中模型版本不一致問題；配合 v2.1.175 的 `enforceAvailableModels` 可形成完整的企業模型管控鏈（限制可用模型 → 設定預設模型）。

**快速上手：**
```
# 管理員在 org console 設定後，使用者執行：
/model
# 選單出現「Org default」或「Role default」選項
```

**注意事項：** 需要 org console 管理員權限才能設定；個人帳號或 Team 以下方案未確認是否支援；同日 v2.1.197 的 `/model` 已出現 Sonnet 5 選項（尚無法選用，正式發布在即）。

---

### CLAUDE_CODE_DISABLE_MOUSE_CLICKS 環境變數
**發布：** 2026-06-26（v2.1.195） | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** 設定此環境變數後，Claude Code 全螢幕模式下停用滑鼠點擊、拖拉、懸停事件，但保留滾輪，讓終端滑鼠事件直通底層（如 tmux）。

**為何熱：** 解決 tmux / 多工終端使用者長期痛點：Claude Code 全螢幕 TUI 截奪滑鼠後，外層終端多工軟體的滑鼠操作失效；此環境變數提供乾淨的逃生口。

**快速上手：**
```bash
export CLAUDE_CODE_DISABLE_MOUSE_CLICKS=1
claude
```

**注意事項：** 僅影響全螢幕模式；滾輪捲動不受影響。適合 tmux / screen / Zellij 重度使用者；純鍵盤工作流無需啟用。

---

### autoMode.classifyAllShell 設定
**發布：** 2026-06-25（v2.1.193） | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** 新增 `autoMode.classifyAllShell` 設定，啟用後所有 Bash/PowerShell 指令都會路由至 auto-mode 分類器，而非只有任意程式碼執行（arbitrary code execution）模式才路由。

**為何熱：** 讓 auto-mode 對 shell 指令有更完整的分類覆蓋，使用 auto-mode 的工程師可獲得更一致的指令路由行為。

**快速上手：**
```json
{
  "autoMode": {
    "classifyAllShell": true
  }
}
```
在 `settings.json` 或 `~/.claude/settings.json` 中加入以上設定。

**注意事項：** 僅對使用 auto-mode 的場景有效；若未啟用 auto-mode，此設定無影響。

---

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
**發布：** 2026-06-09 | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布（2026-07-01 出口管制已解除，全球恢復存取）

> **2026-07-01 更新：** 出口管制已解除，全球恢復存取；Pro/Max/Team 用戶 7/7 前享 50% 配額。詳見 [[entities/fable-5]] 與 [[topics/anthropic-government-policy]]。
> **2026-06-29 更新（歷史）：** Anthropic 正式獲美國政府許可，可向特定信任合作夥伴恢復 Mythos 存取（[qz.com](https://qz.com/anthropic-mythos-5-clearance-trusted-partners-commerce-062926)）；Axios 報導 Fable 5「可能本週內回歸」。
> **2026-06-13 更新（歷史）：** 美國政府出口管制指令，Anthropic 於當日 5:21pm ET 對全體用戶停用 Fable 5 與 Mythos 5。其他模型（Opus 4.8、Sonnet 4.6 等）不受影響。

**是什麼：** Anthropic 首款向大眾開放的 Mythos 級模型。Fable 5 = Mythos 5 模型權重 + 安全分類器護欄，觸發時靜默 fallback 至 Opus 4.8（< 5% session）。定價 $10/$50 per million token，context 1M，max output 128K。

**為何熱：** HN 2,448 分，近 2,000 評論。幾乎所有 benchmark SOTA，任務越長期越複雜優勢越大。首次讓開發者在一般工作流中使用 Mythos 等級推理能力。

**注意事項：** 2026-07-01 起出口管制已解除，全球恢復存取；Pro/Max/Team 用戶 7/7 前享 50% 配額，之後配額政策待確認。詳見 [[entities/fable-5]]。

---

> 2026-05 功能詳細條目已封存，見 [[feature-radar-archive-2026-05]]

