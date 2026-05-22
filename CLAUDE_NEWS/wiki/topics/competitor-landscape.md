# AI 編碼工具競品動態

**狀態：** ongoing
**開始日期：** 2026-04
**最後更新：** 2026-05-22

---

## 摘要

Claude Code 已成為 AI 輔助編碼的標竿產品，但競爭正快速升溫。2026-05 是關鍵轉折月：OpenAI Codex 下載量單週爆增 1,397%、OpenCode 吸走 15.7 萬開發者、Microsoft 取消數千名員工授權改推 Copilot CLI——分流訊號同步出現。另一方面，Anthropic 企業採用率首次超越 OpenAI（34.4% vs 32.3%），競爭格局呈現「高速成長與高速流失並行」的雙面態勢。

| 關鍵指標 | 數值（2026-05-18）|
|---------|------|
| Anthropic 企業採用率 | **34.4%**（首超 OpenAI 32.3%）|
| OpenCode 分流開發者 | **157,000 名**（The New Stack）|
| Codex 週下載量成長 | **+1,397%**（v0.128.0 發布後）|
| Claude Code 同期下滑 | **−38%**（720 萬次）|
| Microsoft 取消 Claude Code 授權 | 數千名員工，改推 Copilot CLI |

---

## 主要競品追蹤

### Google 未命名競品 🔴
- **狀態**：秘密開發中
- **關鍵人物**：Sergey Brin 親自主導
- **首報**：2026-04（India Today、HN 跟進）
- **意義**：Google 同時是 Anthropic 股東（400 億投資），投資方與競爭者並存的矛盾結構

### OpenAI Codex CLI 🔴
- **狀態**：Active（快速成長）
- **關鍵轉折**：v0.128.0（2026-04-30）新增持久化 `/goal` 跨步驟任務規劃
- **下載數**：8,610 萬次（週增 +1,397%）vs Claude Code 720 萬次（-38%）
- **互通**：社群工具 `claude-anyteam` 已讓 Codex 加入 Claude Code Agent Teams

### OpenCode
- **狀態**：Active（開源替代，快速成長）
- **規模**：157,000 名開發者轉向（The New Stack，2026-05-12）
- **定位**：開源替代 Claude Code；XDA 評測認為功能與體驗相當
- **插件**：`OpenCode-power-pack` 已移植 Anthropic 官方 11 個 skills

### GitHub Copilot
- **狀態**：Active（2026-05-16 推出全新應用程式，明確點名對標 Claude Code）
- **母公司**：Microsoft / GitHub
- **關鍵事件**：Microsoft 內部從 Claude Code 切換至 Copilot CLI（2026-05-15）

### Cursor / Windsurf
- **狀態**：Active（IDE 整合型，與 Claude Code CLI-first 定位有別）

### DeepSeek 🔴
- **狀態**：正式宣布建構 Claude Code 競品（2026-05-22）
- **策略**：「Beijing Wants the Whole Stack」——DeepSeek 不只是低成本替代生態，而是公開宣稱要打造從模型到開發工具的完整技術棧
- **既有基礎**：DeepClaude（聲稱降低 17 倍成本）、DeepSeek-based Claude Code clone（8,700 Stars）
- **意義**：Claude Code 類產品已成為國家層面 AI 競爭的戰場；DeepSeek 轉向正面競爭標誌低成本替代生態進入下一階段

### Alibaba Qwen3.7-Max
- **狀態**：宣稱支援 Claude Code harness（2026-05-22）
- **特點**：聲稱可持續自主運行 35 小時，直接瞄準 Claude Code 的長時間自主執行場景
- **意義**：競品開始直接以「相容 Claude Code harness」作為賣點，顯示 Claude Code 已建立足夠影響力讓競品主動相容

---

## 技術彙整

- **多 LLM 混合架構**：Opus 4.7 作 orchestrator + DeepSeek V4 Pro 承擔大量 token 輸出，是 Max20 方案下最大化性價比的主流策略
- **claude-anyteam**：讓 OpenAI Codex CLI 加入 Claude Code Agent Teams，實現跨模型協作
- **CC-Canary**：效能監測工具，讀取 `~/.claude/projects/` JSONL log（見 [[topics/code-quality-decline]]）
- **Claude Desktop 第三方 LLM 支援**：Anthropic 悄悄加入 OpenAI、Gemini、本地模型、Bedrock/Vertex 支援，競爭格局從「Claude vs others」走向「Claude 作多模型接入層」
- **Claude Connectors 擴展**：進入 Adobe、Blender、Ableton、Affinity、Autodesk Fusion 等創意工具，與 Figma 展開競爭

---

## 觀察重點

- **投資 vs 競爭的矛盾**：Google 400 億投資 Anthropic 的同時開發競品，Amazon 雙品牌並行部署（Claude Code + Codex）——大型科技公司不押注單一供應商
- **開源替代加速**：OpenCode 157K、DeepClaude 17x 成本節省——訂閱政策收緊（OpenClaw 禁令、6/15 計費結構）正在為開源方案創造需求
- **企業成本臨界點**：Microsoft 退訂、Uber 燒光全年預算——企業 AI 工具採購的成本敏感度正在形成新的市場分水嶺

---

## 相關實體

- [[entities/claude-code]]
- [[topics/google-investment]]
- [[topics/anthropic-government-policy]]
- [[topics/enterprise-cost-management]]

## 參考來源

- [[news/2026-05-19]] · [[news/2026-05-18]] · [[news/2026-05-17]] · [[news/2026-05-16]] · [[news/2026-05-15]]
- [[news/2026-05-14]] · [[news/2026-05-12]] · [[news/2026-05-07]] · [[news/2026-05-06]]
- [[news/2026-05-05]] · [[news/2026-05-04]] · [[news/2026-05-02]] · [[news/2026-05-01]]
- [[news/2026-04-30]] · [[news/2026-04-29]] · [[news/2026-04-28]] · [[news/2026-04-27]]
- [[news/2026-04-26]] · [[news/2026-04-25]]
- [India Today：Google 秘密競品](https://www.indiatoday.in/technology/news/story/google-is-secretly-building-a-claude-code-challenger-sergey-brin-is-personally-involved-2899415-2026-04-21)

---

## 時序

#### 企業競爭白熱化（2026-05-12 至 2026-05-19）

### 2026-05-19
- **[dev.to 深度揭露] Microsoft 內部測試全貌：開發者愛它，財務殺了它**：「Microsoft Just Killed Claude Code Internally. Their Own Devs Loved It.」一文詳述 Experiences + Devices 部門六個月測試結果——開發者普遍認為 Claude Code 優於自家工具，但財務層以成本終止採購；此案例在 dev.to #claudecode 社群引發廣泛討論，成為「使用者滿意度 vs 企業採購決策」結構性落差的標準案例；與 [[topics/enterprise-cost-management]] 的成本壓力分析直接呼應

### 2026-05-22
- **DeepSeek 正式宣布建構自有 Claude Code 競品**：Decrypt 報導 DeepSeek 公開宣稱目標是「建立涵蓋模型到開發工具的完整技術棧」，戰略層級從低成本替代品升格為全棧競爭者；Anthropic 面臨的不再只是功能競爭，而是產品生態的整棧複製
- **Qwen3.7-Max 宣稱支援 Claude Code harness，35 小時自主運行**：阿里巴巴 Qwen3.7-Max 聲稱可持續自主運行 35 小時並支援 Claude Code 等外部 harness，意味著競品開始主動定位為「Claude Code 相容」工具，而非建立自己的生態

### 2026-05-21
- **vibe-skill：Claude 規劃 + Mistral 執行，成本降逾九成**：開發者開源 vibe-skill，讓 Claude 負責高層規劃與 diff 審查，實際撰碼委派給 Mistral Vibe；10 天實測節省 57M tokens，成本降逾九成；是 6/15 計費壓力下「多 LLM 成本分流」策略的最具體落地案例，顯示 Anthropic 正以失去執行層 token 份額為代價換取規劃層地位
- **DeepSeek Agent Harness R&D 招募**：DeepSeek 公開招募 Agent Harness 工程師，顯示其正在建立針對 Claude Code 場景的持續對標測試基礎建設；與 vibe-skill 等「以 DeepSeek 替代 Claude 執行層」工具生態形成呼應

### 2026-05-18
- **Microsoft 遷移獲主流媒體確認**：Developer Tech News 正式報導「Microsoft moves engineers from Claude Code to GitHub Copilot CLI」，確認 2026-05-15 記錄的事件，在企業採購圈引發廣泛討論
- **Forbes 深度報導 Uber 燒光 AI 預算**：四個月耗盡 2026 全年 AI 預算，Forbes 將此推向主流財經媒體；凸顯 Anthropic 缺乏企業層級細粒度配額工具的系統性問題（見 [[topics/enterprise-cost-management]]）
- **「Codex 超越 Claude Code」三位創作者同步發聲**：同週三篇 dev.to 評測文章，以個人體驗為主；與 5/5 Codex 下載量 +1,397% 數據並列，顯示競爭敘事的媒體動能持續
- **Claude Code + Codex 混搭工作流**：XDA 報導開發者同時使用兩工具，「依工作流組合 AI 工具」策略興起，市場從「二選一」走向「混搭」

### 2026-05-17
- **techbuzz.ai 再度報導 Microsoft 授權取消**：被 Google News / Phoronix 收錄；原始事件已於 5/15 確認，此波為額外媒體曝光
- **Adobe Lightroom CC Linux 移植借助 Claude Code 完成**：Phoronix 報導，驗證 Claude Code 在跨平台高難度移植工程的實際能力

### 2026-05-16
- **GitHub Copilot 新應用程式明確點名 Claude Code**：首次以產品名直接對標，AI 編碼 agent 賽道從比功能進入正面搶用戶階段（The New Stack）
- **Anthropic 積極尋找下一個「Claude Code 等級」突破**：據 Alex Heath 報導，管理層將 Claude Code 視為創新基準，承受持續創新壓力

### 2026-05-15
- **Microsoft 取消內部 Claude Code 授權**：去年 12 月起向數千名員工（工程師、PM、設計師）開放，因成本壓力陸續取消，改推 GitHub Copilot CLI；Anthropic 與 Microsoft 企業市場正面競爭首次明確浮現
- **Anthropic 企業採用率首超 OpenAI**：Ramp AI Index 34.4% vs 32.3%，Claude Code 是主驅動力；但分析師提醒市場高度動盪，領先地位不穩固
- **第三方工具分化**：Zed、Conductor、Superset 確認受 6/15 計費衝擊；Lanes 聲明不受影響（見 [[entities/pricing]]）

### 2026-05-14
- **6/15 programmatic 用量改按 API 費率，加速競品轉換**：`claude -p`、Agent SDK、CI/CD 全數剝離訂閱；已有用戶宣告轉向 Codex 或 Gemini（見 [[entities/pricing]]、[[entities/openclaw]]）
- **多 LLM 混合策略成主流**：Opus 4.7 orchestrator + DeepSeek V4 Pro 執行層，Anthropic 不再是所有 token 的唯一供應商

### 2026-05-12
- **OpenCode 157,000 名開發者里程碑**：The New Stack 報導，即便 Anthropic 宣佈倍增速率限制，vendor lock-in 顧慮仍驅動開源轉移；是 Claude Code 崛起後最具體的競品分流數據
- **UiPath 開放平台優先整合 Claude Code 與 Codex**：RPA 龍頭進入 AI 編碼工具市場，Claude Code 藉此進入企業流程自動化生態
- **Signadot Kubernetes 整合**：讓 Claude Code、Codex、Cursor 直接在真實 K8s 環境驗證變更，競爭延伸至生產環境驗證階段

---

#### Codex 崛起與分流（2026-05-01 至 2026-05-07）

### 2026-05-07
- **DeepSeek V4 替換 Claude Opus 4 的 30 天實測**：1 億 token 成本與品質對比，社群待進一步驗證
- **Cursor 重度用戶全面轉換至 Claude Code**：六個月雙工具對比後全面切換，月費高峰超過 $60

### 2026-05-06
- **DeepSeek Claude Code Clone 達 8,700 Stars**：同期 DeepClaude 聲稱降低 17 倍成本；低成本替代生態加速形成
- **Claude Code 累積 121,000 GitHub Stars**：Augment Code 分析文章探討 CLI-first 工具勝出 IDE 的原因

### 2026-05-05
- **OpenAI Codex 下載量首次超越 Claude Code**：8,610 萬次（+1,397%）vs 720 萬次（-38%）；轉折點為 v0.128.0 新增持久化 `/goal` 工作流
- **Amazon 雙品牌並行部署**：全體員工同時開放 Claude Code 與 Codex，反映大型企業不押注單一供應商的策略

### 2026-05-04
- **Claude Desktop 悄悄加入第三方 LLM 支援**：涵蓋 OpenAI、Gemini、本地模型、Bedrock/Vertex，無官方公告，完全由社群挖掘；競爭定位從「Claude vs others」轉向「Claude 作多模型接入層」
- **Claude Connectors 進入創意工具**：Adobe、Blender、Ableton 整合，正式進入 Figma 競爭版圖

### 2026-05-02
- **OpenCode 被 XDA 評為可行替代方案**：功能與體驗與 Claude Code 相當，直接回應 OpenClaw 禁令後的替代需求

### 2026-05-01
- **五角大廈排除 Anthropic**：與 7 家公司簽署 AI 機密網路部署協議，Anthropic 因堅持安全護欄遭排除；見 [[topics/anthropic-government-policy]]
- **Apple 內部採用 Claude**：外洩文件確認，企業滲透觸及科技業頂層
- **Uber 四個月耗盡全年 AI 預算**：首次報導（Forbes 於 5/18 深度確認）
- **The Atlantic：Claude Code 是 AI 商業化核心驅動**：指出 AI 產業實際營收正追上前期基礎建設投資，Anthropic 為核心受益者

---

#### 早期格局（2026-04-24 至 2026-04-30）

### 2026-04-30
- **"Is Anybody Using Codex?" HN 討論**：Claude Code 討論量遠超 Codex，但能力被認為相近（Opus 4.7 ≈ GPT-5.5）
- **GameMaker 整合 Claude Code**：垂直軟體深度整合的新案例

### 2026-04-29
- **Codex vs Claude Code 生產環境比較**：大型 Python monolith 測試，作者偏好 Codex；HN 結論「不同工具適合不同場景」

### 2026-04-28
- **哈佛 FAS 以 Claude 取代 ChatGPT Edu**：頂尖學術機構出現結構性轉變
- **XDA 四工具橫向評測**：Claude Code、Codex、Lovable、Replit 並排比較

### 2026-04-27
- **HackerNoon**：AI 工具競爭護城河快速縮窄，開源替代使商業模型差異化愈來愈脆弱
- **HN Claude vs GPT-5 體驗比較**：Claude 前端設計與初始結構佔優；GPT 核心邏輯更強；Claude 易忽略資安標頭

### 2026-04-25–26
- **Google 競品消息登上 HN**：Sergey Brin 親自主導 Claude Code 競品；「投資者即競爭者」的矛盾引發廣泛討論

### 2026-04-24
- **Anthropic CPO Mike Krieger 辭去 Figma 董事會**：暗示 Opus 4.7 將內建設計工具，可能直接與 Figma 競爭
