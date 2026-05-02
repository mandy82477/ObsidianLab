# Claude Security

**類型：** product
**狀態：** public beta（公開測試版）
**首次出現：** 2026-04-30
**最後更新：** 2026-05-02

---

## 現況

Claude Security 於 2026-04-30 宣布推出公開測試版，並於 2026-05-01 正式向**全部 Enterprise 客戶**開放。ZDNET、SecurityWeek、SiliconANGLE、CRN、Pulse 2.0 等多家媒體報導。這是 Anthropic 首次以**獨立資安產品形式**跨足 AI 輔助資安市場，直接整合於 Claude Code 開發環境。

核心運作方式：以類安全研究員的方式**讀取 Git 歷史**、**跨檔案追蹤資料流**，目標大幅降低傳統規則掃描的誤報率。多位開發者指出「**推理式驗證（reasoned verification）**」才是本次發布真正的差異化設計決策——工具可自動確認漏洞真實性並提出修復建議，而非僅標記疑似問題。

---

## 核心差異化

與傳統 CVE 掃描器相比，Claude Security 的關鍵差異在於：
- **情境化安全評估**：結合應用程式的**業務邏輯**提供安全評估，而非僅比對已知 CVE 資料庫
- **開發流程整合**：直接嵌入 Claude Code 環境，在開發階段即攔截安全問題
- **架構層理解**：能判斷「應用邏輯是否安全」，補足傳統 SAST 工具的盲點

社群工具 **Trent**（Show HN: 2026-04-30）提供類似定位——在 Claude Code 環境中提供應用架構層級的安全評估，可視為 Claude Security 的社群先行版本。

---

## 競品關係

- **傳統 SAST 工具**（SonarQube、Checkmarx 等）：僅掃描已知漏洞模式，不理解業務邏輯
- **Bugcrawl**（Anthropic 內部工具，見 [[entities/bugcrawl]]）：較早期的 Claude Code 漏洞偵測測試工具
- **Mythos**（見 [[entities/mythos]]）：能力更強的 AI 資安模型，目前未公開；Claude Security 可能使用不同底層能力

---

## 相關實體

- [[entities/claude-code]]
- [[entities/mythos]]
- [[entities/bugcrawl]]

## 參考來源

- [[news/2026-04-30]]

## 歷史記錄

| 日期 | 事件 |
|------|------|
| 2026-05-01 | Claude Security 正式向全部 Enterprise 客戶開放；社群討論「推理式驗證」為核心差異 |
| 2026-04-30 | Claude Security 公開測試版正式推出，多家資安媒體同步報導 |
