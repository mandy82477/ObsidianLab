# Claude Sonnet 5

**類型：** model
**狀態：** active（正式發布）
**領域：** 🤖 模型
**首次出現：** 2026-07-01
**最後更新：** 2026-07-02
**最後新聞更新：** 2026-07-02

> **最新動態**（2026-07-02）
> 發布次日出現兩則爭議性回饋（皆屬主觀/分析性質，非量化評測）：HN 一篇分析文章指 Anthropic 修改了官方對比圖表（原版本讓 Sonnet 5 表現不佳），引發資料呈現可信度討論（score 3，訊號弱）；同時 Reddit 多位使用者反映 Sonnet 5 雖智力提升，但互動個性/語氣不如 Sonnet 4.6。

---

## 現況

Claude Sonnet 5 於 2026-07-01 正式發布，定位為 Anthropic **最 agentic 的 Sonnet 模型**，在 reasoning、tool use、coding、knowledge work 等多個面向均有顯著提升，效能接近 Opus 4.8。

**與 [[entities/fable-5]] 的定位差異**：Fable 5 是目前最高階旗艦（Mythos 級推理能力，適合最複雜的多步驟任務）；Sonnet 5 則是主力平衡選項——以約 60% 的成本換取接近 Opus 4.8 的效能，適合日常 agentic 工作流與成本敏感場景，非追求極致推理深度的定位。

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
- **1M token context**：原生支援，無需外部管理
- **Claude Code 預設**：v2.1.197 起為 Claude Code 預設模型

**待驗證：** 社群評測提及 Sonnet 5 在 Terminal-Bench 2.1（2026-06）leaderboard 有排名，且「#1 仍為外界無法取用的型號」，但缺乏具體名次數字與來源連結，暫不列為已確認核心能力。

## 爭議

- ⚠️ **官方對比圖表遭質疑修改（2026-07-02，待核實）**：分析文章指出 Anthropic 修改了官方 Sonnet 5 對比圖表，該圖表原版本呈現 Sonnet 5 表現較差（[vincentschmalbach.com](https://www.vincentschmalbach.com/anthropic-changed-sonnet-5-chart-after-it-made-sonnet-look-bad/)，HN score 3）；HN score 3 訊號極弱，且原文未提供修改前後圖表對照的完整存檔連結，暫列「待核實」，不寫成定論
- ⚠️ **個性/語氣不如 Sonnet 4.6（主觀回饋）**：Reddit 多位使用者反映 Sonnet 5 智力提升但互動個性流失——Sonnet 4.6 原本較有個性、懂得對話節奏、簡短回應精準，Sonnet 5 感覺更像通用「help」助手而非有特色的對話夥伴（[Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ulf5xc/something_important_was_lost_between_sonnet_46/)）；屬主觀體驗回饋，非量化評測，與 Fable 5「失去靈魂」討論（見 [[entities/fable-5]] 爭議區）呈現類似的世代模型「個性 vs 能力」取捨模式（推論）

## 相關議題

- [[entities/fable-5]] — 現任最高階公開模型；Sonnet 5 為次階平衡選項，定位差異見上方「現況」
- [[entities/opus-4-8]] — Opus 4.8 能力對比（Sonnet 5 效能接近 Opus 4.8）
- [[entities/pricing]] — 完整定價與促銷方案細節
- [[entities/claude-code]] — Claude Code v2.1.197 更新

## 參考來源

- [Anthropic Blog：Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)（2026-07-01）
- [[news/2026-07-01]]

## 歷史記錄

### 2026-07-02
**發布次日爭議：圖表可信度質疑 + 個性流失回饋**：
- **官方圖表修改爭議（待核實）**：HN 文章指控 Anthropic 修改官方 Sonnet 5 對比圖表，原版本讓 Sonnet 5 表現不佳（[vincentschmalbach.com](https://www.vincentschmalbach.com/anthropic-changed-sonnet-5-chart-after-it-made-sonnet-look-bad/)），HN score 3 訊號弱，尚待更多獨立來源佐證
- **個性流失回饋**：Reddit 多位使用者反映 Sonnet 5 相較 Sonnet 4.6 智力提升但互動個性/語氣弱化，感覺更通用化（[Reddit](https://www.reddit.com/r/ClaudeAI/comments/1ulf5xc/something_important_was_lost_between_sonnet_46/)），屬主觀體驗，非量化評測

### 2026-07-01
**正式發布**：Claude Sonnet 5 正式上線，定位最 agentic Sonnet。效能接近 Opus 4.8，促銷定價 $2/$10 per Mtok 至 2026-08-31。Claude Code v2.1.197 設為預設模型。Terminal-Bench 2.1（2026-06）有明確排名；社群稱「cost reset for AI agents」（多篇社群評測，待具體 benchmark 連結補充）。
