# 全站頁面 review 總帳

流程與角色見 `.claude/skills/page-audit-review/SKILL.md`；共用派工前綴見 `docs/page-audits/dispatch-prefix.md`。

**起點（使用者裁決 2026-09-05）：** 從讀者三個根問題各走一條路徑，不從單一樞紐頁擴散。
**裁決節奏（使用者裁決 2026-09-05）：** 授權主 session 下非阻擋級裁決（文筆、欄位、表格判準、蒸餾）；**拆頁／砍整節／改頁面使命句／砍整頁／併兩頁／新增一頁**必須停下來問使用者（後三項 2026-09-06 加：使用者指出四波從沒判過頁面層去留，skill Q4 已加「頁面去留」欄）。

## 三條路徑

| 路徑 | 讀者的根問題 | 涉及頁面（依入邊） |
|---|---|---|
| P1 | 我該用哪個模型／誰比較強 | `topics/model-comparison`(28)、`topics/model-task-leaderboard`(5)、`topics/competitor-landscape`(52，已定稿) |
| P2 | 我該不該升版 | `wiki/feature-radar`、`entities/claude-code`、`topics/code-quality-decline`（待盤點） |
| P3 | 外面有什麼會衝擊我／要花多少錢 | `entities/pricing`(135)、`topics/enterprise-cost-management`、`topics/competitor-landscape`（待盤點） |

## 分層判準（入邊數，`python scripts/wiki_graph.py explain <slug>`）

樞紐 ≥15：完整六問卡＋設計／評審（Opus）｜中層 5–14：輕量卡（Q1/Q2/Q4/Q5）｜葉子 <5：機械掃描＋一句冷讀者判斷（Sonnet）

## 總帳

| 波 | 頁面 | 層 | 健檢日 | 裁決 | 複驗 | 回訪日 | 產物 |
|---|---|---|---|---|---|---|---|
| 0（試點） | topics/competitor-landscape | 樞紐(52) | 2026-09-05 | 已定稿（雷達表／一行制時序／06 月封存；587→423 行） | ✅ 原考題複驗過 | 2026-09-12 | `competitor-landscape-2026-09-05{,-proposals,-review,-final}.md` |
| 1 | topics/model-comparison | 樞紐(28) | 2026-09-05 | 定稿：使命句定稿、三節移出正文、Benchmark 表凍結降位第 8 節（到期 2027-03-04）、摘要補真答案＋出口 | ✅ 複驗過（Q1 死路→3 跳拿到帶數字答案；Q2–Q4 由 2 跳→1 跳） | 2026-09-12 | `model-comparison-2026-09-05{,-proposals,-review,-final}.md`、`wave1-cold-reader-2026-09-05.md` |
| 1 | topics/model-task-leaderboard | 葉子(5)→升輕量卡 | 2026-09-05 | 定稿：摘要宣告「跨家到此為止」、承認本頁量模型不量工具＋懸置登記、index 補路由 | ✅ 複驗過（Q1 死路→3 跳拿到帶數字答案；Q2–Q4 由 2 跳→1 跳） | 2026-09-12 | 併入同一波產物 |
| 2 | entities/managed-agents | 樞紐(31) | 2026-09-05 | 定稿：留頁、使命句「做到哪一格＋怎麼選」（使用者委由主 session 判）、砍使用指南 75 行留官方連結、新增四軸選型分界表、零件表提位、熱度 🔥🔥🔥🔥🔥→🔥🔥 一次性下修；**主編查證更正**：狀態 beta 非正式發布、計費 $0.08/hr＋token 直接寫入取代懸置 | ✅ 複驗過（四題全拿到：Q1 4 跳沒拿到→2 跳、Q3 零覆蓋→拿到計費；首屏 index L31 直達；唯一殘留卡點「訂閱配額 vs token 兩種貨幣怎麼換算」屬資料缺口） | 2026-09-13 | `managed-agents-2026-09-05{,-final,-review,-verified}.md`、`wave2-cold-reader-2026-09-05.md` |

| 3 | entities/pricing ＋ topics/enterprise-cost-management（併卡） | 樞紐(136)＋樞紐低標(24) | 2026-09-06 | 定稿：使命句 A「Claude 現在怎麼收你的錢，以及最近哪幾件事改變了這個答案」（使用者裁決）；ECM「一家公司導入 Claude 之後帳單會怎麼長，別人踩到什麼、怎麼收斂」；三子故事不拆；pricing 753→688 行改「三結論表打頭（我的方案／一小時多少／事故還在不在）＋事件流證據層」，22 條事故補五值狀態、總表 6 列＋留表優先序入規則檔、蒸餾 2 時段建 `entities/pricing-archive`（全庫首個 entities archive）、砍 4 節；ECM 缺口三項依官方 blog 結案（Enterprise-only 明示）、指標表重算 12 案例、砍「目前結論」；讀者語言閘 +4 詞基線重建；index 首屏補「錢」路由；**主編查證**：數字七項全對、$35M 事實更正、促銷頁一手原文；主 session 代判 3 裁決點（砍兩節、加四詞）與 4 條狀態符號 | ✅ 複驗過（Q2 半→**拿到**，Q3 半→**拿到 1 跳**；Q1／Q4 由「拿到」改「半拿到」是頁面改成不虛報的結果：官方不公布配額絕對量、Spend Controls 僅限 Enterprise）；複驗抓到 40–44 倍撐不起與 10 條洩漏已修 | 2026-09-13 | `pricing-2026-09-06{,-verified,-proposal,-proposal-map,-review}.md`、`wave3-cold-reader{,-recheck}-2026-09-06.md` |

| 4 | wiki/feature-radar ＋ entities/claude-code（併卡；topics/code-quality-decline 只動兩處） | 樞紐(39)＋樞紐(75) | 2026-09-06 | 定稿（使用者授權自跑，使命句主 session 定）：radar「這禮拜官方動了什麼、值不值得你現在跟，以及跟上去會壞什麼」；claude-code「Claude Code 現在有什麼毛病、哪些修了、哪些你得繞過去」。radar：升版風險改「從你現在的版本升上去會遇到什麼」**版本階梯表 12 列**（依 gh 抓完整 changelog，非報導覆蓋率）、熱度與試用價值**只住全覽表**（刪 39 處副本，`check_feature_radar.py` 加單一家檢查已驗紅）、推薦節改名補「怎麼開始」、keybindingFlavor 已失效三處同改；claude-code：新增「現在會咬到你的」7 列結論表（判準：壞掉而非還沒做、每列寫誰會遇到）、13 筆逾期懸置 7 結案＋Apps Gateway 事實更正、7 處節名消費端同步、帳本 6 筆；code-quality-decline 懸置以官方 v2.1.116 結案。**裁決**：砍「近期重要更新（2026 Q2 精選）」使用者未回→預設不砍只搬警示；熱度單一家與腳本五行主 session 代判 | ✅ 複驗過（Q1 半→**拿到**、Q2 半→**拿到**、Q4 拿到；Q3 仍半拿到：區塊名「這禮拜」含 07-25 條、Fable 5.1 model id 自打——已修）；評審複核有條件放行 3 🔴 已修 | 2026-09-13 | `p2-2026-09-06{,-verified,-proposal,-proposal-map,-draft,-review}.md`、`wave4-cold-reader{,-recheck}-2026-09-06.md` |

> 第 1 波同時吃掉 `wiki/reader-notes.md` 的 ⏳「『誰比較強』三頁互踢」——考題集必含「Codex 和 Claude 誰強」，落點必須唯一。

## 待辦（第 3 波遺留）

- **讀者語言閘缺詞「已掃日報至」——四處同改**：`.claude/commands/wiki-lint.md:94` 措辭改為「截至 YYYY-MM-DD 未見後續報導」、`.claude/review-registry.json:713` 同步更新、`scripts/check_reader_language.py` TERMS 加入該禁詞、`data/reader-language-baseline.json` 全庫基線重建。四處須同一 commit 完成，否則規則檔與禁詞互打（見 `pricing-2026-09-06-proposal.md` 第二輪 🟡-5 反駁）。

## 本波順帶落地的機械看守（第 1 波）

| 閘 | 治什麼 | 存量處置 | 驗證 |
|---|---|---|---|
| `scripts/check_cell_limits.py`（掛 `run_tests.py`） | 儲存格 >120／細節區條列 >200 —— 規則檔明文兩個月、零偵測器 | `data/cell-limit-baseline.json` 1191 筆／38 頁，只擋新增 | 注入 121／201 字元 → FAIL；邊界值 → 通過 |
| `build_web.py` 錨點掃描補 `weekly/` 並改致命 | 節名凍結的第二把鎖（registry `anchors` 只擋節名被改，擋不到別頁把錨點打錯） | 存量失效 0 筆，今天成本 0 | 注入壞錨點 → exit 1 指名該筆；還原 → exit 0 且 byte-identical |

## 2026-09-12 回訪要查什麼（第 1 波）

1. 每日更新有沒有把兩頁磨回舊形狀（MC 三節有沒有長回來、LB 摘要的邊界句還在不在）
2. 凍結節名有沒有被改（`registry` anchors 兩筆＋錨點致命閘應該擋得住，但要確認擋的是對的東西）
3. `check_cell_limits` 有沒有誤擋（記者改寫既有超限文字會脫離指紋基線）——看 lint 回報有沒有人抱怨
4. 複驗留下的未修項：LB `## 本週註記` 的編輯部進度報告口吻（修它要同步改 `/wiki-lint` 5b，否則下週長回來）、`⟨Q-nn⟩` 短標記無圖例
5. 三筆轉知帳本（H-7dbf7a／H-27721d／H-402a37）有沒有被接手

## 健檢卡校準（第 3 波起累積）

| 波 | 卡點命中 | 跳數命中 | 六問抓不到、下波要加的 |
|---|---|---|---|
| 4 | 4/4 | 3/4（口徑統一後跳數可信；Q4 沒對上是「讀者起點」假設錯——冷讀者走 index L28 而非 claude-code） | (1) **結論句反向掃描**：結論句對同頁反例（「以上皆非可直接升級」vs 靜默截斷）；(2) 首屏路由加「看不看得見」（量路由句所在段落字數）；(3) 考題集加「讀者起點」欄；(4) 鄰居頁數字掃描射程要涵蓋 Q4 分工的頁；(5) 內部用語閘清單缺口連兩波命中（懸置括號語法／候選症狀／補跑日報／標題進度標記）——該提案補閘而非逐波人工 |
| 3 | 4/4 | 0/4（健檢卡把頁內捲動當一跳、冷讀者把開頁當一跳；下波統一用「開了幾頁」） | (1) index 首屏有沒有路由到本頁——六問無此問；(2) 數字自洽掃描（pricing L216「184 僅次於 67」）；(3) 鄰居清單要由 `wiki_graph.py explain` 的入出邊機械產生，健檢卡憑印象挑漏了真被搞混的那對（pricing↔model-comparison）；(4) 讀者語言閘清單缺「已掃日報至」「候選症狀」「不重複維護」類維運句 |

## 使用者裁決紀錄

- **2026-09-06｜熱度上限式判準不成法（選 b）**：維持「連續 4 週零命中 −1 格」，接受版號流水撐熱度的假陽性；managed-agents 的 🔥🔥 屬本頁一次性下修，不寫進 `wiki-ingest-features.md`。條文原文留在 `managed-agents-2026-09-05-final.md` §3-(2) 供日後翻案。
- **2026-09-06｜第 3 波走 P3「成本與衝擊」**（`entities/pricing` 為主、`topics/enterprise-cost-management` 為鄰居）。

## 2026-09-13 回訪要查什麼（第 3 波）

1. 事故總表有沒有被 ingest 寫回編年史（商業記者是否照「計費事故」列填狀態、覆寫總表）；06-24 盜刷 09-22 起應轉 ⏸
2. 09-14 換軌過後：callout 第一則與計費規則第 1 條有沒有人改成「已生效」；feature-radar ⏰ 該列移除後 pricing L1xx 是否仍在
3. 「一小時／一個月」表有沒有被加第二種口徑；牌價變動時是否整表重算
4. ECM 指標表案例數與實列數是否仍一致；「目前結論」有沒有被 lint 3c 長回來
5. 未修項：model-comparison L99／L119 編輯政策混在標題與儲存格（冷讀者複驗第 4 節第 10 條，第 1 波頁面）；ECM 🧰 圖例缺（社群格式）；「已掃日報至」四處同改待辦
6. 健檢卡下波要加的四問（校準表）有沒有真的加進派工前綴

## 2026-09-13 回訪要查什麼（第 4 波）

1. **版本階梯表有沒有人續抓 changelog**（唯一無機械看守的單點）：`gh api repos/anthropics/claude-code/contents/CHANGELOG.md -H "Accept: application/vnd.github.raw"` 本機 grep 破壞性／預設值改變；建議固化進 `/wiki-lint` 週步驟並寫腳本 `scripts/changelog_ladder.py`（待辦）
2. 熱度副本有沒有被 ingest 寫回（`check_feature_radar.py` 應擋）；「現在值得跟的三件」的「怎麼開始」有沒有被磨掉
3. claude-code「現在會咬到你的」七列狀態有沒有人翻；🧠 組頭統計是否仍與實列一致
4. 砍「近期重要更新（2026 Q2 精選）」整節——使用者裁決仍懸；懸則下次 lint 再問一次
5. 他頁未修項（本波不動，記回訪或轉知）：coding-workflow-guide 標題進度標記 `[已深查]／[社群面待補]／[已補：庫內證據]`（L230／L384／L444 等）與 L51 進度自述；code-quality-decline L89「候選症狀」L107 `⟨Q-01⟩`；skill-interest-watch L31／L72 機器產出自述、**L82 星數 210,287 vs claude-code L66「131,000+」矛盾且榜無抓取日期**、L52 Groundtruth 單一 04-27 實測當唯一首選 vs guide 第 9 段不提；index L28「它說做完了沒做」兩頁給不同首選
6. 字元上限基線本波 `--rebuild` 回填 7 筆（4 持平 3 縮短，主編核對未增長；其中兩筆只改複查日即脫離指紋——指紋含日期屬設計缺口，待辦：指紋排除懸置括號內日期）
7. 帳本 6 筆（H-881390／H-34f143／H-fbfbc0／H-a55c12／H-849df2／H-3c570b）有沒有被接手

## 待使用者裁決（第 2 波遺留，已於 2026-09-06 裁決 b，留作原文）

- **熱度上限式判準要不要成為全站規則**：設計者發現現行「連續 4 週零命中 −1 格」對 managed-agents 機械上降 0 格（近 4 週命中 2 天，但一則是版號流水、一則是他人拿它當對照組），提出「提及天數 → 熱度上限；全屬版號流水或負向對照再降一格」。評審判定這是全站立法：寫進 `wiki-ingest-features.md`「熱度降溫」節會在下次 lint 5a 波及 radar 現有 26 列 🔥🔥🔥🔥，且與同節「不降的例外」無優先序。本波只做本頁一次性下修；條文原文見 `managed-agents-2026-09-05-final.md` §3-(2)。**選項**：(a) 成法，先定與「不降的例外」的優先序並對 26 列做一次 dry run；(b) 不成法，維持「零命中才降」，接受版號流水撐熱度的假陽性。


## 待辦（第 4 波 P2，2026-09-06）

- `topics/coding-workflow-guide` 三處標題進度標記（:510／:444／:341）——屬功能記者自己的頁（不是他頁），下波功能線處理。
