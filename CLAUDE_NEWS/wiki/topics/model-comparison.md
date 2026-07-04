# Claude 模型選型對照

**狀態：** ongoing
**領域：** 🤖 模型
**開始日期：** 2026-07-02
**最後更新：** 2026-07-04
**最後新聞更新：** 2026-07-02

> **最新陣容變化**（2026-07-02）
> Sonnet 5 於 07-01 發布並成為 Claude Code 預設（促銷 $2/$10 至 8/31）；同日 Fable 5 / Mythos 5 出口管制解除、全球恢復。目前公開陣容五級：Fable 5（旗艦）> Opus 4.8 > Sonnet 5（主力）> Sonnet 4.6 > Haiku 4.5。

---

## 摘要

本頁回答一個問題：**「我該用哪個 Claude 模型？」** 各模型的深度資訊（爭議、時序、已知問題）在各自的 entities 頁；本頁只做橫向對照與情境推薦，模型陣容變化時同步更新。

## 快速選型表

| 模型 | 定位 | 定價（in/out per Mtok）| Context | 最適合 | 不適合 | 狀態 |
|------|------|------|------|------|------|------|
| [[entities/fable-5\|Fable 5]] | 旗艦（Mythos 級公開版） | $10 / $50 | 1M | 多步驟複雜任務、長期 agentic 工作流、安全漏洞分析 | 日常短問答（太貴）；前沿 LLM 開發（護欄靜默降級） | ✅ 已解禁（7/7 後訂閱改 usage-based） |
| [[entities/opus-4-8\|Opus 4.8]] | 次旗艦 | ~$5 / $25（估計） | 1M | 大型 agentic 任務、1M context 長文件、Fast Mode 省時場景 | 追求穩定性的生產環境（曾有行為退步回報） | ✅ Active |
| [[entities/sonnet-5\|Sonnet 5]] | **主力平衡選項（Claude Code 預設）** | $2 / $10（促銷至 8/31） | 1M | agentic 工作流、Claude Code 日常、tool use 密集、成本敏感 | 需要 Mythos 級推理深度的極複雜任務 | ✅ Active（v2.1.197 預設） |
| Sonnet 4.6 | 前代主力 | 低於 Sonnet 5 正式價 | 200K | 已驗證穩定的既有工作流；偏好其互動個性者 | 新專案（Sonnet 5 促銷期 CP 值更高） | ✅ Active |
| Haiku 4.5 | 輕量 worker | 最低 | 200K | 混合架構低成本 subagent、批量簡單任務 | 複雜推理、長鏈 agentic 任務 | ✅ Active |
| [[entities/opus-4-7\|Opus 4.7]] | 已被取代（第三階） | 同 4.8 | 200K | agentic coding 仍有口碑 | 新採用（已有兩代後繼） | ⚠️ 已被取代 |
| [[entities/mythos\|Mythos 5]] | 無護欄完整版 | — | — | 授權機構的安全研究 | 一般開發用途（非此定位） | ✅ 已解禁（僅限授權機構/安全研究用途，非一般消費市場） |

## 情境推薦

| 你的情境 | 建議 | 理由 |
|---------|------|------|
| Claude Code 日常開發 | **Sonnet 5**（預設即是） | 效能接近 Opus 4.8、成本約 60%，1M context |
| 跨多天的複雜 agentic 任務 | **Fable 5** | 任務越複雜越長期優勢越明顯；注意 7/7 後計費變化 |
| 資安審查 / 漏洞分析 | **Fable 5**（留意誤判） | 能力最強，但 07-02 起 Defense in Depth 分類器有誤判實測 |
| 需要壓成本的批量任務 | **Haiku 4.5 做 worker + Sonnet 5 做協調** | 社群驗證的混合架構模式 |
| 生產環境求穩 | **Sonnet 4.6 或 Sonnet 5** | Opus 4.8 曾有行為退步與 529 事件記錄 |

## Benchmark 對照（有來源者才列）

| 指標 | Fable 5 | Opus 4.8 | Sonnet 5 | 備注 |
|------|---------|----------|----------|------|
| SWE-bench Pro | SOTA（官方） | 69.2% | 接近 Opus 4.8（社群評測） | Sonnet 5 官方對比圖表有修改爭議（2026-07-02） |
| 綜合定位 | 幾乎所有 benchmark SOTA | 第三方評測曾小輸 Gemini 3.5 Flash（35.4 vs 34.8，主因指令遵循） | agentic / tool use 接近次旗艦 | 各數據測試日期與條件見各模型頁 |

> 數據截至 2026-07-02；詳細評測條件與矛盾結果並陳原則見各模型 entities 頁。

## 相關實體

- [[entities/fable-5]] · [[entities/opus-4-8]] · [[entities/sonnet-5]] · [[entities/opus-4-7]] · [[entities/mythos]]
- 功能熱度與升版建議：[[feature-radar]]
- 定價細節：[[entities/pricing]]

## 時序（陣容變化）

- 2026-07-01：Sonnet 5 發布（Claude Code 預設）；Fable 5 / Mythos 5 解禁
- 2026-06-13：Fable 5 / Mythos 5 出口管制停用（至 06-30）
- 2026-06-09：Fable 5 發布，Opus 4.8 退居次旗艦
- 2026-05-28：Opus 4.8 發布
- 2026-04-24：Opus 4.7 發布
