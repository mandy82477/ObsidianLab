# 主編官方查證 — entities/pricing（2026-09-06，UTC 17:1x）

記者與設計者無 web 工具，本步是唯一能抓到「頁面 vs 官方現況」落差的層。全部由主 session WebFetch／WebSearch，逐條附出處。

## 一、頁面既有數字對官方定價頁（全部相符）

來源：[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)、[Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)

| 頁面條目（行） | 官方現況 | 判定 |
|---|---|---|
| L86 Sonnet 5 $2/$10 永久化、9/1 漲價取消 | 官方 Note 逐字：「is now the standard price. The previously scheduled increase to $3/$15 … on September 1, 2026 will not occur.」 | ✅ 一致 |
| L87 Fable 5.1 $10/$50、快取命中 ×0.025、Batch $5/$25；Mythos 5.1 同價僅限授權 | 表列一致；Mythos 5.1 標「limited availability」 | ✅ 一致 |
| L88–92 Fable 5 / Opus 5 / Opus 4.8 / Sonnet 4.6 / Haiku 4.5 價格 | $10/$50、$5/$25、$5/$25、$3/$15、$1/$5 | ✅ 一致 |
| L110–112 Managed Agents：token＋$0.08/session-hour、只計 running、不適用 Batch 與 partner 雲、算例 $0.705／$0.525 | 逐字一致 | ✅ 一致 |
| L113 Managed Agents 仍 beta | overview「Claude Managed Agents is in beta. All … endpoints require the `managed-agents-2026-04-01` beta header」 | ✅ 一致 |
| L150 乘數節（快取 1.25×／2×／0.1×、inference_geo 1.1×、fast mode $10/$50） | 一致；補充：**Batch 與快取可疊加**、fast mode 不可與 Batch 併用；1M context 全程標準價 | ✅ 一致（可補兩句） |

**官方頁面有、本頁沒有、但讀者會問的**（供設計者判斷要不要收）：
- 4.7 以後模型與 Mythos 用新 tokenizer，**同一段文字約多 30% token**（官方 Note 逐字）。這直接回答 L100 The Register「tokenizer 讓成本難比」那條懸而未決的標題式報導——現在有官方數字了。
- Claude Platform on AWS／Microsoft Foundry 以 **CCU（$0.01/CCU，100 CCU＝$1）**計費、只能後付、折扣以少計 CCU 呈現。本頁「通路」表（L133）沒有這兩條通路。
- Code execution 每月 **1,550 免費小時**，超出 $0.05/hr；web search $10/1,000 次；web fetch 免費。

## 二、週配額促銷（L118–121、index L50、feature-radar 倒數）

官方 support 文章 WebFetch 兩個 URL 皆未取得原文（11145838 只說 Pro/Max 共用限額；11014257 回 404）。改以多家獨立媒體交叉（BleepingComputer、SmartScope、AI Catchup、explainx、digitalapplied，皆引 08-29 官方公告）：

- +50% 促銷延長至 **2026-09-13 23:59 PT**；**09-14** 起標準週配額永久 +25%，適用 Pro、Max、Team、座位制 Enterprise；相對促銷水位 **−17%**。
- 判定：本頁 L118–121 三個數字（09-13、+25%、−17%）與適用範圍**一致**。「23:59 PT」是本頁沒有的精度，可補。
- ⚠️ 未能取得官方 support 原文，屬二手交叉查證；頁面現行出處（support.claude.com 09-02 更新）由 09-02 ingest 記者登記，本次未推翻。

## 三、逾期懸置 4 筆的處置建議

| 行 | 懸置 | 查證結果 | 建議 |
|---|---|---|---|
| **L341**（＋L337 小標） | $35M 額度「供企業透過 Claude Security 導入 Mythos 5」，細節未見 | **事實更正**：官方 blog（[2026-08-21](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)）$35M 是 **Defender Advantage Fund (0xDAF)**，對象是「幫開源維護者修漏洞的組織」，形式為 Claude credits，先做少數大額 pilot grants，**不是企業導入額度**。企業端另一件事：Claude Enterprise 可在 Claude Security 跑 Mythos 5，**按既有方案的標準 token 用量計費、無加購**。 | 結案：小標與內文改寫成兩件事；「計費規則」節可加一條「Claude Security × Mythos 5 掃描＝標準 token 計費」 |
| **L358** | DevOps.com 08-19「boost expires tonight」與 +50% 延長是否同一時程 | 官方時間軸：促銷歷次到期日 07-19→08-18 前後→08-31→09-13。08-19 前後正是一次到期／延長交接點，DevOps.com 標題描述的是「當期到期日」，之後被延長。與本頁時序不矛盾。 | 結案為「同一促銷、當期到期日被延長」，移出待查證 |
| **L503** | 配額重置機制是否變動（單一 Reddit） | 官方無任何公告；本次查證 09-06 仍無 | 依「單一回報、逾期、官方無回應」慣例改為已掃無後續的結案句（同 L511／L515 寫法） |
| **L509** | usage limits 是否曾調整 | 同上，官方未證實也未否認 | 同上 |

## 四、給設計者的一句話

pricing 頁的**數字本身是準的**（七項全對），問題不在事實而在形狀：讀者要的「這個月我會多花／少花多少」沒有一處直接回答，而 09-14 這個全站最大的即將發生衝擊被埋在計費規則第 8 條。

## 五、健檢卡「需官方查證表」V2／V5／V6／V7（第二輪，UTC 17:2x）

| # | 結果 | 出處 | 對頁面的意義 |
|---|---|---|---|
| V2 週配額絕對量 | **官方不公布**每週小時／token 絕對量，只在 `Settings > Usage` 顯示個人數字。第三方量測口徑：Max 5x ≈ 每週 480 Sonnet 小時或 40 Opus 小時（多家整理站互抄，無官方原文） | tokn.watch、claudelimit.com、explainx 等（二手） | Q1「17% 換成體感」**結構上答不了**；頁面能做的是「17% × 你 Settings > Usage 裡的數字」一句換算法，不給絕對量 |
| V5 Fable 5.1 每小時算例 | 官方定價頁**只有 Opus 5** 一小時算例（$0.705）；Fable 5.1 無 | pricing 頁 Managed Agents 節 | Q2 的錨要自己算：同算例代 Fable 5.1 牌價＝50k×$10＋15k×$50＋$0.08 ≈ **$1.33／小時**（標明「依官方 Opus 5 算例的 token 量代入 Fable 5.1 牌價」，屬推算） |
| V6 Spend Controls 粒度 | 官方 blog 2026-07-02：Enterprise 專屬；**org 層 spend cap（75%／90% 警示）＋ group／部門層 cost 報表 ＋ per-user 可見度與限額（75%／95% 通知）**；model entitlements 可依角色鎖模型；有 Admin API；Claude Code 有專屬分析（cost per commit 等，每日更新） | [官方 blog](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend) | **ECM L58–61 三項「🧪 部分回應」可結案為 ✅ 有官方對應**，只剩「混合計費管理」仍 ❌。這是 ECM 頁最大的一筆過期 |
| V7 $100 過渡 credit | 2026-09-17 23:59 PT 到期，**到期即作廢**，不可續買、不轉存；適用 07-19 前的 Pro／Team standard，Max 與 premium seat 本無此 credit | 多家轉述官方說明中心（二手交叉，口徑一致） | L55「記得用掉」正確；可補「到期作廢」四字＋ feature-radar ⏰ 是否已有此列待查 |

## 六、第三輪（UTC 20:3x）：V1 升級為一手＋雲端 09-05 新懸置結案

- **V1 一手確認**：[官方促銷說明頁](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion) 逐字：「From May 13, 2026 through September 13, 2026, your weekly usage limit in Claude Code is 50% higher」「valid … through September 13, 2026 at 11:59 PM PT」「available for Pro, Max, and Team plans, as well as legacy seat-based users on Enterprise plans」「5-hour usage limits are not affected by this promotion」。**該頁不提 09-14 +25%**（那是 08-29 Bluesky 公告，非說明中心）——頁面若把兩者寫成同一出處要拆開。第二節「二手交叉」註記可撤。
- **雲端 09-05 ingest 新增懸置**（pricing 現行 L327「改版後完整價格結構待查證，複 09-19」）：主編 09-06 已開官方定價頁全文，結構＝本檔第一節那張表（模型牌價 × 5 欄快取／輸出、Batch 表、Managed Agents 節、AWS／Foundry CCU 節、tool 計價節）。記者機械 diff 看到的「新增 Mtok 區間段、移除企業人數規模段」對應的是 platform 文件頁改版，非價格變動。**結案：價格未變，結構見 verified 第一節**。
- **同日「Anthropic Resets Claude Limits」媒體副標**：與 09-13／09-14 換軌一致，無新事實；callout 該句可撤。
