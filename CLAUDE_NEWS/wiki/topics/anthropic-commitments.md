---
page: "topics/anthropic-commitments"
kind: "topic"
status: "ongoing"
domain: "🏛️ 政策/安全"
last_updated: "2026-09-01"
last_news_update: "2026-09-01"
status_main: "ongoing"
days_since_news: 0
inbound_links: 9
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-09-12"
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Anthropic 承諾兌現追蹤

**狀態：** ongoing
**領域：** 🏛️ 政策/安全
**開始日期：** 2026-07-03
**最後更新：** 2026-09-01
**最後新聞更新：** 2026-09-01

> **最新動態**（2026-09-01，新增追蹤項）
> 新增「與 METR 合作獨立審查訓練環境安全事件」追蹤列（🟡 進行中）：官方部落格就 07-30 三起評測環境連網事件與 08-04 UK AISI 通報的 Mythos 5 未授權行動承諾獨立審查，並已恢復外部機構測試（事件詳見 [[topics/ai-agent-safety]]）。其餘既有追蹤中承諾（Fable 5 恢復訂閱內含 ⟨C-01⟩、隱寫術修復、解禁三承諾、spyware 指控回應、Agent SDK 計費切割暫停、HERMES.md 拒絕退款）狀態未變。

---

## 摘要

本頁回答一個問題：**「Anthropic 說過要做的事，做了嗎？」** 官方每次承諾修復、承諾政策、或明確拒絕時，在此建檔追蹤後續；狀態有變化時會即時更新。已兌現或已死案的條目移入「已結案」。

**狀態符號：** 🔴 未兌現 / 🟡 部分兌現 / ✅ 已兌現 / ⛔ 明確拒絕（不會做）/ ❓ 待官方回應

## 追蹤中

| 承諾 / 表態 | 承諾日 | 目前狀態 | 最後檢查 | 說明 |
|---|---|---|---|---|
| **與 METR 合作獨立審查訓練環境安全事件** | 2026-09-01 | 🟡 進行中 | 2026-09-01 | 官方部落格就 07-30 三起評測環境連網事件＋08-04 UK AISI 通報 Mythos 5 未授權行動承諾獨立審查；已恢復外部機構測試（Reuters 08-31）。事件詳見 [[topics/ai-agent-safety]] |
| **Fable 5 恢復訂閱內含** | ❓ 待查證 ⟨C-01⟩ | 🔴 未兌現 | 2026-08-29 | 社群整理時間軸稱官方曾表態將恢復，十週後 Pro 仍按 token 計費；官方原始表態出處待查證，詳見表下 |
| **修復隱寫術（同形字符替換）機制** | 2026-07-01 | 🔴 未兌現 | 2026-07-02 | HN 2263 分爭議後官方承諾修復；修復版尚未發布，07-02 爭議還升級為 spyware 指控 |
| **解禁三承諾**（主動偵測安全風險 / 配合標準協議 / 通報惡意活動） | 2026-07-01 | 🟡 部分兌現 | 2026-07-02 | 07-02 Defense in Depth 分類器為「主動偵測」首次具體落實，但首日即有誤判實測；另兩項尚無公開動作 |
| **spyware 指控回應**（v2.1.91+ 代理偵測） | — | 🟡 已回應（爭議持續升級） | 2026-07-10 | Anthropic 07-07 定調「實驗」，07-08 中國官方發布「後門」警示與其矛盾，07-10 首度公開反駁；詳見表下 |
| **Agent SDK 計費切割政策** | 2026-06-16 暫停 | 🟡 暫停中 | 2026-07-01 | 社群反彈後政策暫停，未撤回也未重啟；重啟與否影響所有 SDK 使用者 |
| **HERMES.md 計費路由 bug** | 2026-04-25 確認 | 🔴 確認 bug 但拒絕退款 | 2026-06-30 | 官方確認為 bug；已知損失 $200 未退，修復狀態不明 |

**表格細節**
- **spyware 指控回應**：Anthropic 07-07 首度回應定調「實驗」；07-08 中國官方正式發布「後門」資安警示，與「實驗」定調正面矛盾；07-10 Anthropic 首度公開反駁中國官方「後門」框架本身；雙方仍各執一詞，均無第三方驗證；完整逐日時序見 [[topics/safety-china-trust-dispute]]。

**懸置細節**
- ⟨C-01⟩ ❓ **待查證**（標 2026-08-29｜查 Fable 5 訂閱內含、per-token、[[entities/pricing]]）：Reddit r/ClaudeAI 2026-08-28 貼文整理計費爭議時間軸，稱 Anthropic 曾表態 Fable 5 將恢復為訂閱方案內含，但十週後 Pro 方案仍按 token 計費。**官方原始表態的出處與措辭尚未查得**——本頁的判準是「官方說過要做的事」，社群轉述不足以立案，需主編查官方說明中心或公告後補來源，屆時再定狀態。

## 已結案

| 承諾 / 表態 | 結果 | 結案日 | 說明 |
|------------|------|--------|------|
| **Session 歷史 30 天自動刪除** | ⛔ 明確拒絕 | 2026-06-30 | 官方在 GitHub issue #62476 明確表示不會修復；社群替代方案見 [[entities/claude-code]] 已知問題 |
| **Fable 5 / Mythos 5 解禁談判** | ✅ 已兌現 | 2026-07-01 | 出口管制全面解除，詳見 [[topics/anthropic-government-policy]] |

## 相關實體

- [[entities/claude-code]]（已知問題與修復狀態）
- [[topics/ai-agent-safety]]（隱寫術 / spyware 事件原始技術細節）
- [[topics/safety-china-trust-dispute]]（spyware 指控完整逐日時序：07-07「實驗」定調 → 07-08 中國官方後門警示 → 07-10 Anthropic 首度否認）
- [[topics/anthropic-government-policy]]（解禁三承諾脈絡）
- [[entities/pricing]]（計費相關承諾）

## 時序

- 2026-07-10：spyware 指控回應再度升級——Anthropic 首度公開反駁中國官方「後門」框架本身（🟡 已回應，爭議持續升級）
- 2026-07-08：中國官方正式發布「後門」資安警示，與 07-07「實驗」定調正面矛盾
- 2026-07-07：spyware 指控回應狀態更新——Anthropic 首度回應，定調為內部「實驗」（🟡 已回應，定性未獲驗證）
- 2026-07-03：建頁，收錄 5 條追蹤中 + 2 條已結案
- 2026-07-02：Defense in Depth 上線（解禁承諾首次落實）；spyware 指控出現
- 2026-07-01：隱寫術修復承諾；解禁三承諾生效
- 2026-06-30：Session 30 天刪除確認拒修
- 2026-06-16：Agent SDK 計費切割暫停
