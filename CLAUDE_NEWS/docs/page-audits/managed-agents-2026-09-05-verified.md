# 主編官方查證記錄：managed-agents（2026-09-06 查證）

設計者無 web 工具，定稿刻意留空官方 URL 與計費數字、標為需主編查證。本檔是主 session 以 WebFetch 對官方一手來源查證的結果，實作時逐字取用；每條附來源 URL 與查證日，歸因 slug `user-query`（主編查證通道，見 `./CLAUDE.md`「使用者提問」列）。

## 1. 狀態：仍是 beta，不是「正式發布」（**事實更正**）

- 來源：<https://platform.claude.com/docs/en/managed-agents/overview>（2026-09-06 查證）
- 原文：「Claude Managed Agents is in beta. All Managed Agents endpoints require the `managed-agents-2026-04-01` beta header. … Access to Claude Managed Agents (enabled by default for all API accounts)」
- 影響：本頁標頭 `狀態：active（正式發布）`、feature-radar L226「正式發布」、index L56 皆須改為 **beta（所有 API 帳號預設可用，須帶 beta header）**。健檢卡與設計者都沒抓到——他們無 web 工具，這正是主編查證存在的理由。
- 同頁其他可直接用的事實：
  - 定位句：「Pre-built, configurable agent harness that runs in managed infrastructure. Best for long-running tasks and asynchronous work.」；與 Messages API 的官方對照表（What it is／Best for）
  - 四個核心概念：Agent／Environment（雲端沙箱或自架沙箱）／Session／Events
  - 官方列的適用情境：長時執行（分鐘到小時）、雲端沙箱、自架沙箱（合規／資料落地）、免自建 agent loop、有狀態 session、排程執行（scheduled deployments）
  - **不適用 Zero Data Retention 與 HIPAA BAA**（因 session 狀態存在伺服器端）——這是選型分界「執行位置／合規」軸的官方依據
  - MCP tunnels 與 dreaming 為「更受限的 research preview」，須另外申請：<https://claude.com/form/claude-managed-agents>
  - 亦可在 Claude Platform on AWS 使用，功能可用性與 session 行為有差異

## 2. 計費：官方有明文，可直接取代設計者的懸置 ⟨Q-03⟩

- 來源：<https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing>（2026-09-06 查證）；`managed-agents/pricing` 子頁為 404，計費住通用定價頁
- 兩個維度：**token**（依模型牌價，快取乘數同樣適用；session 內 web search 另計 $10／1,000 次；`inference_geo: "us"` 1.1×；fast mode 溢價適用）＋ **session runtime $0.08／session-hour**（只計 `running` 狀態，`idle`／`rescheduling`／`terminated` 不計，毫秒計量）
- **不適用**：Batch API 折扣（有狀態互動、無批次模式）、partner 雲端平台（Bedrock／Vertex 不提供）
- Session runtime **取代** code execution 的 container-hour 計費，不會重複收
- 官方算例：Opus 5 跑 1 小時、50k 輸入／15k 輸出 → $0.25＋$0.375＋$0.08 ＝ **$0.705**；若 40k 輸入為快取讀取 → **$0.525**
- 落點：本頁選型分界表「計費」軸一格＋`entities/pricing.md`「當前生效的計費規則」加一條（商業記者頁，但此為主編查證通道，可直接寫入並標查證日）。設計者開給商業記者的 handoff 改為「已由主編查證寫入，請複核」而非「請查證」

## 3. Dreaming：research preview、須申請、另一個 beta header

- 來源：<https://platform.claude.com/docs/en/managed-agents/dreams>（2026-09-06 查證）
- 原文：「Dreaming is a research preview feature. Request access to try it.」；「Dream endpoints are gated by the `dreaming-2026-04-21` beta header; the `managed-agents-2026-04-01` header on its own doesn't grant access」
- 是什麼（一句）：非同步工作，讀既有 memory store＋1–100 個過去 session 的 transcript，產出**新的**、去重／更新／萃取洞見後的 memory store；輸入 store 不被改動
- 計費：依所選模型的標準 API token 費率，無另計；支援 `claude-opus-5`／`fable-5`／`opus-4-8`／`opus-4-7`／`sonnet-5`／`sonnet-4-6`
- 對冷讀者 Q4「Dreaming 對我有什麼用」的誠實答案：**要先在用 memory store、且申請到 research preview**；一般 Claude Code 使用者現在碰不到——頁面要直說
- 順帶解掉本頁既有懸置 ⟨Q-01⟩（「dreaming API 是否對應 Dreaming 記憶整合功能」，標 2026-08-10）：官方 dreams 文件即該功能的 API，**可由主編結案**（5c 權限），改寫為事實並移除標記

## 4. `/goal` 與 Agent View：官方 changelog 可證，作為最小用法的官方連結

- 來源：<https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md>（2026-09-06 查證）
- `/goal` 命中 2.1.239（check-in 退避 30 分→1 小時→每 2 小時；`--resume` 恢復 active goal）、2.1.243（idle session 每個 goal 至多三次 check-in）
- Agent View 命中 2.1.246／2.1.247（`claude agents` 修復項）
- code.claude.com 文件站的 slash-commands 頁**未收錄** `/goal`（2026-09-06 抓取重導至 skills 頁，零命中）——所以「官方文件連結」給 changelog，不給文件站；頁面上寫「官方文件尚未收錄，以 changelog 為據」
- 本頁原寫 `/goal`「v2.1.139+」：changelog 最早命中為 2.1.239，**v2.1.139 的出處待核**——實作時若庫內 `entities/claude-code.md` 版本表查得到 2.1.139 有 `/goal` 條目就保留，查不到改「2.1.239 前已存在（首見版次待核）」，不硬寫

## 5. 尚未查證（不寫入，留懸置或不提）

- Managed Agents 在 Claude Platform on AWS 的功能差異細節（overview 只說「有差異」）
- 第三方生產採用回饋（官方文件不會有；冷讀者 Q2 的「有沒有人在用」仍為零，頁面照實寫）
