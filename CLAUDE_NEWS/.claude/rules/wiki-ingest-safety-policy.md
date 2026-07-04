# Wiki Ingest — 安全政策記者指南

分類為「安全政策」的新聞條目由此記者負責。讀此檔後直接操作，需建立新頁面時另讀 `.claude/rules/wiki-ingest-format.md`。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/topics/anthropic-government-policy.md` | Anthropic 與各國政府互動、出口管制、軍事合約 |
| `wiki/topics/ai-agent-safety.md` | AI agent 安全事件、漏洞披露、提示注入 |
| `wiki/topics/recursive-self-improvement.md` | AI 遞歸自我改進、全球監管呼籲 |

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 🏛️ 政策/安全 的所有頁面（含日後新增）皆由本記者負責維護與 lint。

---

## anthropic-government-policy 更新規則 `[加入: 2026-06-18]`

**觸發條件：** 日報出現 Anthropic 與美國政府（或其他國家政府）的新互動事件。

**每次 ingest 後依序：**
1. 在 `## 攻防紀錄` 表格**最上方** prepend 新行（格式：`| 日期 | 🏛️/🏢/🌐 | 動作 | 效果 |`）
2. 更新 `## 目前局勢` 的管制狀態、雙方底線、意外效果（如有變化）
3. 若事件影響三個戰場的任一條故事線，在對應的 `## 三個戰場` 子段落補充說明
4. 在 `## 時序` prepend 新日期區塊
5. 更新頁面「最後更新」日期

---

## ai-agent-safety 更新規則

**觸發條件：**
- 新的 Claude Code 安全漏洞披露（含 CVE 或具名披露）
- 提示注入攻擊案例（遠端或本地）
- 惡意套件 / 假冒安裝包事件
- Anthropic 官方安全回應聲明

**更新動作：**
1. 在 `## 事件記錄` 最上方 prepend 新條目（`### YYYY-MM-DD 事件名稱`）
2. 更新 `## 摘要` 若有整體態勢變化
3. 更新「最後更新」日期

---

## 回報格式

```
## 安全政策 記者回報
更新頁面：[list]
feature-radar 新增：無
index.md 狀態變更：[page: 舊狀態 → 新狀態 or 無]
新增頁面：[filepath or 無]
同步自查：[✅ 已同步 / ⚠️ 需主編轉知（說明）/ 不適用]
```
