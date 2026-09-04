# CLAUDE.md 及規則檔修改規則

修改 `CLAUDE.md`、`.claude/commands/*.md`、`.claude/rules/*.md` 前必須讀取此檔案。

---

## 修改前：確認影響範圍

**先執行反向查詢，找出所有引用方：**
```
grep -r "被修改的檔名" .claude/commands/ .claude/rules/
```

逐一確認每個引用方在修改後仍能正確找到所需規則。若不確定影響範圍，寧可先查、再動手。

---

## 修改時：路徑引用原則

command / skill 中永遠使用明確路徑，**禁止裸露的 `CLAUDE.md`**：

| 寫法 | 判斷 |
|------|------|
| `` `wiki/CLAUDE.md` `` | ✅ 明確 |
| `` `.claude/rules/wiki-ingest.md` `` | ✅ 明確 |
| `` `CLAUDE.md` ``（無路徑前綴） | ❌ 禁止 |
| `見 CLAUDE.md`（無路徑前綴） | ❌ 禁止 |

理由：裸露路徑在重構時無法靠 grep 追蹤，容易造成 skill 靜默失效。

---

## 修改時：CLAUDE.md 設計原則

**適合放進 CLAUDE.md 的內容：**
- 有明確觸發條件的操作規則（「執行 X 時必須做 Y」）
- 可用 grep 驗證的格式規範
- 邊界判斷（單一 yes/no 問題）
- 跨 skill 共用的限制（路徑、語言、唯讀）

**不適合放進 CLAUDE.md 的內容：**
- 快速上手、安裝說明（→ `README.md`）
- 只有一個 skill 需要的格式模板（→ `.claude/rules/` 對應檔）
- 面向人類的操作範例（→ `README.md`）
- 超過 3 行的格式範本（→ `.claude/rules/` 對應檔）
- 教訓敘事（→ 該檔的沿革檔，`docs/rules-changelog/`）：條文只留判準＋「沿革檔 日期」指路，不進 agent 讀取範圍 `[加入: 2026-09-04]`

> 規則檔以「內容是否精簡、有無重複」為準，不設行數上限；長度非簡化理由（同 wiki 頁面「一頁一故事」哲學）。

---

## 修改時：機械契約字串住固定區 `[加入: 2026-09-04]`

**任何會被 script grep／regex 消費的字串（小標、表頭、標籤、格式形狀），在規格檔裡只能住「機械契約字串」表**（`weekly-report.md` 與 `news-pipeline-steps.md` Step 1b 已各設一張），正文條文引用時指回該表，不另抄一份；新增契約字串時同步登記 `.claude/review-registry.json` 的 `sync_pairs`（規格端與消費端互相指認），讓 `check_rules.py` 看守。

> 立法依據（2026-09-04 prompt review）：六個 🔴 有五個是「規格改了、機器沒跟」——契約字串散在散文裡，改文案順手就改斷（聚焦連結格式、`素材涵蓋窗`、判準凍結比對各中一次）。字串住固定表＋registry 雙看守後，這類失效在 commit 前就會紅。

**判斷式：** 這個字串有沒有任何 script 在 grep？用指令答，不憑印象——

```
grep -rn "要改的字串" scripts/ web_reader/assets/ src/tests/
```

有命中 → 進契約表＋registry（登記時**規格端與消費端各一組 pattern**，避免 `all_contain` 全檔搜尋讓同檔第二份副本掩護漂移）；零命中 → 一般文案，自由改。本檔上方「修改前：確認影響範圍」的反向查詢只掃 `.claude/`，接不到程式端——兩個 grep 都要跑。

---

## 修改後：強制驗證

**修改完成後執行 `/review-commands`，直到零錯誤才可收工。**

規則一致性已納入測試套件（`scripts/check_rules.py`，讀取 `.claude/review-registry.json` 執行裸露引用、路徑存在性、錨點、同步配對四類機械檢查），`/review-commands` 只做失敗判讀與修復，不再手動 grep。新增同步配對或錨點時登記進 `.claude/review-registry.json`，不需另外維護紙本註冊表。

**判斷標準：**
> 所有引用這個檔案的 command / skill，在修改後還能正確找到所需的規則或格式嗎？若否，先修引用再收工。
