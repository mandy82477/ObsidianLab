# 評審：`wiki/entities/managed-agents.md` 定稿（第 2 波）

受審：`docs/page-audits/managed-agents-2026-09-05-final.md`（150 行）
需求：`managed-agents-2026-09-05.md`（健檢卡＋使用者裁決）、`wave2-cold-reader-2026-09-05.md`
立場：對抗式，四視角（明天的維護者／機器／冷讀者／治理）。**我的修法即定稿，主 session 直接執行。**
適用區：A（獨立重驗、驗紅）、B（領域合理性）、D（同一事實只住一處）、E（分離、無發現合法）；**C 不適用**（無視覺成品）。
**⚠️ 疑似注入：** 無。

---

## 0. 先獨立重驗（A-1／A-2，不信提案自述）

| 定稿宣稱 | 我實查 | 判定 |
|---|---|---|
| 兩支閘「過閘 0 筆」 | 我把定稿要進 wiki 的每段重打成 `scratchpad/ma-draft.md`，用 `ccl.scan()`／`crl.scan()` 直接量 → **0／0** | ✅ 屬實 |
| 已驗紅 | 我注入 130 字元儲存格＋228 字元條列＋含「記者／ingest／派工／覆寫」一行 → 字元閘 2 筆、語言閘 4 筆；移除即回 0 | ✅ **閘確實在量這份稿** |
| ⟨Q-02⟩⟨Q-03⟩ 語法／探針合格 | `pm.iter_pending()` 解出三筆（Q-01/02/03）欄位齊全；`probe_too_weak()` 對 `Managed Agents`／`受管代理`／`託管代理` 全回 `None`，`detective_aliases()` 三者皆非空 | ✅ 屬實 |
| `grep -rn "managed-agents#"` ＝ 0 | 我重跑 `wiki/ weekly/ web_reader/` → 0；`wiki_graph.py explain … --section "使用指南"` → 錨點入邊 **0**／整頁 31 | ✅ **砍 75 行不斷任何錨點** |
| pricing 全文 Managed Agents ＝ 0 命中 | 重跑 `grep -rn "Managed Agents\|受管代理" wiki/entities/pricing.md` → 0 | ✅ ⟨Q-03⟩ 成立 |
| `news_mentions --since 4w` 回 0 天、grep 回 2 天 | 重現。**但 `--any` 旗標早就存在**，`--any` 直接回「2 天，08-20／09-03」並印出原文行 | ⚠️ 事實對、處方錯 → 🔴-R2 |
| 逐行號去向表 | 抽驗 12 段（L26–33／L35–36／L40–46／L50–59／L63–64／L65–76／L77–81／L83–130／L132–136／L138–153／L157–161／L184–211）**全對**；未列的只有空行與 `---` | ✅ 高可信 |
| 「208 → 約 150 行」 | 現檔實為 **211 行**；照去向表加總（−75 −7 −2 ＋1 ＋28 ＋2 ＋2 ＋1 ＋1）＝ **約 162 行** | ⚠️ 見 🟡-Y6 |

---

## 🔴 R1（治理）｜熱度上限判準是**全站立法**，會在下次 5a 波及整張 radar

定稿 §3-(2) 把新條文插進 `.claude/rules/wiki-ingest-features.md`「熱度降溫：它不是棘輪」節——那一節管的是**所有追蹤中的功能**，不是本頁。`wiki/feature-radar.md` 現有 **26 列帶 🔥🔥🔥🔥**；照新判準（4 週提及 ≥8 天才准 🔥🔥🔥🔥🔥、4–7 天上限 🔥🔥🔥🔥），下次 `/wiki-lint` 5a 主編必須對每一列跑一次天數量測並大量下修——這是一次沒有人裁決過的全站評級重排。

而且它與**同節既有的「不降的例外」**（`「⏰ 倒數中」或本輪熱度／試用價值有變動者，本輪不降`）沒有優先序：一個 ⏰ 倒數中、4 週只提及 2 天、現掛 🔥🔥🔥🔥🔥 的條目，兩條規則給出相反答案。

**修法（本輪改成兩件事，不寫進共用節）：**

1. **本頁與 radar 一次性下修照做**（🔥🔥🔥🔥🔥 → 🔥🔥），但理由寫成一次性編輯判斷，不寫成規則的產物。定稿 §1.3 那段括號說明改為：

   > **降到 🔥🔥 的一次性下修（2026-09-05 頁面健檢）**：近 4 週（08-09~09-06）日報提及 2 天（`python scripts/news_mentions.py --since 4w --any "Managed Agents" "受管代理"`，命中 08-20、09-03），性質為 `news/2026-08-20.md` 版號無細節與 `news/2026-09-03.md` 他人拿它當對照組；正向採用回報 0 則、實質新功能停在 05-22。現行「連續 4 週零命中 −1 格」對本頁降 0 格，故本次為編輯判斷而非規則計算。`wiki/feature-radar.md` L226 同步。

2. **§3-(2) 整段不寫入規則檔**，改成待裁決提案，寫進 `docs/page-audits/ledger.md` 第 2 波那列的「裁決」欄末尾：

   > 待使用者裁決（未實作）：是否把「4 週提及天數＝熱度上限（≥8→🔥🔥🔥🔥🔥／4–7→🔥🔥🔥🔥／1–3→🔥🔥🔥），且全屬版號流水或負向對照再降一格」寫成 `.claude/rules/wiki-ingest-features.md`「熱度降溫」的全站條文。影響面：radar 現有 26 列帶 🔥🔥🔥🔥，首次套用等於全站評級重排；且需先定與「不降的例外」的優先序。

> 判斷式：這條規則下週會動到幾頁？答案是「整張 radar」→ 它不是本頁的定稿，是待裁決的立法。

## 🔴 R2（機器）｜處方叫人手刻 grep，而官方旗標早就在

§3-(2) 逐字寫「天數用 `news_mentions.py --since 4w` 量；回 0 天時再以單一名稱 `grep -rlin` 複核一次」。但 `scripts/news_mentions.py` L142 `ap.add_argument("--any", ...)`、L44 檔頭已明載「`--any` 任一詞命中即算（預設需 ≥2 詞同日命中）」，L171 `need_two=not args.any`。我實跑：預設回「命中 0 天」，`--any` 回「命中 2 天，最後一次 2026-09-03」**並印出兩行原文供逐條看**。

叫人改用臨場 grep，正好違反同檔多處的明文「**用共用腳本查，不要臨場手刻 grep**」（`wiki-ingest-features.md` 熱度降溫節、⏳ 觀望節），也丟掉腳本強制的「逐條看命中原文行」防線。

**更大的事：這是全站假陰性機器。** 預設 `need_two` 要求兩個別名**同一天**命中；日報是繁中寫的、但多數功能沒有慣用中文譯名（本頁「受管代理」在近 4 週日報一次都沒出現），於是這類功能**每週都被量成 0 天、每週被 −1 格**。

**修法：**

1. R1 的第 1 點已把量測指令改成 `--any` 版本，本頁到此為止。
2. 另開一筆給主編（不進本頁定稿）：在 `.claude/rules/wiki-ingest-features.md`「熱度降溫」與「⏳ 觀望」兩節的量測指令句，把 `news_mentions.py --since 4w` 改為 `news_mentions.py --since 4w --any`，並在句末補一句「`--any` 的輸出必須逐條看原文行再下結論（腳本末行的警告即為此）」。此改動影響兩節共用的判定，屬全站規則變更，**與 R1 的提案一起端給使用者**，不由本波逕改。

## 🔴 R3（治理）｜「否定證據也要有路回來」寫給了看不到那則條目的人

§3-(3) 把新規則放進 `.claude/rules/wiki-ingest-features.md`（功能記者的檔），要求「日報條目若拿某個官方功能當對照組……在對應 `entities/` 頁的細節區記一行」。但健檢卡第 4 點自己診斷過：09-03 那則落在日報「💬 技術熱度討論」→ **社群類** → 社群記者手上，**功能記者結構上看不到它**。規則寫在收件人那一側，發訊端沒有任何人被要求發訊 → 這條規則永遠不會被觸發，和沒寫一樣。

本庫已有對稱防線的先例（`wiki-reporter-shared.md`「規則檔優先於派工訊息」：派工端與記者端兩側都改，理由逐字寫著「只修一側仍依賴某人每次記得」）。

**修法（兩側都要，逐字）：**

(a) `.claude/rules/wiki-ingest-community.md`，「回報格式」節之前新增：

```
## 官方功能的負向對照要回流 `[加入: 2026-09-05]`

社群條目若**拿某個官方功能當對照組**、宣稱替代方案在成本／準度／速度上更好（無論該條目是否達本頁收錄門檻），在回報「同步自查」欄寫一行：
`⚠️ 需主編轉知功能記者：[官方功能名] 出現負向對照（來源＋日期＋證據等級：如「單一 Reddit 貼文，未附測試方法」）`。
你不寫該功能的 entities 頁，只負責讓這則證據被看見——它結構上只會經過你手上（2026-09-03 教訓：唯一一則對 Managed Agents 有決策價值的證據被合法擋在社群通道，功能記者四個月不知情）。
```

(b) `.claude/rules/wiki-ingest-features.md` §3-(3) 原文保留，但開頭改成「**收到主編轉知的**日報條目若拿某個官方功能當對照組……」，末句補「發訊端規則見 `.claude/rules/wiki-ingest-community.md`「官方功能的負向對照要回流」」。

(c) 本輪 09-03 那則的補記，走帳本補一筆（與 §5 的 pricing 那筆並列）：

```
python scripts/pending_handoffs.py open --from 主編 --to 功能 --page entities/managed-agents \
  --note "2026-09-03 Reddit 貼文（r/LocalLLaMA）拿 Managed Agents 當對照組宣稱同模型同準度、成本低最多 75%，未附測試方法與資料集。本輪已由頁面健檢直接寫入 entities/managed-agents 選型細節與歷史記錄；此筆為新規則「官方功能的負向對照要回流」的首次示例，供下次同型條目對照"
```

## 🔴 R4（明天的維護者）｜零件表「一字不動」＋「資料截至 2026-08-20」＝ 帶著兩個已知錯誤上站

定稿 §1.5：「原 L140–153 表身 **10 列一字不動**」，並在表上加「資料截至 2026-08-20（狀態每週複查）。」但我逐列對 `wiki/feature-radar.md`：

| 零件 | 本頁 L150／L151 | radar | 差 |
|---|---|---|---|
| Proactive Workflows | 公開測試 | L219 `公告（細節待確認）`＋「公告後 102 天無後續報導，細節未公布」 | ❌ |
| Capability Curve | 公開測試 | L220 同上 | ❌ |

而定稿自己寫的新規則 §3-(1) 就是「不一致**以 radar 為準覆寫本表**」。首次套用的結果今天就查得出來，卻要讀者等到下週——「資料截至 2026-08-20」這行等於為兩個已知錯誤背書。同時 Q1 表第五欄「多數零件仍在公開測試」在修正後也失真（10 列變成：1 正式發布／2 研究預覽／2 公告未詳／5 公開測試）。

**修法（三處，實作時一併改）：**

1. 零件表兩列改為：

```
| Proactive Workflows | Agent 可主動排程並自動觸發任務，不需人工輸入即可啟動 | 公告（細節待確認，公告後逾 100 天無後續） |
| Capability Curve | Agent 能力曲線追蹤，評估不同任務類型能力進展 | 公告（細節待確認，公告後逾 100 天無後續） |
```

2. 表上方那行改為 `資料截至 2026-09-05（狀態每週複查，以 [[feature-radar]] 為準）。`
3. Q1 表 Managed Agents 那列第五欄改為 `⚠️ 框架已正式發布，10 個零件中只有 /goal 正式發布`。
   同步 §1.2 現況第一段末句改為：「……只有 `/goal` 已達正式發布，Dreaming 與 Agent View 仍是研究預覽，Proactive Workflows 與 Capability Curve 自 2026-05-18 公告後細節未公布。」

（三處改完我已用 `ccl.scan()` 量過形狀：最長儲存格 53 字元，遠低於 120。）

---

## 🟡

- **Y1｜「最後新聞更新」應填 2026-09-03，不是 09-05。** `scripts/check_wiki_freshness.py` 檔頭逐字：「「最後新聞更新」填**日報日期**，不是新聞事件發生日」。本輪納入的是 `news/2026-09-03.md` 的條目，且 `news/2026-09-05.md` 根本不存在（最新為 09-04）。定稿 §1.1「兩日期皆改 2026-09-05」與它自己的 callout 日期（09-03）也不一致。
  **改法：** `**最後更新：** 2026-09-05` ／ `**最後新聞更新：** 2026-09-03`。
- **Y2｜漏了來源歸因一行。** `.claude/rules/wiki-ingest.md` 第三步要求新落地事實 append `data/source_attribution.jsonl`；定稿 §4「需主編」四項沒有這筆。缺它，`check_wiki_freshness` 第 1 類雖不會紅（既有歸因 08-20 < 09-03 不觸發），但來源記分卡會漏記 Reddit 的貢獻。
  **改法（append 一行）：**
  ```json
  {"date": "2026-09-03", "source": "reddit", "category": "功能", "page": "entities/managed-agents", "item_url": "https://www.reddit.com/r/LocalLLaMA/comments/1w65ise/we_built_an_opensource_modelneutral_agent_harness/", "item_title": "We built an open-source, model-neutral agent harness and compared it with claude managed agents - for the same model, got same accuracy, upto 75% lower cost"}
  ```
- **Y3｜Q1 表 Agent SDK 的「✅ 正式發布」庫內查無出處**，且定稿的現況改寫順手刪掉了原 L44「原生 SDK 支援自 TypeScript v0.95.0、Python v0.100.0 起」——那句正好是這一格唯一的證據。兩件事一起解：
  該格改為 `✅ 正式發布（Python SDK v0.100.0＋／TypeScript v0.95.0＋）`。
- **Y4｜guide 的出口放錯層。** §1.6／§3-(4) 只在 `## 6. 測試與上線` 段末加一行（我核對過：該段末確有「**缺口**」行，兩處描述其實一致，不是矛盾）。但冷讀者的路徑是 guide 的 `## 我想問的是⋯⋯` 導航表——那張表 18 列裡沒有任何一列講「讓它自己跑」。§6 那行照留，**另加導航表一列**（該表是功能記者自己的頁，可直接改；插在「它說做完了，我怎麼知道是真的」那列之後）：
  ```
  | 我想讓它自己跑幾小時／過夜，該用哪個 | [第 6 段](#6-測試與上線-怎麼讓它自己驗完再交給你社群面待補)；四個選項的分界見 [[entities/managed-agents]]「你該用哪個」 |
  ```
- **Y5｜§3-(1) 條文讓新表在表格普查裡仍是「無機制」。** 我讀 `scripts/table_census.py` `_mechanism()` L38–50：需**同一行**同時出現節名與 `MECH_RE`（L26：`淘汰|移除|保留|封存|覆寫|蒸餾|汰除|到期|清理`）。§3-(1) 提到「你該用哪個」的那句是「`## 你該用哪個` 表第五欄與本表同源，一併回掃」——`回掃` 不在清單內。
  **改法（該句改一詞）：** 「`## 你該用哪個` 表第五欄與本表同源，一併**覆寫**、不得留舊值。」
  （`## 各零件現在到哪` 那句我已驗過：同行含「覆寫」，普查會由「無」→「有」，定稿的宣稱屬實。）
- **Y6｜行數帳兩處都對不上：** 基線是 **211 行**（非 208），照去向表加總後約 **162 行**（非 150）。不影響任何動作，但 ledger 那列別抄 150。

## 🟢

- **G1｜本頁 pending 由 2 筆變 3 筆**（Q-01/Q-02/Q-03），其中兩筆探針完全相同（`anthropic-sdk-python`、`dreaming API`），加上 `entities/claude-code` L799/L800 的 ⟨Q-14⟩⟨Q-15⟩，同一批 dreaming 疑問全庫共 **4 筆**會被每日掃描同時打中。定稿 §4-2 已列為 5c 待裁決是對的（記者與健檢皆無權結案）；建議在該項補一句「4 筆同探針，掃描每次同時觸發，5c 優先處理」。
- **G2｜`check_cell_limits.scan()` 對讀不到的檔靜默 `continue`**（L163–166 的 `except: continue`）。我第一次驗紅時因 shell 編碼寫出 cp950 檔，兩支閘都回「0 筆」而不是報錯——**讀不到 = 通過**。不影響本波（我改用 UTF-8 重寫後即驗紅成功），但值得日後補一筆。
- **G3｜Q1 表 5 欄不是問題。** 我逐格量渲染可見寬度：最寬 53 字元（`/goal` 分界格），其餘 ≤ 41。不必為欄數瘦身。
- **G4｜⟨Q-03⟩ 探針用頁面主體名（Managed Agents 等）合法但偵測粒度粗**——任何 Managed Agents 新聞都會通知，而懸置問的是計費。因該詞 4 週只出現 2 天，誤報成本低，維持原樣即可。

---

## 照順序執行（實作單）

| # | 改什麼 | 動作 |
|---|---|---|
| 1 | `wiki/entities/managed-agents.md` | 照定稿 §1.1–§1.6 全量改寫，**但套用**：Y1（最後新聞更新 ＝ 2026-09-03）、Y3（Agent SDK 格補 SDK 版號）、R4-1/2/3（兩列狀態、資料截至日、Q1 第五欄與現況末句）、R1-1（熱度說明改為一次性下修措辭） |
| 2 | `wiki/feature-radar.md` L226 | 🔥🔥🔥🔥🔥 → 🔥🔥（主編項，與第 1 步同一 commit——單邊下修是矛盾的來源） |
| 3 | `wiki/topics/coding-workflow-guide.md` | §6「**缺口**」行之前插定稿 §1.6 那句；**另加** Y4 的導航表一列 |
| 4 | `.claude/rules/wiki-ingest-features.md` | 只寫入定稿 §3-(1)（含 Y5 的「覆寫」改詞）與 §3-(4)；**§3-(2) 不寫入**（R1-2 改列 ledger 待裁決）；§3-(3) 照 R3-(b) 改開頭與末句 |
| 5 | `.claude/rules/wiki-ingest-community.md` | 新增 R3-(a) 整節 |
| 6 | `docs/rules-changelog/wiki-ingest-features.md` | 補 2026-09-05 段：零件表無進料通道的教訓＋負向對照回流的兩側設計（**不寫熱度上限判準**，它還沒生效） |
| 7 | `data/source_attribution.jsonl` | append Y2 那一行 |
| 8 | 交辦帳本 | 跑定稿 §5 的 pricing 那筆，**再跑** R3-(c) 那筆 |
| 9 | `wiki/index.md` | 定稿 §4-3 的「💻 開發實務入口」新列（主編項） |
| 10 | `docs/page-audits/ledger.md` | 第 2 波列填裁決摘要；加 R1-2 的待裁決句；行數寫 211→約 162（Y6） |

**跑什麼驗證、預期輸出：**

| 指令 | 預期 |
|---|---|
| `python scripts/check_reader_language.py` | `OK: 無新增命中`，exit 0 |
| `python scripts/check_cell_limits.py --page managed-agents` | 零新增命中，exit 0 |
| `python scripts/check_pending_markers.py` | 語法通過；本頁短標記／定義成對 **3 組**（Q-01／Q-02／Q-03），逾期數 2→2（Q-03 未到期） |
| `python scripts/table_census.py entities/managed-agents` | **4 張**表（多出「你該用哪個」）；`各零件現在到哪` 與 `你該用哪個` 機制欄皆「有（wiki-ingest-features.md）」 |
| `python scripts/check_wiki_freshness.py` | exit 0（最後新聞更新 2026-09-03 ≥ 歸因 2026-09-03） |
| `python scripts/check_rules.py` | 綠（本波未動 registry） |
| `python scripts/gen_wiki_frontmatter.py` → `python scripts/run_tests.py` | 全綠 exit 0；本頁 frontmatter `pending_count` 2→3 |
| `python scripts/build_web.py` | 錨點 WARN 不增（本頁錨點入邊 0，已驗） |
| `python scripts/wiki_graph.py explain entities/managed-agents` | 出邊 6 → 8（新增 coding-workflow-guide、pricing） |
| `python scripts/news_mentions.py --since 4w --any "Managed Agents" "受管代理"` | 命中 2 天（08-20、09-03）——熱度下修理由的可重現證據 |

**驗紅（A-2）：** 第 1 步改完後，臨時把某格加到 121 字元、某節塞「ingest」一詞，兩支閘應各紅一筆；還原後回綠。我已在 scratchpad 對定稿逐字稿做過此測（字元閘 2 筆／語言閘 4 筆 → 0），閘確實在量這份稿。

---

## 需 WebFetch 查證的官方 URL 清單（主 session 一次查完，填進「參考來源」）

定稿刻意不填未查證的官方連結是對的（設計者無 web 工具）。要補的有五條：

| # | 要什麼 | 預期路徑 |
|---|---|---|
| 1 | Managed Agents 產品／總覽文件 | `platform.claude.com/docs/en/agents/…` 或 `/docs/en/managed-agents`（可能落在 `code.claude.com` 側） |
| 2 | **⟨Q-03⟩ 的答案**：Managed Agents 計費 | `platform.claude.com/docs/en/about-claude/pricing` 是否列 managed agents 項；否則 `support.claude.com` 說明中心搜 managed agents billing |
| 3 | Dreaming／Agent View 目前階段（是否仍 Research Preview） | Claude Platform release notes 或 `/docs/en/agents/memory` 類頁；用來驗 R4 的零件表 |
| 4 | **Proactive Workflows／Capability Curve 有無正式文件**（R4 的正解，關係到那兩列該寫「公告未詳」還是「公開測試」） | 同 3；查無即維持 R4 的改法 |
| 5 | 自架沙箱參考文件（本頁 2026-05-22 記「完整參考文件發布」卻無連結） | `platform.claude.com/docs/en/agents/self-hosted-sandboxes` 類 |

1、3、5 查到即補「參考來源」；2 查到則回填 ⟨Q-03⟩ 並同步 `entities/pricing`（§5 帳本那筆隨之 close）；4 查到則第 1 步就用官方值，不用 radar 值。
