# 主編官方查證 — entities/opus-5（2026-09-07）

行號＝檔案原始行號（含 frontmatter）。查證對象：現況節（L40–62）、index L54 鉤子、三筆逾期懸置（L152／L155／L158）。一手：platform 模型頁、anthropic.com 公告、code.claude.com What's new W30。

## 一、頁面事實對官方

| 頁面句（行） | 官方現況（逐字＋來源） | 判定 |
|---|---|---|
| L46「2026-07-25 正式發布」＋L52「日期說明：RSS 07-24 17:00 UTC，pricing 標 07-24，本頁 07-25」 | platform `models/opus-5/overview`：「**Latest.** Released July 24, 2026」；Retirement「Not sooner than July 24, 2027」 | ⚠️ 官方發布日 **07-24**；本頁用日報收錄日 07-25 當發布日並花一段解釋，該改成官方日＋一句「本站 07-25 收錄」。退役下限全站零處寫 |
| L50「能力定位：Frontier-Bench、GDPval-AA 上逼近 Fable 5…資安任務落後 Mythos 5」 | anthropic.com〈Claude Opus 5〉：「comes close to the frontier intelligence of Claude Fable 5 at half the price」；Frontier-Bench v0.1 超越所有對手、CursorBench 3.2「Within 0.5% of Fable 5's peak at half the cost per task」、ARC-AGI 3 三倍於次佳、OSWorld 2.0 超越 Fable 5 且成本三分之一；「remains behind Mythos 5 on cybersecurity exploitation tasks」；misalignment score 最低 | ✅ 方向對；官方四個具體數字頁面只引兩個名稱，可補一列「官方宣稱 vs 社群實測」 |
| L54「定價定位：官方宣稱定價為 Fable 5 的一半（the-decoder 轉載）」；index L54「定價定位待彙整」 | 官方：$5 / $25（與 Opus 4.8 相同）；cache read $0.50、5m write $6.25、1h write $10；Batch 50%；「Fast mode runs 2.5x faster at double base price」＝$10／$50（W30） | ✅ 數字有官方；**「待彙整」是過期宣稱**（第 10 波校準第三種互斥）——index 鉤子改；本頁該引官方模型頁不引 the-decoder |
| L56「預設模型變化：現為 Claude Max 新預設模型、Claude Pro 最強模型」 | code.claude.com W30（07-20～24）：「Claude Opus 5 is the new default Opus model in Claude Code. It's the default on Max, Team Premium, Enterprise pay-as-you-go, and the Anthropic API… On the Anthropic API and on Max, Team, and Enterprise plans, Opus 5 runs with a 1M-token context window… Requires v2.1.219 or later」；公告：「Available on Claude Max, Claude Pro, and the API」；support〈Models, usage, and limits in Claude Code〉：「Sonnet is the default and is the right choice for the large majority of coding work」 | ⚠️ 兩層要分開：Claude Code 的**整體預設是 Sonnet**，Opus 5 是「預設的 Opus」且在 Max／Team premium／Enterprise PAYG／API 為預設；**Pro 可用但 Pro 的 1M 官方未列**（W30 只列 API／Max／Team／Enterprise）——「Pro 最強模型」句無官方出處，Fable 5.1 在 Pro 走 usage credits（第 10 波查證），所以 Pro 免額外付費的最強是 Opus 5 這句要寫成那樣 |
| L48／L58「取代 Opus 4.8」；index L55 opus-4-8「已被取代」 | `models/opus-4-8/overview`：「**Legacy.** Released May 28, 2026… you should consider migrating to Claude Opus 5」；Retirement「Not sooner than May 28, 2027」；同價 $5／$25；知識截止 Jan 2026（Opus 5 為 May 2026）；W30：「Fast mode no longer supports Opus 4.7: /fast now applies to Opus 5 and Opus 4.8」 | ✅；Q2「4.8 還能用多久」的官方答案＝Legacy、至少到 2027-05-28、同價、知識舊 4 個月——全站零處寫 |
| L59「Opus 5 vs 4.8 兩個 breaking change」（頁面有無？） | `models/opus-5/overview`：「two breaking changes for code running on Claude Opus 4.8: thinking is on by default, and thinking can be disabled only at effort `high` or below」；「Effort defaults to `high` on Claude Opus 5 and matters more than on earlier models」 | 頁面核心功能節（L77）若無此兩條，是 Q2 缺的一手 |
| L158「Reddit：effort 旋鈕非單調，超過 high 分數反降」（07-29，社群） | 官方 Effort 文件只說 effort matters more；SitePoint〈Claude Opus 5 Is Most Efficient at Medium Effort: FrontierCode Benchmark Data〉存在但**SitePoint 同系列文章事實全錯**（見下） | 社群單一貼文，留原等級；不升級 |

## 二、三筆逾期懸置

| 行 | 懸置 | 查證結果 | 處置建議 |
|---|---|---|---|
| L152 ⟨Q-03⟩ Reddit「Opus 不再是必要依賴」證據（複 09-06） | 原文為圖片卡片，兩次查證不可取得 | **結案（不可查證）**：連同 08-13／08-08／08-07 三則同型「社群觀感」合併成一列「社群觀感分歧（07-30～08-28，五則單一貼文，無量化）」，標記移除須先確認是唯一的家（保命條款） |
| L155 ⟨Q-04⟩ SitePoint 效能評測具體數據（複 08-25） | sitepoint.com〈Claude Opus 5: Performance Benchmarks for Developers〉可取得，但內文寫「200K context」「$15／$75」「released July 17, 2025」——**三項與官方全錯**（1M／$5／$25／2026-07-24） | **結案（來源不可靠）**：改寫為「SitePoint 08-10 評測文事實與官方不符（200K、$15／$75、2025 發布），不採信」，標記移除 |
| L158 ⟨Q-05⟩ Reddit「minor」問題所指（複 08-24） | 原文截斷，08-10 與 09-07 兩次不可取得 | **結案（不可查證）**：併入上列「社群觀感分歧」一列 |

三筆結案後本頁懸置歸零；`data/pending-marker-count.json` 基線 141→138 需 `--rebuild-count --reason`。

## 三、給設計者

1. 本頁三題的官方答案各一句：拿得到嗎（Max／Team premium／API 預設，Pro 可用、Claude Code 整體預設仍 Sonnet）、跟 4.8 差在哪（同價、知識新 4 個月、兩個 breaking change、4.8 Legacy 至 2027-05-28）、什麼時候該用 Fable 5.1（官方：「Use Fable 5.1… when your evals on Opus 5 at higher effort still fall short」——第 10 波 verified 已引）。第 10 波兩代對照表的形狀可直接複用：Opus 5 vs Opus 4.8 七列，或三代一表（4.8／5／Fable 5.1）由設計者判。
2. 現況節 L40–62 有 10 段、5 個日期並排（08-28、08-27、07-25、07-26、07-24），與 fable-5 改版前同病。
3. 「定價定位待彙整」在 index 鉤子上掛了六週，官方數字 07-24 就有——第三種互斥的實例。
4. 歷史記錄 15 則全在 07-24 之後，未達蒸餾門檻；三筆懸置結案後歷史記錄可縮成「社群觀感分歧」一列＋逐則。
