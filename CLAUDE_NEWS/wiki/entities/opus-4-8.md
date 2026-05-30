# Claude Opus 4.8

**類型：** model
**狀態：** active
**首次出現：** 2026-05-28
**最後更新：** 2026-05-29

---

## 現況

Claude Opus 4.8 於 2026-05-28 正式發布，是目前 Anthropic 最高階的公開模型。同步推出 Dynamic Workflows（Research Preview）與 Fast Mode 降價，是 2026 年以來 Anthropic 發布規模最大的旗艦更新。

---

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 大型 agentic 任務、multi-step 工作流、需要 1M context 的長文件處理 |
| 不適合 | 追求穩定性的生產環境（初期社群反映有行為退步）|

> 詳細最新熱度見 [[feature-radar]]

---

## 核心指標

| 項目 | 數值 |
|------|------|
| SWE-bench Pro | 69.2% |
| Context Window | 1M tokens |
| 定價 | 與 Opus 4.7 相同 |
| Fast Mode 速度 | 2.5× 標準速度 |
| Fast Mode 費用 | 前代的 1/3 |
| Dynamic Workflows 子代理上限 | 1,000 個平行子代理 |

---

## 新功能

### Dynamic Workflows（Research Preview）

允許 Claude Code CLI、Desktop 及 VS Code 擴充在單一 session 內動態撰寫 orchestration scripts，最多啟動 **1,000 個平行子代理**，處理超大規模工作：

- 跨 service 的 bug hunt
- 觸及數百個檔案的大型 migration
- 多角度壓力測試

**目前限制：** Research Preview，限 Max 方案用戶。見 [[feature-radar]]。

```bash
# Dynamic Workflows 在 Claude Code CLI 中自動啟用（Max 方案）
claude code "Migrate all legacy API endpoints in this monorepo"
```

### Fast Mode

Opus 4.8 的 Fast Mode（2.5× 速度）費用降至前代的 **1/3**，顯著降低高速推論的成本門檻。

### 使用者可控任務努力程度

claude.ai 用戶現可調節 Claude 在任務上投入的努力程度，不再完全由模型自行決定。

---

## 社群初期反映

### 正面
- HN score 1662（發布後 24 小時最高討論量）
- Dynamic Workflows 被視為 Claude Code 工作流的重大突破
- Fast Mode 降價受到廣泛歡迎

### 負面（待觀察）
- Reddit 部分用戶反映 4.8 引入奇怪的 "pecl scripts" 行為，強制使用自訂工具做簡單文件修改
- "thinking blocks cannot be modified" 400 錯誤：v2.1.156 已修復（[[entities/claude-code]]）
- MarginLab SWE-bench-Pro 追蹤發現：Opus 4.7 在 4.8 發布前一週有統計顯著下降，發布後立即恢復（見 [[topics/code-quality-decline]]）
- **UltraCode 嚴重 bug（2026-05-30）**：Dynamic Workflows 用戶回報 1.7M tokens 消耗後零輸出；8 個子代理陷入退化迴圈（結果未快取、多次重新部署）；Anthropic 無退款機制；建議生產環境設定嚴格 token 上限
- **德語品質退步（2026-05-29–30）**：德語用戶反映文法異常、Max Thinking 模式過慢；整體感覺不及 Opus 4.6 穩定（Reddit）
- **Qwen distillation 爭議（2026-05-29–30）**：社群截圖流傳 Opus 4.8 自稱 Alibaba Qwen；主流判斷為 proxy 詐騙服務而非真實 distillation（HN score 20）

---

## 與前代比較

| 指標 | Opus 4.7 | Opus 4.8 |
|------|---------|---------|
| SWE-bench Pro | — | 69.2% |
| Context Window | — | 1M tokens |
| Dynamic Workflows | ❌ | ✅ Research Preview |
| Fast Mode 費用 | 基準 | 1/3 |
| 定價 | 基準 | 同價 |

---

## 核心功能
- [[entities/claude-code]]（Dynamic Workflows 整合）
- [[feature-radar]]（功能熱度追蹤）

## 相關議題
- [[topics/code-quality-decline]]（升版前效能下降事件）
- [[entities/opus-4-7]]（前代模型）
- [[topics/anthropic-business]]（同步融資公告背景）

## 參考來源
- [[news/2026-05-29]]
- [Claude Opus 4.8 官方公告](https://www.anthropic.com/news/claude-opus-4-8)
- [Dynamic Workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-05-28 | 正式發布，HN 1662 分；Dynamic Workflows Research Preview 同步推出；Fast Mode 降至前代 1/3 費用 |
| 2026-05-30 | UltraCode 嚴重 bug 揭露：1.7M tokens 消耗無輸出，Anthropic 無退款；Qwen distillation 爭議（社群主流否定）；德語品質投訴；v2.1.158 Auto mode 擴展至 Bedrock/Vertex/Foundry |
| 2026-05-29 | v2.1.156 修復 thinking blocks 400 錯誤；社群混合反映（行為退步投訴 + 大型任務好評）|
