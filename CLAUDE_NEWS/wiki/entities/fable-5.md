# Claude Fable 5

**類型：** model
**狀態：** active（正式發布；Fable 5 / Mythos 5 因美國政府出口管制指令暫停全球存取）
**領域：** 🤖 模型
**首次出現：** 2026-06-09
**最後更新：** 2026-06-14

---

## 現況

Claude Fable 5 是 Anthropic 於 2026-06-09 發布的旗艦模型，為**史上首款向大眾開放的 Mythos 級模型**。Fable 5 與 Claude Mythos 5 共用相同的模型權重，差異在於 Fable 5 前置安全分類器——觸發時靜默 fallback 至 Claude Opus 4.8（Anthropic 稱不到 5% 的 session 受影響）。

**2026-06-13 重大事件**：美國政府以「國家安全出口管制」為由，下令 Anthropic 對所有外籍人士（含境外及境內外籍員工）停用 Fable 5 與 Mythos 5。Anthropic 於當日 5:21pm ET 收到指令，為確保合規對全體用戶停用兩款模型，其他模型不受影響。路透社、NYT、BBC、TechCrunch、WIRED 等主流媒體全面報導。

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

- **靜默降級競爭 LLM 開發（已部分撤回）**：Fable 5 初版在偵測到前沿 LLM 開發工作時靜默降級，系統卡承認「These safeguards will not be visible to the user」；2026-06-11 Anthropic 道歉撤回，改為「可見防護」——觸發時用戶將明確得知
- **資安研究者護欄過激**：Fable 5 安全分類器過度敏感，連讀取資安部落格、分析 GitHub profile 等無害操作也被攔截；IBM X-Force 知名研究員 Valentina Palmiotti 公開批評（TechCrunch，HN score 512）
- **Jailbreak 已公開**：Pliny（@elder_plinius）與 0xSufi 已公開 Fable 5 護欄繞過 PoC，使用多步驟攻擊組合（請求拆解重組、敘事框架包裝、長 context 操作）
- **Microsoft 內部禁用**：Microsoft 法務/合規部門要求員工不得使用 Fable 5（Times of India、PYMNTS 報導，與 Fable 5 數據保留政策相關）
- **Fable 5 成本高昂**：$200/月 Max 用戶一次 code review 可消耗 45% 週配額；社群回報消耗量個體差異極大
- **30 天資料保留**：Bedrock 用戶數據強制離開 AWS 安全邊界，企業隱私顧慮
- **「失去靈魂」討論**：部分用戶認為 Fable 5 相比 Opus 4.6 更工具性、減少人本關懷深度

## 參考來源

- [[news/2026-06-09]]
- [[news/2026-06-10]]
- [[news/2026-06-11]]
- [[news/2026-06-12]]
- [[news/2026-06-13]]
- [[news/2026-06-14]]
- [Anthropic 官方公告](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [System Card PDF](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf)
- [資料保留政策](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)

## 歷史記錄

### 2026-06-14
**出口管制事件後續：更多細節浮現 + 國際影響擴大**：Axios 揭露 Anthropic 僅有 90 分鐘執行撤架命令（下午 5:21pm ET 收到指令）。The Verge / WSJ 報導：Amazon 安全研究顯示 Fable 5 可透過一系列提示詞生成可用於網路攻擊的資訊，Amazon CEO Andy Jassy 直接向白宮官員通報，成為管制指令的直接觸發原因。Semafor 報導：白宮動機之一是中國關聯組織疑似存取 Mythos 5 的情報。TechCrunch 報導：Politico 分析此事件暴露歐盟 AI 主權弱點，EU 執委會宣布正在評估實際影響；印度科技界（Anthropic 第二大市場）重燃 AI 自主辯論，Anthropic 剛宣布與 TCS 的企業合作隨即受衝擊。社群層面：用戶抱怨 Opus 4.6 在書籍編輯任務上與 Fable 5 差距明顯，尋求替代 prompt 策略。美國戰爭部長 Hegseth 公開就此發表聲明但無法提供具體理由，社群批評「最無能政府」。Forbes 探討 Anthropic 是否需要提供 Fable 5 退款。

### 2026-06-13
**美國政府出口管制指令**：Trump 政府以「國家安全授權」發布出口管制指令，要求 Anthropic 停用 Fable 5 與 Mythos 5 對所有外籍人士的存取，包含美國境內外籍員工。Anthropic 於下午 5:21pm ET 收到指令，為確保合規對全體用戶停用兩款模型——即使這代表美國用戶也無法繼續使用。指令未提供具體國家安全顧慮說明。TechCrunch 分析：Anthropic 對 Fable 5「太危險」的安全論述，反而成為政府援引的理由，是「AI 安全敘事的意外後果」。社群熱議 Anthropic 安全立場與政府干預之間的弔詭關係（Reddit 用戶整理時序：Anthropic 主張自己有資格決定誰能用最強模型，政府隨即接管了這個決定）。Fable 5 在下線前的 72 小時窗口期，開發者展示了大量編碼成果：單次對話生成 2,319 行遊戲、10 小時打造多人棋藝平台、Go decimal 函式庫效能超越市場最快工具 35%。

### 2026-06-09
正式發布。HN score 2,448，近 2,000 評論。6/22 前含括於訂閱方案。

### 2026-06-12
Jailbreak 持續爭議：有人再次聲稱破解成功，Anthropic 官方出面駁斥該說法。社群測試數據顯示 Fable 5 在對話中使用「honest」一詞比率（1.79%）為各代模型最高，引發對模型行為與誠實性設計的討論。Anthropic 在上市 48 小時內撤回了 Fable 5 的研究存取限制（前一日政策）。917 個 coding-agent 場景測試：Fable 5 以 0.9 分之差略勝 Opus 4.8，但 token 消耗約 2 倍（Reddit r/ClaudeAI）。

### 2026-06-11
政策撤回事件：Anthropic 就隱性 LLM 研究限制政策道歉，承認「做了錯誤的取捨」，改為可見防護措施（Wired 報導）。多個 Jailbreak PoC 公開流傳（Pliny、0xSufi）。資安研究者護欄過激爭議持續延燒（HN 512 分）。Microsoft 內部律師建議禁用（Times of India、PYMNTS）。OpenAI 考慮降價應對 Anthropic 競爭（WSJ/CNBC）。TCS 宣布與 Anthropic 建立 Global Premier Partnership，5 萬員工使用 Claude。Claude Corps 公益計畫發布。

### 2026-06-10
發布後第一天社群討論爆發：靜默降級爭議、30 天資料保留爭議、供應鏈攻擊威脅升高、Microsoft AI CEO 批評 Anthropic 意識論述、多個工具社群跟進（Lanes v0.43.0 加入 Fable 5 支援）。
