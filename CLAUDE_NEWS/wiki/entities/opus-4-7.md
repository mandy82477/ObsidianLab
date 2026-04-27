# Claude Opus 4.7

**類型：** model
**狀態：** active（爭議中）
**首次出現：** 2026-04-24
**最後更新：** 2026-04-27

---

## 現況

Claude Opus 4.7 於 2026-04-24 正式發布，是目前 Anthropic 最高階的公開模型。伴隨發布的還有 Rate Limits API（管理員可程式化查詢速率限制）與 Managed Agents Memory Beta（在 `managed-agents-2026-04-01` 請求標頭下啟用）。

然而，該模型在社群中引發大量爭議，主要集中在定價策略與自適應思考深度的問題。

---

## 已知問題與爭議

### 思考深度不可控
Opus 4.7 由模型自行決定思考深度，而非由使用者控制。社群反映在需要深度推理的問題上，模型有時給出淺薄回應。這與使用者對「旗艦模型」的期待存在落差。

### 定價門檻提高
- 使用 Claude Code 存取 Opus 模型的**額外用量**現需 **Pro 以上方案**才能啟用
- 見 [[entities/pricing]]

### Usage Policy 隨機觸發拒絕（2026-04-26 以來）
Hacker News 多名用戶反映自 Opus 4.7 版本以來，Claude Code 頻繁出現隨機觸發 Usage Policy 拒絕的錯誤，無明確觸發條件。官方暫時建議切換至 `/model claude-sonnet-4-20250514` 作為緩解手段；根本原因尚未公開說明。

### Prompt Cache 問題
從其他模型切換至 Opus 4.7 時，整個 prompt cache 會被清除，對大型專案造成顯著的 token 成本增加。

### Transparency Hub 缺席
社群發現 Anthropic 未將 Opus 4.7 與 Mythos Preview 納入透明度中心（Transparency Hub），引發對資訊公開一致性的質疑。

---

## 同步發布功能

- **Rate Limits API**：允許管理員以程式化方式查詢當前速率限制
- **Managed Agents Memory Beta**：跨 session 持久記憶，透過請求標頭 `managed-agents-2026-04-01` 啟用

---

## 社群觀點

> 「Opus 4.7 可以用一個改變來拯救：讓使用者控制思考深度，而非模型自行決定。」
> — Reddit r/ClaudeAI

HN 討論（2026-04-27）顯示社群對 Sonnet 與 Opus 實際差距看法分歧：部分重度使用者認為兩者表現相近，但也有人指出 **Opus 在 context 不完整時明顯更穩定**，Sonnet 的非預期失誤率達 20–35%。此討論與隨機 Usage Policy 拒絕問題同步出現，使部分用戶暫時轉回 Sonnet。

---

## 相關議題

- [[topics/code-quality-decline]]

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-27]]
