---
page: "entities/opencode"
kind: "entity"
type: "product"
status: "active（快速成長）"
domain: "🛠️ 工具/功能"
last_updated: "2026-08-27"
last_news_update: "2026-05-22"
status_main: "active"
days_since_news: 107
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 107
inbound_links: 6
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# OpenCode

**類型：** product
**狀態：** active（快速成長）
**領域：** 🛠️ 工具/功能
**首次出現：** 2026-04-27
**最後更新：** 2026-09-05
**最後新聞更新：** 2026-05-22

> **最新動態**（2026-05-22）
> XDA 正式評為 Claude Code 的可行開源替代方案，同期 `OpenCode-power-pack` 完成移植官方 11 個 skills。

---

## 現況

**最新動態（2026-05-22）：** XDA 正式評為 Claude Code 的可行開源替代方案，同期 `OpenCode-power-pack` 完成移植官方 11 個 skills；截至目前（最後新聞更新 2026-05-22）無更新後續報導。

OpenCode 是 Claude Code 的主要開源替代品，截至 2026-05-12 已吸引 **157,000 名開發者**轉向（The New Stack 報導）。功能與體驗被 XDA 評測認為與 Claude Code 相當，且完全開源免費。即便 Anthropic 宣布倍增速率限制，對 vendor lock-in 的顧慮仍持續驅動開發者轉向開源方案。

另有 tech-insider.org（Google News 轉載，2026-08-01）稱 OpenCode 下載量達 Claude Code 的 **5.4 倍**（比較定價 Free vs $20）。🔎 **查無官方**（標 2026-08-10｜查 tech-insider.org、OpenCode 下載量｜複 2026-09-13）：此下載量倍數之統計方法與時間範圍，查證後仍未見揭露。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ✅ 廣泛採用 |
| 最適合 | 成本敏感開發者、希望避免 vendor lock-in 的團隊、需要開源方案的使用者 |
| 不適合 | 依賴 Anthropic 官方整合深度功能的場景 |

> 詳細最新熱度見 [[feature-radar]]

---

## 核心功能

- **開源免費**：無訂閱費，對成本敏感開發者最直接的替代路徑
- **插件生態**：`OpenCode-power-pack` 已移植 Anthropic 官方 11 個 Claude Code skills（代碼審查、安全審計、前端設計等），打破官方插件的工具綁定限制
- **社群整合**：`claude-anyteam` 工具已讓 OpenCode 代理加入 Claude Code Agent Teams，實現跨工具協作
- **競爭定位**：XDA 於 2026-05 正式評為 Claude Code 的可行替代方案，直接回應 OpenClaw 禁令後的替代需求

---

## 分流背景

OpenCode 的成長發生在幾個推力同時出現的時間點：
1. **OpenClaw 禁令**（2026-04 底）：Anthropic 對第三方 agentic 工具的限制引發開源替代需求
2. **6/15 計費調整**：`claude -p` 改按全額 API 費率計費，推動尋找低成本替代
3. **Claude Code 效能退步事件**（2026-03～04）：品質下滑期間開發者開始評估替代方案

---

## 相關實體

- [[topics/competitor-landscape]]（主要競品分析）
- [[entities/openclaw]]（OpenClaw：Anthropic 限制後促成 OpenCode 需求的前置事件）
- [[entities/pricing]]（計費調整是分流動因之一）
- [[topics/code-quality-decline]]（效能退步期間開發者評估替代方案）

---

## 參考來源

- [[news/2026-04-27]]
- [[news/2026-05-12]]
- [[news/2026-05-22]]
- [The New Stack 報導（157K 開發者）](https://thenewstack.io/)

---

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-05-22 | XDA 評為可行替代方案；`OpenCode-power-pack` 移植官方 11 個 skills；DeepSeek 宣布建構自有競品，顯示開源 Claude Code 競品格局持續擴大 |
| 2026-05-12 | The New Stack 報導 157,000 名開發者里程碑；Anthropic 宣布倍增速率限制後 vendor lock-in 顧慮仍驅動轉移 |
| 2026-04-27 | 首次出現社群討論，OpenCode-power-pack 移植 Anthropic 官方 skills |
