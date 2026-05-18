// data-sample.js — edit THIS file for content changes; do not edit component JSX for data.
// Components read window.SAMPLE_* at render time.
// Last sync: 2026-05-17

window.SAMPLE_META = {
  lastIngest:       "2026·05·17",      // footer display
  lastIngestFull:   "2026-05-17",      // EntityList hero
  archiveStart:     "2026-03-09",
  archiveEnd:       "2026-05-17",
  archiveDays:      52,
  archiveArticles:  "1,243",
  archiveSources:   "5/5",
};

window.SAMPLE_ENTITIES = [
  { path: "claude-code",       type: "product", state: "active",            stateColor: "success", summary: "Claude Code CLI 主頁：功能、已知問題、社群工具",                                      updated: "2026-05-17" },
  { path: "opus-4-7",          type: "model",   state: "active（爭議）",    stateColor: "warn",    summary: "Opus 4.7 發布細節、思考深度爭議、cache 問題",                                        updated: "2026-05-17" },
  { path: "pricing",           type: "policy",  state: "持續調整",           stateColor: "warn",    summary: "訂閱方案、近期政策變動、token 成本注意事項",                                          updated: "2026-05-17" },
  { path: "mythos",            type: "model",   state: "限制存取",           stateColor: "danger",  summary: "高能力安全模型，七週發現 2,000+ 漏洞",                                               updated: "2026-05-17" },
  { path: "managed-agents",    type: "feature", state: "active（正式）",    stateColor: "success", summary: "官方框架：Dreaming 記憶整合、20 路並行子代理、Outcomes 規格驗證",                    updated: "2026-05-17" },
  { path: "claude-security",   type: "product", state: "public beta",      stateColor: "info",    summary: "資安產品，情境化安全評估，整合於 Claude Code 開發環境",                              updated: "2026-05-17" },
  { path: "openclaw",          type: "product", state: "允許（信用池計費）", stateColor: "warn",    summary: "第三方 agentic 工具，禁令後 6/15 起恢復，改走信用池 API 費率計費",                  updated: "2026-05-17" },
  { path: "google-investment", type: "event",   state: "resolved",         stateColor: "success", summary: "Google 投資 400 億美元歷史紀錄，含循環算力交易結構",                               updated: "2026-05-10" },
  { path: "bugcrawl",          type: "feature", state: "測試中",             stateColor: "info",    summary: "Claude Code 漏洞偵測工具",                                                       updated: "2026-04-26" },
  { path: "claude-design",     type: "feature", state: "active（初期）",   stateColor: "info",    summary: "AI 設計工具，首日反映幻覺多、風格偏移、Claude Code 整合差",                         updated: "2026-04-27" },
  { path: "project-deal",      type: "feature", state: "實驗中",             stateColor: "info",    summary: "代理人自主交易談判實驗，Opus vs Haiku 差異顯著",                                    updated: "2026-04-27" },
  { path: "boris-cherny",      type: "person",  state: "active",            stateColor: "success", summary: "Claude Code 創始人：「Loops 是未來」、「coding is solved」論戰、第三方工具邊界聲明",  updated: "2026-05-17" },
  { path: "cat-wu",            type: "person",  state: "active",            stateColor: "success", summary: "Claude Code 產品負責人：「AI 下一步是主動性 proactivity」",                         updated: "2026-05-17" },
];

window.SAMPLE_TOPICS = [
  { path: "topics/official-community-gap",      state: "ongoing",    stateColor: "warn",    summary: "官方功能 vs 社群痛點缺口矩陣：哪些痛點官方正在解決、哪些結構性缺席" },
  { path: "topics/code-quality-decline",        state: "monitoring", stateColor: "warn",    summary: "Claude Code 效能退步事件，Anthropic 已承認工程疏失" },
  { path: "topics/ai-agent-safety",             state: "ongoing",    stateColor: "warn",    summary: "AI agent 安全：假冒安裝包 + AI 生成程式碼 90% 漏洞 + CVE-2026-39861 + 資料庫刪除事件" },
  { path: "topics/anthropic-government-policy", state: "monitoring", stateColor: "warn",    summary: "Anthropic 政府與軍事政策：五角大廈排除、安全護欄堅持、白宮重啟談判（11 天無新進展）" },
  { path: "topics/competitor-landscape",        state: "ongoing",    stateColor: "info",    summary: "Google 祕密開發競品 + OpenCode 157K 分流 + DeepSeek clone 低成本替代生態" },
  { path: "topics/community-tech-tools",        state: "ongoing",    stateColor: "info",    summary: "社群工具目錄：80+ 工具的活躍度、採用狀態追蹤" },
  { path: "topics/community-tech-patterns",     state: "ongoing",    stateColor: "info",    summary: "社群技術模式：multi-agent、skills 設計、工作流最佳實踐" },
  { path: "topics/community-tech-discussions",  state: "ongoing",    stateColor: "info",    summary: "社群技術討論趨勢：設計哲學辯論、實證研究、架構反思（HTML vs MD、Skill Atrophy 等）" },
  { path: "topics/google-investment",           state: "migrated",   stateColor: "info",    summary: "⚠️ 已遷移至 [[entities/google-investment]]" },
];

// Archive entries — add newest row at the top of each month block.
// Format: { date, dow, tag, title, sub, count }
// tag options: "major" | "track" | "trend" | "tool" | null
window.SAMPLE_ARCHIVE_MAY = [
  { date: "2026-05-17", dow: "sun", tag: "trend", title: "Claude Skills 靜默覆蓋指令，透明度疑慮升溫",
    sub: "Context 管理四工具整理 · claude -p 計費後自動化工作流調適", count: 26 },
  { date: "2026-05-16", dow: "sat", tag: "major", title: "GitHub Copilot 與 OpenCode 157K 星分流加速",
    sub: "多帳號架構合規紅線明確 · Anthropic 未官方回應", count: 33 },
  { date: "2026-05-15", dow: "fri", tag: "major", title: "Anthropic 正式將 claude -p 移出訂閱方案",
    sub: "SDK 計費門檻大幅調整 · 開發者自動化工作流受衝擊", count: 41 },
  { date: "2026-05-14", dow: "thu", tag: "track", title: "OpenClaw 於禁令後以信用池計費方式恢復",
    sub: "Cat Wu：AI 下一步是主動性 proactivity · claude-code stars 121K+", count: 35 },
  { date: "2026-05-13", dow: "wed", tag: "track", title: "Boris Cherny：千支子 agent 徹夜作業",
    sub: "企業成本管理 topic 開設 · OpenCode 競爭態勢加劇", count: 35 },
];

window.SAMPLE_ARCHIVE_APR = [
  { date: "2026-04-30", dow: "wed", tag: "major", title: "Claude Code \"OpenClaw\" 事件暴露 AI 工具的信任危機",
    sub: "白宮介入 Mythos · Anthropic 估值逼近 $9000 億 · Claude Security 公測上線", count: 52 },
  { date: "2026-04-29", dow: "tue", tag: "track", title: "CC 2.1.124 → 2.1.126：system prompt 一進一退 79 tokens",
    sub: "Opus 4.7 thinking-depth 爭議延燒第三日 · Mythos red-team 公布", count: 41 },
  { date: "2026-04-28", dow: "mon", tag: "tool",  title: "Show HN：Nimbalyst — 多 Agent 視覺化工作台",
    sub: "Claude Code、Codex、OpenCode 三家並列 · WYSIWYG diff", count: 38 },
  { date: "2026-04-27", dow: "sun", tag: "major", title: "Claude Code API 金鑰外洩漏洞被媒體報導",
    sub: "版本從 2.1.120 回滾至 2.1.119 · 疑似靜默撤版", count: 47 },
  { date: "2026-04-26", dow: "sat", tag: "major", title: "HERMES.md 計費路由 bug 曝光",
    sub: "git commit 含字串即觸發 API 額外計費 · Anthropic 拒絕退款", count: 44 },
  { date: "2026-04-25", dow: "fri", tag: "track", title: "Anthropic 估值首次突破 $8000 億美元",
    sub: "Google 報導押注 $400 億 · 多家主動出擊", count: 36 },
  { date: "2026-04-24", dow: "thu", tag: "major", title: "Anthropic 正式承認 Claude Code 效能退步源於工程疏失",
    sub: "Stop Hooks regression 被回報 · 影響依賴 hooks 的工作流", count: 39 },
  { date: "2026-04-23", dow: "wed", tag: "trend", title: "「Opus 4.7 可以用一個改變來拯救」貼文衝上 HN 前頁",
    sub: "Max 20x 訂戶集體抱怨「過度後設化」", count: 33 },
  { date: "2026-04-22", dow: "tue", tag: "tool",  title: "anthropic-sdk-typescript v0.91.0 釋出",
    sub: "Managed API 預備 · Claude Managed Agents 基礎設施", count: 28 },
  { date: "2026-04-21", dow: "mon", tag: "track", title: "Mythos 模型存取政策第二輪緊縮",
    sub: "白宮持續關注 · 與五角大廈政策角力", count: 31 },
  { date: "2026-04-20", dow: "sun", tag: null,    title: "週日整理：Bugcrawl 公開測試版安裝筆記",
    sub: "Anthropic 漏洞偵測工具 · 七週發現 2000+ 漏洞", count: 22 },
  { date: "2026-04-19", dow: "sat", tag: "trend", title: "社群開始討論 Claude Code 與 Codex 的代碼風格差異",
    sub: "Reddit 與 HN 三條 thread 同步爆發 · 情緒偏中性", count: 26 },
  { date: "2026-04-18", dow: "fri", tag: "tool",  title: "Show HN：claude-design 首日試用回饋",
    sub: "Anthropic AI 設計工具 · 首日評價偏負面 · 4 件已知問題", count: 35 },
  { date: "2026-04-17", dow: "thu", tag: "track", title: "Opus 4.7 cache 命中率回報異常",
    sub: "重複請求 cache 失效 · 影響高頻 agent 工作流", count: 29 },
];

window.SAMPLE_ARCHIVE_MAR = [
  { date: "2026-03-31", dow: "tue", tag: "major", title: "Anthropic 宣布 Project Deal：Claude 代理人自主交易談判實驗",
    sub: "首次公開 agent-to-agent 商業協議 demo", count: 48 },
  { date: "2026-03-30", dow: "mon", tag: "tool",  title: "MCP Server 註冊表更新：本週新增 18 個社群工具",
    sub: "其中 6 個聚焦於 obsidian / vault 整合", count: 34 },
  { date: "2026-03-28", dow: "sat", tag: "track", title: "Google 投資 $400 億美元正式生效",
    sub: "[[topics/google-investment]] 議題收束 · 移至已解決", count: 41 },
  { date: "2026-03-25", dow: "wed", tag: "trend", title: "「HTML vs Markdown for agent skills」HN 800+ 留言辯論",
    sub: "催生 agent-html-skills 開源工具 · 共識仍未收束", count: 37 },
  { date: "2026-03-22", dow: "sun", tag: null,    title: "Claude Code 2.1.x 系列發布節奏整理",
    sub: "兩週內六次 patch · 多為 hooks 與 token 預算修正", count: 24 },
  { date: "2026-03-20", dow: "fri", tag: "tool",  title: "Opus 4.7 正式發布 · 思考深度可調節參數曝光",
    sub: "thinking-depth 0–4 · 預設 2 · 直接影響 token 計費", count: 52 },
  { date: "2026-03-17", dow: "tue", tag: "track", title: "Bugcrawl 第一次內測通報：七週發現 2000+ 漏洞",
    sub: "包括 OpenSSL、libcurl 與多個 npm 套件", count: 33 },
  { date: "2026-03-14", dow: "sat", tag: "trend", title: "社群開始用 Claude Code 寫 Claude Code 的 plugin",
    sub: "self-hosting agent loop · 風險與想像並陳", count: 28 },
  { date: "2026-03-12", dow: "thu", tag: null,    title: "Anthropic Blog 沉默第 12 天",
    sub: "通常 7–10 天會發 changelog · 社群猜測有大型發布", count: 19 },
  { date: "2026-03-10", dow: "tue", tag: "track", title: "API 定價結構小幅調整 · token 拆分計費 phase out",
    sub: "input / output / cache 三路統一 · 影響企業合約", count: 31 },
  { date: "2026-03-09", dow: "mon", tag: null,    title: "本檔案室啟用首日",
    sub: "5 sources · 26h lookback · LLM-scored ≥3", count: 18 },
];

// Sparkline — one count per day, oldest first. Add new value at the end.
window.SAMPLE_SPARKLINE = [
  18, 24, 31, 22, 19, 28, 33, 30, 27, 33,   // 2026-03-09..03-18
  25, 23, 52, 29, 33, 24, 37, 28, 35, 41,   // 2026-03-19..03-28
  24, 34, 48,                                // 2026-03-29..03-31
  25, 28, 24, 32, 26, 21, 35, 23, 29, 35,   // 2026-04-01..04-10
  26, 28, 30, 22, 25, 19, 29, 35, 26, 22,   // 2026-04-11..04-20
  31, 28, 33, 39, 36, 44, 47, 38, 41, 52,   // 2026-04-21..04-30
  41, 33, 33, 35, 35, 26,                   // 2026-05-13..05-17 (5 latest)
];
