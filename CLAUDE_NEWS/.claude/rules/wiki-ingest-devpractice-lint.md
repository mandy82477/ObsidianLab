# Wiki Ingest — 開發實務（devpractice）週彙整指南（lint 層）`[加入: 2026-09-02]`

`/wiki-lint` 步驟 5f 由主編派 devpractice 記者執行（此為週彙整的明文觸發邊）。每日 ingest 不讀此檔——daily 只沉澱候選帳本（`.claude/rules/wiki-ingest-devpractice.md`），彙整全在本檔。

**執行順序前提：** 5f 在六記者 lint 收報**之後**跑（功能記者的 guide 清冊週更、社群記者的 tools 策展已完成），所以本步讀到的都是本週最終狀態，寫入不會互踩。

---

## 每週三件事

### 1. 覆寫 guide「本週 coding 亮點」節

讀近 7 天 `data/devpractice-candidates.jsonl`，在 `wiki/topics/coding-workflow-guide.md` 維護 `## 本週 coding 亮點` 節（首次執行時建立，位置在「我想問的是」表之前）：

- **覆寫不 prepend**（同 feature-radar「本週推薦」哲學——它回答「這禮拜」，不是編年史）
- ≤ 10 行條列，每條：一句話＋指向細節所在頁的 wikilink（事實的家在原頁，本節只做導流）
- 本週零候選 → 節內留一行 `> 本週無新亮點（YYYY-MM-DD 檢查）`，不得拿舊料充數
- **連續 2 週無亮點 → 在回報標「⚠️ 連續 2 週零亮點，建議檢討收錄判準是否過嚴」轉知主編**（同 feature-radar「本週推薦連續 3 週無替補」警訊哲學）——coding 是本庫大宗，正常週該有料；連續空手更可能是判準太嚴或 daily 沉澱失靈，不是世界真的安靜

### 2. guide「[社群面待補]」逐段輪替深查

guide 第 4、6、7、8、9 段標著「社群面待補」。每週**選一段**（從第 9 段起、依 9→4→6→7→8 輪替，做完一輪重數），用**庫內證據**（候選帳本、`community-tech-patterns`、`community-tech-tools`、近 30 天 `news/*.md`）補該段社群面：

- 有證據 → 補入該段，標來源與日期，該段標記升為 `[已補：庫內證據]`
- 查無 → 該段不動，在回報寫「已查範圍＋零證據」——誠實留白優於通用工程常識灌水（guide「不做的事」明文禁止）
- 無 web 工具；需要官方查證的線索走「⚠️ 需主編轉知」

### 3. coding 跨頁對帳

檢查三處引用是否失步（引用方 vs 事實的家）：

| 引用方 | 事實的家 | 對什麼 |
|---|---|---|
| guide 導航表「社群側見…」行 | `community-tech-tools` 🧩 Skills 速查 | 節名還在嗎 |
| `community-large-codebase-workflow` 各線 🧰 行 | tools「我卡在這裡」決策表 | 症狀句與首選還對得上嗎（機械層已有 `scripts/check_tools_page.py`，此處看語意） |
| `wiki/index.md` 💻 開發實務入口表 | 各目標頁 | 路由描述還成立嗎；本週有新 coding 頁值得入表嗎 |

失步屬自己可改的（guide）直接改；屬他人頁面（tools、large-codebase、index）→ 回報「⚠️ 需主編轉知」。

## 欄位與回報

- guide 只更新「最後更新」（亮點來自已沉澱的 wiki 內容，非新日報條目，不動「最後新聞更新」）
- 回報格式：

  ```
  ## 開發實務 記者回報（weekly 彙整）
  本週亮點：N 條（or 無）
  深查段：第 X 段——已補／零證據（已查範圍）
  跨頁對帳：✅ 一致 ／ ⚠️ 失步 M 處（已改 a／需轉知 b）
  同步自查：[✅ / ⚠️ 需主編轉知（說明）]
  ```
