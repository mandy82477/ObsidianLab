# 大型企業 AI 編碼工具使用追蹤

**狀態：** ongoing
**開始日期：** 2026-05-26
**最後更新：** 2026-05-26

## 摘要

追蹤各大型企業目前正在使用的 AI 編碼工具，以及工具選擇的變化軌跡。資料來源為公開報導與內部消息洩露，僅記錄有明確來源佐證的事實。

---

## 企業工具使用現況

> 狀態說明：✅ 使用中 ／ ⚠️ 縮減中 ／ 🔄 切換中 ／ ❌ 已退出 ／ ❓ 未確認

| 企業 | 規模 | AI 編碼工具 | 狀態 | 備註 | 最後確認 |
|------|------|-----------|------|------|---------|
| Microsoft | 頂尖 | GitHub Copilot CLI | ✅ | 從 Claude Code 切換；6/30 完全停用 Claude Code | 2026-05-25 |
| Microsoft | 頂尖 | Claude Code | ❌ | 數月燒完全年 AI 預算，6/30 正式停用 | 2026-05-25 |
| Amazon | 頂尖 | Claude Code | ✅ | 雙軌並行，不押注單一供應商 | 2026-05-05 |
| Amazon | 頂尖 | OpenAI Codex | ✅ | 雙軌並行，與 Claude Code 同時部署 | 2026-05-05 |
| Uber | 頂尖 | Claude Code | ⚠️ | 4 個月燒完全年 AI 預算，Uber CTO 承認成本失控 | 2026-05-18 |
| Apple | 頂尖 | Claude（API） | ✅ | 外洩文件確認內部採用，非 Claude Code | 2026-05-01 |
| KPMG | 大型 | Claude | ✅ | 戰略合作，重新定義客戶服務 | 2026-05-25 |
| iCapital | 大型 | Anthropic API | ✅ | 替代資產平台，為客戶建立 AI 工具 | 2026-05-01 |
| UiPath | 大型 | Claude Code + Codex | ✅ | RPA 平台同時整合兩套工具 | 2026-05-12 |
| 哈佛 FAS | 大型 | Claude | ✅ | 取代 ChatGPT Edu，學術授權 | 2026-04-28 |

---

## 工具競爭態勢（企業視角）

| 工具 | 企業採用數 | 趨勢 | 主要阻力 |
|------|----------|------|---------|
| Claude Code | 3（Amazon、Uber、UiPath） | ⚠️ 成本壓力浮現 | 缺乏企業層級預算管控 |
| Claude（API） | 4（Apple、KPMG、iCapital、哈佛） | 🟢 持續擴張 | — |
| GitHub Copilot CLI | 1（Microsoft） | 🟢 Microsoft 背書 | 生態鎖定 |
| OpenAI Codex | 2（Amazon、UiPath） | 🟢 快速成長 | — |

---

## 市場分層觀察

- **頂尖企業（>10 萬員工）**：成本是最大決策因子。Microsoft 退出、Uber 警戒，Amazon 雙軌分散風險
- **大型企業（1–10 萬員工）**：以 API 整合為主（KPMG、iCapital），不直接讓工程師用 Claude Code
- **新創圈**：Business Insider（2026-05-23）確認 Claude Code 已取得主導地位，Cursor 份額下滑

---

## 時序

### 2026-05-25
- **Microsoft 宣布 6/30 完全停用 Claude Code**：Cybernews 報導，原因是數月內燒完整年 AI 預算

### 2026-05-12
- **UiPath 同時整合 Claude Code 與 Codex**：RPA 龍頭進入 AI 編碼工具市場，雙平台策略

### 2026-05-05
- **Amazon 雙品牌並行部署**：全體員工同時開放 Claude Code 與 Codex

### 2026-05-01
- **Apple 內部採用 Claude 確認**：外洩文件，企業滲透觸及科技業頂層
- **Uber 成本問題首報**：Forbes 後於 5/18 深度確認

### 2026-04-28
- **哈佛 FAS 以 Claude 取代 ChatGPT Edu**：學術機構結構性轉換

---

## 相關實體

- [[topics/competitor-landscape]]
- [[topics/enterprise-cost-management]]
- [[entities/claude-code]]

## 參考來源

- [[news/2026-05-25]]
- [[news/2026-05-18]]
- [[news/2026-05-15]]
- [[news/2026-05-12]]
- [[news/2026-05-05]]
- [[news/2026-05-01]]
- [[news/2026-04-28]]
