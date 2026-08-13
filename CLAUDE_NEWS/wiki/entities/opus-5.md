---
page: "entities/opus-5"
kind: "entity"
type: "model"
status: "active"
domain: "🤖 模型"
last_updated: "2026-08-12"
last_news_update: "2026-08-12"
status_main: "active"
days_since_news: 1
inbound_links: 25
attribution_count: 14
attribution_last: "2026-08-12"
top_source: "google-news"
pending_count: 2
pending_overdue: 0
pending_next_review: "2026-08-24"
pending_signalled: 0
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Opus 5

**類型：** model
**狀態：** active
**領域：** 🤖 模型
**首次出現：** 2026-07-25
**最後更新：** 2026-08-12
**最後新聞更新：** 2026-08-12

> **最新進展**（2026-07-26）
> Anthropic 於 2026-07-25 正式推出 Claude Opus 5，終結了近兩週的「Opus 5」傳聞（詳見 [[entities/opus-4-8]] 歷史記錄）。定位為 thoughtful and proactive 的新一代模型，在編碼與知識工作評測（Frontier-Bench、GDPval-AA）上逼近 Fable 5 的 frontier intelligence，官方稱定價為 Fable 5 的一半；現為 Claude Max 新預設模型、Claude Pro 最強模型，取代 Opus 4.8 成為次旗艦。資安任務上仍落後 Mythos 5。**07-26 MLQ.ai／PCMag 標題「tops」措辭已查證**：第三方 Artificial Analysis Intelligence Index 上 Opus 5 確以 60.7% 微幅領先 Fable 5 的 59.9%；GDPval-AA v2（1861 Elo，+114）、AA-Briefcase（1720 Elo，+146）亦領先，同時 AA-Briefcase 每任務成本僅 $10.41，較 Fable 5 的 $22.30 低 54%。詳見 [[topics/model-comparison#Benchmark 對照（有來源者才列）]]。

---

## 現況

Anthropic 於 2026-07-25 正式發布 Claude Opus 5，是繼 2026-07-13 起多篇媒體「Opus 5 傳聞」報導後的官方證實版本（詳見 [[entities/opus-4-8]] 「下一代模型觀察」歷史記錄）。官方定位此模型為 thoughtful and proactive，設計目標是**日常可用**且效率優於其他模型，而非單純堆疊評測分數。

**能力定位：** 在編碼與知識工作評測基準 Frontier-Bench、GDPval-AA 上逼近 Fable 5 的 frontier intelligence，是新的 state-of-the-art——但在資安任務上仍落後 [[entities/mythos|Mythos 5]]。相較前代 [[entities/opus-4-8|Opus 4.8]]，官方稱「相同成本下效能大幅提升」，取代 Opus 4.8 成為次旗艦地位。

**日期說明（非矛盾，時區/收錄週期差異）：** 官方公告 RSS 項目時間戳為 2026-07-24 17:00 UTC，[[entities/pricing]] 依此標記發布日為 07-24；本頁與日報同步收錄於 2026-07-25 版面（常見的跨日收錄延遲），故沿用「2026-07-25」作為本頁與 [[topics/model-comparison]] 的記錄日期，兩頁日期差一天為收錄時序差異，非事實矛盾。

**定價定位：** 官方宣稱定價為 Fable 5 的一半（[the-decoder.com](https://news.google.com/rss/articles/CBMixAFBVV95cUxQd3dndnBYZjY0MVBWTjAtNGFYMmFkVUFEUHZmMkZpWVBscjh2VGlRNlJSREdfV3ZmNURtcWVWeTNhYnRudEU3eUhMMkt6bTBRNGRkS2I3WTMwWU5IcmxLdGFXcm56cGJMcmZoWjlpeWdwSjZlRVpRelhFcTkza01tdkZjcGNOQjBKa0JlOFV1bGtRSGJwVkRDb2h3STRKRVN5NEJmM1Q3aVZtUzBRQURlaXpxUENyWHFQZVk0LVBrdUM2QlZm?oc=5)，2026-07-25）；另有 MarkTechPost 報導稱 Opus 5 是在**維持原 Opus 定價**下達到 frontier 級的程式撰寫與電腦操作能力（[Google News/MarkTechPost](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOS0JSUzdUZmhBMVJ3bkFpcXFINFdKalE4NU1YZ1lxSnpBazVRWkl4SUx1RTlEYmI3azJKUFJTbXJGYUxzQTM2UkNjektPMGJxVGdRSTNoSE93SkJZTmFrekFiTjEwdEhxMjZkenBDMGx6cDU0OS1zTzhwWWhpX3RqYWY3TUlCaVg5ZmFJZW5meU04Y09kNDdnTXhjTG1mYXlHTG1hY1lTd3NuUlhwZGJ3VFI0M2VjWUQ2eDF0WVBuYXFuOUVfTTVtRWl6N1A3ZG1DMENraWtCNNIB3AFBVV95cUxPdExPRlliYXRNMjVRVTFJY0xEcFllWjJkdHRmNnNuUDgyMXNOd0VlckNjNmxsaTdpTUtpeklJUEdfMjdGekpPbGl6ZjFTb0tfYVpJbUlEX18tQjlwalQ4amNJcHAwUmZoUm1BWmpLSFY5bS1ibTY1WmlqX0FTUG1LZkdKd01mUjdYSFg0ZFVaNVJ4aHZGaHE1OEM0RHdmUXd6R0dpeVM0SjhPdzF2UTloTTdGaHVpZ2dEUG8wdUIzWmhyQVNnMUtaQ2d4Tk1mMXdCRFdhaXhmcmJ3X3Yz?oc=5)，2026-07-24）。兩則報導對「定價相對前代是否維持不變或砍半」的敘述方向不完全一致，**具體定價數字留給** [[entities/pricing]] 查證彙整。07-26 EdTech Innovation Hub 另有報導標題稱 Opus 5「at same price as Opus 4.8」發布，若屬實則與 MarkTechPost「維持原定價」方向一致，可視為互相呼應的補充訊號——惟本則同樣僅標題級可用，具體 $/Mtok 數字仍待 [[entities/pricing]] 逐項查證。

**07-26 媒體標題「tops」措辭（2026-08-10 第三方基準查證）：** MLQ.ai 標題稱 Opus 5「Tops AI Benchmark Index」、PCMag 標題稱 Opus 5「Tops Fable 5 on Agentic Search」（[MLQ.ai](https://mlq.ai/news/anthropic-launches-claude-opus-5-tops-ai-benchmark-index-at-half-the-cost-of-fable-5/)、[PCMag](https://www.pcmag.com/news/anthropics-newest-ai-model-opus-5-is-now-available)，均 2026-07-26 經 Google News 收錄）。經查證第三方基準 [Artificial Analysis](https://artificialanalysis.ai/articles/opus-5)，「tops」措辭**有事實依據，非誇大**：Opus 5 在 Artificial Analysis Intelligence Index 以 60.7% 微幅領先 Fable 5 的 59.9%（GPT-5.6 Sol 58.9% 居三）；在 GDPval-AA v2（1861 Elo，+114 領先 Fable 5）與 AA-Briefcase（1720 Elo，+146 領先）兩項知識工作基準亦是新龍頭，且 AA-Briefcase 每任務成本僅 $10.41（high 效努力），較 Fable 5 的 $22.30 低 54%。與官方系統卡「逼近但未超越」的框架落差可理解為：官方以自有 Frontier-Bench／GDPval-AA 基準保守表述整體定位，第三方獨立基準則顯示 Opus 5 在多個綜合指數上已實質超車，兩者並非矛盾，而是評測基準與措辭尺度不同。

**預設模型變化：** 現為 Claude Max 新預設模型、Claude Pro 最強模型，取代 Opus 4.8 的角色。

**安全宣稱：** Claude Code 創辦人 Boris Cherny 表示，比起評測分數，更讓他興奮的是 Opus 5 是 Anthropic 目前最難被提示注入（prompt injection）攻破的模型（[simonwillison.net](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything)，2026-07-25）。此為單一人士（Claude Code 創辦人）發布日當天的表態，尚無獨立第三方測試佐證，列為待社群驗證的技術宣稱，人物面向詳見 [[entities/boris-cherny]]。

**SDK 支援：** `anthropic-sdk-python` v0.120.0 與 `anthropic-sdk-typescript` sdk-v0.115.0 已同步加入 `claude-opus-5` model 支援（均為 2026-07-24 發布，早於官方公告數小時，屬常見的 SDK 先行上架模式）。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 日常 agentic 使用、編碼與知識工作任務、Claude Max/Pro 用戶 |
| 不適合 | 資安/滲透測試等安全導向任務（仍不及 Mythos 5）|

> 發布首日資料，社群實測與長期穩定性尚待觀察；詳細最新熱度見 [[feature-radar]]

---

## 核心功能

- **Thoughtful and proactive** 設計理念，目標為日常可用、效率優於其他模型
- **Frontier-Bench、GDPval-AA** 評測逼近 Fable 5 的 frontier intelligence，新的 state-of-the-art
- **資安任務仍落後 Mythos 5**——官方自陳的能力邊界，非全面超越
- **相較 Opus 4.8**：官方稱相同成本下效能大幅提升
- **提示注入抵抗力**：Boris Cherny 稱其為目前最難被攻破的模型（待社群驗證，見上方「安全宣稱」）
- **SDK 支援**：`anthropic-sdk-python` v0.120.0、`anthropic-sdk-typescript` sdk-v0.115.0

---

## 相關議題

- [[entities/fable-5]] — 現任旗艦，Opus 5 於編碼/知識工作評測逼近但未超越其 frontier intelligence
- [[entities/opus-4-8]] — 前代次旗艦，被 Opus 5 取代
- [[entities/mythos]] — 資安任務上仍領先 Opus 5
- [[entities/sonnet-5]] — Claude Code 主力平衡選項，與 Opus 5 分屬不同定位
- [[entities/pricing]] — 定價細節（Fable 5 一半 vs 維持原 Opus 定價，兩說法待彙整查證）
- [[entities/boris-cherny]] — 提示注入抵抗力聲明來源
- [[topics/model-comparison]] — 完整選型對照
- [[feature-radar]] — 功能熱度追蹤

## 參考來源

- [Claude Opus 5 官方公告](https://www.anthropic.com/news/claude-opus-5)（2026-07-24/25）
- [Claude Opus 5 System Card](https://www.anthropic.com/claude-opus-5-system-card)
- [anthropic-sdk-python v0.120.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.120.0)
- [anthropic-sdk-typescript sdk-v0.115.0](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.115.0)
- [MLQ.ai：Tops AI Benchmark Index at Half the Cost of Fable 5](https://mlq.ai/news/anthropic-launches-claude-opus-5-tops-ai-benchmark-index-at-half-the-cost-of-fable-5/)（2026-07-26）
- [PCMag：Tops Fable 5 on Agentic Search](https://www.pcmag.com/news/anthropics-newest-ai-model-opus-5-is-now-available)（2026-07-26）
- [EdTech Innovation Hub：Anthropic releases Claude Opus 5 at same price as Opus 4.8](https://news.google.com/rss/articles/CBMinwFBVV95cUxOUExpODBocm5KMzF1WjlIREJrZEFFWG9KZVVqQVpZeVhBQndwbm9xZ19VQm5CODNfc2xvd0hfd18weDNON2pKV3JWOGQ0bEd5X2VMMzdqaXlfTzZnX1FSa3NERWxNa0ctWkx4YVctMGZKUDlkVUFrU0hMUjVDU1VKb0lkazlrckZXUFB6OVpOWGxYOVpqODJqY25qZlZYNDA?oc=5)（2026-07-26）
- [Reddit r/artificial：Opus 5's effort dial is not monotonic above "high"](https://www.reddit.com/r/artificial/comments/1v60pga/opus_5s_effort_dial_is_not_monotonic_above_high/)（週熱門，2026-07-25）
- [官方 migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide)（查核日 2026-07-29）
- [Reddit：Opus 5 is not as good as i thought](https://www.reddit.com/r/ClaudeCode/comments/1var15k/opus_5_is_not_as_good_as_i_thought/)（2026-07-30，無週熱門標記，score 不可信）
- [Reddit：I defended Opus 5 - and then I realised otherwise](https://www.reddit.com/r/ClaudeAI/comments/1vibkny/i_defended_opus_5_and_then_i_realised_otherwise/)（週熱門，2026-08-07）
- [[news/2026-07-25]]、[[news/2026-07-26]]、[[news/2026-07-28]]、[[news/2026-07-29]]、[[news/2026-07-30]]、[[news/2026-08-07]]

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-08-11 | SitePoint 刊出針對開發者的 Claude Opus 5 效能評測整理，原文僅提供標題層級資訊。❓ **待查證**（標 2026-08-11｜查 SitePoint、效能評測｜複 2026-08-25）｜**SitePoint 開發者效能評測具體數據**：未見量化基準、測試任務或對比對象，內容待查證（Google News/SitePoint，2026-08-11） |
| 2026-08-08 | Reddit r/ClaudeAI 週熱門貼文「PSA: Be careful letting Claude use WebFetch for research」：作者請 Opus 5 研究 AI agent 記憶架構時，發現其以 WebFetch 生成看似真實、實則捏造的具體統計數字、百分比與引述，提醒他人使用 WebFetch 做研究時需小心查核；單一使用者回報、無具體案例引文或跨來源佐證，列為待社群驗證的可靠性觀察，非量化評測結論（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vim8b7/psa_be_careful_letting_claude_use_webfetch_for/)，週熱門，2026-08-08） |
| 2026-08-07 | Reddit r/ClaudeAI 週熱門貼文「I defended Opus 5 - and then I realised otherwise」稱作者原本認為 Opus 5 是目前最「奇特獨特」的模型、稱讚其思考過程（reasoning trace）而非單純能力，深入分析其思考過程後改變了看法；原文於「actually reading through and analysing it's thought process I find fascinati...」處截斷，具體轉折方向（趨向更正面或更負面）不可考。與 07-29～08-04 已記錄的「過度自信」「不如跑分預期」「令人挫折」負向回饋屬同一波「上線兩週後社群重新評估」現象，惟本則聚焦 reasoning trace 角度且結論方向不明，暫列觀察、不代入評測結論（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1vibkny/i_defended_opus_5_and_then_i_realised_otherwise/)，週熱門，2026-08-07） |
| 2026-07-30 | Reddit r/ClaudeCode 貼文（無「週熱門」標記，score 恆為 0 屬 RSS 已知限制不可信）稱使用者原先參考跑分認為 Opus 5 優於 Fable 5，實際使用後認為 Opus 5 仍有落差，提及遇到「minor」問題（原文於此截斷，具體細節不可得）；缺乏具體數字、跨來源佐證或問題細節，僅記錄社群出現不如預期的觀感回報，不代入評測結論。❓ **待查證**（標 2026-08-10｜查 minor、效能落差｜複 2026-08-24）｜**「minor」問題具體所指**：Reddit 原文於此截斷，2026-08-10 查證嘗試無法再取得該貼文內容或後續討論，具體細節與效能落差幅度仍未經查證（[Reddit](https://www.reddit.com/r/ClaudeCode/comments/1var15k/opus_5_is_not_as_good_as_i_thought/)，2026-07-30） |
| 2026-07-29 | Reddit r/artificial 週熱門貼文稱 Opus 5 的 effort 旋鈕「非單調」——超過 `high` 後（`xhigh`／`max`）程式碼任務分數反而下降，並稱官方 migration guide 本身即有此說明；**2026-08-08 查證官方文件後判定此說法不成立**——[What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) 明載「Claude Opus 5 converts additional effort into better results more reliably than any earlier Opus model」，並將 test-time compute scaling（效果隨 effort 提升直到 `max`）列為主要能力改進；官方對 `xhigh`／`max` 的唯一告誡是「須設較大 `max_tokens`」，以及 `thinking: disabled` 在 `xhigh`／`max` 會回 400。未見任何「高於 high 即單調下降」文字，社群措辭比官方原文更強烈——核心說法已證偽，無下降幅度可言，完整比對見 [[topics/model-comparison]] |
| 2026-07-26 | MLQ.ai／PCMag 媒體標題分別稱 Opus 5「Tops AI Benchmark Index」「Tops Fable 5 on Agentic Search」——**2026-08-10 第三方基準查證屬實**：Artificial Analysis Intelligence Index Opus 5 60.7% vs Fable 5 59.9%，GDPval-AA v2／AA-Briefcase 亦領先，詳見上方「現況」；EdTech Innovation Hub 報導稱 Opus 5 與 Opus 4.8 同價發布，與 MarkTechPost「維持原定價」方向一致——**2026-08-08 官方查證確認兩說皆成立**：$5/$25 per Mtok，官方逐字載明「unchanged from Claude Opus 4.8」，同時也確為 Fable 5（$10/$50）的一半，兩種描述指的是同一組數字的不同對照對象（見 [[entities/pricing]]）；Reddit r/ClaudeAI 週熱門貼文提及第三方 benchmark 平台 MineBench.ai 有 Fable 5 vs Opus 5 差異討論——**2026-08-08 查證後不可採信**：MineBench 測的是 3D voxel 空間推理（與編碼／agentic 能力無關），榜上查無 Fable 5 或 Opus 5 條目 |
| 2026-07-25 | 正式發布，取代 Opus 4.8 成為 Claude Max 新預設模型、Claude Pro 最強模型；HN score 1587；SDK（Python/TypeScript）同步加入模型支援；Boris Cherny 稱其為最難被提示注入攻破的模型 |
| 2026-07-24 | Reddit r/ClaudeAI 週熱門貼文稱 Opus 5 於長時間任務（long-horizon task）表現最佳、Low effort 設定下成本效益極高，屬單一社群主觀評價，無量化數字佐證 |
