# Anthropic 訂閱方案與計費政策

**類型：** policy
**狀態：** active（持續調整中）
**最後更新：** 2026-04-26

---

## 現行方案（2026-04）

| 方案 | 月費 | Claude Code 模型存取 |
|------|------|----------------------|
| Free | $0 | 基本限制 |
| Pro | $20 | 含 Sonnet；Opus 需另購額外用量 |
| Max | 更高 | 更高用量上限 |
| API | 按量計費 | 全模型，依 token 計費 |

> **注意**：以上為社群整理的近似資訊，確切定價請以官方頁面為準。

---

## 近期政策變動

### 2026-04-25：HERMES.md 靜默計費 bug
git commit 歷史中出現大寫字串「HERMES.md」，會觸發 Claude Code 靜默切換至 API 額外計費模式，完全繞過 Max 方案配額，已知造成用戶單日損失 **$200**。Anthropic 支援確認為 bug，但**拒絕退款**。

**立即行動**：`git log --all | grep -i HERMES` 檢查 commit 歷史。
來源：[GitHub Issue #53262](https://github.com/anthropics/claude-code/issues/53262)、[[news/2026-04-26]]

### 2026-04-25：Token 配額快速耗盡（$20 方案）
$20 Pro 方案用戶反映 Claude Code 在 **2 小時內耗盡每日配額**；使用 career-ops 等大型工具最快 30 分鐘見底。社群分享節省 token 的實務技巧（分層模型策略：以 Sonnet 為主力，需要時才讓 Sonnet「諮詢」Opus，聲稱節省約 60% 用量）。

### 2026-04-25：Anthropic 限制 OpenClaw 等第三方 agentic 工具配額
The Verge 報導 Anthropic 嚴格限制 OpenClaw 等第三方 agent 工具的使用配額。Claude Code 負責人 Boris Cherny 公開表示：「訂閱方案的設計並非為這類第三方使用模式而生。」預示 agentic 工具的付費門檻將持續提高。

### 2026-04-24：Opus 額外用量需 Pro 起
Anthropic 更新政策，使用 Claude Code 存取 Opus 模型的**額外用量**現在須先訂閱 Pro 以上方案才能開通。官方說明了三種切換模型的方式：
1. `/model` 指令
2. `--model` CLI 旗標
3. 環境變數設定

**影響**：原本以低階方案搭配額外用量的用戶受到顯著影響。

### 2026-04-24：降級後用量不重置
一名用戶回報在 Anthropic 發布重置用量承諾的六天前降級帳號，導致被排除在重置範圍外。Anthropic 拒絕為其重置，引發補償政策時間邊界的爭議。

---

## 宏觀趨勢

The Verge（2026-04-24）報導，AI 商業化壓力下，Anthropic 等實驗室開始大幅限制第三方工具用量。Claude Code 負責人 Boris Cherny 公開表示：

> 「訂閱方案的設計並非為這類第三方使用模式而生。」

此言論被視為付費門檻將持續提高的明確信號。

---

## Token 成本注意事項

- 多個 MCP Server 併用時，每條訊息可能消耗 **20,000+ tokens**（見 [[entities/claude-code]]）
- 切換至 Opus 4.7 會清除整個 prompt cache，導致額外 token 成本

---

## 相關議題

- [[topics/code-quality-decline]]（用戶因品質下滑要求退款或降級）

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-26]]
- [官方說明文件](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
