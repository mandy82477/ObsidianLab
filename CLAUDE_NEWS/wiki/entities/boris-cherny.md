# Boris Cherny

**類型：** person
**狀態：** active
**首次出現：** 2026-04-23（事後報告發布）
**最後更新：** 2026-05-13

---

## 現況

Boris Cherny 是 Anthropic Claude Code 的創始人與負責人（Head of Claude Code），是 Claude Code 產品方向最主要的公開代言人。他以高頻率的公開聲明、哲學宣言與工程分享，持續引發開發者社群廣泛討論，被視為 Anthropic 技術文化的外部窗口。

---

## 公開言論與主張

### 「Loops 是未來」（2026-05-05）
在 podcast 中宣示已 100% 用 Claude Code 取代手動編碼，並提出 **Loops（迴圈執行）是 AI 編碼的未來範式**，而非單次 prompt 補全。這是 Claude Code 設計哲學的第一手公開陳述，解釋了 Claude Code 為何以 Hooks、Skills、session 持久化為核心設計——目標是讓 agent 能在無人監督下持續迴圈執行。

### 「軟體工程已死」（2026-05-06）
再次公開宣示 Anthropic 內部已無傳統軟體工程師職位，引發業界廣泛論戰，Times of India 等媒體跟進報導，開發者身份認同議題持續發酵。

### 每晚數千個 AI 子代理工作流（2026-05-13）
公開了每晚讓數千個 AI 子代理執行「深度工作」的工作流架構，被 Business Insider 與 Let's Data Science 同步報導，成為本週最受矚目的 agentic AI 使用案例。案例展示：白天由人類設定任務框架，夜間由數千個並行子代理自主深入研究執行「深度工作」，早上整合結果；是其「Loops 是未來」（2026-05-05）哲學的最極端公開實踐。此報導進一步推動社群對大規模並行代理架構的廣泛討論，結合 v2.1.140 的 subagent_type 匹配改善，顯示官方工具正在降低大規模子代理配置的摩擦。見 [[entities/managed-agents]]。

### 「coding is solved」（2026-05-08）
在「Code with Claude」大會宣稱「寫程式問題已被解決」，並公開表示厭倦「vibe coding」一詞，尋找替代描述；自稱 2026 年從未手寫一行程式。言論在 Business Insider、HN、YouTube 等多平台引發廣泛討論，社群反應兩極：有人認同 AI 輔助開發效率躍升，也有人直接回應「Claude Code 太不穩定、已放棄使用」。

### 4/23 事後報告（2026-04-23）
Claude Code 效能退步事件確認後，Boris Cherny 發布事後報告，承諾超過 50 項修復。2026-05-03，社群開發者開始逐一獨立驗證這些承諾，為少見的社群對官方承諾進行系統性問責案例。詳見 [[topics/code-quality-decline]]。

### 第三方工具邊界聲明（2026-04-25）
在 The Verge 報導中公開表示：「訂閱方案的設計並非為這類第三方使用模式而生」，被視為 Anthropic 將持續收緊第三方 agentic 工具門檻的明確信號。詳見 [[entities/pricing]] 與 [[entities/openclaw]]。

---

## 術語貢獻

- **Loops**：AI 編碼的核心範式描述，強調迴圈執行優於單次對話補全
- 反對「vibe coding」：認為該詞已不足以描述當前 AI 輔助開發的工程嚴謹性，推動術語向「spec-driven development」靠攏
- 詳見 [[topics/community-tech-patterns]]（Boris Cherny 設計哲學相關技術彙整）

---

## 社群影響力評估

Boris Cherny 的公開言論呈現兩種截然不同的社群反應：
- **認同面**：被視為 AI 輔助開發方向的領航者，設計哲學（Loops、Hooks 驅動 agentic 工作流）對社群工具生態有明顯影響
- **批評面**：「軟體工程已死」與「coding is solved」等宣言被部分開發者認為過度誇大，且與 Claude Code 頻繁出現可靠性問題（CVE、Windows regression、Cowork 沙箱故障）形成認知落差

---

## 相關實體

- [[entities/claude-code]]（Boris Cherny 主導的產品）
- [[entities/pricing]]（第三方工具邊界聲明）
- [[entities/openclaw]]（第三方工具管控政策）
- [[topics/code-quality-decline]]（4/23 事後報告與社群問責）
- [[topics/community-tech-patterns]]（設計哲學：Loops、vibe coding 反思）

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-26]]
- [[news/2026-04-28]]
- [[news/2026-05-03]]
- [[news/2026-05-05]]
- [[news/2026-05-06]]
- [[news/2026-05-08]]
- [[news/2026-05-13]]
