# 主編官方查證檔骨架（`docs/page-audits/{slug}-{date}-verified.md`）

方法見 `../SKILL.md`「主編官方查證」。與健檢卡、冷讀者同時開工；查證結果分次 append，每次新增一節並 SendMessage 通知在跑的設計者與評審「第 n 節新增」。

```
# 主編官方查證 — {slug}（{date}）

行號為檔案原始行號（含 frontmatter）。記者與 agent 無 web 工具；本檔對照「頁面 vs 一手現況」。

## 一、頁面既有數字對官方（{n} 項）

| 頁面條目（行） | 官方現況（逐字引用＋連結＋日期） | 判定 |
|---|---|---|
| … | … | ✅ 一致／⚠️ 二手交叉／**事實更正** |

**官方頁面有、本頁沒有、但讀者會問的**（供設計者判斷要不要收）：
- …

## 二、{考題的錨：某題官方原文}

- …（適用範圍寫清楚：官方只寫哪個版本／哪些方案）

## 三、逾期懸置 {n} 筆（去重後 {m} 事實）處置建議

| 行 | 懸置 | 查證結果 | 處置（✅ 結案／事實更正／❓ 維持＋新複查日／二手待補） |
|---|---|---|---|

未查（媒體轉述型，記者依日報回訪）：…。同一事件掛在幾處：…。

## 四、給設計者的三句話

1. 本頁最缺的一句官方立場：…
2. 跑錯家的事：…
3. 可合併的懸置：…

## 五、{第二輪：健檢卡查證表 V1…／複驗後補查}
```

常用一手來源：`platform.claude.com/docs/en/about-claude/pricing`、`/models/overview`、`/managed-agents/overview`；`claude.com/blog`、`anthropic.com/news`、`support.claude.com`；`gh api repos/anthropics/claude-code/contents/CHANGELOG.md -H "Accept: application/vnd.github.raw"`；`gh issue view <n> -R anthropics/claude-code --json state,updatedAt,comments,labels`。抓不到（403／404）才 WebSearch 多家交叉並標二手。
