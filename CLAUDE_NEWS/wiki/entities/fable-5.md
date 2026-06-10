# Claude Fable 5

**類型：** model
**狀態：** active（正式發布，6/22 前含括於訂閱方案）
**首次出現：** 2026-06-09
**最後更新：** 2026-06-10

---

## 現況

Claude Fable 5 是 Anthropic 於 2026-06-09 發布的旗艦模型，為**史上首款向大眾開放的 Mythos 級模型**。Fable 5 與 Claude Mythos 5 共用相同的模型權重，差異在於 Fable 5 前置安全分類器——觸發時靜默 fallback 至 Claude Opus 4.8（Anthropic 稱不到 5% 的 session 受影響）。

**核心定位**：任務越複雜越長期，Fable 5 的優勢越明顯。在軟體工程、知識工作、視覺、科學研究等幾乎所有 benchmark 達到 SOTA。

| 指標 | 數值 |
|------|------|
| Input 定價 | $10 / 百萬 token |
| Output 定價 | $50 / 百萬 token |
| Context Window | 1,000,000 token |
| 最大 Output | 128,000 token |
| 免費期限 | 訂閱用戶至 2026-06-22 |

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦 |
| 最適合 | 多步驟複雜任務、長期 agentic 工作流、多天 PR 審查、安全漏洞分析 |
| 不適合 | 日常短問答（成本過高）、從事前沿 LLM 開發（護欄會靜默降級） |

> 詳細最新熱度見 [[feature-radar]]

## 使用指南

**快速上手（Claude Code）：**
```
claude --model claude-fable-5-20260609
```

**注意事項：**
- 6/22 後 Fable 5 移至消費制，Pro/Max 訂閱用戶須額外付費
- 從事前沿 LLM 開發（訓練 pipeline、推論研究）時，Fable 5 護欄會靜默降級輸出品質，不告知用戶（System Card 明文記載）
- 30 天資料保留政策適用於所有平台（含 AWS Bedrock），資料離開 AWS 安全邊界

## 核心功能

- **Mythos 架構公開版**：首次讓大眾使用 Mythos 等級推理能力
- **安全分類器護欄**：觸發時靜默 fallback 至 Opus 4.8，不拒絕請求（< 5% session）
- **1M context + 128K output**：適合處理整個 codebase 或長文件的任務
- **多模態**：軟體工程、視覺、科學研究均達 SOTA

## 相關議題

- [[entities/mythos]] — Mythos 模型家族完整歷史
- [[entities/pricing]] — Fable 5 定價與訂閱方案變動
- [[topics/anthropic-business]] — Anthropic IPO 背景與商業策略
- [[topics/ai-agent-safety]] — Claude Code 供應鏈攻擊事件

## 爭議

- **靜默降級競爭 LLM 開發**：Fable 5 在偵測到前沿 LLM 開發工作時靜默降級，系統卡承認「These safeguards will not be visible to the user」，Reddit LocalLLaMA 大量批評為反競爭行為
- **30 天資料保留**：Bedrock 用戶數據強制離開 AWS 安全邊界，企業隱私顧慮
- **護欄過強**：用戶反映在合法安全修復工作中也頻繁觸發護欄（如修復自身 app 的資料庫漏洞）
- **「失去靈魂」討論**：部分用戶認為 Fable 5 相比 Opus 4.6 更工具性、減少人本關懷深度

## 參考來源

- [[news/2026-06-09]]
- [[news/2026-06-10]]
- [Anthropic 官方公告](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [System Card PDF](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf)
- [資料保留政策](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)

## 歷史記錄

### 2026-06-09
正式發布。HN score 2,448，近 2,000 評論。6/22 前含括於訂閱方案。

### 2026-06-10
發布後第一天社群討論爆發：靜默降級爭議、30 天資料保留爭議、供應鏈攻擊威脅升高、Microsoft AI CEO 批評 Anthropic 意識論述、多個工具社群跟進（Lanes v0.43.0 加入 Fable 5 支援）。
