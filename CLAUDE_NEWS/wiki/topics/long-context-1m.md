---
page: "topics/long-context-1m"
kind: "topic"
status: "ongoing"
domain: "🛠️ 工具/功能"
last_updated: "2026-08-31"
last_news_update: "2026-08-31"
status_main: "ongoing"
days_since_news: 0
inbound_links: 8
attribution_count: 2
attribution_last: "2026-08-31"
top_source: "github-issues"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 1M context：加不加價、你能不能關

**狀態：** ongoing
**領域：** 🛠️ 工具/功能
**別名：** 1M context window, long context, `[1m]`
**開始日期：** 2026-04-10
**最後更新：** 2026-08-31
**最後新聞更新：** 2026-08-31

> **最新動態**（2026-08-30）
> 使用者回報選用 opus-plan 模型時，即使已達成 1M context 資格仍被要求另開用量額度（#61869）——「資格達成」與「計費閘門」互相打架的訊號再添一筆，繼「狀態列顯示不準」（08-29，#61734，24 則留言）與「Pro 預設開啟關不掉」（08-25，62 則留言）之後。三者官方均未回應。

---

## 摘要

官方說 Claude 4.6 以後的 1M context **不加價**——這句話是對的，但它只回答了三個問題裡的一個。另外兩個是「**我手上是不是舊世代**」（舊世代超過 200K 要付兩倍輸入價）與「**我能不能決定要不要開**」（Pro 預設開啟且關不掉、選定的 1M 變體會從選單消失）。

本頁把這三件事收在一起。**單一數字的計費規則**在 [[entities/pricing]]，**模型怎麼選**在 [[topics/model-comparison]]，本頁只回答「1M 這個旋鈕本身」。

## 你的 1M 會不會加價

| 你在用的 | 超過 200K 時 | 依據 |
|---|---|---|
| Claude 4.6 以後（Fable 5／Opus 5／Sonnet 5／Sonnet 4.6）| **不加價**，900k 與 9k 同費率 | 官方定價頁 Long context pricing（2026-08-29 查證）|
| Sonnet 4／4.5 世代 | **×2.0 輸入、×1.5 輸出** | 該世代 1M 為 public preview（AWS 公告）|
| Haiku 4.5 | 不適用——上限 200K | 官方模型總覽頁（2026-08-20 查證）|

**分界是模型世代，不是「1M」這個功能。** 這也是為什麼在 Amazon Bedrock 的模型清單裡，同一個家族會同時出現 1M 與 200K 兩種條目並列——那不是兩個等級的方案，是兩個世代的模型放在同一頁。兩代混用時，**兩套規則會出現在同一份帳單上**。

乘數全表（快取、Batch、資料落地、地區端點如何互相疊乘）見 [[entities/pricing]] 的「通路與乘數」；「換個模型同一份工作差多少」見 [[topics/model-comparison#同一份工作，換設定差多少]]。

## 你控制不了的地方

即使費率不加價，**你是否走在 1M 上這件事本身不完全由你決定**——四條獨立的社群回報指向同一個缺口，而最後一條讓前三條更難自救：**你連自己現在在不在 1M 上都看不準**。

| 現象 | 證據 | 狀態 |
|---|---|---|
| **預設開啟、找不到關閉方式**（Pro）| 62 則留言、44 個讚，2026-08-25 | 🔴 官方未回應 |
| **選定狀態保不住**——1M 變體從 model picker 消失，session 中途被降級 | [#46221](https://github.com/anthropics/claude-code/issues/46221)，2026-04-10 開立 | ❓ 以 duplicate 關閉（關聯 #45978），全程無官方留言確認修復 |
| **`[1m]` 後綴自成一個模型 id**，會影響配額判定 | 受影響帳號存的是 `claude-fable-5[1m]`；[#79337](https://github.com/anthropics/claude-code/issues/79337) Max 誤判需買 credits | 官方 07-20 定性為誤判，社群回報延燒至 08-07 |
| **你看不出自己在不在 1M 上**——狀態列對 Sonnet 4.6 顯示 200k，而該模型實際支援 1M | [#61734](https://github.com/anthropics/claude-code/issues/61734)，24 則留言，2026-08-29 | 🔴 官方未回應 |
| **已達 1M 資格仍要求另開用量額度**（opus-plan 模型）| [#61869](https://github.com/anthropics/claude-code/issues/61869)，2026-08-30 開立 | 🔴 官方未回應 |

各條的完整脈絡：第一、二、四條見 [[entities/claude-code]] 的已知問題，第三條見 [[entities/fable-5]]。模型釘選／靜默降級的跨機制敘事見 [[topics/code-quality-decline]]。

> **這件事對成本估算的意義：** 任何「我選了 X 模型所以會花 Y」的估算，都預設了「我選的算數」。上表三條說明這個前提有缺口，估算前先確認釘選是否成立。

## 帳單對不上時怎麼判

| 症狀 | 最可能的原因 |
|---|---|
| 價差**只在大請求**出現 | 舊世代（Sonnet 4／4.5）的長脈絡溢價 |
| **小請求也貴同樣比例** | 資料落地（`inference_geo:"us"`）或地區端點，各 ×1.1 |
| 儀表板顯示 **0% 訂閱用量卻仍被收費** | 1M context 走獨立 API 計費通道——2026-05-11 有實例，0% 用量下遭收取 $3.37 Extra Usage |
| 雲端環境（CI/CD、Docker、K8s）整批走 API 計費 | `ANTHROPIC_API_KEY` 環境變數存在時，所有呼叫自動改走 API 通道而非訂閱配額 |

後兩列的完整規則見 [[entities/pricing]] 的「當前生效的計費規則」。

## 相關實體

- [[entities/pricing]] — 費率、乘數、通路：單一數字的來源
- [[topics/model-comparison]] — 我該用哪個模型，含跨世代實付成本換算
- [[entities/claude-code]] — 預設開啟與 model picker 兩條已知問題
- [[entities/fable-5]] — `claude-fable-5[1m]` 與 #79337
- [[topics/code-quality-decline]] — 模型釘選／靜默降級訊號群

## 時序

### 2026-08-30
[#61869](https://github.com/anthropics/claude-code/issues/61869)：使用者回報選用 opus-plan 模型時，即使已達成 1M context 使用資格，仍被要求另開用量額度（Usage credits）才能使用——與既有「`[1m]` 後綴自成模型 id 影響配額判定」（#79337）同屬資格與計費閘門不一致，涉及模型不同，暫分列追蹤。

### 2026-08-29
[#61734](https://github.com/anthropics/claude-code/issues/61734)：context window 狀態列對 Sonnet 4.6 顯示 200k 上限，但該模型實際支援 1M（24 則留言）——**顯示與實際不符，使用者無從確認自己是否在 1M 上**。

### 2026-08-25
Pro 方案新開 session 預設開啟 1M 且找不到關閉方式（62 則留言、44 個讚），官方尚未回應。

### 2026-07-20
Fable 5 免費期到期當天，Max 方案一度被誤判需購買 usage credits 才能執行 Fable 5，受影響帳號的已儲存模型為 `claude-fable-5[1m]`（[#79337](https://github.com/anthropics/claude-code/issues/79337)）；官方當日定性為誤判並建議重啟，社群回報延燒至 08-07。

### 2026-07-01
Claude Code v2.1.197 將 Sonnet 5 設為預設模型，所有新 session 原生享有 1M context——**1M 由選項變成預設**，這是後續「關不掉」問題的起點。

### 2026-06-11
v2.1.173 修正模型名稱含 `[1m]` 後綴時無法正規化的問題（Fable 5 預設含 1M，後綴自動移除）。

### 2026-05-11
使用者在儀表板顯示 0% 訂閱用量的情況下遭收取 $3.37 Extra Usage，歸因於 1M context 觸發獨立 API 計費通道。

### 2026-04-10
[#46221](https://github.com/anthropics/claude-code/issues/46221) 開立：Opus 4.6 1M context 從模型選單消失被 200K 變體取代，預設無預警切為 Sonnet，進行中 session 被中途降級；以 duplicate 關閉（關聯 #45978），該 issue 雖標記 `completed` 但全程無官方或協作者留言確認修復方式。
