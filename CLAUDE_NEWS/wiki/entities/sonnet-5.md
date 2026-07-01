# Claude Sonnet 5

**類型：** model
**狀態：** active（正式發布）
**領域：** 🤖 模型
**首次出現：** 2026-07-01
**最後更新：** 2026-07-01
**最後新聞更新：** 2026-07-01

> **最新動態**（2026-07-01）
> Claude Sonnet 5 正式發布，定位為最 agentic 的 Sonnet 模型（[Anthropic Blog](https://www.anthropic.com/news/claude-sonnet-5)）。效能接近 Opus 4.8，促銷定價 $2/$10 per Mtok 至 2026-08-31。Claude Code v2.1.197 已將 Sonnet 5 設為預設模型，社群稱之為「cost reset for AI agents」。

---

## 現況

Claude Sonnet 5 於 2026-07-01 正式發布，定位為 Anthropic **最 agentic 的 Sonnet 模型**，在 reasoning、tool use、coding、knowledge work 等多個面向均有顯著提升，效能接近 Opus 4.8。

**Claude Code 預設模型**：Claude Code v2.1.197 起已將 Sonnet 5 設為預設模型，取代前一代 Sonnet 版本。

**定價**：促銷定價 $2/$10 per Mtok（input/output）有效期至 2026-08-31。相較 Opus 4.8（$5/$25，估計）成本差距約 60%，社群稱此為「cost reset for AI agents」。

**1M context window**：原生支援 100 萬 token 上下文，與 Fable 5 / Opus 4.8 相同。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ✅ 廣泛推薦 |
| 最適合 | agentic 工作流、Claude Code 日常使用、tool use 密集任務、成本敏感場景 |
| 不適合 | 需要 Mythos 級推理深度的極複雜長期任務（此時考慮 Opus 4.8） |

> 詳細最新熱度見 [[feature-radar]]

## 使用指南

**快速上手（Claude Code）：**
```
# Claude Code v2.1.197 已預設使用 Sonnet 5，無需指定
claude

# 明確指定：
claude --model claude-sonnet-5-20260701
```

**注意事項：**
- 促銷定價 $2/$10 per Mtok 有效期至 2026-08-31，之後定價待公布
- 效能接近 Opus 4.8，但 60% 成本差距使其在 agentic 工作流中具備明顯性價比優勢
- 1M context 原生支援，適合整個 codebase 的大型 agentic 任務

## 核心能力

- **Agentic 定位**：reasoning、tool use、coding、knowledge work 全面提升，是 Anthropic 目前最強 agentic Sonnet
- **效能 vs Opus 4.8**：社群多篇評測確認在 agentic 任務上效能接近 Opus 4.8，60% 成本差距
- **Terminal-Bench 2.1（2026-06）**：Sonnet 5 在 leaderboard 有明確排名；#1 仍為外界無法取用的型號（待核實細節）
- **1M token context**：原生支援，無需外部管理
- **Claude Code 預設**：v2.1.197 起為 Claude Code 預設模型

## 相關議題

- [[entities/opus-4-8]] — Opus 4.8 能力對比（Sonnet 5 效能接近 Opus 4.8）
- [[entities/pricing]] — 完整定價與促銷方案細節
- [[entities/claude-code]] — Claude Code v2.1.197 更新

## 參考來源

- [Anthropic Blog：Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)（2026-07-01）
- [[news/2026-07-01]]

## 歷史記錄

### 2026-07-01
**正式發布**：Claude Sonnet 5 正式上線，定位最 agentic Sonnet。效能接近 Opus 4.8，促銷定價 $2/$10 per Mtok 至 2026-08-31。Claude Code v2.1.197 設為預設模型。Terminal-Bench 2.1（2026-06）有明確排名；社群稱「cost reset for AI agents」（多篇社群評測，待具體 benchmark 連結補充）。
