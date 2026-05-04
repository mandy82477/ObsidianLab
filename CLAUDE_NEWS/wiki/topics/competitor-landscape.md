# AI 編碼工具競品動態

**狀態：** ongoing
**開始日期：** 2026-04
**最後更新：** 2026-05-04

---

## 摘要

Claude Code 已成為 AI 輔助編碼領域的標竿產品，但競爭正在快速升溫。最值得關注的是 Google 聯合創辦人 Sergey Brin 親自主導的內部計畫，目標是打造一款直接對標 Claude Code 的工具。2026-05-04 新發展：Anthropic 已悄悄讓 Claude Desktop/Cowork 支援任意第三方 LLM（OpenAI、Gemini、本地模型、企業閘道），競爭格局從「Claude vs. others」正在轉向「Claude 作為多模型接入層」；Claude Connectors 同期擴展至創意工作軟體（Adobe、Blender、Ableton 等），正式進入 Figma 等工具的競爭版圖。

---

## 主要競品追蹤

### Google 未命名 Claude Code 競品 🔴 新威脅
- **狀態**：秘密開發中
- **關鍵人物**：Sergey Brin（Google 聯合創辦人）親自參與
- **時間線**：2026-04 首次被媒體報導（India Today、HN 跟進）
- **意義**：Google 同時是 Anthropic 的大股東（見 [[topics/google-investment]]），此舉顯示即使是戰略投資方也將 Claude Code 視為必須正面競爭的對手

### OpenAI Codex CLI
- **狀態**：Active
- **差異**：以 OpenAI 生態為核心；社群已有工具（claude-anyteam）讓 Codex 加入 Claude Code Agent Teams

### OpenCode
- **狀態**：Active（開源替代方案）
- **定位**：開源替代 Claude Code，XDA 評測指出功能與使用體驗與 Claude Code 相當
- **意義**：為不願受限於 Anthropic 訂閱政策（OpenClaw 禁令、Pro/Max 第三方工具限制）的開發者提供具體可行的替代方案；OpenCode-power-pack 已將 Anthropic 官方 11 個技能移植至此平台

### Cursor / Windsurf
- **狀態**：Active
- **定位**：IDE 整合型，與 Claude Code 的 CLI-first 定位有所區別

### GitHub Copilot
- **狀態**：Active
- **母公司**：Microsoft / GitHub
- **差異**：深度 IDE 整合，主要面向 VS Code 生態

---

## 技術彙整

- **Claude Code 定位**：CLI-first，與 Cursor / Windsurf 的 IDE 整合型定位有所區別
- **claude-anyteam**：社群工具，讓 OpenAI Codex CLI 加入 Claude Code Agent Teams，實現跨模型協作
- **CC-Canary**：社群開發的效能監測工具，讀取 `~/.claude/projects/` JSONL log（見 [[topics/code-quality-decline]]）
- **Anthropic CPO 動向**：Mike Krieger 離開 Figma 董事會，暗示 Anthropic 可能擴張至設計工具領域，與 Figma 直接競爭

---

## 觀察重點

- **投資 vs 競爭的矛盾**：Google 對 Anthropic 投資 400 億的同時，也在打造競品，這種雙軌策略值得持續追蹤
- **Anthropic 的 CPO 動向**：Mike Krieger 離開 Figma 董事會，暗示 Anthropic 可能在設計工具領域進行擴張
- **社群工具生態**：無論競品如何發展，Claude Code 周邊的社群工具生態（CC-Canary、claude-anyteam 等）顯示其開發者黏著度仍高

---

## 相關實體

- [[entities/claude-code]]
- [[topics/google-investment]]
- [[topics/anthropic-government-policy]]（五角大廈排除事件）

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-26]]
- [[news/2026-04-27]]
- [[news/2026-04-28]]
- [[news/2026-04-29]]
- [[news/2026-04-30]]
- [[news/2026-05-02]]
- [[news/2026-05-04]]
- [India Today 報導](https://www.indiatoday.in/technology/news/story/google-is-secretly-building-a-claude-code-challenger-sergey-brin-is-personally-involved-2899415-2026-04-21)

## 時序

### 2026-05-04
- **[重大變化] Claude Desktop/Cowork 悄悄加入第三方 LLM 支援**：作者花 20 小時研究後發現 Anthropic 已在 Claude Desktop/Cowork 中加入支援任意第三方 LLM 的功能，涵蓋 OpenAI、Gemini、開源模型（透過 OpenRouter）、本地模型及企業閘道（Bedrock、Vertex、Foundry），無任何官方公告，完全由社群自行挖掘。此舉代表 Anthropic 實際上已將 Claude Code/Cowork 定位為多模型平台，競爭格局從「Claude vs. others」轉向「Claude 作為多模型接入層」
- **Claude Connectors 正式進入創意工作軟體領域**：Adobe、Blender、Ableton、Affinity、Autodesk Fusion 整合，代表 Claude 的競爭範疇已從純開發工具延伸至設計與創作工作流程，新進入 Figma 等創意工具的競爭版圖
- **Claude Haiku 4.5 SWE-bench Verified 73.3%**：社群分析文章說明何時選 Haiku 4.5 vs Sonnet 4.6，顯示 Anthropic 在低成本層模型能力持續提升，壓縮競品在 cost-performance 定位的空間

### 2026-05-02
- **OpenCode 被 XDA 評為 Claude Code 的可行替代方案**：XDA 實測後認為 OpenCode 功能與使用體驗與 Claude Code 相當，直接回應 Anthropic 訂閱政策收緊（OpenClaw 禁令）後開發者的替代需求，是目前最具可操作性的開源替代選項
- **OpenClaw 禁令持續發酵**：Anthropic 於 4 月 4 日修改條款禁止 Pro/Max 訂閱額度透過第三方框架調用，依賴此類工具節省成本的開發者被迫切換至 API 計費，實際費用大幅攀升；社群持續討論轉向開源替代方案

### 2026-05-01
- **[重大事件] 五角大廈排除 Anthropic**：美國國防部與 SpaceX、OpenAI、Google、Microsoft、NVIDIA、AWS、Reflection 共 7 家公司簽署 AI 機密網路部署協議，**Anthropic 因堅持軍事用途須納入安全護欄而遭排除**。白宮在 Anthropic 宣布多項技術突破後已重啟談判，此事件對 Anthropic 的政府市場佈局影響深遠；見 [[topics/anthropic-government-policy]]
- **Apple 內部採用 Claude（外洩文件）**：根據外洩文件，Apple 已在內部工作流程中採用 Claude，顯示 Anthropic 的企業滲透已觸及科技業最頂層玩家；此消息對外界評估 Anthropic 市場地位具有重要參考意義
- **Uber 四個月耗盡全年 AI 預算**：Uber 工程師對 Claude Code 與 Cursor 的依賴程度遠超預期，四個月內耗盡全年 AI 預算；Uber CTO 坦言效益毋庸置疑，但大規模成本控管已成企業採用 AI 開發工具的核心挑戰
- **iCapital 採用 Anthropic 打造金融客戶工具**：另類資產平台 iCapital 宣布採用 Anthropic 技術為客戶建立 AI 工具，顯示 Claude 在金融服務領域的企業採用持續擴展
- **The Atlantic：AI 泡沫論降溫，Claude Code 為商業化核心驅動**：The Atlantic 指出隨著 Claude Code 等 AI Agent 工具帶動企業付費，AI 產業實際營收正快速追上前期大規模基礎建設投資，Anthropic 被點名為商業化轉折的核心受益者
- **GPT-5.5 vs Opus 4.7 基準測試**：56 個真實開源 repo 任務測試，Opus 4.7 寫出更精簡 patch，GPT-5.5 的 patch 更常通過 code review；見 [[entities/opus-4-7]]

### 2026-04-30
- **"Is Anybody Using Codex?" HN 討論**：社群觀察 HN 上 Claude Code 討論量遠超 OpenAI Codex，留言者普遍認為兩者能力相近（Opus 4.7 ≈ GPT 5.5），但 Claude Code 社群能見度明顯更高；Codex 曝光度有限，實際採用規模不明
- **GameMaker 整合 Claude Code**：遊戲引擎平台 GameMaker 宣布整合，是 Claude Code 在垂直軟體領域深度整合的新案例，顯示 IDE 整合型競品（Cursor、Copilot）之外，Claude Code 也在各垂直領域形成整合生態
- **BrowserCode 瀏覽器端執行 Gemini CLI**（Claude Code 支援規劃中）：WebAssembly 沙盒技術讓 Gemini CLI 可在瀏覽器直接執行，Claude Code 支援已在路線圖中，跨工具的「瀏覽器化」趨勢值得關注

### 2026-04-29
- **Codex vs Claude Code 生產環境比較**：一名開發者在多年積累的大型 Python monolith 上日常對比兩款工具，最終偏好 Codex，指出 Claude Code 對複雜遺留架構的處理未達預期；作者強調此為個人情境，非通用結論，HN 引發「不同工具適合不同場景」討論

### 2026-04-28
- **哈佛大學文理學院改用 Claude**：哈佛 FAS 計畫為師生提供 Anthropic Claude 存取，同步逐步淘汰 ChatGPT Edu，代表頂尖學術機構在 AI 工具選擇上出現結構性轉變。
- **XDA 四工具橫向評測**：將 Claude Code、OpenAI Codex、Lovable 與 Replit 並排比較，結論是其中僅一款工具被評者認為已達真實工作場景使用標準（具體勝出者及評分細節詳見原文）。
- **Anthropic 開設雪梨辦公室、任命 ANZ 總經理**：Theo Hourmouzis（前 Snowflake SVP，逾 20 年亞太科技業資歷）擔任澳紐區總經理，標誌 Anthropic 在亞太地區的實體佈局大幅提速。

### 2026-04-27
- HackerNoon 分析文章以 Claude Code 為例，指出 AI 工具的競爭護城河正在迅速縮窄——開源替代品與快速跟進的競爭者使商業模型差異化優勢愈來愈脆弱
- HN 社群熱烈比較 Claude vs GPT-5 實際開發體驗：Claude 在前端設計與初始結構上佔優，GPT 在核心邏輯上表現更好；Claude 容易忽略資安標頭設定，GPT 傾向過度防禦
- Claude Code + Figma MCP 設計工作流程獲 Creative Bloq 評測，吸引設計與開發跨領域關注

### 2026-04-26
- Google 競品消息再次登上 HN 重點話題，與 Google Cloud CEO 公開談及 Anthropic 與 TPU 部署同步出現，競爭態勢明顯升溫

### 2026-04-25（approx）
- HN 報導 Google 祕密開發 Claude Code 競品，Sergey Brin 親自主導
- 消息引發社群廣泛討論（「投資者同時也是競爭者」的矛盾關係）

### 2026-04-24
- Anthropic CPO Mike Krieger 辭去 Figma 董事會，媒體指出 Opus 4.7 將內建設計工具、可能與 Figma 直接競爭
