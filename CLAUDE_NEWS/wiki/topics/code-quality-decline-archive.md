---
page: "topics/code-quality-decline-archive"
kind: "topic"
status: "resolved（封存頁）"
domain: "🌐 社群"
last_updated: "2026-09-07"
last_news_update: "2026-05-29"
status_main: "resolved"
days_since_news: 103
parent: "topics/code-quality-decline"
children: "[]"
page_role: "archive"
days_since_news_subtree: 103
inbound_links: 0
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
# Claude Code 效能退步事件 · 原始條目

**狀態：** resolved（封存頁）
**領域：** 🌐 社群
**上層：** [[topics/code-quality-decline]]
**開始日期：** 2026-03
**最後更新：** 2026-09-07
**最後新聞更新：** 2026-05-29

> 本頁是原始條目的存放處，重點層見 [[topics/code-quality-decline]]。

---

## 2026-05

#### 2026-05-29

- **Opus 4.7 升版前一週效能下降（MarginLab SWE-bench-Pro 追蹤）**：MarginLab 每日對 Claude Code 執行 SWE-bench-Pro 追蹤，發現 Opus 4.7 在 [[entities/opus-4-8|Opus 4.8]] 發布前**連續五天**呈現統計顯著的 pass rate 下降，發布後立即恢復。此為「靜默的日常效能變化」模式的又一次文件化案例——launch benchmark 只呈現發布當下數字，無法捕捉前後的漸進變化（來源：https://marginlab.ai/blog/claude-code-degraded-before-opus-4-8/）
- **thinking blocks 400 錯誤**：Opus 4.8 升版後，多名用戶回報 `API Error: 400 thinking or redacted_thinking blocks cannot be modified` 錯誤；v2.1.156 已修復，workaround 為 `/exit` 後 resume session（見 [[entities/claude-code]]）
- **4.8 行為退步投訴**：部分用戶反映 Opus 4.8 比 4.7 更差——obsessive tool use，傾向以 "pecl scripts" 處理簡單文件操作（來源：Reddit r/ClaudeAI）

#### 2026-05-21
- **Opus 退化三週結構化記錄**：用戶以三週結構化 session log（含 metacognitive 欄位）記錄 Opus 4.7 / Sonnet 4.6 在複雜本地 AI 記憶體專案（Qdrant + Neo4j + Graphiti）上的持續失敗，並記錄到競品模型成功捕捉 Claude 遺漏的錯誤；是目前 r/ClaudeAI 最具文件支撐的退化投訴案例，Anthropic 未回應

#### 2026-05-09
- **靜默模型切換（11.5 倍效率差距）**：開發者持續 36 天記錄 Claude Code 使用數據，量化出不同模型間 11.5 倍的效率差距，並觀察到模型有時靜默切換（silent model switching）且無明確通知；對有成本意識的長期用戶是重要的監控警示，建議搭配 Throttle Meter 或 session log 監控實際模型使用情況

#### 2026-05-05
- **Opus 4.7 退步討論再升溫**：dev.to 文章《Claude Opus 4.7 Is a Regression》引發討論，部分開發者聲稱 Opus 4.7 在編碼任務中不如 4.6，已主動回退舊版；與 4/30 的「後設化退步」批評相互呼應；見 [[entities/opus-4-7]]

#### 2026-05-03
- **[社群問責] 4/23 事後報告 50+ 修復社群獨立驗證**：社群開發者主動逐一驗證 Claude Code 負責人 Boris Cherny 在 4/23 發布的事後報告中承諾的超過 50 項修復，提供獨立於官方的實測評估。此為少見的社群對官方承諾進行系統性問責的行動，驗證結果正逐步揭露哪些修復已落實、哪些仍有差距。

## 2026-03～04

#### 2026-04-30
- **Opus 4.7「後設化」退步**：重度 Max 20x 用戶直言 Opus 4.7 嚴重退步，過度「後設化」無法直接回答問題；當時另引學術研究（arxiv 2604.24827）稱 Opus 4.7 參數約 4T、少於 Opus 4.6 的 5.3T，**該組數字經 2026-08-26 查證論文原文後不成立**（論文未給 Opus 4.7 估算，見 [[entities/opus-4-7]]），本則僅保留「社群失望情緒累積」此一社群訊號
- **Claude Projects 對話消失**：重度使用者三度遭遇整天的創作對話無故消失，無法搜尋找回，呼籲改善 Projects 資料保留機制

#### 2026-04-29
- **Speed Bumps 頻率增加**：多位長期使用者回報 Claude Code 本週起明顯增加中途暫停詢問的頻率，即使簡單任務也頻繁打斷工作流程，社群猜測與系統層級的行為調整有關，但目前無官方說明
- **Max 方案 API 錯誤**：高價訂閱用戶遭遇內部 API 錯誤，Anthropic 支援 AI 卻持續建議排查 VPN 等不相關問題，無法識別實際服務故障，引發對支援品質的強烈批評

#### 2026-04-28
- **「Anthropic 安全定義過窄」批評**：Jonathan Nen 發文指出 Anthropic 的安全關注過度聚焦在模型行為，忽視產品可靠性、定價策略與溝通透明度；以四月 Claude Code 品質問題與 Pro 用戶 Opus 存取爭議為佐證，文章在技術社群引發強烈共鳴，HN 登上精選話題。
- **信任侵蝕進入結構性階段**：定價不透明（Opus 圍牆事件）+ 使用量計量異常 + 基礎設施可靠性問題（Auto Compact 失效、Prompt Cache Race Condition）在同日密集出現，社群對平台可靠性的質疑已超出「效能退步」的原始邊界，擴大為對 Anthropic 整體產品治理的不信任。

#### 2026-04-25
- 社群推出 **CC-Canary** 工具，透過讀取 `~/.claude/projects/` JSONL session log 自動偵測效能漂移，提供 HOLDING / SUSPECTED REGRESSION / CONFIRMED REGRESSION 等判定等級（工具目錄見 [[topics/community-tech-tools]]）

#### 2026-04-24
- **Anthropic 正式公開說明**：承認工程疏失導致效能退步（Fortune、XDA 等媒體同步報導）
- **Stop hooks 失效問題獨立回報**：Claude 4.7 開始無視自訂 stop hooks，屬獨立的行為退步（regression），與效能下滑為不同問題；截至 2026-07-11，[[entities/claude-code]] 已知問題仍將此列為 🔴 未修復（非僅指控）
- HN 討論串累積近 80 則留言

#### 2026-04（早期）
- 大量開發者在 Reddit r/ClaudeAI、Hacker News 回報效能下滑
- 社群質疑是否為刻意調整（RLHF 過度修正、成本考量等），Anthropic 長期未正式回應

#### 2026-03（推測）
- 效能退步開始，早期用戶開始察覺異常
