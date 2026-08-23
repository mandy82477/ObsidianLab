---
page: "topics/anthropic-commitments"
kind: "topic"
status: "monitoring（29 天無新兌現動態，追蹤項目均無官方後續，持續低頻觀察）"
domain: "🏛️ 政策/安全"
last_updated: "2026-08-08"
last_news_update: "2026-07-10"
status_main: "monitoring"
days_since_news: 44
inbound_links: 8
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
# Anthropic 承諾兌現追蹤

**狀態：** monitoring（29 天無新兌現動態，追蹤項目均無官方後續，持續低頻觀察）
**領域：** 🏛️ 政策/安全
**開始日期：** 2026-07-03
**最後更新：** 2026-08-08
**最後新聞更新：** 2026-07-10

> **最新動態**（2026-07-10，議題持續低頻觀察）
> 「spyware 指控回應」持續升級：繼 07-07 Anthropic 將「隱藏追蹤器」定調為內部「實驗」後，中國官方於 07-08 正式發布「後門」資安警示，與「實驗」定調正面矛盾；Anthropic 於 07-10 首度公開反駁中國官方「後門」框架本身。雙方仍各執一詞，均無第三方驗證，完整逐日時序見 [[topics/safety-china-trust-dispute]]（該頁維持 monitoring）。隱寫術修復（07-01 承諾）修復版仍未發布。**截至 2026-08-08 複查，五項追蹤中承諾持續均無新官方動作**（隱寫術修復、Agent SDK 計費切割重啟、HERMES.md 退款均維持原狀，近 14 天 news 亦無相關後續），故本頁維持 monitoring；若任一項出現官方新動作將立即恢復 ongoing。

---

## 摘要

本頁回答一個問題：**「Anthropic 說過要做的事，做了嗎？」** 官方每次承諾修復、承諾政策、或明確拒絕時，在此建檔追蹤後續；狀態有變化時會即時更新。已兌現或已死案的條目移入「已結案」。

**狀態符號：** 🔴 未兌現 / 🟡 部分兌現 / ✅ 已兌現 / ⛔ 明確拒絕（不會做）/ ❓ 待官方回應

## 追蹤中

| 承諾 / 表態 | 承諾日 | 目前狀態 | 最後檢查 | 說明 |
|------------|--------|---------|---------|------|
| **修復隱寫術（同形字符替換）機制** | 2026-07-01 | 🔴 未兌現 | 2026-07-02 | HN 2263 分爭議後官方承諾修復；修復版尚未發布，07-02 爭議還升級為 spyware 指控 |
| **解禁三承諾**（主動偵測安全風險 / 配合標準協議 / 通報惡意活動） | 2026-07-01 | 🟡 部分兌現 | 2026-07-02 | 07-02 Defense in Depth 分類器為「主動偵測」首次具體落實，但首日即有誤判實測；另兩項尚無公開動作 |
| **spyware 指控回應**（v2.1.91+ 代理偵測） | — | 🟡 已回應（爭議持續升級） | 2026-07-10 | Anthropic 07-07 首度回應定調「實驗」；07-08 中國官方正式發布「後門」資安警示，與「實驗」定調正面矛盾；07-10 Anthropic 首度公開反駁中國官方「後門」框架本身；雙方仍各執一詞，均無第三方驗證；完整逐日時序見 [[topics/safety-china-trust-dispute]] |
| **Agent SDK 計費切割政策** | 2026-06-16 暫停 | 🟡 暫停中 | 2026-07-01 | 社群反彈後政策暫停，未撤回也未重啟；重啟與否影響所有 SDK 使用者 |
| **HERMES.md 計費路由 bug** | 2026-04-25 確認 | 🔴 確認 bug 但拒絕退款 | 2026-06-30 | 官方確認為 bug；已知損失 $200 未退，修復狀態不明 |

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
