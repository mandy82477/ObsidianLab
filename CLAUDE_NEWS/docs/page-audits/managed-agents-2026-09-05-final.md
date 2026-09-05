# 設計定稿：`wiki/entities/managed-agents.md`（第 2 波，樞紐 入邊 31）
2026-09-05｜設計者（只派一次）｜適用區 A／B／D／E，**C 不適用**（無視覺成品）｜⚠️ 疑似注入：無
## 0. 定稿一句
> **留頁，把「Managed Agents 百科」改成「官方多 agent 這一格：各零件到哪一級、四個選項怎麼挑」**——砍 SDK 程式碼 75 行，新增四選項分界表（Q1）與計費懸置（Q3），零件狀態表提位並補週更回訪，熱度 🔥🔥🔥🔥🔥→🔥🔥。208 → 約 150 行。
- **不選的方向（各一行）：** 併入 `official-community-gap` 不選，因為該矩陣按**社群模式**分列（L52 一列已塞四代官方對應），零件表按**官方產品**分列，塞進去一列會撐成十列。刪頁不選（使用者 2026-09-05 已裁決留頁）。拆頁不選：子故事三題——自己的問題 ✅／自己的結論與時序 ❌（全頁一條時序）／被獨立引用 ❌（`grep -rn "managed-agents#" wiki/ weekly/` ＝ **0 筆**）。歷史蒸餾本波不做：2026-05 命中「唯一細節出處」例外（現況所述 05-11 正式發布的細節只在該月列），2026-04 僅 2 列、為 2 列開 archive 子頁成本大於收益 → 列入下次每週整理候選。
- **可行性前提（一行）：不需要任何新進料。** 四個選項的分界全部取自庫內既有文字（`coding-workflow-guide` §2/§6、`entities/pricing`「當前生效的計費規則」、本頁零件表）；Q3 本來就沒進料，所以答案是懸置＋交辦而非等抓取。唯一需外部查證的是官方 Managed Agents 文件 URL（§4-4）——**本稿刻意不寫任何未經查證的官方連結**。
## 1. 逐字內容（可直接貼上）
### 1.1 標頭與 callout（取代 L26–36）
標頭三處變動：「領域」之後補 `**別名：** Anthropic Managed Agents, 受管代理`；「最後更新」「最後新聞更新」皆改 `2026-09-05`（本輪納入 09-03 條目）。L35–36 兩則疊句的 callout 整段換成（60 字，上限 120）：
```
> **最新動態**（2026-09-03）
> Reddit 出現「同一模型、同準度、成本低最多 75%」的開源替代方案宣稱，未附測試方法；官方端自 05-22 起無新功能，只有 SDK 版號擴充。
```
### 1.2 現況（取代 L40–46；吸收 L157–161 唯一可留的一句）
```
Anthropic Managed Agents 是 Claude Platform 上的官方 agent 框架：持久記憶（含 Dreaming 記憶整合）、20 路並行子代理、Outcomes 規格驗證、Proactive Workflows、企業自架沙箱。框架整體自 2026-05-11 正式發布，但各零件成熟度不一——只有 `/goal` 已達正式發布，Dreaming 與 Agent View 仍是研究預覽。Outcomes 讓規格文件成為執行時的強制依據（官方語「Specs become load-bearing」）。
實質新功能停在 2026-05-22；此後四筆全是 SDK 版號擴充，官方 changelog 未列細節。獨立第三方生產環境回饋至今為零——本頁引用到的兩則使用案例，一則用的是自組架構、一則來自 Claude Code 創始人。
```
第二段直接回答冷讀者「最近三個月發生了什麼」「有沒有人在用」（原頁要讀者自己算日期）。L42 的機器語法標記移出散文 → §1.5。
### 1.3 熱度與試用價值（取代 L50–59）
```
| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 要跑數小時以上、跨 session 保留狀態的工作流；需要資料不出境（自架沙箱） |
| 不適合 | 單次 30 分鐘內做得完、或不需保留跨 session 狀態的任務——`/goal` 就夠 |

> 跨功能的熱度對比見 [[feature-radar]]；四個選項怎麼挑見下一節。
```
**降到 🔥🔥 的證據**（現行「熱度降溫」只處理「連續 4 週零命中 −1 格」，本頁 4 週有 2 天命中 → 機械上降 0 格，故需補上限式判準，逐字見 §3-(2)）：近 4 週（08-08~09-05）提及 **2 天**（`grep -rlin "managed agent\|受管代理\|managed_agents" news/` → 08-20、09-03；`news_mentions.py --since 4w` 因雙詞同日條件回 0 天）；性質為 `news/2026-08-20.md:32` 版號無細節、`news/2026-09-03.md:60` **他人拿它當對照組**；正向採用回報 0 則。依 §3-(2)：2 天 → 上限 🔥🔥🔥，全屬版號流水或負向對照 → 再降一格 ＝ **🔥🔥**。`wiki/feature-radar.md` **L226** 同步（單邊下修是矛盾的來源）。
### 1.4 新節「你該用哪個」＋「接下來看什麼」（插在熱度表之後、零件表之前）
四根軸皆可自我對號（時長／持久記憶／執行位置／計費），第五欄答「拿不拿得到」。**Q3 不寫金額**：pricing 全文「Managed Agents」grep ＝ 0 命中，只有 Agent SDK／`claude -p`（L44／L114／L552 節）→ 標 ❓ 並交辦（§5）。

````
## 你該用哪個

以下分界只填本庫查得到出處的欄位，查不到的留 `—` 或標為待查證，不以通用工程常識補。

| 選項 | 選它的分界（可自我對號） | 跨 session 記憶／執行位置 | 計費走哪條 | 現在拿得到嗎 |
|------|------|------|------|------|
| `/goal`（Claude Code 內建） | 單一 session 內跑得完，且完成條件寫得成一條可執行檢查（如 `npm test` exits 0） | 無／你自己的機器 | 計入訂閱配額 | ✅ 正式發布（v2.1.139） |
| 內建 subagent（Explore／Plan／general-purpose） | 只是要把大量讀檔丟進獨立 context；Explore 唯讀、一次性、不能追問 | 無／你自己的機器 | 計入訂閱配額 | ✅ 正式發布 |
| **Managed Agents** | 要跑數小時以上並跨 session 保留狀態，或需 20 路並行、資料不出境 | 有（持久記憶）／Claude Platform，企業可自架沙箱 | ❓ 待查證 ⟨Q-03⟩ | ⚠️ 框架已正式發布，多數零件仍在公開測試 |
| Agent SDK | 要把 agent 包進自己的產品或 CI，自己控制迴圈 | 由你自己實作／你自己的基礎設施 | 計入訂閱配額（2026-06-16 起計費切割暫停，重新推行時間未定） | ✅ 正式發布 |

**選型細節**

- **`/goal` 的條件怎麼寫**：一個可量測的結束狀態、一條明確檢查方式、過程中不得改變的約束；條件上限 4,000 字元，可加「or stop after 20 turns」設界。最小用法 `/goal npm test 執行結果零失敗`；四級驗證階梯見 [[topics/coding-workflow-guide]] 第 6、9 段與[官方文件](https://code.claude.com/docs/en/goal)。
- **內建 subagent 的限制**：Explore 唯讀、跳過 CLAUDE.md、一次性不能追問，模型繼承主對話但以 Opus 為上限（v2.1.198 起）；要來回追問得改用 `general-purpose`。見 [[topics/coding-workflow-guide]] 第 2 段。
- **計費的依據**：Claude Code 的互動用量與 Agent SDK 用量皆計入訂閱配額，見 [[entities/pricing]]「當前生效的計費規則」（2026-06-18 起維持至今）；Managed Agents 本身的計費未見官方說法，見下方 ⟨Q-03⟩。
- **成本對照的唯一第三方數字，本庫未採信**：2026-09-03 一則 Reddit 貼文宣稱以同一模型跑自建開源框架，準確度與 Managed Agents 打平、成本低最多 75%，但未附測試方法與資料集，屬單一未驗證宣稱，不列入上表（[原文](https://www.reddit.com/r/LocalLLaMA/comments/1w65ise/we_built_an_opensource_modelneutral_agent_harness/)）。
- **社群自組替代**：Opus 決策層＋OpenCode 執行層的自組架構（Reddit 開發者 70 天實戰，2026-05-11）仍是可行選擇，核心結論是任務簡報品質決定成敗；與官方框架的對照見 [[topics/official-community-gap]]。

**懸置細節**
- ⟨Q-03⟩ ❓ **待查證**（標 2026-09-05｜查 Managed Agents、受管代理、託管代理）｜**Managed Agents 本身怎麼計費**：[[entities/pricing]] 只載 Agent SDK 與 `claude -p` 的規則，未見 Managed Agents 的費率、計費單位或是否走獨立通道；本頁不寫金額。

## 接下來看什麼

- **等哪個訊號**：Dreaming 或 Agent View 從研究預覽升格、官方公布 Managed Agents 的計費方式、出現第一則獨立生產環境回饋。三者任一發生，上面兩張表就會變。
- **你的選項**：(a) 什麼都不做，先用 `/goal` 把單 session 的完成條件立起來；(b) 只在需要資料不出境時評估自架沙箱；(c) 想要跨 session 記憶又不想綁平台，先看社群自組架構——但目前唯一的成本數字未附方法。
````
### 1.5 零件表與兩筆逾期懸置
原 L140–153 表身 **10 列一字不動**，節名改 `## 各零件現在到哪`、提位到「你該用哪個」之後，表上加一行 `資料截至 2026-08-20（狀態每週複查）。`（治「指標表凍結」；回訪規則見 §3-(1)）。
`check_pending_markers.py` 實測本頁 2 筆各逾期 12 天（`:42`、`:211`）。**設計者不得結案**（結案要 web 查證，屬每週整理 5c）。L211 ⟨Q-01⟩ 留原位（短標記 L189 與定義成對，格式正確）；L42 散文裡的完整標記**搬家不刪**，成為 2026-07-16 那列的短標記 ⟨Q-02⟩，**標記日 2026-08-10 與探針原文一字不改**：

```
| 2026-07-16 | **anthropic-sdk-python v0.117.0** 新增「api: add support for dreaming」，命名疑似對應 Dreaming 記憶整合 ❓ 待查證 ⟨Q-02⟩（見 [Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.0)）|
```
底下這條進頁尾「懸置細節」區（與 ⟨Q-01⟩ 並列）：
```
- ⟨Q-02⟩ ❓ **待查證**（標 2026-08-10｜查 anthropic-sdk-python、dreaming API）：v0.117.0 的「api: add support for dreaming」是否對應本頁 Dreaming 記憶整合功能，官方 changelog 未說明技術細節，尚待後續版本或文件確認。同一疑問在 [[entities/claude-code]] 亦有記錄。
```
⚠️ 同一疑問**三份副本**（本頁 ⟨Q-02⟩、`entities/claude-code` L799 ⟨Q-14⟩／L800 ⟨Q-15⟩，皆為 v0.117.0 dreaming），違反 REVIEW-PRINCIPLES 22 → 合一屬 5c 裁決，本稿不動（§4-2）。
### 1.6 歷史記錄新增一列（最上方）／相關議題（取代 L165–169）／guide 側
```
| 2026-09-03 | Reddit 貼文宣稱自建開源 agent 框架以同一模型達同準度、成本低最多 75%，未附測試方法與資料集（[原文](https://www.reddit.com/r/LocalLLaMA/comments/1w65ise/we_built_an_opensource_modelneutral_agent_harness/)）|
- [[entities/claude-code]]（Managed Agents 整合於 Claude Code 工作流；SDK 版本流水與已知問題住該頁）
- [[topics/coding-workflow-guide]]（`/goal`、驗證階梯與內建 subagent 的實際用法）
- [[topics/official-community-gap]]（官方對應程度與社群缺口對照）
- [[topics/community-tech-patterns]]（社群工具 Dreamer 採用類似理念，早於官方功能出現）
- [[entities/pricing]]（訂閱配額與 Agent SDK 計費規則）
```
`wiki/topics/coding-workflow-guide.md` §6 的「**缺口**」段之前插一行（同為功能記者的頁，可直接改）；連頁不連錨——該 h2 標題帶 `[社群面待補]` 進度標記，會隨進度改名，錨點必腐：
```
`/goal` 只管單一 session；要跨 session 保留狀態或 20 路並行，官方的另一格是 Managed Agents——四個選項的分界見 [[entities/managed-agents]]「你該用哪個」。
```
## 2. 逐行號去向（一行不憑空消失）
| 原行號 | 內容 | 去向 |
|---|---|---|
| L1–25 | frontmatter | 不手改（`gen_wiki_frontmatter.py` 生成） |
| L26–33 | 標頭欄位 | **改**：補別名、兩日期改今日（§1.1） |
| L35–36 | callout（兩則疊一句、版號流水） | **改**為單則 delta；被換掉的 v0.118.0／v0.125.0 事實已在 L188–189 |
| L40–46 | 現況（含機器語法標記） | **改**寫兩段（§1.2）；標記搬 §1.5；「agentic AI 的 AWS」定位語刪（行銷語，事實留在 L201） |
| L50–59 | 熱度與試用價值 | **改**：熱度降格、最適合／不適合換成可對號分界、指路句改指新節（§1.3） |
| L63–64、L83–130 | 「使用指南」節標＋Python／TS SDK 範例 47 行 | **砍**（零入邊、零日報出處、115 天未動；git history 保留） |
| L65–76、L132–134 | `/goal` 用法範例＋關鍵注意事項前 2 條 | **下沉**為選型細節第 1 條（一行最小用法＋Outcomes 寫法＋官方文件連結）；「Dreaming 不宜上生產」＝零件表「研究預覽」已表達 |
| L77–81 | Agent View `claude agents` | **併**入零件表既有那列（L148 已寫 `claude agents`） |
| L135–136 | 社群替代方案＋70 天洞察 | **移**至選型細節末條（原位置在勸退句旁丟第四個選項，冷讀者卡點 L23） |
| L138–153 | 核心功能表 | **提位＋改名**「各零件現在到哪」，表身不動，加「資料截至」行（§1.5） |
| L157–161 | 架構意義 3 條 | **併／砍**：Outcomes 一句併入現況；規模化一句與零件表重複 → 砍；社群工具對比（Dreamer/NanoBrain/Memex）→ 砍，家在 [[topics/official-community-gap]]（相關議題已連） |
| L165–169、L171–182 | 相關議題／參考來源 | 前者**改**為 5 條（§1.6）；後者**留**，不新增未查證的官方 URL |
| L184–211 | 歷史記錄＋細節＋懸置細節 | **留**；表頂加 09-03 一列、L190 補 ⟨Q-02⟩ 短標記、細節區加 ⟨Q-02⟩ 定義（⟨Q-03⟩ 定義住新節表下）。**新增兩節** `## 你該用哪個`、`## 接下來看什麼`（逐字皆在 §1.4） |
## 3. 維護者同步（`.claude/rules/wiki-ingest-features.md`，逐字）
**(1) 新增節，放在「1M 專頁的觸發邊」之後（同為明文觸發邊）：**
```
## Managed Agents 零件狀態表的回訪 `[加入: 2026-09-05]`
`wiki/entities/managed-agents.md` 的 `## 各零件現在到哪` 是**覆寫式**狀態表：10 列的狀態欄（研究預覽／公開測試／正式發布）會變，但沒有任何日報條目會通知你它變了——近四個月該頁實際進料 100% 是 SDK release note，而 release note 從不說成熟度。
**每次 `/wiki-lint`（週更）：** 逐列比對 `wiki/feature-radar.md` 全覽表與 `## 🆕 最新功能` 詳細條目中同名功能的狀態欄，不一致以 radar 為準覆寫本表，並更新表上方「資料截至 YYYY-MM-DD」為今日；radar 亦無該功能時保留原值、不臆測升格。`## 你該用哪個` 表第五欄與本表同源，一併回掃。lint 回報加一行：`零件狀態表：N 列比對／M 列已覆寫／資料截至 YYYY-MM-DD`。
```
**(2) 「熱度降溫：它不是棘輪」節內，接在現有「判定」條之後：**
```
- **提及天數是熱度的上限，不只是 −1 格的觸發** `[加入: 2026-09-05]`：近 4 週日報提及**天數** ≥8 天可到 🔥🔥🔥🔥🔥、4–7 天上限 🔥🔥🔥🔥、1–3 天上限 🔥🔥🔥、0 天照上條 −1 格。若該窗提及**全部**屬 (a) 無細節的版本號流水、或 (b) 他人拿它當對照組的負向提及，再降一格（下限 🔥）。天數用 `python scripts/news_mentions.py --since 4w` 加英文名與中文譯名量；回 0 天時再以單一名稱 `grep -rlin` 複核一次，避免雙詞同日條件把真命中判死。（立法依據見沿革檔 2026-09-05）
```
**(3) 「feature-radar 動作表」下方新增一條：**
```
### 否定證據也要有路回來 `[加入: 2026-09-05]`
日報條目若**拿某個官方功能當對照組**，宣稱替代方案在成本、準度或速度上更好（無論該條目被分類成社群、是否達收錄標準），在對應 `entities/` 頁的細節區記一行，**必附證據等級與缺什麼**（如「單一貼文，未附測試方法」），並於回報「同步自查」欄註明來源日期。**不進 feature-radar、不改熱度以外的評級**——它是讀者判斷「值不值得」的唯一反向材料，不是功能異動。（立法依據見沿革檔 2026-09-05）
```
**(4) 「負責頁面」表 `topics/coding-workflow-guide` 那列的觸發條件補一句：**
```
；`## 6. 測試與上線` 段末保留一行指向 [[entities/managed-agents]]「你該用哪個」的出口（連頁不連錨——該段標題帶進度標記會改名）
```
> 沿革檔 `docs/rules-changelog/wiki-ingest-features.md` 補 2026-09-05 段（熱度上限式判準與否定證據回流的教訓敘事；條文只留判準，依 `.claude/rules/claude-md-edit.md`）。
## 4. 需主編（記者無權處理）
1. `wiki/feature-radar.md` **L226** Managed Agents（全套）🔥🔥🔥🔥🔥 → **🔥🔥**（與本頁同一份值）。
2. v0.117.0 dreaming **三份副本合一**（本頁 ⟨Q-02⟩、`claude-code` L799 ⟨Q-14⟩／L800 ⟨Q-15⟩）→ 每週整理 5c 查證後裁決留哪份。
3. `wiki/index.md`「💻 開發實務入口」缺一列（冷讀者：9 列裡沒有「我想讓 agent 自己跑」，L30 提 `/goal` 卻不提本頁）。建議：`| 我想讓 agent 自己跑幾小時／過夜，該用哪個 | [[entities/managed-agents]]「你該用哪個」 |`
4. 官方 Managed Agents 文件 URL 查證 → 補進「參考來源」。本庫全文查無可信 URL，本稿刻意不填。
## 5. 交辦帳本（跨維護者，不直接改他人頁）
```
python scripts/pending_handoffs.py open --from 功能 --to 商業 --page entities/pricing \
  --note "Managed Agents 本身的計費（費率、計費單位、是否走獨立通道）在 pricing 全文零命中，只有 Agent SDK／claude -p 的規則；managed-agents 已標 ⟨Q-03⟩ 待查證（標 2026-09-05）。屬官方說明中心事實，請依商業記者規則標『需主編查證』升級；查到後兩頁同步並回填 ⟨Q-03⟩"
```
## 6. 自己過閘的輸出＋看守宣稱核實
兩支閘的 `scan()` 直接量本稿要寫進 wiki 的每一段（暫存 `scratchpad/ma-draft.md`＋`ma-hist.md`）：`=== 讀者語言閘 === OK: 無命中（0 筆）` ／ `=== 字元上限閘 === OK: 無命中（0 筆）`。
**驗紅（A-2，不只看綠）：** 同一份稿注入 1 行含「ingest／派工」＋130 字元儲存格＋228 字元條列 → 讀者語言閘命中 2 筆（`ingest`、`派工` @L97）、字元上限閘命中 2 筆（`table_cell` 130/120、`list_item` 228/200）；移除注入回到 0。**閘確實在量這份稿。** 過程中被擋下並已修一處：2026-07-16 那列補 ⟨Q-02⟩ 後儲存格 130 字元，刪「；changelog 無技術細節」後合格。
懸置語法另以 `pending_markers.py` 驗：`iter_pending()` 解出 ⟨Q-02⟩⟨Q-03⟩（符號／類別詞／標記日／探針齊全），`probe_too_weak()` 對 `Managed Agents`／`受管代理`／`託管代理` 皆回 `None`，`detective_aliases()` 三者皆有偵測力。
| 宣稱 | 真的有嗎 | 出處 |
|---|---|---|
| 儲存格 >120／條列 >200 被擋 | ✅ 已驗紅 | `check_cell_limits.py` `scan()` L157、`_table_cells()` L141、`main()` L230；掛 `run_tests.py` |
| 內部用語被擋 | ✅ 已驗紅 | `check_reader_language.py` `TERMS` L49 起（22 詞）、`scan()` L228 |
| 懸置語法／探針品質被擋 | ✅ | `check_pending_markers.py` L24 四類檢查；`pending_markers.py` `probe_too_weak()` L207、`PROBE_STOPLIST` L82 |
| 改節名不會打斷別頁錨點 | ✅ 安全 | `grep -rn "managed-agents#" wiki/ weekly/` ＝ 0 筆；第 1 波錨點致命閘不會因本波變紅 |
| 零件表週更「會被機器抓到」 | ❌ **無機械看守** | 只有 `table_census.py` 機制欄會由「無」→「有」：`_mechanism()` L39 在規則檔搜節名 ＋ `MECH_RE` L26（`淘汰\|移除\|保留\|封存\|覆寫\|蒸餾\|汰除\|到期\|清理`），§3-(1) 條文同時含「各零件現在到哪」與「覆寫」。**它只證明規則存在，不證明有人做**；執行靠 `/wiki-lint` 步驟 2 記者讀規則檔（與 guide 週更動作同一條路），回報行是唯一可稽核痕跡 |
| 熱度上限判準會被機器算 | ❌ 無 | 人工步驟：`/wiki-lint` 5a，量測指令寫在 §3-(2) 條文內 |
## 7. 實作後的驗證清單（依序跑，附預期值）
1. `check_reader_language.py` → `OK: 無新增命中`（exit 0）｜2. `check_cell_limits.py` → exit 0（本頁改動處零新增命中）｜3. `check_pending_markers.py` → 語法通過；本頁短標記／定義成對 3 組（Q-01／Q-02／Q-03）
4. `table_census.py entities/managed-agents` → 3 張表；`各零件現在到哪` 機制欄「無」→「有（wiki-ingest-features.md）」｜5. `check_rules.py` → 綠（本波未動 registry）
6. `gen_wiki_frontmatter.py` → `run_tests.py` → 全綠 exit 0｜7. `build_web.py` → 錨點 WARN 不增（本頁錨點入邊 0）｜8. `wiki_graph.py explain entities/managed-agents` → 出邊 6 → 8（新增 coding-workflow-guide、pricing）
