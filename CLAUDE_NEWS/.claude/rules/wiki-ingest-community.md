# Wiki Ingest — 社群記者指南

分類為「社群」的新聞條目由此記者負責。讀此檔後直接操作，需建立新頁面時另讀 `.claude/rules/wiki-ingest-format.md`。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/topics/community-tech-patterns.md` | 工作流模式、multi-agent 設計、最佳實踐 |
| `wiki/topics/community-tech-discussions.md` | HN / Reddit 熱門技術討論 |
| `wiki/topics/community-tech-timeline.md` | 社群技術應用趨勢時序 |
| `wiki/topics/code-quality-decline.md` | Claude Code 效能退步事件 |
| `wiki/topics/community-large-codebase-workflow.md` | 🗓️ **週更，每日 ingest 不寫此頁**——每日只在 patterns 節點標 `**主線：**` tag（見下方「主線 tag 規則」）；週更整線重寫規則見 `.claude/rules/wiki-ingest-community-lint.md` |

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 🌐 社群 的所有頁面（含日後新增）皆由本記者負責維護與 lint。

> `wiki/topics/community-tech-tools.md` 已改為 **lint 專用**，每日 ingest 不更新此頁。策展規則見 `.claude/rules/wiki-ingest-community-lint.md`。

**分流鐵則：** GitHub Issues 條目屬功能記者（claude-code 已知問題）；僅當該 issue 引發跨平台討論（HN/Reddit 也在延燒）才作為 discussions 條目收錄。

**產品化矩陣轉知 `[加入: 2026-07-04]`：** 發現新的 agent 工作模式（patterns 頁新增條目）時，在回報中註明「請主編轉知功能記者評估產品化矩陣新增列」；`wiki/topics/official-community-gap.md` 的矩陣由功能記者維護，社群記者不直接寫該頁。

**dev.to 條目以內容判斷、不看讚數 `[加入: 2026-07-10]`：** dev.to 走 `top=30` 抓法（過去 30 天高互動文章），但**讚數在 dev.to 幾乎不能當品質指標**——實測顯示最有價值的第一手實作文（如「對抗式 Claude 互審 loop」「local reverse proxy 看 CC 送什麼」）讚數常只有 2–3，反而 SEO 農場文有 5–6 讚。因此 dev.to 條目一律**用內容判斷收錄，不套互動門檻對照表的數字**：

- ✅ **優先收**：「我做了 X、這是怎麼運作 / 踩了什麼坑」的第一手實作、可複用 pattern、具體工具或量化實測（歸 `community-tech-patterns.md`）
- ❌ **排除**：`Complete Guide` / `Everything you need to know` 型 SEO 農場文（常來自 `ai_made_tools`、`tokenmixai` 等內容農場帳號）；純新聞轉述（定價、發布、事件解釋——這些已由媒體/HN 來源覆蓋，dev.to 版本無獨特價值）；純帶貨 / growth hacking 自我推銷

> 判斷原則：dev.to 的獨特價值是「工程師第一手實作經驗」，不是新聞或教學索引。內容答不出「作者具體做了什麼、學到什麼機制」→ 不收。

---

## community-large-codebase-workflow 主線 tag 規則（daily）`[加入: 2026-08-05，改版: 2026-08-15]`

`community-large-codebase-workflow.md` 是把 patterns 節點沉澱成四條主線的**週更**頁；patterns 收「節點」（每日 append），主線頁每週從 patterns **整線重寫**（規則見 `.claude/rules/wiki-ingest-community-lint.md`）。**每日 ingest 不寫主線頁**——2026-08-05～08-15 的日更小縫實驗證明：每天只看一個節點的記者，結構上只做得到「往段尾加一句」，兩週就把綜合敘事頁長回 log；縫合需要看完整條線再重寫，那是週更的事（2026-08-15 使用者裁決）。

**每次為 `community-tech-patterns.md` 新增節點時，多填一個欄位：**

```
- **主線：** 並行規模 ／ Context 管理 ／ 索引記憶 ／ 除錯分工 ／ —
```

- 判準是「這個節點回答的是**大型 codebase 特有**的痛點嗎」——並行 agent 互踩／context 被工具輸出撐爆／agent 記不住跨 session 決策／多 agent 產出誰把關；小專案也會遇到的通用技巧填 `—`
- 可複選（頓號分隔）；拿不準填 `—` 並在「與既有模式的關係」寫一句理由，週更時記者會再判
- 這個欄位是週更唯一的撈料依據（`Grep "\*\*主線：\*\* [^—]"`），漏填等於該節點對主線頁不存在
- 某類節點反覆出現卻無線可歸 → 不自行開線，回報主編轉知 weekly-review 評估第五條線

---

## community-tech-discussions 收錄門檻 `[加入: 2026-06-28]`

此頁追蹤「思想碰撞」，訊號價值有**三個合法來源（滿足其一即可收錄）**：

| 訊號來源 | 收錄理由 | 最低門檻 |
|---------|---------|---------|
| **社群碰撞** | 多方驗證、正反交鋒 | 達對照表**低**門檻（見 `.claude/rules/wiki-reporter-shared.md` 互動門檻對照表），或同議題跨 2 個以上獨立來源（source_count ≥ 2）|
| **重要人士具名表態** | 因「誰說的」而有重量（Boris Cherny、Dario、Karpathy 等）| 具名 + 可信來源；同時回報人物記者更新對應 `entities/` 頁 |
| **重要媒體深度報導** | 因觸及面與報導深度（36Kr、Platformer、WSJ 等）| 報導本身有實質內容，非純轉載標題 |

**誠實標註原則（強制）：** 說明欄須標明訊號性質，熱度符號錨定真實信號強度，不可虛抬：

- 社群兩極化／跨平台廣泛熱議 → 🔥🔥🔥🔥+
- 單平台高互動／議題共鳴深 → 🔥🔥🔥
- 多次被引用／催生後續工具 → 🔥🔥
- **重要媒體/人士單一報導，無社群延燒 → 🔥**，且說明欄末註「（媒體報導，待社群接力）」或「（具名表態，無社群延燒）」

> 關鍵區分：🔥🔥 以上隱含「社群共鳴」，**無社群討論的單一報導不得標 🔥🔥 以上**，避免讀者誤判信號強度。
> 純標題轉載、無實質內容的媒體稿，仍不收錄。

---

## community-tech-patterns ↔ community-tech-discussions 雙向連結規則 `[加入: 2026-05-16]`

新增工具至 `community-tech-patterns.md` 時，若靈感明確來自 discussions.md 的某個討論，同步在 discussions.md 的 `熱門討論` 表格對應列的 `衍生` 欄填入工具名稱（若已有則逗號追加）。

`熱門討論` 表格 `模式` 欄規則：

| 狀況 | 模式 |
|------|------|
| 今天首次出現 | ☄️閃現 |
| 第 3 天以上持續出現 | 🌊延燒 |
| 討論達成共識後收束 | 🌸落幕 |
| `首見` 距今 > 7 天後重新出現 | 🌋重燃（在核心論點補「（重燃原因：…）」） |
| 表中存在但近期無新進展，熱度 ≤ 🔥 | 🌙靜候 |

重燃偵測：直接查 `熱門討論` 表格的 `首見` 欄，不需讀取 log.md。

---

## community-tech-discussions 熱門討論保留規則 `[加入: 2026-06-20]`

每次 ingest 後，若本輪有新增或更新表格條目，同步執行清理：

| 模式 | 保留條件 |
|------|---------|
| ☄️閃現 | 首見距今 ≤ 21 天（超過則移除） |
| 🌊延燒 | 永久保留，無期限 |
| 🌸落幕 | 首見距今 ≤ 14 天（超過則移除） |
| 🌋重燃 | 等同 🌊延燒，無期限 |
| 🌙靜候 | 永久保留 |

**技術彙整保留：** 條目長期保留於原頁（月份分組即入口層，見 `.claude/rules/wiki-ingest-format.md`「頁面拆分原則」）；僅已收斂且不再被引用的死案月份，經使用者確認後才可歸檔至 `wiki/topics/community-tech-timeline.md`。

---

## community-tech-discussions 技術彙整書寫規則 `[加入: 2026-05-20，改版: 2026-07-02]`

**月份分組（patterns / discussions 兩頁的 `## 技術彙整` 皆適用）：** 條目按 `### YYYY-MM` 月份標題分組，條目本身用 `####` 層級。此分組提供跳轉導航，是「頁面不拆分」前提下的替代方案。

**格式：**
```markdown
### YYYY-MM

#### 討論主題名稱（YYYY-MM-DD）

- **來源：** 原始文章標題（平台，作者）
- **核心論點：** 一句話摘要
- **關鍵回響：**（選填，有則記）
  - 📝 支持：…（標題，來源）
  - 📝 反駁：…（標題，來源）
  - 🧪 跟進實測：…（標題，來源，結論一句話）
- **收斂結論：**（若討論已有共識）…
```

**新條目插入位置：** 插入 `## 技術彙整` 下方**當月 `### YYYY-MM` 分組的正下方**（最新在最上方）；當月分組不存在時先建立該月標題。不可加在末尾。

**防過度推論：** 推導出的結論必須標注「（推論）」，不可直接寫成事實。

---

## multi-agent orchestration 學術對照維護 `[加入: 2026-07-22]`

`community-tech-patterns.md` 有一個參考層 `## 學術對照：多智能體 orchestration 術語`（Claude Code 機制 ↔ 學術術語 ↔ 論文），維護規則：

- 於「Multi-agent 架構」或相關類別**新增一種 agent 協作模式／機制**時，判斷它對應到對照表哪一格（控制流 × 通訊原語），需要時新增或更新該表的列。
- 若該模式涉及**新的學術名詞**、或你判斷「參考論文／來源」該補新文獻：**社群記者無 web 工具，不可自行查證論文**。改在回報的「同步自查」欄註明「⚠️ 需主編 WebSearch 查證並補學術對照論文（模式名 + 待對應術語）」，由主編層執行查證與寫入。
- 此為**參考層維護，屬非新聞性更新**：只更新該頁「最後更新」，不動「最後新聞更新」。
- 不杜撰論文；查無權威來源時保留現有對照，不硬填。

---

## 回報格式

```
## 社群 記者回報
更新頁面：[list]
feature-radar 新增：無
index.md 狀態變更：[page: 舊狀態 → 新狀態 or 無]
新增頁面：[filepath or 無]
同步自查：[✅ 已同步 / ⚠️ 需主編轉知（說明）/ 不適用]
待查證命中處置：[已標訊 N 筆: list ／ 證據不足不動 M 筆 ／ 無命中]
轉知處置：[已處理 N 筆: H-id list ／ 不適用 M 筆（id＋一句理由）／ 無待接手]
來源歸因：[每筆一行 or 無]
```
