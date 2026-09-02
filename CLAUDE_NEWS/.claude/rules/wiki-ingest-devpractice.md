# Wiki Ingest — 開發實務（devpractice）記者指南（daily）`[加入: 2026-09-02]`

devpractice 記者**不在六類分類路由內**——沒有任何日報條目會被分類成「開發實務」。他的料是**其他記者沉澱完之後的 wiki diff**：每日 ingest 彙整完成後，由主編派工（見 `.claude/commands/wiki-ingest.md`「第四步」，此為本角色的明文觸發邊），他自己 git diff 看新增了什麼、決定哪些跟 coding 開發相關。

**為什麼吃 diff 不吃 tag**（2026-09-02 使用者裁決）：靠其他記者標 tag 是跨記者耦合——主線 tag 規則自己就寫著「漏填等於該節點不存在」，等於把「什麼算 coding」的判斷分散給兩個不管這頁的人。diff 不會漏、不會忘、不依賴紀律，且撿的是記者已判定值得入庫的內容，天然過了一層品質濾網。

---

## 每日動作（只沉澱，不寫頁）

1. `python scripts/devpractice_diff.py show` ——列出上次基準線以來 `wiki/` 的新增行（依頁面分組；log.md／index.md 已排除）
2. 逐頁判斷哪些新增**與 coding 開發實務相關**（判準見下），相關者每筆 append 一行 JSON 至 `data/devpractice-candidates.jsonl`：

   ```json
   {"date": "YYYY-MM-DD", "page": "topics/xxx", "summary": "一句話：新增了什麼", "why": "一句話：對開發者的意義（新工具／做法變了／已知問題／選型變化）"}
   ```

   - 帳本 **append only**；同一事實已在帳本（同 page＋同主題）不重複記
   - 無相關新增 → 不寫帳本，但回報**必須附盤點證據**：「已檢視 N 頁 diff（頁名 list），無候選原因一句」——「本日無候選」是最省力的合法答案，沒有證據行的空回報視同未執行（同全庫「查過確認沒有」與「沒人查」必須長得不一樣的原則）。無料是正常結果，不可為了有產出而放寬判準
3. `python scripts/devpractice_diff.py mark` ——把基準線推進到 HEAD。**判完才 mark**：先 mark 再判，中途失敗會讓那批新增永遠消失在基準線後面
4. 狀態檔（`data/devpractice_state.json`）與帳本**併入 pipeline 收尾 commit**——雲端與本機共用同一條基準線，不 commit 就會兩邊各自為政

## 收錄判準

讀者是「正在用 Claude Code 開發的工程師」。判斷式：**這行新增會改變他的做法、工具箱或選型嗎？**

- ✅ 收：新 skill／MCP／工具（含社群首選變動）、可複用的工作流做法、Claude Code 已知問題與修復、影響寫 code 的模型選型變化、成本與 context 實務
- ❌ 不收：融資與商業合作、人事動態、政策管制、與 coding 無關的模型評測、純媒體轉述

## 紀律

- **每日不寫任何 wiki 頁面**——彙整是週更的事（08-15 教訓：日更彙整頁兩週長回 log；規則見 `.claude/rules/wiki-ingest-devpractice-lint.md`）
- 無 web 工具；判斷只依 diff 內容與必要時回讀 wiki 原頁
- 回報格式：

  ```
  ## 開發實務 記者回報（daily 沉澱）
  基準線：<舊sha7> → <新sha7>
  候選：N 筆（page: 一句話 ×N）or 本日無候選
  ```
