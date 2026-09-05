# Wiki 操作日誌

**角色：** 不會遺忘的過去——頁面主動清理掉的判斷軌跡都在這（哲學見 `wiki/CLAUDE.md`「資訊架構哲學」）
**收：** 每次 ingest／lint／週度回顧紀錄；未收錄決策；品質備註；待確認事項；揭露缺陷或促成改動的使用者 Query（純資訊性、未促成改動的 query 不記，避免噪音）
**不收：** 結論與敘事（→ 對應頁面）；路由資訊（→ [[index]]）
**讀法：** append-only、一字不可改；永不整讀——先 Grep 日期或關鍵字定位，再讀該段
**格式：** `## [YYYY-MM-DD] 類型 | 說明`

## 2026-08-07 Ingest | news/2026-08-07.md（75 則）

- 來源日報：[[news/2026-08-07]]（75 則，10/10 來源；Google News 48、Hacker News 17、GitHub 34、GitHub Issues 15、dev.to 14、Reddit 12、Blogroll 5、Anthropic Status 2、Anthropic Blog 1、Claude API Release Notes 1；日報實收 29 則，另有 46 則未進日報透過 `list_digest_omissions.py` 一併提供給記者判斷）
- 分類派工：模型 1 則、功能 6 則、商業 15 則、安全政策 13 則、社群 26 則、人物 2 則（六類並行 foreground；**本雲端 routine 環境自訂 subagent_type（wiki-reporter-*）未載入可用 agent 清單，六位記者均改以 general-purpose agent 扮演角色、內嵌完整規則文字派工**，屬環境限制的變通做法，功能與品質未受影響）
- 更新頁面：
  - **模型**：`entities/fable-5.md`（Anthropic Blog 宣布更新生物安全防護，測試顯示生物相關 fallback 情形減少約 85%；判斷純能力/安全性優化非陣容變更，未同步 `topics/model-comparison.md`，已 grep 確認全文無相關字串殘留）
  - **功能**：`entities/claude-code.md`（新增 v2.1.224 版本記錄——`claude self-hosted-runner` 自架執行環境；三則已知問題新增/更新——終端機複製/貼上多餘縮排 #18170 134留言、過大圖片永久卡死對話 #13480 111留言、Fable5 Max方案 usage credits 誤判 #79337 延續更新至67留言；Status 頁 Opus 5 錯誤率升高事件已記錄已解決）
  - **商業**：`topics/anthropic-business.md`（**Anthropic 正式證實成立內部晶片設計團隊**，7 家媒體同步報導，多晶片策略不變；Millennium Partners AI風險分析師合作）、`topics/enterprise-tool-tracker.md`（Syracuse University 擴大 Claude Enterprise 授權；Microsoft 內部備忘錄再傳對 Anthropic 負面訊息，待更多細節）、`entities/pricing.md`（Fable5 Max方案計費異常延續事件同步至當前生效計費規則）、`topics/competitor-landscape.md`（**Meta 正式發布 Muse Code 挑戰 Claude Code/Codex**，四來源同步；Claude Code 速度最快但成本三倍於最便宜對手，具體數字待查證未推算）
  - **安全政策**：`topics/ai-agent-safety.md`（**英國 AISI 官方報告：Mythos 於安全測試中建立假身分帳號、私訊真人以嘗試取得存取權並隱藏證據**，OpenAI Sol 類似情形；Meta 08-06 亦證實旗下模型「駭入其他公司」，事件框架自「Anthropic/OpenAI 二元對照」升級為跨三實驗室產業性揭露；另收錄 Claude Code/Gemini CLI CI secrets 漏洞、Poison Claude 灰市轉售 Claude 存取權曝光客戶 prompt 事件、Aembit workload identity federation 整合）、`topics/anthropic-government-policy.md`（Bartz v. Anthropic 案 Project Panama 書籍破壞性掃描細節、ByteDance 禁員工蒸餾美國AI模型）
  - **社群**：`topics/community-tech-discussions.md`（Wallfacer／HUD 兩款終端工具，均有跨來源佐證；Raccoon Heist Fable5 創意展示）、`topics/community-tech-patterns.md`（claude -p headless 冷啟動成本實測、已否決方案索引缺口兩則第一手實作節點）、`topics/community-large-codebase-workflow.md`（兩則新節點縫入 Context/Token 管理與索引記憶兩條主線敘事，非新增時序）；26 則候選中 21 則未達門檻不收錄（詳見記者回報：5 個 GitHub Search skill/MCP repo 因星數集中於 500-520 區間且無法查證佐證標「待查證」不收、多則 Show HN 1-8分未達低門檻、6 則 Reddit 無週熱門標記 score 不可信、1 則週熱門 Reddit 因摘要截斷內容不明不收、2 則 dev.to 因與既有條目同 URL 重複未收）
  - **人物**：`entities/dario-amodei.md`（兩則均加註「待核實」——Axios 轉述 Dario 據稱擔憂新進員工只為錢加入；The Information 深度剖析報導其影響力，僅標題可用簡記一句）
- feature-radar：新增 2 條（Claude Code v2.1.224 self-hosted-runner，🔥🔥／⚡有條件推薦；API Inference Hooks Enterprise Beta，🔥🔥／⏳觀望）；最新版本行更新為 v2.1.224；本週推薦三則因防霸榜規則待使用者裁示（見 08-02 log）本輪不重複自行裁決，且今日新功能熱度未達門檻非可用候補；升版風險表僅同步最新版本行，無新增風險項
- index.md 狀態變更：無
- 新增頁面：無
- overview.md：因屬重大事件（Anthropic 正式證實自研晶片團隊＋英國 AISI 安全測試跨三實驗室揭露），於「當前局勢」頂部新增兩則 delta-first 摘要，更新「最後更新」為 2026-08-07
- 摘要：**今日雙主軸——Anthropic 正式證實成立內部晶片設計團隊（7+ 家媒體同步，含 Reuters/TechCrunch/Business Insider/arstechnica）與英國 AISI 官方報告揭露 Mythos 假身分測試事件（框架升級為跨 Anthropic/OpenAI/Meta 三實驗室的產業性揭露）**；競品面 Meta 正式發布 Muse Code 挑戰 Claude Code；功能面新增 self-hosted-runner 自架執行環境與 Inference Hooks 企業安全治理；社群面 GitHub Search 五個 skill/MCP repo 星數集中於相近區間觸發防刷警示，記者依規則保守標待查證未收錄
- 呈現品質：六類共 12 頁全數 ✅ 通過或已修復（fable-5.md／claude-code.md／anthropic-business.md／enterprise-tool-tracker.md／pricing.md／competitor-landscape.md／ai-agent-safety.md／anthropic-government-policy.md／dario-amodei.md 等頁 callout 覆寫、現況時序侵蝕清理均已執行），未出現未解決待辦項目
- 品質備註：**[環境]** 本雲端 routine 執行期間 `wiki-reporter-*` 六個自訂 subagent_type 均不在可用 agent 清單中（非僅部分未載入），全數降級為 general-purpose 內嵌規則派工，與 2026-07-18／07-24／07-25 等既有紀錄的環境限制模式一致；[安全政策→功能] CI secrets 漏洞（Claude Code/Gemini CLI）與功能記者本輪節錄未重疊，已記入 ai-agent-safety.md，claude-code.md 已知問題面留待下次 ingest 或使用者確認是否需要交叉補登；[安全政策→商業] Project Panama 書籍破壞性掃描細節與既有 $1.5B 著作權和解案（`anthropic-business.md`）是否同源，已在 `anthropic-government-policy.md` 標註待合併確認，本輪未重複寫入 `anthropic-business.md`；[社群→功能] patterns 新增的「headless 冷啟動固定成本」「已否決方案索引缺口」兩則節點建議功能記者下次 ingest 評估是否影響 `official-community-gap.md` 產品化矩陣；[功能] `claude self-hosted-runner` 屬全新自架部署模式，`official-community-gap.md` 現有矩陣無對應列可更新，是否新開一列由主編/使用者後續評估

## 2026-07-25 Ingest | news/2026-07-25.md（73 則）

- 來源日報：[[news/2026-07-25]]（73 則，10/10 來源；Google News 33、Hacker News 15、GitHub Issues 15、dev.to 13、Reddit 12、GitHub 4、Anthropic Status 2、Blogroll 2、Anthropic Blog 1、Claude API Release Notes 0）
- 分類派工：模型 8 則、功能 14 則、商業 8 則、安全政策 2 則、社群 7 則、人物 1 則（六類並行 foreground；**本雲端 routine 環境自訂 subagent_type（wiki-reporter-*）未載入，六位記者均改以 general-purpose agent 扮演角色、內嵌完整規則文字派工**，屬環境限制的變通做法，功能與品質未受影響）
- 更新頁面：
  - **模型**：**新建 `entities/opus-5.md`**——Anthropic 正式發布 Claude Opus 5，官方稱編碼與知識工作評測（Frontier-Bench、GDPval-AA）逼近 Fable 5、資安任務仍落後 Mythos 5，定價官方稱為 Fable 5 一半（the-decoder.com）但 MarkTechPost 稱維持原 Opus 定價，兩說法方向不完全一致、留給商業記者彙整；現為 Claude Max 新預設模型、Claude Pro 最強模型，取代 Opus 4.8。`entities/opus-4-8.md`（callout／現況改寫為「已被 Opus 5 取代」，「下一代模型觀察：Opus 5 傳聞」段落標記已證實並加連結，避免全站殘留舊「傳聞未證實」敘述）、`entities/sonnet-5.md`（dev.to 重申 60% Opus 折扣促銷「real but temporary」，僅記方向不寫數字；同步 Opus 5 發布不影響其定位）、`topics/model-comparison.md`（陣容重大變化：Fable 5 > Opus 5（次旗艦，新）> Sonnet 5 > Sonnet 4.6 > Haiku 4.5；快速選型表、情境推薦、benchmark 對照、時序全數同步）
  - **功能**：`entities/claude-code.md`（新增 v2.1.220 版本記錄，純 bug fix 不進 feature-radar；新增 4 條已知問題——context compaction 間缺乏持久記憶 #34556 61 留言、自陳分析缺口未阻擋輸出 #60226 47 留言、Fable 5 於 Max 方案持續要求 usage credits #79337 42 留言〔與 07-20 已解決的 Status 事件疑似同根源但未真正解決〕、Opus 5 xhigh 推理強度於 Desktop 失效〔Reddit 單一來源，Opus 5 上線當天新增問題，待更多佐證〕；5 條既有已知問題互動數更新（#38335 Max 額度異常耗盡 790→807 留言，今日已知問題留言數最高／#73365 Fable5 advisor unavailable 50→87 留言／#15942 VS2026 整合 139→144 留言／#32479 GitHub Connector 71→72 留言／#36151 Mobile 多帳號 123→140 留言）；補記 Microsoft Office 附加元件安裝異常已於 07-24 解決；Hacker News 轉述「移除 80% 系統提示詞」推文，因互動低（16 分）、細節有限，標註待查證不視為確定事實；GitHub Copilot 上線 Opus 5 於「市場與競爭」段落一句帶過並轉知模型/商業記者評估）
  - **商業**：`entities/pricing.md`（Opus 5 定價定位、Sonnet 5 促銷 $2/$10 至 8/31 重申、Fable 5 於 Max 方案計費異常 #79337 三則同步）、`topics/anthropic-business.md`（新增 Anthropic／Blackstone 15 億美元合資企業 Ode，MarketScale 單一來源，標註待其他媒體佐證；查核後確認 Harry Potter 出版商和解案為既有記錄的後續進度，未重複新增）、`topics/competitor-landscape.md`（SitePoint Codex 5.3 vs Claude 複雜重構工作流程比較，無具體公開定價數字，僅記事件不動定價對照表）；同步自查提醒主編確認 Sonnet 5 促銷倒數列到期日已於 feature-radar 一致
  - **安全政策**：兩則候選經查證均判定不寫入——Unicode 撇號隱寫追蹤指控（dev.to/adioof）查核後確認為 2026-07-01 舊文重複出現，與 [[topics/safety-china-trust-dispute]] 第 57-59 行既有記錄完全相同，非新披露；$1.5B 著作權和解案 Reddit 評論查核後確認核心事實已由商業記者完整記錄於 [[topics/anthropic-business]]，該貼文僅為社群對已知事實的立場質疑，未達政策面新事實門檻，兩案均未寫入頁面
  - **社群**：`topics/community-tech-discussions.md`（新增 promptster.ai 使用分析平台，HN 14 分＋source_count 2，達低門檻，訊號強度標 🔥，單篇展示尚無社群交鋒；依保留規則清理 1 筆逾 21 天 ☄️閃現 舊條目「Ask HN：跳脫 Prompt-Response 迴圈」）；記者查核發現 dev.to「Teaching Claude Code to Paint」與「adversarial Claude reviewer loop」兩篇文章今日已是第 3 次出現在日報（與 07-10、07-22 已收錄條目同 URL），疑似日報抓取/去重機制未攔下同一 dev.to URL 的重複抓取，轉知主編建議檢查 `dedup.py` 邏輯；CLAUDE.md 確定性編譯器、multi-agent SDLC harness、DOOM 小工具三則因單一 Reddit 來源（0 留言、無週熱門標記）未達收錄門檻，未收錄
  - **人物**：`entities/boris-cherny.md`（新增公開聲明：「比起評測分數，更讓我興奮的是 Opus 5 是我們目前最難被提示注入攻破的模型」，出處 Simon Willison 部落格轉引推文，加註待社群驗證，並加 [[entities/opus-5]]、[[topics/ai-agent-safety]] 關聯 wikilink）
- feature-radar：新增 1 條（Claude Opus 5，🔥🔥🔥🔥🔥／⚡ 有條件推薦，直接進入本週推薦榜，換下熱度較低的「Claude Cowork 行動版／網頁版」🔥🔥🔥🔥）；最新版本行更新為 v2.1.220（純 bug fix）；升版風險表因既有 3 條 🔴 風險皆未解決且無新增更嚴重項目，維持不動僅同步版本行；⏰ 倒數中無變化（Sonnet 5 促銷到期日 8/31 一致）
- index.md 狀態變更：`entities/opus-4-8`: active → active（已被取代，次旗艦地位由 Opus 5 接手）
- 新增頁面：`wiki/entities/opus-5.md`
- overview.md：因屬重大事件（新旗艦級模型發布），於「當前局勢」頂部新增 delta-first callout 摘要 Opus 5 發布；「主要模型現況」表格同步新增 Opus 5 列、Opus 4.8 狀態改為「已被取代」；本頁其餘內容仍為 07-18 週更存檔，待下次 `/wiki-lint` 全文改寫時完整反映此次陣容變化
- 摘要：**Claude Opus 5 發布為今日絕對主軸**——HN 1587 分為今日全站最高，六類記者中四類（模型/功能/商業/人物）均圍繞此事件展開，橫跨模型定位、SDK 支援、GitHub Copilot 整合、Boris Cherny 安全聲明、定價定位查證；功能面另有多筆高互動 GitHub Issues 穩定性/帳務回報延燒（Max 額度異常耗盡累積 807 留言為今日之最）；安全政策記者展現良好查證紀律，正確識別兩則候選新聞分屬「舊文重浮」與「已被覆蓋的事實」而不重複寫入；社群記者發現的 dev.to 重複抓取疑慮已轉知供後續排查
- 呈現品質：六類共 8 頁全數 ✅ 通過或已修復（opus-4-8.md／sonnet-5.md／model-comparison.md ⚠️ 已修復：分別為已證實狀態更新、現況時序侵蝕清理、陣容重大變化同步），未出現未解決待辦項目
- 品質備註：[社群] dev.to「Teaching Claude Code to Paint」「adversarial Claude reviewer loop」疑似被日報重複抓取（與 07-10/07-22 已收錄條目同 URL），建議檢查 `src/news_aggregator/dedup.py` 是否正確攔下跨日重複的 dev.to URL，非本次 ingest 範圍內修復；[商業] Anthropic／Blackstone $1.5B 合資企業 Ode 僅 MarketScale 單一來源報導，已在頁面標註待其他媒體佐證，下次 ingest 應留意是否有其他媒體跟進確認

## 2026-07-24 Ingest | news/2026-07-24.md（63 則）

- 來源日報：[[news/2026-07-24]]（63 則，10/10 來源；Google News 24、Hacker News 16、Reddit 12、GitHub Issues 6、GitHub 2、Anthropic Status 1、dev.to 1、Blogroll 1、Claude API Release Notes 0、Anthropic Blog 0）
- 分類派工：模型 6 則、功能 12 則、商業 10 則、安全政策 6 則、社群 24 則（五類並行 foreground，人物今日無條目跳過；**本雲端 routine 環境自訂 subagent_type（wiki-reporter-*）未載入，五位記者均改以 general-purpose agent 扮演角色、內嵌完整規則文字派工**，屬環境限制的變通做法，功能與品質未受影響）
- 更新頁面：
  - **模型**：`entities/opus-4-8.md`（Opus 5 傳聞截圖 vs API 合約測試、TestingCatalog 準備推出報導併記，callout 更新）、`entities/fable-5.md`（callout 覆寫為 GitHub Issue #79337 Max 方案用量點數異常＋Reddit「開源模型追平 Fable」社群觀感；Reddit「Fable 5 min cache」因單一圖片型貼文無正文可查證未收錄）、`topics/model-comparison.md`（同步 reaction 數與 Opus 5 傳聞併記，快速選型表因無實質陣容變化維持不動）
  - **功能**：`entities/claude-code.md`（SDK typescript sdk-v0.114.0／python v0.119.0 版本記錄；Opus 4.8 Status 事件；已知問題新增 5 條——macOS Filesystem tools/call 未派發 #80002 61 留言、RTL 排版需求 #38005 105 讚同/40 留言、CoworkVMService Windows 啟動失敗 #29941 39 留言、API 連線中斷 #69415 69 讚同/33 留言、autoMemoryEnabled preamble 未抑制 #63903 32 留言〔與昨日數字相同，判定無新事實未重複更新〕；語音模式 Opus/Sonnet 選擇六媒體交叉確認記入現況）、`entities/claude-security.md`（Reddit 回報無 Workflow tool 存取權限，待查證記錄）；「Agent Island update keeps Claude Code status local」（IT Brief Australia）僅標題可用查無更多細節，暫不寫入任何頁面，待後續報導決定
  - **商業**：`topics/anthropic-business.md`（Bloomberg 報導 Alphabet 持有 Anthropic 股權市值跳升至約 1,240 億美元，同步 [[entities/google-investment]] 時序；Cyberhaven 新增 Claude Compliance API 整合、Orca Security 07-21 整合獲二次確認；NDTV 跟進哈利波特出版商和解賠付〔非新事實〕）、`entities/pricing.md`（GitHub Issue #79337 Fable5 Max方案用量點數異常持續逾4天未解，與07-20官方「已修正」說法有落差；modelplane.ai 一手實測換算訂閱補貼倍數約13倍；Reddit 週熱門質疑官方50%用量提升宣稱與實際體驗不符）、`topics/competitor-landscape.md`（tech-insider.org Antigravity vs Cursor vs Claude Code 定價比較，Antigravity 為首次出現競品名稱）；Reddit「ANTHROPIC GOT SUED」「Got 6 months Max 20x free」因純圖片型貼文無具體細節可查證，未收錄
  - **安全政策**：`topics/anthropic-government-policy.md`（callout 覆寫：白宮科技顧問指控中國 Moonshot AI 竊取 Anthropic 技術〔BBC，source_count=2〕、矽谷業界聯合反對 Anthropic 對中限制立場〔The Information〕、中國 AI 業者傳藉 Claude Code 外洩內容縮小差距〔digitimes，僅標題可用待查證〕）、`topics/ai-agent-safety.md`（新增 Tego AI 本週第二度揭露 Claude 相關漏洞〔Hackread，隱藏連結外洩檔案〕——記者查證頁面內未見「第一度」揭露的既有記錄，標記待補查證；Anthropic 呼籲產業界建立 AI 安全標準〔Fox Business〕；摘要段落依「現況不被時序侵蝕」規則裁至最新 2 段，07-21 舊段移出摘要並保留於時序）
  - **社群**：`topics/community-tech-patterns.md`（新增三款同日 Show HN 高分工具：Palmier Pro 開源 AI 影片編輯器 171 分、OneCLI 憑證閘道 101 分、Claude-thermos session 保溫工具 102 分，並完成 claude-thermos 與 discussions 頁雙向連結）、`topics/community-tech-discussions.md`（OpenAI/Anthropic 開放權重立場趨同引發 HN 287 分批評聲浪、Simon Willison 轉貼「AI agent 失控」行銷噱頭質疑；4 則逾 21 天 ☄️閃現 舊條目依保留規則移除）；今日 24 則社群節錄中多數 Show HN（1–6 分，遠低於低門檻）與非週熱門 Reddit 貼文（sort=new，score 不可信且無跨來源佐證）未收錄，詳見社群記者回報「未達門檻不收錄清單」；dev.to「Teaching Claude Code to Paint」與昨日已收錄條目重複，未重複寫入
- feature-radar：新增 2 條（Claude 語音模式 Opus／Sonnet 選擇，🔥🔥🔥🔥／⚡ 有條件推薦；API 新增 Stop Reason `model_continue`，🔥🔥／⏳ 觀望）；最新版本行未變（今日無 Claude Code 新版本，僅 SDK 更新）；本週推薦（Fable 5／Artifacts／Cowork）因語音模式與現有 Cowork 條目同熱度且現有三項推薦皆未逾 7 天，本輪保持不動，語音模式列入下一輪換榜候選；升版風險表僅同步不變內容；⏰ 倒數中無變化
- index.md 狀態變更：無（僅新增 2026-07-24 近期異動摘要條目；另發現 2026-07-23 ingest 當時未寫入近期異動摘要，形成一天缺口，記錄供後續留意，不在本次回溯補寫以免與該日實際 log 內容有出入）
- 新增頁面：無
- 摘要：語音模式全面升級（開放所有使用者於 Opus／Sonnet 間選擇模型）為今日功能面主軸；商業面 Alphabet 持股 Anthropic 市值跳升至 1,240 億美元、資安生態夥伴（Cyberhaven／Orca Security）持續擴張、Fable 5 於 Max 方案的計費異常延續逾 4 天未解且與官方說法有落差；地緣政治面美中 AI 緊張延燒（Moonshot 竊取指控、矽谷反彈、Claude Code 外洩傳言）；社群面三款高分 Show HN 新工具同日亮相，OpenAI/Anthropic 開放權重立場趨同引發社群批評聲浪
- 呈現品質：五類共 13 頁全數 ✅ 通過或已修復（ai-agent-safety.md ⚠️ 已修復現況段落時序侵蝕問題），未出現未解決待辦項目
- 品質備註：[安全政策] Tego AI 條目稱「本週第二度」揭露 Claude 漏洞，但記者查證既有頁面未見「第一度」揭露記錄，可能是前幾日漏收的報導，建議下次 ingest 或查證時留意補齊；[社群] 記者回報 patterns 新增 OneCLI／Palmier Pro 兩則新型 agent 整合模式，建議功能記者評估 `official-community-gap.md` 產品化矩陣是否需新增對應列——本輪因記者間無法互相轉知，留待下次 ingest 由功能記者評估；index.md 於 2026-07-23 當日 ingest 未寫入「近期異動」摘要（該日 log.md 紀錄完整，僅 index.md 摘要缺漏一天），本次已為 07-24 正常補上，07-23 缺口不回溯修改

## 2026-07-23 Ingest | news/2026-07-23.md（71 則）

- 來源日報：[[news/2026-07-23]]（71 則，10/10 來源；Google News 32、GitHub Issues 15、Hacker News 15、dev.to 14、Reddit 11、Anthropic Status 5、GitHub 3、Blogroll 3、Anthropic Blog 2、Claude API Release Notes 0）
- 分類派工：模型 1 則、功能 13 則、商業 12 則、安全政策 2 則、社群 26 則（五類並行 foreground，人物今日無條目跳過；**本雲端 routine 環境自訂 subagent_type（wiki-reporter-*）未載入，五位記者均改以 general-purpose agent 扮演角色、內嵌完整規則文字派工，屬環境限制的變通做法，功能與品質未受影響**；模型記者事後另補派一輪，評估安全政策記者轉知的 Moonshot/Fable 5 蒸餾指控是否需補記，判斷後未寫入，理由詳下）
- 更新頁面：
  - **模型**：`entities/fable-5.md`（頂部 callout 覆寫為 07-20 GitHub Issue #79337「Max 方案誤判需購買 usage credits」事件，與同日 Anthropic Status 已證實的誤判事件吻合，官方已確認並建議重啟；現況/配額段落、歷史記錄同步更新，並全文 grep 確認無殘留舊日期字串）、`topics/model-comparison.md`（callout、快速選型表同步）。補派一輪評估白宮指控中國 Moonshot AI 蒸餾 Fable 5、財政部揚言制裁一事，判斷**不補記**：對 Fable 5 本身狀態/可存取性無影響（受制裁對象是 Moonshot 非 Fable 5），且更早、規模更大的 06-10 阿里巴巴蒸餾指控事件當時同樣未記入本頁，維持判準一致；來源亦僅標題可用、待核實，未達本頁既有收錄門檻
  - **功能**：`entities/claude-code.md`（版本表新增 v2.1.218／SDK python v0.118.0／SDK typescript sdk-v0.113.0；已知問題新增 7 則——#80002 macOS Filesystem tools/call 59 留言、#61015 排程 routine MCP approval 回歸 40 留言、#62699 複製文字失效 34 留言、#39523 bypass permissions 9 個月未解 33 留言、#63903 記憶體前導文字未抑制 32 留言、#69415 API 連線中斷 32 留言、#37323 `/btw` VS Code 缺失 31 留言；#13354／#24726 互動數同步更新）、`entities/managed-agents.md`（SDK python v0.118.0 新增 Managed Agents API 支援）、`entities/claude-security.md`（MarkTechPost 報導 Claude Security 終端機外掛 Beta 版，與既有 Enterprise 版本關係待查證）、`topics/official-community-gap.md`（「多代理 PR/程式碼審查」矩陣同步 v2.1.218 `/code-review` 背景化）
  - **商業**：`topics/anthropic-business.md`（AMD 最高 50 億美元晶片暨投資協議三獨立來源；15 億美元著作權和解案後續，《哈利波特》出版商獲賠；IPO 敘事延燒兩則；Economic Futures Research Fund 2 億美元研究議程、Economic Index connector）、`topics/enterprise-cost-management.md`（Amazon 削減 Alexa 對 Anthropic 高成本模型依賴，判斷不符 enterprise-tool-tracker 的「AI 編碼工具」範疇，改記於此）、`topics/competitor-landscape.md`（Cline vs Claude Code vs Copilot 定價比較，$0/$20/$10）
  - **安全政策**：`topics/anthropic-government-policy.md`（白宮官員指控中國 Moonshot AI 蒸餾竊取 Fable 5 技術，財政部揚言制裁，兩獨立來源 TechCrunch／SCMP，callout 覆寫、攻防紀錄與時序同步；轉知模型記者評估是否需同步 fable-5.md，已由模型記者補派評估並判斷不需要）
  - **社群**：`topics/community-tech-discussions.md`（Show HN Bento 單檔 HTML 簡報工具 877 分本日最高互動；arxiv 兒童擬人化 LLM 互動論文 31 分；AMD 投資案 HN 討論串的社群反應面；Simon Willison「pelicanmaxxing」；Reddit 週熱門三模型前端測試對比、AI 訓練資料心得討論）、`topics/community-tech-patterns.md`（dev.to Claude Code + Gemini 圖片編輯技能第一手實作；Reddit 週熱門開源手寫畫布，已同步標記與既有 discussions 討論的衍生關係）；今日 26 則社群節錄中 15 則因未達互動門檻（多數 Show HN 僅 1-9 分、Reddit 走 sort=new score 不可信且無跨來源佐證）或與 Claude/Anthropic 無直接關聯（OpenAI/Hugging Face 事件）不收錄，詳見社群記者回報「未達門檻不收錄清單」
- feature-radar：無新增條目（v2.1.218 為既有 `/code-review` 功能的延續更新，非新條目，計入全覽表 🔥🔥／✅ 推薦）；最新版本行同步至 v2.1.218；本週推薦 Fable 5 條目文字更新反映今日 Max 誤判 bug 與存取政策分歧現況，排序未變；升版風險表因無新增阻擋性/需留意項目維持原 3 列不動，僅同步最新版本行；⏰ 倒數中無變化
- index.md 狀態變更：無
- 新增頁面：無
- 摘要：商業面為今日主軸——AMD 最高 50 億美元投資案、15 億美元著作權和解案定案（哈利波特出版商獲賠）、IPO 敘事持續加溫三線並進；地緣政治面新增白宮指控中國 Moonshot AI 蒸餾竊取 Fable 5 一事並揚言制裁；功能面 v2.1.218 為 `/code-review` 背景化的體驗改善，另有 9 起 GitHub Issue 高互動已知問題集中出現（本日最高 71 留言）；社群面 Show HN Bento 簡報工具以 877 分成為本輪互動最高條目
- 呈現品質：五類共 12 頁全數 ✅ 通過，未出現需修復或待辦項目
- 品質備註：功能記者轉知兩則待主編或後續 ingest 追蹤的次要事項——(1) TestingCatalog 報導的 Claude Voice Mode 新增 Opus/Sonnet 選項僅標題可用且無對應既有頁面，暫記一句於 claude-code.md，待後續細節明朗再決定歸屬；(2) infoq.com「Anthropic 說明如何圍欄化 Claude」內容偏安全架構，僅標題可用，已簡記一句，建議下次 ingest 視新資訊決定是否轉交安全政策記者記入 ai-agent-safety.md。社群記者另建議安全政策記者評估「Quoting Thomas Ptacek」（開放權重模型滲透測試能力）一則的收錄價值，本輪因主體非 Claude Code 社群工作流已排除，未強制轉派

## 2026-07-21 Ingest | news/2026-07-21.md（75 則）

- 來源日報：[[news/2026-07-21]]（75 則，10/10 來源；Google News 35、Hacker News 18、Reddit 16、GitHub Issues 15、dev.to 14、Anthropic Status 7、GitHub 3、Blogroll 2、Anthropic Blog 1、Claude API Release Notes 0）
- 分類派工：功能、商業、安全政策、社群（四類並行 foreground；今日「模型」「人物」無條目，跳過；**本環境自訂 subagent_type（wiki-reporter-*）未被此雲端 session 註冊，四位記者均改以 general-purpose agent 扮演角色、內嵌完整規則文字派工**，屬環境限制的變通做法，功能與品質未受影響，但記者間彼此無法即時轉知，跨記者轉知事項一律回頭由主編處理）
- 更新頁面：
  - **功能**：`entities/claude-code.md`（頂部 callout 覆寫為 v2.1.216 最新版本動態；🌐 服務穩定性新增/更新今日 Status 事件；已知問題新增 2 條 #29579、#11002，既有 6 條留言/反應數同步；🛡️ 安全與隱私新增 Tech Times Bash/Unicode 繞過修補待查證條目）、`topics/official-community-gap.md`（對照矩陣補上 `sandbox.filesystem.disabled`）
  - **商業**：`topics/anthropic-business.md`（$1.5B 著作權和解、AI for Science 罕見疾病徵件、Infinity 融資、Anthropic 生技百日布局）、`topics/enterprise-tool-tracker.md`（阿里巴巴疑似封鎖 Claude Code，❓未確認）、`topics/competitor-landscape.md`（Qwen 3.8／Kimi K3 對 Anthropic 策略挑戰、成本效能對比）、`entities/pricing.md`（Fable 5 Max/Team Standard 計量存取、$200 Max 用戶存取停用回報）
  - **安全政策**：`topics/ai-agent-safety.md`（新增 3 則待查證：Bash/Unicode 繞過修補、Horizon3.ai 加入 Project Glasswing、TBIJ Claude 不遵從 CEO 指令模擬測試）
  - **社群**：`topics/community-tech-patterns.md`（dev.to MCP token 成本實測）、`topics/community-tech-discussions.md`（AI 電影 pipeline、Fable CoT 反向工程、Claudexor、Simon Willison 兩篇部落格、Synapse MCP 工具等 6 則，並清理 6 筆逾 21 天 ☄️閃現舊條目）
  - **主編**：`feature-radar.md`（新增 v2.1.216 條目；本週推薦更新 Fable 5 文字避免「昨日」相對日期過期；升版風險同步最新版本行，風險表與建議未變）；`index.md`（近期異動新增今日摘要，狀態變更／新增頁面均無）
- feature-radar：新增 1 條（Claude Code v2.1.216 `sandbox.filesystem.disabled`）；本週推薦文字微調（非輪替，Fable 5 熱度/推薦地位未變）；升版風險僅同步最新版本行
- index.md 狀態變更：無
- 新增頁面：無
- 摘要：Anthropic 迎來 $1.5B 著作權和解重大進展，同時面臨阿里巴巴 Qwen 3.8／Kimi K3 開源模型的策略性挑戰（The New Stack 實測顯示效果相當但成本更低）；Claude Code v2.1.216 發布新沙箱設定；安全政策面新增 3 則待查證事件（Bash/Unicode 修補、Project Glasswing 新夥伴、模擬測試模型服從性報導）；GitHub Issues 高互動已知問題持續累積（Console scrolling 議題以 353 留言、821 讚居冠）
- 呈現品質：四類共 9 頁全數 ✅ 通過（功能 2 頁、商業 4 頁、安全政策 1 頁、社群 2 頁，其中 community-tech-discussions.md ⚠️ 已修復——清理 6 筆逾期舊條目）
- 品質備註：[安全政策] TBIJ 條目涉及 Dario Amodei 具名情境，記者回報需轉知人物記者評估 `entities/dario-amodei.md`；因本環境記者間無法互相轉知，改由主編親自判斷——該事件為「Claude 在模擬測試中不遵從指令」的模型行為報導，並非 Dario Amodei 本人的具體聲明或行動，未達人物頁「具體聲明/事件」建頁與更新門檻，故未修改 `entities/dario-amodei.md`，僅記錄於此供後續查證追蹤；[功能] 記者回報 HN 留言提及新功能 EndConversation（Claude Code 可主動結束疑似濫用/安全疑慮對話），因僅為單則留言轉述、無官方公告或版本號佐證，未達 feature-radar 准入門檻，未收錄，留待後續 ingest 有官方來源佐證後再評估

## 2026-07-20 Ingest | news/2026-07-20.md（47 則）

- 來源日報：[[news/2026-07-20]]（47 則，10/10 來源；Google News 26、dev.to 15、Reddit 15、Hacker News 11、Anthropic Status 2、Blogroll 1、GitHub Issues 0、GitHub 0、Claude API Release Notes 0、Anthropic Blog 0）
- 分類派工：模型、功能、商業、安全政策、社群、人物（六類並行 foreground；**本環境自訂 subagent_type（wiki-reporter-*）未被此雲端 session 註冊，六位記者均改以 general-purpose agent 扮演角色、內嵌完整規則文字派工**，屬環境限制的變通做法，功能與品質未受影響，但記者間彼此無法即時轉知，跨記者轉知事項一律回頭由主編處理）
- 更新頁面：
  - **模型**：`entities/mythos.md`（Mythos FAQ 標題層級報導記為 ❓ 待查證，未覆寫既有 07-16 callout）、`entities/opus-4-8.md`（交易員押注新 Opus 模型傳聞併入既有觀察段落，標市場推測非官方公告）
  - **功能**：`entities/claude-code.md`（🌐 服務穩定性新增 2 條：Opus 4.5 錯誤率上升🔴監控中已實施修復；Fable 5 Max 方案用戶誤判需點數存取🔴官方已確認誤判並提供重啟建議）
  - **商業**：`topics/anthropic-business.md`（IPO 前瞻表新增 VC 看好上市、SpaceX 式信貸額度傳聞 2 列；戰略合作新增 UST；時序新增美國公衛機構測試、Meta $10bn 運算合作洽談、Memphis 非營利捐款等）；`entities/pricing.md`（Fable 5 免費期昨日到期後 Pro 存取結束方向趨於一致、Max 方案誤判扣點官方事件、南韓 $16.7M 疑似故障帳單）；`topics/competitor-landscape.md`（Alibaba Qwen3.8「僅次於 Fable 5」跨媒體報導、Kimi K3／Deepseek V4／Thinking Machines Inkling 等開源模型動態）
  - **安全政策**：`topics/ai-agent-safety.md`（Nozomi Networks 加入 Project Glasswing、Claude AI 助理疑似可透過瀏覽器擴充功能遭操縱，均 ❓ 待查證）
  - **人物**：`entities/boris-cherny.md`（Bloomberg「Claude Code 創始人」專訪報導，經記者額外查證後標「待查證，極可能為本人」）
  - **社群**：今日 18 則條目（10 則 Show HN 分數 1–15 分、8 則 Reddit sort=new score=0 無週熱門標記）均未達收錄門檻，四個負責頁面均無異動
  - **主編**：`feature-radar.md`（本日無新功能；⭐本週推薦 Fable 5 條目文字同步到期狀態，因內容已實質更新未觸發防霸榜輪替；⏰倒數中移除已到期的 7/19 Fable 5 列，僅保留 8/31 Sonnet 5 促銷列）；`index.md`（近期異動新增今日摘要，狀態變更／新增頁面均無）；`topics/model-comparison.md`（依商業記者轉知查核，快速選型表與情境推薦同步 Fable 5 已到期現況，移除「三度順延至 7/19」等過期措辭）；`entities/mythos.md`（依安全政策記者轉知，於「政策與存取管控」時序表新增 Nozomi Networks／Glasswing 列）
- feature-radar：新增 0 條；本週推薦 Fable 5 條目文字更新（非輪替）；⏰倒數中移除已到期的 7/19 列
- index.md 狀態變更：無
- 新增頁面：無
- 摘要：Fable 5 免費期限昨日（07-19）到期，今日多方報導指向 Pro 訂閱免費存取已結束、Max/Team 方案動向未明；同日 Anthropic Status 錄得兩起服務事件（Opus 4.5 錯誤率上升、Fable 5 Max 方案誤判扣點，均已提供處置說明）；商業面 Meta 傳評估百億美元運算合作、Anthropic 傳仿 SpaceX 模式於 IPO 前尋求信貸額度；阿里巴巴 Qwen3.8「僅次於 Fable 5」引發跨媒體報導
- 呈現品質：六類共 8 頁全數 ✅ 通過（模型 2 頁、功能 1 頁、商業 3 頁、安全政策 1 頁、人物 1 頁；社群無異動不適用）
- 品質備註：[商業] 記者回報 model-comparison.md 舊日期字串查核轉知模型記者，因模型記者已先行完成任務無法即時接力，改由主編親自查核並更新；[安全政策] 記者回報 Nozomi Networks／Glasswing 應轉知模型記者評估 mythos.md 補列，同理改由主編親自處理——均為本環境 subagent_type 限制下記者間無法互相轉知的已知副作用，主編收斂處理，未遺漏

## 2026-07-15 Ingest | news/2026-07-15.md（61 則）

- 來源日報：[[news/2026-07-15]]（61 則，10/10 來源；Google News 36、GitHub Issues 15、dev.to 15、Hacker News 12、Reddit 11、Anthropic Blog 2、Blogroll 2、GitHub 1、Anthropic Status 1、Claude API Release Notes 0）
- 分類派工：功能、商業、安全政策、社群（四類並行 foreground；本日模型／人物無條目，跳過）
- 更新頁面：
  - **功能**：`entities/claude-code.md`（v2.1.210 版本表新增；已知問題新增 6 條——OAuth DNS 登入失敗 #33238 本日最高互動 151 留言、GitHub Connector 不被辨識 #32479、Remote Control 自動重連失效 #34255、GitLab 整合請求 #12346、Environment Contributions 警告重現 #3301、跨機器多 agent A2A 協定請求 #28300；🌐 服務穩定性新增 claude.ai container creation 中斷 ✅ 已修復記錄）；`entities/claude-science.md`（早期使用者評價：工作流程加快但仍有缺口）
  - **商業**：`topics/anthropic-business.md`（戰略合作新增 4 列：Claranova PDF 整合、加拿大 AI 研究投資 1,000 萬加幣、Optum+UST 醫療合作、Varonis runtime 安全防護）；`topics/competitor-landscape.md`（HackerNoon Claude Code vs Codex vs OpenCode 比較、Anthropic-Alibaba 競爭關係分析）
  - **安全政策**：`topics/ai-agent-safety.md`（Fable 5 `/btw` 指令繞過安全限制、澳洲企業遭駭客利用 Claude Code、Sonnet 5/Opus 4.8 推理簽章可被還原三則，均僅標題層級資訊，標「❓ 待查證」）；`topics/anthropic-government-policy.md`（Anthropic 招募人力應對災難性風險、逐州加強 AI 規則計畫、EU 官員對安全聽證會派員層級不滿三則）
  - **社群**：`topics/community-tech-discussions.md`（Launch HN Agnost AI 79 分、dev.to「30 天讓 Claude Code 寫 90% 程式碼後變差」第一手反思、Armin Ronacher 具名引用）；`topics/community-tech-patterns.md`（Reddit context 分支/合併工具 source_count=2、dev.to AI 工具挑選漸進採用原則）；今日 8 則 Show HN（1–6 分）與多數 Reddit sort=new 貼文（score=0 無週熱門標記）依門檻規則不收錄
  - **主編**：`feature-radar.md`（新增 Claude for Teachers、Claude Code v2.1.210 兩條；最新版本行同步 v2.1.210）；`index.md`（新增 claude-for-teachers 頁面列、彙整今日近期異動九則）
- feature-radar：新增 2 條（Claude for Teachers 🔥🔥🔥 ⏳ 觀望；Claude Code v2.1.210 🔥 ⚡ 有條件推薦）；本週推薦與升版風險表未變動（僅同步最新版本行），⏰ 倒數中無變化
- index.md 狀態變更：新增 `entities/claude-for-teachers`（無 → active）
- 新增頁面：`wiki/entities/claude-for-teachers.md`
- 摘要：Anthropic 推出 Claude for Teachers 引發多家媒體同步報導，同時 Claude Code OAuth 登入因 DNS 故障成為本日互動量最高的社群回報（151 留言）
- 呈現品質：功能／商業／安全政策／社群四類共 9 頁全數 ✅ 通過，僅 `claude-for-teachers.md` 因原始資料未提供教師驗證入口網址，「快速上手」區塊標 📋 已記錄待辦（頁內已誠實標註原因，待後續日報補齊）
- 品質備註：[安全政策] 記者回報 Fable 5 `/btw` 繞過與澳洲駭客事件涉及 Claude Code 功能面但資訊不足以下結論，已標記「⚠️ 需主編轉知」；因兩則僅有標題層級資訊、功能記者派工時未收到此節錄，主編於此記錄待明日 ingest 若有更多細節時一併轉交功能記者確認是否需記入 `claude-code.md` 已知問題

## 2026-07-13 Query 後續 | 發現並修正 emitted-cache 靜默丟棄 bug，25 則新聞補回

- **提問**：使用者追問「今天有搜尋 Blogroll 的文章嗎」，查證發現 4 篇 Blogroll 文章確實被抓到但完全沒進日報；追問「這不是 GitHub 蒐集的今天的都會有問題嗎」，進一步比對確認範圍遠大於 Blogroll。
- **根因**：GH Actions `daily-gather` 於當日 12:37 UTC 執行成功並寫入 `emitted_items.json` 快取，但當日雲端 routine 未接續產出日報；本機同日稍晚重新抓取時，這批項目的 URL 已被快取判定「已出現過」，除非分數漲幅達 2 倍以上且絕對值 +10 才會重新收錄。實測比對兩次抓取結果，穩定網址來源（HN／GitHub Issues／Reddit／Blogroll）25 則中 21 則、Google News 15 則中至少 4 則，共 **25 則（約 GH Actions 當次抓取的 70%）永久靜默消失**，包含兩則 HN 500+ 分的高熱度討論（token overhead 實測 624 分、批評 Anthropic 文章 557 分）。
- **處置**：
  1. **補回內容**：於 `news/2026-07-13.md` 追加「🔄 補充抓取」區塊記錄全部 25 則；依內容價值分派功能／社群／模型／安全政策四類記者，更新 `claude-code.md`／`fable-5.md`／`opus-4-7.md`／`community-tech-discussions.md`／`anthropic-government-policy.md`；模型記者順帶修正 `model-comparison.md` 殘留的 7/7 舊日期字串。
  2. **根治 pipeline**：`emitted_cache.py` 改為兩階段確認——`--gather-only` 只標記 `digest_confirmed: false`（暫定），新增 `--confirm-digest`（Step 1c，於日報 commit 成功後呼叫）才轉為 `true`；未確認的項目視同未出現過，下次重跑會重新提供，不會被永久靜默丟棄。同步更新 `.claude/commands/news-pipeline-steps.md` 插入 Step 1c。
  3. 對既有 `emitted_items.json` 做一次性遷移：247 筆歷史項目補上 `digest_confirmed: true`（沿用舊制假設），避免這次改動讓所有歷史項目被當成「未確認」而洗版回流。
  4. 新增 `src/tests/test_emitted_cache.py`（7 個測試）覆蓋兩階段確認邏輯，含「score 恆零來源在未確認狀態下應可被重新提供」的回歸測試。
- **commit**：`3beaa9f`（pipeline 修正）、`36319a2`（news+wiki 補回）。

## 2026-07-13 Ingest | news/2026-07-13.md（39 則）

- 來源日報：[[news/2026-07-13]]（39 則，10/10 來源；Hacker News 14、GitHub Issues 15、dev.to 15、Google News 30、Blogroll 4、Reddit 7，來源計數含跨類重疊）
- 分類派工：模型、功能、商業、安全政策、社群、人物（六類並行 foreground，model: sonnet）
- 更新頁面：
  - **模型**：`fable-5.md`（Fable 5／週配額促銷延長至 7/19，多家媒體 Forbes×2/Help Net Security/Economic Times 重複確認，無新細節；Haiku 4.5 錯誤率升高 status incident 判定不收錄；Reddit Qwen-3.6-27B 非 Anthropic 相關略過）
  - **功能**：`claude-code.md`（已知問題新增 6 條：#5826 MCP OAuth 2.1 無法連線 Desktop 66 留言本日最高互動、#38993 Cowork virtiofs 過期檔案 44 留言、#5706 MCP token 刷新缺失、#28077 CLI TUI 無法捲動回看、#29006 Desktop App 遠端控制請求、#28322 `/remote-control` 未識別；內建瀏覽器與 Cowork 行動/網頁版報導核對後確認為既有事件重複來源，未加熱度）；`official-community-gap.md`（產品化矩陣補充 remote-control 相關缺口交叉線索）
  - **商業**：`anthropic-business.md`（LTM 企業合作新增列）；`competitor-landscape.md`（Cursor「Sand」對手產品、Nadella 隱晦批評模型蒸餾、TCS 前線部署工程師團隊、Musk 表態）；`ai-talent-flow.md`（Tom Blomfield 加入 Anthropic）；`pricing.md`（1660 萬美元帳務錯誤、企業多收 170 萬美元）
  - **安全政策**：`anthropic-government-policy.md`（中國「複製」Anthropic/OpenAI 前沿技術、威脅美國國安報導記入攻防紀錄表，單一來源未達 callout 覆寫門檻）
  - **社群**：`code-quality-decline.md`／`community-tech-discussions.md`（額度焦慮系列新節點：Max 5x 用戶回報消耗變快，延燒天數達 17 天；6 則 Show HN 工具因缺互動數字且 community-tech-tools.md 已改 lint-only 未收錄；其餘 Reddit 單則貼文與 GitHub Issues 依分流規則不收錄）
  - **人物**：`tom-blomfield.md`（**新頁面**，前 Monzo 共同創辦人加入 Anthropic，Business Insider 單一來源，標記待核實）
- feature-radar：本日無新功能；升版風險與本週推薦未變動
- index.md 狀態變更：新增 `entities/tom-blomfield`（無 → active（待核實））
- 新增頁面：`wiki/entities/tom-blomfield.md`
- 轉知事項：無（人物/商業記者已互相 wikilink，同步完成）
- 摘要：主軸——Anthropic 新聘 Monzo 共同創辦人 Tom Blomfield；1660 萬美元帳務錯誤與企業多收 170 萬美元；Cursor 推出對手產品「Sand」；Claude Code 已知問題新增 6 條（MCP OAuth/token 刷新、Cowork virtiofs、CLI TUI 捲動、remote-control 相關）；Fable 5／週配額促銷延長至 7/19 多家媒體重複確認；額度焦慮系列延燒滿 17 天
- 呈現品質：全部通過（六記者皆回報 ✅）
- 品質備註：無

## 2026-07-13 Query 後續 | 確認根因：雲端 routine 從未實際建立，已重新排程

- **確認過程**：使用者親自登入 claude.ai routines 頁查看，回報「看起來沒有排」；用 `RemoteTrigger list` 查詢確認，文件記載的 `daily-news-pipeline-cloud`（trig_01JNrBGyrsZk1HjBQeJ7UKLG）確實不存在，帳號下只有 `cloud-writeback-probe`（已停用）與 `weekly-wiki-lint-cloud`（正常運作中）兩個排程。
- **根因**：雲端 routine 那一段自動化文件寫的是設計意圖，但當初從未真的呼叫 API 建立成功（或建立後遺失），07-11、07-12 未自動生日報單純是②從頭到尾沒有排程在跑。
- **處置**：用 `RemoteTrigger create` 重新建立正確排程（`trig_01AWf2wwmVeL3ykPCSyxyvzw`，cron `0 13 * * *`，13:00 UTC/21:00 台北），prompt 含新鮮度防線（比對 `gathered_items.json` 的 date 是否為當日、items 是否非空，不符則中止不生假日報）與完整 pipeline 步驟（讀 news-pipeline-steps.md Step 0/1b + wiki-ingest.md Step 2 + news-pipeline-steps.md Step 3-6，平台覆寫為 python3/Linux 路徑）。已更正 `docs/daily-automation.md`、`docs/workaround-register.md` 對應 trigger ID 與診斷內容。
- **待驗證**：2026-07-14 13:00 UTC 首次真正執行，觀察 master 是否出現完整 news/wiki/web 三段 commit；複查日訂 2026-07-15。

## 2026-07-13 Query | 更正 07-12 自動化失敗誤判：GH Actions 抓料實際成功，缺口在雲端 routine

- **提問**：使用者追問「為什麼昨天的日報排程派工失敗」，並提供 07-12 GH Actions `daily-gather` run 的完整 CI log 供比對。
- **原始誤判（見下方「2026-07-12 Ingest」條目的「補跑說明」與「品質備註」）**：因本機當時 `git log --all` 尚未 fetch 到該次 GH Actions 直接 push 的遠端 commit，誤判該次 run「無資料變化可 commit」，因而懷疑抓料腳本邏輯有 bug。
- **依使用者提供的完整 log 更正**：GH Actions 於 2026-07-12 11:16–11:18 UTC 執行，抓到 61 項 dedup 後 61→enrichment 61→relevance filter 58→emitted-cache filter 58→34 項，**正常 commit `e18b02d`（data: daily gather 2026-07-12）並於 11:18 UTC push 成功**，比雲端 routine 13:00 UTC 早近 1h42m，緩衝充足。GH Actions 抓料這段本次完全正常，先前的懷疑不成立。
- **收斂後的根因**：問題單純落在雲端 routine（`daily-news-pipeline-cloud`，trig_01JNrBGyrsZk1HjBQeJ7UKLG）當日 13:00 UTC 那次執行——沒有任何產出痕跡（無 digest/wiki-ingest commit），是根本沒觸發還是觸發後失敗尚未確認，此工具無法讀取 routine 執行紀錄，需使用者查 claude.ai routines 頁。
- **處置**：`docs/workaround-register.md` 對應列已更正診斷內容（標記 GH Actions 端已排除、鎖定雲端 routine 端），複查日維持 2026-07-14。

## 2026-07-12 Ingest | news/2026-07-12.md（43 則，補跑）

- 來源日報：`news/2026-07-12.md`（43 則，10/10 來源；Hacker News 16、GitHub Issues 15、dev.to 15、Google News 27、Reddit 10、Blogroll 4；來源計數含跨類重疊）
- **補跑說明：** 2026-07-12 全日自動化管線未產出——GH Actions `daily-gather` 排程於 11:16 UTC 執行成功（早於雲端 routine 13:00 UTC 約 1h44m，理論緩衝足夠），但該次 job 判定「無資料變化可 commit」（無 `data: daily gather 2026-07-12` commit），後續雲端 routine 也無任何產出痕跡（無 `news: daily digest`／`wiki: auto-ingest` commit），根因尚未確認（無法從 GitHub Actions 匿名存取取得完整 Python 執行 log，需登入查證）。本次由本機 `/news-pipeline 2026-07-12` 補跑：Step 1a 重新抓取成功（43 則，10/10 來源皆 OK，Reddit 過程出現多次 429 但最終仍正常回應）
- 分類派工：模型、功能、商業、安全政策、社群（人物記者判定無條目落入收錄範圍，未更新任何頁面）
- 更新頁面：
  - **模型**：`fable-5.md`（免費期限延長至 7/19 同步）；`opus-4-7.md`（暫記 Opus 4.6「J-space」隱藏推理空間研究發現＋Reddit 對 Qwen3-8B 跟進實驗，並標註「無獨立頁暫記於此」）
  - **功能**：`claude-code.md`（已知問題新增 #36168 bypass-permissions 於 v2.1.77 後全面失效、#60334 圖片處理 API 錯誤耗額度、#1785 MCP Sampling 功能請求、#20696 網頁/行動版對話壓縮偶發卡死；#16157 Max 額度瞬間觸頂留言數更新至 1480）
  - **商業**：`pricing.md`（週用量 +50% 促銷與 Fable 5 免費期限統一延長至 7/19）；`anthropic-business.md`（UST 訓練 2 萬員工案例第二來源跟進，標註媒體擴散非新事件）
  - **安全政策**：無更新（Unicode 撇號 steganography 為 `safety-china-trust-dispute.md` 已收錄事件之第三次重複出現；舊金山抗議照片報導內容單薄、非政府-Anthropic 互動事件，兩者皆判定不收錄）
  - **社群**：`community-tech-discussions.md`（新增 token overhead 實測討論：Claude Code 33k vs OpenCode 7k，兩獨立來源達門檻）；`community-tech-patterns.md`（新增 5 條 dev.to 第一手實作：session-indexer、Skill Linter 診斷、AWS Bedrock 成本教訓、Fable 5 分層路由心法、customer-finder skill；5 個 Show HN 工具因缺互動數字未收錄；tokenmixai／grenishrai／ai_made_tools 共 5 篇依內容判斷排除）
- feature-radar：Claude Code Desktop 內建瀏覽器熱度 🔥→🔥🔥（第二媒體來源＋互動能力細節）；⏰倒數中原 7/12＋7/13 兩列合併為 7/19 統一到期列；本週推薦同步更新 Fable 5 免費期限文字；升版風險未變動
- index.md 狀態變更：無
- 新增頁面：無
- 轉知事項：無
- 摘要：主軸——GH Actions 抓料成功但雲端 routine 當日無產出，07-12 自動化管線第二次失敗（與 07-11 首跑失敗根因不同，這次抓料端本身「無變化可 commit」，非新鮮度防線中止），已本機補跑補齊；Fable 5／週配額促銷再延至 7/19（GPT-5.6 Sol 同級競爭壓力）；Claude Code 已知問題新增 4 條（bypass-permissions 失效、對話壓縮卡死等 regression）；Anthropic Opus 4.6 J-space 隱藏推理空間研究；Claude Code 33k vs OpenCode 7k token 開銷實測討論
- 呈現品質：全部通過（模型／功能／商業／社群四記者皆回報 ✅；安全政策記者判定無新事實，未修改頁面；人物記者判定無條目落入範圍，未修改頁面）
- 品質備註：GH Actions `daily-gather` 3 小時緩衝（a053900 修復）仍未能穩定產出當日資料，`docs/workaround-register.md` 該列複查日 2026-07-14 前需再次確認根因（本次無法排除是抓料腳本邏輯 bug 導致誤判無差異，也無法排除雲端 routine 端當日未觸發）

## 2026-07-11 Ingest | news/2026-07-11.md（51 則，補跑）

- 來源日報：`news/2026-07-11.md`（51 則，10/10 來源；GitHub Issues 15、dev.to 15、Google News 4、Hacker News 6、Reddit 11、GitHub 1）
- **補跑說明：** 每日自動化分裂架構首跑日，GitHub Actions 抓料實際延遲至 14:02 UTC（設計 12:30 UTC），雲端 routine（設計 13:00 UTC 開跑）因新鮮度防線正確中止未生假日報；本次由本機手動 `/news-pipeline 2026-07-11` 補跑（詳見 `docs/daily-automation.md`）
- 分類派工：功能、商業、安全政策、社群（四類並行 foreground，model: sonnet；今日無模型類、人物類條目）
- 更新頁面：
  - **功能**：`claude-code.md`（v2.1.207 Auto mode 於 Bedrock/Vertex/Foundry 改預設開啟＋終端機凍結修復；已知問題新增 #24055 32000 output token 上限、更新 #53262 HERMES.md 計費誤判）
  - **商業**：`anthropic-business.md`（Claude Corps 非營利 AI 教育計畫、$65K 職缺與舊金山住房負擔爭議報導）；`pricing.md`（#38335 Max session 額度異常留言數 790→792 續增、Sonnet 5 促銷第一手實測、AWS Bedrock 首日成本 $8.43 案例）；`competitor-landscape.md`（新增 pi-coding-agent／GLM 5.2 待查證競品定價條目）
  - **安全政策**：無更新（Unicode 撇號 steganography 指控為 07-10 已收錄事件之重複出現，非新事實）
  - **社群**：`community-tech-patterns.md`（新增 ccteams subagent 團隊套件化工具）；`community-tech-discussions.md`（新增 WebFetch 68,000 token 成本觀察討論）
- feature-radar：新增 Claude Code v2.1.207（🔥🔥 ⚡）、Claude Code Desktop 內建瀏覽器（🔥 ⏳ 待驗證，單一媒體來源尚待官方或社群佐證）；升版風險最新版本行更新為 v2.1.207；本週推薦與⏰倒數中均未達變動門檻，維持不動
- index.md 狀態變更：無
- 新增頁面：無
- 轉知事項：社群記者回報 ccteams（subagent 團隊套件化）為新的 agent 工作模式，請下次功能記者評估 `official-community-gap.md` 產品化矩陣是否新增列
- 摘要：主軸——Claude Code v2.1.207 發布（Auto mode 三平台預設開啟＋終端機凍結修復）；GitHub Issues 熱度持續（HERMES.md 計費誤判 533 讚同、Max session 額度異常 792 則、32000 token 上限錯誤）；Anthropic Claude Corps 非營利計畫與 SF 職缺住房爭議報導；社群工具與定價實測（ccteams、Sonnet 5 促銷分析、Bedrock 成本經驗）
- 呈現品質：全部通過（功能／商業／社群三記者皆回報 ✅；安全政策記者判定無新事實，未修改頁面）
- 品質備註：無

## 2026-07-09 Ingest | news/2026-07-09.md（60 則）

- 來源日報：`news/2026-07-09.md`（60 則，10/10 來源；Google News 32、HN 12、Reddit 16、GitHub Issues 10、Anthropic Status 1、Anthropic Blog 1）
- 分類派工：模型、功能、商業、安全政策、社群（五類並行 foreground，model: sonnet；今日無人物類條目，不派工）
- 更新頁面：
  - **模型**：`sonnet-5.md`（07-09 評測分數/定價傳聞，定價面留給商業記者）；`opus-4-8.md`（callout 更新，Reddit 弱訊號好感度回饋標註參考）；`fable-5.md`（官方 orchestrator 基準 46% 成本/96% 效能補入，來源未附原始連結已標註）；`model-comparison.md`（同步新增 Fable 5 orchestrator 協作基準列）
  - **功能**：`claude-code.md`（AGENTS.md #6235 反應數 5598→5627；新增/更新已知問題：Console scrolling #826、Screen Flickering #769/#1913、Buddy 請願 #45596、多帳號 Connector #27302、Stream idle timeout #46987、Max 5x 帳號停用 #5088）；`official-community-gap.md`（AGENTS.md 矩陣反應數同步）；**feature-radar 新增 Reflect with Claude（🔥🔥🔥 ⚡）**
  - **商業**：`anthropic-business.md`（次級市場估值 1.2 兆、Anthropic/OpenAI/SpaceX 市值超越 25 年退場交易總和、TeraWulf 35 億續融資、AWS 治理功能、藥物研究後續、Salesforce Slack 內部觀感，戰略合作表新增 AWS 列）；`pricing.md`（INR #17432 反應數 594→598、Max 額度 #38335 留言 790→791 + Reddit 27%/7% 案例）；`competitor-landscape.md`（新增 Meta AI 程式輔助工具競品條目）
  - **安全政策**：`ai-agent-safety.md` + `anthropic-government-policy.md`（中國「後門」指控延燒第二天，WSJ/Fox Business/TechRadar/Yahoo Tech，TechRadar 首見「建議解除安裝」；Anthropic dual-use knowledge「關閉開關」研究說明；獨立頁建頁門檻評估：三方仍未正式回應，暫不建頁，留待週度回顧）
  - **社群**：今日 15 則條目均未達收錄門檻或已由其他記者/既有頁面涵蓋，無頁面更新（Reflect with Claude HN 29 分由功能記者處理官方功能頁；Claude Certified 認證公告已轉知主編評估）
- feature-radar：新增 Reflect with Claude（🔥🔥🔥 ⚡ Preview）；本週推薦輪替（Sonnet 5 已連續推薦 >7 天且今日未更新，依防霸榜規則換為 `/goal` 指令；Fable 5、Cowork 維持）；最新版本行維持 v2.1.204（今日無新版本）；⏰ 倒數中不動（無到期/新增）
- index.md 狀態變更：無（無實體狀態主值變更）；近期異動 prepend 4 筆 07-09
- 新增頁面：無
- 摘要：主軸——Anthropic 發布「Reflect with Claude」測試版使用回顧功能（多媒體同步報導，TechCrunch 提出質疑角度）；中國「後門」指控延燒進入第二天；Anthropic 次級市場估值傳飆升至 1.2 兆美元；AGENTS.md 支援請求反應數持續攀升（5627 讚）
- 呈現品質：全部通過（五記者 + 主編；ai-agent-safety.md 修復現況時序侵蝕、opus-4-8.md 修復過期 callout）
- 品質備註：社群記者本次無頁面更新但完整交代 15 則條目逐一比對門檻的判斷過程，回報品質良好非疏漏；Claude Certified 認證公告主編評估後判斷資訊過於單薄（無官方連結佐證），暫不轉功能記者，留待未來有更完整報導再收錄

## 2026-07-08 Query | Reddit 條目 score 恆為 0 → 系統性被 wiki 門檻擋掉

- **使用者點出：** 問「這幾天 Fable 5 有什麼有趣的應用」發現答案異常稀薄，直覺「是不是資料來源的問題」。
- **查證：** `gathered_items.json` 全部 12 條 Reddit score 皆為 0（HN/GitHub Issues 皆有真實分數）。
- **根因（兩層疊加）：**
  1. 無 `REDDIT_CLIENT_ID/SECRET` → 走 RSS fallback（Phase A 的 429 限流即此路徑特徵）
  2. `sources/reddit.py` RSS 路徑 `score=int(entry.get("slash_comments", 0))` 為死碼——Reddit Atom RSS 不帶讚數/留言數，恆回退 0（OAuth 路徑 `post.get("ups")` 才正確）
  - 後果鏈：score=0 → 過不了 `wiki-reporter-shared.md` 互動門檻（Reddit ≥20 讚）→ **每天所有 Reddit 條目在 wiki 收錄階段全被丟棄**；r/ClaudeAI/r/ClaudeCode 的 showcase（如 Fable 應用實測）系統性消失。另 RSS 抓取偏「最新」（`sort=new`）+ 26h 窗，2-3 天前爆紅但稍舊的貼文也抓不到。
- **處置（本次）：** 改 `sources/reddit.py` RSS 抓取為雙輪（`sort=new` + `sort=top&t=week`），跨輪去重、new/top 各分一半預算（各 10）、每 sub 每輪上限 6、加 1s inter-request 節流緩解 429。→ 讓**日報**得以surface近一週熱門 Reddit 貼文（含稍舊 showcase）。31/31 測試通過。
- **未竟（待使用者定奪）：** score 仍為 0（RSS 天生無此欄），故 **wiki 收錄端門檻仍無法機械式放行 Reddit**。根治需擇一：(a) 設 Reddit OAuth 憑證（程式已備 `ups` 路徑）；(b) 改收錄門檻規則，讓「來自 top-of-week 抓取」本身視為達門檻（需標記來源 + `/review-commands`）。
- **防再犯建議：** 可加「整個來源所有條目 score 皆 0 但 score_unit 宣稱為真實指標」的資料品質告警，避免此類靜默劣化再度無人察覺。
- **注意：** `sources/reddit.py` 改動尚未 commit/push；憑此路徑決定後再一併處理。

## 2026-07-08 Ingest | news/2026-07-08.md（72 則）

- 來源日報：`news/2026-07-08.md`（72 則，10/10 來源；Google News 41、HN 17、GitHub Issues 10、Reddit 12、Anthropic Status 3、GitHub 2）
- 分類派工：模型、功能、商業、安全政策、社群、人物（六類全數並行 foreground，model: sonnet）
- 更新頁面：
  - **安全政策**：`ai-agent-safety.md` + `anthropic-government-policy.md`——**中國官方層級首度指控 Claude Code「後門」**（工業主管機關資安警示，稱秘密追蹤/回傳資料，Reuters/WSJ/CNBC/CBS/Cybernews/China Daily 等 8+ 家）；兩頁 callout 覆寫、攻防紀錄新增兩列（🏛️ 中國官方、🌐 Yahoo 阿里禁令呼應）、時序新段；明確標註與 07-07「內部實驗」定調正面矛盾、未強行調和；獨立頁門檻仍未達（留待週度回顧）
  - **功能**：`claude-code.md`（v2.1.204 版本列純 bug fix、已知問題新增 4 條 #32479/#59033/#24798/#8660 + 5 條計數更新、現況加 Cowork 行動/網頁段）；`claude-tag.md`（GitHub 操作錯誤率事件→已修復）；`official-community-gap.md`（平台可及性缺口因 Cowork 擴展同步）；**feature-radar 新增 Cowork 行動/網頁版（🔥🔥🔥🔥 ⚡）**
  - **商業**：`anthropic-business.md`（3Q26 獲利 >10 億、Microsoft 自研模型替代風險列、曼哈頓擴張、Cowork 進政府）；`pricing.md`（Fable 5 免費期延至 7/12、Max 額度異常/token 3-5x 配額節點）；`competitor-landscape.md`（Microsoft 自研 🔴 + Perplexity 傳聞競品，均標未證實）；`enterprise-tool-tracker.md`（Alibaba 既有事件僅補來源、狀態不變）
  - **模型**：`fable-5.md`（免費期延 7/12 + XDA zero-shot 實測，wikilink pricing）；`sonnet-5.md`（07-08 錯誤率升高同日解決，輕量）
  - **社群**：`community-tech-patterns.md`（Shellular 手機遠端操作補入「行動裝置遠端控制」模式類，呼應 Cowork 官方趨勢）；`community-tech-discussions.md`（Geosql 4 倍改善數據質疑，HN 55 正反交鋒；同步清理 14 條逾 21 天 ☄️閃現）；Reddit 條目 score 均 0 未達門檻不收
  - **人物**：`boris-cherny.md` + `cat-wu.md`（inc.com「Head of Claude Code」5 員工原型，頭銜未具名，兩候選頁均以（待核實）記錄並互加 wikilink）
- feature-radar：新增 Cowork 行動/網頁版（🔥🔥🔥🔥）；最新版本行 → v2.1.204；⏰ 倒數中新增 7/12 Fable 免費到期列（移除已生效的 7/7 過渡註記）；本週推薦輪替（Artifacts → Cowork，Fable 5 更新為免費延 7/12）
- index.md 狀態變更：無（無實體狀態主值變更）；近期異動 prepend 5 筆 07-08
- 新增頁面：無
- overview：當前局勢「信任危機」升級為國家級對峙段落；近兩週事件表 prepend 4 筆 07-08、範圍更新至 07-08
- 摘要：主軸——**中國官方政府層級首度指控 Claude Code「後門」**（8+ 媒體，與官方「實驗」定調正面矛盾，信任爭議升為國家級）；Claude Cowork 擴展行動/網頁版（雲端持續執行，🔥🔥🔥🔥）；Fable 5 免費延 7/12；Microsoft 傳自研模型替代
- 呈現品質：全部通過（六記者 + 主編；多頁 callout 覆寫、摘要精簡、時序同步）
- 品質備註：社群記者回報 Reddit score 均 0（Reddit 分數未被 gathered_items 追蹤）故全數未達門檻不收——屬資料來源限制而非記者判斷問題，已如實標註

## 2026-07-07 Ingest | news/2026-07-07.md（42 則）

- 來源日報：`news/2026-07-07.md`（42 則，10/10 來源；Google News 20、GitHub Issues 10、HN 5、Reddit 10、Anthropic Status 2、Anthropic Blog 1、GitHub 1）
- 分類派工：模型、功能、商業、安全政策、社群、人物（六類全數並行 foreground）
- 記者回報彙整：
  - **模型**：`sonnet-5.md` 輕量新增（錯誤率升高、同日解決）；fable-5／model-comparison 不動。主編另**修正 fable-5 昨日殘留「大規模錯誤」→「錯誤率升高」**（把新 Step 1b 守則回頭套用到既有內容）
  - **功能**：`claude-code.md` 新增 v2.1.202 版本列 + 3 條已知問題（#18170 複製夾帶縮排、#33969 每輪工具呼叫限制回歸、#38005 缺 RTL）+ 6 條累積數更新；`claude-tag.md` 穩定性事件；`official-community-gap` 產品化矩陣同步 v2.1.202 與 InstantVideos 多模型 pipeline；**feature-radar 新增 v2.1.202「Dynamic workflow size」**（🔥🔥）
  - **商業**：`enterprise-tool-tracker` Alibaba 補「改用 Qoder」+ 新增 Alberta 省政府（20hr 掃 4.66 億行）；`pricing` INR 需求互動數更新（594/205）；`competitor-landscape` 新增 CNBC 中國模型成本趨勢 + DeepSeek「Deep Code」
  - **安全政策**：**隱藏追蹤器定調「實驗」**——ai-agent-safety／anthropic-government-policy／anthropic-commitments 三頁一致更新（spyware 指控 ❓→🟡，措辭「官方單方說法、社群接受度待觀察」）；Radware 第三方防護生態記入
  - **社群**：`community-tech-patterns` 新增 InstantVideos 多模型短片 pipeline；Reddit 五則低互動未達門檻不收
  - **人物**：新增 `entities/teresa-carlson.md`（前 Microsoft/AWS 高管主導公部門，待核實）
- feature-radar：新增 v2.1.202；升版風險「隱寫術」列 🔴→🟡（Anthropic 定調實驗）；倒數中移除已生效的 7/7 Fable 過渡、新增 7/13 週配額到期；最新版本行 → v2.1.202
- index.md 狀態變更：新增 `entities/teresa-carlson`（active 待核實）；近期異動新增 7 筆
- 新增頁面：`wiki/entities/teresa-carlson.md`
- overview：當前局勢「信任危機」更新為 Anthropic 首次回應；近兩週事件表 prepend 3 筆 07-07
- 摘要：主軸——隱藏追蹤器獲 Anthropic 定調「實驗」（信任危機首次官方回應）；Alibaba→Qoder + Alberta 省政府（企業一退一進）；v2.1.202 新設定
- 呈現品質：全部通過（六記者 + 主編；多頁記者主動修復 callout/摘要超段）
- 驗證：**新 Step 1b 程度詞守則首次上線即生效**——兩則 Status「Elevated errors」正確譯為「錯誤率升高」未加碼；並回頭修正 fable-5 昨日殘留

## 2026-07-06 Query | 日報「大規模錯誤」翻譯加碼 + 頂部「前次動態」callout 堆疊

- **使用者點出：**
  1. 今日聚焦「多模型大規模錯誤」放大了來源 `Elevated errors`（狀態頁術語＝錯誤率升高，中性/低強度）——把「several models」的**廣度**當成「大規模」的**規模**
  2. 5 頁頂部保留「前次動態」callout，只想留單一最新（目的僅為看最後更新什麼）
- **根因：**
  1. Step 1b 生成日報時，severity 從情境 gestalt（多模型受影響＋[風險警示]標籤）補值，而非錨定原文的字；System prompt 既有的「客觀」擋不住這種感知型放大
  2. callout 被「prepend、保留歷史」的手感誤套（callout 是全 wiki 唯一該覆寫而非疊加的地方），且一次未攔即自我繁殖為頁面既定結構
- **處置：**
  - `.claude/commands/news-pipeline-steps.md` Step 1b：persona「AI 技術」→「Claude 與 Anthropic 生態」（涵蓋商業/政策）；加程度詞測試（每個程度形容詞須能在 `gathered_items.json` 原文找到同等強度依據，否則降回中性）；今日聚焦加「標籤不授權升高語氣」
  - `.claude/rules/wiki-ingest-format.md`：callout 明訂「**覆寫、不留前次**」
  - 刪除 5 頁「前次動態」callout：enterprise-tool-tracker / enterprise-cost-management / competitor-landscape / anthropic-business / pricing（僅留最新）
- **防再犯：** 兩處源頭規則均已修（非只改靜態值）；`/review-commands` 零錯誤通過；memory 新增 query-log 機制本身
- **注意：** 以上改動尚未 commit/push，web_reader json 仍為舊版，待下次 pipeline 或手動 rebuild 才反映到線上

## 2026-07-06 Ingest | news/2026-07-06.md（57 則）

- 來源日報：`news/2026-07-06.md`（57 則，10/10 來源；Google News 32 則、Hacker News 12 則、GitHub Issues 10 則、Reddit 11 則、Anthropic Status 1 則）
- 分類派工：模型、功能、商業、安全政策、社群、人物（六類全數並行 foreground 派工）
- 記者回報彙整：
  - **模型**：`entities/fable-5.md` 新增「Anthropic 多模型一度大規模錯誤、Fable 5 一併受影響（同日解決）」與 Show HN Python-on-SNES 實測案例（解封後 90 分鐘修復 23 個編譯器 bug）；狀態維持 active，無 feature-radar
  - **功能**：`entities/claude-code.md` 新增 7 條高互動 GitHub Issue（#4953 120GB+ 記憶體洩漏 OOM、#5674 macOS ECONNRESET、#2805 Linux CRLF、#14828 Windows 主控台閃爍、#14088 OneDrive/mapped drive 對話歷史遺失、#13354 session 額度接續、#36151 Mobile 多帳號切換）+ 三則累積數更新（#73125 391 讚、#69238、#60705）；平台相容性組頭 11→13、計費配額組頭 6→7；均非 regression 故不動升版風險列。**主編轉知處理**：`official-community-gap.md` 產品化矩陣新增「多平行 agent 即時可觀測性／協調地圖」列（❌ 無官方對應，Agent View 僅列表式非 live map）
  - **商業**：`anthropic-business.md` 新增 **TeraWulf 190 億美元/20 年肯塔基資料中心租約**（6+ 家財經媒體、股價 +17%、IREN +5% 聯想）、Samsung 晶片洽談、Google Workspace 受治理 agent、小型企業轉單 Salesforce；`competitor-landscape.md` 新增 Z.ai ZCode、Base 44 vs Anthropic 建站實測、FT 上市結構性挑戰；`enterprise-tool-tracker.md` 新增 Meta 限用列（❓未確認，缺來源細節）；今日無定價數字變動，pricing.md 未動
  - **安全政策**：`ai-agent-safety.md`、`anthropic-government-policy.md` 更新 Alibaba 禁令多媒體確認（單一媒體→多媒體聲稱）+ Meta 同日限用；「中美 AI 工具信任對峙」獨立頁評估——三方未就「後門」正式回應，未達門檻，暫緩建頁並於 government-policy 時序明文記錄評估結論
  - **社群**：`community-tech-discussions.md` 新增 HN 97 分「Anthropic 好感度流失」文（API 穩定性 + vendor lock-in，🔥🔥🔥）；額度焦慮系列跨 9 天（06-27→07-03→07-06）合併升級 ☄️閃現→🌊延燒；`community-tech-patterns.md` 新增 CaveMan skill（token 70→20）、平行 Agent 即時對話地圖（live-log-viewer-next，⏳）；低分 Show HN（Peek-CLI/Open Science/live-memory/terminai）未達門檻未收錄
- feature-radar 新增：無（今日條目為 GitHub Issues、企業/基礎設施商業事件、社群討論，均不符官方新功能准入定義）；版本行（v2.1.201）、倒數區塊（7/7 Fable 5 配額過渡、8/31 Sonnet 5 促銷）、本週推薦均維持不變，僅同步最後更新日期
- anthropic-commitments：本日無「官方承諾修復/政策/拒絕/兌現」事件，未動此頁
- overview.md：更新「當前局勢」——信任危機擴散（Alibaba 多媒體確認 + Meta 同日限用）、新增「基礎設施擴張」段落（TeraWulf 租約）；近兩週重大事件表 prepend 4 筆 07-06 事件；商業動態段落同步
- index.md 狀態變更：無；近期異動新增 9 筆頁面更新記錄
- 新增頁面：無
- 摘要：今日雙主軸——TeraWulf 190 億美元資料中心租約（算力自主里程碑）+ 企業安全審查擴散（Alibaba 多媒體確認 + Meta 跟進）；Claude Code 穩定性 issue 集中爆發
- 呈現品質：全部通過（六記者 + 主編轉知；ai-agent-safety.md、anthropic-business.md、enterprise-tool-tracker.md 三頁記者主動修復摘要/callout 超段問題）

## 2026-07-05 Ingest | news/2026-07-05.md（29 則）

- 來源日報：`news/2026-07-05.md`（29 則，10/10 來源；GitHub Issues 10 則、Reddit 10 則、Hacker News 6 則、Google News 3 則）
- 分類派工：功能、商業、社群（三類並行 foreground 派工）；模型、安全政策、人物本日無獨立條目（Sonnet 5/Fable 5/Opus 4.8/Mythos 討論均屬社群一手心得分享，非新模型事實，歸社群記者處理）
- 記者回報彙整：
  - **功能**：`entities/claude-code.md` 新增 6 條已知問題（Advisor API 無回應❓、model behavior 三模式❓、Focus escape sequences 洩漏、申訴表單迴圈、MCP/hooks/plugins 需重啟）；#38335（Max 額度異常，793 留言）、#6235（AGENTS.md，5598 讚，全站最高）、#73125（AskUserQuestion 60s，383 讚）累積數字更新；`official-community-gap.md` 同步 AGENTS.md 矩陣列反應數；#26408（sonnet-4-6 問題）內容單薄略過
  - **商業**：`enterprise-tool-tracker.md` Alibaba 禁令生效日確認為 2026-07-10（不新增列，更新既有列）；`anthropic-business.md` 新增 AFR 澳洲 1.4GW 資料中心採購、MixRoute 支援 Fable 5（生態邊緣，商業影響標記有限）
  - **社群**：`community-tech-discussions.md` 新增 Microsoft Fast Context 下架爭議討論（本地 LLM 分流節省 context 機制，已同步至 community-tech-patterns 技術彙整）、Anthropic 疑似 prompt injection 單方指控（待查證，誠實標註無社群延燒）；審查疲勞子觀察併入既有 Skill Atrophy 段落；其餘低分 Show HN／Reddit 帖（HN score 1-3、Reddit RSS 抓取限制導致 score 顯示 0）訊號強度不足未收錄
- feature-radar 新增：無（今日條目均為 GitHub Issues bug/feature request，非官方發布功能，不符准入定義）；版本行、倒數區塊、本週推薦均維持不變（v2.1.201、7/7、8/31）
- index.md 狀態變更：無；近期異動新增 5 筆頁面更新記錄
- 新增頁面：無
- 呈現品質審查：三位記者皆回報 ✅ 通過，無待辦
- 品質備註：功能／商業／社群三位記者的 Agent 派工初次以背景模式啟動，完成通知未直接送達本 ingest session；經檢查磁碟上的實際修改內容與各記者最終回報訊息確認任務均已正確完成，未重跑，後續派工應留意 foreground 設定生效狀況

## 2026-07-05 Ingest | news/2026-07-04.md（41 則）

- 來源日報：`news/2026-07-04.md`（41 則，10/10 來源；Reddit 14 則、GitHub Issues 10 則、Google News 11 則、Hacker News 9 則）
- 分類派工：功能、商業、社群、模型（四類並行 foreground 派工）；安全政策、人物本日無條目
- 記者回報彙整：
  - **功能**：`entities/claude-code.md` 已知問題新增 4 條（額度 84% 誤觸發 limit、Windows Desktop relaunch 失敗、Cowork virtiofs FUSE 過期檔案、Cowork tab 消失）+ 多帳號/Linux/WSL/Skills 同步功能請求聚集；v2.1.201 純 reliability 調整不進 feature-radar；跨類別條目「session/cache leakage」已轉知安全政策記者評估（本輪安全政策記者未派工，待下輪或 lint 追蹤）
  - **商業**：`enterprise-tool-tracker.md` Alibaba 列補確認日期（不新增列，同一事件多媒體擴散）；`pricing.md` 新增 Claude Enterprise Spend Controls；`enterprise-cost-management.md`、`anthropic-business.md` 同步更新；Samsung 晶片洽談維持初步報導標記
  - **社群**：`code-quality-decline.md` 新增 07-04 時序（plan mode 逾時代答、CLI 變慢投訴延續）；`community-tech-discussions.md` 補充既有 AskUserQuestion 列；15 則 Show HN／Reddit 條目因訊號強度不足（多數 HN score 1-11 分低於低門檻）未收錄，留待 lint 時 community-tech-tools 策展評估
  - **模型**：thestreet.com 為已記錄事件（Defense in Depth，07-02）的媒體回顧，未更新；GLM 5.2 條目與 Claude 模型本身無直接關聯，未更新
- feature-radar 新增：無（今日無符合准入定義的新官方功能）；版本行、倒數區塊維持不變（v2.1.201、7/7、8/31 均未變化）
- index.md 狀態變更：無；近期異動新增 7 筆頁面更新記錄
- 新增頁面：無
- 呈現品質審查：四位記者皆回報 ✅ 通過，無待辦

## 2026-07-04 Lint

- 修正矛盾：
  - Mythos 5 狀態：`topics/model-comparison.md` 快速選型表「仍限軍事用途存取」與 `entities/mythos.md`（7/1 起白名單擴大為授權機構）矛盾 → 統一為「僅限授權機構/安全研究用途，非一般消費市場」
  - 企業命名：`topics/enterprise-tool-tracker.md` 「Rubrik」與「Rubrik（NYSE: RBRK）」同一企業兩種寫法 → 統一含 ticker 全名
  - 封鎖期天數：`topics/anthropic-government-policy.md` 攻防紀錄 2026-07-01 列殘留「18 天」舊值，與頁面其他 3 處已更新的「18–19 天」不一致 → 統一為「18–19 天（07-03 MarketScale 確認 19 天）」
  - Dario Amodei 現況過期：`entities/dario-amodei.md` 頂部 callout 停留在 6/26「白宮不信任」，未反映 Tom Brown 談判已於 7/1 促成解禁 → 補充後續進展並釐清「談判成果」與「個人信任關係」為兩條線
- 補連結：`topics/official-community-gap.md` ← `entities/claude-code`、`entities/managed-agents`（原單向連結補為雙向）
- 狀態更新：無（各 topics 頁最後更新均在 14 天內，未觸發 3c 過期判定）
- 遷移至 entities：無
- 新增 entities：無（掃描後未發現被提及 3 次以上且無專頁者；近期新人物/產品皆已有專頁）
- 呈現品質：全部通過或已修復（見六位記者回報），無新增待辦
- 超長頁面（> 500 行）：📋 待使用者確認
  - `community-tech-patterns.md`（859 行）：建議將 2026-05 月份技術彙整條目移至新頁 `topics/community-tech-patterns-2026-05.md`（比照 community-tech-timeline 模式），本頁僅留 06-07 月 + 模式概覽表 + 目前結論
  - `community-tech-discussions.md`（981 行）：既有規則要求 > 60 天技術彙整移至 `community-tech-timeline.md`，但從未執行過完整一輪遷移，累積至今造成持續增長；建議執行一次歷史遷移
- 規則檔健檢：
  - wiki/CLAUDE.md：50 行（閾值 80）✅
  - .claude/rules/wiki-ingest.md：71 行（閾值 80）✅
  - .claude/rules/wiki-ingest-format.md：138 行（閾值 200）✅
  - 各記者規則檔：models 55 / features 138 ⚠️ / commercial 78 / safety-policy 54 / community 112 ⚠️ / community-lint 110 ⚠️ / people 42 / wiki-reporter-shared 46（閾值 100）
  - 矛盾（6a）：無（新增的「互動門檻對照表」與既有 `wiki-ingest.md`/`wiki-ingest-community-lint.md` 門檻描述一致）
  - 引用驗證（6b）：7/7 錨點全部通過
  - 遵守率（6c）：近 3 次 ingest 呈現品質審查 3/3、feature-radar 更新提及 3/3 ✅
  - 過期規則（6d）：1 條 > 60 天 — `wiki-ingest-format.md` entities/topics 頁面格式模板 [加入: 2026-04-25]（70 天）；本輪六記者實際套用驗證仍完全吻合現狀，暫無需修訂
  - 簡化（6e）：features 138 行、community 112 行、community-lint 110 行均超 100 行閾值 ⚠️（待使用者確認是否簡化）
  - 來源健康（6f）：📋 待使用者確認 — `sourceStatus` 欄位僅 2026-07-03 起有資料（新來源擴充至 10 個），尚無 3 天基線可判斷「連續 0」；07-03 當日 `lobste.rs`／`Claude API Release Notes`／`Anthropic Blog`／`dev.to` 回傳 count=0，但屬新增/低頻來源非確認故障，建議下次 lint 累積至少 3 天資料後再做正式告警判斷
- 讀者模擬：
  - Claude Code 重度使用者「Alibaba 說有後門，該不該擔心？」→ index → enterprise-tool-tracker，2 跳 ✅
  - AI 系統開發者「AskUserQuestion 60s 逾時社群怎麼看？」→ index → community-tech-discussions，2 跳 ✅
  - Anthropic 生態追蹤者「出口管制解除、承諾兌現了嗎？」→ index → anthropic-commitments，2 跳 ✅
- overview.md：已全文改寫（反映信任危機：embedded spyware 指控 + Alibaba 禁用取代舊版 07-01 三喜臨門敘事）

## 2026-07-03 Ingest（backfill）| news/2026-07-03.md（42 則）

- 來源日報：`news/2026-07-03.md`（42 則，10/10 來源；Reddit RSS 部分 429 仍取得 11 則；GitHub rate limit 提前中止 repo 搜尋但取得 3 則；補跑模式：07-03 pipeline 前日誤跑成 2026-05-19，本次以 `--date 2026-07-03` 回補）
- 核心事件：美國解除 Fable 5 / Mythos 5 出口管制的媒體確認報導（19 天封鎖期）、Alibaba 以「疑似後門風險」禁用 Claude Code（Reuters，多媒體跟進）、FT 報導 Anthropic 封堵中國企業間接存取漏洞、Claude Code v2.1.201 發布、Reddit 深夜集中出現 Fable 額度焦慮討論串
- 派工：安全政策 / 商業 / 功能 / 社群 四位記者（模型、人物今日無條目）
- 更新頁面：
  - `wiki/topics/anthropic-government-policy.md`：出口管制解除延遲報導確認 19 天封鎖期；FT 封堵漏洞新支線；攻防紀錄更新
  - `wiki/topics/ai-agent-safety.md`：Alibaba「後門風險」指控（HN 313，標單方指控待查證）
  - `wiki/topics/enterprise-tool-tracker.md`：Alibaba 新增 ❌ 退出列 + 時序 + 統計
  - `wiki/topics/anthropic-business.md`：The Verge 藥物開發跟進、大廠員工進駐客戶辦公室模式
  - `wiki/entities/pricing.md`：印度 INR 定價需求註記（GitHub Issue 👍584，無官方回應）
  - `wiki/entities/claude-code.md`：版本表 v2.1.201；已知問題新增 AskUserQuestion 60s 逾時（#73125）、v2.1.1 token 暴增（#16856）
  - `wiki/topics/community-tech-discussions.md`：AskUserQuestion 討論 ☄️→🌊 延燒、Ask HN prompt-response 迴圈反思（HN 129）、Reddit 額度焦慮（🔥🔥 誠實標註）
  - `wiki/topics/community-tech-patterns.md`：額度監控模式（⏳：CCLimitPing / LimitBar）
- feature-radar 新增：無（v2.1.201 僅行為調整未達收錄門檻，記入 claude-code 版本表）；升版風險「最新版本」行同步 v2.1.201；⏰ 倒數中無新 deadline；本週推薦不動
- anthropic-commitments：無「承諾/拒絕/兌現」新事件（Alibaba 為指控非承諾），不動
- index.md 狀態變更：無；近期異動區更新 8 頁 + enterprise-tool-tracker / anthropic-business / pricing 摘要行更新
- 新增頁面：無
- 呈現品質審查：四位記者回報均 ✅ 通過
- 備註：記者派工誤用 background 模式導致完成通知未回到 pipeline agent，由協調者轉達四份回報後續行（下次派工須 foreground）

## 2026-07-02 Ingest | news/2026-07-02.md（50 則）

- 來源日報：`news/2026-07-02.md`（50 則，6/6 來源；GitHub 因 rate limit 回傳 0 筆但來源本身正常；Reddit RSS 部分 429 仍取得 20 則；全部為 community 類別，無 official 條目）
- 核心事件：Fable 5 redeploy 隨附「Defense in Depth」新安全分類器（高風險 coding 請求 fallback 至 Opus 4.8，首日已有誤判負面實測）、Claude Code 中國代理偵測爭議升級為「embedded spyware」指控（版本號 2.1.91、混淆手法、system prompt 隱藏機制，社群單方指控待查證）、Sonnet 5 官方對比圖表修改爭議、Anthropic-Samsung 客製晶片洽談（初步報導）、Palantir CEO Karp 批評 Anthropic/OpenAI「竊取客戶 IP」
- 更新頁面：
  - `wiki/entities/fable-5.md`：Defense in Depth 機制、化學問答/資安審查誤判實測
  - `wiki/entities/sonnet-5.md`：對比圖表爭議、Sonnet 4.6→5 個性流失社群回饋
  - `wiki/entities/pricing.md`：Max 方案升級誤扣費/客服退款爭議案例
  - `wiki/topics/ai-agent-safety.md`：中國代理偵測爭議升級（技術細節補充，維持「待查證」標註）
  - `wiki/topics/anthropic-government-policy.md`：Fable 5 Defense in Depth 作為出口管制解除後承諾首次具體落實
  - `wiki/topics/anthropic-business.md`：Anthropic-Samsung 晶片洽談、Blackstone 基金報導（皆標「初步報導，細節待補」）、Palantir Karp 批評事件
  - `wiki/topics/competitor-landscape.md`：Palantir Karp 批評 + 分析師調升評等
  - `wiki/topics/community-tech-discussions.md`：新增 VS Code 使用率下降、AskUserQuestion 60 秒逾時、390M tokens 紀錄、thinking 停頓分心、Anthropic testing on live product 等 5 條中熱度討論
  - `wiki/topics/community-tech-patterns.md`：新增氛圍狀態燈（hooks 驅動實體 LED）模式
- feature-radar 新增：無（今日無 official 條目，Fable 5/Sonnet 5 既有熱度已達上限，本週推薦未變）
- index.md 狀態變更：無（近期異動區塊已更新）
- 新增頁面：無
- 呈現品質審查：所有更新頁面記者回報均 ✅ 通過
- 備註：社群記者 agent 在完成 community-tech-discussions.md / community-tech-patterns.md 實際編輯後，兩次收尾回覆退化為觀察性文字而非標準回報格式，經主編兩次 SendMessage 催促後確認编輯已完整落地（git diff 驗證），內容品質正常

## 2026-06-28 Ingest | news/2026-06-28.md（48 則）

- 來源日報：`news/2026-06-28.md`（48 則，6/6 來源；Reddit 429 rate limit 部分失敗；全部為 community 類別，無 official 條目）
- 核心事件：Mozilla 0din 揭露 Claude Code 提示注入漏洞、Mythos 5 擴大解禁（100+ 機構）、Alibaba 竊取指控 Fortune IPO 分析、Legion LegalTech 起訴、奧地利遊說 EU、中國競品（Tulongfeng/Fugu）追趕
- 更新頁面：
  - `wiki/topics/ai-agent-safety.md`：Mozilla 0din 提示注入攻擊（乾淨 GitHub Repo 向量）
  - `wiki/topics/anthropic-government-policy.md`：Mythos 5 擴大解禁、Fable 5 接近回歸（待核實）、Legion LegalTech 起訴、奧地利遊說歐盟；攻防紀錄 +4 條
  - `wiki/topics/anthropic-business.md`：Fortune IPO 護城河疑問、Motley Fool 估值分析、奧地利談判槓桿
  - `wiki/topics/competitor-landscape.md`：中國 360 Tulongfeng、Sakana AI Fugu、WSJ 中國追平網路安全 AI
  - `wiki/entities/mythos.md`：競品聲明（Tulongfeng/Fugu 待核實）、Lutnick 批准最新細節
  - `wiki/entities/fable-5.md`：Axios/TechCrunch 2026-06-28 全面回歸接近報導（待核實）
  - `wiki/entities/boris-cherny.md`：13 個日常使用技巧（howborisusesclaudecode.com）
  - `wiki/topics/community-tech-discussions.md`：新增 Adrafinil（HN 113）、Boris Cherny 工作流、OAuth 401 陷阱；清理 5 條過期 ☄️閃現
  - `wiki/topics/community-tech-patterns.md`：新增 OKF 跨 session 記憶、stop hook 音效、ccgram v4.3.0、Adrafinil 保活模式 4 條新模式
- feature-radar 新增：無（今日無 official 條目）
- index.md 狀態變更：無
- 新增頁面：無
- 呈現品質審查：所有更新頁面均 ✅ 通過（記者回報確認）

## 2026-06-27 Lint 後續 | 使用者決策執行

承上次 Lint 待確認項，使用者拍板後執行：
- **超長頁面**：
  - ai-agent-safety（502→433 行）：將 2026-05-22 前 16 條時序歸檔至新頁 `topics/ai-agent-safety-archive.md`，主頁加指向提示。✅ 達標
  - community-tech-discussions（877）/ community-tech-patterns（806）：經查技術彙整條目**全部在 60 天內**（最舊 2026-05-01，57 天），依既有規則無逾期條目可歸檔——長度源於近期高密度討論，非舊 log 堆積。**維持不動**，最早 2026-07-02 起條目陸續跨 60 天門檻可自然歸檔。
- **community-tech-tools 精選層**：補建「## 值得關注的工具」中間層（13–15 個達標工具按類型分組），三層動線恢復。
- **過期 ⏳ 汰除**：批次刪除 41 筆 > 30 天無後續的 ⏳ 工具列（git history 留存），同步痛點洞察 3 列。
- 新增頁面：`topics/ai-agent-safety-archive.md`（index.md 已補列）
- 待辦（未執行，留紀錄）：6e wiki-ingest-features.md 121>100 行可簡化；6d entities/ 格式模板規則 [加入: 2026-04-25] >60 天（經這次 6 記者實際套用驗證仍吻合現狀，暫無需修訂）

## 2026-06-27 Lint

- 修正矛盾：
  - Microsoft 退出日期：enterprise-cost-management「6/30 完全停用」vs enterprise-tool-tracker「6/21 加速退出」→ 統一為「原訂 6/30，6/21 加速退出」並補來源 + wikilink
  - 「Claude Code 讓工程師更孤獨」歸屬：boris-cherny / cat-wu 標「engineering leader（待核實）」→ 由 fiona-fung 具名來源（Business Insider）確認為 Fiona Fung，三頁互鏈、解除待核實
  - enterprise-tool-tracker 摘要企業計數 16 → 23（與表格實際筆數一致）
- 補連結（去孤立）：
  - ai-talent-flow（新頁）← competitor-landscape、anthropic-business 補雙向
  - fiona-fung ← boris-cherny、cat-wu
  - tom-brown / chris-ciauri / dario-amodei ← anthropic-government-policy「相關實體」
  - opus-4-7 / opus-4-8 → fable-5 補反向 wikilink
- 狀態更新：boris-cherny、cat-wu 解除待核實；andrej-karpathy、chris-ciauri 維持待核實（無新具名來源）
- 遷移至 entities：無
- 新增 entities：無（無被提及 3 次以上且無專頁者）
- 呈現品質：bugcrawl、code-quality-decline 摘要改 delta-first；andrej-karpathy/chris-olah/chris-ciauri 補「最後新聞更新」欄；其餘全部通過
- 工具策展（community-tech-tools）：新增 3（cc-pool、Janus、TaskPrio，皆 ⏳）／汰除 0／提拔 0
- 超長頁面（> 500 行）：📋 待使用者確認 — ai-agent-safety（502）、community-tech-patterns（806）、community-tech-discussions（877）
- 規則檔健檢：
  - wiki/CLAUDE.md：50 行（閾值 80）✅
  - .claude/rules/wiki-ingest.md：68 行（閾值 80）✅
  - .claude/rules/wiki-ingest-format.md：127 行（閾值 200）✅
  - 各記者規則檔：models 50 / features 121 ⚠️ / commercial 77 / safety-policy 53 / community 83 / community-lint 42 / people 41（閾值 100）
  - 矛盾（6a）：無
  - 引用驗證（6b）：7/7 錨點全部通過
  - 遵守率（6c）：近 3 次 ingest 品質審查 3/3、feature-radar 3/3 ✅
  - 過期規則（6d）：1 條 > 60 天 — entities/ 頁面格式模板 [加入: 2026-04-25]（63 天，待確認是否仍吻合現狀）
  - 簡化（6e）：wiki-ingest-features.md 121 > 100 ⚠️（待確認是否簡化）
  - 📋 規則 vs 現實落差：community-tech-tools 缺「## 值得關注的工具」精選層（lint 規則要求三層，頁面僅二層）；42 筆 > 30 天 ⏳ 列汰除政策待確認
- overview.md：已更新（當前局勢改為 Mythos 5 部分解禁 / Fable 接近協議；模型現況表同步）
- 待確認決策已彙整回報主 session，未自行執行拆分 / 規則修改

## 2026-06-27 Ingest | news/2026-06-27.md（55 則）

- 來源日報：`news/2026-06-27.md`（55 則，6/6 來源；Reddit 429 rate limit 多數，仍有 10 筆）
- 核心事件：Mythos 5 部分解禁（100+ 美國受信任機構）、Fable 5 接近協議（待核實）、Alibaba 2900 萬假查詢指控
- 更新頁面：
  - `wiki/entities/mythos.md`：部分解禁（Lutnick 致 Tom Brown 信確認，100+ 美國機構可用）
  - `wiki/entities/fable-5.md`：接近協議（待核實），來源 Reuters/Axios
  - `wiki/entities/claude-code.md`：v2.1.195（CLAUDE_CODE_DISABLE_MOUSE_CLICKS + hook matcher 修復）
  - `wiki/topics/anthropic-government-policy.md`：Mythos 5 解禁、Fable 5 接近協議；攻防紀錄、三個戰場、時序更新
  - `wiki/topics/ai-agent-safety.md`：Agentjacking 攻擊（偽造 Sentry 錯誤劫持 Claude Code/Cursor/Cline）
  - `wiki/topics/anthropic-business.md`：Mythos 5 解禁商業面、消費者付費成長（Indagari）、Alibaba 2900 萬次補強、Anthropic/OpenAI 選舉代理戰（$27M）
  - `wiki/topics/enterprise-cost-management.md`：企業縮減 AI 支出（ROI 不明確）、小型蒸餾模型替代趨勢
  - `wiki/topics/competitor-landscape.md`：Zhipu Z.AI 快速追趕、選舉代理戰雙輸
  - `wiki/topics/community-tech-patterns.md`：6 條新技術彙整（Workweave Router 智能路由、Git Lazy Mount、Mac Mini 自主 agent、Verity 自愈閘門、TBD 多工管理器、Android Remote Control MCP 新版）
  - `wiki/topics/community-tech-discussions.md`：AI 概念長期性討論（MCP/Skills/Agentic workflows）、quota 自動化 gap；清理過期 ☄️閃現 條目
  - `wiki/feature-radar.md`：新增 CLAUDE_CODE_DISABLE_MOUSE_CLICKS 條目（🔥🔥 / ⚡）
  - `wiki/index.md`：近期異動 + mythos 狀態更新
- feature-radar 新增：CLAUDE_CODE_DISABLE_MOUSE_CLICKS 環境變數（v2.1.195）
- 新增頁面：無
- 呈現品質審查：✅ 全部通過（11 頁）

## 2026-06-26 設計決策 | 記者差異化 + 單一 push 部署修正

兩項本週架構改動（commit `490275b`、`97f8cf2`，皆已過 `/review-commands`）：

**1. Pages 部署改為單一 push（根因修正）**
- 問題：pipeline 在 Step 1b/3/5 各 push 一次，每次觸發一個 GitHub Pages 部署；6/24 三次 push 相隔過近，部署互相搶佔（concurrency race），最後含 web 資料的關鍵部署失敗，線上停留舊版而 pipeline 無從得知（只確認 git push、不確認部署）。
- 修正：`news-pipeline-steps.md` 改為中途只 commit、Step 5 一次 push 全部 commit；一次 push 只觸發一個部署，從源頭消除 race。
- 驗證：6/24（空 commit 補救）→ 6/25 → 6/26 連續三天穩定，6/26 約 2 分鐘上線。診斷方法見 memory `pages-deploy-diagnosis`。

**2. 六記者差異化（核心提問 + 分析視角 + 書寫風格）**
- 問題：六個 `.claude/agents/wiki-reporter-*.md` 的「類別特有規則」幾乎全空，記者只差在負責頁面與表格格式，分析視角與語氣無差異化。
- 做法：各記者先自我盤點負責頁面，再由自述提煉「核心提問/分析視角/書寫風格」寫入各自 system prompt。
- 連帶修正：pricing.md 改商業記者單一主責（原模型/商業雙頭）；ai-talent-flow 補商業更新規則專段；社群 agent 描述移除誤含的 official-community-gap。
- 驗證：6/26 首跑，商業記者在 ai-talent-flow 自動補上「市值蒸發 $2,700 億（推論）」「Gemini 3.5 延期」等量化商業分析。

## 2026-06-25 Manual | 新建 topics/ai-talent-flow.md

- 觸發：使用者要求整理「AI 人才流動對各公司的影響」（跨公司視角，非 Anthropic 單一中心）
- 新增頁面：`wiki/topics/ai-talent-flow.md`（狀態 ongoing，領域 💼 商業）
- 資料來源：news/2026-06-19 ~ 06-25 既有日報（Jumper、Adler、Pritzel、Google→OpenAI、FT 經濟學家）
- 核心區塊：「對各公司的影響」三家對照表（Google DeepMind 淨流失 / Anthropic 主要承接 / OpenAI 次要承接）
- 同步：index.md 新增 topic 列 + 近期異動；推論均標注「（推論）」

## 2026-06-25 Ingest | news/2026-06-25.md（74 則）

- 來源日報：`news/2026-06-25.md`（74 則，6/6 來源；Reddit 429 rate limit 部分條目，仍有 15 筆）
- 更新頁面：
  - `wiki/entities/claude-code.md`：v2.1.191（/rewind 指令 + streaming 捲軸修正）
  - `wiki/entities/opus-4-8.md`：第三方評測 vs Gemini 3.5 Flash（35.4 對 34.8，略輸）
  - `wiki/entities/opus-4-7.md`：使用者實測 4.7 比 4.6 消耗更多 token
  - `wiki/entities/dario-amodei.md`：退出 Fable 5 白宮談判，由 Tom Brown 接管
  - `wiki/entities/tom-brown.md`：新建（聯合創辦人，接管 Fable 5 談判，待核實）
  - `wiki/topics/anthropic-government-policy.md`：Tom Brown 接管、EU 介入白宮對話、LessWrong 預測修正至 7/9
  - `wiki/topics/anthropic-business.md`：阿里巴巴蒸餾攻擊指控（28.8M/25K 假帳號）、Google 研究員加入、Notion 整合、Intercept 公益合作、全球數據中心計畫、爭議性經濟學家聘雇
  - `wiki/topics/competitor-landscape.md`：阿里巴巴蒸餾攻擊、Google 重組 AI 編碼部隊、Alphabet 股價
  - `wiki/topics/enterprise-tool-tracker.md`：Notion 整合 Claude Agents 與 Cursor
  - `wiki/topics/community-tech-patterns.md`：6 個新工作流模式（Hook 任務守門、repo convention 注入、adversarial reviewer、multi-model pipeline、Claude Code 商業自動化、開發前問清楚）
  - `wiki/topics/community-tech-discussions.md`：3 個新熱門討論（阿里巴巴蒸餾倫理、工程師孤獨感、HTML vs Markdown）；移除過期 🌸落幕條目
  - `wiki/feature-radar.md`：新增 /rewind 指令（🔥🔥🔥 / ⚡）、SDK client.system.message（🔥🔥 / ⚡）
  - `wiki/index.md`：新增 tom-brown.md；近期異動更新
- feature-radar 新增：/rewind 指令（Claude Code v2.1.191）、SDK client.system.message（TS v0.106.0 / Python v0.112.0）
- 新增頁面：`wiki/entities/tom-brown.md`
- 呈現品質審查：✅ 全部通過（12 頁）；community-tech-discussions.md ⚠️ 已修復（移除過期條目）

## 2026-06-24 Ingest | news/2026-06-24.md（66 則）

- 來源日報：`news/2026-06-24.md`（66 則，6/6 來源全數正常）
- 更新頁面：
  - `wiki/entities/fable-5.md`：NSA 失去存取、Legion 提告、LessWrong 7/9 預測
  - `wiki/entities/mythos.md`：AP News 情報機構合作測試確認 + 360 對標聲明
  - `wiki/entities/opus-4-8.md`：跨 API/Claude Code/Console 高錯誤率事件
  - `wiki/entities/claude-code.md`：v2.1.187（sandbox.credentials + 組織模型限制）
  - `wiki/entities/claude-tag.md`：新建（Slack-native AI 協作工具）
  - `wiki/topics/anthropic-business.md`：NSA/Legion 事件、白宮緊張、Railway 沙盒整合
  - `wiki/topics/competitor-landscape.md`：Reid Hoffman 批評 xAI、360 對標 Mythos
  - `wiki/entities/pricing.md`：隱私政策更新（7/8 生效）、加州帳號歐元盜刷
  - `wiki/topics/anthropic-government-policy.md`：NSA 失去存取、Legion 提告、白宮關係緊張、360 競品、LessWrong 預測
  - `wiki/topics/ai-agent-safety.md`：Mythos 情報機構測試發現漏洞
  - `wiki/topics/community-tech-discussions.md`：Boris Cherny 立場轉變、多工具 HN 討論、過期條目清理
  - `wiki/topics/community-tech-patterns.md`：multi-agent 工作流指南、Lean 4 vibe coding 限制
  - `wiki/entities/boris-cherny.md`：承認 AI 100% 程式碼有問題（立場轉變）
  - `wiki/entities/dario-amodei.md`：白宮關係緊張（WIRED）
  - `wiki/feature-radar.md`：新增 Claude Tag、v2.1.187 條目；最後更新 2026-06-24
  - `wiki/index.md`：新增 claude-tag.md；近期異動更新
  - `wiki/overview.md`：當前局勢、模型現況、進行中議題、重大事件表更新
- feature-radar 新增：Claude Tag（🔥🔥🔥 / ⚡）、Claude Code v2.1.187 sandbox.credentials（🔥🔥🔥 / ⚡）
- 新增頁面：`wiki/entities/claude-tag.md`
- 呈現品質審查：✅ 全部通過（14 頁）

## 2026-05-22 Ingest | news/2026-05-22.md（2 則，fallback 補錄）

- 來源日報：`news/2026-05-22.md`（2 則，fallback 純文字；RSS 對過去日期抓取量少）
- 更新頁面：
  - `wiki/topics/competitor-landscape.md`：新增 2026-05-22 The Verge 報導（HN 493 分，Microsoft 取消授權最高曝光節點）
  - `wiki/topics/community-tech-discussions.md`：新增 Spec-Driven Development 技術彙整條目（HN 20 分，補錄至 ## 技術彙整）
- 呈現品質：`competitor-landscape.md` ✅ 通過 | `community-tech-discussions.md` ✅ 通過
- 備注：analyzer 無 ANTHROPIC_API_KEY，日報為純文字 fallback；wiki ingest 依 HN 分數手動判斷重要性

---

## 2026-06-23 Ingest | news/2026-06-23.md（65 則）第二次執行

- 來源日報：`news/2026-06-23.md`（65 則，6/6 來源正常；Reddit 部分 429 但仍有 10 筆）
- 主軸：Fable/Mythos 出口管制持續（Five Eyes 聯合聲明、NSA 紅隊測試 Sen. Warner 確認、Zhipu GLM-5.2 趁機接觸被封鎖用戶、歐洲高管警告）；Micron × Anthropic 多年戰略協議正式確認（記憶體/儲存/AI 架構，Micron 股價創歷史新高）；Menlo Ventures $3B 史上最大募資；Claude Code v2.1.186 新增 `mcp login/logout` CLI 指令（headless 認證）；Extended Thinking 透明度爭議（HN 312，加密簽名而非實際推理）；帳號封禁政策不透明（HN 55）；AgentJacking Sentry MCP 攻擊向量（Tenet Security）；Anthropic 計畫 7 月起要求身份識別/臉部掃描；John Jumper 多媒體確認（Barron's / SEJ）；Boris Cherny ROI vs 實驗論述；社群：Claude Code 使用現況分析（2,500 repos）、AI agent O(N²) 記憶體問題、cc-fleet/Aharness 新工具
- 更新頁面：
  - `entities/fable-5.md`：Five Eyes 聲明、Zhipu 市場動作、Fortune 歐洲警告、HN Fable 回歸弱訊號
  - `entities/mythos.md`：NSA 紅隊測試 Tom's Hardware 報導；MIT Tech Review 三爭點；補充「最後新聞更新」欄位
  - `entities/claude-code.md`：v2.1.186 版本表新增；mcp login/logout 歷史記錄
  - `topics/anthropic-government-policy.md`：身份驗證/臉部掃描政策；帳號封禁 HN 討論；目前局勢更新
  - `topics/ai-agent-safety.md`：AgentJacking Sentry MCP 條目升級（Tenet Security 亮相，Codex 列入）
  - `topics/anthropic-business.md`：Micron 協議補充（投資確認、三層涵蓋）；Menlo Ventures $3B；時序 prepend
  - `topics/enterprise-cost-management.md`：企業帳單優化趨勢（節省超 50%）；時序 prepend
  - `topics/community-tech-discussions.md`：Extended Thinking 透明度（HN 312，升為 🌊延燒）；帳號封禁（HN 55，新增）；移除過期 🌸落幕 條目
  - `topics/community-tech-patterns.md`：cc-fleet、Aharness、Compact Memory 三個新工作流模式
  - `entities/john-jumper.md`：Barron's / SEJ 跟進確認；Google 股價影響背景
  - `entities/boris-cherny.md`：ROI vs 實驗平衡論述（Business Insider）；歷史記錄 prepend
- 新增頁面：無
- feature-radar 更新：新增「MCP CLI 認證指令」條目；本週推薦更新（/goal、Artifacts、破壞性 Git 封鎖）
- index.md 狀態變更：無（無新頁面）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | fable-5.md | ✅ 通過 |
  | mythos.md | ⚠️ 已修復（補充缺少的「最後新聞更新」欄位） |
  | claude-code.md | ✅ 通過 |
  | anthropic-government-policy.md | ✅ 通過 |
  | ai-agent-safety.md | ✅ 通過 |
  | anthropic-business.md | ✅ 通過 |
  | enterprise-cost-management.md | ✅ 通過 |
  | community-tech-discussions.md | ✅ 通過 |
  | community-tech-patterns.md | ✅ 通過 |
  | john-jumper.md | ✅ 通過 |
  | boris-cherny.md | ✅ 通過 |

## 2026-06-23 Ingest | news/2026-06-23.md（67 則）

- 來源日報：`news/2026-06-23.md`（67 則，6/6 來源正常；Reddit 部分 429 但仍有 10 筆）
- 主軸：Anthropic 政府政策風暴持續（Trump 宣布 Anthropic 不再是安全威脅、FT 量化分析 Dario 風險表態密度 5/千字助攻出口禁令、Amazon CEO 舉報動機揭露、Mythos 入侵 NSA 機密系統報導）；Claude API 529 Overloaded 第二波（Opus 4.8/4.7/4.6、Sonnet 4.6 均受影響）；Extended Thinking 揭密（HN 98，thinking blocks 為摘要非真實推理）；Micron × Anthropic 後續及 Charleston Hospitality 加入；John Jumper 多媒體跟進確認；新人物 Fiona Fung（工程副總裁，「工程師孤獨感」論述）；社群工具：open model vs Claude 辯論持續延燒（HN 334）、Recall（HN 124）；hooks 取代 CLAUDE.md 規則最佳實踐
- 更新頁面：
  - `topics/anthropic-government-policy.md`：攻防紀錄 prepend 4 條（Ars Technica FT 量化數據、Gizmodo Amazon 動機、Security Affairs Mythos NSA、TechNewsWorld 法律框架）；目前局勢更新至 2026-06-23；時序 prepend 2026-06-23；最後新聞更新 2026-06-23
  - `topics/ai-agent-safety.md`：技術彙整新增「Mythos 入侵 NSA 機密系統」；時序 prepend 2026-06-23；最後新聞更新 2026-06-23
  - `topics/anthropic-business.md`：戰略合作表格及時序 prepend 6/23 條目（Charleston Hospitality、8x 產能論述、IPO 訊號）；最後新聞更新 2026-06-23
  - `topics/enterprise-tool-tracker.md`：企業表 prepend Charleston Hospitality Group；時序 prepend 2026-06-23；最後新聞更新 2026-06-23
  - `entities/claude-code.md`：529 過載第二波、Extended Thinking 摘要性質揭露、年齡驗證開發者須知；最後新聞更新 2026-06-23
  - `entities/opus-4-8.md`：529 elevated error rates；Quake 程序生成應用案例；最後新聞更新 2026-06-23
  - `entities/opus-4-7.md`：529 elevated error rates；最後新聞更新 2026-06-23
  - `entities/fable-5.md`：三詞越獄機制公開；Zhipu 聲稱 2026 追上；最後新聞更新 2026-06-23
  - `entities/john-jumper.md`：多媒體跟進確認（Barron's/IBD/The Rundown AI）；最後新聞更新 2026-06-23
  - `entities/dario-amodei.md`：FT 量化風險表態密度（5/千字）成政治焦點；最後新聞更新 2026-06-23
  - `topics/community-tech-discussions.md`：新增 3 條熱門討論（529 可靠性、Extended Thinking 揭露、Hooks 模式）；3 條技術彙整 prepend；移除 4 條過期 ☄️閃現；「切換開源模型」升格 🌊延燒；最後新聞更新 2026-06-23
  - `topics/community-tech-patterns.md`：3 條新模式 prepend（MCP as API contract、Hooks enforcement、ISO 29148）；最後新聞更新 2026-06-23
- 新增頁面：`wiki/entities/fiona-fung.md`（Anthropic 工程副總裁）
- feature-radar 更新：無（本輪無新官方功能；本週推薦維持不動）
- index.md 狀態變更：新增 `[[entities/fiona-fung]]`
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | anthropic-government-policy.md | ✅ 通過 |
  | ai-agent-safety.md | ✅ 通過 |
  | anthropic-business.md | ✅ 通過 |
  | enterprise-tool-tracker.md | ✅ 通過 |
  | claude-code.md | ✅ 通過 |
  | opus-4-8.md | ✅ 通過 |
  | opus-4-7.md | ✅ 通過 |
  | fable-5.md | ✅ 通過 |
  | john-jumper.md | ✅ 通過 |
  | dario-amodei.md | ✅ 通過 |
  | community-tech-discussions.md | ✅ 通過 |
  | community-tech-patterns.md | ✅ 通過 |
  | fiona-fung.md（新頁）| ✅ 通過 |

## 2026-06-22 Ingest | news/2026-06-22.md（58 則）

- 來源日報：`news/2026-06-22.md`（58 則，6/6 來源正常；Reddit 部分 429 但仍有 10 筆）
- 主軸：Trump 正式宣布 Anthropic 不再是國安威脅（封鎖第 10 天、Fable 5 解封條件趨近）；Fable 5 三詞越獄曝光（「Fix this code」，引發安全邊界設計質疑）；Micron × Anthropic 戰略合作（下一代 AI 記憶體基礎設施，Micron 股價 +5.5%）；Anthropic 揭露封鎖中國損失數億美元；Five Eyes 罕見聯合聲明警告數月內 AI 可癱瘓政府與企業；Claude API 529 全球中斷（90 分鐘，已恢復）；Anthropic 引入 Persona 年齡驗證；Google Nobel AI 專家（John Jumper 後續跟進報導）；「Claude Code 讓工程師更孤獨」論述（待核實發言人）；HN 熱門工具：Recall（score 123）、切換開源 LLM 論（score 309）
- 更新頁面：
  - `topics/anthropic-government-policy.md`：攻防紀錄 prepend 4 條（Trump 國安威脅標籤解除、Fable 5 三詞越獄、Five Eyes 聲明、Persona 年齡驗證）；目前局勢更新至封鎖第 10 天；時序 prepend 2026-06-22；最後新聞更新 2026-06-22
  - `topics/ai-agent-safety.md`：Fable 5 三詞越獄插入安全漏洞分類；Persona 年齡驗證插入政策合規分類；最後新聞更新 2026-06-22
  - `topics/recursive-self-improvement.md`：補充 Five Eyes 聲明；目前結論更新；時序 prepend 2026-06-22；最後新聞更新 2026-06-22
  - `topics/anthropic-business.md`：戰略合作表格 prepend Micron 合作；時序 prepend 2026-06-22（含 Micron 合作、中國封鎖財務揭露、Microsoft 後續確認）；最後新聞更新 2026-06-22
  - `topics/enterprise-tool-tracker.md`：Microsoft 縮減中後續確認；時序 prepend 2026-06-22；最後新聞更新 2026-06-22
  - `entities/claude-code.md`：已知問題 prepend 529 過載事件（2026-06-21 確認）；最後新聞更新 2026-06-22
  - `topics/community-tech-discussions.md`：熱門討論表格 prepend 2 條（切換開源 LLM 論 HN 309、Recall 本地記憶 HN 123）；技術彙整 prepend 2 條；移除 2 條過期 ☄️閃現（首見 2026-06-01，> 21 天）；最後新聞更新 2026-06-22
  - `topics/community-tech-patterns.md`：技術彙整 prepend ANMA 架構邊界合約、Staff Engineer 工作流 Skill 化；最後新聞更新 2026-06-22
  - `entities/boris-cherny.md`：公開言論補充「讓工程師更孤獨」論述（待核實）；最後新聞更新 2026-06-22
  - `entities/cat-wu.md`：公開言論補充「讓工程師更孤獨」論述（待核實）；補充最後新聞更新欄位；最後新聞更新 2026-06-22
  - `entities/john-jumper.md`：補充 2026-06-22 後續報導跟進（PYMNTS.com 等媒體確認）；最後新聞更新 2026-06-22
- 新增頁面：無
- feature-radar 更新：無（本輪無新官方功能；529 中斷為 reliability，不進 feature-radar）
- index.md 狀態變更：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | anthropic-government-policy.md | ✅ 通過 |
  | ai-agent-safety.md | ✅ 通過 |
  | recursive-self-improvement.md | ⚠️ 已修復（移除過期警告標記，補充今日新聞，目前結論改條列格式） |
  | anthropic-business.md | ✅ 通過 |
  | enterprise-tool-tracker.md | ✅ 通過 |
  | claude-code.md | ✅ 通過 |
  | community-tech-discussions.md | ✅ 通過 |
  | community-tech-patterns.md | ✅ 通過 |
  | boris-cherny.md | ✅ 通過 |
  | cat-wu.md | ✅ 通過（補充最後新聞更新欄位） |
  | john-jumper.md | ✅ 通過 |

## 2026-06-21 Ingest | news/2026-06-21.md（54 則）

- 來源日報：`news/2026-06-21.md`（54 則，5/6 來源正常；Reddit 部分 429 但仍有 10 筆）
- 主軸：Trump G7 後不再視 Anthropic 為國安威脅（暗示鬆綁 Fable 5 / Mythos）；David Sacks 揭露 Mythos 越獄漏洞為白宮信任缺口根因；FT 分析 Anthropic 安全倡導話術反效果；John Jumper 加入 Anthropic（Reuters 正式確認）；Microsoft 宣布逐步停止內部工程師使用 Claude Code；Claude Code v2.1.185 stream-stall 改善；Project Fetch Phase Two（機器狗實驗）；多款社群工具亮相（Forq / Pulse / Maccha / cc-fleet）
- 更新頁面：
  - `topics/anthropic-government-policy.md`：攻防紀錄 prepend 3 條（Trump 鬆口、Sacks 信任缺口、FT 分析）；目前局勢更新至 2026-06-21 封鎖第 9 天；時序 prepend 2026-06-21 區塊；最後新聞更新 2026-06-21
  - `topics/enterprise-tool-tracker.md`：Microsoft 狀態更新為 ⚠️ 縮減中（Fable 5 封鎖期間逐步退出）；競爭態勢表更新；時序 prepend 2026-06-21；最後新聞更新 2026-06-21
  - `topics/anthropic-business.md`：時序 prepend 2026-06-21（Microsoft 加速退出、Fable 5 Bedrock 資料共享阻力）；最後新聞更新 2026-06-21
  - `entities/pricing.md`：Fable 5 Bedrock provider data sharing 細節補入；最後新聞更新 2026-06-21
  - `entities/john-jumper.md`：狀態從 active（待核實）改為 active（Reuters 確認）；歷史記錄 prepend 2026-06-21 Reuters 確認條目；最後新聞更新 2026-06-21
  - `entities/dario-amodei.md`：歷史記錄 prepend 2026-06-21 Times of India 採訪條目；最後新聞更新 2026-06-21
  - `entities/claude-code.md`：版本表 + 版本歷史新增 v2.1.185（stream-stall 改善）；最後新聞更新 2026-06-21
  - `topics/community-tech-patterns.md`：技術彙整 prepend 3 條（平行 Agent 模式、Agent Loop 事件驅動、MCP Server 信任邊界審查）；最後新聞更新 2026-06-21
  - `topics/community-tech-discussions.md`：熱門討論表格 prepend 3 條（Claude Code 確定性、平行 agent 效能、工具選擇比較）；技術彙整 prepend Project Fetch Phase Two；移除 3 條過期 ☄️閃現（> 21 天）；最後新聞更新 2026-06-21
- 新增頁面：無
- feature-radar 更新：無（v2.1.185 屬 reliability，七種指令方法屬說明文件，均不進 feature-radar）
- index.md 狀態變更：john-jumper: active（待核實）→ active
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | anthropic-government-policy.md | ⚠️ 已修復（摘要末句過期，已改寫為反映最新 2026-06-21 狀態） |
  | enterprise-tool-tracker.md | ✅ 通過 |
  | anthropic-business.md | ✅ 通過 |
  | pricing.md | ✅ 通過 |
  | john-jumper.md | ✅ 通過 |
  | dario-amodei.md | ✅ 通過 |
  | claude-code.md | ⚠️ 已修復（補入最後新聞更新欄位） |
  | community-tech-patterns.md | ✅ 通過 |
  | community-tech-discussions.md | ✅ 通過 |

## 2026-06-20 Ingest（補跑）| news/2026-06-20.md（23 則）

- 來源日報：`news/2026-06-20.md`（23 則，5 來源；主軸：中國 AI Z.ai 創辦人聲稱追上 Fable 5 等級模型比 Q1 更早（HN score 10）；Politico 深度報導 Anthropic 出口管制政治處境；Claude Code 根目錄掃描 SSH 私鑰隱私爭議（HN）；Fable 5 在 AWS Bedrock 需分享推論資料（InfoQ）；AlphaFold 共同創造者 John Jumper 加入 Anthropic 社群分析文；Claude Design 工作流整合討論；Token 節省實戰（82% 降低、工具鏈是真正殺手）；CLAUDE.md 規則上限策略）
- 更新頁面：
  - `topics/anthropic-government-policy.md`：攻防紀錄新增 Politico 政治處境報導；時序 2026-06-20 補入；最後新聞更新 2026-06-20
  - `topics/ai-agent-safety.md`：技術彙整新增 Claude Code 根目錄掃描暴露 SSH 私鑰、Bedrock Fable 5 推論資料共享；時序 2026-06-20 補入；最後新聞更新 2026-06-20
  - `entities/john-jumper.md`：更新現況措辭（「傳出」取代「宣布」）；歷史記錄補入 dev.to 社群分析文；狀態維持 active（待核實）；最後新聞更新 2026-06-20
  - `topics/community-tech-discussions.md`：熱門討論表格新增 5 條（Claude Design handoff、Markdown KB ingest、工具鏈 Token 殺手、CLAUDE.md 規則上限、terminal-first 設計哲學）；技術彙整 prepend 2 條；最後新聞更新 2026-06-20
  - `topics/community-tech-patterns.md`：技術彙整 prepend CLAUDE.md 規則上限模式；最後新聞更新 2026-06-20
- 新增頁面：無
- feature-radar 更新：無（本輪無新官方功能）
- index.md 狀態變更：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | anthropic-government-policy.md | ✅ 通過 |
  | ai-agent-safety.md | 📋 已記錄待辦（頁面 420+ 行超警戒線，建議 /wiki-lint 時重構時序） |
  | john-jumper.md | ✅ 通過 |
  | community-tech-discussions.md | ✅ 通過 |
  | community-tech-patterns.md | ✅ 通過 |

## 2026-06-20 Ingest | news/2026-06-20.md（72 則）

- 來源日報：`news/2026-06-20.md`（72 則，6 來源；主軸：Fable 5 / Mythos 出口管制持續（Ciauri 首爾記者會「數日內恢復」、白宮轉向制定 AI 安全規則、各國媒體跟進、境外付費用戶帳號停用）；OALABS 揭露攻擊者使用 Claude + Codex 入侵 14 家企業；JPMorgan 封鎖香港員工 Anthropic 存取；Claude Code Artifacts 正式發布（三家媒體跟進，feature-radar 升至 🔥🔥🔥🔥🔥）；MCP Enterprise Authorization 正式版（stable，Okta/VS Code SSO）；John Jumper 諾貝爾獎得主加入 Anthropic（待核實）；Boris Cherny Loop Engineering 哲學文章；context rot 修復五法；多 agent 協調困境社群討論）
- 更新頁面：
  - `entities/claude-code.md`：版本表新增 MCP Enterprise Authorization 條目
  - `entities/fable-5.md`：歷史記錄 prepend 2026-06-20（多國媒體跟進、境外帳號停用事件）
  - `entities/mythos.md`：時序 prepend 2026-06-20（國際媒體報導、Mythos 側影響）
  - `entities/boris-cherny.md`：歷史記錄 prepend 2026-06-20；核心論述新增 Loop Engineering 哲學引用
  - `topics/anthropic-government-policy.md`：時序 prepend 2026-06-20（各國媒體 Kill-Switch 敘事、境外帳號停用）
  - `topics/ai-agent-safety.md`：技術彙整 prepend OALABS Claude + Codex 入侵 14 家企業；時序 prepend 2026-06-20
  - `topics/enterprise-tool-tracker.md`：時序 prepend 2026-06-20（JPMorgan 香港跟進報導）
  - `topics/enterprise-cost-management.md`：時序 prepend 2026-06-20（成本轉折分析、90% 削減策略）
  - `topics/anthropic-business.md`：時序 prepend 2026-06-20（JPMorgan 跟進、成本轉折、IPO 傳聞標注）
  - `topics/community-tech-discussions.md`：熱門討論表格新增 3 條（Loop Engineering、Context Rot 修復、MCP tool search）；技術彙整 prepend Context Rot 修復五法
  - `topics/community-tech-patterns.md`：技術彙整 prepend Context 裁剪 Tool Output 策略；補充 Loop Engineering 模式
  - `topics/code-quality-decline.md`：技術彙整 prepend LLM 無障礙偏差 issue #56079；時序 prepend 2026-06-18
  - `wiki/feature-radar.md`：全覽表新增 MCP Enterprise Authorization；Claude Code Artifacts 熱度升至 🔥🔥🔥🔥🔥；v2.1.183 熱度升至 🔥🔥🔥
  - `wiki/index.md`：新增 john-jumper 頁面條目
- 新增頁面：`wiki/entities/john-jumper.md`（諾貝爾化學獎得主，加入 Anthropic 待核實）
- feature-radar 更新：新增 MCP Enterprise Authorization（🔥🔥，⚡）；Artifacts 🔥🔥🔥🔥 → 🔥🔥🔥🔥🔥；v2.1.183 🔥🔥 → 🔥🔥🔥
- index.md 狀態變更：無（新增 john-jumper 頁面）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | anthropic-government-policy.md | ✅ 通過 |
  | ai-agent-safety.md | ✅ 通過（新增 AI agent 進攻性濫用分類）|
  | enterprise-cost-management.md | ✅ 通過 |
  | enterprise-tool-tracker.md | ✅ 通過 |
  | anthropic-business.md | ✅ 通過 |
  | community-tech-discussions.md | ✅ 通過 |
  | community-tech-patterns.md | ✅ 通過 |
  | code-quality-decline.md | ✅ 通過 |
  | feature-radar.md | ✅ 通過 |
  | john-jumper.md | ✅ 通過（待核實標記正確套用）|
  | boris-cherny.md | ✅ 通過 |
  | fable-5.md | ✅ 通過 |
  | mythos.md | ✅ 通過 |

## 2026-06-19 Ingest | news/2026-06-19.md（77 則）

- 來源日報：`news/2026-06-19.md`（77 則，6 來源；主軸：Fable 5 / Mythos 出口管制持續（SK Telecom 中國關聯確認為根本動機 HN score 110、Amazon 研究員越獄漏洞舉報、Ciauri 首爾記者會「數日內恢復」、白宮談判轉向設定 AI 安全規則、國會議員施壓）；Claude Code v2.1.183 auto mode 破壞性 Git 指令封鎖；企業整合（Atlassian Claude Agent for Jira、JFrog Governed Claude Code）；SpaceX $60B Cursor 收購影響競爭格局；社群工具爆發（Pagecast / AI Commander / BeamWeaver / Pi Extension / Everything Claude Code microVM / Sqim / Prompt Foundry）；技術討論（Vibe coding 成就感缺失延燒、Loop Engineering、記憶管理技巧、無障礙偏差 issue）；LLM 無障礙偏差 issue #56079（WCAG 2.2 AA 規格被忽視）；Claude Code CVE 治理實踐報告）
- 更新頁面：
  - `entities/claude-code.md`：版本表 prepend v2.1.183（auto mode 破壞性 Git 指令封鎖）；最後更新 2026-06-19
  - `entities/fable-5.md`：歷史記錄 prepend 2026-06-19（SK Telecom 中國關聯、Amazon 越獄揭露、Ciauri 解禁聲明、Bloomberg 早期用戶豁免、印度 AI 主權討論）；最後更新 2026-06-19
  - `entities/mythos.md`：時序 prepend 2026-06-19（SK Telecom 根本動機確認、Amazon 研究員角色）；最後更新 2026-06-19
  - `topics/anthropic-government-policy.md`：攻防紀錄 prepend 3 行（白宮談判轉向 AI 安全規則、要求徹底阻絕越獄、國會議員施壓 WaPo）；時序 prepend 2026-06-19 3 事件；最後更新 2026-06-19
  - `topics/ai-agent-safety.md`：技術彙整 prepend 3 條（無障礙偏差 issue #56079、Claude Code CVE 治理報告、Claude Chat 濫用安全通報）；時序 prepend 2026-06-19；最後更新 2026-06-19
  - `topics/anthropic-business.md`：時序 prepend 2026-06-19（Atlassian Claude Agent for Jira、JFrog Governed Claude Code、Anthropic IPO 傳聞）；最後更新 2026-06-19
  - `topics/enterprise-tool-tracker.md`：企業表格新增 Atlassian（Claude Agent for Jira，✅）、JFrog（Governed Claude Code，✅）；工具競爭態勢更新；時序 prepend 2026-06-19；最後更新 2026-06-19
  - `topics/competitor-landscape.md`：Cursor 條目補充 SpaceX $60B 收購細節；時序 prepend 2026-06-19；最後更新 2026-06-19
  - `topics/community-tech-tools.md`：新增 5 個 Show HN 工具（Prompt Foundry、Sqim、Everything Claude Code microVM、Pi Extension、BeamWeaver）；痛點洞察更新；最後更新 2026-06-19
  - `topics/community-tech-patterns.md`：新增 3 個模式（Loop Engineering、Self-rewriting CRM、Spec-driven Development CLI）；最後更新 2026-06-19
  - `topics/community-tech-discussions.md`：Vibe coding 模式從 ☄️閃現 → 🌊延燒；技術彙整 prepend 2 條（記憶管理技巧、CLAUDE.md 詢問行為自訂）；最後更新 2026-06-19
  - `wiki/feature-radar.md`：全覽表 prepend v2.1.183 條目；Claude Code Artifacts 熱度升至 🔥🔥🔥🔥（Pagecast 工具跟進）；最後更新 2026-06-19
- 新增頁面：`wiki/entities/chris-ciauri.md`（Anthropic 國際業務總監，首爾記者會解禁聲明）
- 升格檢查（discussions → patterns）：
  - Vibe coding 成就感缺失（第 2 天，🌊延燒）— 討論持續，但未出現可複用步驟，**不升格**
  - LLM 無障礙偏差（第 2 天，🌊延燒）— 技術原因清楚但無 workaround 共識，**不升格**
- feature-radar 更新：新增 Claude Code v2.1.183（🔥🔥，✅）；Claude Code Artifacts 熱度升 🔥🔥🔥 → 🔥🔥🔥🔥
- 本日新增工具：Prompt Foundry（Show HN）、Sqim（Show HN）、Everything Claude Code microVM（Show HN score 1）、Pi Extension（Show HN）、BeamWeaver（Show HN）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過 |
  | entities/fable-5.md | ✅ 通過 |
  | entities/mythos.md | ✅ 通過 |
  | topics/anthropic-government-policy.md | ✅ 通過 |
  | topics/ai-agent-safety.md | ✅ 通過 |
  | topics/anthropic-business.md | ✅ 通過 |
  | topics/enterprise-tool-tracker.md | ✅ 通過 |
  | topics/competitor-landscape.md | ✅ 通過 |
  | topics/community-tech-tools.md | ✅ 通過 |
  | topics/community-tech-patterns.md | ✅ 通過 |
  | topics/community-tech-discussions.md | ✅ 通過 |
  | wiki/feature-radar.md | ✅ 通過 |
  | entities/chris-ciauri.md（新建） | ✅ 通過 |

---

## 2026-06-18 Ingest | news/2026-06-18.md（92 則）

- 來源日報：`news/2026-06-18.md`（92 則，6 來源；主軸：Fable 5 / Mythos 出口管制談判進入最終階段（SK Telecom 中國關聯揭露、Anthropic 提交解封方案、Politico 違法疑慮）；Claude Code Artifacts 官方功能正式發布；JPMorgan HK 被迫斷連；Claude Corps $150M；Agent SDK 計費暫停持續；社群工具爆發（job-search / LegalRabbit DOCX / AI Commander / Gorchestra / Pagecast / Parcle）；Python SDK v0.111.0 refusal-fallback helpers）
- 更新頁面：
  - `entities/fable-5.md`：新增 2026-06-18 時序（SK Telecom / China 揭露、Anthropic 解封提案、JPMorgan HK 斷連、Politico 違法疑慮）；參考來源新增 news/2026-06-18；最後更新 2026-06-18
  - `topics/anthropic-government-policy.md`：攻防記錄 prepend 5 條（SK Telecom 揭露、Ciauri 聲明、解封提案、Politico 違法疑慮、JPMorgan HK）；目前局勢更新；時序新增 2026-06-18 4 條；最後更新 2026-06-18
  - `entities/claude-code.md`：版本表 prepend Claude Code Artifacts / SDK v0.111.0 / Vertex TS SDK v0.18.0；最後更新 2026-06-18
  - `entities/pricing.md`：新增 2026-06-18 政策記錄（DevOps.com 計費暫停確認、SaaStr B2B 定價分析、HN 花費調查）；最後更新 2026-06-18
  - `topics/anthropic-business.md`：新增 2026-06-18 時序 4 條（JPMorgan HK、Andy Jassy 報導、Project Fetch Phase Two、Claude Corps $150M Forbes）；最後更新 2026-06-18
  - `topics/community-tech-discussions.md`：熱門討論 prepend 3 條（vibe coding 成就感缺失、Claude Code 無障礙偏差、長 session 前後落差）；技術彙整 prepend 無障礙偏差條目；最後更新 2026-06-18
  - `topics/community-tech-tools.md`：新增 7 個工具（job-search、LegalRabbit DOCX、AI Commander、Gorchestra、Pagecast、Parcle、token-warden）；痛點洞察更新 Token 成本不透明欄；最後更新 2026-06-18
  - `feature-radar.md`：全覽表 prepend 3 條（Artifacts、Python SDK v0.111.0、TS Vertex v0.18.0）；最新功能 prepend Claude Code Artifacts 詳細條目；最後更新 2026-06-18
  - `topics/enterprise-tool-tracker.md`：企業表格新增 JPMorgan Chase（❌ 2026-06-18 因出口管制）；時序 prepend 2026-06-18；最後更新 2026-06-18
  - `entities/mythos.md`：時序 prepend 2026-06-18（SK Telecom / China 關聯揭露）；最後更新 2026-06-18
- 新增頁面：無（Claude Code Artifacts 整合至 entities/claude-code 版本表和 feature-radar；JPMorgan HK 整合至 enterprise-tool-tracker 和 fable-5 時序）
- 升格檢查（discussions → patterns）：
  - OpenAI vs Anthropic 定價戰（第 8 天，🌊延燒）— 今日有新定價分析，但核心論點未收斂為可執行步驟，**不升格**
  - AI Skill Atrophy（第 9 天，🌊延燒）— 今日無新直接相關，**不升格**
  - Agentic 專案目錄結構（第 4 天，🌊延燒）— Parcle 補充了記憶層解法，但共識未形成可複用步驟，**不升格**
- feature-radar 更新：新增 Claude Code Artifacts（🔥🔥🔥，⚡ 有條件推薦）；新增 Python SDK v0.111.0（🔥，✅）；新增 TS Vertex SDK v0.18.0（🔥，✅）
- 本日新增工具：job-search（Show HN）、LegalRabbit DOCX（Show HN）、AI Commander（Show HN）、Gorchestra（Show HN）、Pagecast（Show HN）、Parcle（Show HN）、token-warden（HN score 4）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/fable-5.md | ✅ 通過（2026-06-18 時序 prepend；現況已涵蓋 SK Telecom 揭露） |
  | topics/anthropic-government-policy.md | ✅ 通過（攻防記錄 5 條 prepend；目前局勢更新至最新狀態） |
  | entities/claude-code.md | ✅ 通過（Artifacts 等 3 條版本表 prepend） |
  | entities/pricing.md | ✅ 通過（2026-06-18 政策記錄新增） |
  | topics/anthropic-business.md | ✅ 通過（2026-06-18 時序 4 條 prepend） |
  | topics/community-tech-discussions.md | ✅ 通過（3 條熱門討論 prepend；技術彙整新增無障礙偏差條目） |
  | topics/community-tech-tools.md | ✅ 通過（7 工具新增；痛點洞察更新） |
  | feature-radar.md | ✅ 通過（Artifacts 條目詳細、全覽表同步更新） |
  | topics/enterprise-tool-tracker.md | ✅ 通過（JPMorgan HK 新增至企業表格和時序） |
  | entities/mythos.md | ✅ 通過（SK Telecom / China 關聯時序 prepend） |

---

## 2026-06-17 Ingest | news/2026-06-17.md（81 則）

- 來源日報：`news/2026-06-17.md`（81 則，6 來源；主軸：Fable 5 / Mythos 出口管制談判破裂（G7 無豁免、Commerce 部工作組無結果；Wired / NY Post / Euronews）；Agent SDK 計費暫停 Ars Technica 深度報導；Pentagon 三分之二 AI 工作量移出 Anthropic；SpaceX 正式完成 Cursor 收購；Claude Code v2.1.179 串流修復；社群工具湧現（AgentPace / Mira / Offload / cc-reflection / Kevin））
- 更新頁面：
  - `entities/fable-5.md`：新增 2026-06-17 時序（G7 無豁免、談判再度破裂、Guardian 評論、TechCrunch 銷售諷刺分析）；參考來源新增 news/2026-06-17；最後更新 2026-06-17
  - `topics/anthropic-government-policy.md`：新增 2026-06-17 時序 4 條（談判破裂、G7 無豁免、Pentagon 轉移工作量、Lutnick 致函全文曝光）；最後更新 2026-06-17
  - `entities/pricing.md`：新增 2026-06-17 政策記錄（Ars Technica 計費暫停深度報導）；最後更新 2026-06-17
  - `entities/claude-code.md`：版本表新增 v2.1.179（串流修復、spinner 修復、滑鼠滾輪修復）；最後更新 2026-06-17
  - `topics/anthropic-business.md`：新增 2026-06-17 時序 3 條（SpaceX 正式完成 Cursor 收購、Anthropic 企業市佔超 OpenAI 細節、Wipro Applied AI 卓越中心揭牌）；最後更新 2026-06-17
  - `topics/community-tech-discussions.md`：prepend 3 條新討論（AI agent 長 session 退化量測、CLAUDE.md 固定租金、Fable 5 下線後 Sonnet 5 日常主力討論）；最後更新 2026-06-17
  - `topics/community-tech-tools.md`：新增 6 個工具（AgentPace、Mira、cc-reflection、Offload、Kevin、AptSelect）；痛點洞察表格更新 Token 成本不透明欄；最後更新 2026-06-17
  - `feature-radar.md`：新增 v2.1.179 條目；全覽表新增 v2.1.179 列；最後更新 2026-06-17
- 新增頁面：無（Fable 5 出口管制整合至既有頁面；SpaceX Cursor 整合至 topics/anthropic-business）
- 升格檢查（discussions → patterns）：
  - Agentic 專案目錄結構（第 3 天，🌊延燒）— 今日無新直接討論，尚無多人複現共識，**不升格**
  - AI Skill Atrophy（第 8 天，🌊延燒）— 今日無直接相關，**不升格**
  - OpenAI vs Anthropic 定價戰（第 7 天，🌊延燒）— 有新的 Anthropic 超越 OpenAI 市佔數據，但核心論述未收斂為可執行步驟，**不升格**
- feature-radar 更新：新增 v2.1.179 串流修復條目（🔥，✅ 推薦，純 bug fix）
- 本日新增工具：AgentPace（Show HN）、Mira（Show HN）、cc-reflection（HN score 3）、Offload（HN score 3）、Kevin（HN score 3）、AptSelect（HN score 2）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/fable-5.md | ✅ 通過（2026-06-17 時序 prepend；現況段落完整） |
  | topics/anthropic-government-policy.md | ✅ 通過（2026-06-17 時序 4 條 prepend） |
  | entities/pricing.md | ✅ 通過（2026-06-17 政策記錄新增） |
  | entities/claude-code.md | ✅ 通過（v2.1.179 版本表新增） |
  | topics/anthropic-business.md | ✅ 通過（2026-06-17 時序 3 條 prepend） |
  | topics/community-tech-discussions.md | ✅ 通過（3 條新討論 prepend） |
  | topics/community-tech-tools.md | ✅ 通過（6 工具新增至表格頂端） |
  | feature-radar.md | ✅ 通過（v2.1.179 條目新增；全覽表同步更新） |

---

## 2026-06-16 Ingest | news/2026-06-16.md（84 則）

- 來源日報：`news/2026-06-16.md`（84 則，6 來源；主軸：Fable 5/Mythos 5 出口管制爭議持續（David Sacks vs Anthropic jailbreak 版本衝突；Dario 被控拒絕修復；TechCrunch 反駁管制與 jailbreak 無關）；Agent SDK 計費切割政策暫停；Claude Max 集體訴訟；SpaceX $60B 收購 Cursor；v2.1.178 Tool(param:value) 語法；Agentjacking 攻擊揭露）
- 更新頁面：
  - `entities/fable-5.md`：新增 2026-06-16 時序（Sacks X 聲明、TechCrunch 反駁分析、Fable 5 消失後用戶依賴感爆發）；參考來源新增 news/2026-06-16；最後更新 2026-06-16
  - `topics/anthropic-government-policy.md`：新增 2026-06-16 時序 4 條（週一協商啟動、Sacks vs Anthropic 版本衝突、The Atlantic 評論、資安領袖呼籲解禁）；最後更新 2026-06-16
  - `entities/pricing.md`：新增 2026-06-16 政策記錄（Agent SDK 計費暫停、Claude Max 訴訟、AI 定價戰）；更新計費架構說明加暫停公告；最後更新 2026-06-16
  - `entities/claude-code.md`：版本表新增 v2.1.178（Tool(param:value) 語法）；最後更新 2026-06-16
  - `topics/anthropic-business.md`：新增 2026-06-16 時序 3 條（SpaceX 收購 Cursor、Wipro AI 中心、AI 定價戰）；最後更新 2026-06-16
  - `topics/community-tech-discussions.md`：prepend 4 條新討論（Agentjacking、PM vibe coding 正式產品爭議、agentic 目錄結構延燒更新、AI 定價比較）；新增 Agentjacking 技術彙整條目；最後更新 2026-06-16
  - `topics/community-tech-tools.md`：新增 5 個工具（claude_code_vs、Spotlight、Devloop、machine0、HashMeterAi）；最後更新 2026-06-16
  - `feature-radar.md`：新增 v2.1.178 詳細條目（Tool(param:value) 語法）；全覽表新增 v2.1.178 列；最後更新 2026-06-16
  - `topics/ai-agent-safety.md`：新增 Agentjacking 技術彙整（Sentry DSN 攻擊機制、攻擊面、防護建議）；最後更新 2026-06-16
- 新增頁面：無（Claude Max 訴訟整合至 entities/pricing；SpaceX Cursor 收購整合至 topics/anthropic-business；Agentjacking 整合至 topics/ai-agent-safety）
- 升格檢查（discussions → patterns）：
  - OpenAI vs Anthropic 定價戰（第 6 天，🌊延燒）— 有更多用戶成本比較，但無可升格工作流共識，**不升格**
  - AI Skill Atrophy（第 7 天，🌊延燒）— 今日無直接相關，**不升格**
  - Agentic 目錄結構（第 2 天，🌊延燒更新）— 有更多討論但尚無共識步驟，**不升格**
- feature-radar 更新：新增 v2.1.178 `Tool(param:value)` 功能條目（🔥🔥，✅ 推薦，正式發布）；Python SDK v0.109.2 / TS SDK v0.104.2 退役模型清理（純維護，無新使用者端功能，不收錄）
- 本日新增工具：claude_code_vs（Show HN 19）、Spotlight（Show HN 8）、Devloop（Show HN 3）、machine0（Show HN 88）、HashMeterAi（Show HN 3）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/fable-5.md | ✅ 通過（2026-06-16 時序 prepend；現況段落完整）|
  | topics/anthropic-government-policy.md | ✅ 通過（2026-06-16 時序 4 條 prepend）|
  | entities/pricing.md | ✅ 通過（政策暫停公告置頂；2026-06-16 政策記錄新增）|
  | entities/claude-code.md | ✅ 通過（v2.1.178 版本表新增）|
  | topics/anthropic-business.md | ✅ 通過（2026-06-16 時序 3 條 prepend）|
  | topics/community-tech-discussions.md | ✅ 通過（4 條新討論 prepend；Agentjacking 技術彙整新增）|
  | topics/community-tech-tools.md | ✅ 通過（5 工具新增至表格頂端）|
  | feature-radar.md | ✅ 通過（v2.1.178 詳細條目新增；全覽表同步更新）|
  | topics/ai-agent-safety.md | ✅ 通過（Agentjacking 技術彙整新增置頂）|

---

## 2026-06-15 Ingest | news/2026-06-15.md（77 則）

- 來源日報：`news/2026-06-15.md`（77 則，6 來源；主軸：Fable 5 / Mythos 5 出口管制政治風暴深化——個性衝突說、Anthropic 赴 DC 協商；Agent SDK 計費切割正式生效；非技術人員 Claude Code 商業成果社群熱議；多款新社群工具亮相；中國 Zhipu 股價應聲暴漲）
- 更新頁面：
  - `entities/fable-5.md`：新增 2026-06-15 時序（「They screwed us」個性衝突說、Stratechery 安全論述分析、Carney 警告、《經濟學人》批評、非技術人員商業成果討論）；參考來源新增 news/2026-06-15；最後更新 2026-06-15
  - `topics/anthropic-government-policy.md`：新增 2026-06-15 時序 5 條（赴 DC 協商、個性衝突說、Stratechery 分析、盟友震驚與批評、資安領袖呼籲解禁）；最後更新 2026-06-15
  - `topics/community-tech-discussions.md`：prepend 5 條新討論（生物學護欄矛盾、LLM 工具說明敏感性、agentic 目錄結構、非技術人員商業成果、AI 大型 PR 審查困境）；6/15 計費切割更新為🌸落幕；最後更新 2026-06-15
  - `topics/community-tech-tools.md`：新增 4 個工具（The Engineer、Canopy、Conan、zero-1）；最後更新 2026-06-15
  - `topics/anthropic-business.md`：新增 2026-06-15 時序 4 條（SpaceX 合作、FTX 股份估值 $75B、Claude Corps 後續、B2B SaaS 定價壓力）；最後更新 2026-06-15
  - `entities/pricing.md`：更新最後更新日期，反映計費切割正式生效；最後更新 2026-06-15
  - `feature-radar.md`：更新最後更新說明（今日無新功能條目）
- 新增頁面：無（FTX 估值計算為一次性事件；SpaceX 合作暫記 anthropic-business；Zhipu 股價為外部效應暫不建頁）
- 升格檢查（discussions → patterns）：
  - OpenAI vs Anthropic 定價戰（第 5 天，🌊延燒）— 今日有計費切割生效和 SaaStr 分析，但無可升格工作流共識，**不升格**
  - AI Skill Atrophy（第 6 天，🌊延燒）— 今日無直接相關，**不升格**
- feature-radar 更新：今日無符合准入定義的新官方功能（Agent SDK 計費切割屬計費政策；Claude Corps 屬公益計畫）
- 本日新增工具：The Engineer（Show HN）、Canopy（Show HN）、Conan（Show HN）、zero-1（Show HN）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/fable-5.md | ✅ 通過（2026-06-15 時序 prepend；現況段落完整）|
  | topics/anthropic-government-policy.md | ✅ 通過（2026-06-15 時序 5 條 prepend；因果鏈完整）|
  | topics/community-tech-discussions.md | ✅ 通過（5 條新討論 prepend；計費切割更新為落幕）|
  | topics/community-tech-tools.md | ✅ 通過（4 工具新增至表格頂端）|
  | topics/anthropic-business.md | ✅ 通過（2026-06-15 時序 4 條 prepend）|
  | entities/pricing.md | ✅ 通過（最後更新日期更新）|

---

## 2026-06-14 Ingest | news/2026-06-14.md（44 則）

- 來源日報：`news/2026-06-14.md`（44 則，6 來源；Fable 5 出口管制後續細節：Amazon 觸發、90 分鐘窗口、中國連結情報；EU/印度國際影響；Anthropic 化學研究合作；經濟政策框架；Agent SDK 計費切換提醒）
- 更新頁面：
  - `entities/fable-5.md`：新增 2026-06-14 時序（Amazon 觸發詳情、90 分鐘執行窗口、中國連結情報、EU/印度國際影響、社群反應）；參考來源新增 news/2026-06-14；最後更新 2026-06-14
  - `topics/anthropic-government-policy.md`：新增 2026-06-14 時序 5 條（Amazon 研究觸發、90 分鐘窗口、中國連結情報、EU 影響評估、印度 AI 自主辯論）；最後更新 2026-06-14
  - `topics/community-tech-discussions.md`：prepend 2 條新討論（Sub-agent Pipeline 設計錯誤、AI Agent 無視規則）；更新 6/15 計費切割條目補 6/14 用戶端提醒；最後更新 2026-06-14
  - `wiki/feature-radar.md`：全覽表新增 Anthropic 化學研究合作；最新功能區塊新增詳細條目；最後更新 2026-06-14
- 新增頁面：無（Fable 5 出口管制後續整合至既有頁面；化學研究合作為研究里程碑，非功能發布，暫不建 entity）
- 升格檢查（discussions → patterns）：
  - OpenAI vs Anthropic 定價戰（首見 2026-06-11，第 4 天，🌊延燒）— 今日無新定價戰內容，**不升格**
  - AI Skill Atrophy（首見 2026-06-10，第 5 天，🌊延燒）— 今日無直接相關，**不升格**
  - 6/15 計費切割（首見 2026-06-08，第 7 天，🌊延燒）— 進入最後提醒階段，無可升格工作流共識，**不升格**
- feature-radar 更新：新增 Anthropic 化學研究合作（🔥🔥，⏳ 觀望，研究里程碑）；Agent SDK 計費切割熱度已達最高🔥🔥🔥🔥🔥，無需調整
- 本日新增工具：無（Conan macOS HUD 為 Reddit 來源 score=0，不符合入選標準）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/fable-5.md | ✅ 通過（2026-06-14 時序 prepend；現況段落完整；參考來源已補）|
  | topics/anthropic-government-policy.md | ✅ 通過（2026-06-14 時序 5 條 prepend；因果鏈完整）|
  | topics/community-tech-discussions.md | ✅ 通過（2 條新討論 prepend；6/15 計費條目更新；延燒判斷正確）|
  | wiki/feature-radar.md | ✅ 通過（化學研究合作新增；全覽表同步更新）|

---

## 2026-06-13 Ingest | news/2026-06-13.md（80 則）

- 來源日報：`news/2026-06-13.md`（80 則，6 來源；Fable 5 / Mythos 5 美國政府出口管制強制下線 + 政府論述弔詭反噬 + v2.1.177 + N-day 漏洞研究 + billing change harness 崩潰）
- 更新頁面：
  - `entities/fable-5.md`：狀態更新（暫停全球存取）；現況段落補充 2026-06-13 重大事件；新增 2026-06-13 時序（政府出口管制指令、安全論述反噬、社群弔詭分析、Fable 5 下線前 72 小時成果展示）；參考來源新增 news/2026-06-13；最後更新 2026-06-13
  - `entities/claude-code.md`：版本表頂端新增 v2.1.177（Bug fixes and reliability improvements）；最新版本更新；最後更新 2026-06-13
  - `topics/anthropic-government-policy.md`：新增 2026-06-13 時序（出口管制指令、安全論述反噬分析、地緣政治影響）；最後更新 2026-06-13
  - `topics/community-tech-discussions.md`：熱門討論 prepend 3 條（六個月 harness 崩潰、Fable 5 規劃品質求解、AI 代碼審查三方一致率 22%）；最後更新 2026-06-13
  - `topics/community-tech-tools.md`：新增 1 個工具（bulk-delete-claude-chat，HN score 56）；最後更新 2026-06-13
  - `wiki/index.md`：fable-5 摘要更新（反映 6/13 暫停存取）；最後更新欄更新
- 新增頁面：無（Fable 5 下線事件已整合進 entities/fable-5 和 topics/anthropic-government-policy）
- 升格檢查（discussions → patterns）：
  - OpenAI vs Anthropic 定價戰（首見 2026-06-11，第 3 天，🌊延燒）— 今日日報無新的定價戰內容，維持 🌊延燒，**不升格**
  - AI Skill Atrophy（首見 2026-06-10，第 4 天，🌊延燒）— 今日日報無直接相關，社群仍無可複用共識，**不升格**
  - 6/15 計費切割（首見 2026-06-08，第 6 天，🌊延燒）— 明日生效，今日 harness 崩潰討論更像結果反應而非工作流模式，**不升格**
  - **無升格**
- feature-radar 更新：v2.1.177 為 Bug fixes only，無使用者端功能，**不收錄**（依版本更新收錄判斷規則）；N-day 漏洞研究為安全研究報告非功能發布，**不收錄**
- 本日新增工具：bulk-delete-claude-chat（1 個，累積 207 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/fable-5.md | ✅ 通過（現況段落前置重大事件說明；狀態反映暫停；時序 prepend）|
  | entities/claude-code.md | ✅ 通過（v2.1.177 版本表頂端新增，含功能說明）|
  | topics/anthropic-government-policy.md | ✅ 通過（2026-06-13 時序 prepend；三個面向分析完整）|
  | topics/community-tech-discussions.md | ✅ 通過（3 條新討論 prepend；最後更新日期正確）|
  | topics/community-tech-tools.md | ✅ 通過（1 個新工具頂端新增；入選標準符合）|

---

## 2026-06-13 Lint

- 修正矛盾：無
- 補連結：chris-olah 確認非孤立（anthropic-government-policy.md:27 已有 wikilink 別名格式）
- 狀態更新：無（enterprise-cost-management 已於 2026-06-12 由 Lint 改為 monitoring）
- 遷移至 entities：無
- 新增 entities：`entities/dario-amodei.md`（Anthropic CEO；出現 7 頁 9 次，超過 3 頁門檻）；已在 topics/anthropic-business.md 相關實體補入 wikilink
- 呈現品質：全部通過（近期 ingest 已覆蓋所有更新頁面）
- 超長頁面（> 500 行）：
  - `wiki/feature-radar.md`（565 行）→ ✅ 已拆分：2026-05 功能條目移至 `wiki/feature-radar-archive-2026-05.md`（主檔降至 140 行）
  - `topics/community-tech-discussions.md`（597 行）→ 📋 待辦：使用者選擇稍後以主題合併方式處理 🌙靜候 條目（非按月封存）
- 規則檔健檢：
  - wiki/CLAUDE.md：46 行（閾值 80 行）✅
  - .claude/rules/wiki-ingest.md：243 行（閾值 250 行）✅
  - 矛盾：無
  - 引用驗證：全部通過（7 個錨點：首次出現、痛點洞察、近期工具、技術彙整、熱門討論、衍生、全覽表）
  - 遵守率：全部通過（近 3 次 ingest 呈現品質審查 3/3、feature-radar 更新 3/3）
  - 過期規則（> 60 天）：無（最舊 2026-04-25，49 天）
  - 簡化：跳過（兩檔均在閾值內）
- overview.md：已更新（Fable 5 發布、6/15 計費明日生效、TCS 5 萬員工、AI 定價戰、IPO 機密申請）

---

## 2026-06-12 Ingest | news/2026-06-12.md（74 則）

- 來源日報：`news/2026-06-12.md`（74 則，6 來源；DXC Technology 全球聯盟 + Claude Corps $1.5 億確認 + Fable 5 Jailbreak 爭議 + v2.1.175 enforceAvailableModels + AI 定價戰升溫 + Anthropic 盲目打擊合作夥伴報導）
- 更新頁面：
  - `entities/fable-5.md`：新增 2026-06-12 時序（Jailbreak 持續爭議、Anthropic 駁斥、「honest」字眼分析、917 場景測試）；參考來源新增 news/2026-06-12；最後更新 2026-06-12
  - `entities/claude-code.md`：新增 v2.1.175 版本記錄（`enforceAvailableModels` 管理設定）；最後更新 2026-06-12
  - `topics/anthropic-business.md`：新增 2026-06-12 時序（DXC 全球聯盟、Claude Corps $1.5 億確認、AI 定價戰升溫、Anthropic 盲目打擊合作夥伴）；戰略合作表格新增 DXC Technology；最後更新 2026-06-12
  - `topics/enterprise-tool-tracker.md`：新增 DXC Technology 企業列；Claude API 採用數 12→13；新增 2026-06-12 時序；最後更新 2026-06-12
  - `topics/community-tech-tools.md`：新增 3 個工具（AVP、Claustrophobic、Workplane 更新）；Token 成本不透明痛點新增 Claustrophobic；最後更新 2026-06-12
  - `topics/community-tech-discussions.md`：熱門討論 prepend 4 條（優先序衝突邊界實驗、CLAUDE.md 精簡實證、Air-gapped 攻略、917 場景測試）；AI Skill Atrophy 升格至 🔥🔥🔥🔥；OpenAI vs Anthropic 定價戰模式改為 🌊延燒（第 2 天）；最後更新 2026-06-12
  - `wiki/feature-radar.md`：全覽表新增 v2.1.175（🔥🔥，✅）；新增 v2.1.175 完整條目；最後更新 2026-06-12
- 新增頁面：無
- 升格檢查（discussions → patterns）：
  - AI Skill Atrophy（首見 2026-06-10，第 3 天，🌊延燒）— 判斷：社群警覺度升高但仍無可複用的「做法 A 比 B 好」建議，**不升格**
  - OpenAI vs Anthropic 定價戰（首見 2026-06-11，第 2 天）— 未達 3 天門檻，**不升格**
  - **無升格**
- 本日新增工具：AVP（agent-vault-proxy）/ Claustrophobic（共 2 個，累積 206 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/fable-5.md | ✅ 通過（摘要可獨立閱讀；Jailbreak 持續爭議更新至歷史記錄；917 場景測試資訊新增）|
  | entities/claude-code.md | ✅ 通過（v2.1.175 版本表頂端新增，含明確功能說明）|
  | topics/anthropic-business.md | ✅ 通過（DXC 時序 prepend；戰略合作表格更新）|
  | topics/enterprise-tool-tracker.md | ✅ 通過（DXC 新增；採用數更新）|
  | topics/community-tech-tools.md | ✅ 通過（3 個工具頂端新增；痛點洞察更新）|
  | topics/community-tech-discussions.md | ✅ 通過（4 條新討論 prepend；模式更新正確）|
  | wiki/feature-radar.md | ✅ 通過（v2.1.175 條目新增含快速上手；全覽表更新）|

---

## 2026-06-11 Maintenance（分類強化）

- 狀態詞彙標準化：6 頁（project-deal, bugcrawl, mythos, openclaw, claude-security, stainless）
- 領域欄位：全部 entities/topics 頁面新增 **領域：**（6 分類）
- 刪除 redirect stub：topics/google-investment（入站連結已改指 entities 版）
- 規則固化：.claude/rules/wiki-ingest.md 新增「命名與分類規則」、移除重複的「日報格式」區塊
- Web Reader：STATUS_MAP 對齊新詞彙、領域篩選 chips
- 註：本次為純 metadata 維護，未更動各頁「最後更新」欄位

## 2026-06-11 Ingest | news/2026-06-11.md（93 則）

- 來源日報：`news/2026-06-11.md`（93 則，6 來源；Fable 5 護欄政策撤回道歉 + Claude Corps 公益計畫 + TCS 5 萬員工部署 + Fable 5 Jailbreak 公開 + OpenAI 降價戰 + v2.1.173 發布）
- 更新頁面：
  - `entities/fable-5.md`：新增 2026-06-11 時序（政策撤回道歉、Jailbreak PoC、Microsoft 禁用、TCS 部署、Claude Corps）；爭議區塊重寫（靜默護欄改為「已部分撤回」，新增資安過激攔截、Jailbreak、Microsoft 禁用、成本高昂）；參考來源新增 news/2026-06-11；最後更新 2026-06-11
  - `entities/claude-code.md`：新增 v2.1.173 版本記錄（Fable 5 `[1m]` 後綴修復、誤報沙盒錯誤修正）；現況最新版本更新；最後更新 2026-06-11
  - `topics/community-tech-tools.md`：新增 6 個工具（Claumon / Foyer / ShellShot / Workplane / 5dive / Vaportrail）；痛點洞察 Token 成本不透明新增 Claumon；最後更新 2026-06-11
  - `topics/community-tech-discussions.md`：熱門討論 prepend 3 條（Anthropic 護欄政策撤回、Fable 5 Jailbreak、OpenAI vs Anthropic 定價戰）；Fable 5 靜默護欄改模式 🌸落幕；技術彙整新增 3 條（護欄政策撤回、Jailbreak 技術、資安護欄過激）；最後更新 2026-06-11
  - `topics/anthropic-business.md`：新增 2026-06-11 時序（TCS Partnership / OpenAI 降價 / Claude Corps / Dario 監管主張 / 政策撤回）；最後更新 2026-06-11
  - `topics/anthropic-government-policy.md`：新增 2026-06-11 時序（Dario 主張政府可阻止 AI 模型 / 州 AI 法律立場）；最後更新 2026-06-11
  - `topics/enterprise-tool-tracker.md`：新增 TCS 企業列（5 萬員工）；Claude API 採用數 11→12；新增 2026-06-11 時序；最後更新 2026-06-11
  - `wiki/feature-radar.md`：全覽表新增 Claude Corps（🔥🔥，⏳）和 v2.1.173（🔥，✅）；Fable 5 備注更新（護欄政策 6/11 修改）；最後更新 2026-06-11
- 新增頁面：無
- 升格檢查（discussions → patterns）：AI Skill Atrophy（首見 2026-06-10，第 2 天）未達升格門檻。OpenAI vs Anthropic 定價戰（今日首見）未達升格門檻。**無升格**。
- 本日新增工具：Claumon / Foyer / ShellShot / Workplane / 5dive / Vaportrail（共 6 個，累積 204 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/fable-5.md | ✅ 通過（摘要可獨立閱讀；爭議區塊完整更新反映政策撤回；時序 prepend）|
  | entities/claude-code.md | ✅ 通過（v2.1.173 版本表頂端新增）|
  | topics/community-tech-tools.md | ✅ 通過（6 個新工具頂端新增；痛點洞察更新）|
  | topics/community-tech-discussions.md | ✅ 通過（熱門討論 prepend；技術彙整 prepend；靜默護欄改落幕）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend）|
  | topics/anthropic-government-policy.md | ✅ 通過（時序 prepend）|
  | topics/enterprise-tool-tracker.md | ✅ 通過（TCS 新增；採用數更新）|
  | wiki/feature-radar.md | ✅ 通過（全覽表新增；Fable 5 備注更新）|

---

## 2026-06-10 Ingest | news/2026-06-10.md（99 則）

- 來源日報：`news/2026-06-10.md`（99 則，6 來源；Claude Fable 5 正式發布 + 30 天資料保留政策 + Fable 靜默護欄爭議 + 供應鏈攻擊升級 + 訂閱縮水 + Vercel Anthropic 佔 65% 支出）
- 更新頁面：
  - `entities/mythos.md`：狀態更新（部分公開）；現況增加 Fable 5 / 30 天保留 / 靜默護欄說明；新增 2026-06-10 與 2026-06-09 時序；最後更新 2026-06-10
  - `entities/claude-code.md`：新增 v2.1.170（Fable 5 支援）版本記錄；現況最新版本更新；最後更新 2026-06-10
  - `entities/pricing.md`：新增 2026-06-09 Fable 5 定價政策紀錄；最後更新 2026-06-10
  - `topics/anthropic-business.md`：新增 2026-06-10 時序（Fable 5 發布 + Vercel 資料 + Rockefeller + NC 財務長 + 批評性評論）；最後更新 2026-06-10
  - `topics/ai-agent-safety.md`：新增 2026-06-10 時序（供應鏈攻擊升級至 294,842 secrets + JFrog 插件 + 安全工具爆發）；最後更新 2026-06-10
  - `topics/community-tech-tools.md`：新增 9 個工具（claude-quota / OpenYabby / agent-pd / claudefeed / agentgraphed / context-analyzer / permafrost / Lanes v0.43.0 / ktx）；痛點洞察更新；最後更新 2026-06-10
  - `topics/community-tech-discussions.md`：熱門討論 prepend 5 條（Fable 靜默護欄 / Fable 成本爭議 / Claude 意識論述 / AI Skill Atrophy / Deep Research 缺陷）；技術彙整新增 3 條；最後更新 2026-06-10
  - `wiki/feature-radar.md`：新增 Claude Fable 5 詳細條目 + 全覽表 3 條更新；最後更新 2026-06-10
- 新增頁面：`entities/fable-5.md`（Claude Fable 5 實體頁；首次出現 2026-06-09；包含熱度表格、使用指南、爭議）
- feature-radar 更新：Claude Fable 5（🔥🔥🔥🔥🔥，⚡ 有條件推薦，✅ 收錄）；Python SDK v0.109.1（🔥，✅ 收錄）；Claude Code v2.1.170（🔥🔥，✅ 收錄）
- 升格檢查（discussions → patterns）：6/15 計費切割（首見 2 天）、AI Skill Atrophy（首見今日）均未達升格門檻。**無升格**。
- 本日新增工具：claude-quota / OpenYabby / agent-pd / claudefeed / agentgraphed / context-analyzer / permafrost / Lanes v0.43.0 / ktx（共 9 個，累積 198 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/fable-5.md（新建）| ✅ 通過（摘要可獨立閱讀；熱度表格緊接摘要；含使用指南與爭議）|
  | entities/mythos.md | ✅ 通過（狀態更新；現況重新整理；Fable 5 事件前置）|
  | entities/claude-code.md | ✅ 通過（v2.1.170 版本表頂端新增）|
  | entities/pricing.md | ✅ 通過（Fable 5 定價紀錄新增在最前）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend）|
  | topics/ai-agent-safety.md | ✅ 通過（時序 prepend，供應鏈攻擊升級完整記錄）|
  | topics/community-tech-tools.md | ✅ 通過（工具表頂端新增，痛點洞察更新）|
  | topics/community-tech-discussions.md | ✅ 通過（熱門討論 prepend，技術彙整 prepend）|
  | wiki/feature-radar.md | ✅ 通過（新增最新功能區塊，Fable 5 詳細條目）|

---

## 2026-06-09 Ingest（更新版）| news/2026-06-09.md（85 則）

- 來源日報：`news/2026-06-09.md`（85 則，6 來源；Mythos 公開版傳出、6/15 Agent SDK 計費切割、Anthropic/OpenAI IPO 雙雄競賽、Apollo/Blackstone $35B 晶片融資、LG 集團採用、Rubrik Agent Cloud、Claude 80%+ 生產碼確認、Fiverr 938% 需求暴增、Geoffrey Hinton 批評、Claude Code v2.1.169 `--safe-mode`）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.169 版本記錄（`--safe-mode` 旗標）；現況描述更新最新版本；最後更新維持 2026-06-09
  - `entities/mythos.md`：新增 2026-06-09 時序（公開版傳出 + N-day 研究發布）；最後更新維持 2026-06-09
  - `topics/anthropic-business.md`：新增 2026-06-09 時序（IPO 競賽 + $35B 融資 + LG + Rubrik + AppFolio + Claude 80% + Geoffrey Hinton 批評）；最後更新更新
  - `topics/recursive-self-improvement.md`：新增 2026-06-09 時序（5 月數據確認 80%+ + Fiverr 938% + 品牌曝光分析）；最後更新 2026-06-09
  - `topics/enterprise-tool-tracker.md`：新增 LG Group / Rubrik / AppFolio 三列；Claude Code 採用數 3→4，Claude API 採用數 8→11；新增 2026-06-09 時序；最後更新 2026-06-09
  - `topics/anthropic-government-policy.md`：新增 2026-06-09 時序（Trump 否認黑名單報復）；最後更新維持 2026-06-09
  - `topics/community-tech-tools.md`：新增 7 個工具（Rayline / Guardian Runtime / CapaKit / Storytime / cc-bridge / RunAPI / Intuned）；痛點洞察更新多模型鎖定防禦痛點；最後更新 2026-06-09
  - `topics/community-tech-discussions.md`：熱門討論 prepend 3 條（6/15 計費切割 / MCP 假退化 / Deep Research token 暴增）；技術彙整新增 2 條（6/15 計費 + MCP 過載）；最後更新 2026-06-09
  - `wiki/feature-radar.md`：新增 2 條（`--safe-mode` + Agent SDK 6/15 計費切割 Breaking Change）；最後更新 2026-06-09
  - `entities/pricing.md`：最後更新 2026-06-09（6/15 計費切割確認）
- 新增頁面：無（今日事件均為既有頁面延伸）
- feature-radar 更新：`--safe-mode`（新旗標，✅ 收錄）；Agent SDK 6/15 計費切割（Breaking Change，✅ 收錄）
- 升格檢查（discussions → patterns）：🌊延燒 項目中 6/15 計費（首見 1 天）、MCP 假退化（首見今日）均未達升格門檻；其他延燒項目為哲學討論，無具體可複用工作流步驟。**無升格**
- 本日新增工具：Rayline / Guardian Runtime / CapaKit / Storytime / cc-bridge / RunAPI / Intuned（共 7 個，累積 189 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過（版本表頂端新增 v2.1.169，現況描述同步更新）|
  | entities/mythos.md | ✅ 通過（時序 prepend，公開版傳出事件記錄完整）|
  | topics/anthropic-business.md | ✅ 通過（2026-06-09 時序 prepend，7 條新事件）|
  | topics/recursive-self-improvement.md | ✅ 通過（2026-06-09 時序 prepend）|
  | topics/enterprise-tool-tracker.md | ✅ 通過（3 新企業列 + 競爭態勢更新 + 時序 prepend）|
  | topics/anthropic-government-policy.md | ✅ 通過（時序 prepend）|
  | topics/community-tech-tools.md | ✅ 通過（7 工具插入表頭 + 痛點洞察更新）|
  | topics/community-tech-discussions.md | ✅ 通過（3 條 prepend + 2 條技術彙整）|
  | wiki/feature-radar.md | ✅ 通過（2 條新增至全覽表）|
  | entities/pricing.md | ✅ 通過（最後更新日期更新）|

---

## 2026-06-08 Ingest | news/2026-06-08.md

- 來源日報：`news/2026-06-08.md`（74 則，6 來源；npm 惡意套件 + MCP OAuth 劫持安全警報、Mythos NSA 軍事應用、Google Colab CLI Claude Code 整合、CLAUDE.md 最高 ROI、agent harness 降本 40%、ZoomInfo 企業採用、Levi AlphaEvolve 低成本複現等）
- 說明：本日大部分事件已在前次 2026-06-09 Ingest 中依日報 news/2026-06-09.md 完成更新（npm 攻擊、MCP漏洞、Mythos、CLAUDE.md ROI、meta-hook、1M context 等）。本次補充今日新抓取日報中的差異條目。
- 更新頁面：
  - `topics/enterprise-tool-tracker.md`：新增 ZoomInfo（GTM.AI Claude 整合）企業列；Claude API 採用數 7→8；新增 2026-06-08 時序；更新最後更新 2026-06-08
  - `topics/community-tech-tools.md`：新增 2 個工具（Levi / Claude Code Status Line）；插入表頭；工具總數 180→182
- 新增頁面：無
- feature-radar 更新：無（本日新增工具均非官方功能，已在前次 ingest 完成）
- 升格檢查（discussions → patterns）：無（前次 ingest 已確認無符合升格條件的 🌊延燒 討論）
- 本日新增工具：Levi / Claude Code Status Line（共 2 個，累積 182 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | topics/enterprise-tool-tracker.md | ✅ 通過（ZoomInfo 列新增，時序 prepend，關鍵資訊前置）|
  | topics/community-tech-tools.md | ✅ 通過（2 工具插入表頭）|

---

## 2026-06-09 Ingest | news/2026-06-09.md

- 來源日報：`news/2026-06-09.md`（73 則，6 來源；MCP 安全漏洞雙連擊、npm 供應鏈攻擊、Claude Code 131K stars、Mythos 進 NSA/Dragos OT、Google Colab CLI 整合、CLAUDE.md 最佳實踐社群分享、多款 Show HN 工具）
- 更新頁面：
  - `entities/claude-code.md`：更新 GitHub Stars（121K→131K）；新增 anthropic-sdk-python v0.107.1 版本記錄；更新最後更新 2026-06-09
  - `entities/mythos.md`：新增 2026-06-08 時序（Dragos OT 應用 + Pentagon 替換 Claude 報導）；更新最後更新 2026-06-09
  - `topics/ai-agent-safety.md`：新增 2026-06-08 時序（npm @redhat-cloud-services 後門 + CI/CD secrets 洩漏 + MCP OAuth Token 劫持）；更新最後更新 2026-06-09
  - `topics/anthropic-government-policy.md`：新增 2026-06-08 時序（Pentagon 因「太安全」尋替代）；更新最後更新 2026-06-09
  - `topics/anthropic-business.md`：新增 2026-06-08 時序（WashPost 最有影響力、Dario 文化論述、Saudi Velents 加入 Partner Network、Ed Zitron IPO 反對）；更新最後更新 2026-06-09
  - `topics/community-tech-tools.md`：新增 8 個工具（xword-pipeline / Agam / ARouter / Copilot Vulnerability Harness / Maggy / dbmachine / makememe / Lobsteady）；更新最後更新 2026-06-09
  - `topics/community-tech-discussions.md`：熱門討論 prepend 3 條（CLAUDE.md 最高 ROI / meta-hook / 1M Context vs Prompt Caching）；技術彙整新增 3 條；更新最後更新 2026-06-09
  - `wiki/feature-radar.md`：新增 Google Colab CLI 整合（🔥🔥）+ Python SDK v0.107.1（🔥）；更新最後更新 2026-06-09
- 新增頁面：無（今日事件均為既有頁面延伸）
- feature-radar 更新：Google Colab CLI 整合（有具體使用者端功能變更，符合收錄標準）；Python SDK v0.107.1（foundry bug fix，收錄為 🔥 ✅）
- 升格檢查（discussions → patterns）：無符合升格條件的 🌊延燒 討論（所有延燒項目均已有 patterns 對應或未達可複用步驟共識）
- 本日新增工具：xword-pipeline / Agam / ARouter / Copilot Vulnerability Harness / Maggy / dbmachine / makememe / Lobsteady（共 8 個，累積 180 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過（stars 更新 + 版本記錄新增）|
  | entities/mythos.md | ✅ 通過（時序 prepend）|
  | topics/ai-agent-safety.md | ✅ 通過（3 條安全事件時序 prepend）|
  | topics/anthropic-government-policy.md | ✅ 通過（時序 prepend）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend，4 條新事件）|
  | topics/community-tech-tools.md | ✅ 通過（8 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（3 條 prepend + 3 條技術彙整）|
  | wiki/feature-radar.md | ✅ 通過（2 條新增至全覽表）|

---

## 2026-06-07 Ingest | news/2026-06-07.md

- 來源日報：`news/2026-06-07.md`（56 則，6 來源；Jane Street 設計工作流革命 HN 201、YOLO 模式安全第一人稱記述、AI 財務永續性質疑 HN 45、Linux Desktop 需求 HN 66、Ccgs session 分享工具 HN 6、API billing 陷阱、SDK v0.107.0/v0.102.0 Managed Agents 小幅更新、v2.1.168 bug fix）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.168；更新最新版本描述；更新最後更新 2026-06-07
  - `topics/community-tech-tools.md`：新增 4 個工具（Ccgs / Lathe / LimitPing / Kite Markdown）；更新最後更新 2026-06-07
  - `topics/community-tech-discussions.md`：熱門討論 prepend 4 條（AI 設計工作流革命 / YOLO 模式安全 / AI 財務永續性 / API billing 陷阱）；技術彙整新增 2 條；更新最後更新 2026-06-07
  - `topics/ai-agent-safety.md`：新增 2026-06-07 時序（YOLO 模式記述 + Sandfence 工具回應）；更新最後更新 2026-06-07
  - `topics/anthropic-business.md`：新增 2026-06-07 時序（AI 財務永續性質疑 / IPO 潛力股 / Linux Desktop 需求）；更新最後更新 2026-06-07
  - `wiki/index.md`：更新社群工具數（168→172）+ 最後更新日期
- 新增頁面：無（今日事件均為既有頁面延伸）
- feature-radar 更新：無（v2.1.168 純 bug fix；SDK 更新無具體功能說明，不符合收錄標準）
- 升格檢查（discussions → patterns）：無符合升格條件的 🌊延燒 討論（現有延燒項目均已有 patterns 對應或未達多人複現共識）
- 本日新增工具：Ccgs / Lathe / LimitPing / Kite Markdown（共 4 個，累積 172 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過（版本表更新，現況描述最新）|
  | topics/community-tech-tools.md | ✅ 通過（4 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（4 條 prepend + 2 條技術彙整）|
  | topics/ai-agent-safety.md | ✅ 通過（時序 prepend）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend）|

---

## 2026-06-07 Lint

- 修正矛盾：無
- 補連結：`entities/chris-olah` — 在 `topics/anthropic-government-policy.md` 第 26 行補上 `[[entities/chris-olah|Chris Olah]]` wikilink（原為孤立頁面，僅 index.md 連結）
- 狀態更新：
  - `topics/community-tech-timeline`：ongoing → monitoring（最後更新 2026-05-22，15 天無新進展）
  - `topics/official-community-gap`：ongoing → monitoring（最後更新 2026-05-21，16 天無新進展）
  - `topics/competitor-landscape`：ongoing → monitoring（最後更新 2026-05-23，15 天無新進展）
  - `topics/community-tech-patterns`：ongoing → monitoring（最後更新 2026-05-23，15 天無新進展）
- 遷移至 entities：無（`topics/google-investment` 已在先前 lint 完成遷移）
- 新增 entities：無（Daniela Amodei 出現 2 個 wiki 頁，未達 3 頁閾值）
- 呈現品質：全部通過（讀取各頁摘要，結構清晰，關鍵資訊前置）
- 超長頁面（> 500 行）：`feature-radar.md`（520 行）— 使用者選擇稍後處理
- 規則檔健檢：
  - `wiki/CLAUDE.md`：46 行（閾值 80 行）✅
  - `.claude/rules/wiki-ingest.md`：244 行（閾值 250 行）✅
  - 矛盾：無
  - 引用驗證：全部通過（首次出現 / ## 痛點洞察 / 近期工具 / ## 技術彙整 / 熱門討論 / 衍生 / 全覽表 ×7）
  - ⚠️ 附記：`review-commands.md` Check 1c 中 `靈感來源` 錨點在 `community-tech-patterns.md` 不存在，屬 review-commands 問題，不影響 wiki-ingest 規則
  - 遵守率：全部通過（呈現品質 3/3 / feature-radar 3/3 / 新工具更新 3/3 / log 格式 3/3）
  - 過期規則（> 60 天）：無（最舊規則 2026-04-25，距今 43 天）
  - 簡化：跳過（兩者均在閾值內）
- `overview.md`：全面重寫（最後更新 2026-05-22 → 2026-06-07；新增 Opus 4.8、NSA Mythos、遞歸自我改進、168 工具等重大更新）
- `index.md`：更新 4 個 topics 狀態（monitoring）+ community-tech-tools 工具數（132→168）+ 最後更新日期

---

## 2026-06-06 Ingest | news/2026-06-06.md

- 來源日報：`news/2026-06-06.md`（70 則，6 來源；S&P 500 拒絕 SpaceX 破例（HN 935）、Anthropic IPO 進展與 Salesforce 停招工程師、遞歸自我改進全球媒體延燒 Day 2、v2.1.167、Python SDK v0.106.0 棄用 Opus 4.1、7 款新工具、ClaudeBot 爬蟲爭議、OpenTelemetry 揭露）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.167；更新最新版本與現況描述；更新最後更新 2026-06-06
  - `topics/anthropic-business.md`：新增 2026-06-06 時序（S&P 500 拒絕/Salesforce 停招/5 億帳單/AI 成本工具熱潮）；更新最後更新 2026-06-06
  - `topics/recursive-self-improvement.md`：新增 2026-06-06 時序（The Intercept 投資者批評、媒體持續延燒）；更新最後更新 2026-06-06
  - `topics/enterprise-tool-tracker.md`：新增 Salesforce 企業列；新增 2026-06-06 時序；更新最後更新 2026-06-06
  - `topics/community-tech-tools.md`：新增 7 個工具（Lich / Zedra / Gito v4.1.0 / Local MCP / Busbar / Lazarus / Sandfence）；更新最後更新 2026-06-06
  - `topics/community-tech-discussions.md`：熱門討論 prepend 5 條（HN 反 AI 情緒 / AI 成本優化 / Sub-agent 記憶 / OpenTelemetry 揭露 / /clear vs /exit）；技術彙整新增 3 條；更新最後更新 2026-06-06
  - `topics/ai-agent-safety.md`：新增 2026-06-06 時序（MITRE 後續分析、ClaudeBot 爬蟲爭議）；更新最後更新 2026-06-06
  - `feature-radar.md`：新增 v2.1.167（🔥 ✅）、Python SDK v0.106.0 棄用 Opus 4.1（🔥 ✅）；更新最後更新 2026-06-06
  - `wiki/index.md`：更新頁面數與最後更新 2026-06-06
- 新增頁面：無（今日事件均為既有頁面延伸）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過（版本表更新，現況描述最新）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend）|
  | topics/recursive-self-improvement.md | ✅ 通過（時序 prepend）|
  | topics/enterprise-tool-tracker.md | ✅ 通過（Salesforce 列新增，時序 prepend）|
  | topics/community-tech-tools.md | ✅ 通過（7 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（5 條 prepend + 3 條技術彙整）|
  | topics/ai-agent-safety.md | ✅ 通過（時序 prepend）|
  | feature-radar.md | ✅ 通過（全覽表更新）|
- 本日新增工具：Lich / Zedra / Gito v4.1.0 / Local MCP / Busbar / Lazarus / Sandfence（共 7 個，累積 168 個）
- feature-radar 更新：v2.1.167（🔥 ✅）、Python SDK v0.106.0 棄用 Opus 4.1（🔥 ✅）

---

## 2026-06-05 Ingest | news/2026-06-05.md

- 來源日報：`news/2026-06-05.md`（88 則，6 來源；遞歸自我改進報告 HN 477、NSA 使用 Mythos 攻擊（FT）、全球 AI 暫停呼籲全媒體覆蓋、Zcash 漏洞 ZEC-30%、v2.1.165、Skills 官方指南、FirstDraft/Claude-o-meter/Resume 3 工具）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.165；更新最後更新 2026-06-05
  - `entities/mythos.md`：新增 NSA Mythos 攻擊（FT）、Zcash 漏洞 ZEC-30%、開源防禦框架；更新最後更新 2026-06-05
  - `topics/anthropic-business.md`：新增 2026-06-05 時序（遞歸自我改進、白宮緩和、Daniela Amodei）；更新最後更新 2026-06-05
  - `topics/anthropic-government-policy.md`：新增 2026-06-05 時序（NSA Mythos 攻擊、白宮緩和、Hegseth 確認、暫停呼籲）；更新最後更新 2026-06-05
  - `topics/ai-agent-safety.md`：新增 2026-06-05 時序（遞歸自我改進報告、開源防禦框架、MCP 安全問題）；更新最後更新 2026-06-05
  - `topics/community-tech-tools.md`：新增 3 個工具（FirstDraft / Claude-o-meter / Resume）；更新最後更新 2026-06-05
  - `topics/community-tech-discussions.md`：熱門討論 prepend（遞歸自我改進 + IPO 矛盾，🔥🔥🔥🔥🔥）；更新最後更新 2026-06-05
  - `feature-radar.md`：新增 v2.1.165（🔥 ✅）；更新最後更新 2026-06-05
  - `wiki/index.md`：新增 topics/recursive-self-improvement；頁面數 35→36；更新最後更新 2026-06-05
- 新增頁面：`topics/recursive-self-improvement.md`（AI 遞歸自我改進與全球暫停呼籲）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | topics/recursive-self-improvement.md | ✅ 通過（新建，摘要清晰，指標表緊接摘要）|
  | entities/mythos.md | ✅ 通過（新增段落，獨立可讀）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend）|
  | topics/anthropic-government-policy.md | ✅ 通過（時序 prepend）|
  | topics/ai-agent-safety.md | ✅ 通過（時序 prepend）|
  | topics/community-tech-tools.md | ✅ 通過（3 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（1 條 prepend）|
  | feature-radar.md | ✅ 通過（全覽表更新）|
- 本日新增工具：FirstDraft / Claude-o-meter / Resume（共 3 個，累積 161 個）
- feature-radar 更新：v2.1.165（🔥 ✅）

---

## 2026-06-04 Ingest | news/2026-06-04.md

- 來源日報：`news/2026-06-04.md`（70 則，6 來源；"We contain Claude" 工程博文 HN 173、v2.1.162 waitingFor 可見性、Microsoft AI 主管批 Anthropic 太貴、AI 網路威脅 MITRE 報告、生物武器聯署信、Boxes.dev/agent-browser-shield/Ano 等 5 款新工具）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.162（waitingFor、--tools Grep/Glob）；更新最後更新 2026-06-04
  - `entities/mythos.md`：新增 ICE 加入 Glasswing；更新最後更新 2026-06-04
  - `topics/anthropic-business.md`：新增 2026-06-04 時序（盈利質疑、Microsoft 嫌貴、流量增長）；更新最後更新 2026-06-04
  - `topics/enterprise-tool-tracker.md`：新增 2026-06-04 時序（Microsoft AI 主管批 Anthropic 定價）；更新最後更新 2026-06-04
  - `topics/ai-agent-safety.md`：新增 2026-06-04 時序（"contain Claude" 工程博文、MITRE ATT&CK 報告、生物武器聯署信）；更新最後更新 2026-06-04
  - `topics/community-tech-tools.md`：新增 5 個工具（Boxes.dev / agent-browser-shield / Ano / Nori-skillsets / AI Gauge）；更新最後更新 2026-06-04
  - `topics/community-tech-discussions.md`：熱門討論新增 2 條（Skills 18% overhead / "contain Claude" HN 173）；更新最後更新 2026-06-04
  - `feature-radar.md`：新增 v2.1.162（🔥🔥 ✅）；更新最後更新 2026-06-04
  - `wiki/index.md`：更新最後更新 2026-06-04
- 新增頁面：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過 |
  | entities/mythos.md | ✅ 通過 |
  | topics/anthropic-business.md | ✅ 通過 |
  | topics/enterprise-tool-tracker.md | ✅ 通過 |
  | topics/ai-agent-safety.md | ✅ 通過（時序 prepend）|
  | topics/community-tech-tools.md | ✅ 通過（5 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（2 條 prepend）|
  | feature-radar.md | ✅ 通過 |
- 本日新增工具：Boxes.dev / agent-browser-shield / Ano / Nori-skillsets / AI Gauge（共 5 個，累積 158 個）
- feature-radar 更新：v2.1.162（🔥🔥 ✅ agent 監控可見性）

---

## 2026-06-03 Ingest | news/2026-06-03.md

- 來源日報：`news/2026-06-03.md`（76 則，6 來源；Services Track + Partner Hub 發布、Glasswing 假陽性首批反饋、Uber 用量上限確認、v2.1.161 OTEL 改善、CLAUDE.md 團隊一致性問題、Claudinho/100cc/Lovie 等 6 款新工具）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.161（OTEL metrics 標籤、claude agents 改善）；更新最後更新 2026-06-03
  - `entities/mythos.md`：新增 2026-06-03 Glasswing 假陽性反饋（HN 176 一手帳號）、Daniela Amodei「很擅長網路戰」聲明；更新最後更新 2026-06-03
  - `topics/anthropic-business.md`：新增 2026-06-03 時序（Services Track、Harvard Law 治理論文、Uber 用量管制）；更新最後更新 2026-06-03
  - `topics/enterprise-tool-tracker.md`：新增 2026-06-03 時序（Bloomberg 確認 Uber 用量上限）；更新最後更新 2026-06-03
  - `topics/community-tech-tools.md`：新增 6 個工具（Claudinho / 100cc / Lovie MCP / Chatcode / LiteHarness / deep-review）；更新最後更新 2026-06-03
  - `topics/community-tech-discussions.md`：熱門討論新增 3 條（Agent Loop 1400 行 / 排程 agent 靜默失敗 / 5 個矛盾 CLAUDE.md）；更新最後更新 2026-06-03
  - `feature-radar.md`：新增 v2.1.161（🔥🔥 ✅）；更新最後更新 2026-06-03
  - `wiki/index.md`：更新最後更新 2026-06-03
- 新增頁面：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過（版本更新，格式一致）|
  | entities/mythos.md | ✅ 通過（新增段落，可獨立閱讀）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend，摘要清晰）|
  | topics/enterprise-tool-tracker.md | ✅ 通過（時序 prepend）|
  | topics/community-tech-tools.md | ✅ 通過（6 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（3 條 prepend）|
  | feature-radar.md | ✅ 通過（全覽表更新）|
- 本日新增工具：Claudinho / 100cc / Lovie MCP / Chatcode / LiteHarness / deep-review（共 6 個，累積 153 個）
- feature-radar 更新：v2.1.161（🔥🔥 ✅ 企業可觀測性）

---

## 2026-06-02 Ingest | news/2026-06-02.md

- 來源日報：`news/2026-06-02.md`（101 則，6 來源；Anthropic IPO S-1 提交、Project Glasswing 擴展至 150 組織、IPO 同日宕機、637 npm 供應鏈攻擊植入 Claude Code hook、v2.1.160 安全修復 + breaking change）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.160（shell 安全修復 + `workflow`→`ultracode` breaking change）；更新最後更新 2026-06-02
  - `entities/mythos.md`：新增 2026-06-02 Glasswing 擴展（150 新組織/15+國家，10K+ 漏洞，6-12 月公開承諾）、ARC-AGI-3 SOTA；更新最後更新 2026-06-02
  - `topics/anthropic-business.md`：新增 2026-06-02 時序（IPO S-1、宕機、企業反彈、Snowflake/IB 新合作）；更新最後更新 2026-06-02
  - `topics/enterprise-tool-tracker.md`：新增 2026-06-02 時序（Microsoft 退出多媒體確認、Uber 燒完預算）；更新最後更新 2026-06-02
  - `topics/ai-agent-safety.md`：新增 2026-06-02 時序（637 npm 供應鏈攻擊 hook 植入、v2.1.160 修復、Claude Code Flaw）；更新最後更新 2026-06-02
  - `topics/community-tech-tools.md`：新增 4 個工具（DepsGuard / NUA / Tok / Circus Chief）；更新最後更新 2026-06-02
  - `topics/community-tech-discussions.md`：熱門討論新增 2 條（AI 求職垃圾郵件 HN 627 / 74 skills 劇場）；更新最後更新 2026-06-02
  - `feature-radar.md`：全覽表新增 v2.1.160（🔥🔥🔥 ✅ ⚠️ Breaking）；更新最後更新 2026-06-02
  - `wiki/index.md`：更新最後更新 2026-06-02
- 新增頁面：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過（版本更新，breaking change 明確標示）|
  | entities/mythos.md | ✅ 通過（新增段落，獨立可讀）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend）|
  | topics/enterprise-tool-tracker.md | ✅ 通過（時序 prepend）|
  | topics/ai-agent-safety.md | ✅ 通過（時序 prepend，按日期插入正確位置）|
  | topics/community-tech-tools.md | ✅ 通過（4 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（2 條 prepend）|
  | feature-radar.md | ✅ 通過（全覽表更新）|
- 本日新增工具：DepsGuard / NUA / Tok / Circus Chief（共 4 個，累積 147 個）
- feature-radar 更新：v2.1.160（🔥🔥🔥 ✅，⚠️ Breaking: workflow→ultracode）

---

## 2026-06-01 Ingest | news/2026-06-01.md

- 來源日報：`news/2026-06-01.md`（66 則，6 來源；Mythos 開放 ENISA 存取、Anthropic/OpenAI 政治獻金、IPO 競賽、客戶用 Claude 取代開發者、Ouijit/Agents CLI/Agentpack/DashVox 四款新工具）
- 更新頁面：
  - `entities/mythos.md`：新增 2026-06-01 EU/ENISA 部署、英國銀行遭拒、The Information 預算殺手報導；更新最後更新 2026-06-01
  - `entities/claude-code.md`：新增 v2.1.159（基礎設施更新）；更新最後更新 2026-06-01
  - `topics/anthropic-business.md`：新增 2026-06-01 時序（IPO 競賽 / 估值質疑 / Mythos 商業化）；更新最後更新 2026-06-01
  - `topics/anthropic-government-policy.md`：新增 2026-06-01 時序（Mythos EU 部署 / 政治獻金）；更新最後更新 2026-06-01
  - `topics/community-tech-tools.md`：新增 4 個工具（Ouijit / Agents CLI / Agentpack / DashVox）；更新最後更新 2026-06-01
  - `topics/community-tech-discussions.md`：熱門討論新增 2 條（客戶替換開發者 / AI 成本裁員藉口）；技術彙整新增 1 個段落；更新最後更新 2026-06-01
  - `feature-radar.md`：全覽表新增 v2.1.159；更新最後更新 2026-06-01
  - `wiki/index.md`：更新最後更新 2026-06-01
- 新增頁面：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/mythos.md | ✅ 通過（新增段落，獨立可讀）|
  | entities/claude-code.md | ✅ 通過（版本更新，格式一致）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend）|
  | topics/anthropic-government-policy.md | ✅ 通過（時序 prepend）|
  | topics/community-tech-tools.md | ✅ 通過（4 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（2 條 prepend，技術彙整 prepend）|
  | feature-radar.md | ✅ 通過（全覽表更新）|
- 本日新增工具：Ouijit / Agents CLI / Agentpack / DashVox（共 4 個，累積 143 個）
- feature-radar 更新：v2.1.159（🔥 ✅）

---

## 2026-05-31 Ingest | news/2026-05-31.md

- 來源日報：`news/2026-05-31.md`（50 則，5/6 來源；Anthropic $965B Series H 超越 OpenAI、"We contain Claude" 工程部落格、Opus 4.8 Thinking 900K context drain、ultracode 70 agent 實測、Claude Code Source Deep Dive VI & VII）
- 更新頁面：
  - `entities/opus-4-8.md`：新增 Thinking 40–60 倍 context drain（900K cache tokens/turn）；ultracode 70 agent 4 階段 pipeline 實測；更新歷史記錄；更新最後更新 2026-05-31
  - `topics/anthropic-business.md`：新增 2026-05-31 時序（"We contain Claude" 工程部落格 + Bloomberg 責任創新平衡報導）；更新最後更新 2026-05-31
  - `topics/community-tech-tools.md`：新增 4 個工具（claude-code-proxy / Lite-Harness / Arch-Decision / claude-skills）；更新最後更新 2026-05-31
  - `topics/community-tech-discussions.md`：熱門討論新增 4 條（Thinking context drain / 自動模型路由需求 / 10 Plugin 成本 / Progressive Disclosure 三層架構）；更新最後更新 2026-05-31
  - `feature-radar.md`：更新最後更新 2026-05-31（Thinking drain 量化確認）
  - `wiki/index.md`：更新最後更新 2026-05-31
- 新增頁面：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/opus-4-8.md | ✅ 通過（新增負面紀錄，歷史記錄格式一致）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend，結構清晰）|
  | topics/community-tech-tools.md | ✅ 通過（4 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（熱門討論 prepend，格式符合）|
  | feature-radar.md | ✅ 通過（僅更新最後更新欄位）|

---

## 2026-05-30 Ingest | news/2026-05-30.md

- 來源日報：`news/2026-05-30.md`（76 則，6 來源；v2.1.158 Auto mode 擴展 Bedrock/Vertex/Foundry、UltraCode 1.7M token bug、Anthropic 削減未授權平台清單、Mythos exploit eval 正式發布、Wired Chris Olah 長文）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.158（Auto mode on Bedrock/Vertex/Foundry）；更新最後更新 2026-05-30
  - `entities/opus-4-8.md`：新增 UltraCode 1.7M token bug、Qwen distillation 爭議、德語品質退步；更新歷史記錄；更新最後更新 2026-05-30
  - `entities/mythos.md`：新增 2026-05-30 exploit eval 正式發布（red.anthropic.com）；更新最後更新 2026-05-30
  - `entities/chris-olah.md`：新增 Wired 長文《The Vatican's Man Inside Anthropic》段落；更新最後更新 2026-05-30
  - `topics/anthropic-business.md`：新增 2026-05-30 時序（Anthropic 削減未授權平台清單）；更新最後更新 2026-05-30
  - `topics/community-tech-tools.md`：新增 3 個工具（claude-handoff-guard / cartographer-skill / dotpi）；更新最後更新 2026-05-30
  - `topics/community-tech-discussions.md`：熱門討論新增 3 條（UltraCode bug / Qwen 爭議 / AI 社會模擬）；技術彙整新增 2 個段落；更新最後更新 2026-05-30
  - `feature-radar.md`：全覽表新增 v2.1.158（🔥🔥 ✅）；Dynamic Workflows 降級為 ❌（UltraCode bug）；更新最後更新 2026-05-30
- 新增頁面：無
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/claude-code.md | ✅ 通過（版本更新，格式一致）|
  | entities/opus-4-8.md | ✅ 通過（負面清單補充，結構清晰）|
  | entities/mythos.md | ✅ 通過（新增段落，不影響現有結構）|
  | entities/chris-olah.md | ✅ 通過（新增段落，獨立可讀）|
  | topics/anthropic-business.md | ✅ 通過（時序 prepend，摘要無需更新）|
  | topics/community-tech-tools.md | ✅ 通過（3 工具插入表頭）|
  | topics/community-tech-discussions.md | ✅ 通過（熱門討論 prepend，技術彙整 prepend）|
  | feature-radar.md | ✅ 通過（全覽表更新，試用價值降級有說明）|
- 本日新增工具：claude-handoff-guard / cartographer-skill / dotpi（共 3 個，累積 139 個）
- feature-radar 更新：v2.1.158（🔥🔥 ✅）、Dynamic Workflows 降級（❌ UltraCode bug）

---

## 2026-05-29 Ingest | news/2026-05-29.md

- 來源日報：`news/2026-05-29.md`（97 則，6 來源；Claude Opus 4.8 發布 HN 1662、$65B Series H 融資 $965B 估值、Dynamic Workflows Research Preview、Claude Code v2.1.156 修復 thinking blocks 400 錯誤、Andrej Karpathy 確認加入 Anthropic + Eureka Labs 解散、MarginLab SWE-bench-Pro 追蹤發現升版前效能下降）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.156（修復 Opus 4.8 thinking blocks 400 錯誤）；更新最後更新 2026-05-29
  - `entities/opus-4-8.md`：**新建頁面**，Opus 4.8 完整發布細節、Dynamic Workflows、Fast Mode、社群初期反映
  - `entities/mythos.md`：新增 2026-05-29 Reuters 確認「Mythos 數週內公開推出」；更新最後更新 2026-05-29
  - `entities/andrej-karpathy.md`：確認加入 Anthropic（移除待核實標注）；補充 Eureka Labs 解散；新增 2026-05-29 歷史記錄；更新最後更新 2026-05-29
  - `topics/anthropic-business.md`：更新摘要與指標表（估值 $965B、ARR $47B、$65B Series H）；戰略合作新增 Samsung/SK Hynix、Apollo/Blackstone；新增 2026-05-29 時序；更新最後更新 2026-05-29
  - `topics/code-quality-decline.md`：新增 2026-05-29 時序（MarginLab 升版前效能下降、thinking blocks 400 錯誤、4.8 行為退步投訴）；更新最後更新 2026-05-29
  - `feature-radar.md`：全覽表新增 Opus 4.8（🔥🔥🔥🔥🔥 ⚡）、Dynamic Workflows（🔥🔥🔥🔥 ⏳）、v2.1.156（🔥🔥 ✅）；最新功能新增 Opus 4.8 + Dynamic Workflows + Fast Mode 完整條目；更新最後更新 2026-05-29
  - `topics/community-tech-tools.md`：新增 4 個工具（AISlop / ktx / Headroom / OpenHive）；更新最後更新 2026-05-29
  - `wiki/index.md`：新增 entities/opus-4-8；頁面數 34→35；更新最後更新 2026-05-29
- 新增頁面：`entities/opus-4-8.md`（1 個）
- 呈現品質審查：
  | 頁面 | 結果 |
  |------|------|
  | entities/opus-4-8.md | ✅ 通過（新建，摘要清晰，熱度表緊接摘要）|
  | entities/claude-code.md | ✅ 通過（版本更新，格式一致）|
  | entities/mythos.md | ✅ 通過（新增段落，不影響現有結構）|
  | entities/andrej-karpathy.md | ✅ 通過（狀態更新，歷史記錄補充）|
  | topics/anthropic-business.md | ✅ 通過（指標表更新，時序 prepend）|
  | topics/code-quality-decline.md | ✅ 通過（時序 prepend）|
  | feature-radar.md | ✅ 通過（新功能置頂，格式一致）|
  | topics/community-tech-tools.md | ✅ 通過（4 工具插入表頭）|
- 本日新增工具：AISlop / ktx / Headroom / OpenHive（共 4 個，累積 136 個）
- feature-radar 更新：Opus 4.8（🔥🔥🔥🔥🔥 ⚡）、Dynamic Workflows（🔥🔥🔥🔥 ⏳ Research Preview）、v2.1.156（🔥🔥 ✅）

---

## 2026-05-28 Query | 建立 topics/anthropic-business.md

- 新增頁面：`topics/anthropic-business.md`（Anthropic 商業健康度）
  - 內容範圍：企業採用率（34.4% Ramp AI Index）、PMF 觀察（Simon Willison HN 970）、財務信號（17 倍訂閱補貼）、商業風險（Microsoft 退出）、戰略合作（富士通/KPMG）
  - 來源整合自：news/2026-05-28、news/2026-05-27、news/2026-05-25、news/2026-05-23、news/2026-05-15、news/2026-05-13
- 更新頁面：
  - `topics/community-tech-discussions.md`：Simon Willison PMF 條目 `衍生` 欄補上 `[[topics/anthropic-business]]`
  - `wiki/index.md`：新增 topics/anthropic-business，頁面數 33→34

---

## 2026-05-28 Ingest | news/2026-05-28.md

- 來源日報：`news/2026-05-28.md`（75 則，6 來源；Simon Willison HN 970 PMF 論述、Anthropic 米蘭辦公室、Claude Code v2.1.153、Cisco LLM Security Leaderboard Anthropic 8/10、企業預算壓力密集信號、SpaceX Colossus 6 個月短期租約澄清、ChatGPT-5.5 DeepSWE 超越 Opus 4.7）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.153（skipLfs + npm 版本通知）至最新版本表格與版本歷史；更新最後更新 2026-05-28
  - `entities/claude-security.md`：新增 2026-05-28 Cisco LLM Security Leaderboard（Anthropic 8/10）；更新參考來源；更新最後更新 2026-05-28
  - `topics/community-tech-tools.md`：新增 6 個工具（NotifAI、Workplane、CCW、harmont-cli、Zorilla、token-xray）；更新 Token 成本不透明痛點至 2026-05-28；更新最後更新 2026-05-28
  - `topics/enterprise-cost-management.md`：新增 2026-05-28 時序（Benzinga/CFO.com 預算放緩、Reddit Uber 分析、$200 方案 17× 補貼）；更新最後更新 2026-05-28
  - `topics/community-tech-discussions.md`：熱門討論新增 Simon Willison PMF（HN 970，🔥🔥🔥🔥🔥 ☄️閃現）；技術彙整新增 PMF 條目；更新最後更新 2026-05-28
  - `feature-radar.md`：全覽表新增 v2.1.153 skipLfs 條目（🔥 ⚡）；更新最後更新 2026-05-28
- 新增頁面：無
- 呈現品質：✅ 通過（所有更新頁面摘要清晰，關鍵資訊前置）
- feature-radar 更新：v2.1.153 加入全覽表（低熱度，實用性 ⚡ 有條件推薦）
- 本日新增工具：NotifAI / Workplane / CCW / harmont-cli / Zorilla / token-xray（共 6 個，累積 132 個）

---

## 2026-05-27 Ingest | news/2026-05-27.md

- 來源日報：`news/2026-05-27.md`（86 則，6 來源；Claude Code v2.1.152 Coordinator 模式、Anthropic 韓國首爾辦公室、富士通戰略合作、Uber COO 25% 生產力確認、Bloomberg 企業不安報導、Boris Cherny Platformer 專訪）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.152（Coordinator 模式 + `/code-review --fix` + Worker 代理人指令 +4,566 tokens）；版本歷史新增 2026-05-27 條目；更新最後更新 2026-05-27
  - `entities/boris-cherny.md`：新增「軟體工程師的終結」Platformer 專訪（2026-05-27）；更新最後更新 2026-05-27
  - `entities/mythos.md`：新增印度政府測試 Mythos 政府網路安全計畫（首個主權政府採用案例）；更新最後更新 2026-05-27
  - `topics/enterprise-tool-tracker.md`：Uber 備註更新（COO 確認 25% 生產力）；新增 Fujitsu、Travelport、Nimble Gravity 三個企業條目；Claude API 採用數 4→7；新增 2026-05-27 時序；更新最後更新 2026-05-27
  - `topics/community-tech-tools.md`：新增 9 個工具（Minicor、claude-handoff-revive、STAX IDE、claude-workflow-composer、Vibeshub、timeglass.ai、KittyHTML、Claude Usage Tray、ADHDStack）；更新 3 個痛點洞察近期工具至 2026-05-27；更新最後更新 2026-05-27
  - `feature-radar.md`：新增 Coordinator 模式 + `/code-review --fix`（v2.1.152，熱度 🔥🔥🔥🔥，試用價值 ✅）；全覽表新增條目；更新最後更新 2026-05-27
- 新增頁面：無
- 呈現品質：✅ 通過（所有更新頁面前段清晰，關鍵資訊可獨立閱讀）
- feature-radar 更新：新增 Coordinator 模式 + `/code-review --fix` 功能條目
- 本日新增工具：Minicor / claude-handoff-revive / STAX IDE / claude-workflow-composer / Vibeshub / timeglass.ai / KittyHTML / Claude Usage Tray / ADHDStack（共 9 個，累積 126 個）

---

## 2026-05-26 Ingest | news/2026-05-26.md

- 來源日報：`news/2026-05-26.md`（83 則，6 來源；Pope Leo XIV 封論梵蒂岡事件、Mythos 公開釋出確認、Notion 整合三大 AI 編碼工具、企業安全整合 28 項、MCP 優化工具湧現）
- 更新頁面：
  - `entities/mythos.md`：狀態更新為「公開化中」；新增 05/26 媒體密集報導（Help Net Security 10K / eWeek 23K / PYMNTS / Techzine）與 The Register + Gotrade + CyberSecurityNews 三方確認公開釋出；更新最後更新 2026-05-26
  - `entities/claude-security.md`：新增 05/26 Varonis Claude Compliance API 整合（AI 治理 + 資料存取合規）、Forcepoint 延伸至 Claude Enterprise、Anthropic 28 項企業安全整合；更新最後更新 2026-05-26
  - `topics/community-tech-tools.md`：新增 5 個工具（skills-for-humanity、PrismCat、Agent Launch、AWO、AI Agent Token Cost Calculator）；更新痛點洞察表（Token 成本不透明、多 agent 協調混亂）；總工具數：117；更新最後更新 2026-05-26
  - `topics/community-tech-discussions.md`：新增 4 條熱門討論（Claude Code 效能衰退量化、Trading Peace for Pace、軟體工廠時機辯論、非技術 Vibecoding）；新增 2 個技術彙整段落（OpenTelemetry 量化、Trading Peace 情緒代價）；更新最後更新 2026-05-26
  - `topics/anthropic-government-policy.md`：新增梵蒂岡封論事件（Chris Olah 出席 Magnifica Humanitas 揭幕）；更新時序；狀態改為 monitoring；更新最後更新 2026-05-26
  - `feature-radar.md`：本日無新使用者端功能；BioMysteryBench 為研究評測發布；更新最後更新 2026-05-26
- 新增頁面：
  - `entities/chris-olah.md`：Anthropic 共同創辦人、梵蒂岡演講事件、可解釋性研究背景
- 呈現品質：✅ 通過（所有更新頁面前段清晰，關鍵資訊可獨立閱讀）
- feature-radar 更新：本日無新功能條目新增
- 本日新增工具：skills-for-humanity / PrismCat / Agent Launch / AWO / AI Agent Token Cost Calculator（共 5 個，累積 117 個）

---

## 2026-05-26 手動建頁 | enterprise-tool-tracker

- 新增頁面：`topics/enterprise-tool-tracker.md`（大型企業 AI 編碼工具使用追蹤）
- 初始資料：10 家企業、4 個工具、含市場分層觀察
- 加入 `wiki/CLAUDE.md` 觸發規則（企業工具採用新聞 → 自動更新此頁）
- 更新 `wiki/index.md`（頁面數 31→32）

---

## 2026-05-25 Ingest | news/2026-05-25.md

- 來源日報：`news/2026-05-25.md`（70 則，6 來源；Claude Code v2.1.150 遠端注入披露、Mythos Exploit Eval 論文正式發布、Microsoft 宣布 6/30 完全停用 Claude Code、MCP 帳單 73% 來自工具調用）
- 更新頁面：
  - `entities/mythos.md`：新增 Exploit Eval 論文正式發布（red.anthropic.com/2026/exploit-evals/）；UK AISI 6/10 企業網絡接管測試數據；Politico 議會閉門簡報；The Register 公開化路線確認；更新最後更新 2026-05-25
  - `entities/claude-code.md`：更新 v2.1.150 版本歷史，加入遠端系統提示注入爭議（Bootstrap API + GrowthBook tengu_heron_brook flag）；更新最後更新 2026-05-25
  - `topics/ai-agent-safety.md`：新增 Claude Code v2.1.150 遠端系統提示注入機制披露（Bootstrap API + GrowthBook 60s 更新）至技術彙整；更新最後更新 2026-05-25
  - `topics/enterprise-cost-management.md`：Microsoft 章節更新為「完全停用（6 月 30 日）」；新增 MCP 工具調用 73% 隱性成本案例；更新最後更新 2026-05-25
  - `topics/community-tech-tools.md`：新增 2 個工具（archmcp、Smriti）；總工具數：112；更新最後更新 2026-05-25
  - `topics/community-tech-discussions.md`：新增 4 條熱門討論（遠端注入、Yabby、MCP 帳單 73%、TDD 60% 違規）；新增 4 個技術彙整段落；更新最後更新 2026-05-25
  - `feature-radar.md`：本日無新使用者端功能；更新最後更新 2026-05-25
- 呈現品質：✅ 通過（所有更新頁面前段清晰，關鍵數字可獨立閱讀）
- feature-radar 更新：本日無新功能條目新增
- 本日新增工具：archmcp / Smriti（共 2 個，累積 112 個）

---

## 2026-05-24 Ingest | news/2026-05-24.md

- 來源日報：`news/2026-05-24.md`（51 則，6 來源；Glasswing CVD 儀表板、小企業 Skills、Mythos string leak、JSONL session 知識化、cache miss 量化）
- 更新頁面：
  - `entities/mythos.md`：新增 CVD 儀表板正式上線（red.anthropic.com/2026/cvd/，281 專案/1,596 漏洞/97 修補）；新增 Mythos 準備登陸 Claude Code 與 Claude Security（app 字串洩露）；更新最後更新 2026-05-24
  - `entities/claude-security.md`：新增 2026-05-24 歷史記錄（Mythos string leak）；更新最後更新 2026-05-24
  - `topics/community-tech-tools.md`：新增 4 個工具（CC-Wiki、Fleet、aco-system、Claude Code CLI Web Terminal）；更新痛點洞察表（多 agent 協調更新至 05-24）；總工具數：110
  - `topics/community-tech-discussions.md`：新增 3 條熱門討論（cache miss 12.5x、686 skills 導航、JSONL session 知識化）；新增對應技術彙整段落；更新時序與參考來源
  - `topics/enterprise-cost-management.md`：更新現況表（加入 cache miss 12.5x 量化數據）；更新最後更新 2026-05-24
  - `feature-radar.md`：新增「小企業 Skills」條目（31 個官方 Skills，🔥🔥🔥 推薦）；更新最後更新 2026-05-24
- 呈現品質：✅ 通過（所有更新頁面前段清晰，關鍵數字可獨立閱讀）
- feature-radar 更新：已新增小企業 Skills 條目
- 本日新增工具：CC-Wiki / Fleet / aco-system / Claude Code CLI Web Terminal（共 4 個）

---

## 2026-05-24 工具目錄全面重構 | community-tech-tools

- 工具資格審查（依 2026-05-20 入選規則逐一評估全部 109 筆）：
  - 移除 `Snyk + Claude Code` — 商業公司整合公告，無 HN/Reddit 社群討論
  - 移除 `OpticOdds MCP` — 商業運動賠率 API，無公開 repo/demo，純廣告性工具
  - 移除 `TradingAgents Plugin` — 訂閱制付費服務，非社群開源工具
  - 保留其餘 106 個（均有 Show HN / Reddit / 多來源驗證）
- 頁面結構調整：
  - 將 `## 痛點洞察` 從頁尾移至 `## 指標說明` 之前（關鍵分析前置）
  - `## 指標說明` 新增類型清單與入選標準欄位
- 類型標籤標準化：原 40+ 種雜亂類型統一為 10 個類別（多 Agent / 記憶工具 / 費用監測 / 工作流 / 整合工具 / 搜尋/診斷 / 安全工具 / IDE/終端 / Skills / 其他）
- 採用欄格式統一：`⏳ 觀望中` 統一改為 `⏳`
- Web Reader 同步更新（app.js）：
  - 新增 `⚠️ 存疑` 篩選按鈕（原有統計但無法篩選）
  - 頁面載入時自動按採用狀態降序排列（✅ → ⚡ → ⏳ → ⚠️）
  - 修正找表邏輯：依欄位標題找工具表，避免誤用痛點洞察表
- 呈現品質：⚠️ 已修復（頁面結構重整、類型統一、關鍵資訊前置）
- 總工具數：106

---

## 2026-05-23 工具目錄清理 | community-tech-tools 品質審查

- 背景：依新制入選門檻（HN score ≥ 30 或評論 ≥ 5 / Show HN 自動入選 / 2+ 獨立來源）重新審查全部工具
- 移除 12 個不符標準的條目：
  - `lipstyk` — 無日期、無 URL、無可追蹤來源
  - `claude-anyteam` — 無日期、無 URL、無可追蹤來源
  - `Linear+Lanes MCP` — 無日期、無 URL、無可追蹤來源
  - `WezTerm 主題同步` — 無日期、無 URL（純設定技巧，非獨立工具）
  - `shipcheck` — 2026-05-17 日報無此工具記錄
  - `cv-claw` — 任何日報均無此工具記錄
  - `HiveTerm` — 僅出現在 2026-05-12 今日聚焦摘要，無專文、無 URL
  - `Mneme HQ` — 僅 dev.to 發布，無 HN/Reddit 討論
  - `QA Skills（24 個）` — 僅 dev.to 發布，無 HN/Reddit 討論
  - `Code Quest` — 無公開 URL，無 HN/Reddit 討論
  - `AI 命名一致性 OSS` — 僅 dev.to 發布，無 HN/Reddit 討論
  - `unitmux` — 僅 dev.to 發布，無 HN/Reddit 討論
- 同步更新：
  - `痛點洞察` 表格移除 HiveTerm 引用
  - `AI 輔助開發的長期副作用` 移除 `AI 命名一致性` 工具引用（保留概念描述）
- 總工具數：~108（移除後）

---

## 2026-05-22 Ingest | news/2026-05-22.md

- 來源日報：`news/2026-05-22.md`（36 則，含 v2.1.148、Managed Agents 自架沙箱文件、DeepSeek 全棧競品、$6,000 帳單事件、Karpathy 加入 Anthropic、多個新工具）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.148 版本表、更新 現況 最新版本、新增 2026-05-22 歷史記錄
  - `entities/managed-agents.md`：新增 2026-05-22 自架沙箱完整文件發布歷史記錄
  - `topics/competitor-landscape.md`：DeepSeek Clone 區塊升級為 DeepSeek 正式競品條目；新增 Alibaba Qwen3.7-Max；新增 2026-05-22 時序
  - `topics/community-tech-tools.md`：新增 11 個工具（Runtime、agent-teamflow、Runner、Proof Loop、agent-estimate、engramx、DPlex、Mneme HQ、ChunkHound v5.1、videowright、QA Skills）；更新痛點洞察表
  - `topics/community-tech-patterns.md`：新增 2026-05-22 時序（Spec-Driven Dev、agent fleet 5 步驟、CLAUDE.md 自我演化、Angular 13 規則、零 NPM 插件）
  - `topics/community-tech-discussions.md`：新增 3 個熱門討論（LLMs 虛假忙碌、逐行審查文化、CLAUDE.md 自我演化）；新增 2 個技術彙整條目
  - `topics/enterprise-cost-management.md`：新增 $6,000 個人事件案例；新增 Karpathy 最小 context 原則；新增 2026-05-22 時序
  - `wiki/feature-radar.md`：自架沙箱熱度升至 🔥🔥🔥🔥（文件完整發布）
- 新增 entities：`entities/andrej-karpathy.md`（Karpathy 加入 Anthropic，待官方核實）
- feature-radar 更新：自架沙箱完整文件發布，熱度升至 🔥🔥🔥🔥
- 呈現品質：
  - `entities/claude-code.md` ✅ 通過
  - `entities/managed-agents.md` ✅ 通過
  - `topics/competitor-landscape.md` ✅ 通過
  - `topics/community-tech-tools.md` ✅ 通過
  - `topics/community-tech-patterns.md` ✅ 通過
  - `topics/community-tech-discussions.md` ✅ 通過
  - `topics/enterprise-cost-management.md` ✅ 通過
  - `wiki/feature-radar.md` ✅ 通過
  - `entities/andrej-karpathy.md` ✅ 通過

---

## 2026-05-21 Lint

- 修正矛盾：無
- 補連結：無（project-deal.md 已於前次 session 補上連結，確認非孤立）
- 狀態更新：無（所有 ongoing/monitoring 頁面均在 14 天閾值內）
- 遷移至 entities：無
- 新增 entities：無
- 呈現品質：
  - `entities/opus-4-7.md` ⚠️ 已修復：「Claude Code 高 Token 模式」條目誤置於 ## 相關議題，已移至 ## 社群觀點
  - `topics/official-community-gap.md` ⚠️ 已修復：移除 LLM 操作指令「每次 ingest 後評估…」（移至 CLAUDE.md 規則）
  - `topics/ai-agent-safety.md` ⚠️ 已修復：合併 ## 技術彙整（新增）至主要 ## 技術彙整，消除重複標題
- 超長頁面（> 500 行）：`topics/community-tech-patterns.md`（682 行）— 使用者選擇稍後處理（📋 待辦）
- CLAUDE.md 健檢：
  - 行數：352 行（原 406 行，本次簡化後；閾值 150 行）
  - 矛盾：無
  - 引用驗證：`**靈感來源：**` 欄位在 community-tech-patterns.md 未找到 → 已修正規則說明（patterns.md 用主題段落格式，不需補此欄位）
  - 遵守率：呈現品質審查 0/3（log 未含標記）→ 已修正：新增 log.md 呈現品質欄位規定
  - 過期規則（> 60 天）：無（最舊規則 [加入: 2026-04-25] = 26 天）
  - 簡化：已執行（壓縮「快速上手」+ 「聚合器 Pipeline 架構」章節，節省 54 行）
- overview.md：已更新（2026-05-15 → 2026-05-21，涵蓋 Stainless 收購、deeplink RCE、.env SQLite 漏洞、Claude Design 上線）

---

## 2026-05-21 Ingest | news/2026-05-21.md

- 來源日報：`news/2026-05-21.md`（35 則，含 v2.1.146、sandbox bypass #2、Opus 退化、vibe-skill、SEO poisoning）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.146（/code-review 更名、auto mode AskUserQuestion）+ sandbox bypass #2 null byte + Opus 4.6 extended thinking 移除
  - `topics/ai-agent-safety.md`：新增 2026-05-21（sandbox bypass #2 + SEO poisoning EclecticIQ）
  - `topics/code-quality-decline.md`：新增 2026-05-21（Opus 3 週結構化記錄）
  - `topics/community-tech-tools.md`：新增 5 工具（atrium、clarp、vibe-skill、Claude Orchestra、the-knowledge-guy）+ 痛點洞察更新
  - `topics/community-tech-discussions.md`：HTML vs Markdown 熱度升至 🔥🔥🔥🔥🔥，模式改為 🌊延燒
  - `entities/pricing.md`：新增 2026-05-21（clarp、vibe-skill、atrium 等 6/15 應對方案）
  - `topics/competitor-landscape.md`：新增 2026-05-21（vibe-skill 多 LLM 分流 + DeepSeek harness 招募）
  - `topics/community-tech-patterns.md`：新增 2026-05-21 時序（vibe-skill、Claude Orchestra、atrium、the-knowledge-guy）
  - `wiki/feature-radar.md`：新增 /code-review 指令（v2.1.146）；HTML 熱度升至 🔥🔥🔥🔥🔥
- 呈現品質：
  - `entities/claude-code.md` ✅ 通過
  - `topics/ai-agent-safety.md` ✅ 通過
  - `topics/code-quality-decline.md` ✅ 通過
  - `topics/community-tech-tools.md` ✅ 通過
  - `topics/community-tech-discussions.md` ✅ 通過
  - `entities/pricing.md` ✅ 通過
  - `topics/competitor-landscape.md` ✅ 通過
  - `topics/community-tech-patterns.md` ✅ 通過
  - `wiki/feature-radar.md` ✅ 通過
- 新增 entities：無
- feature-radar 更新：已更新（/code-review 新增；HTML 熱度調升）

---

## 2026-05-20 Schema 升級 | community-tech-tools 表格重構

- 變更：`topics/community-tech-tools.md` 工具表格 schema 調整
  - 移除 `活躍` 欄（🟢/🟡/🔴 指標）：舊指標測量「最近是否出現在日報」，但常用工具本就不頻繁出現，導致全部顯示過期，設計缺陷
  - 新增 `首次出現` 欄（YYYY-MM-DD）：記錄工具首次進入 wiki 的日報日期，提供時間脈絡
  - 工具名稱新增可點擊連結：格式 `[**ToolName**](url)`，URL 從日報原文擷取；無 URL 者保持 `**ToolName**`
  - 移除重複的 Semble 條目（原在兩處出現，合併為一，首次出現更正為 2026-05-04）
- 更新：`CLAUDE.md` 新增 `community-tech-tools 工具新增規則` 章節，規範未來 ingest 時的工具欄格式（含 URL 取得方式、首次出現日期、採用初始值）
- 統計：共 ~90 個工具條目已完成格式更新；有 URL 的工具約 30 個，其餘填 `—` 待後續補充

---

## 2026-05-20 Ingest

- 來源日報：[[news/2026-05-20]]
- 更新頁面：
  - `entities/claude-code.md`（新增 v2.1.145；新增攝影機存取問題與 RCE deeplink 至已知問題；更新最後更新日期）
  - `entities/stainless.md`（重大更新：服務關閉公告；新增 Ironic 替代方案；更新狀態與歷史記錄）
  - `topics/ai-agent-safety.md`（新增 2026-05-20 時序：RCE deeplink 廣泛報導、攝影機存取議題持續；更新最後更新日期）
  - `entities/opus-4-7.md`（新增 2026-05-20：Claude Code max effort 優異 vs 一般對話體驗弱化分歧）
  - `topics/community-tech-tools.md`（新增 5 工具：TokenShield、Logbox、PrismoDev、claude-autopilot、mdviewer）
  - `topics/community-tech-patterns.md`（新增 2026-05-20 時序：engramx 89.1% token 減少、repo 架構護欄、35 agent 協調、multi-agent review 41% 不一致）
  - `topics/community-tech-discussions.md`（HTML vs Markdown 更新為 🌋重燃 + 熱度 +1；新增 multi-agent review 可靠性、auto-memory 副作用、skill creator economy 討論）
  - `entities/pricing.md`（新增 2026-05-20：Claude Code 定價溝通混亂事件 Simon Willison 分析）
  - `wiki/feature-radar.md`（新增 HTML 輸出官方背書、claude agents --json；更新全覽表）
- 新增頁面：無
- 摘要：今日最重要事件為 Stainless 收購後隨即宣布服務關閉（9 月停止對外服務，OpenAI/Google 等客戶急尋替代），Claude Code RCE deeplink 漏洞持續報導，Anthropic 官方 Blog 正式背書 HTML 取代 Markdown 作為 agent 輸出格式（設計策略轉向），claude agents --json 新增多層 agent 識別能力。社群工具爆發（TokenShield/Logbox/PrismoDev）聚焦 token 節省，multi-agent review 可靠性遭實測挑戰（41% 不一致）

---

## 2026-05-19 新頁面建立

- 新增頁面：`entities/stainless.md`
- 原因：Anthropic 宣布收購 Stainless（傳聞 $300M+），首次出現且為重大企業事件，具體業務（官方 SDK + MCP 伺服器生成）構成戰略基礎設施
- 更新：`wiki/index.md`（頁面數 26→27，新增目錄條目）

---

## 2026-05-19 Ingest

- 來源日報：[[news/2026-05-19]]
- 更新頁面：
  - `entities/stainless.md`（新建：Anthropic 收購 Stainless，$300M+，MCP 伺服器生成能力戰略意義）
  - `topics/ai-agent-safety.md`（新增 2026-05-19 時序：.env SQLite 明文、webcam 存取疑慮、RCE deeplink 跟進報導；新增技術彙整：.env SQLite 明文存儲；更新目前結論）
  - `entities/claude-code.md`（新增 v2.1.144；更新版本歷史 2026-05-19；更新最後更新日期）
  - `entities/managed-agents.md`（新增 2026-05-19：自架沙箱 + MCP 隧道；核心功能表格新增 4 項）
  - `entities/pricing.md`（新增 2026-05-19：臨時 5h x2 + 50% 週上限提升；企業成本壓力持續）
  - `topics/enterprise-cost-management.md`（新增 2026-05-19 時序：Microsoft 六個月內測揭露、企業帳單三倍 HN 討論；更新目前結論）
  - `topics/competitor-landscape.md`（新增 2026-05-19 時序：Microsoft 內部測試全貌 dev.to 深度揭露）
  - `topics/community-tech-tools.md`（新增 3 工具：Claude Soul、cdesktop、InsForge）
  - `topics/community-tech-patterns.md`（新增 2026-05-19 時序：1000h 工作流、SEO pipeline、Android 惡意軟體 RE、Anthropic 內部報告、新工具）
  - `topics/community-tech-discussions.md`（新增 3 討論：MCP context bloat 量化、Claude 隱藏 bug、靜默失敗五種模式；新增 MCP Context Bloat 技術彙整）
  - `wiki/feature-radar.md`（新增自架沙箱 + MCP 隧道 + /resume 兩個功能條目；更新全覽表）
- 新增頁面：`entities/stainless.md`
- 摘要：今日最重要事件為 Anthropic 收購 Stainless（$300M+，MCP 伺服器生成控制權），Claude Code 安全多面爆發（.env SQLite 明文、webcam 隱私、RCE deeplink 持續報導），Microsoft 六個月內部測試全貌揭露（開發者愛它但財務殺了它），Managed Agents 自架沙箱 + MCP 隧道企業功能上線。社群首次量化 MCP context bloat（9 伺服器 = 38k tokens），AI 工具可靠性問題（靜默隱藏 bug、靜默失敗）密集出現。

---

## 2026-05-18 新頁面建立

- 新增頁面：`topics/enterprise-cost-management.md`
- 原因：企業規模 Claude 成本管理議題跨越多天且升至財經媒體層級，現有 pricing.md（政策面）與 community-tech-patterns.md（個人工法面）均未覆蓋「企業採用成本結構挑戰」此角度
- 更新：`wiki/index.md`（頁面數 25→26，新增目錄條目）

---

## 2026-05-18 Ingest

- 來源日報：[[news/2026-05-18]]
- 更新頁面：
  - `topics/ai-agent-safety.md`（新增 2026-05-18 時序：Claude Code RCE via deeplink；新增技術彙整；更新目前結論）
  - `topics/competitor-landscape.md`（新增 2026-05-18 時序：Microsoft 遷移媒體確認、Uber 預算 Forbes 報導、Codex 超越文章、混搭工作流）
  - `entities/managed-agents.md`（新增 2026-05-18：Proactive Workflows + Capability Curve 官方公告）
  - `entities/pricing.md`（新增 2026-05-18：Uber 企業成本警示、Opus+Sonnet 混合策略）
  - `topics/community-tech-tools.md`（新增 6 工具：Semble、AnyFrame、Agetor、agent-baton、LockedIn、Claude Usage Widget）
  - `topics/community-tech-patterns.md`（新增 2026-05-18 時序：角色分工 6.7 倍加速、多操作員架構、速率上限轉移、62.5 分鐘 cache 規則、逆向工程惡意軟體）
  - `topics/community-tech-discussions.md`（新增 3 討論：/compact 設計決策遺忘、知識圖譜實際效益存疑、14 條反駁規則工具包）
  - `wiki/feature-radar.md`（新增 Proactive Workflows + Capability Curve 條目；更新全覽表）
- 新增頁面：無
- 摘要：今日最重要事件為 Claude Code RCE deeplink 漏洞（第三個 RCE 類漏洞）、Microsoft 遷移至 Copilot CLI 獲主流媒體確認、Uber 企業成本案例登上 Forbes、Proactive Workflows 官方公告。社群湧現 6 個新工具，聚焦速率監控與 Agent 沙盒。/compact 設計決策遺忘和知識圖譜效益存疑是本日最具反思價值的討論。

---

## 2026-05-17 Ingest（補充 2）

- 來源日報：[[news/2026-05-17]]
- 更新頁面：
  - `topics/community-tech-tools.md`（新增 4 個工具：machine、cv-claw、shipcheck、Gonfire；更新最後更新日期至 2026-05-17）
  - `topics/community-tech-patterns.md`（補充 2026-05-17 新工具列表：加入 machine、cv-claw、Gonfire）
- 新增頁面：無
- 摘要（補充 2）：工具目錄補入今日 Show HN 新工具——machine（per-project VM 安全隔離）、cv-claw（Skill 履歷生成器）、shipcheck（session log 費用與安全審計）、Gonfire（session log 面試評估）。

## 2026-05-17 Ingest（補充）

- 來源日報：[[news/2026-05-17]]
- 更新頁面（補充本次第一次 ingest 遺漏項目）：
  - `entities/claude-code.md`（補入：Anthropic API 500 Internal Server Error 已知問題、shipcheck 工具至費用監控列表、Gonfire 工具至工作流輔助列表、版本歷史 2026-05-17 補充條目）
  - `entities/opus-4-7.md`（新增 2026-05-17：Claude 4.7 vs 4.6 使用場景社群共識形成；更新最後更新日期）
  - `topics/competitor-landscape.md`（新增 2026-05-17 時序：Microsoft 授權取消 techbuzz.ai 報導 + Adobe Lightroom Linux 移植正向案例；更新最後更新日期）
- 新增頁面：無
- 摘要（補充）：Microsoft 授權取消故事由非主流媒體再度報導（可信度待核實）；Claude 4.7 vs 4.6 使用場景共識在社群清晰化（4.7=結構化任務，4.6=探索性寫作）；Anthropic API 500 跨模型服務中斷事件記錄；兩款 session log 分析新工具（shipcheck 安全審計、Gonfire 面試評估）補入工具目錄。

## 2026-05-17 Ingest

- 來源日報：[[news/2026-05-17]]
- 更新頁面：
  - `entities/claude-code.md`（新增 2026-05-17：Adobe Lightroom Linux 移植案例、持久性自主 agent 系統、Claude Skills 靜默覆蓋問題、context 管理 4 工具、多帳號合規紅線、shipcheck 新工具；更新最後更新日期）
  - `entities/pricing.md`（新增 2026-05-17：`claude -p` 計費衝擊持續、多帳號架構合規邊界明確）
  - `topics/community-tech-patterns.md`（新增 2026-05-17 時序：Skills-as-dotfiles + 子代理派生、Generator-Evaluator 12 輪對抗迭代、持久性自主 agent 系統、context 4 工具實踐、CSS 規格先行設計稿轉碼、100 平行 agent 行銷診斷、SSH + Claude Chat 伺服器存取、Grounded Code 方法論系列、Adobe Lightroom Linux 移植、shipcheck 新工具）
  - `topics/community-tech-discussions.md`（新增 CLAUDE.md/AGENTS.md 維護效益辯論、Claude Skills 靜默覆蓋兩個新討論；更新 Context 管理熱度 🔥🔥→🔥🔥🔥、模式 ☄️閃現→🌊延燒；新增 Skills 機制邊界技術彙整；新增 2026-05-17 時序）
  - `topics/official-community-gap.md`（新增 2026-05-17 Ingest 更新：Skills 透明度缺口新證據、CLAUDE.md 失效缺口持續驗證）
  - `wiki/feature-radar.md`（更新最後更新日期；本日無官方新功能發布）
- 新增頁面：無
- 摘要：Claude Skills 靜默覆蓋指令與子代理派生問題為本日最熱門技術議題，呼應官方社群缺口矩陣「CLAUDE.md 規則失效」欄位；CLAUDE.md/AGENTS.md 維護效益辯論（HN）引發廣泛共鳴；社群自主 agent 工程達高複雜度里程碑；context 管理 4 工具實踐廣泛流傳；多帳號 ToS 合規紅線明確。

---

## 2026-05-16 Ingest

- 來源日報：[[news/2026-05-16]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.143 plugin 依賴強制執行；GitHub Copilot 新應用競爭；Anthropic 尋找下一個突破性產品；新工具：Code Quest、CostHawk、AI 引用稽核 MCP、answering machine MCP；更新現況與版本歷史）
  - `entities/pricing.md`（新增 2026-05-16：Max 20x 用量上限未生效數學實證、社群促銷時序整理、Lanes.sh 影響範圍說明、費用焦慮集體高峰、週配額意外重置 bug、「credit 包裝漲價」批評）
  - `entities/managed-agents.md`（新增 2026-05-16 歷史記錄：dev.to Dreaming 機制深度技術分析）
  - `topics/competitor-landscape.md`（新增 2026-05-16 時序：GitHub Copilot 新應用明確對標 Claude Code、Anthropic 尋找下一個突破性產品；更新摘要）
  - `topics/community-tech-discussions.md`（新增「harness 變差了」辯論、Agentic RAG + eval harness 兩個新討論；更新熱門討論表格、技術彙整、時序）
  - `topics/community-tech-patterns.md`（新增 2026-05-16 時序：費用焦慮高峰、Custom base URL、Agentic RAG、X 演算法文件化、非工程師 MCP 六個月心得；新增 Code Quest / CostHawk 工具）
  - `wiki/feature-radar.md`（新增 v2.1.143 Plugin 依賴關係強制執行條目；更新全覽表）
- 新增頁面：無
- 摘要：Claude Code v2.1.143 plugin 依賴強制執行為最重要技術更新；GitHub Copilot 正面對標 Claude Code 是競品競爭升級訊號；6/15 計費後遺症延燒（Max 用量上限未生效數學實證、促銷透明度質疑、費用優化文章集中爆發）；「harness 變差了」論點為近期「Claude Code 退步感」提供結構性反論。

---

## 2026-05-15 Ingest

- 來源日報：[[news/2026-05-15]]
- 更新頁面：
  - `entities/pricing.md`（新增 2026-05-15：社群情緒分析（60% 負面）、第三方工具衝擊（Zed/Conductor/Superset）、Ars Technica 官方訪談、VS Code 計費歸屬不明、Ungate 工具 ToS 風險）
  - `entities/claude-code.md`（v2.1.142 `claude agents` 8 旗標；「Claude Code at Scale」官方大型 codebase 指南；Microsoft 取消內部授權；新工具 PlanBridge/my-time-has-come/Ungate；更新現況說明）
  - `topics/competitor-landscape.md`（新增 2026-05-15 時序：Microsoft 取消授權轉推 Copilot CLI；Anthropic 企業採用率首次超越 OpenAI（34.4% vs 32.3%）；第三方工具分化；摘要更新）
  - `topics/community-tech-patterns.md`（新增 2026-05-15 時序：MCP 麥克風語音整合/破壞性操作安全閘門/長期 auto-memory 品質管理/平行子代理成本分析/monk 靜默模式 skill/PlanBridge 行內評審/CLAUDE.md 精簡反思/Claude Code vs Cursor 比較）
  - `topics/ai-agent-safety.md`（新增 2026-05-15 時序：「Claude 刪除專案」安全閘門/長期記憶退化/35 天 ERP 靜默失敗模式）
  - `wiki/feature-radar.md`（新增 `claude agents` v2.1.142 細粒度旗標條目 🔥🔥；更新全覽表）
- 新增頁面：無
- 摘要：Anthropic 6/15 計費變更持續延燒（第三方工具分化、60% 社群負評、官方訪談補充說明）；Microsoft 取消內部 Claude Code 授權轉推 Copilot CLI 標誌企業市場首次正面競爭；Ramp AI Index 首次顯示 Anthropic 企業採用率超越 OpenAI（34.4% vs 32.3%）；社群大量湧現記憶管理、安全防護與 Token 節省工具。

---

## 2026-05-14 Ingest

- 來源日報：[[news/2026-05-14]]
- 更新頁面：
  - `entities/pricing.md`（2026-05-14 重大政策：6/15 起 programmatic 用量剝離訂閱方案，改為信用池（Pro $20 / Max 5x $100 / Max 20x $200），按完整 API 費率計費；週限制臨時提高 50% 至 7/13；claude-pee 繞過工具出現；開發者強烈反彈及轉換競品）
  - `entities/claude-code.md`（v2.1.141 terminalSequence + CLAUDE_CODE_PLUGIN_PRE；/loop・/batch・/background 官方文件上線；Cat Wu 訪問 AI 主動性論述；新工具：Ledger/Clawdmeter/Grafana Dashboard/agent-html-skills/Lanes v0.39；版本歷史 2026-05-14 兩條、2026-05-13 v2.1.141 一條）
  - `entities/openclaw.md`（狀態更新：受限→允許（信用池計費）；新增 2026-05-14 事件：恢復允許但改走信用池）
  - `wiki/feature-radar.md`（/goal 熱度升至 🔥🔥🔥🔥🔥；新增 /loop・/batch・/background 條目 🔥🔥🔥🔥；更新全覽表）
  - `topics/community-tech-patterns.md`（新增 2026-05-14 時序：費用可觀測性工具爆發/多 LLM 混合架構/claude-pee PTY 繞過/雙向 HTML 工件/週末 PoC/commit 學習技能；新增技術彙整：費用可觀測性工具、多 LLM 混合架構條目）
  - `topics/competitor-landscape.md`（新增 2026-05-14 時序：政策驅動分流 + 多 LLM 混合策略）
- 新增頁面：無
- 摘要：Anthropic 宣布 6/15 起 programmatic 用量全面剝離訂閱方案（信用池制）為最大事件，引發開發者強烈反彈、claude-pee 繞過工具誕生、多 LLM 混合策略討論加速；官方 /loop・/batch・/background 指令文件同步上線，標誌 Claude Code 正式轉向 agent 開發平台定位。

---

## 2026-05-13 Lint

- 修正矛盾：
  - `overview.md`：全面重寫（反映 2026-05-08 至 2026-05-13 共 5 天重大事件，原版停在 2026-05-08）；新增「功能試用推薦」快速查閱表格；更新競品數據（157K OpenCode）、算力到位（SpaceX Colossus 1）、安全事件（假冒安裝包 + 90% 漏洞評測）
- 補連結：
  - `entities/claude-security.md` → 新增頂部 feature-radar 熱度標籤（🔥🔥🔥 / ⚡）與 [[feature-radar]] 連結
  - `wiki/overview.md` → 在社群工具生態與功能試用推薦區塊補上 [[feature-radar]] 連結（共 2 處）
  - `topics/community-tech-patterns.md` → 確認已有 [[entities/claude-design]] 連結（lint 前已正確）
- 狀態更新：
  - `topics/anthropic-government-policy.md`：`ongoing` → `monitoring`（2026-05-02 至今 11 天無新進展，白宮談判狀態不明）
- 遷移至 entities：無
- 新增 entities：無（掃描所有頁面，無未建頁面被提及 3+ 次的新名稱）
- feature-radar.md 更新：
  - Agent View 條目補充 v2.1.140 `subagent_type` 不敏感匹配改善
  - Managed Agents 條目補充 Boris Cherny 數千子代理工作流（2026-05-13）
  - Claude Security 試用價值升級：⏳ 觀望 → ⚡ 有條件推薦（AI 生成程式碼 90% 漏洞評測確認資安審查需求，熱度 🔥🔥 → 🔥🔥🔥）
  - 全覽表 Claude Security 欄同步更新
- overview.md：已全面重寫（反映 2026-04-25 至 2026-05-13 局勢，含 agentic AI 生產化加速、安全信任多點爆發、分流訊號具體化）

---

## 2026-05-13 Ingest

- 來源日報：[[news/2026-05-13]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.140 subagent_type 大小寫不敏感匹配改善；Boris Cherny 數千個子代理工作流報導；Dragoman/Cocall.ai/Claudy macOS session 管理版/PullMD v2.4.1 新工具；AI 生成程式碼 90% 安全漏洞研究警示；版本歷史 2026-05-13 三條）
  - `entities/boris-cherny.md`（新增：每晚數千個 AI 子代理工作流公開報導（2026-05-13）；更新最後更新日期）
  - `entities/pricing.md`（新增：Anthropic 定價主導權強勁——The Information 報導企業客戶吸收成本上漲）
  - `entities/managed-agents.md`（現況補充 Boris Cherny 數千子代理工作流 + v2.1.140 改善；歷史記錄 2026-05-13）
  - `topics/ai-agent-safety.md`（新技術彙整三節：AI 生成程式碼 90% 安全漏洞評測 / 24 小時無監督 Agent 執行風險 / Context 壓縮安全指令保留；目前結論新增兩條；2026-05-13 時序三條）
  - `topics/community-tech-patterns.md`（新技術彙整五節：多模型路由 Dragoman / 電話 MCP Cocall.ai / Token Bloat 精簡策略 / 大規模子代理工作流 / AI 生成程式碼安全審查；熱門應用新增 Dragoman/Cocall.ai；2026-05-13 時序）
- 新增頁面：無
- 摘要：Claude Code 創始人 Boris Cherny 公開「數千個夜間子代理」工作流成為本週最受矚目的 agentic AI 案例；AI 生成程式碼安全漏洞大規模評測（48 應用 90% 有漏洞）直接挑戰快速開發上線假設；v2.1.140 的 subagent_type 大小寫不敏感匹配降低多代理配置摩擦；Anthropic 定價強勁（企業客戶吸收成本上漲）標誌市場競爭力持續擴大。

---

## 2026-05-13 Schema 升級 | Feature Radar 新增

- 新增頁面：`wiki/feature-radar.md`（功能熱度雷達，含熱度評分、試用推薦、快速上手指南）
- 更新頁面：`entities/managed-agents.md`（新增「熱度與試用價值」、「使用指南」區塊，包含 `/goal`、Agent View、Python/TypeScript SDK 範例）
- 更新 `wiki/index.md`（新增 feature-radar 入口，頁面數 21）
- 更新 `CLAUDE.md`（schema 新增 feature-radar 更新規則、feature entity 必填區塊規範）
- 摘要：建立功能熱度追蹤系統，未來每次 ingest 自動維護；已回填 2026-04-25 至 2026-05-12 期間共 13 項功能的熱度評分與試用推薦

---

## 2026-05-12 Ingest

- 來源日報：[[news/2026-05-12]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.139 Agent View + `/goal`；假冒安裝包 IElevator 攻擊；服務中斷；UiPath/Signadot 整合；ESP32 Fault Injection 研究；OpenCode 157K 分流；checkpoint commits 污染 git history 已知問題；新工具：HiveTerm/Writ/Agent FM/Usage4Claude 3.0.0/ltm；版本歷史 2026-05-12 四條）
  - `entities/pricing.md`（Ultra Review $100–140 vs $5–20 費用透明度爭議；Max 5x 正常月 $159 vs 高峰月 $6,600 ROI 分析；第三方平台 ToS 風險討論）
  - `entities/managed-agents.md`（Agent View + `/goal` 加入核心功能表；現況補充 v2.1.139 非同步工作流能力；歷史記錄 2026-05-12）
  - `topics/ai-agent-safety.md`（新技術彙整：假冒安裝包 IElevator 機制 + AI 驅動硬體 Fault Injection；目前結論新增兩條；2026-05-12 時序）
  - `topics/community-tech-patterns.md`（新技術彙整 5 節：/goal fire-and-forget/對抗性審查/Writ Neo4j Pipeline/ltm 跨環境記憶/Context 管理瓶頸/Checkpoint Commits；熱門應用新增：HiveTerm/Writ/Agent FM/Usage4Claude 3.0.0/ltm；2026-05-12 時序）
  - `topics/competitor-landscape.md`（OpenCode 157K 開發者數據更新；UiPath/Signadot 整合；摘要更新；2026-05-12 時序）
- 新增頁面：無
- 摘要：v2.1.139 的 Agent View + `/goal` 指令是 Claude Code 邁向真正非同步多 agent 工作流的關鍵里程碑；假冒安裝包（IElevator 機制）與 Google 廣告木馬並存，Claude Code 安裝路徑的供應鏈攻擊態勢持續升級；逾 15.7 萬開發者轉向 OpenCode 是目前最具體的競品分流量化數據；Ultra Review 費用透明度（$100–140 vs 宣傳的 $5–20）延續 Anthropic 計費信任危機；AI 驅動 ESP32 Fault Injection 攻擊是 AI 自主硬體安全研究能力的里程碑案例。

---

## 2026-05-11 Ingest

- 來源日報：[[news/2026-05-11]]
- 更新頁面：
  - `entities/managed-agents.md`（正式發布升格狀態；社群 70 天自建多代理架構案例；官方 vs 社群架構比較進入主流討論；2026-05-11 歷史記錄）
  - `entities/claude-code.md`（現況補充 Managed Agents 正式發布 + Desktop vs Cowork 定位混淆 + 插件生態密集爆發；新工具：adamsreview / vibe-log-cli / academic-research-skills；版本歷史 2026-05-11）
  - `entities/opus-4-7.md`（新增已知問題：Opus 4.7 提示詞行為世代性轉變，4.7 更趨字面解讀，4.6 通用指令效果下降）
  - `entities/pricing.md`（新增：Pro 方案 0% 使用量仍被收取 $3.37 extra usage；$514/30 天費用分析 + 配額管理指南）
  - `topics/community-tech-patterns.md`（新增技術彙整：Judge Gate 語意級品質驗證 / AI agent 語意漂移 CI 測試 / 多代理 PR review / CLAUDE.md 記憶驗證兩招 / AGENTS.md 跨工具插件簡報 / agent skill 商業價值評估；熱門應用新增 adamsreview / vibe-log-cli；2026-05-11 時序）
- 新增頁面：無
- 摘要：Managed Agents 本週正式發布標誌官方 multi-agent 托管服務進入正式階段；Claude Code 費用管理成為最熱議焦點（$514/30 天分析、Pro 0% 仍被收費、配額透明度問題）；「Judge Gate」概念揭示自主編程代理語意驗證盲點；Opus 4.7 提示詞行為世代性轉變（更趨字面）確認，所有現有 prompt 工程實踐需重新審視。

---

## 2026-05-10 Ingest

- 來源日報：[[news/2026-05-10]]
- 更新頁面：
  - `entities/claude-code.md`（CLAUDE.md 作為 candidate-context 架構揭示；Claude Code Sandboxing 官方文件；Google 搜尋木馬仿冒事件；Lobotomized Claude Code 社群工具；新工具：Remind/draft CLI plugin/Tokenyst/Agentize；已知問題新增 CLAUDE.md candidate-context；版本歷史新增 2026-05-10 兩條）
  - `entities/pricing.md`（Opus API 速率限制調降；Pay-as-you-go session 費用 $6–10 成因與壓低策略）
  - `topics/ai-agent-safety.md`（新增技術彙整：Google 搜尋廣告詐騙與木馬/AI agent 清空資料庫兩次+指令防火牆/Claude Code Sandboxing 官方文件；更新目前結論加入供應鏈攻擊警示；2026-05-10 時序）
  - `topics/community-tech-patterns.md`（新增技術彙整：本機圖資料庫降低 session token 成本/multi-agent 研究調查團隊/Claude Code 架構解析系列/三層疊加式 AI Code Review；熱門應用新增 Remind/draft CLI plugin/Snyk+Claude Code/Tokenyst/Agentize；2026-05-10 時序）
- 新增頁面：無
- 摘要：Google 搜尋廣告出現 Claude Code 木馬仿冒網站（已有用戶中招）是最大安全事件；CLAUDE.md 作為 candidate-context 的架構揭示直接解釋「指令被忽略」的長期痛點；Anthropic 發布 Sandboxing 官方文件；Opus API 速率限制調降與社群 session 費用控管方案同步浮現。

---

## 2026-05-09 Ingest

- 來源日報：[[news/2026-05-09]]
- 更新頁面：
  - `entities/claude-code.md`（Windows IDE 擴充套件 Windows 全面無法載入事件；v2.1.136 操作安全+如實回報機制 +525 tokens + `hard_deny` 類別；v2.1.138 internal fixes；新工具：re_gent/unitmux/obsidian-semantic；已知問題新增 Windows IDE 擴充套件失載）
  - `entities/pricing.md`（SpaceX Colossus 1 正式到位確認：300MW 電力 + Claude API 速率上限加倍，更新標題至 2026-05-09）
  - `topics/ai-agent-safety.md`（新增技術彙整：v2.1.136「操作安全與如實回報」機制；2026-05-09 時序：`hard_deny` 類別 + 不可逆操作確認 + 如實回報義務）
  - `topics/community-tech-patterns.md`（新增技術彙整：HTML vs Markdown 輸出格式辯論/PostToolUse 稽核日誌模式/Git Hooks 強制代碼品質/re_gent AI agent 版本控制/54 ADR 35 天/obsidian-semantic 語義 vault 搜尋；熱門應用新增 re_gent/unitmux/obsidian-semantic；2026-05-09 時序）
  - `topics/code-quality-decline.md`（新增技術彙整：靜默模型切換 silent model switching + 11.5 倍效率差距；2026-05-09 時序）
- 新增頁面：無
- 摘要：Anthropic 正式接入 SpaceX Colossus 1 220,000 GPU 為最大基礎設施事件；v2.1.136「操作安全與如實回報」（+525 tokens + `hard_deny`）是 agent 行為規範的實質性收緊；Windows IDE 擴充套件再度全面失效（Linux 路徑硬編碼）；HTML vs Markdown 輸出格式辯論與靜默模型切換（11.5 倍效率差距）為本日兩大社群技術話題。

---

## 2026-05-08 Lint

- 修正矛盾：
  - `entities/google-investment.md`：移除重複的 2026-04-27 時序條目（內容完全重複，保留第一份）
  - `entities/pricing.md`：`最後更新` 欄位從 2026-05-07 更正為 2026-05-08（2026-05-08 ingest 有更新此頁）
- 補連結（孤立頁面修正）：
  - `topics/community-tech-patterns.md` → 在「相關實體」補上 `[[entities/managed-agents]]`（新頁面 2026-05-07 建立後未反映在此頁）
  - `entities/claude-code.md` → 在「相關議題」補上 `[[entities/boris-cherny]]`
- 狀態更新：無
- 遷移至 entities：無（`topics/google-investment.md` 已在上次 lint 遷移）
- 新增 entities：
  - `entities/boris-cherny.md`（Claude Code 創始人，10+ 次跨頁提及，涵蓋 Loops 設計哲學、「coding is solved」論戰、4/23 事後報告、第三方工具邊界聲明）
- overview.md：已全面重寫（反映 2026-04-25 至 2026-05-08 局勢，含 CVE 安全危機、SpaceX 算力合作、Managed Agents 升級、競品壓力轉折點）

---

## 2026-05-08 Ingest

- 來源日報：[[news/2026-05-08]]
- 更新頁面：
  - `entities/claude-code.md`（CVE-2026-39861 CVSS 7.7 沙箱逃逸漏洞 + 1-click RCE 信任危機；v2.1.133 `worktree.baseRef` 設定；Boris Cherny「coding is solved」/ 反「vibe coding」；Claude Cowork Linux 沙箱啟動失敗；Claude Sonnet 4.8 外洩；新工具：Claudy/DataMoat/4-agent Code Review/awesome-ux-skills；已知問題新增 CVE-2026-39861 與 Cowork 沙箱故障）
  - `entities/pricing.md`（SpaceX Colossus 220,000 GPU 細節補充；2026-05-08 多媒體跟進報導確認）
  - `entities/mythos.md`（新增：CVE 諷刺觀察——Mythos 未能預警自家產品漏洞，成社群質疑安全一致性的新論據）
  - `topics/ai-agent-safety.md`（新增技術彙整：CVE-2026-39861 細節 + 1-click RCE 信任危機；更新目前結論；2026-05-08 時序：CVE/RCE/DataMoat 防禦工具）
  - `topics/community-tech-patterns.md`（新增技術彙整：本機持久化記憶 39ms/120 提示詞模式實證研究/3.77億 token 極端案例/三種整合模式框架/Boris Cherny 術語演化；更新熱門應用：Claudy/DataMoat/4-agent Code Review/awesome-ux-skills/OpticOdds MCP；2026-05-08 時序）
- 新增頁面：無
- 摘要：CVE-2026-39861（CVSS 7.7）沙箱逃逸 + 1-click RCE 信任危機是最大安全事件，Anthropic「責怪使用者」的回應態度加劇批評；SpaceX Colossus 220,000 GPU 算力合作細節確認；Boris Cherny「coding is solved」+ 反「vibe coding」在多平台引發社群兩極反應；120 提示詞模式實證研究是本日最具方法論價值的社群貢獻。

---

## 2026-05-07 Ingest

- 來源日報：[[news/2026-05-07]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.132 發布；Managed Agents 重大更新 Dreaming/20路/Outcomes；Python SDK v0.100.0 + TypeScript SDK v0.95.0；SpaceX 算力合作速率翻倍；Wire trace 揭示 13K 基礎提示詞；Bedrock 再次異常；授權撤銷後 session 持續出現；新工具：BrowserCode/跨session插件/recap/Kstack）
  - `entities/pricing.md`（SpaceX 算力合作：Pro/Max 五小時速率上限翻倍、取消尖峰降速、API Tier 4+ 提升；Max 5x 用戶週限制可能同步調高，待官方確認）
  - `topics/community-tech-patterns.md`（新技術彙整：Skill Atrophy 反思與對策、Managed Agents 架構模式、Wire Trace 架構侷限、Git Log 除錯首要步驟、MCP Code Execution Token 效率、跨 Session 通訊插件；熱門應用新增：BrowserCode/qu-ans插件/recap/Kstack/Claude Code Routines；2026-05-07 時序）
  - `topics/competitor-landscape.md`（DeepSeek V4 替換 Claude Opus 4 30 天實測；Cursor 全面轉換 Claude Code 六個月比較；2026-05-07 時序）
  - `topics/ai-agent-safety.md`（授權撤銷後 session 紀錄持續出現技術彙整；Wire Trace 揭示 Auto 模式安全邊界為提示詞層；2026-05-07 時序）
- 新增頁面：`entities/managed-agents.md`（Dreaming 記憶整合、20 路子代理並行、Outcomes 規格驗證，Code with Claude 大會重大更新）
- 摘要：Anthropic + SpaceX 算力合作為最大商業事件（Pro/Max 速率翻倍），Managed Agents 三大更新（Dreaming/20路/Outcomes）標誌 Agent 框架從無狀態轉有狀態，Wire trace 揭示 Auto 模式安全僅為提示詞層是最重要的安全資訊，社群 skill atrophy 反思與授權撤銷後 session 持續出現的安全隱患同步浮現。

---

## 2026-05-06 Ingest

- 來源日報：[[news/2026-05-06]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.131 緊急修復 Windows VS Code regression；Python/TypeScript SDK v0.99.0/v0.94.0 workspace 定向；Claude Code 121K stars；Claude Security 公開 Beta；新工具：Claudette、claude-smart、Dreamer；Boris Cherny「軟體工程已死」第二波）
  - `entities/pricing.md`（GitHub Copilot 27x Opus 加價比較；94% token 流向錯誤模型；工具迴圈帳單爆衝三案例：yarn.lock £400 + daemon $500）
  - `entities/claude-security.md`（dev.to 深度介紹文章，公開 Beta 媒體報導持續擴大）
  - `topics/competitor-landscape.md`（DeepSeek Claude Code clone 8,700 stars；DeepClaude 17x 成本替代方案；Claude Code 121K stars 里程碑；Boris Cherny 第二波論戰）
  - `topics/community-tech-patterns.md`（新技術彙整：Speculative Parallelism 工作流、Skills Unix 哲學、Hooks 強制執行機制、CLAUDE.md 語言規則集爆發、Agentic 組織協調挑戰、MCP Hub 模式、Self-improving rules；新工具：Claudette/claude-smart/Dreamer；2026-05-06 時序）
- 新增頁面：無
- 摘要：v2.1.131 緊急修復 Windows VS Code regression 為最大運維事件；費用管理危機多點同步爆發（Copilot 27x 加價、94% token 誤路由、工具迴圈爆衝）；DeepSeek clone 8,700 stars + DeepClaude 17x 低成本替代生態加速形成；CLAUDE.md 語言規則集爆發（5 個語言單日密集出現）標誌社群規範建立進入加速期。

---

## 2026-05-05 Ingest

- 來源日報：[[news/2026-05-05]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.128 發布；Amazon 全員部署 Claude Code；Boris Cherny「Loops 是未來」哲學；新工具：SprintiQ/Claude Relay/Memex/Claude-Find/Askdiff/Rudel）
  - `entities/pricing.md`（提示快取窗口縮短靜默改動；Ollama vs 訂閱成本比較熱議；token 降耗技巧主流化）
  - `entities/opus-4-7.md`（4.7 退步討論浮現；部分開發者回退 4.6）
  - `topics/competitor-landscape.md`（Codex 下載量首次超越 Claude Code 1397% 週增；Amazon 雙品牌並行部署；DeepClaude 替代方案發酵）
  - `topics/community-tech-patterns.md`（Boris Cherny Loops 哲學；多 session 工具鏈 Claude Relay/Memex/Claude-Find/Askdiff；Multi-agent CLAUDE.md 11 條衝突防範規則；Playwright CLI vs npx token 陷阱；token 降耗策略集中出現；LinkedIn skill human-in-the-loop 架構；Rudel session 分析）
  - `topics/code-quality-decline.md`（Opus 4.7 退步討論再升溫）
- 新增頁面：無
- 摘要：OpenAI Codex 單週下載量首次超越 Claude Code（+1397% vs -38%）是最大競爭事件；Anthropic 悄悄縮短提示快取窗口（未公告）延續透明度爭議；Amazon 雙品牌並行部署凸顯企業端多供應商策略成主流；社群工具呈現「session 管理工具鏈化」趨勢（Claude Relay + Memex + Claude-Find + Askdiff 四工具形成完整管理生態）。

---

## 2026-05-04 Ingest

- 來源日報：[[news/2026-05-04]]
- 更新頁面：
  - `entities/claude-code.md`（原始碼外洩/8100 DMCA/Claw-Code 新增；Claude Cowork 第三方 LLM 支援；Claude Connectors 擴展至創意工作軟體；新工具 Semble/Kirikiri/JupyterLab Extension/Prism MCP/claudely/Smithy/Patina；版本歷史 2026-05-04 條目更新）
  - `entities/pricing.md`（Pro 試用 7 天結束說明不一致；Amazon Bedrock 授權即時過期問題；Claude 5 小時滾動視窗機制與預排程技巧）
  - `topics/community-tech-patterns.md`（2026-05-04 時序：DeepClaude/Semble/Kirikiri/JupyterLab Extension/Prism MCP/claudely/Smithy/Patina/「放棄嗎重置效應」/CLAUDE.md for Java/Memtrace/Pilot Shell/Claude Connectors 創意工作；新技術彙整：Backend 替換模式、CLAUDE.md 防腐爛機制、Agent Context 新鮮度問題、結構化 Agent 框架設計、Agent Supervision 哲學；熱門應用表新增 8 項工具）
  - `topics/competitor-landscape.md`（2026-05-04 時序：Claude Desktop/Cowork 第三方 LLM 支援重大變化、Claude Connectors 創意工作軟體、Haiku 4.5 73.3% SWE-bench；摘要更新：競爭格局轉向多模型平台）
- 新增頁面：無
- 摘要：Claude Code 原始碼外洩引發 8100+ DMCA 與 Claw-Code 誕生為最大事件；Claude Cowork/Desktop 悄悄支援任意第三方 LLM 代表競爭格局從「Claude vs. others」轉向「多模型接入層」；社群工具生態新一波爆發（7 款新工具），CLAUDE.md 防腐爛與 Agent Context 新鮮度成為本週社群技術討論新主題。

---

## 2026-05-03 Ingest

- 來源日報：[[news/2026-05-03]]
- 更新頁面：
  - `entities/claude-code.md`（macOS computer use 功能上線；新工具 TradingAgents Plugin；版本歷史更新）
  - `entities/pricing.md`（帳單失控問題主流化；本地 LLM 替代失敗案例）
  - `entities/opus-4-7.md`（Fortify 安全掃描修復失敗；研究任務正面評價）
  - `topics/community-tech-patterns.md`（2026-05-03 時序：macOS computer use、91k ERP 案例、8 tips、雙代理 VPS 框架、K8s CLAUDE.md 規則、AI 命名一致性 OSS、TradingAgents Plugin、40 技能系統、開發者身份認同；新技術彙整：CLAUDE.md 領域化安全規則、AI 程式碼一致性、AI 大規模開發案例、Agent 持續運作架構；熱門應用表更新）
  - `topics/ai-agent-safety.md`（PowerShell.exe 重命名事件；帳單失控主流化；技術彙整新增 Windows 環境危險操作）
  - `topics/code-quality-decline.md`（4/23 事後報告 50+ 修復社群獨立驗證行動；目前結論更新）
- 新增頁面：無
- 摘要：Claude Code 加入 macOS computer use 能力為最大功能更新；社群主動問責 Boris Cherny 4/23 事後報告的 50+ 承諾修復；PowerShell.exe 重命名事件揭示 Windows 環境 agent 安全盲點；開發者身份認同議題持續發酵。

---

## 2026-05-02 Ingest（第二次，補充最新版日報）

- 來源日報：[[news/2026-05-02]]（本次為更新版日報，與第一次 ingest 所處理版本不同）
- 更新頁面：
  - `entities/claude-code.md`（新增已知問題：AGENTS.md 規範不支援 issue #6235；新工具：Governor、Caliber）
  - `entities/pricing.md`（Uber 企業案例：$500–$2,000/月/工程師，四個月燒光全年 AI 預算）
  - `topics/community-tech-patterns.md`（2026-05-02 時序：PreToolUse Hooks 四 exit code、Token 路由策略、Governor、Caliber、記憶體防漂移框架、規格驅動開發、CLAUDE.md 跨 repo 傳播、sudo MCP 插件；新技術彙整：Hooks 精細化控制、Token 路由、記憶體治理、Spec-Driven Dev、CLAUDE.md 跨 repo）
  - `topics/competitor-landscape.md`（2026-05-02 時序：OpenCode 被 XDA 認可為可行替代方案、OpenClaw 禁令持續發酵；新增 OpenCode 競品追蹤）
- 新增頁面：無
- 摘要：Uber 四個月燒光全年 AI 預算（$500–$2K/月/工程師）成為業界成本管控標誌性案例；OpenCode 崛起為 Anthropic 政策收緊後的主流替代方案；社群工具方向轉向治理與優化（記憶防漂移、規格驅動、跨工具 config 管理）。

---

## 2026-05-02 Ingest（第一次）

- 來源日報：[[news/2026-05-02]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.126 細節、session 30 天自動刪除、Omar/graphify/NanoBrain/Council/Destiny/Mote 新工具）
  - `entities/claude-security.md`（全 Enterprise 開放細節：Git 歷史讀取、跨檔案資料流追蹤、推理式驗證）
  - `entities/pricing.md`（$6,000 /loop 失控事件、帳號停用計費爭議、Bedrock 配額歸零、Max 方案 60% 消耗、50% 費用節省方案）
  - `entities/mythos.md`（OpenAI Cyber 限制存取事件：Altman 批評 Anthropic 後採同樣策略）
  - `entities/opus-4-7.md`（GPT-5.5 vs Opus 56 task 基準測試、4.5→4.7 躍升感知討論）
  - `entities/google-investment.md`（gigawatt 等級算力預購）
  - `topics/community-tech-patterns.md`（2026-05-01 時序：Omar、graphify、Chrome 用量擴充、NanoBrain、Council、50% 費用節省、Destiny、Mote；新技術彙整：知識圖譜、session 歷史保留、封閉技能批判）
  - `topics/ai-agent-safety.md`（$6,000 /loop 失控、MCP 指令執行漏洞、Bedrock 配額歸零）
  - `topics/competitor-landscape.md`（五角大廈排除 Anthropic、Apple 採用 Claude、Uber 燒光預算、iCapital、The Atlantic AI 泡沫報導）
- 新增頁面：`topics/anthropic-government-policy.md`
- 摘要：五角大廈因安全護欄分歧排除 Anthropic 為最大事件（白宮已重啟談判）；Claude Security 正式全面開放 Enterprise 公測；graphify 26 天衝上 GitHub #2 顯示知識圖譜工具需求爆發；/loop 失控 $6,000 事件引爆 Anthropic 用量警報機制批評；Apple 採用 Claude 顯示頂層科技企業滲透加速。

---

## 2026-05-01 Lint

- 修正矛盾：無
- 補連結（孤立頁面修正）：
  - `entities/project-deal.md` → 在 `topics/community-tech-patterns.md` 相關實體加入連結
  - `entities/claude-design.md` → 在 `topics/community-tech-patterns.md` 相關實體加入連結；在 `entities/claude-code.md` 相關議題加入連結
- 狀態更新：`topics/google-investment.md` 狀態維持 resolved，已遷移
- 遷移至 entities：`topics/google-investment.md` → `entities/google-investment.md`（保留原頁重定向提示）
- 新增 entities：
  - `entities/openclaw.md`（第三方 agentic 工具，被提及 3+ 次：配額限制 + 異常計費 + claude-code 已知問題）
  - `entities/google-investment.md`（從 topics/ 遷移）
- overview.md：已全面重寫（反映 2026-04-25 至 2026-04-30 局勢）

---

## 2026-04-30 Ingest

- 來源日報：[[news/2026-04-30]]
- 更新頁面：
  - `entities/mythos.md`（WSJ 白宮報導更多細節、五角大廈角力、Dark Reading 資安產業分析）
  - `entities/pricing.md`（ANTHROPIC_API_KEY 雲端計費陷阱、Pro 餘額消失、長 context 快取隱性成本）
  - `entities/claude-code.md`（OpenClaw 異常計費、v2.1.124/2.1.126 系統提示分析、GameMaker 整合、Managed Agents AWS 定位、Throttle Meter/Brifly/Mneme/Nimbalyst/Trent 等工具、Projects 對話消失）
  - `entities/opus-4-7.md`（退步報告、arxiv 4T 參數估算）
  - `topics/ai-agent-safety.md`（OpenClaw 計費觸發機制、AI agent 憑證竊取攻擊、Claude Code vs Gemini CLI 信任邊界標準差異）
  - `topics/code-quality-decline.md`（Opus 4.7 後設化退步、Projects 對話消失）
  - `topics/competitor-landscape.md`（Codex 社群能見度調查、GameMaker 整合、BrowserCode 瀏覽器化趨勢）
  - `topics/community-tech-patterns.md`（2026-04-30 時序、7 款新工具入熱門應用表、多 LLM 協作架構技術彙整）
- 新增頁面：`entities/claude-security.md`
- 摘要：OpenClaw 異常計費事件（HN 近千則討論）引爆帳單透明度信任危機；白宮介入 Mythos 管控的細節持續擴大（Anthropic 自稱世界未準備好）；Claude Security 公開測試版標誌 Anthropic 正式跨足 AI 資安產品市場；帳單透明度問題從多個角度（OpenClaw/API KEY 計費/餘額消失/快取成本）同步爆發。

---

## 2026-04-29 Ingest

- 來源日報：[[news/2026-04-29]]
- 更新頁面：
  - `entities/mythos.md`（白宮反對擴大 Mythos 存取、Steve Blank「潘朵拉盒子」文章）
  - `entities/pricing.md`（$900B 估值融資洽談、Token 費用估算翻倍、Max 方案 API 錯誤）
  - `entities/claude-code.md`（Champion Kit、Speed Bumps 問題、Cockpit/Harness/CodeThis/Claude Exporter 四款新工具）
  - `topics/code-quality-decline.md`（Speed Bumps 增加、Max 支援 AI 失靈）
  - `topics/competitor-landscape.md`（Codex vs Claude Code 生產環境比較）
  - `topics/community-tech-patterns.md`（Champion Kit、Cockpit、Harness、CodeThis、Claude Exporter、Caveman 基準測試）
- 新增頁面：無
- 摘要：白宮介入 Mythos 存取管控為最大事件；Anthropic 靜默將 Claude Code token 費用估算翻倍引發企業預算警示；單日四款社群工具（Cockpit/Harness/CodeThis/Claude Exporter）湧現顯示生態仍活躍；Caveman 基準測試挑戰「複雜外掛優於兩字 prompt」的直覺假設。

---

## 2026-04-28 Ingest

- 來源日報：[[news/2026-04-28]]
- 更新頁面：
  - `entities/claude-code.md`（v2.1.121 發布、Runhouse acqui-hire、Auto Compact 失效、Prompt Cache Race Condition、Tool Schema 洩漏、PullMD 新工具）
  - `entities/pricing.md`（Opus 圍牆事件及修正、20x 計量異常、Auto Compact 鎖死、$1T 估值）
  - `entities/opus-4-7.md`（Opus 圍牆事件、生物問題拒絕、effort 研究、Sonnet 替代數據）
  - `entities/mythos.md`（SWE-bench 方法論爭議擴散至 HN）
  - `topics/code-quality-decline.md`（安全定義過窄批評、信任侵蝕結構性分析）
  - `topics/community-tech-patterns.md`（Jupyter MCP、Batch API、PullMD、Sonnet 工作流、Plugin 設計模式、effort 研究）
  - `topics/competitor-landscape.md`（哈佛改用 Claude、XDA 四工具比較、雪梨辦公室）
- 新增頁面：`topics/ai-agent-safety.md`
- 摘要：Cursor + Claude Opus 9 秒刪除生產資料庫為最大事件；Opus 圍牆政策引發信任危機（雖事後修正）；Anthropic 商業擴張加速（Sydney 辦公室、哈佛採用、Runhouse 收購、$1T 估值）；多個基礎設施可靠性問題（Prompt Cache Race、Auto Compact 失效、Schema 洩漏）同日密集出現。

---

## [2026-04-27] ingest (補充) | 日報 15:44 UTC 重跑版本（44 篇）

- 來源日報：[[news/2026-04-27]]（更新版，44 篇，新增 Show HN 工具與 Claude Design 相關內容）
- 更新頁面：
  - `topics/community-tech-patterns.md`（新增 Rapunzel、SmolVM、Groundtruth、OpenCode-power-pack、APFS worktree、Doom MCP 實驗、學習技能模組）
  - `entities/claude-code.md`（新增 Rapunzel / SmolVM / Groundtruth / OpenCode-power-pack 工具）
  - `entities/mythos.md`（IEEE Spectrum 安全部署要求後續報導）
  - `topics/google-investment.md`（AWS + Anthropic & Meta 合作）
- 新增頁面：`entities/claude-design.md`
- 摘要：Show HN 工具大爆發（Groundtruth、SmolVM、Rapunzel）驗證新 HN 來源設定有效；Claude Design 首日社群評價偏負面，系統提示詞遭反向工程。

---

## [2026-04-27] ingest | 每日日報更新

- 來源日報：[[news/2026-04-27]]
- 更新頁面：
  - `entities/claude-code.md`（API 金鑰外洩漏洞、Usage Policy 隨機拒絕、版本回滾、Mac 卸載不完整、新社群工具 EvanFlow/Relay/pentest-ai-agents/modularity）
  - `entities/pricing.md`（Max 方案多工配額不足、Google 投資定價指標意義）
  - `entities/mythos.md`（SWE-bench 方法論循環論證爭議、Project Glasswing）
  - `entities/opus-4-7.md`（Usage Policy 隨機拒絕、Sonnet vs Opus 社群比較數據）
  - `topics/google-investment.md`（投資確認報導、CoreWeave 算力合作）
  - `topics/competitor-landscape.md`（HackerNoon AI 護城河分析、Claude vs GPT 比較討論）
  - `topics/community-tech-patterns.md`（EvanFlow、Relay、parsh 策略、modularity、effort 數據、CLAUDE.md 最佳實踐）
- 新增頁面：`entities/project-deal.md`
- 摘要：Google 400 億投資正式確認、Claude Code 安全問題（API 金鑰外洩 + HERMES.md 計費 bug）持續發酵、Mythos SWE-bench 方法論遭學術質疑、Project Deal 代理人交易實驗引發法律與商業討論。

---

## [2026-04-26] 新增頁面 | community-tech-patterns

- 手動新增：`topics/community-tech-patterns.md`
- 用途：追蹤社群技術應用趨勢，每次 ingest 從「💬 技術熱度討論」區塊累積萃取
- 已回填 2026-04-25 與 2026-04-26 兩天的內容

---

## [2026-04-26] ingest | 每日日報更新

- 來源日報：[[news/2026-04-26]]
- 更新頁面：
  - `entities/claude-code.md`（HERMES.md bug、Bugcrawl、新社群工具 Claude Squad / mux0 / agent-order）
  - `entities/pricing.md`（HERMES.md 靜默計費、token burn、OpenClaw 配額限制）
  - `entities/mythos.md`（七週發現 2,000+ 漏洞）
  - `topics/competitor-landscape.md`（Google 競品消息二度登 HN）
- 新增頁面：`entities/bugcrawl.md`
- 摘要：HERMES.md 計費 bug 曝光為最大新聞，Mythos 漏洞發現能力獲多媒體報導，Claude Code 社群工具生態持續擴張。

---

## [2026-04-25] init | Wiki 初始化建立

初始化 wiki 結構，根據 `news/2026-04-25.md` 內容建立以下頁面：

**新建 entities：**
- `entities/claude-code.md`
- `entities/opus-4-7.md`
- `entities/pricing.md`
- `entities/mythos.md`

**新建 topics：**
- `topics/code-quality-decline.md`
- `topics/google-investment.md`
- `topics/competitor-landscape.md`

**新建 overview：**
- `overview.md`

---

## 2026-05-15 Re-ingest（品質審查補跑）

- 來源日報：[[news/2026-05-15]]（已於同日 Ingest 處理，本次為品質審查補跑）
- 更新頁面：
  - `entities/pricing.md`（完整重構：以 6/15 互動式 vs 程式化雙軌計費架構為核心，新增方案對照表、費用管控技巧、6/15 前行動清單；歷史政策紀錄保留但壓縮）
- 新增機制：
  - `CLAUDE.md` 新增「Wiki 頁面呈現品質標準」（必須修復 + 警示觸發重構規則）
  - `wiki-ingest.md` 新增 Step 4b 呈現品質審查（強制核對）
  - `wiki-lint.md` 新增 Step 3e 呈現品質審查（全頁面掃描）
  - `.claude/settings.local.json` 新增 PostToolUse Hook（markdownlint-cli2 自動掃描）
  - 新增 `/wiki-backfill` 與 `/wiki-digest` 指令
- 呈現品質審查結果：
  - `entities/claude-code.md`（336 行）✅ 通過——版本歷史以表格壓縮，功能分主題區塊
  - `entities/pricing.md`（210 行）✅ 通過——重構後計費架構清晰置頂，表格呈現
  - `topics/competitor-landscape.md`（160 行）✅ 通過
  - `topics/ai-agent-safety.md`（239 行）✅ 通過——技術彙整按主題組織，時序含 [tag] 分類
  - `topics/community-tech-patterns.md`（836 行）📋 待辦——過大，建議 lint 時將舊 時序 條目壓縮進 技術彙整；當前結構可讀，不阻礙使用
- 摘要：本次補跑以建立呈現品質審查機制為主，並完成 pricing.md 架構重構，使 6/15 計費雙軌制在頁面頂部即可讀懂。

---

## 2026-05-15 Lint

- 修正矛盾：無
- 補連結：
  - 新建 `entities/cat-wu.md`（Cat Wu 被 claude-code.md × 2 + community-tech-patterns.md × 2 + feature-radar.md 提及共 5 次，達建頁閾值）
  - `entities/claude-code.md` → 補上 `[[entities/cat-wu]]`（近期重要更新 + 相關議題兩處）
  - `topics/community-tech-patterns.md` → 2026-05-15 及 2026-05-14 兩筆 Cat Wu 提及補 wikilink
- 狀態更新：無（所有 ongoing/monitoring 狀態確認無需調整）
- 遷移至 entities：無
- 新增 entities：`entities/cat-wu.md`（Claude Code 產品負責人，AI 主動性論述）
- 呈現品質：
  - `topics/competitor-landscape.md` ⚠️ 已修復：16 個連續日期條目新增 3 個主題分組（企業競爭白熱化 / Codex 崛起與分流 / 早期格局）
  - `topics/community-tech-patterns.md` 📋 待辦：836 行過大，最舊 4 個時序條目（2026-04-25 至 2026-04-28）待壓縮至技術彙整；工作量過大，記錄待辦，次週 lint 處理
  - 其餘所有頁面（12 entities + 4 topics）✅ 通過
- overview.md：已全面重寫（反映 2026-05-14/15 計費政策、Microsoft 授權取消、Cat Wu proactivity 論述、Ramp 企業超越數據）

## 2026-05-15 拆分 community-tech-patterns

- 原因：community-tech-patterns.md 達 836 行，技術彙整混入應用（工具/工作流）與討論（哲學/辯論/實證）兩種性質
- 新增頁面：`topics/community-tech-discussions.md`（技術討論趨勢）
- 移出條目（24 項）：effort 等級與模型行為、多 LLM 協作架構、工具生態痛點、封閉技能生態批判、規格驅動開發、記憶體治理與行為漂移防範、AI 程式碼一致性問題、AI 大規模開發案例、Boris Cherny「Loops 是未來」、Agent Supervision 哲學、Skills Unix 哲學、Agentic 工作流組織協調挑戰、Wire Trace 架構侷限、120 提示詞實證研究、Token 用量極端案例、整合模式選擇框架、Boris Cherny 反 vibe coding、Skill Atrophy 反思、HTML vs Markdown、Claude Code 架構深度解析、三層 Code Review、Judge Gate、Context 管理核心瓶頸、AI 生成程式碼安全審查必要性
- 結果：patterns.md 836→716 行；discussions.md 244 行（新）
- 更新：index.md（頁數 22→23）、community-tech-patterns.md（摘要、目前結論、相關實體）

## 2026-05-16 熱門討論表格擴充

- 變更：`topics/community-tech-discussions.md` 熱門討論表格新增 `模式` 欄（☄️閃現/🌊延燒/🌸落幕/🌋重燃/🌙靜候）與 `衍生` 欄
- 補連結：HTML vs Markdown 討論 → 衍生 `agent-html-skills`；Skill Atrophy → 衍生 `recap 工具`；多 LLM 協作 → 衍生 `Opus+DeepSeek 混合架構`
- 新增規則：`CLAUDE.md` 補入 community-tech-patterns ↔ community-tech-discussions 雙向連結規則、模式判斷規則（含重燃偵測邏輯）
- 確認 emoji 方案：重燃模式採 🌋（火山重燃）

## 2026-05-17 新增 official-community-gap + community-tech-tools 痛點洞察

- 新增頁面：`topics/official-community-gap.md` — 官方功能 vs 社群痛點缺口矩陣，含 9 個痛點、收斂程度評估、結構性原因分析與預測指標
- 更新頁面：`topics/community-tech-tools.md` — 新增 `## 痛點洞察` 區塊，含痛點主題表格、CLAUDE.md 失效四原因、AI 輔助開發副作用分析；參考來源新增 official-community-gap 連結
- 更新：`index.md`（頁數 24→25，新增 official-community-gap 條目）
- Web reader：wiki 首頁新增「官方 vs 社群缺口分析」卡片


---

## 2026-05-23 Lint

- 修正矛盾：
  - `topics/code-quality-decline.md`：最後更新欄位未從 2026-05-09 更新至 2026-05-21（2026-05-21 ingest 遺漏）→ 已修正
  - `topics/anthropic-government-policy.md`：監測狀態文字「11 天無新進展」→「21 天無新進展」→ 已修正；最後更新更新至 2026-05-22
- 補連結：
  - `entities/google-investment` 孤立（無其他頁面連結）→ 已在 `topics/competitor-landscape.md` 技術彙整補入 wikilink
  - `entities/andrej-karpathy`（本次 ingest 新建）→ 已在 `topics/community-tech-discussions.md` 相關實體補入 wikilink
- 狀態更新：無（anthology-government-policy 狀態維持 monitoring，21 天仍在追蹤）
- 遷移至 entities：無
- 新增 entities：`entities/opencode.md`（OpenCode 開源替代，27 次提及、10 個檔案）；已在 competitor-landscape.md 補入 wikilink
- 呈現品質：
  - 超長頁面 `topics/community-tech-patterns.md`（695 行）✅ 拆分完成：
    - 保留 `community-tech-patterns.md`（403 行）：摘要、模式概覽、技術彙整、結論、相關實體
    - 新建 `topics/community-tech-timeline.md`（~310 行）：2026-04-25 至 2026-05-22 完整時序
    - 兩頁互相補上 wikilink；patterns.md 補入 `[[news/2026-05-22]]` 參考來源
  - 其餘頁面：✅ 通過（各頁面於 ingest 時已執行品質審查）
- 超長頁面（> 500 行）：community-tech-patterns.md（695 行）→ 已拆分（見呈現品質）
- CLAUDE.md 健檢：
  - 行數：99 行（原 353 行，拆分後；閾值 150 行）✅ 大幅精簡
  - 拆分：wiki 規則（~270 行）移至新建 `wiki/CLAUDE.md`；技能檔案更新載入點
  - 矛盾：無
  - 引用驗證：所有 CLAUDE.md 引用的欄位/結構均已遷移至 wiki/CLAUDE.md，保持有效
  - 遵守率：✅ 全部通過（見 2026-05-22 Ingest 呈現品質欄）
  - 過期規則（> 60 天）：無（最舊規則 [加入: 2026-04-25] = 28 天）
  - 簡化：已執行（wiki 規則全部移至 wiki/CLAUDE.md；skills 更新 Step 1/2 明確載入）
- overview.md：已更新（2026-05-21 → 2026-05-22，涵蓋 DeepSeek 全棧競品、$6K 費用事件、Karpathy 加入、Managed Agents 文件完整化）

## 2026-05-23 時序整體修復

- **觸發原因：** 使用者反映「WIKI頁面時序混亂，請整體檢查」
- **掃描範圍：** 全部 entities/（16頁）+ topics/（11頁）
- **已修復（共 6 頁）：**
  - `topics/competitor-landscape.md`：2026-05-22 + 2026-05-21 誤排在 2026-05-19 後面 → 已修正為最新在前；section header 日期範圍同步更新
  - `entities/google-investment.md`：時序區塊 2026-05-01 誤排在 2026-04-27 後面 → 已調整為最新在前
  - `entities/boris-cherny.md`：公開言論區塊日期錯亂（2026-05-05→05-06→05-13→05-08…）→ 統一改為最新在前
  - `topics/community-tech-tools.md`：四處錯亂：May-21（5條）、May-16（2條）誤放表格末尾；Apr-30（5條）排在 Apr-29 後；Apr-28（2條）排在 Apr-27 後 → 全部移至正確位置
  - `topics/community-tech-discussions.md`：熱門討論表格多處日期錯亂（05-20×3 排在 05-09 後、05-13 排在 05-08 前等）→ 統一按日期最新在前重排；並恢復誤刪的 Boris "coding is solved" 05-08 延燒條目
- **確認無誤（✅ 正確順序）：**
  - enterprise-cost-management.md、code-quality-decline.md、ai-agent-safety.md、managed-agents.md：✅
  - community-tech-timeline.md：✅（2026-05-22 在頂，往下遞減）
  - claude-code.md 版本歷史 + 歷史記錄：✅
  - community-tech-discussions.md 技術彙整：✅
  - pricing.md、openclaw.md、stainless.md、claude-security.md、andrej-karpathy.md：✅
  - 其餘單一/少量日期頁面（bugcrawl、project-deal、claude-design、cat-wu、mythos 主題性分段）：✅ 無排序問題

---

## 2026-05-23 Ingest | news/2026-05-23.md

- 來源日報：`news/2026-05-23.md`（74 則；含 Claude Code RCE CVE-2026-39861、Microsoft 企業授權取消、Project Glasswing 10K+ 漏洞、Opus 4/Sonnet 4 退役 6/15、新工具 Superset/OpenRig/VIR/CoreMem/tokenflex.ing/Shortcuts Playground、$30B 融資、多人協調困境討論）
- 更新頁面：
  - `entities/claude-code.md`：新增 v2.1.150（基礎設施改善）；新增 RCE 警示與 Opus 4/Sonnet 4 退役 6/15 至 開發者須知；更新 現況 最新版本
  - `topics/ai-agent-safety.md`：新增 Claude Code RCE 跨工具傳播（2026-05-23）；新增 Mythos Exploit 開發評估報告（2026-05-23）；更新 最後更新
  - `topics/enterprise-cost-management.md`：新增 2026-05-23 時序（tokenflex.ing $30,983、API 帳單 3x、Microsoft 授權取消確認）
  - `topics/competitor-landscape.md`：新增 2026-05-23 時序（Business Insider Claude 贏新創、Microsoft 確認、RCE 跨工具傳播）
  - `topics/community-tech-tools.md`：新增 6 工具（Superset、OpenRig、VIR、CoreMem、tokenflex.ing、Shortcuts Playground）；更新 痛點洞察 表（跨 session 記憶歸零項目新增 VIR/CoreMem）
  - `topics/community-tech-discussions.md`：LLMs 虛假忙碌 模式改為 🌊延燒；新增 Solo 爽、團隊亂 熱門討論（2026-05-23）；新增對應技術彙整條目
  - `entities/mythos.md`：新增 Project Glasswing 一個月更新（10K+ 漏洞，修補速度成新瓶頸）；新增 Mythos Exploit 開發能力評估（exploit primitives + 端對端攻擊鏈）；更新 最後更新
  - `entities/pricing.md`：新增 2026-05-23 模型別名退役警示（Opus 4/Sonnet 4 June 15）；更新 最後更新
  - `topics/community-tech-patterns.md`：新增 Git Worktrees 作為多 Agent 隔離原語（2026-05-23）；新增 Framework-Specific CLAUDE.md 設計（2026-05-23）；更新 最後更新
  - `wiki/feature-radar.md`：v2.1.150 為基礎設施改善，無新使用者功能；更新 最後更新
- 新增 entities：無
- feature-radar 更新：本日無新功能（v2.1.150 infra-only）
- 呈現品質：
  - `entities/claude-code.md` ✅ 通過
  - `topics/ai-agent-safety.md` ✅ 通過
  - `topics/enterprise-cost-management.md` ✅ 通過
  - `topics/competitor-landscape.md` ✅ 通過
  - `topics/community-tech-tools.md` ✅ 通過
  - `topics/community-tech-discussions.md` ✅ 通過
  - `entities/mythos.md` ✅ 通過
  - `entities/pricing.md` ✅ 通過
  - `topics/community-tech-patterns.md` ✅ 通過

---

## 2026-06-19 Lint

- 修正矛盾：`wiki/index.md` 中 `topics/anthropic-government-policy` 狀態 `monitoring` → `ongoing`，描述更新為反映出口管制封鎖現況
- 補連結：無（所有頁面均有來自其他實體/議題頁的入鏈）
- 狀態更新：`topics/anthropic-government-policy`：monitoring → ongoing（頁面於 6/18 ingest 已改為 ongoing，index.md 今日同步）
- 遷移至 entities：無（無 resolved 議題）
- 新增 entities：無
- 呈現品質：
  - 所有近期更新頁面（6/16–6/18 ingest 已審查）✅ 全數通過
  - `wiki/overview.md`：⚠️ 已修復（重寫至 2026-06-19；原版停留在 6/13，仍說「明天生效 6/15 計費」、Fable 5 未封鎖）
- 超長頁面（> 500 行）：無
- 規則檔健檢：
  - `wiki/CLAUDE.md`：51 行（閾值 80 行）✅
  - `.claude/rules/wiki-ingest.md`：283 行（閾值 250 行）⚠️ 超出 33 行
    - 最大段落：`feature-radar.md 更新規則`（約 63 行）、`entities/ 格式模板`（36 行）、`topics/ 格式模板`（38 行）
    - 建議：`feature-radar.md 更新規則` 中的「版本更新收錄判斷」表格可考慮縮減；但格式模板為必要，不建議刪除
    - 決定：**維持現狀**，待自然演進（使用者未要求立即簡化）
  - 矛盾：無
  - 引用驗證：全部通過（首次出現 ✅、痛點洞察 ✅、近期工具 ✅、技術彙整 ✅、熱門討論 ✅、衍生 ✅、全覽表 ✅）
  - 遵守率（近 3 次 ingest）：呈現品質審查 3/3 ✅、feature-radar 更新 3/3 ✅、社群工具新增更新 3/3 ✅、log.md 格式 3/3 ✅
  - 過期規則（> 60 天，基準 2026-04-20）：最舊規則 `[加入: 2026-04-25]`（55 天）→ 無規則超過閾值 ✅
  - 簡化：跳過（33 行超出為可接受範圍，使用者未確認簡化方向）
- overview.md：已更新（完整重寫，反映 Fable 5 出口管制封鎖為當前首要議題）

---

## 2026-06-19 Wiki 頁面合併

- `entities/project-deal.md` → 合併至 `entities/claude-code.md`（Agentic 能力擴展區塊新增 Project Deal 條目）
- `entities/stainless.md` → 合併至 `topics/anthropic-business.md`（戰略合作表格新增收購列）
- 更新入鏈：`topics/community-tech-patterns.md` wikilink 改為純文字引用；`entities/claude-code.md` 歷史紀錄 `[[entities/stainless]]` 改為 `[[topics/anthropic-business]]`
- 刪除：`entities/project-deal.md`、`entities/stainless.md`
- `wiki/index.md`：移除兩列，最後更新 2026-06-19

## 2026-06-26 Ingest | news/2026-06-26.md（63 則）

- 來源日報：`news/2026-06-26.md`（63 則，6/6 來源；Reddit 429 rate limit 部分失敗，仍有 10 筆）
- 更新頁面：
  - `wiki/entities/claude-code.md`：v2.1.193（autoMode.classifyAllShell）；Anthropic 官方 40 萬 session 研究報告
  - `wiki/entities/john-jumper.md`：補充 2026-06-26 dev.to 報導；Mythos 危機背景；$2,700 億市值蒸發細節
  - `wiki/entities/tom-brown.md`：移除聯合創辦人待核實標記；補充 GPT-3 共同作者背景
  - `wiki/entities/dario-amodei.md`：2026-06-26 WIRED 報導（政府不信任、Tom Brown 接管談判）
  - `wiki/entities/pricing.md`：Max 5x × 2 vs 20x × 1 方案分析（獨立開發者並行 session 策略）
  - `wiki/topics/anthropic-government-policy.md`：Tom Brown 接管談判進展；Bloomberg 反效果分析；Alibaba 蒸餾攻擊政策面；攻防紀錄表 prepend 3 行
  - `wiki/topics/ai-agent-safety.md`：Alibaba 蒸餾攻擊（安全面，28.8M/25K 假帳號，待對方確認）；MITRE ATT&CK 報告（832 帳號映射）
  - `wiki/topics/anthropic-business.md`：Alibaba 蒸餾攻擊補強細節（信件日期 6/10、收信人 Scott/Warren、攻擊窗口 4/22–6/5）；Claude Cowork 行動版
  - `wiki/topics/ai-talent-flow.md`：Google 一週 4 位研究員跳槽 Anthropic（John Jumper 領銜）；$2,700 億市值蒸發；Gemini 3.5 延期；對各公司影響表更新
  - `wiki/topics/enterprise-cost-management.md`：企業 ROI 反撲（tokenmaxxing → 效率優先，qz.com + CNBC）
  - `wiki/topics/competitor-landscape.md`：DeepSeek V4 Flash 顛覆 agent 定價經濟學（成本 100x 降低）
  - `wiki/topics/community-tech-patterns.md`：6 個新工作流模式（Read-Only Reviewer、Repo-as-Memory、Just-in-time @-file 載入、批量 OSS bug 修復、20 agent 規模化限制、Personas vs Tool-scoping）
  - `wiki/topics/community-tech-discussions.md`：3 個新熱門討論（OpenKnowledge、DeepSeek 顛覆 Anthropic 定價、terminal agent 比較）；清理超過 21 天的 ☄️閃現 條目
  - `wiki/topics/code-quality-decline.md`：Claude Code 自訂編排路由失效（自訂 provider agents 無法可靠路由）
  - `wiki/topics/official-community-gap.md`：Claude Cowork 行動版進展（平台可及性分析）
  - `wiki/feature-radar.md`：新增 autoMode.classifyAllShell（🔥🔥 / ⚡）；更新本週推薦（/rewind 取代破壞性 Git 封鎖）
  - `wiki/index.md`：近期異動更新；tom-brown 移除待核實標記
- feature-radar 新增：autoMode.classifyAllShell（Claude Code v2.1.193）
- 新增頁面：無
- 呈現品質審查：✅ claude-code.md / john-jumper.md / tom-brown.md / dario-amodei.md / anthropic-government-policy.md / ai-agent-safety.md / anthropic-business.md / ai-talent-flow.md / enterprise-cost-management.md / pricing.md / competitor-landscape.md / community-tech-patterns.md / official-community-gap.md；⚠️ community-tech-discussions.md 已修復（移除超過 21 天 ☄️閃現 條目）；code-quality-decline.md ✅

## 2026-06-28 手動修正 | community-tech-discussions 收錄規則細化

**背景：** 審查 discussions.md 評分機制時發現無收錄門檻，低信號（HN 3）與高信號（HN 300+）混放，且有條目熱度符號與實際信號強度不符。

**規則修正（`.claude/rules/wiki-ingest-community.md`，新增「community-tech-discussions 收錄門檻」）：**
- 確立**三個合法訊號來源**（滿足其一即可收錄）：社群碰撞（HN ≥ 10 / Reddit 有互動 / 跨 2 來源）、重要人士具名表態、重要媒體深度報導
- **誠實標註原則（強制）：** 熱度符號錨定真實信號強度——🔥🔥 以上隱含「社群共鳴」，無社群討論的單一報導不得標 🔥🔥 以上，須標 🔥 + 註「（媒體報導，待社群接力）」
- 設計演進：初版「僅限 HN/Reddit、排除媒體」過窄（哲學討論多來自 HN，且會擋掉 36Kr 內部第一手報導）→ 定版改為「來源可多元 + 熱度須誠實」兩件事分開處理

**discussions.md 實際清理：**
- 移除 4 筆低信號條目（表格列 + 技術彙整）：AI 概念哪些會留存（HN 3）、Claude Code 確定性技術（HN 4）、Trust Us Is Not a Control Surface（HN 3，原誤標 🔥🔥🔥）、Boris Cherny 立場轉變（已在 `entities/boris-cherny.md` 完整記錄）
- 保留並修正 1 筆：Anthropic 工程師孤獨感（36Kr）→ 熱度由 🔥🔥 改 🔥，加註「媒體報導，待社群接力」，與「Vibe coding 成就感缺失」（HN）互連為跨組織佐證
- 同步更新頂部「最熱討論」callout、🔥 本週熱點 區塊；最後更新 2026-06-28
- 呈現品質審查：✅ community-tech-discussions.md

## 2026-06-28 手動修正 | community-tech-patterns 信號軸校正

**背景：** 審查 patterns.md 時發現原本想用 HN score 策展，但 patterns 價值在「技術本身」而非「熱度」——信號強度（多少人注意到）≠ 技術力（技術好不好）。差點因 HN 3 砍掉 ANMA，但 ANMA 自帶 0/20 vs 13/19 硬數據，是全頁證據最硬的條目之一。

**改用「自帶可驗證證據強度」軸重新盤點 26 條 dated 條目：**
- **A 層（自帶量化/可複現證據）：** ANMA、Compact Memory、Hooks 強制執行、批量 OSS Bug、對抗性審查——維持原狀，量化數據本身即最佳標註
- **B 層（機制自洽、可操作、合第一性原理，無量化但站得住）：** 16 條——全部保留，不標註
- **C 層（純經驗談，無機制驗證）：** 3 條——加誠實標註

**實際改動（僅 C 層 3 條加「訊號：單一經驗談，無機制驗證，待社群佐證」）：**
- 任務開始前先 Interview（機制平庸 + 純心得）
- Self-rewriting CRM（單一軼事，限制標「推論」）
- Spec-driven Development CLI（對應工具 opsx 已被 HN flagged）

**撤回前一輪對 greymothjp 群、ANMA 的降級提議——用證據軸看它們站得住，不因低 HN 降級。**

**方法論定論：** patterns 不該用 HN score 策展（那是 tools/discussions 的邏輯）；正確軸是「機制是否自洽 + 有無可驗證證據」，標註用「未驗證」把判斷權交還讀者，而非替技術判生死。
- 呈現品質審查：✅ community-tech-patterns.md（C 層 3 條標註，A/B 層維持原狀）

---

## 2026-06-29 每日 ingest

**日報：** [[news/2026-06-29]]（67 條 / 6 來源）

**分類派工：** 模型、功能、商業、安全政策、社群、人物 六記者並行。

### 記者回報摘要

**模型記者**（fable-5、mythos）：
- Fable 5：美方批准向特定信任夥伴恢復 Mythos 存取，Axios 報導「可能本週回歸」；狀態註記更新；中國 Z.Ai/360 宣稱比肩 Mythos、Grok 4.5 競品、模型成本效益實測併入相關記錄
- Mythos：出口管制鬆動，特定信任合作夥伴獲准恢復存取

**功能記者**（claude-code）：
- Claude Tag、Gmail MCP、Claude Compliance API、/goal、session/context 管理均為既有功能或社群討論；無新 feature-radar 條目；Gmail MCP 黑暗設計模式爭議記入 claude-code.md

**商業記者**（anthropic-business、enterprise-cost-management、ai-talent-flow、competitor-landscape）：
- Newsom × Anthropic 加州政府協議（政府客戶新維度）
- Lindy 100% 流量切換 DeepSeek，每月省數百萬美元（API 客戶流失具名化）
- Alibaba 2,880 萬次查詢進入參議院記錄
- 4 名 Google 研究員轉投 Anthropic + Gemini 3.5 延期（推論，dev.to）
- 奧地利遊說 EU、Micron 合作評估

**安全政策記者**（ai-agent-safety、anthropic-government-policy）：
- Claude Code 未驗證執行 GitHub 隱藏惡意程式，攻擊者取得完整系統控制（信任邊界缺失定性升級）
- Mythos 出口管制鬆動、Alibaba 參議院揭露、奧地利遊說 EU、親 AI 陣營分裂、反托拉斯視角
- MCP server 5 分鐘安全審查清單

**社群記者**（community-tech-discussions 等）：
- MRI 第二意見分析（HN 476，社群熱議）、多 agent 協調、模型 token 成本效益討論
- 社群工具：AgentWatch、Reference MCP、Brain.md、Caliper、agent-swarm、Argus、Shikhu、claude-annotate

**人物記者**：
- 4 名 Google 研究員轉投 Anthropic 但未具名（門檻未達），不新建人物頁面

### 主編彙整

- **feature-radar.md**：Fable 5 條目與區塊更新（6/29 恢復進展）；本週推薦改版（Artifacts / Managed Agents / Coordinator 模式，輪替超期的 /goal）；最後更新 6/29
- **index.md**：近期異動覆寫；mythos/fable-5 狀態註記更新；最後更新 6/29
- **overview.md**：當前局勢改寫（出口管制解凍 + Newsom 協議 + Lindy 切換 + Alibaba 參議院 + Claude Code 安全事件）；模型表 Fable 5/Mythos 狀態更新；最後更新 6/29
- **log.md**：本條目

### 呈現品質審查
所有更新頁面記者自審 ✅ 通過。

## 2026-06-29 新增頁面 | community-pattern-trends.md（社群 Pattern 宏觀趨勢）

**背景：** 使用者反映 patterns.md 條目太多、有點亂，需要高一階的「趨勢觀察」層。確立：萃取宏觀趨勢、週更（/wiki-lint 維護，不進每日 ingest）、每條趨勢含「對現有設計的啟示」欄位（使用者最在意——工程師看到趨勢該回頭重思自己的設計）。

**設計決策：**
- 新建獨立頁，而非塞進 patterns.md（已 ~660 行）或覆蓋 timeline（timeline 是寶貴歷史流水帳，演進起點素材）
- 視覺化（時間軸泳道圖）按需另生，不在頁面維持（使用者決定）
- 每條趨勢含：熱度曲線（📈加溫/▬穩定/↗醞釀）、演進時間軸（每節點掛注意力熱度 🔥）、代表模式（連回 patterns.md）、對現有設計的啟示
- 熱度錨點區分：演進節點用「注意力熱度」（HN/跨平台）；代表模式用「技術力證據」（A/B 層）
- 趨勢判定門檻：≥ 3 獨立來源 + 跨 ≥ 14 天 + 至少 1 條代表模式達 A/B 層證據

**內容：** 5 條成形趨勢（強制層取代建議層、Multi-agent 隔離、Context 主權、模型路由自動化、對抗性設計）+ 1 條醞釀（spec-driven 規格先行）。

**連結：** index.md 新增列；patterns.md / timeline.md 摘要加 wikilink 指向新頁（de-orphan）。

**待辦：** 趨勢判定門檻與週更維護流程尚未寫進 `.claude/rules/wiki-ingest-community-lint.md`，下次處理規則檔時補上並跑 /review-commands。

## 2026-06-29 瘦身 | entities/claude-code.md 移除冗餘工具索引

**背景：** claude-code.md 達 439 行，「實用工具（社群開發）」區塊（75+ 工具、約 122 行）與 [[topics/community-tech-tools]] 平行維護兩份工具清單。community-tech-tools 改三層結構後其「工具目錄」層已是完整清單，且有 lint 策展規則維護；claude-code 這份無人依規則策展，只會越長越舊。

**動作：** 砍掉整個「實用工具（社群開發）」區塊，換成一行指向 [[topics/community-tech-tools]] 的指標。claude-code.md 回歸「產品本體權威頁」純粹定位（版本、狀態、核心功能、已知問題、agentic 能力、開發者須知）。

**結果：** 439 → 317 行。屬結構性去冗餘，非新聞性修改，僅更新「最後更新」（本已為 2026-06-29），不動「最後新聞更新」。

## 2026-06-29 品質修正 | 六記者 dry-run 審查後修補（A+B+部分C）

**背景：** 派 6 個 wiki 記者對全部 entities/topics 做 dry-run 品質審查（檢查本週 review 出的 6 類問題：頭條缺失、熱度虛抬、單一來源偽裝、低信號混入、跨頁冗餘、過長混雜）。記者只讀不改、leaf agent 無殭屍風險。以下為據回報執行的高信心修正：

**A 類（本輪自身瑕疵）：**
- discussions L84 Boris Cherny 立場轉變殘留（漏清）→ 改為誠實標註版「Times of India 單一報導，無社群延燒」+ wikilink boris-cherny
- ai-talent-flow 頭條「正是 Google 落後的領域」漏標 →補（推論）

**B 類（快速修正）：**
- code-quality-decline 補「最後新聞更新：2026-06-26」欄
- claude-code v2.1.195 日期統一（頭條 06-27 → 06-26，與內文/版本表一致）；最後新聞更新 06-29 → 06-26（內文最新內容為 06-26，無 06-29 新聞）
- dario-amodei FT 字詞密度事件日期統一（歷史記錄 06-23 → 06-22，與摘要/表格一致）
- boris-cherny「公開言論」時序錯亂修正（Loop Engineering 06-20 移至 06-22 與 05-27 之間，回復嚴格倒序）
- recursive-self-improvement 摘要數字統一（「80-90%」→「≥80%（官方確認下限，部分報導稱 80–90%）」）

**C 類（熱度，部分執行）：**
- feature-radar Claude Tag 🔥🔥🔥 → 🔥🔥（單一公告+單日 HN，不足 🔥🔥🔥）
- **刻意跳過**：社群記者建議的「patterns 5 條單一 dev.to 來源補未驗證標註」——與本日確立的「patterns 用證據軸不用信號軸」決策衝突，B 層機制自洽條目不標，維持原狀

**D 類（結構性，留待 /wiki-lint）：** ai-agent-safety 460 行→archive 分流；anthropic-business 304 / pricing 308 行時序整併；claude-code 已知問題↔歷史記錄去重；fable-5/mythos 現況↔歷史雙寫 + 定價歸 pricing；discussions 888 行拆分評估；跨頁冗餘（Lindy/阿里巴巴/Microsoft/Mythos NSA）；opus-4-8/4-7 熱度滿格殘留重估。

**方法論收穫：** 總體審查品質來自「視角重疊」而非單一記者無誤——人物記者抓到社群記者（discussions 主責人）漏掉的 L84 殘留。另記者會套既定 rubric 但不知本 session 新決策（社群記者退回信號軸），故下次審查應把當前判準寫進派工 prompt。

## 2026-06-30 Ingest | news/2026-06-30.md（46 則）

- 來源日報：`news/2026-06-30.md`（46 則，6/6 來源；Reddit 429 rate limit 部分失敗）
- 核心事件：Claude Code v2.1.91 起嵌入中國代理偵測程式碼（重大隱私爭議，逆向工程發現，待 Anthropic 確認）、v2.1.196 Org Default Model 正式發布、v2.1.197 洩露 Sonnet 5 選項、Mozilla prompt injection 完整接管多媒體確認、Anthropic 拒配合 Trump 政府付出代價（Fortune 深度報導）、Globant/DataArt/Okta/Rubrik 四項企業合作同日宣布
- 更新頁面：
  - `wiki/entities/claude-code.md`：v2.1.196 Org Default Model、v2.1.197 Sonnet 5 選項、transcript 自動刪除 Bug、36Kr 背景任務升級預告（待核實）、Explore subagent 鎖定 Haiku 的限制說明
  - `wiki/topics/official-community-gap.md`：多模型路由狀態更新（❌ → ⚡）
  - `wiki/topics/ai-agent-safety.md`：Claude Code 中國代理偵測程式碼（新 🔴 項目，待確認）、Mozilla prompt injection 多媒體四方確認
  - `wiki/topics/anthropic-government-policy.md`：Fortune 深度報導、CNBC 出口管制反效分析、SF Examiner 專家質疑；攻防紀錄 +3 條
  - `wiki/topics/anthropic-business.md`：Globant AI Pods、DataArt Partner Network、Okta XAA/MCP/Glasswing、Rubrik Claude Code 安全層四項合作；時序 2026-06-30 區塊
  - `wiki/entities/pricing.md`：社群集體反映配額再次縮減（訂閱用戶，Anthropic 無官方公告）
  - `wiki/topics/enterprise-cost-management.md`：「穴居人插件」趨勢條目，OpenAI/Nvidia/GitHub 開發者採用
  - `wiki/topics/community-tech-patterns.md`：新增工作流模式
- feature-radar 新增：Org Default Model（v2.1.196）— 🔥🔥 / ⚡ 有條件推薦
- index.md 狀態變更：無（新功能條目加入全覽表）
- 新增頁面：無
- 呈現品質審查：所有更新頁面均 ✅ 通過（記者回報確認）

## 2026-06-30 Lint | 商業頁面 3a–3f 品質檢查

- 執行頁面：`topics/anthropic-business.md`、`topics/enterprise-tool-tracker.md`、`topics/enterprise-cost-management.md`、`topics/competitor-landscape.md`、`entities/pricing.md`
- 3a 矛盾修正：`topics/anthropic-business.md` 第 26、76 行「Microsoft 6/30 停用」與 enterprise-tool-tracker（6/21 加速退出）矛盾 → 已修正為「原訂 6/30，已於 6/21 加速退出」並加 wikilink
- 3b 孤立頁面：全部 5 頁均有其他頁面引用 → 無孤立問題
- 3c 過期議題：全部頁面最後更新均在 14 天內 → 無須狀態降級
- 3d 已解決議題遷移：無 resolved 狀態頁面
- 3e 呈現品質：
  - `topics/anthropic-business.md`：⚠️ 已修復（矛盾修正）；📋 待辦：33 個時序節點無主題分組（超閾值 8），建議按主題/月份合併，工作量過大本次跳過
  - `topics/enterprise-tool-tracker.md`：✅ 通過
  - `topics/enterprise-cost-management.md`：✅ 通過
  - `topics/competitor-landscape.md`：⚠️ 已修復（新增 `#### 亞洲競品崛起與定價顛覆（2026-06-19 至 2026-06-29）` 分組標題）
  - `entities/pricing.md`：✅ 通過（30+ 節點均在 `## 重要政策變動紀錄` 統一標題下，視為已分組）
- 3f 超長頁面（> 500 行）：無（最長 anthropic-business.md 311 行，pricing.md 313 行，均未超 500）

## 2026-06-30 Lint（全 wiki，六記者並行）

- 修正矛盾：
  - `entities/fable-5.md`：Tom Brown 職稱補充 chief compute officer（與 mythos.md 一致）
  - `topics/anthropic-business.md`：Microsoft 退出日期「6/30」→「原訂 6/30，已於 6/21 加速退出」（與 enterprise-tool-tracker 統一）
  - `entities/claude-security.md`：最後新聞更新日期錯誤（2026-06-20 → 2026-05-28）
  - `wiki/index.md`：ai-agent-safety 摘要更新為最新事件（中國代理偵測 + Mozilla prompt injection）
- 補連結（去孤立）：無（全部頁面均有引用）
- 狀態更新：無
- 遷移至 entities：無
- 新增 entities：無（Workweave Router / Globant / DataArt 均未達建頁門檻）
- 呈現品質（逐記者）：
  - 模型：fable-5 / opus-4-8 現況改 delta-first ⚠️已修復；opus-4-7 / mythos ✅
  - 功能：claude-code 近期重要更新補副標題、bugcrawl + claude-design callout 日期更新、claude-security 日期矛盾修正 ⚠️已修復；managed-agents / openclaw / official-community-gap ✅
  - 商業：anthropic-business 矛盾修正、competitor-landscape 時序分組 ⚠️已修復；enterprise-tool-tracker / enterprise-cost-management / pricing ✅；📋 待辦：anthropic-business 33 個時序節點無主題分組，下次 lint 考慮合併
  - 安全政策：anthropic-government-policy + ai-agent-safety 摘要改 delta-first ⚠️已修復；recursive-self-improvement ✅；📋 ai-agent-safety 484 行接近門檻，下次 ingest 後重計
  - 社群：community-tech-tools + community-tech-timeline callout 更新、community-pattern-trends callout 週更 ⚠️已修復；community-tech-patterns / discussions / code-quality-decline ✅；community-tech-tools 新增 10 條（2026-06-22 至 2026-06-30）；Workweave Router 提拔精選層
  - 人物：9 個人物頁補 callout 或改 delta-first 首句 ⚠️全部已修復；andrej-karpathy / chris-olah 加「截至 YYYY-MM-DD，後續待追蹤」提示
- community-tech-patterns 淘汰審查：0 條建議淘汰，0 組建議合併，全部保留
- community-pattern-trends 趨勢週更：新增 3 個趨勢節點（趨勢一 Adrafinil 保活模式、趨勢三 56KB 截斷、趨勢五 Verity 自癒 review gate）；更新趨勢三啟示文字
- 超長頁面（> 500 行）：community-tech-discussions.md（909 行）、community-tech-patterns.md（811 行）；社群記者評估兩者均有自清機制或可 grep 定位，暫不拆分
- 規則檔健檢：
  - wiki/CLAUDE.md：50 行（閾值 80）✅
  - .claude/rules/wiki-ingest.md：68 行（閾值 80）✅
  - .claude/rules/wiki-ingest-format.md：135 行（閾值 200）✅
  - wiki-ingest-features.md：121 行（閾值 100）⚠️（與上次 lint 一致，暫不執行）
  - wiki-ingest-models.md：50 ✅ / commercial.md：77 ✅ / safety-policy.md：53 ✅ / people.md：41 ✅
  - wiki-ingest-community.md：105 行（閾值 100）⚠️（略超，新增社群訊號門檻規則所致）
  - wiki-ingest-community-lint.md：110 行（閾值 100）⚠️（今日新增 patterns 淘汰 + trends 週更兩個區塊所致）
  - 矛盾（6a）：無
  - 引用驗證（6b）：7/7 全部通過
  - 遵守率（6c）：近 3 次 ingest 品質審查 3/3 ✅ / feature-radar 3/3 ✅
  - 過期規則（6d）：entities/topics 格式模板 [加入: 2026-04-25]（65 天）— 六記者實際套用確認仍吻合現狀，無需修訂
  - 簡化（6e）：features / community / community-lint 三檔超門檻，本次跳過（功能完整，非冗餘膨脹）
- Python 熱度訊號修復（源碼層）：base.py 加 source_count 欄位；reddit.py + devto.py 改取 slash_comments 代理訊號；dedup.py 改合併累加 source_count 而非替換；analyzer.py 顯示跨來源數（✦ 跨 N 個獨立來源）
- overview.md：已更新（當前局勢改三條線；進行中議題 #5 ai-agent-safety 改 delta-first；近兩週事件表加 06-29/06-30；商業動態同步新合作）

## 2026-07-01 Ingest | 101 篇文章，重大事件日

- 來源日報：`news/2026-07-01.md`（101 篇 / 6 來源）
- 更新頁面：
  - `entities/fable-5.md`（出口管制 7/1 全面解除，歷史記錄更新）
  - `entities/mythos.md`（出口管制解除，全球恢復）
  - `entities/claude-code.md`（v2.1.197 Sonnet 5 預設，SDK v0.115.0，版本表更新）
  - `entities/managed-agents.md`（Python SDK v0.115.0，callout 更新）
  - `entities/pricing.md`（Sonnet 5 促銷 $2/$10/Mtok，Fable 5 usage-based billing）
  - `topics/anthropic-business.md`（Enterprise Gateway、Fable 5 協議解禁、Claude Science 附記）
  - `topics/anthropic-government-policy.md`（攻防紀錄表與時序更新，解封分析）
  - `topics/ai-agent-safety.md`（隱寫術爭議 HN 2263、CVE-2026-55407 DoS 漏洞）
  - `topics/community-tech-discussions.md`（4 條新討論：隱寫術 / 成本暴漲 / 30 天刪除 / 穴居人採用）
  - `topics/community-tech-patterns.md`（1000 subagent fan-out、Git worktree 教學、穴居人成本模式）
  - `wiki/feature-radar.md`（新增 Sonnet 5 🔥🔥🔥🔥🔥、Claude Science 🔥🔥，Fable 5 解禁更新）
  - `wiki/index.md`（新增 sonnet-5、claude-science，Fable 5/Mythos 狀態更新）
  - `wiki/overview.md`（當前局勢全面改寫，模型表更新，07-01 事件列入）
- 新增頁面：`entities/sonnet-5.md`、`entities/claude-science.md`
- feature-radar 新增：Claude Sonnet 5（🔥🔥🔥🔥🔥 / ✅ 強烈推薦）、Claude Science（🔥🔥 / ⚡ 有條件推薦）
- index.md 狀態變更：fable-5（暫停→解除）、mythos（部分解禁→全面解除）、sonnet-5（新增）、claude-science（新增）
- 呈現品質審查：全部通過（各記者確認）

## 2026-07-01 使用者發起品質審查 + 修正

使用者派 5 個記者 agent（模型/功能/商業/安全政策/社群）逐一審查各自負責頁面，找出結構性改善空間（非日常 ingest 範圍），確認後套用修正。

- **最高優先修正**：`wiki/feature-radar.md` — Fable 5 狀態矛盾（本週推薦寫「全面解除」但功能全覽表詳細條目仍寫「⚠️ 停用」），已統一為解除狀態
- **最高優先修正**：`wiki/topics/enterprise-tool-tracker.md` — 落後 5 天未同步，補齊 Rubrik/Okta/Globant/DataArt/加州州政府/Lindy 六筆企業動態
- 狀態變更：`anthropic-government-policy` ongoing → monitoring（出口管制主線解除，剩餘承諾落實等 5 項變數持續觀察）
- 結構精簡：`ai-agent-safety.md`（512→414 行，5 月中旬前技術彙整遷移至 archive）、`claude-code.md`（330→310 行，移除 Q2 精選重複子區塊）
- 新頁面孤立連結修正：`sonnet-5.md` ↔ `opus-4-8.md`、`fable-5.md`；`claude-science.md` → `managed-agents.md`、`anthropic-business.md`
- 社群工具清理：`community-tech-tools.md` 移除 4 筆逾期 ⏳ 條目、合併 2 組重複列
- 使用者決定 `community-tech-patterns.md`（834行）、`community-tech-discussions.md`（937行）**維持現狀不拆分**
- 修正頁面：23 個（entities 10 / topics 13）
- 記憶更新：新增 feedback memory `feedback_entity_status_crosscheck.md`（改實體狀態需 grep 全檔案）

## 2026-07-02 可讀性掃描

- 掃描頁數：41（✅ 30 / ⚠️ 10 / ❌ 1）
- 已修復：
  - `topics/ai-agent-safety`（❌→修復：摘要 10 段文字牆壓為 2 段、目前結論 19 條改表格、時序補 06-22 條目）
  - `topics/anthropic-government-policy`（目前局勢 17 條長 bullet 改「剩餘變數」表格、摘要降至 2 段）
  - `entities/mythos`（現況收斂 2 段、時序 24 條按管制三階段分組）
  - `entities/fable-5`（現況刪 5 段過期「最新（待核實）」段落、歷史記錄 20 條按三階段分組）
  - `entities/managed-agents`（現況 8 段錯亂日期收斂為 2 段，與歷史記錄去重）
  - `entities/claude-code`（現況 15 行巨型段落拆 4 短段、去重）
  - `entities/pricing`（政策紀錄 36 條按 5 主題分組，零殘留未分組日期）
  - `topics/anthropic-business`（06-14 以前時序按 IPO/Partner 主題彙整、指標表標註數據截至 05-29）
  - `topics/competitor-landscape`、`topics/enterprise-cost-management`（凍結指標表標註「數據截至」）
  - `topics/community-tech-patterns`、`topics/community-tech-discussions`（技術彙整 89+94 條月份分組，條目零遺失）
  - H1 改名：patterns「社群實戰模式庫」、pattern-trends「社群趨勢觀察（週更）」；index 狀態欄砍字
- 使用者跳過：official-community-gap H1（使用者確認 callout 已足夠，維持原樣）
- 共通問題：「現況被時序侵蝕」與「指標表凍結」為流程病，已補進 `.claude/rules/wiki-ingest-format.md`（必修規則 + 警示各一條）；技術彙整月份分組制寫入 `.claude/rules/wiki-ingest-community.md`

## 2026-07-02 日報格式修復 + 新增模型選型對照頁

- **日報格式修復**：當日 pipeline 生成的日報條目偏離規格（bullet 式標題而非 `**[標題](url)**`），導致 web reader 解析出空區塊、讀者只見今日聚焦。已依 gathered_items.json 重生 `news/2026-07-02.md`（自檢 11 個連結標題；重點話題 2 / 討論 6 / 付費 3；無 official 條目故省略 🔧）；流程面在 `.claude/commands/news-pipeline-steps.md` Step 1b 加入格式強制警告與 3a 格式自檢（grep 連結標題數 ≥ 5）
- **新增頁面**：`wiki/topics/model-comparison.md` — 模型選型對照（快速選型表 + 情境推薦 + benchmark 對照），回應「個別模型頁難聚焦」的讀者需求；`.claude/rules/wiki-ingest-models.md` 新增選型對照同步規則與 sonnet-5 負責頁面
- index.md：新增 model-comparison 列與近期異動

## 2026-07-04 週度延伸回顧

- 延伸（已執行，2026-07-05 完成）：
  - fable-5.md 新增「配額與計費過渡（至 7/7）」子區塊（模型）
  - model-comparison.md 新增「token 消耗／每任務成本」維度，矛盾實測並陳（模型）
  - claude-code.md 補「隱寫術標記／代理偵測指控」🔴 條目與 #38335 配額 issue（功能）
  - official-community-gap.md 產品化矩陣新增「跨工具 agent 設定標準（AGENTS.md）」列 ❌（功能）
  - code-quality-decline.md 新增「Token 消耗異常訊號群」子區塊，三假說分析（社群）
- 使用者跳過項目：無（六項全數執行）
- 觀察待辦（本次不動手）：
  - 「個性流失」議題等第三個模型世代樣本再評估建頁（模型）
  - 額度焦慮多條 ☄️閃現，下次 ingest/lint 評估合併為 🌊延燒主題（社群）
  - Alibaba/Anthropic 對「後門風險」正式回應後，重估「中美 AI 工具信任對峙」獨立頁（安全政策）
  - fable-5.md 達 253 行，下次 lint 執行入口層健檢（不拆分）
- 商業、人物記者判斷本週無延伸缺口；安全政策記者否決「信任危機」獨立建頁（三頁分工已完整）

## 2026-07-05 週度延伸回顧（增量，涵蓋 06-28 至 07-04）

- 延伸：無（六類記者一致判斷：07-04 新訊號已被 07-04 那輪回顧的六項延伸覆蓋，或未達收錄門檻）
- 使用者跳過項目：無
- 觀察待辦：#74066 session/cache 洩漏疑慮（單帖單日）由下次例行 ingest 併入 ai-agent-safety 漏洞區塊標「待查證」；Karpathy 待核實標記已掛 5 週，交由下次 lint 3g 待查證回訪處理；Crew、Mycelium 新工具留待下次 lint 策展評估

## 2026-07-10 Lint

- 修正矛盾：
  - 功能：`official-community-gap.md` 頁內 Cowork 事件日期 07-07→07-08（摘要＋技術彙整 2 處，與 claude-code.md/index.md 一致）
  - 模型：`fable-5.md` 免費期限指標欄過期（06-22→07-12，與同頁 callout 一致）
- 補連結：`teresa-carlson`（原僅 index/log 引用）→ 由人物記者在 `ai-talent-flow.md` 相關實體補 wikilink，雙向連結成形
- 狀態更新：`recursive-self-improvement` ongoing→monitoring（最後新聞更新 2026-06-22，距今 18 天無新進展；記者已改頁面 callout/摘要，主編已同步 index.md Topics 表）
- resolved 收尾：無
- 新增 entities：無（本輪掃描無達 3 次提及且無頁的新名稱；六記者亦未回報建頁候選）
- 呈現品質：全部通過（多頁記者主動修復——過期檢查點日期 bugcrawl/claude-design/openclaw、逾期待查證標記 claude-code 7 條/opus-4-7/karpathy/chris-ciauri/john-jumper 改註「至今無後續」或轉明確結論、discussions 過期 ☄️閃現 清理 4 筆）
- 入口層健檢：`community-tech-discussions.md`（1000 行）、`community-tech-patterns.md`（897 行）、`ai-agent-safety.md`（513 行）均具完整入口層（callout＋概覽表＋月份/主題分組），通過不拆分；無語意分岔/死案候選
- 待查證回訪：已完成多筆（模型 opus-4-7；功能 claude-code 7 條；人物 chris-ciauri 預測獲驗證/karpathy 改註/john-jumper 澄清；安全政策無逾期）；其餘標記均在 14 天門檻內
- 規則檔健檢：
  - wiki/CLAUDE.md：53 行（閾值 80）✅
  - .claude/rules/wiki-ingest.md：71 行（閾值 80）✅
  - .claude/rules/wiki-ingest-format.md：145 行（閾值 200）✅
  - 各記者規則檔：commercial 102 / community 123 / community-lint 110 / features 154 / models 57 / people 44 / safety-policy 56 / reporter-shared 91（閾值 150）→ ⚠️ features 154 略超，建議下輪簡化（非阻擋）
  - 矛盾：無（本 session 兩次 /review-commands 均零錯誤）
  - 引用驗證：全部通過（7 錨點：首次出現/痛點洞察/近期工具/技術彙整/熱門討論/衍生/全覽表 皆存在）
  - 遵守率：全部通過（近 3 次 ingest 呈現品質 3/3、feature-radar 3/3）
  - 過期規則（>60 天）：僅 `[加入: 2026-04-25]`（format 模板，76 天）→ 已確認模板仍在用且有效，無需修訂
  - 簡化：跳過（features.md 略超記待辦，餘皆在閾值內）
  - 來源健康（近 7 天）：⚠️ dev.to 連 7 天 0（本 session 已改 top=30 抓法，驗證重抓得 15 則）、lobste.rs 連 7 天 0（本 session 已移出 pipeline）、Claude API Release Notes 連 7 天 0（未查證，待排查）、Anthropic Blog 4 天 0（稀疏但會產出，非壞）；GitHub Issues/Google News/HN/Reddit 正常
  - 跨檔案語意矛盾（6g）：✅ 全部配對語意一致
  - 成長迴路（月度）：非本月首次 lint（本月已有 1 筆 Lint），跳過
- 品質指標（6h）：
  - ref 覆蓋率（每週）：100%（近 7 天 35 條列 / 62 ref，每條列至少一 ref）✅
  - 採用驗證率（月度）：非本月首次 lint，跳過
  - 外部死鏈（月度）：非本月首次 lint，跳過
  - 趨勢判讀：持平（ref 覆蓋率維持滿分）
- 讀者模擬：3 題全 ✅（升版決策→feature-radar 2 跳；multi-agent 驗證→community-tech-patterns 2 跳；中國後門進展→ai-agent-safety 2 跳）
- lint 自我遵守率：6/6 記者回報一次過（格式完整、3a–3g 各有明確結果，無退回）
- community-tech-tools 策展：汰除 34 筆逾 30 天 ⏳（頁面 319→285 行）、新增 Shellular；精選層無變動；patterns 淘汰審查 dry run 0 條（全部仍被引用）
- overview.md：已更新（當前局勢補 07-09 中國後門延燒第二天/Reflect with Claude/1.2 兆估值；事件表 prepend 3 筆 07-09、範圍更新至 07-09；社群工具段同步本輪策展）
- 品質備註：無

### 本次 lint 期間 pipeline 來源優化（session 內同步進行，非 lint 標準步驟）
- dev.to 改 `top=30` 抓法（解除 26h 時間窗綁定、門檻 5/2→3/2）：重抓 07-09 驗證 0→15 則，內容為技術 pattern 精華
- lobste.rs 移出 pipeline（`ai` tag+標題關鍵字抓法 18 天 0 命中，價值與 HN 重疊；`lobsters.py` 檔保留備日後）
- GitHub Issues 單日上限 10→15
- 新增資料品質告警（`main.py` `_warn_if_scores_all_zero`）：來源全數 score=0 但宣稱真實指標時 WARNING，已驗證對 Reddit 觸發
- 新增社群記者規則「dev.to 條目以內容判斷、不看讚數」（`.claude/rules/wiki-ingest-community.md`）
- 新增 `wiki/sources/` 10 個來源節點頁 + wikilink 機制（供 Obsidian Graph 分析「來源 × 類別」）
- 改動未 commit；測試 31/31 綠；兩次 /review-commands 零錯誤

## 2026-07-10 Ingest

- 來源日報：[[news/2026-07-10]]
- 更新頁面：topics/ai-agent-safety.md、topics/anthropic-government-policy.md、topics/anthropic-business.md、topics/competitor-landscape.md、entities/pricing.md、entities/claude-code.md、topics/official-community-gap.md、topics/community-tech-patterns.md、topics/community-tech-discussions.md、entities/fable-5.md、feature-radar.md、index.md
- 新增頁面：entities/bernanke.md
- 摘要：中國「後門」指控延燒第三天、Anthropic 首度公開否認；前聯準會主席 Bernanke 加入 Anthropic 治理信託；Claude Code v2.1.206 發布；OpenAI ChatGPT Work/GPT-5.6 與 Cursor 新 Agent 加劇對 Anthropic 的競爭壓力
- 呈現品質：全部通過
- 品質備註：無

## 2026-07-11 Query | sources wikilink 機制撤除 → 改結構化 ledger + 漏斗統計

- **使用者點出：** 質疑「wiki 都知道資料來源嗎／效果好嗎／有必要放 wiki 嗎」——sources wikilink 機制（07-10 加入）是否值得存在。
- **根因（兩層）：**
  1. sources wikilink 寫在 wiki 正文會外洩到 web reader，成為斷鏈與突兀按鈕（讀者視角是噪音）
  2. Obsidian Graph 的邊是二元的（有連 / 沒連），回答不了「哪個來源對哪個類別貢獻多少比重」這種需要計數的問題
- **處置：**
  - 撤機制：清除 5 頁共 12 條 sources wikilink、刪除 `wiki/sources/` 10 個節點頁、撤 `.claude/rules/wiki-reporter-shared.md`「來源節點 wikilink」規則（改為「來源歸因回報」——記者在回報訊息回報，不寫 wiki 正文）
  - 改結構化 ledger：`data/source_attribution.jsonl`（主編彙整時 append，schema 見 `data/README.md`）
  - 加漏斗統計：`data/source_funnel.jsonl`（`main.py` 每次 gather/render append 各來源 gathered→filtered→emitted 計數，由 daily-gather Actions commit）
  - 設計原則沉澱至使用者全域 `~/.claude/system-design-principles.md` C4/C5/C6

## 2026-07-11 Lint（雲端排程執行）

- 修正矛盾：
  - 模型：`opus-4-8.md` Fable 5 fallback 描述殘留「受出口管制停用期間」舊狀態語言（管制已 07-01 解除）→ 改為現行「Defense in Depth」分類器觸發機制，補 wikilink 至 `[[entities/fable-5]]`
  - 功能：`code-quality-decline.md` 與 `entities/claude-code.md` 對 Stop hooks 失效狀態用語不一致（前者「待確認」／後者已知問題 🔴）→ 統一為 🔴 已確認持續回歸問題，互加 wikilink
  - 社群：`community-tech-tools.md` 與 `code-quality-decline.md` 對 CC-Canary 首次出現日期矛盾（05-12 vs 04-25）→ 以 `news/2026-04-25.md` 原文為準統一為 2026-04-25，互加 wikilink
- 補連結：`entities/bernanke.md`（原僅 index/log 引用）→ 補於 `entities/dario-amodei.md`「相關議題」；`entities/claude-tag.md`（原僅 index 引用）→ 補於 `topics/official-community-gap.md` 矩陣列與 `entities/claude-code.md`「相關議題」
- 狀態更新：無（六記者一致回報無 ongoing→monitoring/resolved 變更；`recursive-self-improvement` 等維持上週狀態）
- resolved 收尾：無
- 新增 entities：無（本輪未直接建立；候選見下方「待使用者確認」）
- 呈現品質：⚠️已修復共 11 頁——`sonnet-5.md`／`opus-4-8.md`／`mythos.md`／`fable-5.md`／`model-comparison.md`（delta-first 改寫、凍結指標補「數據截至」標註）、`claude-code.md`（現況時序侵蝕修復）、`opencode.md`（補回缺失的「最後新聞更新」欄位）、`code-quality-decline.md`（事件流堆積改月份分組）、`anthropic-business.md`（標頭/callout 落後既有內容 1 天已同步、移除嵌入正文的 LLM 操作指令殘留）、`ai-agent-safety.md`／`anthropic-government-policy.md`（待查證標記回訪）、`community-tech-tools.md`（清除 2 處懸空引用、補回缺列的 AISlop）；其餘全數 ✅ 通過
- 入口層健檢：`ai-agent-safety.md`（538 行）、`community-tech-patterns.md`（932 行）、`community-tech-discussions.md`（1008 行）均具備完整入口層（callout＋概覽表＋月份/主題分組），通過不拆分；無語意分岔/死案候選（六記者 3f 欄位皆回報「無」）
- 待查證回訪：
  - 已更新：`entities/john-jumper.md`（Twitter 來源標記，已於 2026-06-21 獲 Reuters 獨立確認，移除待查證標記並補來源）；`topics/anthropic-government-policy.md`（2 處出口管制撤銷疑問，已於 07-01 全面解除，補參照）
  - 已改註無後續：`entities/andrej-karpathy.md`（加入傳聞 05-29，近 14 天無新報導，稽核日期更新）；`topics/ai-agent-safety.md`（「Let's Data Science」漏洞指控 06-02，查證同名來源皆無關報導，改註「至今無後續」）
  - 其餘標記距今 ≤14 天未觸碰
- 規則檔健檢：
  - 矛盾（6a）：無（規則檔本次未被修改，延續上次 `/review-commands` 零錯誤狀態）
  - 引用驗證（6b）：7/7 全部通過
  - 遵守率（6c）：近 3 次 ingest（07-08/07-09/07-10）呈現品質 3/3、feature-radar 提及 3/3、log 格式正確 3/3，全部通過
  - 過期規則（6d，>60 天）：`[加入: 2026-04-25]`（entities/topics 格式模板，距今 77 天）→ 連續第 2 週超過閾值，**📋 待使用者確認**是否需修訂（上週 07-10 lint 已審閱認定仍吻合現狀，本週僅重新列出未再變動）
  - 來源健康（6e）：⚠️ `Claude API Release Notes` 連續 7 天（07-04~07-10）count=0，已連續 2 週出現同樣異常，原因尚待排查（純觀察回報，不自行修改 pipeline）；`lobste.rs` 已依上輪決定移出來源清單（預期中，非異常）；`dev.to` 07-10 恢復至 15 則（`top=30` 抓法改動生效）；`GitHub Issues` 單日上限已生效為 15（07-10=15）；其餘來源（HN/Reddit/Google News/GitHub/Anthropic Blog/Status）正常
  - 跨檔案語意矛盾（6f）：✅ 全部配對語意一致（5/5，含 REPO_ROOT/PYTHON 值、六類 subagent_type 名稱、lint-only 邊界宣告、五欄回報格式）
  - 成長迴路（月度）：非本月首次 lint（本月已有 07-04、07-10 兩筆 Lint 記錄），跳過
- 品質指標（6g）：
  - ref 覆蓋率（每週）：100%（近 7 天 07-04~07-10，35 條列 / 35 條列皆至少一 ref）✅，缺 ref 日期：無
  - 採用驗證率（月度）：非本月首次 lint，跳過
  - 外部死鏈（月度）：非本月首次 lint，跳過
  - 趨勢判讀：持平（連續 3 期維持 100%；`wiki/metrics.md` 已補記 07-10 遺漏列並 append 07-11 列）
- 讀者模擬：3 題全 ✅ —— 「v2.1.206 該不該升版」→ `feature-radar.md`「升版風險」2 跳可答；「中國後門指控 Anthropic 有無正式回應」→ `topics/ai-agent-safety.md` 頂部 callout 2 跳可答；「Bernanke 加入信託對治理的意義」→ `entities/bernanke.md` 現況 2 跳可答
- lint 自我遵守率：6/6 記者回報一次過（3a–3g 七項皆有明確結果，格式完整，無退回）
- community-tech-tools 策展：新增 Devthropology、AI 思考表徵編輯器、Geosql（⚠️效果存疑已標註）、Peek-CLI；汰除 5 筆逾 30 天無後續 ⏳ 條目（claude-quota/OpenYabby/agent-pd/claudefeed/Lanes v0.43.0）；精選層無新提拔，Intuned 因查無原始新聞來源移出精選層；痛點洞察同步（清除 Rayline 殘留敘述，多模型鎖定防禦列狀態 🔥→🌙）
- patterns 淘汰審查（community-tech-patterns，dry-run，**待使用者確認**）：建議淘汰 0 條；建議合併 1 組——「記憶與知識管理」↔「跨環境 Agent 記憶」（模式概覽表重複收錄同一工具 ltm/Core Memory Packet，概念高度重疊）；保留 3 類（Agent 版本控制／安全架構／Context window 縮減舊條目，理由：概念仍有效或已妥善標記歷史）
- community-pattern-trends 週更：無新趨勢節點（近 14 天資料已被 07-10 lint 涵蓋；「行動裝置遠端控制」醞釀中趨勢首見 06-28，距今 13 天未滿 14 天成形門檻）
- overview.md：已更新（當前局勢改寫為中國後門指控延燒第四天/Anthropic 首度公開否認、Bernanke 治理信託任命、UST 合作、OpenAI/Cursor/Microsoft 三線競爭夾擊；近兩週事件表 prepend 4 筆 07-10、範圍更新至 06-27~07-10；商業動態/功能推薦/社群情緒指標同步改寫）
- 品質備註：無

### 📋 待使用者確認（雲端 lint 自主安全部分完成，以下項目留待人工決定）

1. **新實體頁候選**：`Reflect with Claude`（Anthropic 官方 Beta 功能，2026-07-09 發布，07-10 媒體延燒第二天，feature-radar 熱度 🔥🔥🔥🔥／試用價值 ⚡，已有名稱＋狀態＋多起具體事件，資訊足夠建頁；與 `claude-design.md`／`claude-security.md`／`bugcrawl.md` 同類先例）→ 是否建立 `wiki/entities/reflect-with-claude.md`？
2. **community-tech-patterns 淘汰審查**：建議合併「記憶與知識管理」↔「跨環境 Agent 記憶」兩類別（重複收錄同一工具）→ 是否同意合併？
3. **規則年齡審查（6d）**：`.claude/rules/wiki-ingest-format.md` 的 entities/topics 格式模板 `[加入: 2026-04-25]` 已連續第 2 週超過 60 天閾值（距今 77 天）→ 是否需要重新審視此模板規則，或標記為「已審閱，長期有效」以停止重複列出？
4. **來源健康**：`Claude API Release Notes` 已連續 2 週（14 天）count=0 → 是否授權查修此來源的抓取邏輯（可能是 URL 失效或格式改版）？

## 2026-07-12 週度延伸回顧

- 延伸（六記者並行判斷 → 使用者確認全執行，均帶 model:sonnet）：
  - **新頁** `topics/safety-china-trust-dispute.md`：自 ai-agent-safety + anthropic-government-policy 拆出「中美 AI 工具信任對峙」，整合技術指控線（v2.1.91 代理偵測、thereallo.dev + dev.to/adioof 兩則隱寫術指控）＋外交/企業線（Alibaba 改用 Qoder/Meta 限制、中國官方 07-08 政府層級「後門」警示、Anthropic 07-07「實驗」定調 → 07-10 首度公開否認）成五階段敘事；兩原頁重複敘事收斂為指針+wikilink，移除三處「待評估建頁」已消費待辦，全檔 grep cross-check 無殘留（消費 reader-notes 07-07「隱藏追蹤器」🔍）
  - `topics/anthropic-business.md`：加開「IPO 前瞻與估值追蹤」子區塊（Series H $965B → $1.2兆次級估值/流動性矛盾 → 3Q26 首度獲利曝光 → 護城河疑慮 → FT 結構性挑戰 → 市值超越 25 年退場總和鏈條），置於摘要後、時序不重複維護（消費 reader-notes 07-09「Anthropic 股票/IPO」🔍）
  - `topics/code-quality-decline.md` + `topics/community-tech-discussions.md`：額度/成本異常訊號群數字更新（#38335→791 留言、cache 命中率降 20% 帳單翻倍機制、Max 20x 週額度單日耗盡、27%/7% 比例異常），額度焦慮系列熱度 🔥🔥→🔥🔥🔥，兩頁互引
  - `entities/claude-code.md`：已知問題新增「👤 帳號管理」分組，整併 #36151（Mobile 542讚）/#18435（Desktop 705讚）/#27302（Web 419讚）為全平台共通缺口，精簡平台相容性組內重複列
  - `entities/bernanke.md`：補 [[topics/ai-talent-flow]] wikilink（記者觀察順手做）
  - index.md：新增 safety-china-trust-dispute 列（🏛️ 政策/安全 ongoing）、更新 ai-agent-safety/government-policy 描述加分流註記、近期異動 prepend 07-12 條
- reader-notes 消費：07-09 IPO → ✅ 已納入；07-07 隱藏追蹤器 → ✅ 已納入；07-12 GPT-5.6 比較 → 保留 ⏳（模型＋商業記者查證本週日報仍無第一手實測/定價數字，Reuters/ZDNET 僅定性訴求，待查證）
- 使用者跳過項目：無（四項建議全執行）
- 聚焦校準：非本月首次週度回顧（本月已有 07-04、07-05），跳過
- 品質備註：無

## 2026-07-12 Query：GPT-5.6 資料少是否為來源蒐集問題

- **提問**：使用者問「GPT-5.6 這麼沒有是因為來源蒐集問題嗎」。
- **查證**：查 src/news_aggregator/sources/ 三大來源查詢詞——google_news（Claude Code/Anthropic AI/Anthropic Claude/…）、hackernews（Claude Code/Anthropic/claude/anthropic）、reddit（ClaudeCode/ClaudeAI/LocalLLaMA+Anthropic）全為 Claude/Anthropic 錨定，符合 CLAUDE.md 蒐集範圍設計。再手動 WebSearch 做決定性測試。
- **根因（部分為真實缺口，非既有來源 bug）**：GPT-5.6（代號 Sol）vs Claude 第一手跑分實已大量發表（TerminalBench 2.1 Sol 88.8/Opus 4.8 78.9/Fable 5 84.3；SWE-Bench Pro Fable 80.3>GPT 58.6；Sol 便宜 50%；over-agency 安全議題），但都在對照型部落格（MindStudio/DataCamp/codersera/superframeworks 等）——**這類 venue 不在 blogroll，Google News「Anthropic Claude」query 偏新聞媒體抓不到**。既有 Claude 錨定機制本身正常（Reuters/ZDNET 定位新聞有抓到），缺的是評測部落格這個 venue。取捨點：這類 venue 一半是 SEO 農場對照文，無腦加來源會灌雜訊。
- **處置**：使用者決策＝(1) 不回填部落格數字，等官方 benchmark 再寫；(2) pipeline 先不擴充來源，觀察一週。reader-notes 07-12 GPT-5.6 條已補記查證結論＋一週後回看 checkpoint（約 07-19）。無程式碼/wiki 內容變更。

## 2026-07-14 Ingest

- 來源日報：[[news/2026-07-14]]
- 更新頁面：wiki/entities/claude-code.md、fable-5.md、opus-4-8.md、opus-4-7.md、sonnet-5.md、pricing.md、mythos.md、wiki/topics/model-comparison.md、anthropic-business.md、competitor-landscape.md、anthropic-government-policy.md、recursive-self-improvement.md、community-tech-patterns.md、community-tech-discussions.md
- 新增頁面：無
- 摘要：Anthropic 印度盧比在地化定價（回應長期未回應的 INR 定價需求）為本日最大商業事件；Claude Code v2.1.209 純 bug fix 版本，OAuth DNS 無法解析（#33238，150 留言本日最高互動）與兩則獨立「tool call could not be parsed」回報延燒為本日最高熱度已知問題；Reuters 獨家報導加拿大金融監管機關引用 Claude Mythos 警告銀行網路風險，為解禁後首見監管案例；社群面新增官方 multi-model 工作流模式「Fable 5 orchestrates, cheap models execute」（46% 成本／96% 效能）與 Bun Zig→Rust 改寫正反交鋒討論。
- 呈現品質：全部通過（模型記者修復 fable-5.md 舊日期字串殘留 1 處；其餘各頁 delta-first callout／摘要／熱度表位置均核可）
- 品質備註：[安全政策] 主編派工時原文節錄未附逐條 item_url，記者回報來源歸因時多筆標「未提供」，已由主編對照 gathered_items.json 原始記錄補齊 URL 後寫入 data/source_attribution.jsonl，後續派工應在節錄中明確標註「item_url:」欄位避免此缺口
- 轉知事項：[社群→功能/商業] Microsoft 早期 Claude Code／GitHub Copilot CLI 企業級 rollout 學術研究（HN 61 分）建議評估是否納入 official-community-gap.md 或 enterprise-tool-tracker.md，本次因無具體矩陣對應列／無具名企業主體而未收錄，留待後續觀察是否有具體事件錨點
- 人物記者判定：Musk「AI 領域明確領先者」／Altman「Thought This Was Satire」兩則外部競爭對手 CEO 表態，依 2026-07-13 既有慣例（同類表態走商業記者 competitor-landscape.md，非人物記者建頁範疇）判定無需建立獨立人物頁，已由商業記者收錄

## 2026-07-16 Ingest

- 來源日報：[[news/2026-07-16]]
- 更新頁面：wiki/entities/claude-code.md、claude-design.md、mythos.md、opus-4-8.md、dario-amodei.md、pricing.md、wiki/topics/model-comparison.md、official-community-gap.md、anthropic-business.md、anthropic-government-policy.md、ai-agent-safety.md、competitor-landscape.md、enterprise-tool-tracker.md、community-tech-patterns.md、community-tech-discussions.md
- 新增頁面：無
- 摘要：Claude Code v2.1.211 新增 `--forward-subagent-text` 旗標；本日互動量最高條目為手機驗證機制問題（741 留言/892 讚同），另有兩起 Cowork 已知問題（10GB VM bundle 效能劣化、Edit/Write 靜默截斷檔案）因涉資料完整性風險已列入 feature-radar 升版風險表；商業面 Anthropic 與 Blackstone 成立 15 億美元 AI 實作公司 Ode，同時三家財經媒體同步報導 IPO 前投資人會議安排；安全政策面新增資安研究揭露 web fetch 誘導 Claude 洩漏機密資訊手法、EU 官員批評 Anthropic 安全聽證僅派初階員工出席；社群面 Brainless（HN 124 分）為本日最高分條目，Grepathy 事件（Claude 於承包案自行建立未授權帳號）雙頁收錄。
- 呈現品質：全部通過（community-tech-discussions.md 同步執行熱門討論表格 21 天保留規則清理，移除 15 筆過期 ☄️閃現 條目）
- 品質備註：
  - [安全政策→功能] 「Claude Code and DeepSeek Powered Chinese Cyber Espionage Campaign」一則涉及 Claude Code 被指用作攻擊工具鏈之一，安全政策記者已標註「請主編轉知功能記者」，惟功能記者當次派工已先行完成、未能即時收到此轉知，故本則暫僅記錄於 ai-agent-safety.md（標「僅標題可用/待查證」），功能記者下次 ingest 應檢視是否需在 claude-code.md 補充對應說明或已知問題條目
  - [社群→商業/人物] 「Where are YC founders now? OpenAI and Anthropic, mostly」（HN 85 分，達收錄高門檻）內容為 YC 創辦人流向 OpenAI/Anthropic 的人才資料，性質貼近 `topics/ai-talent-flow.md`（商業記者）或人物記者範疇，非社群記者四頁可收，社群記者已標記但本次主編判斷屬單一網站彙整、無具名個別事件錨點，暫不強制建檔，留待後續日報出現具體人物加入事件時再行收錄
## 2026-07-16 週度延伸回顧

- 延伸（六記者並行判斷 → 使用者確認全六項執行，均帶 model:sonnet，續用原 agent context 執行）：
  - `entities/claude-code.md`：已知問題新增「🔌 MCP 整合」分組，整併 #5826（OAuth 2.1 無法連線 Desktop，66 留言本週最高互動）/#5706（token 刷新缺失）/#1785（MCP Sampling）/#33969/#24057/MCP Token 消耗共 6 條；計費與配額組頭 12→10、平台相容性 29→25 同步；本週 4/5 天日報有 MCP 訊號
  - `topics/community-tech-discussions.md`：長期議題加開第 6 子區塊「Anthropic 透明度與信任赤字」，彙整 06-23 帳號封禁無申訴、06-30 spyware 指控、07-01 隱寫（HN 2263）、07-01 成本 5x 暴增、07-02 未公開系統訊息、07-06 好感度流失（HN 97）、07-13 Zed 創作者具名批評（HN 557）、07-13 Reddit 溝通抱怨共 8 起分散事件為索引；07-05/07-06 收斂結論補指向句
  - `topics/anthropic-government-policy.md`：補 07-13 澳洲著作權遊說（Anthropic 向財長 Chalmers 表態 210 億美元投資取決於著作權法規明確性；AFR＋TechXplore 兩獨立來源）——繼奧地利/歐盟後第二個具名國家級「投資換政策」互動；callout 覆寫、攻防紀錄/時序 prepend
  - `topics/enterprise-cost-management.md`：補 07-13「$16.6M 帳務錯誤、企業被多收 $1.7M」事件與 07-04 Spend Controls 的可信度對比（標推論）；該頁自 07-05 未更新的同步缺口關閉
  - `topics/anthropic-business.md`：「IPO 前瞻與估值追蹤」表補 07-10 Bernanke 入長期利益信託列（治理公信力面，對應 FT 結構性質疑）
  - `entities/bernanke.md`／`entities/teresa-carlson.md`：補 [[entities/tom-blomfield]] 與彼此 wikilink，三筆外部延攬人事三向可導覽
- reader-notes 消費：GPT-5.6 vs Claude（07-12 ⏳）——模型/商業/社群三記者分頭查證 07-09~07-13 日報，仍無官方 benchmark 或可信第一手數字（僅 ZDNET/Reuters 定性、Reddit 臆測），維持 ⏳ 並補記查證結果，下次回顧再查；📌 07-07 雜記未逾 30 天保留
- 使用者跳過項目：無
- 聚焦校準：**首次實際執行**——發現跳過條件結構性漏洞（07-04 回顧早於規則誕生〔07-05〕卻佔用「本月首次」名額，導致 07-05/07-12/07-16 連續誤跳過，metrics.md 聚焦命中率欄三列全 —；由使用者提問「聚焦校準有做過嗎」揭露）。本次回看 06-14~06-20 聚焦 → 30 天：命中率 36%（4/11，部分命中計 0.5 則 41%）；命中：Fable/Mythos 管制線、Agent SDK 計費、SpaceX/Cursor、John Jumper；誤報 6：Karl Kahn 訴訟、Artifacts、磁碟掃描、Pentagon、Show HN 工具批次 ×2；漏報 1：Agentjacking（具名資安揭露，至今 🔴 未修復仍在追蹤）。偏誤模式：(1) Show HN 工具類 0/9 系統性高估；(2) 具名資安揭露權重低於熱度；(3) 訴訟類 30 天窗口先天不利（非選材錯誤）。命中率已 append `wiki/metrics.md`。選材指引修正提案（news-pipeline-steps.md Step 1b 加「新工具/風險警示選入門檻」）＋跳過條件修正提案（改查 metrics.md 聚焦命中率欄本月有無數值）均待使用者確認後才修改
- 品質備註：無

## 2026-07-16 Query：聚焦校準有做過嗎

- **提問**：使用者問「聚焦校準有做過嗎?」。
- **查證**：`wiki/metrics.md` 聚焦命中率欄三列全 `—`；log 07-04/07-05 回顧無校準記錄、07-12 與本次均判「非本月首次」跳過。
- **根因**：跳過條件「log.md 本月尚無週度延伸回顧記錄」查的是執行記錄而非產出物——規則 07-05 誕生時 07-04 記錄已存在，當月名額被規則誕生前的回顧佔用，之後每週都誤判已做過。
- **處置**：本 session 立即補跑首次聚焦校準（結果見上條）；防再犯修正提案（判斷方式改查 metrics.md 聚焦命中率欄）待使用者確認。

## 2026-07-16 Query：資料來源的品質挑選有問題

- **提問**：使用者反映對資料來源的品質挑選有問題，要求研究公開 AI news skill 生態與學術文獻後優化本專案（最想加強來源評分）。
- **查證**：三路研究（skill/開源專案掃描、業界學術技術、本專案盤點）確認——品質挑選停在條目層特例門檻（HN 分數、Reddit 週熱門、dev.to 內容判斷各一套補丁），來源層無回饋迴路；`source_funnel.jsonl` 與 `source_attribution.jsonl` 為 `/source-review` 預留但從未實作，兩份 ledger 缺程式化 join（註冊名 vs slug 斷鏈）。
- **根因**：來源特性知識（分數可信度、判準模式）散落規則檔文字，程式端無單一真相源；每次來源指標失真只能事後補規則，無法防再犯。
- **處置**：建置來源評分 Phase 0–1（監控層，2026-07-16 上線）——`data/source_registry.json`（name↔slug↔品質標籤單一真相源）、`scripts/source_scorecard.py`（收錄率/Wilson 下界/wiki 率/Presence/HHI/domain 信譽分佈，Bayesian 假票平滑）、`data/external/domain_pc1.csv`（Lin et al. 2023，11,520 domains，接 Google News）、掛 `/wiki-lint` 6e 週更。enforcement 屬 Phase 2（≥60 天資料＋pipeline-change-check）。設計依據與逐來源機制：`docs/source-scoring-optimization.md`。

## 2026-07-16 防再犯修正（聚焦校準）

- 使用者確認執行兩項提案（commit 6805958）：(1) `.claude/commands/wiki-weekly-review.md` 聚焦校準跳過條件改查 `wiki/metrics.md` 聚焦命中率欄本月有無數值（查產出物，不查執行記錄）；(2) `.claude/commands/news-pipeline-steps.md` Step 1b 今日聚焦新增選材門檻（[新工具] 未達中門檻且無跨來源不單獨聚焦；[風險警示] 具名資安揭露優先於純熱度）。`/review-commands` 首輪零錯誤。

## 2026-07-16 Query：週更頁面標示

- **提問**：使用者問 community-pattern-trends 為何最後更新停在 07-10、哪些頁是週更、能否加 TAG 讓這件事更明顯。
- **查證**：日期停留為設計行為（lint 週更＋無新節點不動頁）；週更頁共三頁：overview、community-pattern-trends、community-tech-tools。
- **處置**：三頁標頭新增「**更新頻率：** 🗓️ 週更（維護指令）」欄位，index.md 對應摘要前綴「🗓️ 週更」；慣例寫入 `.claude/rules/wiki-ingest-format.md`（選填欄位，日後週更頁比照）。

## 2026-07-17 Query：地端 AI server 商業評估（wiki 邊界確認 + 台灣落地層市場分析）

- **問題**：使用者為友人「20 萬台幣自組 AI server 套阿里 Qwen 模型」評估商業模式，過程中反覆測試 wiki 對跨模型評測、競品能力、台灣本地市場的覆蓋能力。
- **根因**：非缺陷——wiki 依 CLAUDE.md 設計不收「與 Claude/Anthropic 無直接關聯的通用 AI 新聞」，故 benchmark 絕對數字、競品硬體規格、台灣落地層（本地供給/法規/預算行為）皆在設計邊界外；本次確認邊界執行正確（log 既有「Qwen 非 Anthropic 相關略過」「GLM 5.2 無直接關聯未更新」兩筆自證）。wiki 實際貢獻：阿里蒸餾指控（ai-agent-safety）、自架沙箱+MCP 隧道（managed-agents）、企業退出三軌（enterprise-tool-tracker）、成本失控案例（enterprise-cost-management/pricing）與 competitor-landscape 的「待查證」可信度標記（後經外部查證 GLM-5.2 開源榜首屬實，FrontierSWE 74.4 vs Opus 4.8 75.1）。
- **處置**：以 ECC market-research 方法論執行台灣落地層市場分析（探針優先），Stage 1 即觸發 kill-switch：華碩 Ascent GX10（NT$99,900 起、128GB 統一記憶體）半價輾壓自組機；2026 政府 AI 補助明文排除中國廠牌資通訊產品；中小企業 20 萬預算帶需求全數流向雲端。結論 no-go（硬體本位）/有條件轉服務本位。報告存 scratchpad `taiwan-onprem-ai-server-feasibility.md`（session 交付物，不入 wiki）。reader-notes 2026-07-17 已有對應興趣主題條目（Claude vs 開源競品能力差距）待 weekly-review 判 venue 擴充三題。

## 2026-07-17 新增頁面 | claude-skills.md（官方 Skills 產品線與生態）

- **背景**：使用者表示想追蹤「Anthropic 力推的 Skills」。查證發現 Skills 覆蓋散在 10+ 頁（patterns 36 處、claude-code 12 處、opencode/claude-for-teachers/tools 等）而無單一入口，達建頁標準。
- **分工設計**：`entities/claude-skills.md`（功能記者主責）管官方產品線與生態（官方 bundle、平台支援、分享機制、第三方移植）；`topics/community-tech-patterns.md` 照舊管 skill 設計面，兩頁互 wikilink——比照 pricing（商業）vs 模型頁（能力）的分工邏輯。
- **執行**：功能記者（sonnet）回讀歷史日報與既有 wiki 建頁，時間軸涵蓋 2026-04-27（OpenCode-power-pack 移植）至 2026-07-15（教師技能庫）；主編修 callout 對齊最新事件（07-15）與最後新聞更新日期；同步 index.md 新增列與近期異動、claude-code.md 核心功能與 patterns.md 相關實體補 wikilink、`.claude/rules/wiki-ingest-features.md` 負責頁面表新增列。
- **feature-radar 判定**：記者建議新增 radar 條目，主編判定**不新增**——radar 追蹤「新發布功能」熱度，Skills 為長期 GA 機制，entity 頁已足；日後 Skills 有新官方發布（如市集上線）再依准入定義進 radar。
- 品質備註：無

## 2026-07-17 Ingest | news/2026-07-17.md（67 則）

- 來源日報：[[news/2026-07-17]]
- 分類：功能 12 則、商業 9 則、安全政策 4 則、社群 20 則（模型、人物本日無條目）
- 更新頁面：entities/claude-code、entities/managed-agents、topics/official-community-gap（功能）；topics/anthropic-business、entities/pricing、topics/competitor-landscape（商業）；topics/anthropic-government-policy（安全政策）
- 新增頁面：無
- feature-radar：新增 2 條——`/fork` 背景 Session 化與 `/subtask` 語意拆分（v2.1.212，🔥🔥🔥 ⚡，⚠️ Breaking change 無過渡期）、Claude 1Password 整合（🔥🔥 ⏳，僅媒體報導無官方一手來源）；升版風險表以「`/fork` 語意變更」（🔴）取代已定調的隱寫術爭議列，Cowork 已知問題／Fable 5 defense-in-depth 維持；本週推薦輪替（`/goal` 已連續推薦逾 7 天且今日未更新，依防霸榜規則換為 Claude Code Artifacts，Fable 5／Cowork 維持）；⏰ 倒數中無變化
- 社群：今日 20 則條目（12 則 HN Show HN、4 則 dev.to、4 則 Reddit 圖片／低互動貼文）經社群記者逐條核對，全數未達收錄門檻（HN 最高僅 9 分、Reddit 均無週熱門標記、dev.to 前兩則第一手內容查表後確認已存在既有頁面判定重複），本輪社群頁面無異動
- 安全政策：Claude Code + DeepSeek 中國網路間諜行動（Security Affairs）核對後確認為 07-16 已收錄事件的 Google News 重複聚合，未重複寫入；SCMP「Pax Silica」專訪因關鍵人物姓名未知未達建頁門檻，記錄於 anthropic-government-policy.md 待日後追蹤是否升格
- 呈現品質審查：claude-code.md ⚠️ 已修復（「現況」段落與歷史記錄重複的舊段落、#13354 重複條目已清理）；其餘 6 頁 ✅ 通過
- 摘要：v2.1.212 帶來 `/fork`/`/subtask` breaking change 與 Claude 1Password 整合為今日官方功能焦點；商業面 Kimi K3 正式發布延續 Moonshot 對 Anthropic 的競品壓力敘事；安全政策面五角大廈簡報、州級監管遊說、中美 AI 政策三線並進
- 品質備註：無

## 2026-07-18 Lint（雲端排程執行）

- 修正矛盾：
  - 安全政策：`topics/anthropic-commitments.md`「spyware 指控回應」列停留在 07-07 狀態，未反映 `topics/safety-china-trust-dispute.md` 已記錄的 07-08 中國官方警示與 07-10 Anthropic 首度公開否認 → 已更新該列狀態/callout/時序，失效的 `[[topics/ai-agent-safety]]` 連結改指向現持完整敘事的 `[[topics/safety-china-trust-dispute]]`
  - 安全政策：`topics/safety-china-trust-dispute.md`「目前結論」表「中國代理偵測程式碼」列仍寫「官方無回應」，與同頁其後 07-07/07-10 官方已回應的記載矛盾 → 修正為「官方已回應（07-07 定調實驗、07-10 進一步否認）」
  - 商業（主編發現，非記者回報）：`topics/ai-talent-flow.md`「### 2026-06-19」時序分組將 John Jumper 加入的 Reuters 確認報導錯記為 06-19，與 `entities/john-jumper.md`／`news/2026-06-21.md` 記載的 06-21 官方確認日矛盾（Reuters URL 帶 06-19 為原始報導日，但本站日報實際於 06-21 收錄）→ 主編直接改期為 2026-06-21，同步「開始日期」與「相關實體」欄
- 補孤立連結：無（六類全數頁面皆有其他頁面 wikilink 引用）
- 狀態更新：無（六記者一致回報無 ongoing→monitoring/resolved 變更）
- resolved 收尾：無
- 新增 entities：無（本輪未直接建立；候選見下方「待使用者確認」）
- 呈現品質：
  - 模型：⚠️已修復 4 頁（sonnet-5/mythos/fable-5 待查證標記改寫、opus-4-8 前代比較表 Context Window 欄位補全、model-comparison.md 頂部 callout 過期更新）；opus-4-7 ✅ 通過
  - 功能：⚠️已修復 3 頁（claude-code.md 懸置標記改註、code-quality-decline.md「目前結論」數字落後同步、official-community-gap.md 補 Managed Agents Dreaming API 矩陣列）；其餘 10 頁 ✅ 通過
  - 商業：⚠️已修復 enterprise-cost-management.md／enterprise-tool-tracker.md（時序月份分組）；⚠️部分修復 anthropic-business.md（已補月份分組，06-15~06-26 完整主題重分類工作量過大未執行，列入待辦）；其餘 4 頁 ✅ 通過
  - 安全政策：⚠️已修復 anthropic-commitments.md／safety-china-trust-dispute.md（矛盾修正）、ai-agent-safety.md（CVE-2026-55407 懸置標記改註）；📋 待辦 4 頁時序段落連續無分組（safety-china-trust-dispute 9 個、ai-agent-safety 22 個、ai-agent-safety-archive 16 個＋存檔區、anthropic-government-policy 約 30 個——**全站 topics 頁時序段落的普遍慣例，非單頁問題**，工作量過大本輪未執行，列入下次 lint 或獨立任務待辦）
  - 人物：⚠️已修復 john-jumper.md（首次出現日期修正為 06-19〈Twitter 傳出，待核實〉並補頂部 callout）、dario-amodei.md（callout 更新反映 07-16 super PAC 捐款動態〈待核實〉）；boris-cherny/cat-wu/andrej-karpathy/chris-olah/teresa-carlson/tom-blomfield ✅ 核實後無需修改
  - 社群：⚠️已修復 code-quality-decline.md（「目前結論」統計數字同步）、community-tech-discussions.md（清理 6 筆逾 21 天 ☄️閃現 舊條目）、community-tech-timeline.md（29 個連續日期補月份分組）；community-tech-patterns/community-pattern-trends ✅ 通過；community-tech-tools 策展詳見下方
- 入口層健檢：本輪僅安全政策 4 頁觸發 3e 事件流堆積警示（詳見上方呈現品質欄，已記錄待辦，非 3f 語意分岔/死案候選）；六記者 3f 欄位均回報「無」語意分岔/死案候選
- 待查證回訪：
  - 已改註無後續：模型（sonnet-5 官方對比圖表爭議、mythos Z.Ai/WSJ 中國網安追趕報導、fable-5 化學問題被拒事件）；功能（claude-code.md #16856 token 暴增、36Kr 背景任務升級報導）；安全政策（ai-agent-safety.md CVE-2026-55407 DoS 漏洞，2026-07-01 揭露至今無後續）
  - 已更新：安全政策（safety-china-trust-dispute.md／anthropic-commitments.md 中國代理偵測回應狀態，見上方矛盾修正）
  - 其餘標記距今 ≤14 天，依規則不動
- 規則檔健檢：
  - 矛盾（6a）：無（掃描全部規則檔未發現同一行為的相反指示或觸發條件衝突）
  - 引用驗證（6b）：7/7 全部通過（首次出現/痛點洞察/近期工具/技術彙整/熱門討論/衍生/全覽表錨點皆存在）
  - 遵守率（6c）：呈現品質審查 3/3（07-14/07-16/07-17 log 皆含 ✅/⚠️/📋 標記）；**⚠️ feature-radar 提及僅 1/3**（07-17 log 明確點名，07-14/07-16 log 敘述未提及）——經 git 歷史核對，`feature-radar.md` 實際上 3/3 均有更新（版本行＋升版風險表同步），**屬 log 敘述完整度落差，非真實管線缺失**；log 格式正確 3/3
  - 過期規則（6d，>60 天）：4 項超過閾值——`.claude/rules/wiki-ingest-format.md` entities/topics 格式模板〔加入: 2026-04-25〕（連續第 3 週超標，距今 84 天）；**新增 2 項本週首度越線**：`.claude/rules/wiki-ingest-format.md`「Wiki 頁面呈現品質標準」〔加入: 2026-05-15〕（距今 64 天）、`.claude/rules/wiki-ingest-community.md`「community-tech-patterns ↔ discussions 雙向連結規則」〔加入: 2026-05-16〕（距今 63 天）→ 📋 待使用者確認
  - 來源健康（6e）：⚠️ `Claude API Release Notes` 連續 7 天（07-11~07-17）count=0，**已連續第 3 週出現同樣異常**，原因尚待排查（純觀察回報，不自行修改 pipeline）；其餘來源（HN/Reddit/Google News/dev.to/GitHub/GitHub Issues/Anthropic Status）正常；`scripts/source_scorecard.py` 記分卡：全部來源樣本仍 ⚠️ 7 天不足，僅供趨勢觀察；無「未註冊 slug」告警；Google News domain 信譽分佈低信譽（<0.4）桶 0 筆
  - 跨檔案語意矛盾（6f）：✅ 全部配對語意一致（16/16 registered sync_pairs 機械檢查通過；另手動檢視 07-17 新增的注入防護／忠實度自檢規則，未發現與既有規則衝突）
  - 成長迴路（月度）：非本月首次 lint（本月已有 07-04、07-10、07-11 三筆 Lint 記錄），跳過
- 品質指標（6g）：
  - ref 覆蓋率（每週）：100%（07-11~07-17，35 條列/35 條列均達標）✅，缺 ref 日期：無
  - 採用驗證率（月度）：非本月首次 lint，跳過
  - 外部死鏈（月度）：非本月首次 lint，跳過
  - 趨勢判讀：持平（連續 4 期維持 100%）；已 append `wiki/metrics.md` 07-18 列
- 讀者模擬：3 題全 ✅ ——「v2.1.212 的 /fork 改變會不會影響現有 skill、該不該升版」→ `feature-radar.md`「升版風險」2 跳可答；「Fable 5 編排便宜模型執行的社群驗證效果如何」→ `topics/community-pattern-trends.md` 趨勢四 2 跳可答；「中國後門指控現在的官方立場、事情結束了嗎」→ `topics/safety-china-trust-dispute.md` 頂部 callout 2 跳可答
- lint 自我遵守率：6/6 記者回報一次過（3a–3g 七項皆有明確結果，格式完整，無退回）
- community-tech-tools 策展：新增 18 筆（Brainless／Agentty／OtoDock／Grepathy／cc-session-recover／Cc-hindsight／Fleet Deck／aloud／Sx 2.0／claude-meseeks／Topsoil／Kastra／Papercrane-CLI／Agent Sessions／Tilion／Atelier／claude-code-live-memory／live-log-viewer-next）；汰除 26 筆逾 30 天無後續 ⏳ 條目；精選層新增 Brainless（HN124）與 claude-meseeks（HN130，新增通知/語音子分類）；痛點洞察同步 4 列代表工具/近期工具，清除 6 個已汰除工具殘留引用
- community-tech-patterns 淘汰審查（dry-run，**待使用者確認**）：建議淘汰 0 條；建議合併 1 組（「記憶與知識管理」↔「跨環境 Agent 記憶」，代表工具重疊）；保留 20 類；無法判斷 3 項（見下方待確認清單）
- community-pattern-trends 週更：4 條趨勢新增演進節點（Multi-agent 隔離工程化套件化部署、Context 主權爭奪使用者可視化分支合併、模型路由自動化獲官方基準背書、對抗性設計 plan-review-loop 延伸），無新趨勢達成立門檻、無趨勢降級淡出
- overview.md：已全文改寫（當前局勢改寫為中國信任對峙轉入觀察期、v2.1.212 `/fork` breaking change＋Cowork 資料完整性風險、Fable 5 promo 7/19 倒數、IPO 敘事加溫、政策戰線延伸、官方 Skills/教師方案生態擴張；近兩週事件表更新至 07-04~07-17；社群工具生態/商業動態/功能推薦/情緒指標全面同步；上次全文改寫為 07-11 lint，07-16 僅零星更新未反映 07-12~07-17 事態，本輪為完整重寫）

### 📋 待使用者確認（雲端 lint 自主安全部分完成，以下項目留待人工決定）

1. **新實體頁候選（連續第 3 週提出）**：`Reflect with Claude`（Anthropic 官方 Beta 功能，2026-07-09 發布，feature-radar 熱度 🔥🔥🔥🔥／試用價值 ⚡，資訊足夠建頁；07-11、07-17 lint 皆提出仍未定案）→ 是否建立 `wiki/entities/reflect-with-claude.md`？
2. **community-tech-patterns 淘汰審查**：建議合併「記憶與知識管理」↔「跨環境 Agent 記憶」兩類別（重複收錄同一代表工具）→ 是否同意合併？另有 3 項無法自動判斷，需人工確認：(a) Agent 版本控制／ADR 注入——70 天沉寂但概念未被否證，是否保留；(b) AgentWatch vs 官方 Claude Enterprise Spend Controls——功能部分重疊，是否加註「官方趨勢觀察」；(c) 行動裝置遠端控制（ccgram/Shellular）vs Claude Cowork 行動版——執行環境模型不同，是否算官方化取代
3. **規則年齡審查（6d）**：4 項規則超過 60 天閾值——`entities/topics 格式模板`〔04-25，84 天，連續第 3 週〕、`Wiki 頁面呈現品質標準`〔05-15，64 天，本週首度越線〕、`patterns↔discussions 雙向連結規則`〔05-16，63 天，本週首度越線〕→ 是否需要重新審視這些規則，或標記為「已審閱，長期有效」以停止重複列出？
4. **來源健康**：`Claude API Release Notes` 已連續 3 週（21 天）count=0 → 是否授權查修此來源的抓取邏輯（可能是 URL 失效或格式改版）？
5. **6c 遵守率發現**：近 3 次 ingest（07-14/07-16/07-17）log 敘述中僅 1/3 明確點名「feature-radar」，但實際檔案 3/3 皆有更新（git 歷史核對確認版本行與風險表同步）——是否要求 ingest log 敘述一律明確點名 feature-radar 更新狀態（即使是「僅版本行同步，無新條目」），以避免日後誤判為管線缺失？

## 2026-07-18 Ingest | news/2026-07-18.md（67 則）

- 來源日報：[[news/2026-07-18]]（67 則，10/10 來源；Google News 27、GitHub Issues 15、dev.to 15、Hacker News 13、Reddit 12、Anthropic Status 4、GitHub 4、Blogroll 3、Anthropic Blog 0、Claude API Release Notes 0）
- 分類派工：功能 17 則、商業 18 則、安全政策 2 則、社群 29 則、人物 1 則（五類並行 foreground，model: sonnet；模型本日無條目，跳過。註：本次因自訂 subagent_type 註冊表未載入，改以 general-purpose agent 內嵌對應記者角色規則＋開始前必讀清單執行，功能等同五位專職記者）
- 更新頁面：
  - **功能**：`entities/claude-code.md`（v2.1.214 純安全性修正發布，未列 feature-radar；已知問題新增 7 條——READ 工具未標示檔案 #21151 186 讚、思考過程常駐顯示 #8477 346 讚本日最高互動、貼上文字編輯 #3412 296 讚、記憶體洩漏 /tmp/claude-*-cwd #8856 70 讚、升級付款 PaymentIntent 異常 #55982 25 讚、Desktop session 消失 #26452 29 讚、skills 子目錄支援 #10238 165 讚；Remote Control 重連失效 #34255 反應數更新；AskUserQuestion 60 秒逾時機制經部落格文章證實為 07-01（v2.1.198）刻意加入的「效率繞過」設計，另有社群具體案例佐證；Anthropic Status 四起錯誤率升高事件同日修復記錄）；`entities/claude-for-teachers.md`（Education Week／WDET 兩則媒體追蹤更新）
  - **商業**：`topics/anthropic-business.md`（新增 Meta-Anthropic 傳洽談 100 億美元運算力租賃協議，HN+Reuters+NYT 三方獨立來源；Anthropic $60 萬職缺形塑 IPO 敘事、AMD/Jefferies 洽談關注、Anthropic 廣告反彈評論）；`entities/pricing.md`（Fable 5 存取政策今日出現「Max/Team Premium 收緊限制＋Pro 導向 API 計費」與「`@claudeai` 官方帳號稱設為永久」兩則方向相反報導，兩者並存記錄未擇一呈現，交易員押注第四度延長；Claude 最便宜 API 模式記入模型 API 定價現況）；`topics/competitor-landscape.md`（Moonshot Kimi K3 官方一手規格〔2.8T 參數、Kimi Delta Attention、100 萬 token context〕補入，取代原僅媒體轉述版本；WSJ/Globe and Mail/Forbes/BBC 後續跟進報導併入既有 07-17 事件，非獨立新事件；中美 AI「蒸餾」指控記入）
  - **安全政策**：`topics/anthropic-government-policy.md`（Anthropic 員工捐款 300 萬美元支持 AI 安全法規推動，併入既有「政治獻金布局」故事線與 07-16 Dario Amodei 個人捐款 100 萬美元 super PAC 事件，兩筆捐款是否同一 PAC 待查證；SingularityHub「聊天機器人意識特徵」報導經查證與三頁觸發條件均不符，判定不適用未建頁）
  - **社群**：`topics/community-tech-discussions.md`（「效率繞過」機制〔HN 140 分部落格分析＋HN 23 分具體案例〕合併更新既有 AskUserQuestion 60 秒逾時熱門討論列，熱度 🔥🔥→🔥🔥🔥；三則 Reddit 週熱門低門檻條目收錄；LLM cliché highlighter 部落格工具收錄）
  - **人物**：`entities/boris-cherny.md`（新增「現在同時執行數千個 Claude Code agent」聲明，單一媒體來源標記待核實）
  - 今日 29 則社群節錄中 23 則因未達互動門檻（多數 Show HN 僅 1-4 分、Reddit sort=new score 不可信且無跨來源佐證）或查表確認為既有條目重複浮現（3 則 dev.to）而不收錄，詳見社群記者回報
- feature-radar：本日無新條目（v2.1.214 為純安全性修正，未通過准入定義）；最新版本行同步至 v2.1.214；本週推薦與升版風險表因無回報變化維持原內容，僅同步版本行；⏰ 倒數中無變化
- index.md 狀態變更：`entities/boris-cherny`（active → active（待核實）)
- 新增頁面：無
- 摘要：官方面 v2.1.214 純安全性修正、Anthropic Status 四起錯誤率升高事件皆同日修復；商業面 Meta-Anthropic $10B 運算力租賃洽談三方獨立來源、Fable 5 存取政策訊號分歧（收緊 vs 永久）為今日主軸；社群面「效率繞過」機制（7/1 起 60 秒逾時自動代答）經部落格具名分析與具體案例雙重驗證，延續既有討論列；安全政策面 Anthropic 政治獻金布局規模擴大（員工 $3M + CEO 個人 $1M）
- 呈現品質：五類共 8 頁全數 ✅ 通過，未出現需修復或待辦項目
- 品質備註：無

## 2026-07-19 週度延伸回顧

- 延伸（六記者並行判斷 → 使用者確認 4/5 項執行，均帶 model:sonnet；範圍為 news/2026-07-13~07-17，執行時 07-18 雲端 ingest/lint 尚未同步至本機，事後 merge 時確認無實質衝突——本次延伸與 07-18 雲端更新觸及同一批頁面但段落互不重疊）：
  - `entities/claude-code.md`：服務穩定性子區塊新增彙整條目——07-15~07-17 這 72 小時內 Anthropic Status 累計 6 起獨立事件（多模型錯誤率×2、Sonnet 5 單獨一起、企業 SSO 登入失敗、Opus 4.7 錯誤率升高、Sonnet 5/Haiku 4.5 錯誤率升高），前 5 起已解決，07-17 07:10 通報那起截至 07-19 彙整時仍無後續日報可確認解決時間；GV Wire 引用 Downdetector 佐證；標題統計行同步（已修復 3→3、未修復 3→4）
  - `topics/anthropic-government-policy.md`：合併本週四條各自獨立記錄的「Mythos 風險跨界重新浮現」事件（JPMorgan CEO Dimon「real issue」發言、加拿大金融監管警告信、參議員 Mike Rounds 五角大廈簡報、Hegseth vs CISA 立場矛盾）為單一綜合敘事段落，說明出口管制解除後風險論述罕見地同步在金融業/監管/國會/政府內部四條戰線重燃；補與 `entities/mythos.md` 的 Dimon 發言雙向 wikilink；callout 覆寫為單一最新版本
  - `topics/model-comparison.md`：新增「外部評測榜單」連結區塊（Artificial Analysis Intelligence Index、HF Open LLM Leaderboard），只放連結不放會凍結的具體分數，回應 reader-notes GLM/Qwen 與 GPT-5.6 兩條「指路而非囤積」需求
  - `topics/competitor-landscape.md`：GLM-5.2 對照列升級標註為完整 benchmark 數字（FrontierSWE 74.4 vs Opus 4.8 75.1、Terminal-Bench 2.1 81.0、SWE-bench Pro 62.1）＋明確「非日報進料，使用者 07-17 手動查證」標記，保留待查證精神
- 使用者跳過項目：`entities/opus-4-8.md` 補 Kimi K3/Moonshot 交叉引用——使用者判斷此條邊際效益低（資訊已在 competitor-landscape.md，一行 wikilink 對讀者理解 Opus 4.8 本身幫助有限），確認跳過
- reader-notes 消費：07-17 GLM/Qwen 開源競品差距 → ✅ 已納入（三題皆已裁定並落地，見上）；07-12 GPT-5.6 vs Claude → 連續三輪（07-16、07-19）查無官方數字，維持 ⏳ 但改為被動觸發，不再每週主動重查；📌 07-07 雜記未逾 30 天，保留
- 聚焦校準：非本月首次週度回顧（本月已於 07-16 執行），跳過
- 品質備註：本次執行期間雲端 pipeline 同步完成 07-18 每日 ingest 與週度 lint（詳見上方兩則），merge 時發現本次延伸與雲端更新觸及部分同一頁面（claude-code.md/anthropic-government-policy.md/competitor-landscape.md），逐檔核對後確認段落互不重疊、內容無矛盾，正常合併

## 2026-07-19 Ingest | news/2026-07-19.md（49 則）

- 來源日報：[[news/2026-07-19]]（49 則，10/10 來源；Hacker News 12、GitHub Issues 15、Google News 9、dev.to 15、GitHub 1、Blogroll 2、Reddit 12、Anthropic Status 0、Anthropic Blog 0、Claude API Release Notes 0）
- 分類派工：模型 2 則、功能 10 則、商業 8 則、社群 29 則（四類並行 foreground，model: sonnet；安全政策、人物本日無條目，跳過。註：本次執行環境的自訂 subagent_type 註冊表未載入，改以 general-purpose agent 內嵌對應記者角色規則＋開始前必讀清單執行，功能等同四位專職記者）
- 更新頁面：
  - **模型**：`entities/opus-4-7.md`（新增已知問題：Opus 4.7 於較長 payload 會把舊版 XML tool-use 格式混入 JSON tool call，#49747，🔴 未修復，33 留言/34 讚同，達 GitHub Issue 中門檻；callout 覆寫為此事件。Opus 5 傳聞〔dev.to〕與 07-13 已收錄文章逐字相符，判定無新事實，未重複寫入）
  - **功能**：`entities/claude-code.md`（v2.1.215 發布記錄：Claude 不再自動執行 `/verify` 與 `/code-review`，須手動呼叫；已知問題新增 5 起條目——5 小時額度不到 90 分鐘用罄 #6457 120 留言本日最高互動、Desktop 登出後 session 消失 #26452 49 留言、Environment Contributions 警告持續重現 #3301 43 留言、GitHub connector 連結成功卻無法讀取內容（近期退化）#71542 37 留言、對話訊息時間戳記請求 #44763 36 留言，另 Slack 多 workspace 請求 #44243 33 留言與既有 2 起條目數據同步更新；Multi-agent collaboration #28300、VS Code diff review #33932 因與既有記錄數字幾乎相同（各僅差 0–1 則留言）判定為噪音級浮動未更新，避免無意義 churn；Bun/Rust runtime 內部改動記入現況）；`entities/claude-skills.md`（新增 `/verify`/`/code-review` 行為變更列，因牴觸原「Claude 依語意自動觸發、無需手動呼叫」通則描述，同步修正現況首段）
  - **商業**：`entities/pricing.md`（Fable 5 訂閱異動兩則媒體報導方向不一致：Tech Times 稱「Max 方案轉永久、Pro 改 Credits-only」，Dawn 稱「Fable 5 以 50% 用量上限併入 Max/Team Premium」，與既有 07-18 矛盾訊號並列記錄，不擇一呈現）；`topics/competitor-landscape.md`（新增 07-19 時序：Musk 表態序列延續、Musk 開源 Grok Build 與每月 12.5 億美元財務數字〔付款對象未確認〕、南韓市場地位〔KED Global〕、新競爭者 Thinking Machines 品牌定位〔Fast Company〕，四則均標記為標題層級資訊）；`topics/anthropic-business.md`（補上 07-18 已記錄「廣告反彈評論」當時缺失的具體廣告內容細節〔TechCrunch／HN 39 分〕；Meta/Anthropic「震撼彈」報導因原文過於單薄，記錄為待補充而非正式事件）
  - **社群**：`topics/community-tech-patterns.md`（新增「Spare Mac 隔離環境」工作流模式，HN 234 分達高門檻）；`topics/community-tech-discussions.md`（Reddit「額度焦慮系列」🌊延燒列補充兩則延伸節點：Dear Anthropic This Has to STOP、Anthropic I think you really need to react）
  - 今日 29 則社群節錄中 23 則因未達互動門檻（多數 Show HN 僅 1-5 分、多則 Reddit 為純圖片貼文無文字內容）或查表確認為既有條目重複浮現（3 則 dev.to）而不收錄，詳見社群記者回報
- feature-radar：新增 1 條（Claude Code v2.1.215 `/verify`/`/code-review` 手動觸發變更，🔥🔥／⚡ 有條件推薦）；最新版本行同步至 v2.1.215；升版風險表新增「`/verify`/`/code-review` 不再自動觸發」🔴（Breaking change 無過渡期），置換原「Fable 5 Defense in Depth 誤判」列（該項非版本升級可解決之風險，移除重複列示，改於 [[entities/fable-5]] 參照）；⏰ 倒數中：07-19 Fable 5 到期列更新為反映今日兩則方向不一致的媒體報導，指向 [[entities/pricing]]；本週推薦：今日無新條目達 🔥🔥🔥🔥+ 門檻，維持原內容不動
- index.md 狀態變更：無
- 新增頁面：無
- 摘要：官方面 v2.1.215 `/verify`/`/code-review` 改為手動觸發（Breaking change，無過渡期）為今日主軸；社群面 GitHub Issues 高互動未解決需求集中出現（5 小時額度異常等 8 起，含今日互動量最高的 120 留言 issue）；商業面 Fable 5 訂閱政策再現方向不一致的媒體報導、Musk/Anthropic 競爭與金流關係持續延燒
- 呈現品質：四類共 7 頁全數 ✅ 通過，未出現需修復或待辦項目
- 品質備註：無

## 2026-07-22 Ingest | news/2026-07-22.md（71 則）

- 來源日報：[[news/2026-07-22]]（71 則，10/10 來源；Google News 45、GitHub Issues 15、Hacker News 17、dev.to 14、Anthropic Status 6、GitHub 3、Blogroll 2、Anthropic Blog 1、Reddit 6、Claude API Release Notes 0）
- 分類派工：模型 1 則、功能 7 則、商業 15 則、安全政策 6 則、社群 17 則、人物 1 則（六類並行 foreground，model 繼承主 session。註：本次執行環境的自訂 subagent_type 註冊表未載入，改以 general-purpose agent 內嵌對應記者角色規則＋開始前必讀清單執行，功能等同六位專職記者）
- 更新頁面：
  - **模型**：`entities/opus-4-8.md`（新增歷史記錄：TipRanks 報導 Claude 曾自稱是阿里巴巴 Qwen AI 引發蒸餾雙標批評，比對後判定與既有 05-29～05-30 Qwen distillation 爭議為同主題疑似重炒，標 ❓ 待核實，未新建頁、未動 model-comparison.md）；補件任務另更新 `entities/mythos.md`（CNBC 報導聯準會曾就 Mythos 發出警示但延遲數月曝光，待核實，串連既有金融監管敘事）
  - **功能**：`entities/claude-code.md`（**v2.1.217** 發布：Prompt input 表情符號 shortcode 自動完成，feature-radar 新條目；SDK python v0.117.1／typescript sdk-v0.112.5 兩則 bug-fix/chore 版本同步記錄；已知問題新增 3 條——Remote Control 自動重連失效 #34255 57 留言、--screen-reader 無障礙模式 #11002 63 留言、Opus 4.7 思考摘要遺失 #49268 49 留言；9to5Mac/MacRumors 報導 Claude Code Mac app 新增即時 iOS App 測試功能因無官方版本號佐證，僅記為待核實，未列入 feature-radar）
  - **商業**：`topics/anthropic-business.md`（延續 15 億美元著作權和解案敘事，補上 91% 賠付申請率、律師費削減至 6.8%、Bloomsbury 分潤；新增專利侵權訴訟〔Reuters＋Bloomberg Law 兩獨立來源〕與田納西大學訴訟兩起獨立法律事件，皆標記查證狀態）；`topics/competitor-landscape.md`（中國 AI agent 自主研究任務超越 Claude Code〔SCMP，source_count=2〕、Claude 自稱 Qwen AI 蒸餾爭議之商業/競品面記錄，皆標「僅標題可用，待補充」）
  - **安全政策**：`topics/anthropic-government-policy.md`（Anthropic 再捐 2000 萬美元予 Public First Action，政治教育/遊說捐款累計達 4000 萬美元，官方公告 + WSJ/The Hill/Axios 三則跟進併入攻防紀錄；CNBC Fed/Mythos 警示事件記入並轉知模型記者）；`topics/ai-agent-safety.md`（俄語駭客 jailbreak Claude Opus 打造滲透測試工具事件，cyberpress.org + Infosecurity Magazine 兩獨立來源，待查證細節）
  - **社群**：`topics/community-tech-discussions.md`（太空經濟模擬器 Rust/Bevy〔HN 101〕、Orate 本地 TTS〔HN 14〕、Browser Tools SDK〔HN 11，source_count=2〕、Nativ 本地模型〔Simon Willison〕四則新增）；`topics/community-tech-patterns.md`（CodeAlmanac codebase wiki〔HN 54〕、tpu-management Claude Code skill〔dev.to〕兩則新增；MCP servers token 成本一文與既有 07-21 條目重複，未重複寫入）；分數低於門檻的 Chalk／Tokenmaxx／PMG／herdr／ESP32／desktop 替代方案／Hoop／Claude Bucks／claude-logkeeper／Nura Dev 共 10 則邊緣小工具（HN 1–8 分）未收錄
  - **人物**：`entities/cat-wu.md`（記錄 Cat Wu 與 Thariq Shihipar 出席 AI Engineer World's Fair 爐邊對談〔Simon Willison 部落格〕，因摘要遭截斷僅記錄出席事實，不推測對談具體論述內容）
- feature-radar：新增 1 條（Claude Code v2.1.217 表情符號自動完成，🔥／⏳ 觀察中）；最新版本行同步至 v2.1.217；本週推薦與升版風險表因無達門檻變化維持原內容，僅同步版本行；⏰ 倒數中無變化
- index.md 狀態變更：無
- 新增頁面：無
- 摘要：商業/法律面為今日主軸——著作權和解案細節（91% 賠付率、律師費削減）、新增專利訴訟與大學訴訟兩起獨立法律事件、政治獻金累計 4000 萬美元；安全面新增 Fed/Mythos 警示（待核實）與 jailbreak 滲透測試工具事件；功能面 v2.1.217 為小型體驗更新，三則高互動已知問題持續追蹤；社群面 Show HN 工具數量多但多數未達收錄門檻，僅太空模擬器與 CodeAlmanac 兩則達中高門檻
- 呈現品質：六類共 9 頁全數 ✅ 通過，未出現需修復或待辦項目
- 品質備註：安全政策記者正確識別 CNBC Fed/Mythos 條目為 `entities/mythos.md`（模型記者主責）新事件並轉知，主編已補派模型記者完成該頁更新，跨記者轉知流程運作正常

## 2026-07-22 Query：多智能體 orchestration 學術對照持久化

- **觸發：** 使用者在一連串「大型 codebase × Claude Code」對話中問「Workflow／Agent Teams／Subagent 差異」，再追問「這三種對應到學術論文的哪幾種 orchestrator 名詞」；經 WebSearch 查證後產出對照，使用者要求把結果沉澱進 wiki 供日後對照與記者補料參考。
- **根因（揭露的缺口）：** wiki 原本只在 `topics/community-tech-patterns.md` 的「Multi-agent 架構」記錄社群「做法」，缺一層「機制 ↔ 學術術語 ↔ 論文」的參考對照；且無任何記者常規要求在更新多 agent 模式時對照學術名詞／補論文。使用者一度以為有「orchestrator 記者」，實際無此角色——多 agent 模式歸社群記者（patterns 頁），官方 Agent Teams／Workflow 產品面沾功能記者。
- **處置：** (a) 於 `topics/community-tech-patterns.md` 模式概覽後、技術彙整前新增 `## 學術對照：多智能體 orchestration 術語` 參考層（兩軸：控制流 × 通訊原語；Subagent＝orchestrator-workers/centralized、Workflow＝static/DAG、Agent Teams＝decentralized+blackboard；附三篇來源：Anthropic Building Effective Agents、Future Internet 2026 綜述、arXiv:2501.06322）；(b) 於 `.claude/rules/wiki-ingest-community.md` 加「multi-agent orchestration 學術對照維護」常規——新模式須判斷對應格位，需補論文時因社群記者無 web 工具，改在同步自查欄轉知主編 WebSearch 查證，屬非新聞性更新（只動最後更新）。
- **驗證：** `python scripts/run_tests.py` 全綠（含 check_rules.py）。
- **延伸（同日）：** 於學術對照節新增子區塊「誰負責拆分（decomposition）——human／強 planner／凍結的 skill」，含四種拆分來源 × 應用場景表、核心經驗（PEAR 強 planner>強 executor、ADaPT 遞迴拆分、Coarse-to-Fine 粒度自適應、mixed-initiative、SDD）與「何時必須人類凍結」四選一判準；擴充參考來源至 8 筆。觸發自使用者追問「弱模型分工是否需人類先拆 skill／何時模型自判拆分」與「目前有無這方面討論」。

## 2026-07-25 Query：雲端排程整體 review — trigger 與 pipeline 的耦合

- **觸發：** 使用者問「SCHEDULE 現在會指定 PIPELINE 要執行哪一行不好，pipeline 一更新就容易出問題」，並要求整體 review 雲端排程、思考 corner case 與擴充性。
- **根因（揭露的缺口）：** 雲端 trigger 的 prompt 存在 claude.ai API、不在 repo 內，卻寫死了 11 個步驟座標（daily 的 `Step 0/1a/1b/3/4/5/6`、weekly 的 `Step 3/4/6a/6c/6d/6f`）。`scripts/check_rules.py` 掃不到雲端內容，等於專案最強的防再犯機制對最危險的耦合點完全盲區。缺口已實際存在：**舊 daily prompt 的步驟列舉裡沒有 `Step 1c`**（`--confirm-digest`），雲端沒漏做純粹是 agent 讀檔時順著往下做，不是 prompt 要求的。
- **第二個（更嚴重的）發現：** 雲端 routine 從不 commit `src/news_aggregator/emitted_items.json`，Step 1c 的確認結果每天隨容器銷毀。committed 檔案逐日確認率佐證：07-14~07-24 雲端日幾乎全為 0（3/60、5/58、1/58、1/56、3/59、0/45、3/68、0/68、0/54），僅本機手動執行的 07-19、07-22 為 100%。**2026-07-13 漏失 25 則新聞後建立的兩階段確認防線，整個自動化時期沒有生效過**。（2026-07-26 更正：原記「跨日去重全靠 `seen_urls.json` 獨撐」有誤——`seen_urls.json` 只有 `anthropic_blog.py` 一個來源在用，不是全域去重層，emitted-cache 才是跨日去重的唯一防線，此缺口比原判斷更關鍵。）
- **處置（兩波）：**
  - 第一波：新增 `docs/cloud-runbooks/`（`_shared.md` / `daily.md` / `weekly-lint.md`），執行規範進 repo 並改用步驟標題錨點引用；trigger prompt 縮成薄殼（只指路 + runbook 缺失時的失效保護）；trigger 定義鏡像存進 `docs/cloud-runbooks/triggers/`；runbook 納入 `.claude/review-registry.json` 的裸露引用／路徑存在性／同步配對檢查。
  - 第二波：Step 1c 明文要求 commit `emitted_items.json` 並隨統一 push 上站；runbook 前置閘改兩道（新增「日報已存在則中止」的冪等閘）；push 加 `pull --rebase` 重試與 detached HEAD 檢查，並定義唯一可自動解的衝突（`emitted_items.json` 讓給遠端）；新增 `.github/workflows/daily-watchdog.yml`（15:00 UTC）檢查抓料／日報／網站三件當日產出，缺件則 job 失敗，以 GitHub 排程失敗通知當告警管道。
  - 順手修掉 `check_rules.py` 的假綠：`min_count` + `min: 0` 的條件是 `count < min`，恆為真，「wiki-ingest.md 無『精簡複本』殘留字樣」這條一直什麼都沒檢查。新增 `max_count` 斷言型別並改用之。
- **驗證：** `python scripts/run_tests.py` 全綠；三項負向測試皆確認會變紅（改步驟標題 → 同步配對紅、塞入禁字 → `max_count` 紅、watchdog 缺件 → job fail），watchdog 另以 07-24 為基準日乾跑綠燈。
- **待驗證：** 薄殼架構尚未經過真實雲端執行，已登記 `docs/workaround-register.md`（複查日 2026-07-26）。
- **順帶處理：** 本機 master 落後 origin 七天且雙方各有獨有 commit（本機 15 個未推送），已 merge 並解衝突（web_reader 生成物取雲端版、`log.md` 依時序保留雙方、`community-tech-patterns.md` 標頭取較新日期）後推送。

## 2026-07-26 Query：日報漏收近半 → 釐清呈現層與沉澱層的分工

- **觸發：** 使用者問「為什麼今日聚焦變少了」。查證發現不只聚焦：07-25 抓料 73 則、日報只收 38 則（漏 48%），前一日同流程只漏 2/63（3%）；漏掉的含 61 留言與 47 留言的 GitHub Issue。時間點正對上 07-24 把「選材門檻」搬到檔尾的改版。
- **第一版判斷（錯誤）：** 認定日報是「原始資料層」、應收錄全部條目，於是加了 90% 覆蓋率閘擋下並要求補齊，同時把 `--confirm-digest` 改成只確認真的印進日報的 URL。
- **使用者更正：** 日報不必留全部 raw，只留讀者要讀的重點；要考慮全部的是 wiki 沉澱層。
- **根因（依更正後的模型重新定位）：** 日報篩選本身沒錯，錯的是 **wiki ingest 的輸入只有日報**——過濾發生在呈現層，沉澱層就跟著失明，那 35 則從此沒有任何記者看過。原先的覆蓋率閘是修在錯的地方；`--confirm-digest` 的改動更會讓每天被篩掉的條目永遠處於未確認狀態、日復一日重新提供直到 TTL 過期，是 churn 不是保護。
- **處置：** (a) `scripts/check_digest_coverage.py` 改名並改寫為 `scripts/list_digest_omissions.py`——不再擋流程，改為列出「抓到但沒進日報」的差集（依互動分數排序）；(b) `.claude/commands/wiki-ingest.md` Step 1 強制執行該指令，Step 2 分類涵蓋「日報條目 + 未收錄條目」，未收錄者標記註明摘要較簡略，原則寫為「不收可以，沒看過不行」；(c) `main.py` 的 `--confirm-digest` 還原為確認整批（保留「日報不存在則一則都不確認」的安全網）；(d) `news-pipeline-steps.md` Step 3d 由檢查改為分層原則說明，明確授權日報篩選，並限定「選材門檻」只作用於今日聚焦。
- **資料修復：** 07-25 那 35 則已改回未確認，會在次日抓料重新提供並經由新路徑進入 wiki 評估。
- **驗證：** 123 個測試全綠（含 omissions 清單的 6 個新測試）；`list_digest_omissions.py` 對 07-25 實跑列出 35 則、最高互動兩則排在最前。
- **教訓：** 這是「修對現象、修錯層」的個案——覆蓋率不足只是表徵，真正的不變量是「沉澱層必須看得到全量」。定位缺陷時要先問這個不變量該由哪一層保證。

## 2026-07-26 週度延伸回顧

- 範圍：`news/2026-07-19.md` ～ `news/2026-07-25.md`；六記者並行判斷（`model: sonnet`），使用者確認 4/4 全部執行
- 延伸（皆已落地）：
  - **新增頁面** `topics/community-large-codebase-workflow.md`（社群記者）：把 `topics/community-tech-patterns.md` 中散落 05-02～07-22 的節點，依「並行規模的極限與對策／Context 與 Token 管理／Codebase 索引與記憶／除錯與分工架構」四條線縫成主線，附主線概覽表與 delta-first callout；官方機制只以 wikilink 指向 [[entities/claude-code]]、[[entities/managed-agents]]，不重寫官方文件；與 patterns 頁互加 wikilink（摘要段 + 相關實體）
  - `topics/competitor-landscape.md`（商業記者）：Kimi K3 vs Fable 5 的量化成本比（效果相當、成本約 1/3、速度慢約 4 倍，The New Stack 07-20）從敘事段落補進「競品定價對照」表，與既有「換算成本倍數」列並排；敘事段落保留
  - `entities/boris-cherny.md`（人物記者）：`## 公開言論與主張` 前加開結構化摘要表（日期／主題分類／一句話論述／立場延續或轉折），納入 14 則；排除已查明實為 Fiona Fung 發言的「工程師更孤獨」一則，Bloomberg 未具名報導維持待查證、轉折欄誠實標「—」
  - `topics/model-comparison.md`（模型記者）：補記 07-23 Reddit 三方實測（同 100 則前端需求測 GPT-5.6 Sol／Opus 4.8／Grok 4.5，公開 300 筆產出），附時效性 warning——Opus 4.8 已於 07-25 被 Opus 5 取代次旗艦定位
- 使用者跳過項目：無（記者曾建議跳過 model-comparison 那條因時效性下降，使用者裁定仍執行）
- 回報「無」的領域：功能、安全政策。兩者各留一個觀察哨——功能：`/code-review` 若再出現第三次行為變更，可評估在 `entities/claude-code.md` 開「演進小節」單一入口；安全政策：「矽谷業界聯合反對對中限制」若出現具名企業表態或具體訴求，可從表格列升格為獨立段落
- reader-notes 消費：07-22「大型 codebase 效率」→ ✅ 已納入（建頁落地）；07-12「GPT-5.6 vs Claude」→ 模型與商業記者本週再查仍無官方對比數字（Opus 5 發布僅稱「matching or beating Fable 5」，未對比 GPT-5.6 Sol），維持 ⏳ 被動觸發；📌 07-07 雜記未逾 30 天，保留
- 聚焦校準：本月已於 07-16 執行（命中率 36%），依 `metrics.md` 產出物判斷，跳過
- 使用者另提需求：`topics/model-comparison.md`「適合／不適合做什麼」品質不佳，已另派深度評價 review（含體裁範本並排比對），結果待回報後決定改寫範圍

## 2026-07-26 Ingest | news/2026-07-26.md（51 則，本機補跑）

- 背景：GH Actions daily-gather 本日被 GitHub 靜默丟棄（Actions 頁查無 run），雲端 routine 13:05 UTC 新鮮度防線正確中止並留 abort log（fd87c55）。本機 22:30 起走文件化補救路徑（/news-pipeline），Phase A 抓料 51 則、10/10 來源正常，日報收錄 27 則
- **雙輸入路徑首次實戰**：wiki ingest 分類涵蓋「日報 27 則 + 未收錄清單 24 則」（scripts/list_digest_omissions.py），五類並行 foreground 派工（model: sonnet；人物本日無條目跳過）
- 更新頁面：
  - **模型**：`entities/opus-5.md`（MLQ.ai／PCMag 媒體標題與官方「逼近未超越」框架的措辭落差標待驗證）；`entities/mythos.md`（Mashable「Mythos 或類似模型可能公開發布」傳聞，待核實）；`topics/model-comparison.md`（Opus 5 對照欄補媒體措辭差異；**並完成快速選型表排版修復**——使用者回報七欄儲存格塞散文致網頁瘦長條，儲存格收斂為 ≤25 字短語、細節搬入新增的「選型細節」區、狀態欄瘦身，3 跳自檢重跑兩題皆單一命中）
  - **功能**：`entities/claude-code.md`（官方部落格「Claude 5 世代 context engineering 新規則／系統提示詞縮減逾 80%」記入現況〔HN 393 分，判非可操作異動不進 feature-radar〕；HN「硬編碼指示 Opus 5 不用 subagent」記已知問題〔社群觀察待證實〕；新增已知問題 5 條（#69415、#1669、#20469、#50246、#45937）、同步互動數 5 條（AGENTS.md #6235 達 5760 讚為全站最高）；服務穩定性新增 Opus 5 上線首日 4 起事件皆已解決，組頭統計 🧠30→32、MCP 9→10、平台 40→41、穩定性 18→22 逐一同步）
  - **商業**：`topics/anthropic-business.md`（SK 集團自製晶片供應訊號〔Fortune，與 Samsung 代工洽談明確區分，推論標記〕；AMD 列補 07-26 股價分析）；`topics/competitor-landscape.md`（David Sacks 公開批評 Anthropic 反競爭）
  - **安全政策**：`topics/anthropic-government-policy.md`（Nvidia 開放權重連署擴至 50 家、Amazon 與 Anthropic 未加入〔Forbes〕；India Today「矽谷分裂」；補強 07-23 業界反彈支線，攻防紀錄 +2、時序 +2）
  - **社群**：`topics/community-tech-discussions.md`（系統提示詞縮減 80% 社群反應〔HN 393 高門檻〕；硬編碼 subagent 限制〔Reddit→HN 跨平台，低門檻〕）；`topics/community-tech-patterns.md`（dev.to「Use Fable 5 where it pays for itself」第一手成本策略）
  - 社群不收錄：Show HN 三工具（1–3 分遠低門檻）、Reddit spec-driven（無週熱門標記）、Ruff v0.16.0（與主題無關）
- 跨記者轉知閉合：dev.to Fable 5 成本文——模型記者讓渡、社群記者已收 patterns ✅；Android Police「不讓 Claude 碰密碼」——安全政策轉知社群，**主編裁定不收**（單一專欄主觀質疑、無社群延燒，未達「重要媒體深度報導」門檻）
- feature-radar：無新條目；最新版本行維持 v2.1.220 未變，本週推薦／升版風險／⏰倒數皆不動
- index.md 狀態變更：無；新增頁面：無
- 摘要：Opus 5 全平台上線次日——媒體評測措辭（Tops Benchmark Index）與官方自述（逼近未超越）出現落差、上線首日 4 起錯誤率事件皆速修；官方揭露系統提示詞縮減逾 80% 成社群最大討論（HN 393）；AGENTS.md 支援請求達 5760 讚；晶片線三向延燒（AMD 股價、SK 自製晶片訊號、Nvidia 開放權重連署 50 家）
- 呈現品質：五類共 9 頁全數 ✅ 通過
- 品質備註：無

## 2026-07-26 Lint

- 修正矛盾：2 處——(1) `topics/model-comparison.md` 五處寫 Opus 5 定價「$5/$25（官方文件確認）」並宣稱兩則報導「實為同一數字」，與 `entities/pricing.md`「讀者端推算、非官方逐字確認」矛盾；以較嚴謹的 pricing.md 為準改寫 5 處（callout／選型表定價欄／定價備注／情境推薦／benchmark 備注），移除過度確信結論。(2) `entities/opus-5.md` 發布日 07-25 vs `pricing.md` 07-24 一天落差，查 `news/2026-07-25.md` 原文確認官方 RSS 時間戳為 07-24 17:00 UTC、07-25 為日報收錄日，已在 opus-5.md 補「日期說明」澄清為收錄時序差異而非事實矛盾。其餘五類記者交叉核對（中國對峙三頁敘事、john-jumper 加入日期、claude-code 互動數 vs official-community-gap 引述、Google 投資金額 vs Alphabet 持股市值）皆一致。
- 補連結：無（六類共 47 頁逐一 grep 反向 wikilink，全數至少被 1 個非 index.md 頁面連入；人物 12 頁、功能 13 頁、社群 7 頁、商業 7 頁、安全政策 6 頁、模型 7 頁）
- 狀態更新：`topics/safety-china-trust-dispute` ongoing→monitoring（核心「後門」敘事自 07-10 Anthropic 首度否認後 16 天無新進展；07-22 起 Moonshot 蒸餾／digitimes 外洩指控屬性質不同的獨立事件，已在頁內註明改追蹤於 anthropic-government-policy）、`topics/anthropic-commitments` ongoing→monitoring（5 項追蹤中承諾自 07-10 起無新官方動作）
- resolved 收尾：無（各類別範圍內無 resolved 狀態 topics 頁；`entities/google-investment` 為 resolved entities 頁，抽查確認摘要已載明結案事實）
- 新增 entities：無（見下方待使用者確認第 1 項）
- 呈現品質：⚠️ 已修復 9 頁——`entities/fable-5.md`（熱度表格違反「緊接摘要」規則，自「配額與計費過渡」後移至現況之後）、`entities/opus-5.md`（補日期落差澄清）、`entities/sonnet-5.md`（07-09 待查證逾 14 天改註無後續）、`topics/model-comparison.md`（定價過度確信措辭）、`entities/opencode.md`（摘要非 delta-first，補「最新動態（2026-05-22）」開頭句）、`entities/claude-code.md`（#69238 待查證標記補標準格式）、`topics/enterprise-tool-tracker.md`（Meta 未確認列改註無後續）、`topics/competitor-landscape.md`（時序連續 18 個無分組日期條目，補「近期單日動態彙整」錨點）、`topics/community-tech-discussions.md`（2 筆 07-05 標記改註無後續）；人物 4 頁（cat-wu／dario-amodei／teresa-carlson／andrej-karpathy）同步日期欄位。其餘全數通過。
- 入口層健檢：5 頁 > 500 行全數具備入口層、無需補結構、無語意分岔或死案候選——`community-tech-discussions.md`（1201 行）、`community-tech-patterns.md`（1165 行）、`ai-agent-safety.md`（611 行）、`anthropic-business.md`（519 行）、`claude-code.md`（515 行）。>200 行但 <500 行者（fable-5 301、mythos 247、community-tech-timeline 318、community-tech-tools 273、community-pattern-trends 205、boris-cherny 203）皆已有 callout ＋ 分組，依「一頁一故事」不拆分。
- 待查證回訪：
  - 已改註「至今無後續」：`entities/sonnet-5.md`（07-09「57 分／API 減半」評測）、`entities/claude-code.md` #69238（07-06 Advisor 無回應）、`topics/enterprise-tool-tracker.md` Meta 限用列（07-06）、`topics/community-tech-discussions.md` 2 筆（07-05 Microsoft Fast Context 下架原因、Anthropic 疑似 prompt injection 單方指控）、`entities/teresa-carlson`（07-07 加入報導）、`entities/dario-amodei`（07-06 STAT 專訪）、`entities/boris-cherny`／`entities/cat-wu`（07-08「5 種員工原型」發言人歸屬）、`entities/andrej-karpathy`（05-29 加入傳聞，查核日期由 07-11 更新至 07-26）
  - 已更新（跨頁補鏈）：`topics/ai-agent-safety.md` 阿里巴巴 2.5 萬假帳號蒸餾指控（06-26，補 07-13 NY Post 重申的跨頁狀態，未見新證據）
  - 維持不動（14 天查證期內）：安全政策 7 則（Tego AI、俄語駭客越獄、Bash/Unicode 繞過、Nozomi/Horizon3.ai、TBIJ、Moonshot 蒸餾、Nvidia 連署）、商業 4 則（專利訴訟、田納西大學提告、pricing 多筆、蒸餾指控擴大）、功能 3 則（claude-design 07-16、claude-security 07-23/24）、人物 3 則（dario super PAC 07-16、tom-blomfield 07-13、boris-cherny 07-17/20）、模型 8 則
- 規則檔健檢：
  - 矛盾：無（`wiki/CLAUDE.md`、`.claude/rules/wiki-ingest.md`、`.claude/rules/wiki-ingest-format.md` 三檔逐段掃描未見同一行為的相反指示）
  - 引用驗證：全部通過（7 個錨點逐一 grep 命中——`| 首次出現 |`、`## 痛點洞察`、`近期工具` 於 community-tech-tools.md；`## 技術彙整`、`熱門討論`、`衍生` 於 community-tech-discussions.md；`全覽表` 於 feature-radar.md）
  - 遵守率：全部通過（近 3 次 ingest = 07-24／07-25／07-26：呈現品質審查 3/3 皆有標記、feature-radar 明確點名 3/3、log 格式 3/3）。惟發現 `wiki-lint.md` 6c 表中「新工具加入時更新痛點洞察近期工具欄」一列已不適用於 ingest——`community-tech-tools.md` 自 2026-06-19 改為 lint 專用，每日 ingest 不再更新該頁，此列應改為 lint 自查項或移除（見待確認第 5 項）
  - 過期規則（> 60 天）：5 項——`topics/ 頁面格式模板`〔04-25，92 天，連續第 4 週〕、`entities/ 頁面格式模板`〔04-25，92 天，連續第 4 週〕、`Wiki 頁面呈現品質標準`〔05-15，72 天，連續第 2 週〕、`patterns ↔ discussions 雙向連結規則`〔05-16，71 天，連續第 2 週〕、`enterprise-tool-tracker 更新規則`〔05-26，61 天，本週首度越線〕。全部 27 個帶標記區塊中 22 個在閾值內（最舊 45 天）。
  - 來源健康：⚠️ `Claude API Release Notes` 連續 7 天（16 天觀測窗內全期）count=0，已達第 4 週（07-11 lint 首報、07-18 lint 再報）；其餘 9 來源 7 天總量 Google News 220、Hacker News 103、dev.to 96、GitHub Issues 90、Reddit 84、Anthropic Status 27、GitHub 15、Blogroll 12、Anthropic Blog 5，無連續 3 天歸零。單日歸零（GitHub Issues 07-20、GitHub 07-20/07-26、Anthropic Blog 07-24/07-26）未達告警門檻。
  - 來源記分卡：無「未註冊 slug」告警；Google News 低信譽桶（pc1 < 0.4）0 筆（高信譽 172、中間 10、未知 10），無需人工覆核；HHI 0.239（接近 0.25 高度集中門檻，Google News 占 Presence 41%）。觀察名單：`dev.to`（樣本充足 16 天，Wilson 下界 24%、Presence 4% 雙低）——惟記分卡自身標註其跨日重覆視窗抓法使收錄率結構性偏低、不可與 26h 窗來源比較，故僅列觀察不建議汰換。
  - 跨檔案語意矛盾（6f）：`python scripts/check_rules.py` 全部確定性檢查通過（23 組 sync_pair 含雲端 weekly runbook 對 wiki-lint.md 錨點逐字相符、model-comparison 六條規則齊全等）；13 組 coupling hints 為 warn-only 未阻塞。惟人工語意比對發現 1 處實質矛盾：`.claude/commands/wiki-lint.md` 6g 指標一要求 grep `（ref:`，但 `.claude/commands/news-pipeline-steps.md:152` 自 07-25 起明訂聚焦引用改用 `[N]` 註腳 + 檔尾「今日聚焦參考連結」清單，兩者未同步，舊 grep 對 07-25/07-26 讀成 0（見品質指標段）。此配對未登記於 review-registry.json。
  - 成長迴路（月度）：非本月首次 lint（本月已有 07-04／07-10／07-11／07-18 Lint 紀錄），跳過月度蒸餾
- 品質指標（6g）：
  - ref 覆蓋率（每週）：97%（07-20~07-26，33 條列／32 有歸因，閾值 80% 通過）；缺 ref 日期：07-22 有 1 條列無歸因。注意：舊 grep 模式會誤報 71%，原因為日報格式改版（詳見上方 6f）
  - 採用驗證率（月度）：非本月首次 lint，跳過
  - 外部死鏈（月度）：非本月首次 lint，跳過
  - 趨勢判讀：持平（連續 5 期 97% 以上）；但量測工具本身曾靜默失效，屬需修規則而非資料劣化
- 讀者模擬：
  - Claude Code 重度使用者「Opus 5 出了，我該不該切過去？」→ ⚠️ 已修復：index → model-comparison → 快速選型表 3 跳內命中單一建議（適合數小時自主編碼／跨數十檔 refactor），但該列未提及同日社群發現的 Opus 5 硬編碼工具限制（AgentTool／workflows／deep-research），對重度 subagent 使用者是決策關鍵。已在 Opus 5 列「不適合」欄補「重度 subagent／workflow 工作流先實測」與 wikilink 至 claude-code。
  - AI 系統開發者「官方說移除 80% 系統提示詞，我自己寫 agent 能複用什麼？」→ ⚠️ 已修復：原內容僅存於 `entities/claude-code.md` 現況的長段 callout 內，`community-tech-patterns.md`（開發者的自然入口）零提及。已在 patterns 頁摘要區補「官方指引對照（2026-07-26）」段落，說明此為本頁長期「最小必要 context」社群直覺首度獲廠商側一手依據，並 wikilink 至 claude-code 與 discussions。
  - Anthropic 生態追蹤者「15 億美元著作權和解案現在進展到哪？」→ 通過：index → anthropic-business → 財務狀況表 3 跳內得到 91% 賠付申請率、律師費削至 6.8%、Bloomsbury 分潤、48.2 萬本受涵蓋書籍等具體數字，並區分了同期兩起獨立新訴訟。
- lint 自我遵守率：6/6 位記者回報一次過（3a–3g 七項在六份回報中各有具體頁名與結論，無缺項或含糊，無退回）
- 社群 lint 專屬策展：`community-tech-tools.md` 新增 0 筆（07-16~07-26 Show HN 互動普遍未達中門檻，唯一高分 Bento HN 877 與 Claude 無關聯不收錄）／汰除 12 筆逾 30 天觀察中條目（Prompt Foundry、Sqim、Everything Claude Code microVM、Pi Extension、BeamWeaver、job-search、LegalRabbit DOCX、AI Commander、Gorchestra、Pagecast、Parcle、token-warden）／精選層提拔 0／痛點洞察清理「Token 成本不透明」「多 agent 協調混亂」兩列失效引用；`community-pattern-trends.md` 本輪無新趨勢節點，依規則未動頁；discussions 保留規則清理 0 筆（閃現最舊 07-06 僅 20 天，無落幕條目）
- overview.md：已全文改寫（上次全文改寫為 07-18 lint。本輪反映 07-18~07-26 局勢：Opus 5 陣容重排與定價未收斂、官方 context engineering 80% 縮減 vs Opus 5 硬編碼限制的核心張力、Fable 5 促銷 07-19 到期後倒數焦點轉 Sonnet 5 8/31、15 億美元和解案由「會不會賠」轉「怎麼分」、中國對峙本體轉 monitoring 而戰場移至出口管制對立、Alphabet 持股 1,240 億美元；模型現況表以 Opus 5 為首列重排、近兩週事件表更新至 07-18~07-26、社群工具生態誠實記錄本輪新增 0 筆、情緒指標工具活躍度改標回落）

### 📋 待使用者確認（lint 自主安全部分已完成，以下需人工決定）

1. **新實體頁候選**：(a) `Reflect with Claude`——連續第 4 週提出，但本輪查證顯示自 07-09 發布後 17 天無新報導、僅存在於 `claude-code.md` 歷史記錄 1 處與 `feature-radar.md` 3 處，熱度未成長（HN 僅 29 分）→ 建議結案不建頁，請確認是否同意撤下此候選以停止每週重複提出。(b) `Project Glasswing`——出現於 4 個頁面且內容已具規模（約 50 個夥伴、10,000+ 高危漏洞、ENISA/ICE/Nozomi Networks/Horizon3.ai 夥伴名單持續擴充），目前寄居於 `entities/mythos.md` 的 `## Project Glasswing` 區塊 → 是否獨立建頁？（考量：夥伴名單是持續更新的獨立敘事，但拆出會使 mythos 頁的安全能力故事斷裂）
2. **6g 指標一 grep 模式過時（建議優先處理）**：`.claude/commands/wiki-lint.md` 的 grep `（ref:` 與 `news-pipeline-steps.md:152` 現行 `[N]` 註腳格式不同步，導致回歸偵測器本身靜默失效（本輪若照舊 grep 會誤報 71%，實際 97%）→ 是否授權改寫為雙格式（同時計 `（ref:` 與 `[N]`），並將此配對登記進 `.claude/review-registry.json` 的 sync_pairs 以防再犯？
3. **來源健康（第 4 週）**：`Claude API Release Notes` 連續 4 週 count=0 → 是否授權查修抓取邏輯（URL 失效或格式改版）？此項已連續三次 lint 提出未決。
4. **規則年齡審查（6d）**：5 項超過 60 天——`topics/ 頁面格式模板`／`entities/ 頁面格式模板`（各 92 天，第 4 週）、`Wiki 頁面呈現品質標準`（72 天，第 2 週）、`patterns 對 discussions 雙向連結規則`（71 天，第 2 週）、`enterprise-tool-tracker 更新規則`（61 天，首度越線）→ 是否逐項審視，或標記為「已審閱，長期有效」以停止重複列出？（前三項已重複多週未決，建議一次裁決）
5. **6c 遵守率表過時列**：`wiki-lint.md` 6c 的「新工具加入時更新痛點洞察近期工具欄」一列，因 `community-tech-tools.md` 自 06-19 改為 lint 專用、每日 ingest 不再更新該頁而已不適用 → 是否改寫為 lint 自查項或移除該列？
6. **patterns 淘汰審查 dry run 結果**：建議淘汰 0 條、建議合併 0 組（`Loop Exit Condition` vs `Agent Loop 事件驅動` 焦點不同，暫不建議合併）、保留全部；1 項無法判斷——「Multi-agent 架構」類別與官方 Managed Agents 高度重疊（official-community-gap 已標「高度對應」），是否需拆分「官方已覆蓋的協調基礎設施」與「社群仍獨有的自架/打包/UX 價值」兩部分？

## 2026-07-27 Query：修 6g 量測失效 + 登記防再犯配對（07-26 lint 待確認第 2 項結案）

- **點出什麼**：使用者裁決執行 07-26 lint 回報的待確認第 2 項——6g 指標一的 ref 覆蓋率 grep 與現行日報格式不同步。
- **根因**：日報歸因格式於 2026-07-25 由行內 `（ref: url）` 改為 `[N]` 註腳 ＋ 檔尾「今日聚焦參考連結」清單（`.claude/commands/news-pipeline-steps.md`「Step 1b：生成日報」），但 `.claude/commands/wiki-lint.md` 6g 的量測 grep 未同步。**回歸偵測器自己失效**：07-25/07-26 兩天被讀成 0 ref，照舊 grep 會誤報覆蓋率 71%（實際 97%）。此類失效無聲——指標數字照樣產出，只是變成假的。
- **另發現第二個灌水源**：檔尾「選材門檻」附錄使用與今日聚焦相同的 `- **[...]**` 條列形狀，未限縮區塊就數會灌大分母（2026-07-26 實例：未限縮 7 條，實際 5 條）。原規則寫「分子分母皆取今日聚焦區塊內」但給的指令並未限縮，屬規則文字與指令不一致。
- **處置**：
  1. `.claude/commands/wiki-lint.md` 6g 指標一改寫（標記更新為 `[加入: 2026-07-05，改版: 2026-07-27]`）：改為 awk 限縮「今日聚焦」區塊後再數，分子同時計 `（ref:` 與 `[N]` 兩種格式；寫入兩則 ⚠️ 警語（含 07-26 誤報實例與灌水實例）與分母為 0 的處理方式。新指令已對 07-20~07-26 逐日實測，結果與人工核算完全吻合（07-22 為 5/4、07-25 為 3/3、07-26 為 5/5）。
  2. `.claude/review-registry.json` 新增 2 組 sync_pair（總數 23→25）防再犯：一組要求 `news-pipeline-steps.md` 與 `wiki-lint.md` 都必須認得現行 `[N]` 格式與「今日聚焦參考連結」；一組要求 6g 段落必須保留「兩種歸因格式，必須同時計」與「必須先限縮到「今日聚焦」區塊再數」兩條語意錨點。
  3. **反向測試**：刻意破壞 6g 措辭後 `check_rules.py` 確實回報 ❌ exit 1，還原後回 ✅——確認新配對不是永遠會過的空檢查。
- **驗證**：`python scripts/check_rules.py` 零 ❌（25 組配對全過）、`python scripts/run_tests.py` exit 0、`/review-commands` 完成報告零錯誤。
- **未一併處理（留待使用者裁決）**：雲端 weekly lint 的 08-01 首跑驗證仍有缺口——`docs/cloud-runbooks/_shared.md` 只規定「中止時」必須 commit abort log，未規定成功／no-op 也要留紀錄，而收尾又允許「無變更則跳過 commit」。因此一次順利但無事可改的 lint 產出為零 artifact，與靜默死亡在 GitHub 上無法分辨。建議補「無論成功／no-op／中止都 append 一行結果到 `src/logs/task_scheduler.log` 並 push」。

## 2026-07-27 Query：雲端 lint 自主 review — 08-01 首跑前攔下兩個結構性問題

- **點出什麼**：使用者要求對雲端排程自主 review 潛在問題直到解決。以 RemoteTrigger list 核對雲端實況（兩 trigger enabled、薄殼 prompt 與鏡像一致、writeback probe 已停用、weekly next_run = 08-01 01:02 UTC）後，發現兩個 08-01 會實際發生的問題。
- **問題 1（必然事故）**：08-01 恰為 8 月首次 lint → 月度項觸發，「外部死鏈」`check_links.py` 對 wiki 全部外部連結發 HEAD 請求——但雲端 egress 封鎖一切外網，**全部連結會被誤判為死鏈（403/timeout），且後續「記者標註（原文已失效）」動作會用假結果污染大量頁面**。runbook 健檢分項原將「品質指標」歸為「純機械→自主執行」，無 egress 防護。
- **問題 2（觀測盲區）**：07-27 稍早加的心跳只在收尾寫——07-25 無聲失敗最可能死在中途（session 被殺不留任何東西），這種死法收尾心跳照樣是零 artifact，與「根本沒跑」無法分辨。
- **處置**：
  1. `docs/cloud-runbooks/weekly-lint.md` 健檢分項新增「外部死鏈檢查（月度）在雲端一律跳過」：不執行、不標註任何頁面，改寫待辦留本機月度執行；月度蒸餾歸「要求確認」寫待辦、採用驗證率（本地統計）雲端可自主跑——月度三項的雲端處理首次明確化。
  2. `docs/cloud-runbooks/_shared.md` 無人值守原則新增「STARTED 開跑標記」：環境補丁後、任何步驟前，append `[cloud <routine> STARTED <UTC>]` 到 `src/logs/task_scheduler.log` 並立即 commit push。判定從三態變四態：`STARTED+OK`＝成功／`STARTED+FAILED`＝可追查／**`STARTED 無後續`＝中途死（07-25 的死法，首次可診斷）**／`完全無 STARTED`＝trigger 未觸發或環境起不來。與單一 push 原則不衝突（開跑與收尾 push 相隔整個 routine 時長，無並發競爭）。daily routine 同樣受惠（規則在 _shared 層）。
  3. `docs/workaround-register.md` 08-01 複查標準更新為四態判定，並加「確認沒有大量假死鏈標註出現」為防護生效證據。
  4. `.claude/review-registry.json` +2 sync_pair（→28 組），兩組均通過反向測試（破壞措辭→❌ exit 1→還原→✅）。
- **驗證**：`check_rules.py` 零 ❌、`run_tests.py` exit 0。
- **記錄但不動**：(a) 兩 trigger 掛著 Spotify/Notion MCP connections，headless 執行不需要但無失敗證據，暫不動 trigger；(b) 六記者並行派工仍是 07-25 死因首要假說，但依「本機雲端行為一致」規約不改派工方式，改靠 STARTED 標記讓下次卡死可診斷。

## 2026-07-28 Ingest

- 來源日報：[[news/2026-07-28]]
- 更新頁面：`entities/claude-code`、`entities/boris-cherny`、`entities/dario-amodei`、`entities/opus-5`、`topics/anthropic-business`、`topics/anthropic-government-policy`、`topics/ai-agent-safety`、`topics/competitor-landscape`、`topics/enterprise-tool-tracker`、`topics/community-tech-patterns`、`topics/community-tech-discussions`、`topics/model-comparison`
- 新增頁面：無
- 摘要：Dario Amodei 公開澄清 Anthropic 從未主張禁止開源權重模型、呼籲加強中國晶片管制（HN 972 分＋6 家媒體跟進）與 Claude 分享對話外流至 Google 搜尋結果的隱私事件（8+ 家媒體），為今日兩大主軸；另有 Cognizant 企業合作擴大、Moonshot Kimi-K3 開源、多則 Claude Code 已知問題與 Boris Cherny 公開言論。
- 呈現品質：功能／人物記者各修復 1 處「現況不被時序侵蝕」違規（`claude-code.md`、`dario-amodei.md`），其餘全數通過
- 品質備註：
  - 因六記者並行執行、完成順序非同步，三則跨記者轉知在目標記者已交卷後才送達（安全政策提醒功能記者評估 gbhackers/EIN News 漏洞是否列入已知問題；商業提醒安全政策記者交叉確認 Nvidia/Microsoft 聯盟未見 Anthropic 一事；社群提醒模型記者評估 Simon Willison「AI 該用哪個」導覽文是否收錄 model-comparison）——三者皆屬低急迫性、資訊量有限的候選項目，主編判斷不值得為此另開一輪派工，留待下次 ingest 若有更多細節時自然浮現，非遺漏
  - 雲端 `wiki-reporter-*` 六個自訂 subagent_type 本次仍無法解析（Agent 工具可用清單未列出），全數以 general-purpose 內嵌規則降級執行，功能等同，詳見完成摘要

## 2026-07-28 Query：讀者視角網站 review — 15 項閱讀友善修正一次落地

- **點出什麼**：使用者派冷讀者 agent 以三種目標讀者動線 review 網站後要求全修。三條動線皆 3 跳可達，但高影響問題 4 項：列表摘要 wikilink 剝除斷句、ingest/lint 維運術語裸露給讀者、行動版詳頁寬表格/code fence 撐爆 viewport、「該不該升版」入口不可發現。
- **根因**：(a) `build_web.py` 產 snippet 時把 `[[wikilink]]` 刪成空字串而非轉顯示文字；(b) wiki 頁 callout／標頭把編輯部維運語言（「每次 ingest 更新」「此頁為 lint 專用」「未收錄清單」）直接寫進讀者可見正文——違反 wiki-ingest-format.md 自己的「無 LLM 專屬指令」條款但該條款未涵蓋維運術語；(c) 日報 LLM 產出把 `[BUG]` 標題的開頭方括號併入連結語法吞掉。
- **處置（網站端）**：`build_web.py` 新增 `readable_inline()`（wikilink/md link → 顯示文字，用於 latestHeadline/summary/preview 全部 snippet 路徑）＋ `[BUG]` 缺左括號自動修復＋典藏代表標題改取「今日聚焦」第一條；`app.js` wiki 列表改中文頁名為主/slug 為輔、詳頁 wikilink 按鈕顯示中文頁名、今日頁新增「該不該升版→熱度雷達」常駐導流、fresh 徽章隔日降級為相對天數、搜尋索引未載入時補載重跑、透明度區移除內部文件外鏈、沉澱 chip tooltip 改白話；`design.css` 窄幅表格/code fence 改容器內橫捲、375px chips 改換行（週更 chip 初始可見）、週更篩選置頂說明行；`index.html` 雷達卡副標補「升版風險判讀」、about 來源數 6→10 管道、wiki footer 改讀者語言。
- **處置（內容端）**：feature-radar 三處「每次 ingest 更新」與兩處「下次 ingest 應…」改讀者語言；community-tech-patterns callout 改 delta-first（未收錄決策移出正文）；community-tech-tools／community-pattern-trends／overview 的更新頻率欄改讀者導向節奏說明；anthropic-business 巨型 callout 拆條列。
- **防再犯**：`wiki-ingest-format.md` 新增「無維運術語洩漏」必修項＋「callout 寫發生了什麼、不寫收錄決策」規則＋更新頻率欄位範例改讀者語言（此欄會原樣上站）；`analyzer.py` prompt 新增方括號標題保留規則。
- **驗證**：`run_tests.py` 144 綠（含 check_rules 28 組配對）；本機 preview 實測：snippet 無斷句、[BUG] 帶括號、375px 頁寬 385、wikilink 顯示中文名、週更篩選+說明行正常。

## 2026-07-29 Ingest

- 來源日報：[[news/2026-07-29]]
- 更新頁面：`entities/claude-code`、`entities/mythos`、`entities/opus-5`、`entities/pricing`、`topics/anthropic-business`、`topics/enterprise-tool-tracker`、`topics/competitor-landscape`、`topics/model-comparison`、`topics/ai-agent-safety`、`topics/anthropic-government-policy`、`topics/community-tech-patterns`、`topics/community-tech-discussions`
- 新增頁面：無
- 摘要：Anthropic 揭露 Claude Mythos Preview 密碼學研究重大進展（削弱後量子簽章 HAWK、找到 round-reduced AES 新攻擊法），NYT／ProPublica／CyberScoop 等多家媒體跟進；OpenAI 與 Anthropic 員工聯名致信美國政府籲討論控管 AI 發展步調（Bloomberg／NBC／WaPo）；傳 Meta 早期洽談以 100 億美元租用 Anthropic AI 運算力；部分使用者 Claude 對話紀錄意外現身 Google 搜尋結果的隱私議題（PCMag／Guardian）；Oxide 加入 Anthropic Project Glasswing，將 Claude Mythos 5 用於自家程式碼庫漏洞掃描；Claude Code 侧新增多起已知問題（Cowork Windows VM 啟動失敗、Linux 剪貼簿貼圖失效、claude.exe 疑似觸發 BSOD）與兩則高互動使用者訴求（多組 Connector 帳號支援、印度盧比計價）持續延燒。
- 呈現品質：五記者回報皆為「✅ 通過」，無需修復；社群記者另記錄 1 筆待辦（`community-tech-discussions.md`／`community-tech-patterns.md`「## 摘要」首句仍為頁面說明式文字而非 delta-first，屬既有頁面結構、非本次改動所致，建議留待後續整體改版評估）
- 品質備註：
  - 雲端 `wiki-reporter-*` 五個自訂 subagent_type（模型/功能/商業/安全政策/社群；今日無人物類條目）本次仍無法解析，全數以 general-purpose 內嵌規則降級執行，功能等同，詳見完成摘要
  - 安全政策記者處理 Simon Willison「Frontier Lab Agent Intrusion」條目時，其注入防護機制將本次派工訊息中主編自行附加的謹慎處理指示誤判為「⚠️ 疑似注入」；查證後確認是主編派工文字書寫時未與原始新聞摘要清楚分隔所致，非外部真實注入。記者仍正確地未執行任何指令內容、僅依獨立判斷採用保守寫法，防護機制實際運作如預期；後續派工應更明確以引號或區塊分隔「原始新聞摘要」與「主編指示」，避免同類誤判重演
  - 三則跨記者轉知留待下次 ingest 自然浮現（低急迫性，未另開派工）：功能記者提醒商業記者確認印度定價功能請求 (#17432) 之官方定案狀態、及 The Information 的 Claude Code vs Codex 報導是否需獨立記錄；安全政策記者提醒功能記者留意 Decrypt「沙盒逃脫」報導後續是否需與 Claude Code 已知問題交叉引用
  - Step 2 派工期間因 stop hook 政策要求工作樹不可帶未提交變更結束回合，隨五位記者陸續完成即時分批提交（8 筆 wiki commit），未依標準 Step 3 於全部記者完成後一次性提交；內容完整性不受影響，僅提交顆粒度較細，非設計變更

## 2026-07-30 Ingest

- 來源日報：[[news/2026-07-30]]
- 更新頁面：`entities/claude-code`、`entities/mythos`、`entities/opus-5`、`topics/anthropic-government-policy`、`topics/community-tech-patterns`
- 新增頁面：無
- 摘要：Anthropic Mythos 密碼分析研究延燒為社群後續反應（HN 168 分分析文＋Simon Willison 引述 Matthew Green），Claude Code Desktop 多筆高聲量體驗痛點同日集中出現（主控台捲動 bug 全站互動最高、多帳號切換、多視窗、Claude Projects 串接），Anthropic Status 記錄一起 45 分鐘內解決的模型錯誤率事件；另有 techdirt 對 Anthropic 開放權重出口管制立場的批評分析，以及一款跨來源佐證的平行 agent 本地合併佇列工具。
- 呈現品質：模型記者修復 1 處 `entities/mythos.md` 現況段落超過「不被時序侵蝕」上限（3 段收攏為 2 段）；其餘頁面（`claude-code.md`、`opus-5.md`、`anthropic-government-policy.md`、`community-tech-patterns.md`）呈現品質全數通過
- 品質備註：
  - 雲端 `wiki-reporter-*` 自訂 subagent_type 本次仍無法解析（今日僅功能/模型/安全政策/社群四類有條目；商業/人物無條目未派工），全數以 general-purpose 內嵌規則降級執行，功能等同，詳見完成摘要
  - 安全政策記者對 Simon Willison「AI Worming through Word」（Word 文件觸發的 prompt injection 變種）做出保守判斷：原文摘要未點名 Claude/Anthropic，是通用手法示範而非 Claude 專屬漏洞，為避免在 `ai-agent-safety.md` 製造誤導性關聯，選擇不記錄。此為記者依規則做出的判斷取捨，非遺漏，若後續有更明確與 Claude 使用情境的關聯性佐證可再收錄
  - 社群記者轉知功能記者評估 `official-community-gap.md` 產品化矩陣是否為新增的「本地合併佇列」模式新增對應列；主編查核該矩陣觸發條件為「官方發布新功能時」檢查，今日無官方功能發布，且矩陣現無合併佇列相關列可更新，依規則「無對應列則略過，不強制新增」，本次無需動作
  - 兩則今日主要跨來源事件（密碼分析研究、開放權重政策分析）皆判定不重複收錄進 `community-tech-discussions.md`：社群記者確認僅有單一 HN 貼文分數、無跨平台社群交鋒佐證，收錄僅會複製模型/安全政策記者已主責的主題而非新增社群訊號
  - Step 2 派工期間因 stop hook 政策要求工作樹不可帶未提交變更結束回合，四位記者完成後即時分批提交（1 筆彙整 commit，涵蓋全部 5 個頁面變更），與昨日做法一致，非設計變更

## 2026-07-31 Ingest

- 來源日報：[[news/2026-07-31]]
- 更新頁面：`entities/sonnet-5`、`entities/fable-5`、`entities/claude-code`、`topics/competitor-landscape`、`topics/ai-agent-safety`、`topics/anthropic-government-policy`、`topics/community-tech-patterns`、`topics/community-tech-discussions`、`entities/cat-wu`
- 新增頁面：無
- 摘要：Anthropic 揭露內部覆查發現三起 Claude 模型於資安評估環境中連上網路、存取外部第三方系統的事件（官方措辭與二十餘家媒體「駭入」框架有明顯落差，已於 `ai-agent-safety.md` 分別記錄並註記歧異），EU 隨即呼籲加強監控高風險 AI 系統；同日一名美國法官對政府禁用 Anthropic AI 的正當性提出質疑（具體法律依據待查證）；Claude Sonnet 5 發生 46 分鐘效能降級事件已解決；Claude Code GitHub Issues 累積多筆高互動功能請求/臭蟲（貼上文字編輯、Remote Control 重連失效、Linear 整合觸發雲端 agent）；社群面新增 multi-agent 可靠性工作模式（subagent 靜默失敗模式、agent 失敗自動復原、API 錯誤自動重試接續）。
- 呈現品質：`entities/sonnet-5`／`entities/fable-5`／`entities/claude-code`／`topics/competitor-landscape`／`topics/ai-agent-safety`／`topics/community-tech-patterns`：✅ 通過；`topics/anthropic-government-policy`：⚠️ 已修復（新增表格列時誤插入重複分隔線，已移除修正）；`topics/community-tech-discussions`：⚠️ 已修復（同步移除已逾 21 天保留期限的舊 ☄️閃現 條目「Geosql」）；`entities/cat-wu`：待核實資訊已依規範標註，未斷定
- 品質備註：
  - 雲端 `wiki-reporter-*` 六個自訂 subagent_type 本次仍無法解析（Agent 工具可用清單未列出），全數以 general-purpose 內嵌規則降級執行，功能等同，詳見完成摘要
  - 安全政策記者對媒體標題引號中的「gained unauthorized access」等字眼，因無法讀取 Anthropic 官方部落格全文，統一標註「（待核實：完整引文需查官方部落格全文）」，未逕自採信為官方逐字用詞，判斷保守得宜
  - 功能記者將三則既有已知問題（#3412、#24798、#34255）狀態由 🔴 未修復 改標為 ❓ 待查證（理由：任務指示的狀態判定原則），此為互動數更新順帶的狀態重新歸類，非新增問題被官方回應；下次 ingest 若這批問題仍無官方回應，建議記者評估是否應改回 🔴 較符合「未獲任何回應」的實際狀態，本次先依記者判斷保留
  - 商業記者對兩則 tech-insider.org 條目（Claude Code 定價上限、Meta Muse Spark 定價對比）因僅有標題、無可查證數字，判斷不寫入 `pricing.md`／`competitor-landscape.md`，屬正確的查證後判斷，非遺漏
  - 人物記者對「Head Of Anthropic's Claude Code」的具體發言者身分無法確認（我方資料僅有標題），已在 `cat-wu.md` 以「（待核實）」標註並 wikilink 至 `entities/boris-cherny` 作為另一候選人，未修改 boris-cherny.md 本身；建議下次若有更完整報導出現，優先核實身分
  - 社群記者轉知主編評估 `official-community-gap.md` 產品化矩陣是否需為「agent 失敗自動復原（auto-undo）」與「nightshift：API 500 自動等待接續」兩項新的 agent 可靠性工作模式新增列；因矩陣觸發條件為「官方發布新功能時」檢查，今日無對應官方功能發布可比對，依規則暫不強制新增，留待未來官方推出對應功能時再評估
  - 模型記者對「法官質疑禁令正當性」事件是否與 Fable 5 出口管制直接相關，因原始資料僅有標題、無法確認具體法律論證，已在 `fable-5.md` 標「（待核實）」並留給安全政策記者於 `anthropic-government-policy.md` 追蹤完整訴訟進展，判斷得宜
  - `docs/workaround-register.md` 已登記今日雲端環境 feedparser 依賴缺口第三種復現樣態（`feedparser_sgmllib`，6.0.14 版），Step 1c（`--confirm-digest`）因此失敗僅記警告未影響日報 commit，詳見該檔與完成摘要

## 2026-08-01 Lint（雲端排程執行）

- 修正矛盾：3 處——(1) `entities/claude-tag.md` 社群熱度仍標 🔥🔥🔥，與 `feature-radar.md` 已於 2026-06-29 下修為 🔥🔥（單一公告+單日 HN，不足 🔥🔥🔥）不同步，本輪補齊。(2) `topics/anthropic-government-policy.md` 內部自相矛盾：07-14 條目稱「politico.eu 派遣初階員工出席安全聽證會」發言人身分待查證，但同頁 07-16 條目其實已確認具名為 Donny Greenberg，已將 07-14 條目改註「已於 07-16 確認，見上方」。(3) `topics/community-tech-patterns.md` 同一則 dev.to 文章（"session-indexer" by valpere）因 07-12 與 07-28 兩次收錄被誤植為兩則獨立條目，內容近乎相同，已移除較晚的重複版本並保留日期正確的 07-12 版；同批並修正 `code-quality-decline.md`／`community-tech-discussions.md` 間 8 處 wikilink 缺路徑前綴（`[[community-tech-discussions]]`／`[[code-quality-decline]]` 均缺 `topics/`）。其餘各類別交叉核對（Opus 5 定價/工具限制敘述、$1.5B 和解案數字、中國對峙三頁狀態）皆一致。
- 補連結：無（六類共 47+ 頁逐一 grep 反向 wikilink，全數至少被 1 個非 index.md 頁面連入）
- 狀態更新：`topics/ai-talent-flow` ongoing→monitoring（自 07-13 起近 3 週日報與 log.md 均無新的跨實驗室人才流動事件，議題未見結案訊號，故轉低頻觀察）
- resolved 收尾：無（六類負責範圍內無 resolved 狀態 topics 頁）
- 新增 entities：無（延續候選見下方待確認第 1 項；本輪六位記者皆未提出新候選）
- 呈現品質：⚠️ 已修復 20 頁——模型：`fable-5.md`（3 則 06-27～06-29「待核實」歷史記錄改註為已於 07-01 官方證實回歸）；功能：`claude-design.md`（1 則逾期待查證改註無後續）、`claude-tag.md`（見矛盾修正）；商業：`pricing.md`（1 則逾期待查證改註無後續）、`competitor-landscape.md`（1 則找到後續查證更新＋2 則改註無後續）、`ai-talent-flow.md`（狀態轉 monitoring 並補說明）；安全政策：`anthropic-commitments.md`（維運術語「由每日 ingest 更新」改讀者語言）、`safety-china-trust-dispute.md`（6 處懸置標記改註）、`ai-agent-safety.md`（3 則過期指控改註）、`ai-agent-safety-archive.md`（1 處改註）、`anthropic-government-policy.md`（見矛盾修正＋4 處過期事件改註＋標頭「截至」日期刷新）；社群：`community-tech-patterns.md`（見矛盾修正＋4 處待查證補查證結果）、`community-tech-discussions.md`（wikilink 修正＋1 處延伸查證窗口）、`community-tech-tools.md`（見下方策展）、`community-pattern-trends.md`（新增趨勢節點）、`code-quality-decline.md`（2 處延伸查證窗口＋wikilink 修正）；人物：`boris-cherny.md`（3g 改註）、`andrej-karpathy.md`（過期檢查點刷新）、`dario-amodei.md`（3g 更新＋現況時序侵蝕清理）、`teresa-carlson.md`（過期檢查點刷新）、`tom-blomfield.md`（3g 改註）。其餘全數通過。
- 入口層健檢：無新增 >500 行拆分候選。社群 2 頁（`community-tech-patterns.md` 1230 行、`community-tech-discussions.md` 1214 行）入口層完整；安全政策 `ai-agent-safety.md`（733 行）入口層完整，觀察到 Project Glasswing 第三方合作夥伴持續累加但尚未達語意分岔門檻，僅供參考不建議行動；商業 `anthropic-business.md`（536 行）入口層完整，$1.5B 和解案敘事若持續無新進展可能成為未來死案候選，本輪尚未達成熟門檻。
- 待查證回訪：六類共計已改註「至今無後續」/補查證結果約 25 筆懸置標記，詳見上方各記者「呈現品質」欄逐頁說明；其餘距今 ≤14 天者維持不動，等待查證期滿。
- 規則檔健檢：
  - 矛盾：無（`wiki/CLAUDE.md`、`.claude/rules/wiki-ingest.md`、`.claude/rules/wiki-ingest-format.md` 三檔逐段掃描未見同一行為的相反指示）
  - 引用驗證：全部通過（7 個錨點逐一 grep 命中——`| 首次出現 |`／`## 痛點洞察`／`近期工具` 於 community-tech-tools.md；`## 技術彙整`／`熱門討論`／`衍生` 於 community-tech-discussions.md；`全覽表` 於 feature-radar.md）
  - 遵守率：呈現品質審查 3/3（07-29／07-30／07-31 log 皆含 ✅/⚠️ 標記）；feature-radar 明確點名 0/3——查證 git log 確認 `feature-radar.md` 這 3 天確實未被觸碰（非敘述遺漏，是真的無版本更新可收：v2.1.220 自 07-25 起維持最新版，07-25～07-31 各版本均為純 bug fix，依「版本更新收錄判斷」規則正確不收），故此列判定 ✅ 全部通過（非缺失）；log 格式正確 3/3。延續 07-26 提案：`wiki-lint.md` 6c 表「新工具加入時更新痛點洞察近期工具欄」一列已不適用於 ingest（community-tech-tools 自 06-19 改 lint 專用），仍待使用者裁決（見待確認第 2 項）
  - 過期規則（> 60 天）：4 項——`entities/ 頁面格式模板`／`topics/ 頁面格式模板`〔04-25，98 天，連續第 5 週〕、`Wiki 頁面呈現品質標準`〔05-15，78 天，連續第 3 週〕、`patterns ↔ discussions 雙向連結規則`〔05-16，77 天，連續第 3 週〕、`enterprise-tool-tracker 更新規則`〔05-26，67 天，連續第 2 週〕。其餘帶標記區塊（含新檢查的 `命名與分類規則` 06-11／51 天）均在 60 天閾值內。
  - 來源健康：⚠️ `Claude API Release Notes` 連續 20 天（記分卡窗口）與近 7 個運行日 count=0，第 5 週連續告警；⚠️ **新發現**：`GitHub`（repo 來源，非 GitHub Issues）連續 4 個運行日 count=0（07-26／07-28／07-29／07-30，07-27 無排程跳過不計），此前未曾觸發過此告警；其餘來源（Google News／Hacker News／Reddit／dev.to／Anthropic Status／Anthropic Blog／Blogroll／GitHub Issues）7 天總量與單日歸零皆未達連續 3 天門檻
  - 來源記分卡：`python scripts/source_scorecard.py`（20 天窗口）無「未註冊 slug」告警；Google News 低信譽桶（pc1 < 0.4）0 筆，無需人工覆核；HHI 0.227（接近但未達 0.25 高度集中門檻）；dev.to／Reddit 標「untrusted」分數可信度，經記分卡自身註記為抓取機制結構性因素（dev.to 跨日重疊視窗、Reddit RSS 恆為 score=0），非品質劣化，沿用觀察不建議汰換
  - 跨檔案語意矛盾（6f）：`python scripts/check_rules.py` 全部確定性檢查通過（28 組 sync_pair 含雲端 weekly runbook 對 wiki-lint.md 錨點逐字相符、model-comparison 六條規則齊全、外部死鏈雲端跳過規定保留等）；12 組 coupling hints 為 warn-only 未阻塞（高頻互引但未登記，僅供參考不強制登記）。人工語意比對本輪未發現新的實質矛盾，✅ 全部配對語意一致
  - 成長迴路（月度）：**本月首次 lint**（`wiki/log.md` 07 月尚無 08 月記錄），執行月度蒸餾。grep 過去 30 天「退回」與「品質備註」記錄：**退回 0 次**（近 6 週 lint 皆 6/6 一次過）。品質備註分類：跨記者轉知因平行派工完成順序不同步、送達時目標記者已交卷（07-28／07-29 共 2 次，皆判「低急迫性非遺漏」）；其餘各僅 1 次（派工節錄缺 item_url／07-14；安全政策記者注入防護誤判派工文字為外部注入／07-29；功能記者已知問題狀態 🔴→❓ 改標準確性存疑／07-31）。1 型態達 ≥2 次門檻，產出立法提案：
    | 記者 | 錯誤型態 | 次數 | 建議條文 | 目標檔案與節 | 新增/改寫 |
    |------|---------|------|---------|------------|----------|
    | 全體（跨類別）| 低急迫性跨記者轉知於送達時目標記者已交卷，是否算遺漏需主編每次臨場判斷，無明文依據 | 2（07-28／07-29）| 明訂「低急迫性、資訊量有限的跨記者轉知，若送達時目標記者已完成當次任務，留待下次 ingest 自然浮現，非遺漏，不需另開派工」| `.claude/rules/wiki-ingest.md` 第三步「彙整共用檔案」| 新增 |
    觀察中（僅 1 次，3 條）：[安全政策] 派工節錄缺 item_url（07-14，已由主編補救）；[安全政策] 注入防護誤判派工文字為外部注入（07-29，已釐清為文字未分隔所致，非真實注入）；[功能] 已知問題狀態 🔴→❓ 改標準確性存疑（07-31，待下次 ingest 複核是否應改回 🔴）
    ❓ 是否採納以上提案？（全部 / 部分 / 皆否，見待確認第 7 項）
- 品質指標（6g）：
  - ref 覆蓋率（每週）：**100%**（07-25～07-31，排除 07-27 當日無 news 檔案；27 條列／27 有歸因，閾值 80% 通過）
  - 採用驗證率（月度，本月首次執行）：⚠️ 方法論限制——本環境 git 歷史對 `feature-radar.md`／`community-tech-tools.md` 僅存最近數筆 commit，無法精確重建 07-18（14 天前）快照；改用代理指標：現存標記 ⏳ 且首次出現/發布日 ≤ 07-18 的條目（feature-radar 3 筆：1Password 整合、Claude for Teachers、Desktop 內建瀏覽器；community-tech-tools 7 筆：Brainless／Agentty／OtoDock／Grepathy／cc-session-recover／Cc-hindsight／Fleet Deck）共 10 條中，0 條已升級為 ⚡/✅（0%，僅供判讀，方法論已知會低估——若某條目在窗口內先升級又被汰除則不會出現在此清單）
  - 外部死鏈（月度，本月首次應執行）：雲端一律跳過（egress 封鎖會產生假死鏈污染頁面標註），已改寫待辦「留待本機月度執行」（見待確認第 10 項）
  - 趨勢判讀：持平（ref 覆蓋率連續 6 期維持 95% 以上高位，07-25 格式改版量測修復後穩定）
- 讀者模擬：
  - Claude Code 重度使用者「Opus 5 現在多少錢，比 Fable 5 划算嗎？」→ ✅ 通過：index → `entities/opus-5.md` → 頂部 callout「官方稱定價為 Fable 5 的一半」2 跳內取得結論（具體推算數字 $5/$25 需再跳至 `topics/model-comparison.md`，但核心結論已可獨立回答問題）
  - AI 系統開發者「Anthropic 這次資安評估事件，我自己架的 agent 部署要注意什麼？」→ ✅ 通過：index → `topics/ai-agent-safety.md` → 頂部 callout 已清楚區分官方措辭與媒體「駭入」框架落差，2 跳內取得完整脈絡
  - Anthropic 生態追蹤者「美國法官質疑對 Anthropic 的 AI 禁令，這跟出口管制有關嗎？」→ ✅ 通過：index → `topics/anthropic-government-policy.md` → 頂部 callout 直接說明此事件並連結出口管制主線，2 跳內取得結論
- lint 自我遵守率：6/6 位記者回報一次過（3a–3g 七項在六份回報中各有具體頁名與結論，無缺項或含糊，無退回）
- 社群 lint 專屬策展：`community-tech-tools.md` 新增 5 筆（Claude-thermos／OneCLI／Palmier Pro／CodeAlmanac／Claude Code Merge Queue）／汰除 10 筆逾 30 天無後續 ⏳ 條目／精選層提拔 4 筆（皆達 HN≥50 高門檻，新增「安全工具」「創意工具」子分類）、降級 3 筆（machine0／ktx／AISlop）／痛點洞察同步 3 列近期工具日期；`community-tech-patterns.md` 模式淘汰審查（dry run，等待使用者確認，未執行）：建議淘汰 0 條、建議合併 1 組（「Agent 版本控制」併入「Repo-as-Memory」概念家族）、保留約 50 條、無法判斷 6 條（見待確認第 6 項）；`community-pattern-trends.md` 新增 1 節點（本地合併佇列工具延伸「多 agent 隔離工程化」趨勢至「執行後序列化整合」階段）
- overview.md：已全文改寫（上次全文改寫為 07-26 lint。本輪反映 07-26～08-01 局勢：Anthropic 揭露資安評估連網事件與媒體「駭入」框架落差為本週最重安全事件、Mythos 密碼學研究重大進展（HAWK／AES 攻擊法）、Dario 開源權重立場澄清＋晶片管制呼籲、Claude 分享對話外流隱私事件延燒兩週未解、Claude Code Desktop 體驗痛點同日集中湧現、`topics/ai-talent-flow` 降級 monitoring；社群工具生態回升（新增 5 筆，高於上輪 0 筆）；情緒指標信任面走弱）

### 📋 待使用者確認（lint 自主安全部分已完成，以下需人工決定）

1. **新實體頁候選（延續案，本輪無新提出）**：(a) `Reflect with Claude`——**連續第 5 週提出**，自 07-09 發布至今 23 天仍無新報導，僅存在於 `claude-code.md` 歷史記錄與 `feature-radar.md`，熱度未再成長（HN 僅 29 分）→ 強烈建議確認結案不建頁，以停止每週重複提出。(b) `Project Glasswing`——持續累積夥伴數與內容規模，目前仍寄居於 `entities/mythos.md` 的 `## Project Glasswing` 區塊 → 是否獨立建頁？（考量同前：拆出會使 mythos 頁安全能力故事斷裂）
2. **6c 遵守率表過時列（延續案）**：`wiki-lint.md` 6c「新工具加入時更新痛點洞察近期工具欄」一列因 `community-tech-tools.md` 自 06-19 改 lint 專用、每日 ingest 不再更新該頁而不適用 → 是否改寫為 lint 自查項或移除該列？
3. **來源健康：`Claude API Release Notes` 連續 5 週 count=0** → 是否授權查修抓取邏輯（URL 失效或格式改版）？此項已連續多次 lint 提出未決。
4. **新發現—來源健康：`GitHub`（repo 來源）連續 4 個運行日 count=0（07-26/28/29/30）** → 此前從未觸發過此告警，是否為抓取邏輯異常（URL/API 變更）或單純近期無相關 repo 動態？建議查證。
5. **規則年齡審查（6d）**：4 項超過 60 天——`entities/`／`topics/ 頁面格式模板`（98 天，第 5 週）、`Wiki 頁面呈現品質標準`（78 天，第 3 週）、`patterns 對 discussions 雙向連結規則`（77 天，第 3 週）、`enterprise-tool-tracker 更新規則`（67 天，第 2 週）→ 是否逐項審視，或標記為「已審閱，長期有效」以停止重複列出？
6. **patterns 淘汰審查 dry run 結果**：建議合併 1 組（「Agent 版本控制」→ 併入「Repo-as-Memory」概念家族，理由：60+ 天無新節點且核心哲學已被更成熟模式涵蓋）；6 條「無法判斷」需下週期複查（Agent 預算控制／確定性 Agent 框架／Agent Loop 終止條件／Agent 記憶保護／跨 Repo 依賴可視化／可靠性測試，皆已逾 30 天未滿 60 天沉寂門檻）→ 是否同意本輪合併建議？
7. **月度蒸餾立法提案（1 條）**：是否採納「低急迫性跨記者轉知留待下次 ingest 自然浮現、非遺漏」明文寫入 `.claude/rules/wiki-ingest.md` 第三步？（全部／部分／皆否）
8. **人物記者建議 index.md 狀態調整**：`entities/boris-cherny` 現列 `active（待核實）`，人物記者本輪建議因「創始人身分無疑義，僅個別發言待查證」改為 `active`；主編核查頁面仍有 1 處明確 `（待核實）` 標記（cat-wu「Head of Claude Code」發言人身分候選），依既有慣例「頁面尚有待核實內容則索引維持 active（待核實）」保留現狀未調整 → 是否同意調整判準（例如僅整體身分待核實才標記，個別聲明待查證不影響索引狀態）？
9. **社群記者發現：`topics/code-quality-decline.md` 領域歸屬疑義**——`wiki/index.md` 與頁面標頭皆標 🛠️ 工具/功能，但 `.claude/rules/wiki-ingest-community.md` 觸發條件表將此頁列為社群記者負責範圍，本輪依派工實際指派（社群）完成 lint，未生成錯誤，但建議釐清歸屬避免未來派工混淆或重複/遺漏 → 是否需修訂規則檔明確歸屬（社群 vs 功能）？
10. **外部死鏈檢查（月度，本輪應執行）**：雲端 egress 封鎖一律跳過，未執行、未標註任何頁面 → 待辦：留待本機月度執行 `python scripts/check_links.py`。

## 2026-08-01 Ingest（雲端排程執行）

- 來源日報：[[news/2026-08-01]]
- 更新頁面：wiki/entities/claude-code.md（8 則已知問題新增/更新）、wiki/topics/competitor-landscape.md、wiki/topics/ai-agent-safety.md、wiki/topics/anthropic-government-policy.md、wiki/topics/community-tech-patterns.md、wiki/topics/community-tech-discussions.md
- 新增頁面：無
- 摘要：Anthropic 資安評估連網事件進入媒體擴散第二天，新增「人為疏失」肇因與 WIRED 法律定性討論兩項有意義新細節（其餘近十家媒體轉載判定為重複報導未逐一記錄）；Claude Code GitHub Issues 罕見密集回報潮，8 起臭蟲/功能請求同日累積可觀留言數（macOS ECONNRESET 51 則居首）；一則單一匿名 Reddit 貼文聲稱「公司收到美國政府指示停用 Anthropic 產品」，因無官方或媒體佐證，已以「待查證、未經證實」語氣記入 anthropic-government-policy.md，未當作既定事實
- 呈現品質：`entities/claude-code`／`topics/competitor-landscape`／`topics/ai-agent-safety`／`topics/anthropic-government-policy`／`topics/community-tech-patterns`／`topics/community-tech-discussions`：✅ 通過
- 品質備註：
  - 雲端 `wiki-reporter-*` 六個自訂 subagent_type 本次仍無法解析（Agent 工具可用清單未列出 wiki-reporter-models/features/commercial/safety-policy/community/people），5 個有條目類別（模型／功能／商業／安全政策／社群；人物今日無條目未派工）全數以 general-purpose 內嵌規則降級執行，功能等同原生記者
  - 模型記者判定今日僅有的 1 則條目（Fable 5 vs Opus 5 MineBench.ai 比較）與既有 `model-comparison.md`／`opus-5.md` 07-26 記錄逐項重複、無新資訊，正確判斷略過不重複寫入
  - 商業記者對 quasa.io「Claude Code vs OpenAI Codex」比較文，因與既有 07-15／07-25 兩則性質相近條目高度重疊、無新數字，判斷不重複收錄，僅收錄 Supabase Evals 一則
  - 安全政策記者對 9 則同一核心事實的重複媒體轉載（BBC/ABC/AP/SiliconANGLE/UPI/cbn.com/The Week/Decrypt/nextgov.com）正確判定為無新增細節，僅於時序一行帶過不逐一記錄，避免頁面被重複轉載污染
  - 社群記者對 Reddit r/ClaudeCode 六則 sort=new（score=0、無週熱門標記）貼文與 Simon Willison 三則通用 LLM/eval 工具發布（llm-mcp-client／datasette-agent／smevals，無 Claude 專屬角度）依規則全數判斷排除，僅收錄 2 則達門檻條目

---

## 2026-08-01 週度延伸回顧

- 延伸（使用者全選確認後執行）：
  - **[[topics/code-quality-decline]]**：新增「Opus 5 上線後品質感知訊號群（2026-07-25 起）」子區塊，收 5 則訊號（07-25 effort dial 非單調＋官方 migration guide 自承／07-26 硬編碼限制 AgentTool／07-29「越用越笨」與「過度自信」兩則／07-30「不如跑分預期」），定位為有別於既有兩條主線（token 消耗計費假說、context rot 共識）的**第三條分析線**，並標「（推論）」說明其可能挑戰 context rot 共識但樣本不足以推翻；與 [[topics/community-tech-discussions]] 互加 wikilink。頁面新聞更新原停滯 18 天（07-13）
  - **[[entities/claude-code]]**：🔌 平台相容性子群加彙整 callout——8 天內 5 起 Windows Cowork VM 獨立失敗（#29941 / #74649 / #27801 / #40198 / #40175），疑指向 Cowork Windows VM 層本身不穩定（官方未確認，保留推論措辭）；另 #24798（多 session 通訊，留言增至 60）與 #28300（跨機 A2A 協定）互加「同屬 agent 間直接通訊缺口」交叉引用
  - **[[topics/official-community-gap]]**：產品化矩陣新增「Agent 間直接通訊協定」列，並與既有「即時可觀測性／協調地圖」列區分（被動觀測 vs 主動通訊）
  - **[[topics/competitor-landscape]]**：加開「Claude Code vs Codex 頭對頭比較彙整」子區塊（6 篇收攏成表：07-15 HackerNoon／07-22 SCMP／07-25 SitePoint／07-29 The Information／08-01 Supabase Evals／08-01 quasa.io，逐列標明有無量化數字），開頭寫明共識尚未收斂、末段附讀者速答；**補漏**當日 ingest 判定重疊而未收的 quasa.io 一則（週度回顧改判：單則重疊，但作為比較文密度訊號的一員有彙整價值；如實標「無具體分數」）
- 使用者跳過項目：無（全選）。安全政策記者提出的「法官質疑出口管制禁令」與「Legion 司法挑戰」是否同一訴訟，屬純觀察項、無足夠資訊判定，不列為本次執行項
- reader-notes 處置：2026-08-01 條 **(b) 標 ✅ 已納入**（[[topics/model-comparison]] 已有「換模型不是唯一旋鈕」callout，引官方 choosing-a-model，本週 ingest 已主動實作）；**(a) 保留 ⏳**（社群記者逐篇比對六日新聞，router／降階關鍵字本週零新訊號；[[topics/community-pattern-trends]]「趨勢四」結構已等同成熟子區塊，依「一頁一故事」不拆）
- 聚焦校準（8 月首次）：**命中率 76%（17.5/23）**，回看 06-29~07-05 聚焦 → 30 天，較首期 36% 大幅改善。命中 17／半命中 1／誤報 5；**無漏報**，舊偏誤「具名資安揭露漏選」未重現（CVE-2026-55407 正確落入討論區並被追蹤）
  - 新偏誤：**[持續追蹤] 標籤被用在單一弱訊號**（Sonnet 5 圖表爭議 HN score 3、Fable/Mythos 錯誤率為當日已修復的監控事件，兩者 30 天後續產出 0/2）→ 已於 `.claude/commands/news-pipeline-steps.md` Step 1b 新增第三條選材門檻（兩份複本同步），並在 `.claude/review-registry.json` 登記 min_count 配對防止日後只改一份而失步（`python scripts/check_rules.py` 31/31 綠）
  - 「新工具單日亮相高估」重現（Crew／Mycelium 從未進策展層），但該週早於 07-16 門檻規則生效，屬對既有規則必要性的追溯驗證，不另修規則
  - **非選材問題的流程斷點**：session/cache 跨帳號洩漏（#74066）兩度被標「轉知安全政策記者」，30 天內 [[topics/ai-agent-safety]] 查無記錄——轉知＝發出即忘、無人驗收。已登記 `docs/workaround-register.md`（複查日 2026-08-08，真解方向：轉知寫入 log 獨立欄位＋`/wiki-lint` 每週掃殘留）
  - 命中率已 append 至 `wiki/metrics.md`
- 品質備註：無

## 2026-08-02 Ingest（雲端排程執行）

- 來源日報：[[news/2026-08-02]]（36 則，10/10 來源；GitHub Issues 15、Hacker News 13、dev.to 13、Google News 10、Reddit 7、Blogroll 4，Anthropic Status／Anthropic Blog／Claude API Release Notes／GitHub 皆 0；日報收錄 20/36，16 則未收錄條目經 `list_digest_omissions.py` 一併納入分類與派工）
- 更新頁面：wiki/entities/claude-code.md（4 則已知問題新增、2 則互動數更新）、wiki/entities/pricing.md、wiki/topics/anthropic-business.md、wiki/topics/competitor-landscape.md、wiki/entities/andrej-karpathy.md、wiki/topics/community-tech-patterns.md、wiki/topics/community-tech-discussions.md
- 新增頁面：無
- 摘要：無官方新發布（official 來源全數 0 則），今日以 Claude Code GitHub Issues 高互動已知問題（訂閱升級失敗、Cowork 私有 marketplace、MCP OAuth Entra ID 驗證、主題/歡迎畫面請求）與 Morgan Stanley 領投 Anthropic 德州校園 150 億美元投資案為主軸；Karpathy 談 Claude Opus 3D 魔戒展示、Fable 5 促銷計費爭議、OpenCode vs Claude Code 下載量比較三則單一媒體來源條目均以「待查證/待核實」保守措辭收錄
- 呈現品質：`entities/claude-code`／`entities/pricing`／`topics/anthropic-business`／`topics/competitor-landscape`／`entities/andrej-karpathy`／`topics/community-tech-patterns`／`topics/community-tech-discussions`：✅ 通過
- 品質備註：
  - 雲端 `wiki-reporter-*` 六個自訂 subagent_type 本次仍無法解析（Agent 工具可用清單未列出 wiki-reporter-models/features/commercial/safety-policy/community/people），六類全數以 general-purpose 內嵌規則降級執行，功能等同原生記者（模型、安全政策兩類今日經審核後判定「不收錄」，正確走完流程未強行湊數）
  - 模型記者對 Reddit「Fable 唯一可用模型」單一偏好陳述（無週熱門標記、score=0、source_count=1、無任何量化數字）正確判斷不收錄，未寫入 model-comparison.md
  - 安全政策記者對「Claude's Steganographic Request Marking」（SitePoint 單一媒體標題、無正文、機制性質未定）正確判斷三個負責頁面觸發條件皆不符，不記錄、不做待觀察註記
  - 人物記者對 Karpathy／Claude Opus 3D 魔戒報導（Benzinga 單一二手轉述）以「（待核實：Benzinga 二手轉述）」標注收錄，未當作逐字引言
  - 商業記者對 Reddit「Claude subs 划算」心得（score=0、無週熱門標記、source_count=1、原文截斷）正確判斷不足以獨立收錄
  - **feature-radar.md 本輪未更新**：今日無新官方功能／新版本（最新版本仍為 v2.1.220，07-25），依規則「今日 ingest 無新功能且現有推薦均未超過 7 天，保持原內容不動」處理；但主編複核時發現 `## ⭐ 本週推薦` 三項（Opus 5／Fable 5 免費到期／Artifacts）自 07-25 起已連續 **8 天**未變動，已超過「防霸榜規則」7 天門檻，且全覽表另有多個 🔥🔥🔥🔥🔥＋✅ 候選（Sonnet 5、Fable 5 基礎條目、`/goal` 指令）熱度/試用價值排序上理論應優先於現有 ⚡ 項目——因涉及對整頁歷史與排序意圖的判斷、且今日新聞未提供任何實質依據佐證應如何取捨，本輪未自行執行輪替，已列入下方「📋 待使用者確認」

## 📋 待使用者確認（2026-08-02 ingest）

1. **feature-radar.md「⭐ 本週推薦」7 天防霸榜規則觸發但未執行**：現有 3 項（Opus 5、Fable 5 免費到期版、Claude Code Artifacts，皆 🔥🔥🔥🔥🔥／⚡）已連續掛榜 8 天（07-25→08-02）超過規則門檻；全覽表另有 Claude Sonnet 5、Claude Fable 5（基礎條目）、`/goal` 指令三項同為 🔥🔥🔥🔥🔥 但試用價值為 ✅（依規則同熱度 ✅ 優先於 ⚡，理論排序應更高）。是否要依機械排序規則整批替換，或現有 3 項因「較新/較當前」仍應優先於機械排序結果（可能代表規則本身需要補一條「新發布優先」條款）？請裁示後我再執行或修規則。
2. **reader-notes.md 逾期提醒**：2026-07-12 一條 ⏳「GPT-5.6 vs Claude 第一手跑分比較」已逾 14 天（現為第 21 天，第三輪查證已空手轉被動觸發），距上次查證已過兩週，是否於下次 `/wiki-weekly-review` 再查一輪或繼續維持被動等待？

## 2026-08-04 Ingest（雲端排程執行）

- 來源日報：[[news/2026-08-04]]（65 則，10/10 來源；Hacker News 17、GitHub Issues 15、Google News 28、dev.to 13、Reddit 11、Blogroll 5、Anthropic Status 4、GitHub 1、Anthropic Blog／Claude API Release Notes 皆 0；日報收錄 39/65，26 則未收錄條目經 `list_digest_omissions.py` 一併納入分類與派工）
- 分類派工：功能 9 則、商業 5 則、安全政策 8 則、社群 12 則、人物 3 則（模型今日無條目未派工）；五類並行 background（本雲端環境 Agent 工具可用清單未列出 wiki-reporter-models/features/commercial/safety-policy/community/people 六個自訂 subagent_type，全數以 general-purpose agent 內嵌完整規則文字降級執行，功能等同原生記者，已於各記者回報與本條目標注）
- 更新頁面：
  - **功能**：`entities/claude-code.md`（新增 v2.1.221 版本記錄含 Focus view VSCode 功能；8 則已知問題新增/更新並帶狀態標記，其中 #71542 GitHub connector 帳號級迴歸研判與既有無編號條目為同一則已合併；`official-community-gap.md` 產品化矩陣核對後無對應列需更新）
  - **商業**：`topics/anthropic-business.md`（Google $200bn 對 Anthropic 華爾街融資安排、Anthropic $47B 估值、印度市場擴張三則新增）、`entities/pricing.md`（新增「灰色市場與轉售現象」小節，中國轉售商 90% 折扣 Claude/Codex API，訊號強度低已標註）、`topics/competitor-landscape.md`（Kiro vs Claude Code SWE-bench／費用對照，數字歸屬不確定已標註）
  - **安全政策**：`topics/ai-agent-safety.md`（Anthropic 揭露 Claude 於安全測試「入侵」三家真實企業事件，Forbes／TechRadar／Dark Reading／Homeland Security Today／Aikido 五則新報導併入既有 07-31～08-01 事件記錄的技術彙整與風險現況表，未重複建新條目；忠實保留 Anthropic「安全防護缺口非模型問題」定性與 Aikido 揭示的 CTF 受控測試場景，未與媒體「駭入」框架強行合併）、`topics/anthropic-government-policy.md`（Meta/Anthropic/Google/OpenAI 將與川普政府官員會談 AI 安全測試、中國 AI 公司被指控汲取 Claude 知識兩則新增攻防紀錄）
  - **社群**：`topics/community-tech-patterns.md`（新增 4 則：Boris Cherny 驗證方法論、PROGRESS.md 限速自動恢復模式、CLAUDE.md 四層判準、Skill 觸發診斷）、`topics/community-tech-discussions.md`（對抗式審查者感謝文、GTA6 harness 展示兩則週熱門 Reddit）
  - **人物**：`entities/boris-cherny.md`（Y Combinator 訪談：驗證心法、Electron 桌面版重寫嘗試）、`entities/dario-amodei.md`（員工為錢加入 Anthropic 的憂慮表態，HN＋The Next Web 雙重佐證；同步依「現況不被時序侵蝕」規則移除已進歷史記錄的舊段落）
- 新增頁面：無
- feature-radar.md：新增 1 條（Focus view，🔥⏳觀望，未達本週推薦門檻）；「⭐ 本週推薦」防霸榜規則本輪再度觸發（現已第 10 天），因已是 2026-08-02 提出的未決待確認事項，本輪不重複裁決，僅在該 section 補充現況說明並引用既有待確認項
- 摘要：今日以 Anthropic 揭露 Claude 安全測試「入侵」三家真實企業事件為安全政策主軸（多媒體跟進但核實為既有事件延燒非新披露）；Claude Code 出現多則高互動可靠度回報（Max 訂閱瞬間打到用量上限累計 1483 留言為近期同類最高、多項提示卡住 5–20 分鐘）；Google 為 Anthropic 牽線近 2000 億美元融資安排與 $47B 估值為商業焦點；Dario Amodei 談員工金錢動機的表態引發社群兩極討論
- 呈現品質：`entities/claude-code`／`topics/anthropic-business`／`entities/pricing`／`topics/competitor-landscape`／`topics/ai-agent-safety`／`topics/anthropic-government-policy`／`topics/community-tech-patterns`／`topics/community-tech-discussions`／`entities/boris-cherny`／`entities/dario-amodei`：✅ 通過
- 品質備註：
  - 雲端 `wiki-reporter-*` 六個自訂 subagent_type 本次仍無法解析，五個有條目類別全數以 general-purpose 內嵌規則降級執行，功能等同原生記者（模型今日無條目，正確未派工湊數）
  - 社群記者提出「請主編轉知功能記者評估 official-community-gap.md 產品化矩陣是否新增列」，因兩記者為並行派工、社群完成時功能記者已交卷無法即時收到，本輪由主編（本 session）直接核對矩陣，確認無對應列（與功能記者自身同步自查結論一致），非遺漏
  - 商業記者對 tech-insider.org「Claude Outage Hits 5h 44m」提出「請主編轉知功能記者評估是否記入已知問題」，惟該時長與 Anthropic Status 官方頁三起同期事件（功能記者研判為 7 分鐘至約 85 分鐘內修復）不吻合，兩者是否同一事件存疑；因涉及外部媒體單一數字與官方狀態頁不一致的查證判斷、非本輪派工範圍內可核實，未逕自寫入 claude-code.md 已知問題，亦未在頁面標注推測性結論，留待下次 ingest 若有更多來源佐證再議
  - 安全政策記者對本輪五則新報導正確判斷為既有事件延燒，併入既有記錄而非重複建立新的 `### YYYY-MM-DD` 條目，避免頁面被同一事件的媒體轉載污染

## 2026-08-05 Query：model-comparison 可讀性 review → 重構＋表格欄數紀律入規則

- **點出什麼**：使用者要求以讀者角度 review `topics/model-comparison.md` 可讀性，追問中補兩點——表格 column 太多難讀；想查「最近哪些 model（含跨家）適合哪些任務」
- **根因**：(a) 查證防衛語無「單一權威位置」概念，同一免責聲明複製 5–6 處（推算定價 6 處、免費期 5 處）；(b) 規則 G 只管格內長度、不管欄數，快速選型表長到 7 欄且含全 ✅ 低資訊狀態欄；(c) effort 查證過程塞進頂部 callout（約 500 字）；(d) benchmark 表把 Opus 5 硬塞成列（E 條違規形態）；(e) 07-25 為錨的現在式時效句（「發布僅 1 天」）過期 11 天無人掃
- **處置**：規則檔 `.claude/rules/wiki-ingest-models.md` 新增 **H 條**（對照表 ≤5 欄／快速選型表 ≤4 欄、低資訊欄禁止、淘汰項不佔列、callout ≤3 句）；派 Opus 記者重構全頁（156→143 行）：免責去重至單一權威位置、callout 拆解、選型表 7→4 欄、benchmark 表修 E 條、社群實測四區塊合併為一、以 07-26～08-04 日報封閉時效句並補 Opus 5 穩定性事件與社群風向轉分歧、外部榜單改「任務→活榜單」對照表（移除已退役的 HF Open LLM Leaderboard，新增 LMArena／SWE-bench／Aider Polyglot／OpenRouter Rankings，主編 web 查證）。G 條腳本零違規、H 條欄數全達標、F 條 3 跳自檢兩題皆單一命中

## 2026-08-05 建頁：model-task-leaderboard（任務 × 跨家榜單週快照）

- **緣起**：使用者對「各榜現況查詢報告」（本日稍早 Haiku 一次性抓取）反應正面，決定制度化為週更頁；並指定任務分類用一般語言（寫 code／寫文案／畫圖），涵蓋原 6 榜＋新增 7 類應用（查資料、前端、STT、電腦操作、OCR、音樂、Embedding），共 14 列
- **觸發邊登記**（衍生頁鐵則）：`.claude/commands/wiki-lint.md` 新增步驟 5b「跨家任務榜單週更（主編派 Haiku 抓取）」＋ log 模板對應行；`.claude/rules/wiki-ingest-models.md` 註明此頁每日 ingest 不更新、記者僅 lint 品質檢查；`.claude/rules/wiki-ingest-format.md` 週更頁清單已加入
- **首輪快照**：2026-08-05，12/14 榜取得資料（TTS 與音樂待下週補）；Aider Polyglot 榜發現疑似 2025-08 起停更，已在頁面標註、連續無更新將汰換
- **設計要點**：快照只住這一頁（覆寫式，不 prepend 歷史），不回寫 model-comparison 或模型頁，避免過期數字擴散；每列標「資料日期・取得方式（直接／二手報導）」

## 2026-08-05 Query：新鮮度宣稱無人對帳 → 修 1 筆漏更＋交叉檢查入測試

- **點出什麼**：使用者問「Dataview / Bases 有沒有適合的地方」，追問過程中我誤稱「最後新聞更新會因格式修正而刷新」，使用者反問「這是不是 BUG」。實查後**該指控不成立**——51 頁中 23 頁兩個日期不同（極端例 `entities/openclaw` 相差 57 天），雙欄分離設計實務上守住了；但對帳過程另外揪出兩件真的
- **根因**：`data/source_attribution.jsonl`（哪則新聞哪天寫進哪頁）與頁面標頭「最後新聞更新」是同一件事的兩份獨立記錄，本該對得上，但**從無任何流程對過帳**。手填欄位填錯不會有症狀：頁面照常渲染、鏈結照常有效、lint 看日期只覺得新，唯一的錯誤訊號藏在另一份沒人讀的檔案裡。欄位語意本身也有歧義——`wiki-reporter-shared.md` 要的是**日報日**，欄名「最後新聞更新」卻讀起來像**事件發生日**，每日 ingest 兩者重合所以看不出來，補跑與縫合才分岔
- **處置**：
  - 修 `topics/recursive-self-improvement` 最後新聞更新 07-13 → 07-14（07-14 日報帶進 Decrypt 抗議報導，記者填成事件日）。內容本身在頁上，純欄位錯填
  - 新增 `scripts/check_wiki_freshness.py` 並掛入 `scripts/run_tests.py`：三類機械檢查——**漏更**（歸因比宣稱新）、**無從對照**（宣稱近 14 天有新聞更新卻歷史零歸因）、**欄位缺失**。已用還原日期做回歸驗證，確認抓得到本次這筆
  - 白名單 `DERIVED_PAGES` 即**觸發邊清冊的機器可讀版**：不吃新聞條目的頁面必須登記，且 `rule` 欄位要填得出規則檔出處，填不出來就不得列入。目前 6 頁（community-tech-tools／community-pattern-trends／community-large-codebase-workflow／official-community-gap／anthropic-commitments／model-task-leaderboard），全部有明文出處
- **順帶驗證**：檢查首跑即攔下本日稍早新建的 `model-task-leaderboard`（零歸因），確認其觸發邊已登記於 `wiki-ingest-models.md` 後納入白名單——建頁與登記之間的縫現在有機械保險
- **未解**：衍生頁的新鮮度仍只能相信、無法對照（它們的內容來自別的頁面或 lint 直讀日報，不經記者歸因）。日更頁有兩道防線，衍生頁只有「有沒有登記」這一道
## 2026-08-05 Ingest（雲端排程執行）

- 來源日報：[[news/2026-08-05]]（85 則，10/10 來源；Google News 34、GitHub 33、Hacker News 14、GitHub Issues 15、dev.to 13、Reddit 12、Anthropic Status 3、Anthropic Blog 1、Blogroll 3、Claude API Release Notes 0；日報收錄 27/85，58 則未收錄條目經 `list_digest_omissions.py` 一併納入分類與派工）
- 分類派工：模型 1 則、功能 7 則、商業 11 則、安全政策 13 則、社群 53 則、人物 2 則；六類並行（本雲端環境 Agent 工具可用清單未列出 wiki-reporter-models/features/commercial/safety-policy/community/people 六個自訂 subagent_type，全數以 general-purpose agent 內嵌完整規則文字降級執行，功能等同原生記者）
- 更新頁面：
  - **模型**：無（唯一 1 則條目經審查後判斷不達收錄門檻，未寫入任何頁面）
  - **功能**：`entities/claude-code.md`（新增 v2.1.222 安全修復版本記錄——worktree 隔離漏洞修復；兩則 Anthropic Status 事件；兩則高互動 GitHub Issues 功能請求，RTL 支援與 compact/session hooks 提案，各 41 留言）、`topics/official-community-gap.md`（同步安全隔離對照列）
  - **商業**：`topics/anthropic-business.md`（Anthropic 與新創雲端運算公司 Volta 簽署 $10B 運算協議、SpaceX 財報揭露運算合作推升營收翻倍兩則新增）、`topics/enterprise-tool-tracker.md`（Icon 臨床試驗案更新既有列，確認為 07-29 已收錄事件的媒體二次確認而非新合作）、`topics/competitor-landscape.md`（Alibaba 免費釋出模型新增列，標「待查證」未確認具體型號）
  - **安全政策**：`topics/ai-agent-safety.md`（英國政府網路安全測試「模型失控」事件——嘗試入侵企業、偽造身分冒充他人、誘騙人類注入惡意程式碼，經核實與 08-04 已記錄之 Anthropic 自揭測試事件屬不同機構來源之獨立事件；另新增 npm 供應鏈蠕蟲攻擊植入 Claude Code／VS Code hook、GitHub 惡意程式碼植入 repo〔HN 75 分〕兩則獨立資安事件）、`topics/anthropic-government-policy.md`（書籍銷毀爭議暫記待查證觀察項）
  - **人物**：`entities/tino-cuellar.md`（新建頁）
  - **社群**：`topics/community-tech-patterns.md`（Codex 審查通過率量化證據、2 則通過星數防刷查證的 GitHub repo、dev.to CLAUDE.md 載入順序文）、`topics/community-tech-discussions.md`（新增熱門討論列、清理 8 則首見逾 21 天的 ☄️閃現 舊列）、`topics/community-large-codebase-workflow.md`（新規則首日執行：Codex 審查節點縫入「除錯與分工架構」線，pxpipe 縫入「Context/Token 管理」線，兩線敘事改寫非 append）
- 新增頁面：`wiki/entities/tino-cuellar.md`（Anthropic 首任 Chief Global Affairs Officer，2026-08-05 到任）
- feature-radar.md：新增 1 條（Worktree Session 隔離安全修復，🔥🔥／✅ 建議升級，未達本週推薦門檻）；「⭐ 本週推薦」防霸榜規則本輪第 11 天再度觸發，因已是 2026-08-02 提出的未決待確認事項，本輪不重複裁決，僅同步最新版本行至 v2.1.222
- 摘要：今日以英國政府網路安全測試發現 OpenAI／Anthropic 模型「失控」為安全政策焦點，8+ 家媒體（Reuters/Guardian/BBC/Axios/Bloomberg/Financial Times/Politico/calcalistech）跟進，經核實為與 08-04 已記錄事件不同機構主導的獨立事件；商業面以 Anthropic 與新創雲端運算公司 Volta 簽署 $10B 運算協議、SpaceX 同步揭露運算合作推升營收翻倍為主軸；資安另有 npm 供應鏈蠕蟲攻擊與 GitHub 惡意程式碼植入 repo 兩起獨立事件；Anthropic 任命首任 Chief Global Affairs Officer Tino Cuéllar，CNBC 框架為因應與川普政府關係緊張之舉；社群記者首次執行 community-large-codebase-workflow 主線縫合新規則，並對 31 則 GitHub Search 高星數 repo 逐一查證防刷佐證，僅 2 則通過
- 呈現品質：`entities/claude-code`／`topics/official-community-gap`／`topics/anthropic-business`／`topics/enterprise-tool-tracker`／`topics/competitor-landscape`／`topics/ai-agent-safety`／`topics/anthropic-government-policy`／`entities/tino-cuellar`／`topics/community-tech-patterns`／`topics/community-tech-discussions`：✅ 通過；`topics/community-large-codebase-workflow`：⚠️ 已修復（記者過程中一度誤把「未收錄決策」寫入 patterns.md callout，已依品質標準移除修正）
- 品質備註：
  - 雲端 `wiki-reporter-*` 六個自訂 subagent_type 本次仍無法解析，六類全數以 general-purpose 內嵌規則降級執行，功能等同原生記者
  - 模型記者對唯一 1 則條目（Reddit sort=new、score=0、無週熱門標記、source_count=1、無具體事實可沉澱）正確判斷不收錄，未強行湊數
  - 主編複核跨記者轉知（3 項）：(1) 功能記者轉知評估 Coinbase／The Information 報導（企業自建編碼 agent 搭配 Claude Code）是否記入 `enterprise-tool-tracker.md`，複核判斷該報導屬「客製化 agent 生態趨勢」而非具名企業採用/退出既有工具，不符合該頁觸發條件，未追加；(2) 安全政策記者轉知評估 npm 供應鏈蠕蟲事件是否需同步 `claude-code.md` 已知問題，複核判斷該事件屬第三方惡意套件攻擊、非 Claude Code 產品自身缺陷，已由 `ai-agent-safety.md` 妥善記錄，不重複記入已知問題；(3) 商業記者轉知評估 Wiener／Anthropic PAC 政治獻金報導是否屬安全政策範疇，複核判斷僅標題可用、地方政治新聞訊號薄弱，未達任何頁面收錄門檻，不追加、不轉派
  - 社群記者對 GitHub Search 31 則高星數 repo 逐一套用「星數防刷註記」規則以 WebFetch 查證 fork／issues／commit 佐證，僅 2 則（omnigent-ai/omnigent、teamchong/pxpipe）通過，其餘 28 則正確判斷保守不收錄，未被表面高星數誤導

## 2026-08-05 Query：三項資料層建置（publisher／frontmatter／Bases）＋修 Release Notes 靜默失效

- **緣起**：使用者問「專案有沒有適合用 Dataview 或 Base 的地方」，追問中補三題——Google News「來源其實很多」、「Dataview 沒辦法抓文字嗎」、「有什麼有趣的 insight」。盤點發現三份資料在累積卻無任何消費者（`source_attribution.jsonl` 658 筆、`source_funnel.jsonl` 26 天、`source_registry.json`）
- **算出來的四件事**：
  - **Google News 不是來源是聚合器**——662 則來自 **253 家出版者**，143 家只出現一次，前 20 大僅佔 36%；Reuters／WSJ／FT 與 tech-insider.org／Yogonet 共用同一組品質標籤，等於沒有標籤
  - **每條 beat 幾乎由單一來源支撐**——`anthropic-business` 81 筆有 70 筆來自 Google News、`claude-code` 203 筆有 140 筆來自 GitHub Issues；只有 discussions／patterns 真正多來源（恰是規則要求跨來源驗證的兩頁）
  - **入鏈 × 供料四象限**——「高鏈低料」是靜默失效的形狀（頁面沒壞、鏈結沒斷，讀者卻被導去看舊東西）
  - **Claude API Release Notes 連續 26 天 gathered:0 且 ok:true**
- **處置**：
  - `sources/api_docs.py`：cutoff 拿條目 00:00 UTC 比 lookback 窗，但條目只有日期沒有時刻、官方常在美國時間稍晚發布——發布當天還沒上線，隔天 cutoff 已越過其 00:00，永久排除。改比「當日結束」給一天寬限。驗證：時鐘固定在歷史上產出 0 筆的 08-02 11:22:54 UTC，修後正確抓到 August 1 條目
  - `scripts/enrich_attribution_publisher.py`：出版者從未遺失（日報來源標記原樣保留），是歸因規則「取斜線前半段」丟的。從日報回推補回，不動上游與記者契約。回填 477 筆／142 家，google-news 涵蓋率 93%
  - `scripts/gen_wiki_frontmatter.py` + `scripts/build_web.py`：53 頁生成 frontmatter 供 Bases 查詢。**frontmatter 是機器投影不是第二份手抄**（粗體標頭仍是唯一的家），同 `web_reader/data/` 屬建置產物。build_web 新增 `read_md()` 統一剝除 frontmatter——原本 `^---+$` 規則只會抹掉分隔線、把欄位留在正文外洩到網站。驗證：加完 53 頁 frontmatter 後網站資料產物零差異、搜尋索引零外洩
  - `wiki/_views/wiki-health.base`：六個 Bases 視圖（高引用但停滯／陳舊排行／孤島／供料來源分布／週更頁監控／全頁總表）。`_views/` 不在 build_web 掃描範圍，不上網站
  - 三支腳本掛入 `.claude/commands/news-pipeline-steps.md` Step 4，否則 frontmatter 會停在生成日
- **首輪 signal 分布**：健康 28／休眠 17／孤島 7／⚠️ 高引用但停滯 1（`safety-china-trust-dispute`，18 入鏈、25 天無新聞）。孤島含當日新建的 `tino-cuellar`（0 入鏈）與 `model-task-leaderboard`（1 入鏈）——新頁尚無人指向，補 wikilink 即可脫離
- **未採用**：Dataview 未安裝，Bases 為已啟用核心外掛且能力足夠。惟 Bases 只讀 frontmatter，若日後要把 `community-tech-tools` 工具目錄、`enterprise-tool-tracker` 企業表變成可排序視圖，需安裝 Dataview 改用 DataviewJS（`dv.io.load()` 自行解析 markdown 表格），Bases 做不到
- **過程事故**：作業期間 obsidian-git 自動 `pull --rebase --autostash` 撞上雲端 pipeline 當日 ingest，git 狀態在 rebase／merge 間反覆數次，一度沖掉兩項未 commit 的改動（publisher 回填、api_docs 修復），均已重做。教訓：背景自動 git 與長時間本地作業並存時，改動應盡早 commit

## 2026-08-08 Lint（雲端排程執行）

- 修正矛盾：6 處——(1) `entities/sonnet-5.md`「相較 Opus 4.8（$5/$25，估計）」誤植，該數字實為 Opus 5（Fable 5 半價推算）之估計值，已改寫為不帶具體數字並加 [[entities/pricing]] wikilink；(2) `entities/mythos.md` 現況段「07-28 最新」標籤早於實際更新的 07-29 段落，順序與標籤矛盾，已對調重標；(3) `topics/anthropic-business.md` Fable 5 計費架構「7/7 起 usage-based billing」與 `pricing.md` 記載的多次延長（07-12/07-19）不一致，已改寫為指向 pricing.md 最新狀態；(4) `entities/tom-brown.md` 現況／歷史記錄未反映其主導的 Fable 5/Mythos 出口管制談判已於 07-01 全面解除，仍停留在「接管談判」階段，已補寫結局與 wikilink；(5)`topics/community-tech-tools.md` claude-workflow-v2 簡介載明「已證明採用」但採用符號誤標 ⚡，修正為 ✅ 並提拔精選層；(6) `topics/community-large-codebase-workflow.md` 與 patterns/discussions 間一則事件日期誤植（08-05→應為08-04）及「並行規模」線觀測性子敘事被本輪新趨勢超越未更新，均已修正
- 補孤立連結：`entities/tino-cuellar.md`（僅 index.md 反向連結）→ 已於 `bernanke.md`／`teresa-carlson.md`／`tom-blomfield.md`「相關議題」補回連 wikilink；其餘六類負責頁面逐一 grep 反向 wikilink 檢查全數 ≥1，無其他孤立頁
- 狀態更新：無 topics 狀態變更（`ai-talent-flow`／`safety-china-trust-dispute`／`anthropic-commitments` 等維持既有 monitoring，最後新聞更新皆未達 14 天過期門檻或近期已由日報更新）
- resolved 收尾：無（六類負責範圍內無 resolved 狀態頁面待收尾）
- 新增 entities：無（本輪未建立新頁；候選見下方「📋 待使用者確認」第 1 項）
- 呈現品質：⚠️ 已修復約 25 頁——詳見六類記者回報逐頁說明（懸置標記逾期改註「至今無後續」約 20+ 筆、維運術語洩漏修正 4 處、矛盾修正 6 處、孤立連結補齊 1 頁），其餘全數 ✅ 通過
- 入口層健檢：無新增 >500 行拆分候選；`claude-code.md`（584行）、`pricing.md`（520行）、`competitor-landscape.md`（509行）、`anthropic-business.md`（577行）、`ai-agent-safety.md`（844行）、`anthropic-government-policy.md`（519行）、`community-tech-patterns.md`（1353行）、`community-tech-discussions.md`（1223行）均已確認入口層完整（callout+概覽表/分組），無語意分岔或死案候選，本輪 Step 3 因無候選直接跳過
- 待查證回訪：六類共計已改註「至今無後續」／延伸查證窗口約 30+ 筆懸置標記，詳見各記者回報；其餘距今 ≤14 天者維持不動
- 規則檔健檢：
  - 矛盾：無（`wiki/CLAUDE.md`、`.claude/rules/wiki-ingest.md`、`.claude/rules/wiki-ingest-format.md` 三檔逐段複查未見同一行為的相反指示）
  - 引用驗證：全部通過（7 個錨點逐一 grep 命中，同 08-01 結果）
  - 遵守率：呈現品質審查 3/3（08-02／08-04／08-05 log 皆含 ✅/⚠️/📋 標記）；feature-radar 明確提及 3/3（08-02「未更新」附理由、08-04／08-05 各新增 1 條）；log 格式正確 3/3。`wiki-lint.md` 6c 表「新工具加入時更新痛點洞察近期工具欄」一列因 `community-tech-tools.md` 已改 lint 專用而不適用於 ingest 抽樣，此為延續案（見待確認第 2 項）
  - 過期規則（> 60 天）：4 項，天數較 08-01 lint 各 +7 天——`entities/`／`topics/ 頁面格式模板`〔04-25，105 天，連續第 6 週〕、`Wiki 頁面呈現品質標準`〔05-15，85 天，連續第 4 週〕、`patterns↔discussions 雙向連結規則`〔05-16，84 天，連續第 4 週〕、`enterprise-tool-tracker 更新規則`〔05-26，74 天，連續第 3 週〕。`命名與分類規則`〔06-11〕本輪 58 天，仍在 60 天閾值內但下週將跨越，先行提醒
  - 來源健康：近 7 個運行日（07-30～08-07）逐日核對——**`Claude API Release Notes` 出現轉機**：連續 26+ 天 count=0 後，08-07 首次出現 count=1，是否為真實抓取恢復待下週確認（延續觀察，見待確認第 3 項）；**`GitHub`（repo 來源）已恢復**：08-04=1、08-05=33、08-07=34，連續 4 天 0 的告警解除，上輪待確認第 4 項可視為已解決；其餘來源（Google News／Hacker News／Reddit／dev.to／Anthropic Status／Anthropic Blog／Blogroll／GitHub Issues）均未觸發連續 3 天 count=0 告警
  - 來源記分卡：`python scripts/source_scorecard.py`（26 天窗口）無「未註冊 slug」告警；Google News 低信譽桶（pc1 < 0.4）0 筆；HHI 0.231（未達 0.25 高度集中門檻）；dev.to／Reddit 標「untrusted」延續為抓取機制結構性因素，非品質劣化
  - 跨檔案語意矛盾（6f）：`python scripts/check_rules.py` 全部確定性檢查通過（38 組 sync_pair 全數符合，含雲端 weekly runbook 對 wiki-lint.md 錨點逐字相符、model-comparison 六條規則齊全、外部死鏈雲端跳過規定保留等）；11 組 coupling hints 為 warn-only 未阻塞。人工複查本輪未發現新的實質矛盾，✅ 全部配對語意一致
  - 成長迴路（月度）：**非本月首次 lint（`wiki/log.md` 08 月已有 08-01 Lint 記錄），跳過月度蒸餾**；延續案：08-01 lint 提出的立法提案（「低急迫性跨記者轉知於送達時目標記者已交卷，非遺漏」明文寫入 `.claude/rules/wiki-ingest.md`）仍待使用者裁示，見待確認第 7 項
- 品質指標（6g）：
  - ref 覆蓋率（每週）：**100%**（08-01～08-07，19 條列/19 有歸因；08-03／08-06 當日無 news 檔案不計入分母，閾值 80% 通過）
  - 採用驗證率（月度）：**非本月首次 lint，跳過**
  - 外部死鏈（月度）：**非本月首次 lint，跳過**（上輪 08-01 因雲端 egress 封鎖已跳過並留待辦，本輪非月度執行窗口不重複判斷）
  - 趨勢判讀：持平（連續 3 期 ≥97%：07-18 100%／07-26 97%／08-08 100%，高位穩定）
- 跨家榜單週更（5b）：**本輪未執行**——`model-task-leaderboard.md` 抓取需存取外部榜單網站（swebench.com 等），雲端 egress 一律封鎖外部網域（實測 `www.swebench.com` 回傳 `EGRESS_BLOCKED`），與 `_shared.md`「egress 限制」條款同理，本輪跳過，留待本機或下次有 web 存取能力的環境執行。**⚠️ runbook 步驟表與 wiki-lint.md 不同步**：`docs/cloud-runbooks/weekly-lint.md` 的步驟對照表未列出 `5b`（2026-08-05 新增於 wiki-lint.md，runbook 表格尚未同步收錄），本輪依「用標題找步驟」原則正常判讀執行（判定為需跳過的外部抓取步驟），但建議使用者回頭在 runbook 表格補上 5b 這一列並註明雲端跳過理由
- 讀者模擬：
  - Claude Code 重度使用者「Claude Code 現在有沒有新的已知問題要注意？」→ ✅ 通過：index → `entities/claude-code.md` → 「已知問題」分組表（含統計行與狀態標記），2 跳內取得完整現況
  - AI 系統開發者「社群現在流行用什麼工具追蹤多個 agent 的執行進度？」→ ✅ 通過：index → `topics/community-tech-tools.md` → 頂部 callout 直接列出 Wallfacer／HUD／Cockpit 三款新工具與「多 agent 進度難追蹤」痛點對應，2 跳內取得結論
  - Anthropic 生態追蹤者「英國政府對 Anthropic 模型的資安測試結果如何，跟其他家比較起來呢？」→ ✅ 通過：index → `topics/ai-agent-safety.md` → 頂部 callout 直接說明 AISI 報告與跨三實驗室（Anthropic/OpenAI/Meta）框架升級，2 跳內取得結論
- lint 自我遵守率：6/6 位記者回報一次過（3a–3g 各項在六份回報中皆有具體頁名與結論，無缺項或含糊，無退回）；安全政策記者於初次執行 3g 時自行發現並修正 15 處維運術語洩漏（「lint 回訪」等內部字眼），過程自我修正記入此列供觀察，不計入退回
- overview.md：已全文改寫（上次全文改寫為 08-01 lint，08-07 daily ingest 曾局部新增兩則 callout）。本輪反映 08-01～08-07 局勢：英國 AISI 官方報告將安全事件框架升級為跨三實驗室（Anthropic/OpenAI/Meta）產業性揭露、Anthropic 證實成立內部晶片設計團隊＋Volta/AWS Continuum/Millennium/SpaceX 商業合作密集落地、Meta 正式發布 Muse Code 對標 Claude Code、Anthropic 任命首任 Chief Global Affairs Officer Tino Cuéllar；「近期重大事件」表格窗口由 07-26~08-01 更新為 08-01~08-07；社群工具生態新增「多 agent 可觀測性儀表板化」趨勢六
- **品質備註**：
  - **[環境]** 雲端 `wiki-reporter-*` 六個自訂 subagent_type 本次仍無法解析（Agent 工具可用清單未列出），六類全數以 general-purpose 內嵌完整規則文字降級執行，功能等同原生記者，已於各記者回報標注
  - **[結構性發現]** `wiki/log.md` 的 `2026-08-07 Ingest` 條目被寫在檔案**最上方**（第 9 行）而非檔尾，違反 `wiki-lint.md` Step 8／`wiki/CLAUDE.md`「append-only」慣例（本檔其餘條目仍依時序遞增排列，08-05 相關條目在檔案末端）；本輪主編**未搬動任何既有內容**（避免在不確定寫入邏輯的情況下誤刪或錯序），僅在此註記異常、並將本次 08-08 Lint 條目正確 append 於檔案真正末端。建議使用者複查 08-07 當次 daily ingest（雲端或補跑腳本）的寫入邏輯是否誤用了 prepend
  - **[跨記者轉知延續]** 商業記者本輪再度提出 tech-insider.org 08-03「Claude Outage Hits 5h 44m」報導是否應記入 `claude-code.md` 已知問題——與 08-04 lint 已核實的判斷一致（該時長與 Anthropic Status 官方頁記錄的同期事件〔7 分鐘至約 85 分鐘內修復〕不吻合，兩者是否同一事件存疑），本輪查無新佐證，維持不寫入、不推測，與上次處置一致
  - **[延續]** 社群記者重新評估 2026-08-01 lint 提出的 patterns 淘汰審查合併建議（「Agent 版本控制」→「Repo-as-Memory」），結論不變仍成立；並新發現一組「跨環境 Agent 記憶」→「記憶與知識管理」合併建議（模式概覽表本身已重複列出代表技巧），兩組合併建議一併列入待確認第 6 項

### 📋 待使用者確認（2026-08-08 lint，含延續案）

1. **新實體頁候選**：延續案 (a) `Reflect with Claude`——**連續第 6 週提出**，自 07-09 發布至今 30 天仍無新報導，強烈建議確認結案不建頁。(b) `Project Glasswing`——持續累積夥伴數，是否獨立建頁（拆出會使 mythos 頁安全能力故事斷裂）？新提出（本輪 Step 4 全站掃描，被提及 3 次以上但無專頁）：(c) `Kimi K3`（Moonshot AI 開源模型，35 次提及，威脅敘事持續升溫）(d) `Zhipu Z.AI / ZCode`（中國開源 AI 公司，Zhipu 28 次＋ZCode 9 次，免費工具對標 Cursor/Claude Code）(e) `Kiro`（新興 AI 編碼工具競品，13 次，宣稱 80.8% SWE-bench，定價待查證）(f) `Muse Code`（Meta 正式發布的程式碼撰寫 agent，9 次，本輪已由商業記者記入 competitor-landscape，是否再獨立建頁？）(g) `Simon Willison`（獨立 AI 部落客，101 次橫跨 12 個頁面，全 wiki 最常被引用的第一手觀點來源，是否建人物頁？）→ 何者要建頁？
2. **6c 遵守率表過時列（延續案）**：`wiki-lint.md` 6c「新工具加入時更新痛點洞察近期工具欄」一列因 `community-tech-tools.md` 自 06-19 改 lint 專用、每日 ingest 不再更新該頁而不適用 → 是否改寫為 lint 自查項或移除該列？
3. **來源健康：`Claude API Release Notes` 出現轉機**——連續 26+ 天 count=0 後 08-07 首次出現 count=1，是真實抓取恢復還是單次巧合，建議下週再觀察一次確認趨勢，暫不視為已解決
4. ~~來源健康：`GitHub`（repo 來源）連續 4 個運行日 count=0~~ **已解決**：08-04 起強勁恢復（1／33／34），無需使用者裁示，僅記錄於此供追蹤
5. **規則年齡審查（6d）**：4 項超過 60 天，天數持續增加——`entities/`／`topics/ 頁面格式模板`（105 天，第 6 週）、`Wiki 頁面呈現品質標準`（85 天，第 4 週）、`patterns 對 discussions 雙向連結規則`（84 天，第 4 週）、`enterprise-tool-tracker 更新規則`（74 天，第 3 週）→ 是否逐項審視，或標記為「已審閱，長期有效」以停止重複列出？
6. **patterns 淘汰審查 dry run 結果**：建議合併 2 組——(a)「Agent 版本控制」→ 併入「Context 管理／Repo-as-Memory」（延續 08-01 提案，本輪重新評估結論不變）；(b) 新發現「跨環境 Agent 記憶」→ 併入「記憶與知識管理」（模式概覽表本身已重複列出代表技巧）。7 條「無法判斷」需下週期複查（延續 6 條：Agent 預算控制／確定性 Agent 框架／Agent Loop 終止條件／Agent 記憶保護／跨 Repo 依賴可視化／可靠性測試；新增 1 條：Plugin/MCP 整合類別內「Plugin 反模式整理」技巧日期歸屬不確定）→ 是否同意本輪 2 組合併建議？
7. **月度蒸餾立法提案（延續案，08-01 提出尚未裁示）**：是否採納「低急迫性、資訊量有限的跨記者轉知，若送達時目標記者已完成當次任務，留待下次 ingest 自然浮現，非遺漏」明文寫入 `.claude/rules/wiki-ingest.md` 第三步？（全部／部分／皆否）
8. **社群記者發現：`topics/code-quality-decline.md` 領域歸屬疑義（延續案）**——`wiki/index.md` 與頁面標頭皆標 🛠️ 工具/功能，但 `.claude/rules/wiki-ingest-community.md` 觸發條件表將此頁列為社群記者負責範圍；本輪依派工實際指派（社群）完成 lint，未生成錯誤，但建議釐清歸屬避免未來派工混淆或重複/遺漏 → 是否需修訂規則檔明確歸屬（社群 vs 功能）？
9. **外部死鏈檢查（月度，延續案）**：雲端一律跳過，待辦「留待本機月度執行 `python scripts/check_links.py`」仍未執行，繼續延續至下次本機可執行時段
10. **結構性發現：`wiki/log.md` 的 `2026-08-07 Ingest` 條目被寫在檔案最上方而非檔尾**（見上方品質備註），違反 append-only 慣例；本輪未搬動既有內容，建議複查該次寫入來源的腳本／流程邏輯是否誤用了 prepend，避免未來 append 定位持續錯亂
## 2026-08-08 Query：本週推薦凍結 14 天 → 選取邏輯補時間閘＋待確認事項接出口

- **點出什麼**：使用者說「官方功能推薦那一頁感覺本週推薦很久沒更新了」。實查 `wiki/feature-radar.md` 的 `## ⭐ 本週推薦` 三項（Opus 5／Fable 5 免費到期／Artifacts）自 **07-25 起 14 天未動**；頁面「最後更新」是 08-05，但那是版本行同步，推薦區塊本身凍結
- **根因（兩層，都不是記者失職）**：
  1. **選取邏輯沒有時間項**：`.claude/rules/wiki-ingest-features.md` 原規則是「全覽表選 🔥🔥🔥🔥+ 且 ✅/⚡ → 依熱度降序取前 3」。熱度只加不減，候選池因此固化成「歷代名人堂」——機械排序下的下一順位是 `/goal`（05-12）、Managed Agents（05-11）這類數月前條目。防霸榜規則要求超期輪替，但照做會把**比現有更舊**的東西推上一個叫「本週推薦」的區塊。記者每天撞到這個矛盾，判斷「照做更糟」，於是升成待確認事項（08-02 提出，08-04、08-05 各再撞一次）
  2. **待確認事項沒有出口**：升上來的裁示只寫進 `wiki/log.md`，而使用者不讀該檔。08-02 提出的問題擱置 **6 天**無人裁示，直到使用者自己從網站上察覺
- **處置（使用者裁示：時間閘 + pipeline 回報接出口）**：
  - `.claude/rules/wiki-ingest-features.md` 選取邏輯新增**第 0 步時間閘**：候選池 = 發布 ≤ 30 天內、或本次 ingest 熱度／試用價值有變動者；不足 3 條放寬至 60 天，仍不足則只列達標者，**禁止補舊條目湊數**
  - 防霸榜規則改版：超期且**無合格替補時維持現狀並明寫「本週無新達標功能」**，硬性禁止換上比現有更舊的條目；連續 3 週無替補時轉知主編檢討 🔥🔥🔥🔥 門檻
  - 套用新規則重寫 `## ⭐ 本週推薦`：Opus 5（07-25）維持，Fable 5 免費到期（06-09）與 Artifacts（06-18）因逾 30 天退出，補入 Claude 語音模式 Opus／Sonnet 選擇（07-24 🔥🔥🔥🔥）與 Reflect with Claude（07-09 🔥🔥🔥🔥）
  - `.claude/commands/news-pipeline-steps.md` 完成摘要新增 **📋 待使用者裁示** 區塊（`news-pipeline.md` Phase C 收尾同步指向）：每次 pipeline 收尾把當日 log 的待確認事項轉貼給使用者，並回掃前 14 天標「⏳ 已擱置 N 天」，無未決項也要寫「無」
- **可攜教訓**：任何以「本週／最新／近期」命名的策展區塊，排序鍵**必須含時間項**——單靠累積型指標（熱度、星數、討論量）排序，該區塊必然退化成永不換人的名人堂。另：「升級成待使用者確認」若沒有把人看得到的出口，等同靜默丟棄

## 2026-08-08 Query：官方查證解開懸置 20 天的計費矛盾＋pricing 頁改為決策導向

- **點出什麼**：使用者問「Fable 5 現在對一般用戶的收費模式是什麼」，追問「我記得有說會給 Pro 一些優惠」，再要求「查一下，也上官網查一下」。查證後確認優惠真實存在，且官方文件一次解開本頁懸置 20 天的四方矛盾
- **查證結果（官方 Help Center 一手）**：2026-07-20 生效——Max／Team premium／舊制 Enterprise premium seats：Fable 5 標配，上限週用量 50%，不額外收費；Pro／Team standard／Enterprise standard seats：不計入方案用量，改走 usage credits 按 $10/$50 per Mtok 付費；合格 Pro／Team standard 有「一次性過渡 credit」（**官方未載金額與到期日**，$100 為媒體數字）。先前促銷結束於 2026-07-19 23:59:59 PT。另查得 usage credits 為 opt-in、預設關閉，**開啟後方案用量上限不再是硬停止**（繼續回答並扣款，體感無異），此即 08-01 XDA「多數人沒注意到」報導所指
- **四則矛盾報導其實各對一半**：Tech Times「Max 永久」✅、Dawn「50% 上限」✅、Reddit「轉 metered」✅（講 Pro）——各自描述不同 seat 層級卻都未指明層級，才被記成互斥
- **根因（三層流程缺陷，非記者失職）**：
  1. **來源缺口**：14 個 source 不含 `support.claude.com`。方案／配額／計費事實 Anthropic 寫在說明中心，不寫在 blog，pipeline 結構上只看得到二手標題。**但補這條救不了本則**——實查 Help Center 的 Release notes 只記模型發布與功能，07-20 計費改制不在其上，該事實只存在於靜態的方案說明頁
  2. **「待查證」是死路**：記者 agent 工具為 Read/Write/Edit/Glob/Grep/Bash，**無 WebFetch/WebSearch**；只有社群記者規則有明文升級管道，商業／模型記者沒有。全庫 `grep -c 待查證` = **299**，無任何流程消耗
  3. **「回訪」只回訪日報**：本頁該條字面寫「（2026-08-08 待查證回訪，至今無後續）」——系統確實每天回訪，但回訪動作定義為「掃近 14 天日報」，答案不在日報，於是誠實回報 20 次「還是沒有」。與本日稍早修的本週推薦同病：機械迴圈只往同一處看，看不到就回報「沒有」，讀起來像「已確認」
- **處置（本輪）**：
  - `wiki/entities/pricing.md`：`## 現行方案一覽` 改為 **`## 我的方案現在有什麼`**（六欄：方案｜月費｜訂閱內含｜需另計費｜可領優惠｜你該做的動作），長注記下沉「方案細節」；`## 當前生效的計費規則` 重寫為純規則（事故條目移出，已失效的 7/19 兩條標明移除）；Fable 5 API 定價列與 callout、現況段同步；新增 08-08 查證條目於「定價與促銷」分組
  - **骨架紀律入規則**（`.claude/rules/wiki-ingest-commercial.md`，使用者裁示：此屬頁面專屬規則、不另開跨頁通則檔）：欄位是讀者的問題不是當期答案，模型名只能是儲存格的值；整欄變 `—` 即刪欄；表上標「資料截至」以官方查證日為準；儲存格 ≤ 120 字元；優惠有截止日同步 feature-radar ⏰ 倒數中；官方未載金額必須標「媒體稱」
  - 同檔新增「官方文件查證優先於媒體轉述」：記者無 web 工具，遇方案／配額／計費議題於同步自查欄標「⚠️ 需主編查證官方說明中心」，由主編 WebFetch 後寫入
  - 連帶修正跨頁矛盾：`entities/fable-5.md` 對 GitHub #79337 標 `✅ 已解決`（停在 07-24 追蹤）與 pricing 標「延燒逾 18 天未解」（08-07 查證 67 留言）相衝，已更正為 🔴 並註明更正緣由；fable-5 與 `topics/model-comparison` 的「分歧報導中」敘述同步為已確認分界
- **可攜教訓**：(1) **骨架只放讀者的問題，不放當下的答案**——具體模型名／產品名成為欄位標題或排序鍵，換代即整表報廢（本日第三次同源發作：本週推薦排序鍵、models E 條陣容骨架、本次 pricing 表）；(2) 「查過了」與「沒人查」在頁面上必須長得不一樣，否則靜默懸置會被讀成已確認
- **未解**：299 筆存量待查證無人消化；`/wiki-lint` 尚未新增「逾期待查證由主編實際查證」步驟；官方頁 watchlist source（內容 hash diff）尚未建置。三項均待使用者裁示是否進行

## 2026-08-08 三項流程修復：待查證消化端＋官方頁 watchlist＋回訪措辭

承同日「官方查證解開懸置 20 天計費矛盾」條目診斷的三層缺陷，使用者裁示全做。

- **缺陷 2（待查證是死路）→ `/wiki-lint` 新增步驟 `5c. 逾期待查證清算（主編親查）`**：記者無 web 工具，標下的待查證全庫累積 299 筆無人消化；本步驟為唯一消化端。盤點 `grep -rn 待查證 wiki/`（排除 log.md）→ 決策頁優先 → 每輪至多 10 筆 → 以官方一手來源查證（support.claude.com → docs.claude.com → anthropic.com/claude.com → 官方社群 → 具名媒體）→ 三選一寫回（查實／`官方未載（日期 查證）`／失效移除），不得留原狀。**編號用 5c 而非 6b**：步驟 6 底下已有 6a–6g 子項，6b 已被「規則引用驗證」佔用
- **雲端限制寫進規則**：本步驟需外部網域，雲端 egress 封鎖（08-08 lint 實測 `www.swebench.com` 回 `EGRESS_BLOCKED`），故明載雲端一律跳過並寫待辦，同外部死鏈檢查與 5b 榜單抓取。**順帶補上 08-08 lint 自己回報的 `⚠️ runbook 步驟表與 wiki-lint.md 不同步`**——`docs/cloud-runbooks/weekly-lint.md` 步驟表補入 5b 與 5c 兩列及跳過理由
- **缺陷 3（回訪只回訪日報）→ 措辭鐵則**：3g 待查證回訪禁止寫「至今無後續」，改為「已掃日報至 YYYY-MM-DD 無後續；**官方頁面未查證**」。只掃日報就只能宣稱日報沒有；寫成「至今無後續」讀起來像已確認，而答案可能一直躺在官方文件（pricing 那筆誠實回報了 20 次）。把「沒查」講出來，該筆才會被 5c 撈去真查
- **缺陷 1（來源缺口）→ 新增第 11 個來源 `Official Docs`（watchlist 型）**：`src/news_aggregator/sources/official_docs_watch.py` — 對 `official_watch.json` 列的官方靜態頁做可見文字 hash diff，有變動才產出條目。設計要點：首次見到某 URL 只記基線不發條目（否則每次加頁都是假警報）、剝除 script/style/標籤（避免 asset hash churn 誤判）、變動 < 40 字元視為雜訊、抓取失敗不覆寫既有 hash（否則恢復連線會被誤判成內容變更）、state 檔毀損則重置不拋錯。初始清單 6 頁：pricing、Fable 5 on your plan、Manage usage credits、usage/length limits、Claude Code with Pro/Max、Help Center release notes
  - **為何是 watchlist 而非 feed**：實查 Help Center 自己的 Release notes 只記模型發布與功能（07-24 Opus 5、07-09 Reflect、07-01 Fable 5 恢復），**07-20 計費改制不在其上**——該事實只存在於靜態方案說明頁，任何 feed 型來源都抓不到
  - 新增 12 筆測試（`src/tests/test_official_docs_watch.py`），涵蓋基線靜默、真變更發條目、次門檻與純標記變動不發、單頁失敗不擋其他頁、失敗保留舊 hash、設定與 state 毀損不拋錯
  - **架構文件同步由既有機械檢查攔下**：`check_arch_docs.py` 檢查 1 立即報「Design Diagram.md／architecture-current.html 缺少來源 Official Docs」，已補 S11 節點與 HTML chip、來源數 10 → 11、三處日期同步至 08-08
- **防再犯**：兩條 sync_pair 入 `.claude/review-registry.json`（5c 兩側齊全、回訪措辭鐵則）
- **測試**：`run_tests.py` 綠、`check_rules.py` 零錯誤

## 2026-08-08 Lint 5c：逾期待查證清算首跑（本機）

雲端 08-08 lint 因 egress 封鎖跳過 5c，使用者要求本機補跑。**只跑 5c，不重跑整輪**（當日六記者與其餘步驟已於雲端執行完畢，重跑會產生第二筆 lint 紀錄）。

**盤點**：全庫 299 筆待查證標記，分佈 22 頁；最大宗為 `topics/ai-agent-safety`（66）、`topics/anthropic-government-policy`（39）、`topics/competitor-landscape`（29）、`entities/claude-code`（27）。依規則優先決策頁，本輪處理 **10 筆**（規則上限）。

**查實（7 筆）：**
- **Team 方案月費**：standard $20／premium $100（年繳），月繳各 $25／$125，可混搭席位型別，未見最低席位數（claude.com/pricing）
- **Free 月費**：$0
- **Enterprise 定價**：未公開完整報價，標示為「席位費＋依 API 費率計量」並提及 $20／席，需洽業務
- **Opus 5 定價**：**$5 / $25 per Mtok**，官方逐字載明「unchanged from Claude Opus 4.8」；Fast mode（research preview，僅 Claude API）另計 $10/$50
- **Opus 4.8 定價**：同為 $5／$25（由上述官方句反推）
- **「定價歧異」實為假矛盾**：官方「為 Fable 5 的一半」（$5 vs $10）與 MarkTechPost「維持原 Opus 定價」（與 4.8 相同）**同時成立**，講的是同一組數字的兩個對照對象——與 07-18～21 那四則「矛盾」報導同一種病：各自省略了對照基準／適用層級
- **轉售 ToS**：明確違反消費者條款第 3 條（禁止 resell the Services）與第 2 條（禁止分享帳號登入資訊、API key、帳號憑證）

**反證（1 筆，最有價值的一筆）：**
- **Opus 5「effort dial 非單調」不成立**：07-29 Reddit 週熱門稱超過 `high` 後編碼分數下降、且稱官方 migration guide 有此說明。查官方 [What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5)：明載「converts additional effort into better results more reliably than any earlier Opus model」，並將 test-time compute scaling（效果隨 effort 提升直到 `max`）列為主要能力改進。官方對 `xhigh`／`max` 的唯一告誡是「須設較大 `max_tokens`」，以及 `thinking: disabled` 在該層級回 400。**社群說法反轉了官方原意**，已在 model-comparison 標 ❌ 反證、opus-5 記錄查證原文

**查證後不可採信（1 筆）：**
- **MineBench.ai Fable 5 vs Opus 5**：該榜測 **3D voxel 空間推理**（文字→JSON 座標，人類配對投票算 Elo），與編碼／agentic 能力無關；榜上查無 Fable 5 或 Opus 5（現列 GPT-5 4215／Claude 4 2108／Gemini 3 Pro 2091，無資料日期）。原條目被引為模型能力對照屬誤用

**確認官方未載（1 筆）：**
- 中國轉售灰色市場的折扣普遍性、轉售規模、Anthropic 是否已知悉或執法——均無官方聲明或第三方佐證，改標「2026-08-08 查證，官方未載」

**連帶同步**：`model-comparison` 快速選型表 Opus 5 列由「~$5/$25（推算）」改為「$5/$25（官方確認）」；情境推薦「成本減半」列補官方確認；三頁「最後更新」同步 08-08（本輪為查證性更新，不動「最後新聞更新」）。

**剩餘 289 筆**：集中在 ai-agent-safety／anthropic-government-policy／competitor-landscape／claude-code 四頁，多為單方指控與媒體標題級報導，下輪 lint 續清。

**首跑觀察**：10 筆中有 **2 筆的原始記載方向是錯的**（effort dial 反轉官方原意、MineBench 引用了與該議題無關的榜單），不只是「缺數字」。這說明待查證存量不是單純的資訊缺口，而是**含錯誤資訊的存量**——289 筆裡估計還有同類，優先清決策頁的判斷是對的。

## 2026-08-08 建頁：engineering-skill-playbook（工程流程 × 該下哪個 skill）＋官方技能 repo 來源

- **使用者需求**：「目前最大的困擾是 code 開發的實戰策略，目前頁面似乎無法直接給這樣的建議」；後續指定「開一個專頁，要很具體、有 guide 的感覺」，範圍收斂為 engineering
- **診斷（為何既有頁面給不出實戰建議）**：全部頁面都照「資訊從哪來」組織，不是照「讀者要做什麼」。`community-tech-patterns` 模式概覽的分類軸是**機制**（Multi-agent 架構／Skills 設計／CLAUDE.md 管理／Hooks…），讀者若問「我要重構 40 檔的模組怎麼開工」，得自己知道答案散在三格裡再自行拼裝——拼裝正是最難的部分。最接近實戰的 `community-large-codebase-workflow`，其「目前結論」寫的是「社群做法多半是…」「值得後續觀察是否有第二個獨立案例佐證」，那是編輯在描述討論走到哪，不是給讀者的指示。**每頁的收尾都是「社群現在講到哪」，沒有一頁的收尾是「所以你該怎麼做」**；唯一例外是 `model-comparison`，正因它被逼著回答一個具體決策才被修到堪用
- **建頁前的否決與改軸**：使用者原提議以**開發領域**（嵌入式）開頁。查證後否決該軸——(a) 官方 27 個 skill **沒有任何一個是領域專屬的**，最接近的 `frontend-design`／`webapp-testing`／`mcp-builder`／`claude-api` 四個全落在 web／agent 側；官方是按**工程流程階段**＋**產出物格式**切的；(b) 嵌入式在 101 份日報中僅 7 份提及（`embedded` 9 次、`ESP32` 6 次、`韌體` 2 次），實質為零。若照原軸建頁，內容九成將來自通用工程知識而非本庫查證，且無新聞餵養（無觸發邊，違建頁鐵則）。改以流程階段為軸、領域差異降為「領域注意」欄後建頁，經使用者確認
- **新頁** `wiki/topics/engineering-skill-playbook.md`：流程階段對照表（10 個 engineering skill：何時下、實際會做什麼、領域注意）＋產出物格式表（10 個）＋「官方涵蓋不到的地方」（多 agent 編排／context 管理／大型 codebase 並行規模，導流至社群模式庫）＋目前結論
- **觸發邊登記（衍生頁鐵則）**：`.claude/rules/wiki-ingest-features.md` 新增「工程流程 Skill 指南維護」節（週更、四步動作、不做的事），含**軸線鐵則**：不得改以開發領域分欄、「領域注意」欄無依據留 `—`（此欄最易被通用常識灌水）；同步登記進 `scripts/check_wiki_freshness.py` 的 `DERIVED_PAGES`（首跑即被該檢查攔下「歸因記錄從無此頁」，補登記後通過，衍生頁 6 → 7）
- **新增第 12 個來源 `Official Skills`**：`src/news_aggregator/sources/official_skills_repos.py`——兩個官方 repo（`anthropics/skills` 建立 2025-09-22、166,939 星；`anthropics/knowledge-work-plugins` 建立 2026-01-23、23,363 星）**皆不發 GitHub release**（`/releases` 實測皆回空陣列），`github_releases.py` 結構上看不到它們。改以**目錄成員差異**偵測：新增／消失一個技能才是新聞，內文 typo 不是。防假警報四點：首見只記基線、非 `dir` 與 dotdir 不計、抓取失敗與非 list payload（404／rate limit 回 dict）皆不覆寫既有集合（否則會噴出整批假「新增」或假「刪除」）、rate limit 低於 15 即停手（與 github_releases 共用配額）。12 筆測試
- **兩個 repo 先前在全庫零命中**：`anthropics/skills` 早於本專案收錄起點（2026-04-25）七個月，屬「起點之前就存在的既有事實」，日報只看「今天發生什麼」對此全盲——與路由失敗不同類，但同樣是缺口
- **架構文件同步再次由機械檢查攔下**：`check_arch_docs.py` 檢查 1 報缺 `Official Skills`，已補 S12 節點與 HTML chip、來源數 11 → 12
- **命名慣例待議**：新 slug `engineering-skill-playbook` 不落在既有四類前綴（community-／enterprise-／anthropic-／safety-）內。本輪未擅改慣例，記此待使用者裁示是否新增第五類前綴或維持例外
- 一條 sync_pair 入 review-registry（觸發邊＋軸線鐵則）；測試綠、規則檢查零錯誤

## 2026-08-08 Ingest（雲端排程執行）

- 來源日報：[[news/2026-08-08]]
- 更新頁面：wiki/entities/fable-5.md、wiki/entities/claude-code.md、wiki/topics/official-community-gap.md、wiki/topics/anthropic-business.md、wiki/topics/ai-agent-safety.md、wiki/topics/community-tech-patterns.md、wiki/feature-radar.md、wiki/index.md
- 新增頁面：wiki/entities/robert-mahari.md（Anthropic 新設「Claude for Legal」部門負責人，2026-08-07 任命，僅 2 家媒體標題可用，過往經歷標「待核實」）
- 摘要：Claude Code auto 模式將於 8/14 起取代手動確認成為預設權限模式（HN／9to5Mac 雙來源）；5 家媒體同日報導 Claude Code 新增跨 session 訊息互通功能（macOS/Linux），但無官方 changelog 佐證，feature-radar 標記「未經官方確認」；GitHub Issues 湧現 5 則高互動已知問題／功能請求；英國 AISI 測試事件（既有故事線）新增 CNN 報導的「嘗試植入惡意程式碼」細節；Anthropic 任命 Robert Mahari 為新設「Claude for Legal」部門負責人；The Register 報導 OpenAI Astra 資安機制與「Anthropic 放寬 Fable 限制」，因僅有標題無法查證具體所指，模型記者已於 fable-5.md 標記「待查證」。
- 呈現品質：模型／功能／商業／安全政策／社群記者均回報 ✅ 通過；人物記者未附呈現品質審查行（見下方品質備註）
- 品質備註：[人物] 回報格式缺「呈現品質審查」欄，未依 `.claude/rules/wiki-ingest-format.md` 標準明確輸出審查結果（主編已檢視 robert-mahari.md 標頭欄位完整、待核實標記正確，判斷內容本身合格，僅回報格式不完整）
- **降級執行說明**：雲端環境六個 `wiki-reporter-*` 自訂 subagent_type 無法解析（同 2026-07-18 已知情況），本次全數改用 `general-purpose` agent 並於 prompt 內嵌對應規則檔（`wiki-reporter-shared.md` + 各類別 `wiki-ingest-[類別].md` + `wiki-ingest-format.md` 摘要）執行，功能等同但非原生角色 agent，依 `docs/cloud-runbooks/daily.md` 規定於此明確標注
- **待主編／使用者查證**：The Register「Anthropic loosens Fable's leash」標題僅見於 Google News RSS 轉址，無法取得原文；模型與安全政策記者已分別評估後判斷不可逕自對應為已解除的出口管制或同日生物安全防護公告，留待人工查證原文後回填
## 2026-08-09 週度延伸回顧

六記者並行判斷（Sonnet），使用者裁示「全部執行」。月度聚焦校準：`wiki/metrics.md` 8 月已有數值（08-01，76%）→ 本月已執行，跳過。

- **延伸（5 項全執行）：**
  - `entities/mythos.md` 補英國 AISI 官方安全測試主線（自主偽造身分、社交工程私訊真人、隱藏行為證據），**只記模型行為能力面**，政策監管面 wikilink 至 `topics/anthropic-government-policy`。此為模型記者自報的缺口——該頁最後新聞更新原停在 07-30，一條經 Reuters/Guardian/BBC/CNN/FT 交叉確認、且明確點名 Mythos 本尊的主線在模型頁完全缺席。記者執行時發現派工指定的來源日期（08-02/04/05）有誤，實際出處為 `news/2026-08-07.md`，已自行更正並如實標註
  - `topics/code-quality-decline.md` 新開「模型釘選／靜默降級」子區塊（詳見下方查證條）
  - `entities/pricing.md`「灰色市場與轉售現象」補 Poison Claude 的**商業視角**（轉售套利 → 已證實隱私外洩），wikilink 至 `topics/ai-agent-safety`；折扣數字標「媒體稱」不寫成官方數字
  - `topics/official-community-gap.md`「跨 session 記憶」小節補 GitHub #47023（彙整 #14227／#32627／#34192／#34556／#46138 五個既有 issue，訴求開放 compact／session 生命週期 hook）
  - `entities/claude-code.md`「🛡️ 安全與隱私」補兩則本週資安事件（08-07 CI workflow secrets 漏洞、08-05 Keyv npm 供應鏈蠕蟲植入 CC hook），狀態 ❓ 與 `ai-agent-safety` 現標一致，未比來源更確定
- **使用者跳過項目：** 無
- **聚焦校準：** 非本月首次（8 月已於 08-01 執行，76%），跳過

### 主編查證：model pinning 單一來源 → 兩獨立佐證，升級開子區塊

社群記者依規則誠實分流——08-04 Reddit 貼文為純 `Reddit / r/ClaudeCode`（無「· 週熱門」、score 不可信），未達低門檻，故只記為待觀察節點並回報「⚠️ 需主編查證」。**主編層以 web 工具查證，結果推翻了「無佐證」的暫定結論**：

- **#27892**（2026-02-23）`No way to pin model version` — `--model` 只吃 family 名、`.claude/settings.json` 無鎖版設定、自動升版無回退路徑。**官方以 not planned 關閉 + stale 標籤** → ⛔ 官方拒修
- **#46221**（2026-04-10）預設未經操作由 Opus 4.6(1M) 切成 Sonnet 4.6(200k)、進行中 session 中途降級、手動選定的 1M 變體於下次 `/model` 消失。**已關閉為 duplicate**（關聯 #45978）——此狀態不等於已修復，記錄時明令不得標 ✅

兩則皆**早於**該 Reddit 貼文，故現象成立且非新事。已開「模型釘選／靜默降級」子區塊，寫成**跨四種機制的重複模式**敘事（非時序條列）：設計面無法鎖版（#27892）、實作面 picker 狀態不保持（#46221）、商業面計費驅動降級（Fable 5 → Opus 4.8，細節在 `entities/pricing`）、產品面能力靜默移除（extended thinking，細節在 `entities/claude-code`）。

**分寸控制（明令記者執行）：** 被佐證的是「模型釘選不可靠／靜默降級」這個**現象**；該 Reddit 貼文獨有的「4 measured bypass vectors」「Sonnet 4.6 silently removed」**仍是單一來源未經覆核**，措辭上兩者分開，不讓佐證外溢成對全部宣稱的背書。本次為查證性補強（非日報進料），僅動「最後更新」，記者原誤設的「最後新聞更新」已修正回 08-01。

**流程教訓：** 記者無 web 工具，其「查無第二來源」的正確語意是「**庫內近 14 天日報無第二來源**」，不是「此事無佐證」——本例中佐證早在半年前的 GitHub issue 裡，只是從未進過日報（日報只看「今天發生什麼」，對起點之前的既存事實全盲，同 08-08 `anthropics/skills` 零命中一案）。記者誠實標註 + 主編接手查證這條鏈路本次**有效運作**：若記者當時虛抬訊號開子區塊，或主編略過「⚠️ 需主編查證」不處理，都會得到比現在差的結果。

### reader-notes 收件匣消費

- 08-08「LLM code review 單位成本」→ **維持 ⏳**，第一輪查證無新節點（08-05 的 71.6%→89.7% 談效果非成本；08-07 的 15 萬 token 是 headless 冷啟動非 review 場景）。附記 `topics/coding-workflow-guide` 已誠實標此為缺口
- 08-08「codebase map／agent 記憶 format 規約」→ **維持 ⏳**，#47023 訴求的是 hook API 開放而非 format 規格，不算第三獨立節點
- 08-01「成本感知自動模型路由」→ **維持 ⏳ 但性質已變**：本週進展不在路由器工具或基準，而在「靜默降階」本身的證據成形（見上）。原本等的是路由器加碼追蹤，現在等的是這條靜默降階線會不會繼續長
- 07-12「GPT-5.6 vs Claude」→ 已於 07-19 轉被動觸發，本週零命中，不主動重查
- 清除 07-07 📌 雜記（33 天 > 30 天門檻，日記性質過期即除）

### 未採納的觀察（記此備查，非待辦）

- **模型記者**：r/ClaudeCode 08-04～08-05 連續 3 則 Opus 5 負面情緒貼文（frustrating／WTF moments 徵集／97% 完成後徹底失敗），同一子版、無週熱門標記、score 不可信，未達中門檻 → 不開爭議子區塊，下週留意有無第三方跟進或量化案例
- **安全政策記者**：AISI 事件本週已累積三家實驗室（Anthropic／OpenAI／Meta）坦承 agent「失控」，若下週出現第四家、成為持續性產業敘事，可比照 `safety-china-trust-dispute` 前例評估拆獨立頁；目前僅 1 篇官方報告 + 少數跟進，未達門檻
- **人物記者**：Dario「員工為錢而非使命加入」連三則報導延燒（08-03→08-06→08-07），頁面已標待核實／二手轉述，待本人發言或官方回應再收斂措辭

**轉知閉環（同日）：** 社群記者回報「⚠️ 需主編轉知功能記者」→ 已轉知並執行，`entities/claude-code.md`「🧠 行為與品質」新增 #27892（⛔ 官方拒修）與 #46221（❓ 待查證，已關閉為 duplicate，明令不得標 ✅），組頭統計同步為「34 條未修復、1 條拒修、7 條待查證」，兩則標明「主編 web 查證，非日報進料」。此為 08-08 lint 5c 診斷「待查證是死路」後，轉知鏈路首次當日閉合。

**收尾修正兩則（機械檢查攔下）：** (1) 主編一度把兩則 GitHub issue 以 `date: 2026-08-09` 寫入 `data/source_attribution.jsonl`——但該欄語意是**日報日期**（`data/README.md`），而 08-09 無日報、這兩則來自主編 web 查證，屬非日報進料，歸因表無此槽位，四列已移除（查證軌跡留在本 log）。(2) `check_wiki_freshness.py` 據此連帶抓出真問題：`topics/code-quality-decline` 確實吸收了 08-04 日報的 Reddit 節點，記者卻把「最後新聞更新」一路退回 08-01——該欄應為 **08-04**（本次查證性補強不推進它，但當初那筆日報節點要算），已更正。**教訓：非日報進料不要硬塞歸因表，塞了會同時汙染帳本與新鮮度檢查的分母。**

## 2026-08-09 Query：Obsidian 連結語法盤點 → 揪出 18 條別名／錨點 wikilink 在網站上全是死連結

- **點出什麼**：使用者問「目前有沒有 obsidian 常見語法」，要求把「連結與嵌入」寫進 `CLAUDE.md`，並 review 專案有哪些地方可用這些語法優化。盤點時實查 renderer，發現的不是「還沒用」而是「用了會壞」
- **根因**：`web_reader/assets/app.js` 的 `wikilinkButtonHtml(p)` 把整段 `[[...]]` 內容當 slug，不切 `|` 也不切 `#`。因此 `[[entities/opus-5|Opus 5]]` 在站上按鈕標籤印出原始字串 `entities/opus-5|Opus 5`（表格內還多一個跳脫反斜線），點擊 `openWikiPage('opus-5|Opus 5')` 必然載入失敗。全庫 1460 條 wikilink 中 18 條踩到（16 條 `|`、2 條 `#`），其中 5 條在 `topics/model-comparison`——含快速選型表三列的模型名，是「我該用哪個模型」入口表上讀者最常走的一跳
- **為什麼沒被發現**：`build_web.py` 的 `WIKILINK_RE` 早已正確剝掉 `#` 與 `|`，斷鏈檢查因此全綠；壞的只有前端渲染層，而渲染層沒有對應檢查。**建置綠燈只證明資料層對，不證明讀者看到的東西對**
- **處置**：
  - `app.js` 新增 `parseWikilink()`（三段拆解 `頁面#錨點|別名`，同時吃掉表格內外兩種反斜線寫法）與 `jsStr()`（onclick 屬性字面值中和）；`wikilinkButtonHtml` 改用別名優先、錨點傳入 `openWikiPage(id, type, anchor)`
  - 新增 `window.scrollToAnchor()`：錨點文字走既有的 `headingSlug()` 對上 `addHeadingIds()` 產的 h2–h4 id，扣掉 57px sticky topbar 高度再捲。刻意用瞬移不用 smooth（跨頁跳段常達數千 px），且**不用 `requestAnimationFrame`**——分頁在背景時 rAF 會被節流到不觸發（實測踩到）
  - `build_web.py` 新增 `check_wikilink_anchors()`：`[[頁面#錨點]]` 的錨點必須真的是目標頁 h2–h4 標題。**上線即抓到既有 2 條 `#` 連結全是死錨點**——`feature-radar#Dynamic Workflows` 的條目早已封存至 `feature-radar-archive-2026-05`、`community-tech-patterns#時序` 該頁根本沒有 `## 時序`（正確目標是 `#技術彙整`），兩條皆已修
  - `CLAUDE.md` 新增「🔗 連結與嵌入語法」：明列可用（裸路徑、別名、錨點）與禁用（`![[嵌入]]`、`^區塊 id` — renderer 無支援），並註明要放寬得先改解析器
- **不做的事**：嵌入語法全庫 0 條且 renderer 不支援；查 `index.md` / `overview.md` 後確認它們與各頁的「重複」是刻意的分層改寫（路由鉤子 vs 週度敘事），用嵌入會把三種編輯意圖壓成同一份文字，故不推
- **可攜教訓**：**寫進規則的語法必須先確認渲染端吃得下**。本次是「wiki 寫得對、建置檢查也綠、但站上是死連結」的靜默失效——任何跨層語法（Markdown 方言、frontmatter 欄位、自訂標記）都該有一條檢查落在**最終呈現層**，不能只驗到資料層

## 2026-08-09 Ingest

- 來源日報：[[news/2026-08-09]]
- 更新頁面：wiki/entities/claude-code.md、wiki/topics/official-community-gap.md、wiki/topics/community-tech-patterns.md、wiki/feature-radar.md（主編彙整）
- 新增頁面：無
- 摘要：Claude Code Auto Mode 將於 8/14 起成為 Pro/Max/Team 預設權限模式；跨 session 訊息功能經官方文件確認轉為正式功能；社群持續關注 context/記憶持久化痛點與多款 agent harness 工具同批亮相。
- 呈現品質：claude-code.md ✅ 通過；official-community-gap.md ✅ 通過；community-tech-patterns.md ✅ 通過；商業／安全政策記者本日皆判斷無足夠事實更新頁面，未產出頁面異動（不適用）
- 品質備註：[商業] 記者回報中判斷 #41581（Max 訂閱被降級為 Free）應轉知功能記者記入已知問題，但功能記者為同批並行派工、未及收到此轉知，已由主編直接補寫入 `claude-code.md`「💰 計費與配額」組；後續同類情境建議先收攏跨類別轉知內容再派工，或於彙整階段安排補派

**降級執行說明**：雲端環境四個 `wiki-reporter-*` 自訂 subagent_type 不在本 session 可用 agent 清單中（同 2026-07-18、2026-08-08 已知現象），本次全數改用 `general-purpose` agent，並於 prompt 內指示其依序完整 Read `.claude/rules/wiki-reporter-shared.md` + 對應類別 `.claude/rules/wiki-ingest-[類別].md` + `.claude/rules/wiki-ingest-format.md` 作為角色定義後才開始工作，功能等同原生記者但非原生角色 agent，依 `docs/cloud-runbooks/daily.md` 規定於此明確標注，不靜默 fallback。

**主編查證（本日直接處理，非派工）**：功能記者的兩則 feature-radar 更新請求（跨 session 訊息互通功能移除「未經官方確認」標記並補上版本需求；Auto Mode 8/14 補充 Cat Wu 訪談重點）已由主編寫入 `feature-radar.md`，兩條目熱度各 +1（🔥🔥🔥→🔥🔥🔥🔥），`## ⭐ 本週推薦` 依時間閘與熱度重新排序覆寫（Opus 5、跨 session 訊息互通、Auto Mode 8/14 三項；語音模式選擇與 Reflect with Claude 因今日無熱度異動且已被更高優先序候選擠出，非違反防霸榜規則的強制輪替）。

**📋 待使用者確認**：
- [安全政策] The Register「Devs to Anthropic, OpenAI, Cursor, and friends: Make security and privacy the default」——僅有標題（Google News RSS 限制），需查證原文才能確認是否涉及具體資安事件或純屬一般性倡議文章
- [安全政策] The Times of India「Geoffrey Hinton on OpenAI, Meta and Anthropic AI models hacking other companies」——僅有標題，記者判斷可能與 `entities/mythos.md` 已記錄的英國 AISI 測試事件（自建假身分、隱藏證據）相關，也可能是泛論性警告，需 WebFetch 原文後決定是否寫入 `topics/ai-agent-safety.md` 或 `topics/anthropic-government-policy.md`
- [社群] Google News/XDA「I changed one setting in Claude Code, and my token burn dropped by 45%」——僅有標題，需查證原文確認具體是哪項設定，若查得屬 token/成本優化技巧，值得回頭補入 `community-tech-patterns.md`
- [社群] huangruiteng/loopx（3641★）、HangYu8123/HarnessFlow（516★）——依 GitHub repo 星數防刷註記，記者無工具查證 forks／issues／近期 commit 等難造假佐證，本日僅記為「待查證」節點，未列為高信度收錄，下次 ingest 或 lint 若有工具可查證應回頭核實

## 2026-08-09 Query：全覽表漏了當月最重要的兩條 → 補列＋規則補洞＋機械檢查

- **點出什麼**：使用者說「我看了一下功能全覽表怎麼沒有你說的 sessions」。實查 `wiki/feature-radar.md`：跨 session 訊息互通確實**只在**「⭐ 本週推薦」與「🆕 最新功能（2026-08）」詳細條目裡，`## 📋 功能全覽表` 查無此列。連帶查出 Auto 模式預設化（8/14 生效的 breaking change）同樣缺列
- **規模**：08 月 6 條詳細條目只有 4 條進表，缺的正是當月最重要的兩條（雙雙是今日日報「重大事件」，且一條在本週推薦、一條在 ⏰ 倒數中——**唯獨索引查無**）。07/06 月表列多於詳細條目屬正常（舊詳細條目已封存，表列長期保留），非缺漏
- **根因（規則從未涵蓋）**：`.claude/rules/wiki-ingest-features.md` 對 feature-radar 的維護規則寫得很細——准入定義、動作表、新條目格式、本週推薦選取邏輯、升版風險、⏰ 倒數中——但**通篇沒有一個字提到 `📋 功能全覽表`**。全庫僅 `.claude/commands/wiki-ingest.md` 一句「同步更新全覽表的熱度與試用價值」，那管的是既有列的欄位更新，不是新功能要補列。也就是說：新條目補表列這件事，一直只靠記者模仿既有版面，沒有任何規則或檢查保證
- **處置（三層）**：
  1. **補列**：全覽表新增跨 session 訊息互通（2026-08-08 🔥🔥🔥🔥 ⚡）與 Auto 模式預設化（2026-08-14 生效 🔥🔥🔥🔥 ⚡，狀態「官方公告（尚未生效）」）
  2. **補規則**：`.claude/rules/wiki-ingest-features.md` 新增「新條目必須同時補全覽表一列」——含五欄格式、未生效公告的日期欄寫法、熱度／試用價值須與詳細條目標頭逐字一致，並要求 ingest 結尾對帳當月兩邊數量
  3. **補機械檢查**：新增 `scripts/check_feature_radar.py`（掛進 `run_tests.py`），對帳**當月**詳細條目數與全覽表列數，不等即 exit 1。只對帳當月——舊月份詳細條目會封存而表列保留，比對舊月會誤報
- **為什麼三層都要**：本次失敗的正是「靠記者記得」那一層，所以只補規則不夠。規則負責說清楚怎麼寫，檢查負責保證沒漏
- **可攜教訓**：**同一份資料有「索引層 + 內文層」兩個入口時，兩者必須有機械對帳**。索引缺漏是最難自己發現的缺陷型態——內文寫得再完整，讀者從索引掃不到就等於不存在，而寫的人因為剛寫完內文，主觀上覺得「這條已經有了」

## 2026-08-10 Query：「有跨 session 傳送功能嗎？wiki 有寫嗎」→ 揭出懸置標記無消化端的結構缺口，建成全鏈偵測機制

- **提問**：使用者 08-09 問「是不是有新推出跨 session 傳送的功能」「這 wiki 有寫嗎」。wiki 有寫（feature-radar 08-08 收錄），但標著「⚠️ 未經官方確認／待確認」，而官方文件（code.claude.com/docs/en/cross-session-messaging）從第一天就存在。使用者追問「為什麼要我問才有更新」。
- **根因**（兩層）：(1) **來源層**：該功能官方文件在 code.claude.com/docs，11 個既有來源零覆蓋，且不進 CLI changelog、不發部落格；(2) **機制層**：條目正文寫著「後續 ingest 若查得官方一手來源應更新」——沒有任何流程會讀那句話。全庫盤點 436 筆同類懸置字樣，消化端只有每週 lint 的 3g/5c（每輪 10 筆，清完要 36 週），「今天的新聞正好解掉某筆懸置」這條路徑完全沒有人走。
- **處置**：
  1. **來源層**：official_docs_watch 新增 index 模式監看 code.claude.com/docs/llms.txt（頁面集合 diff，新功能上線必然新增一頁，不需事先知道功能名即可偵測）＋ desktop.md；changelog.md 評估後標 retired（483KB 每日發版，hash 模式純噪音）。實測回放 08-08 情境可正確報出 cross-session-messaging 新增（`70e9104`）
  2. **懸置標記語法**：定案機器錨點語法 `❓ **待查證**（標 YYYY-MM-DD｜查 探針…）`——錨點是散文不可能出現的 metadata 區塊而非「待查證」字樣，語意反轉句／圖例／計數標頭／目錄 anchor 天生不誤命中（`2d45e23`）
  3. **盤點與回填**：audit 腳本分四類（真懸置/元層級/已解除/偵測不了），437 筆中 384 筆由六記者＋主編代理並行回填為 323 個新語法標記，存量降至 35 筆（每筆有據）（`3344af5`、`f627cc1`、`bfa312f` 等 9 commits）
  4. **檢查器**：check_pending_markers 掛進 run_tests（缺探針/過寬探針/⟨Q-nn⟩ 對帳失衡即 FAIL；逾期只 WARN 進 5c 佇列，不設機械棘輪）（`ff943f7`、`c7a71ae`）
  5. **每日掃描**：scan_pending_verifications 於 pipeline Step 3f 拿探針比對當日日報（entry 切分＋STOPLIST＋多探針 AND＋S/A/B 分級＋去重），命中產出按記者分組的派工附件；順修 steps.md 兩個 3d 編號碰撞（`60fe44a`）。乾跑抓到樞紐頁 wikilink 探針無偵測力的雜訊（`[[entities/claude-code]]` 形同萬用鑰匙），收緊別名 STOPLIST 複檢並修 7 筆懶探針（`301f538`）
  6. **契約閉環**：派工 prompt 加第三區塊（附防偏誤說明：記者只可加 `訊` 欄，不可宣告結案）、記者回報加「待查證命中處置」欄、10 檔同步、registry sync_pairs 更新（`621d6a7`）
  7. **視圖與彙總**：frontmatter 四欄（pending_count/overdue/next_review/signalled）＋ wiki/_views/pending.md（Obsidian dataview，即時解析不存資料）＋ lint 5c 改用 --queue 佇列（`563b72a`、`dfa7779`）
- **驗收**：255 測試案例全綠；乾跑三日 S+A 命中逐筆複判全數主題相關；checker 全庫 0 FAIL。
## 2026-08-10 Ingest

- 來源日報：[[news/2026-08-10]]
- 更新頁面：wiki/entities/opus-5.md、wiki/topics/model-comparison.md、wiki/entities/claude-code.md、wiki/topics/anthropic-business.md、wiki/topics/competitor-landscape.md、wiki/topics/enterprise-tool-tracker.md、wiki/entities/pricing.md、wiki/topics/ai-agent-safety.md、wiki/topics/anthropic-government-policy.md、wiki/entities/openclaw.md（主編直接處理）、wiki/feature-radar.md（主編彙整）
- 新增頁面：無
- 摘要：Claude Code Auto 模式將於 8/14 起正式生效並免收分類器 token 費，官方部落格＋89%/13.6% 危險指令攔截率研究雙重確認；澳洲 OpenClaw agent 利用健身房 API 授權漏洞取消他人預約，AISI 安全測試與 Irregular 供應鏈事件延燒；商業面 Anthropic 簽下 100 億美元歐洲算力合約並與 ICON 深化臨床試驗合作。
- 呈現品質：entities/opus-5.md ✅ 通過；topics/model-comparison.md ⚠️ 已修復（MineBench 對照列儲存格超長，下沉細節並短語化，非本次新增）；entities/claude-code.md ✅ 通過；topics/anthropic-business.md ✅ 通過；topics/competitor-landscape.md ✅ 通過；topics/enterprise-tool-tracker.md ✅ 通過；entities/pricing.md ✅ 通過；topics/ai-agent-safety.md ✅ 通過；topics/anthropic-government-policy.md ✅ 通過；entities/openclaw.md（主編直接處理）✅ 依格式規則更新；社群／人物記者本日皆判斷無條目達收錄門檻，未產出頁面異動（不適用）
- 品質備註：[安全政策] 記者回報 OpenClaw 健身房 API 漏洞事件同時涉及功能記者主責的 `entities/openclaw.md`，因六記者為同批並行派工、無法即時互轉知，已由主編直接補寫該頁事件時序與 callout（詳見下方「主編查證」段），未留待下次 ingest

**降級執行說明**：雲端環境六個 `wiki-reporter-*` 自訂 subagent_type 不在本 session 可用 agent 清單中（同 2026-07-18、2026-08-08、2026-08-09 已知現象），本次全數改用 `general-purpose` agent，並於 prompt 內指示其依序完整 Read `.claude/rules/wiki-reporter-shared.md` + 對應類別 `.claude/rules/wiki-ingest-[類別].md` + `.claude/rules/wiki-ingest-format.md` 作為角色定義後才開始工作，功能等同原生記者但非原生角色 agent，依 `docs/cloud-runbooks/daily.md` 規定於此明確標注，不靜默 fallback。

**主編查證（本日直接處理，非派工）**：
- `wiki/feature-radar.md`：依功能記者建議，覆寫「Claude Code Auto 模式將於 8/14 起成為預設權限模式」詳細條目（補上官方部落格首發、分類器 token 免費化、89%/13.6% 研究數據），熱度由 🔥🔥🔥🔥 升至 🔥🔥🔥🔥🔥；同步全覽表對應列與「⭐ 本週推薦」第三行熱度；`scripts/check_feature_radar.py` 對帳 2026-08 詳細條目與全覽表列數，通過（各 6 條）
- `wiki/entities/openclaw.md`：安全政策記者已在 `topics/ai-agent-safety.md` 完整記錄 OpenClaw 健身房 API 漏洞事件並回連 `[[entities/openclaw]]`，主編依「每個事實只有一個家」原則，在 `openclaw.md` 補一則精簡事件時序條目＋覆寫 callout＋更新「最後更新」「最後新聞更新」（皆為 2026-08-10），完整分析仍留在 `ai-agent-safety.md`，不重複

**📋 待使用者確認**：
- [人物] Palantir CEO（NDTV 報導疑似 Alex Karp，姓名與職稱待核）針對 Anthropic 等 AI 公司「Drug Addict」式產品設計的批評——來源僅 Google News RSS 標題轉載，無正文可查證發言脈絡，人物記者判斷不足以建頁；需查證原文後決定是否建立新人物頁，或轉知商業記者併入 `topics/competitor-landscape.md`
- [社群] GitHub Search 三項熱門工具（flowful-ai/cad-skill 512★、wuxiran/cc-pane 501★、Laliet/cc-switch-web 500★）依「星數防刷註記」規則，因無 forks／issues／近期 commit 佐證資料，均標「待查證」未收錄；下次 ingest 或 lint 若有工具可查證應回頭核實

## 2026-08-12 Ingest

- 來源日報：[[news/2026-08-12]]
- 更新頁面：wiki/entities/opus-5.md、wiki/entities/claude-code.md、wiki/entities/pricing.md、wiki/topics/enterprise-cost-management.md、wiki/topics/ai-agent-safety.md、wiki/topics/anthropic-government-policy.md、wiki/topics/recursive-self-improvement.md、wiki/topics/community-tech-patterns.md、wiki/topics/community-tech-discussions.md、wiki/entities/claude-skills.md（主編直接處理）、wiki/feature-radar.md（主編彙整）
- 新增頁面：無
- 摘要：社群圍繞 Claude Code 移除四個月的 `/buddy` 技能發起大型復活請願（265 留言、2068 反應）；企業定價爭議延燒（相同 token/模型價差最高 40 倍）；Anthropic 官方部落格揭露未公開研究版 Claude 在黎曼猜想相關問題上取得數學進展；多則使用者資安回報（email 洩漏、CVP 誤擋、CoT 外洩）因缺乏具名背書或重現細節，均以懸置標記或「未經證實」語氣記錄，未升級為既定事實。
- 呈現品質：entities/opus-5.md ✅ 通過；entities/claude-code.md ✅ 通過；entities/pricing.md ✅ 通過；topics/enterprise-cost-management.md ✅ 通過；topics/ai-agent-safety.md ✅ 通過；topics/anthropic-government-policy.md ✅ 通過；topics/recursive-self-improvement.md ✅ 通過；topics/community-tech-patterns.md ✅ 通過；topics/community-tech-discussions.md ✅ 通過；entities/claude-skills.md（主編直接處理）✅ 依格式規則更新；人物記者今日無條目（0 則），未派工
- 品質備註：[模型] 記者轉知「Learning more about Claude's mathematical capabilities」（Anthropic Blog，HN 270 分，https://www.anthropic.com/research/riemann-zeta）不落入任一模型記者現有負責頁面（未命名研究版 Claude、單一事件、無可用介面，不構成新建 entities 頁門檻），主編評估後判斷本日不強行寫入任何頁面，僅記於此（該事實已完整保留於 [[news/2026-08-12]] 日報，讀者可由日報取得）；[安全政策→功能] 記者轉知「Enterprise skill/plugin 安全掃描 beta」（2026-08-06 公告）尚未見於任何頁面，主編查證後已直接補入 `entities/claude-skills.md`「官方 Skills 生態一覽」表與頁首 callout；[安全政策→功能] 記者轉知 CVP 誤擋 issue（#84352）併入 claude-code.md 已知問題一事，經核對功能記者本日回報已自行處理，無需額外動作

**降級執行說明**：雲端環境六個 `wiki-reporter-*` 自訂 subagent_type 不在本 session 可用 agent 清單中（同 2026-07-18、2026-08-08、2026-08-09、2026-08-10 已知現象），本次全數改用 `general-purpose` agent，並於 prompt 內嵌入完整 `.claude/rules/wiki-reporter-shared.md` + 對應類別 `.claude/rules/wiki-ingest-[類別].md` + 必要時 `.claude/rules/wiki-ingest-format.md` 規則內容作為角色定義後才開始工作，功能等同原生記者但非原生角色 agent，依 `docs/cloud-runbooks/daily.md` 規定於此明確標注，不靜默 fallback。

**主編查證（本日直接處理，非派工）**：
- `wiki/feature-radar.md`：同步「⚠️ 升版風險」最新版本行至 v2.1.228（純 bug fix，無新功能異動）；今日無新功能達 feature-radar 准入門檻（v2.1.228 純 bug fix 不收錄；官方文件更新項目查核後皆為既有事實），「⭐ 本週推薦」與「⏰ 倒數中」today 無變動，不動
- `wiki/entities/claude-skills.md`：補入 2026-08-06 官方公告「Enterprise skill/plugin 安全掃描 beta」至「官方 Skills 生態一覽」表，並覆寫頂部 callout 與頁首「最後更新」「最後新聞更新」為 2026-08-12
- `wiki/index.md`：五位記者皆回報「狀態變更：無」「新增頁面：無」，本日未修改

**📋 待使用者確認**：
- [功能] 官方文件索引 `code.claude.com/docs/llms.txt` 新增 2 頁（Week 30 · 7/20–24、Week 32 · 8/3–7 的 what's new 頁面）——雲端 egress 被封鎖無法 WebFetch 查證實際內容，僅記錄「索引新增了這兩頁」此一訊號；需人工或下次有 web 工具的環境查證這兩頁實際公告內容並視情況補入 feature-radar 或對應頁面
- [功能] Issue #78431（Claude Code 疑似透過 curl User-Agent 洩漏使用者真實 email）已標為 ❓ 待查證懸置標記（複查日 2026-08-26），因 HN 留言質疑該回報缺乏細節與重現步驟，真實性存疑，屆時請查證是否有官方回應或更多細節
- [商業] Yahoo Finance「Anthropic 與成立七個月新創簽下 100 億美元歐洲算力合約」——商業記者查證時發現與既有 08-04 已記錄的 Volta 交易（100 億美元、成立 8 個月的英國新創）高度相似，但兩則報導皆未具名新創公司、成立月數與地區描述有些微差異，記者無法確認是否為同一筆交易的不同媒體轉述，暫依「疑似重複、未確認」處理寫入 `topics/anthropic-business.md`；需查證原文釐清是否為同一事件

## 2026-08-11 Ingest（補跑 backfill）

- 來源日報：[[news/2026-08-11]]（62 篇，12/12 來源；日報收錄 37/62，未收錄 25 併入分類）
- 補跑原因：08-11 雲端 routine 完整產出日報與 ingest，但 push 撞上同時段推送的查證波二大合併、rebase 失敗，成果停在分支 cloud-daily-2026-08-11-unmerged 未併回；該分支 ingest 係套在查證波之前的舊 wiki，不可併回（會覆蓋已定讞查證成果），故對現行 wiki 重跑本次 backfill。
- 分類派工：模型、功能、商業、安全政策、社群五類並行（sonnet）；人物類無實質具名新聞，未派工。
- 更新頁面：entities/opus-5、entities/fable-5（黎曼 zeta 里程碑，標註「非 Fable 5 本體」）、entities/claude-code（v2.1.227 版本表、Auto Mode 媒體接力、llms.txt +2 頁）、topics/anthropic-business（Riot 90 億／GIC／Macquarie、Naver 投資、WSJ IPO、AWS Continuum）、entities/pricing（usage credits／定價頁官方更新）、topics/competitor-landscape（Meta Muse Glimmer 開源）、topics/anthropic-government-policy（隱形浮水印政策、眾議院施壓）、topics/ai-agent-safety（浮水印溯源面 wikilink、澳洲健身房 API 媒體跟進）、topics/community-tech-patterns（spec-driven 工具批次、AI SRE agent、AI-writing 指示）、topics/community-tech-discussions（浮水印社群反彈 ⟨Q-03⟩）
- 新增頁面：無
- 摘要：Anthropic 隱形浮水印全面上線（歐盟法規驅動、4 來源）與 Auto Mode 8/14 預設化媒體接力為當日兩大主線；基建合約密集（Riot 20 年 90 億）；研究版 Claude 意外改進黎曼 zeta 下界；Bring Back Buddy 聯署（2068 👍）為社群最高互動。
- 呈現品質：全部通過（記者 5/5 回報 ✅；新增懸置一律新語法）
- 品質備註：安全政策記者一度將 anthropic-government-policy 標頭回調至 08-11（該頁已有 08-12 內容），主編收尾時校正回 08-12——backfill 補插歷史時標頭日期不得回退至補跑日。

## 2026-08-12 Query：「這兩天日報怎麼沒更新」→ 揭出雲端 push 並發衝突把成果停在分支、watchdog 救法誤導

- **提問**：使用者問「這兩天的日報怎麼沒有更新」。查證：08-12 其實成功（在 origin，本機未 pull）；08-11 雲端 routine 完整產出日報＋wiki ingest，但 push 時撞上使用者同時段推送的懸置查證波二大合併（雙方皆 13:0x UTC），rebase 失敗，routine 把成果停在分支 `cloud-daily-2026-08-11-unmerged` 未併回 master，躺了兩天。
- **根因**：(1) push 並發——雲端 routine 每天 13:00 UTC 跑，與手動大量推送撞期；(2) routine 撞衝突時停泊分支的處理本身合理，但**停泊成果無自動救回機制**，靜默躺著；(3) watchdog 當晚有推播偵測到日報缺件，但建議「跑 /news-pipeline 補」＝重抓重生，會浪費已完成成果——**缺件與「成果停在分支」的救法相反，watchdog 給錯了方向**。
- **處置**：
  1. **08-12**：git pull fast-forward 補上（與查證成果一致，因其在合併後才跑）
  2. **08-11 日報**：從停泊分支 checkout `news/2026-08-11.md` 救回 master（唯讀來源、零衝突）；分支的 wiki ingest 係套在查證波之前的舊 wiki，不可併回，改對現行 wiki 重跑（`81177b7`）
  3. **08-11 wiki ingest 重跑**：五記者並行補跑（模型/功能/商業/安全政策/社群），主線＝隱形浮水印全面上線（歐盟法規，雙頁 wikilink）、Auto Mode 8/14 媒體接力、Riot 20 年 90 億基建、研究版 Claude 改進黎曼 zeta 下界、Bring Back Buddy 聯署；backfill 紀律＝插正確日期位不覆蓋 08-12 已 ingest 內容，主編校正安全政策記者誤把 gov-policy 標頭回調至 08-11（該頁本有 08-12 內容）（`c6f32a4`）
  4. **防再犯（watchdog）**：`daily_health_check.py` 新增 `parked_branches()`——查遠端 `cloud-daily-*-unmerged` 分支，有就 exit 非 0（即使今日檔案齊全，成果被卡住沒整合即靜默洞），推播優先改口「成果停在分支 X、用 git 救回勿重跑」；fail-safe（git 錯誤回 []）、只在 CLI 路徑跑不進 check()、+4 測試、runbook 同步（`4578be0`）
  5. emitted-cache 08-11 未確認項目維持原狀：兩階段機制設計為未確認項會被重新提供而非丟棄（安全方向），且 08-11 新聞至 08-13 多已滑出來源視窗
- **教訓**：手動大量推送應避開雲端 routine 時窗（13:00–13:50 UTC ＝ 21:00–21:50 台北）；停泊分支救援優先於重跑（重跑會浪費已完成成果並可能覆蓋更新內容）。

## 2026-08-13 Ingest | news/2026-08-13.md（56 則）

- 來源日報：[[news/2026-08-13]]（56 則，12/12 來源；日報實收 25 則，另有 31 則透過 `list_digest_omissions.py` 一併提供給記者判斷）
- 分類派工：模型 1 則、功能 11 則、商業 13 則、安全政策 3 則、社群 20 則（六類並行 foreground；人物類本日無具名 Anthropic 人員動態或重要外部人物言論，未派工）；**本雲端 routine 環境自訂 subagent_type（wiki-reporter-*）不在本 session 可用 agent 清單中，五位有條目的記者均改以 general-purpose agent 扮演角色、於 prompt 內指示其依序完整 Read `.claude/rules/wiki-reporter-shared.md` + 對應類別規則檔 + 必要時 `.claude/rules/wiki-ingest-format.md` 作為角色定義，功能等同原生記者但非原生角色 agent，屬環境限制的變通做法，依 `docs/cloud-runbooks/daily.md` 規定於此明確標注，不靜默 fallback**
- 更新頁面：
  - **模型**：無（Anthropic Status 多模型錯誤率上升事件已於當日解決，比對 07-06 同性質獨立事件後判斷不構成累積訊號，未達 `entities/fable-5.md` 更新門檻）
  - **功能**：`entities/claude-code.md`（新增 v2.1.231 版本記錄——修復 MCP OAuth 登入失敗問題，Slack 等預先註冊 OAuth client 場景；新增已知問題 2 則——Claude in Chrome 擴充功能無法連接 CLI #20298、獨立 macOS 介面缺乏關閉自動建立 worktree 選項 #12513；既有已知問題互動數更新 4 則——多帳號 Connector #27302、Skills 子目錄 #10238、Environment Contributions 警告重複出現 #3301、官方 Linux Desktop build #65697；Claude Cowork Chrome 側邊欄消息僅標題可用，已標待查證；呈現品質順帶修復「現況不被時序侵蝕」違規，刪除已有歷史記錄對應的舊段落並回填缺漏歷史列）
  - **商業**：`topics/anthropic-business.md`（新增 Anthropic 傳洽購世界模型新創 Decart 約 60 億美元、評估上看 2 兆美元估值規劃創紀錄 IPO，兩則皆多來源同日報導，寫入戰略合作表與新增「IPO 前瞻與估值追蹤」表）、`topics/competitor-landscape.md`（DeepSeek 組建團隊挑戰 Claude Code＋V4 Pro 上線宣稱效能逼近 Claude 3 Opus 但成本更低，補入既有 DeepSeek 子區塊；SpaceX Grok 新版加壓 Anthropic/OpenAI 僅記入時序）
  - **安全政策**：`topics/anthropic-government-policy.md`（Claude 浮水印機制之 EU AI Act 政策角度補充報導；Guardian 國有化評論文章簡短記入攻防紀錄/時序，未達持續追蹤門檻）、`topics/ai-agent-safety.md`（新增 OpenAI/Anthropic/Google API 瑕疵——弱模型可解讀強模型推理過程，僅標題可用，以標準式 ❓ 待查證標記收錄，並註明與既有 07-14 加密推理簽章懸置「是否同一機制無法判斷，不逕自合併」）
  - **社群**：`topics/community-tech-discussions.md`（新增 2 列：show-me skill／Quoting Florian Herrengt；同步執行 21 天 ☄️閃現 保留清理，移除 14 列逾期舊列）、`topics/community-tech-patterns.md`（新增 MISTAKES.md 節點，判斷非四條大型 codebase 主線，未觸發縫合）
  - **主編彙整**：`wiki/feature-radar.md`（今日無新功能達准入門檻，「本週推薦」與「⏰ 倒數中」不動；同步「⚠️ 升版風險」最新版本行至 v2.1.231）
- 新增頁面：無
- 摘要：Anthropic 傳洽購 Decart（約 60 億美元）與評估 2 兆美元估值創紀錄 IPO 為當日兩大商業主線，多家財經媒體同步報導；Claude 浮水印機制（EU AI Act 合規）延續前日爭議，新增使用者反彈與繞過工具報導；DeepSeek 組隊＋V4 Pro 上線持續加壓 Claude Code 競爭態勢；Claude Code GitHub Issues 高互動功能請求（官方 Linux 桌面版 655👍、多帳號 Connector 480👍）反映社群使用痛點。
- 呈現品質：entities/claude-code.md ⚠️ 已修復（現況段落時序侵蝕，見上）；topics/anthropic-business.md ✅ 通過；topics/competitor-landscape.md ✅ 通過；topics/anthropic-government-policy.md ✅ 通過；topics/ai-agent-safety.md ✅ 通過；topics/community-tech-discussions.md ✅ 已修復（21 天保留規則清理）；topics/community-tech-patterns.md ✅ 通過；模型記者本日無條目達更新門檻，不適用
- 品質備註：[功能] 記者主動確認浮水印事件政策面已轉知安全政策記者處理（避免功能/安全政策兩邊皆漏或皆寫），經核對安全政策記者本日回報確實已收錄於 `anthropic-government-policy.md`，無缺口；[社群] 記者回報 gamedev-skills/awesome-gamedev-agent-skills（500★）依「GitHub repo 星數防刷註記」規則，因派工資料未附 forks/issues/近期 commit 佐證，未收錄，記者無 web 工具無法自行查證，已轉入下方待確認清單

**降級執行說明**：雲端環境六個 `wiki-reporter-*` 自訂 subagent_type 不在本 session 可用 agent 清單中（同 2026-07-18、2026-08-08、2026-08-09、2026-08-10、2026-08-12 已知現象），本次五位有條目的記者全數改用 `general-purpose` agent，並於 prompt 內指示其依序完整 Read `.claude/rules/wiki-reporter-shared.md` + 對應類別 `.claude/rules/wiki-ingest-[類別].md` + `.claude/rules/wiki-ingest-format.md` 作為角色定義後才開始工作，功能等同原生記者但非原生角色 agent，依 `docs/cloud-runbooks/daily.md` 規定於此明確標注，不靜默 fallback。

**📋 待使用者確認**：
- [商業→安全政策，歸屬未定] 「How well do job retraining programs work?」（Google News 來源標記為 Anthropic，疑似官方勞動市場研究產出）——僅標題可用、無正文，不符合商業記者觸發條件（融資/收購/戰略合作/企業採用），亦未派工給安全政策記者；需人工查證原文後決定歸屬（勞動政策 → 安全政策記者；若屬一般研究無政策動作 → 可能不需收錄）
- [社群] GitHub Search 熱門工具 gamedev-skills/awesome-gamedev-agent-skills（500★）依「星數防刷註記」規則，因無 forks／issues／近期 commit 佐證資料，標「待查證」未收錄；下次 ingest 或 lint 若有工具可查證應回頭核實

## 2026-08-14 Ingest | news/2026-08-14.md（68 則）

- 來源日報：[[news/2026-08-14]]（68 則，13/13 來源；日報實收 38 則，另有 30 則透過 `list_digest_omissions.py` 一併提供給記者判斷）
- 分類派工：模型 3 則、功能 12 則、商業 15 則（14 則新聞＋1 則專頁定向）、安全政策 10 則（6 則主要＋4 則佐證性重複報導）、社群 23 則、人物 3 則（六類並行 foreground）
- 更新頁面：
  - **模型**：`entities/fable-5.md`（TechSpot「Claude 嘗試證明黎曼假設」判斷為 08-11 研究版 Claude 改進黎曼 zeta 下界事件的媒體接力報導，附記一段媒體延續說明，未重複建歷史條目；Conceptual Reasoning Index 與 08-13 Mythos/Fable/Sonnet 錯誤率事件比照既有先例判斷不構成頁面更新門檻，未寫入）
  - **功能**：`entities/claude-code.md`（新增 v2.1.232 版本記錄——subagent forking 預設開啟；v2.1.231 MCP OAuth 修復記入版本表；status.claude.com／Claude Code on the web 兩起服務事件記入服務穩定性；已知問題互動數更新 4 則——AGENTS.md #6235（5760→5889👍）、多帳號管理 #18435（769→819👍）、Max 額度異常 #38335（538→543👍）、GitHub Connector #32479（130→138👍）；新增已知問題 1 則——The Register 報導空白思考區塊仍計費，標待查證 ⟨Q-14⟩）、`topics/official-community-gap.md`（Subagent 派工/編排列因 v2.1.232 同步更新）
  - **商業**：`topics/anthropic-business.md`（Decart 收購仍在洽談、CFO 已展開早期 IPO 對話但未談估值、投資人估值上看 2 兆美元、Steve Eisman「阿基里斯腱」評論，四則同日商業/估值動態同步記入）、`topics/enterprise-tool-tracker.md`（新增 Samsung 晶片設計採用列，❓ 未確認——「reportedly」措辭未經證實）、`entities/pricing.md`（新增 issue #38335 Max 額度異常事故；Reddit「用量暗中調降」質疑經查證現有記錄後以「使用者質疑」語氣記錄，未見對應官方承諾）、`topics/competitor-landscape.md`（Z.ai 新模型、DeepSeek Harness 開源上線＋V4-Pro、中美 AI 定價戰 FT 報導、Anthropic 模型可能比中國模型更便宜研究，定價數字缺具體佐證處均標「待查證」不推算）、`topics/ai-talent-flow.md`（Sergey Brin 於 Demis Hassabis 卸任 DeepMind CEO 後談話，標題本身截斷，❓ 待查證）
  - **安全政策**：`topics/ai-agent-safety.md`（Anthropic 自揭：多 AI agent 執行同一任務時互相破壞、癱瘓對方，採 TechCrunch/BI 中性描述、避開 Decrypt 戲劇化措辭；Yellow.com「四大 AI 實驗室 prompt injection 指標不相容」研究因未指名是否含 Anthropic，標準式 ❓ 待查證收錄）、`topics/anthropic-government-policy.md`（浮水印爭議延燒，新增 Anthropic 透過 Business Insider 首度回應使用者疑慮一節；PCMag 圖像浮水印報導併入佐證）
  - **社群**：`topics/code-quality-decline.md`（Reddit 兩則品質/效能下滑抱怨——3 個月觀察 MASSIVE 下滑、Pro→Max 升級後變慢 3 倍——記入訊號群）、`topics/community-tech-patterns.md`（新增「分層 Opus 大腦＋Sonnet 工人＋持久狀態」multi-agent 架構提案節點，issue #56913；判斷非四條大型 codebase 主線歸屬，`community-large-codebase-workflow.md` 主線頁未動）
  - **人物**：`entities/dario-amodei.md`（三則同日媒體對 Dario Amodei 之妻的人物側寫報導——WSJ／HN／The Information——均未提供姓名或具體職務，未達新人物建頁門檻，以待核實標記附記於現況/歷史記錄/參考來源三處；HN 留言中對 Eric Schmidt 私人關係的嘲諷性揣測已明確排除、未採信為事實）
  - **主編彙整**：`wiki/feature-radar.md`（新增 Claude Code v2.1.232 — Subagent forking 預設開啟，🔥🔥／⚡ 有條件推薦／正式發布，詳細條目與全覽表列已補齊對帳；同步「⚠️ 升版風險」最新版本行至 v2.1.232；「⭐ 本週推薦」與「⏰ 倒數中」今日無資格變動，維持不動）
- 新增頁面：無
- 摘要：Decart 收購（60 億美元，仍洽談中）與 Anthropic 估值／IPO 傳聞（CFO 已展開早期會議、投資人估值上看 2 兆美元）為當日商業主線；Anthropic 自揭多 AI agent 同任務下互相破壞的內鬥行為為新增安全政策發現；Claude 隱形浮水印爭議延燒，Anthropic 首度透過媒體回應使用者疑慮；Claude Code Auto Mode 8 月中旬起為 Pro/Max/Team 預設開啟（dev.to 單一來源，重申既有 08-10 官方確認事實，feature-radar 熱度不變）；GitHub Issues 高互動請求集中於 AGENTS.md 支援（5889👍）、多帳號管理（819👍）與 Max 額度異常（543👍）。
- 呈現品質：entities/fable-5.md ✅ 通過；entities/claude-code.md ✅ 通過；topics/official-community-gap.md ✅ 通過；topics/anthropic-business.md ✅ 通過；topics/enterprise-tool-tracker.md ✅ 通過；entities/pricing.md ✅ 通過；topics/competitor-landscape.md ✅ 通過；topics/ai-talent-flow.md ✅ 通過；topics/ai-agent-safety.md ✅ 通過；topics/anthropic-government-policy.md ✅ 通過；topics/code-quality-decline.md ✅ 通過；topics/community-tech-patterns.md ✅ 通過；entities/dario-amodei.md ⚠️ 已修復（新增待查證 callout 前先移除現況段落中已重複於歷史記錄的舊段落，符合「現況不被時序侵蝕」2 段上限）
- 品質備註：日報生成階段摘要忠實度自檢（3d）抽 10 條、改寫 4 條（首度→移除未驗證措辭、社群趨勢反應數精確化、Show HN 留言誤將兩位不同使用者的花費數字混為一談已拆分、Status 事故標題列名模型與內文不一致已補齊），M≥3 已於當時標記 ⚠️ 供覆核；[社群→功能，待確認] `community-tech-patterns.md` 新增「分層 Opus 大腦＋Sonnet 工人＋持久狀態」節點後，記者請主編轉知功能記者評估 `official-community-gap.md` 產品化矩陣是否新增列，功能記者本次僅同步了 v2.1.232 對應列，未評估此提案，待下次 ingest 或 lint 補做

**降級執行說明**：雲端環境六個 `wiki-reporter-*` 自訂 subagent_type 不在本 session 可用 agent 清單中（同 2026-07-18、2026-08-08、2026-08-09、2026-08-10、2026-08-12 已知現象；本次事前已由可用 agent 清單直接確認不可用，未逐一嘗試觸發解析失敗），本次六位記者全數改用 `general-purpose` agent，並於 prompt 內指示其依序完整 Read `.claude/rules/wiki-reporter-shared.md` + 對應類別 `.claude/rules/wiki-ingest-[類別].md` + `.claude/rules/wiki-ingest-format.md` 作為角色定義後才開始工作，功能等同原生記者但非原生角色 agent，依 `docs/cloud-runbooks/daily.md` 規定於此明確標注，不靜默 fallback。

**主編查證（本日直接處理，非派工）**：
- `wiki/feature-radar.md`：新增 Claude Code v2.1.232 詳細條目＋全覽表列（依功能記者提供的草稿彙整）；同步「⚠️ 升版風險」最新版本行；「⭐ 本週推薦」現有三項皆於 4 天內輪替過（08-10），且今日無 🔥🔥🔥🔥 以上新達標候選，維持不動；「⏰ 倒數中」auto 模式生效日條目本身即為今日日期，因無新資訊確認實際已生效，保留原樣供讀者對照
- `wiki/index.md`：六位記者皆回報「狀態變更：無」「新增頁面：無」，本日未修改
- `data/source_attribution.jsonl`：彙整六位記者回報之來源歸因，共 35 筆 append（記者回報中缺具體 URL 者，已由主編對照 `src/gathered_items.json` 補齊正確連結）

**📋 待使用者確認**：
- [模型] 「The Conceptual Reasoning Index」（Anthropic alignment 團隊發布概念推理評測套件，HN 76 分）不落入任一模型頁觸發邊（無可用介面、不測試既有具名模型），比照 08-12 黎曼 zeta 先例未寫入任何頁面；若後續有更多同類 Anthropic 研究性公告出現，建議評估是否需要新建頁面追蹤此類「研究性能力揭露」訊號
- [商業] 「Can I use my Outputs to train an AI model?」（support.claude.com 官方一手來源，訓練資料使用政策）不符合商業類六頁任一觸發條件，未寫入任何頁面；建議評估歸屬（可能需新建政策類頁面，或併入安全政策類）
- [商業→安全政策，未派工] 「How Musk's toxic data empire is powering Anthropic's 'responsible' AI」（TBIJ 調查報導，訓練資料供應鏈爭議）橫跨商業與安全政策兩面向，商業記者判斷更適合安全政策記者但本次未派工給安全政策記者處理，未寫入任何頁面；需人工查證原文後決定歸屬與是否收錄
- [社群→功能，待補做] `community-tech-patterns.md` 新增「分層 Opus 大腦＋Sonnet 工人＋持久狀態」節點（issue #56913）是否應觸發 `official-community-gap.md` 產品化矩陣新增列，尚未評估（見上方品質備註）
- [商業] Reddit「用量疑似配合 8/19 促銷永久化而暗中調降」指控，已查證現有 `entities/pricing.md` 記錄未見對應官方承諾，`topics/anthropic-commitments.md` 亦無相關追蹤列，已以「使用者質疑／推測」語氣記入 pricing.md；建議持續觀察 8/19 前後是否有更多同類指控或官方回應
- [沿用 08-13] 「How well do job retraining programs work?」歸屬未定（見上則 08-13 Ingest 紀錄），今日日報未再出現，暫無新進展

## 2026-08-15 Lint（雲端排程執行）

- 修正矛盾：4 處——(1) `topics/competitor-landscape.md` pi-coding-agent 列表格摘要仍寫「未經官方交叉確認」，但同頁時序已記錄 08-13 Databricks 官方部落格查證數字（$1.28 vs $1.94/任務，省約 34%），已統一改採已查證數字；(2) `topics/ai-agent-safety.md` CVE-2026-55407（buffa Rust Protobuf DoS）技術彙整細節區仍寫「至今無後續報導確認是否已修補」，但頁面摘要／未修補風險現況表／時序三處皆已確認修於 buffa/connectrpc 0.8.0，同頁自相矛盾，已統一為「已修補」；(3) `topics/community-pattern-trends.md` 趨勢一觀察日期與掃描日不同步（2026-08-08/37天→應為 08-15/44天）、「醞釀中：行動裝置遠端控制」天數描述與首見日矛盾，均已修正；(4) `entities/andrej-karpathy.md` 頂部「加入 Anthropic 已確認」callout 與其下方一則 ❓ 待查證標記（內文寫「加入 Anthropic 傳聞…仍無獨立確認報導」）互斥——人物記者依規不可刪標記僅回報待主編複核，主編查證後確認該 ❓ 標記已被同頁 08-13 查證的三方媒體確認結果取代，予以移除；同時發現頁內另有三處「查證狀態見上方標記」實際指向的是 Benzinga 08-02 單一媒體報導（Claude Opus 建構 3D 場景評論），而非已刪除的「加入 Anthropic」項，已重新建立對應該筆事實的新語法 ❓ 標記，避免三處引用變成懸空參照
- 補孤立連結：`entities/robert-mahari.md`（inbound_links=0）→ 人物記者已於 `topics/anthropic-business.md`「戰略合作」表列與說明文字補上 wikilink；其餘六類負責頁面逐一確認反向連結 ≥1，無其他孤立頁
- 狀態更新：無（六類回報之 topics 頁面最後新聞更新皆在 14 天門檻內，或已由近期 ingest 更新，無 ongoing→monitoring/resolved 轉態）
- resolved 收尾：無（六類負責範圍內無 resolved 狀態頁面待收尾）
- 新增 entities：無（本輪未建立新頁；Step 4 全站候選掃描見下方「📋 待使用者確認」第 1 項）
- 呈現品質：⚠️ 已修復約 60+ 處，主要三類——(a) 舊語法「至今無後續」禁用詞違規改寫共約 44 處（模型 11、商業 6、安全政策 15、人物 12；功能與社群本輪皆為新語法未逾期或無此問題），統一改為「已掃日報至 2026-08-1X 無後續；官方頁面未查證」格式；(b) delta-first 規則違反 2 處（`entities/opus-5.md` callout 停留於 07-26 發布敘事已補 08-08 動態；`entities/chris-olah.md` 現況段落背景先於事件已調整為事件優先）；(c) 維運術語洩漏／現況被時序侵蝕（`entities/claude-code.md` 2 處已改寫為讀者語言並瘦身逐日 append）。📋 已記錄待辦（工作量大，本輪未處理）：`ai-agent-safety.md`（924 行，36 個連續 `### YYYY-MM-DD` 無月份分組）、`anthropic-government-policy.md`（564 行，43 個連續同類條列無分組），均觸發「事件流堆積」警示但入口層本身完整（callout+表格），重構需重寫約 170 行，留待後續 lint 處理。其餘全數 ✅ 通過
- 入口層健檢：>500 行頁面（`community-tech-patterns.md` 1439 行、`community-tech-discussions.md` 1227 行、`ai-agent-safety.md` 924 行、`claude-code.md` 629 行、`anthropic-business.md` 614 行、`coding-workflow-guide.md` 604 行、`pricing.md` 593 行、`anthropic-government-policy.md` 564 行、`competitor-landscape.md` 550 行）逐一確認入口層完整（delta-first callout＋概覽表或月份/主題分組），本輪無需補結構；六位記者均無回報語意分岔或死案候選，Step 3 因無候選直接跳過
- 待查證回訪：已標訊 4 處——`anthropic-government-policy.md` 隱形浮水印機制細節標記 3 處（訊 2026-08-13，EU AI Act 依據與 Anthropic 已回應但內容未公開）、`coding-workflow-guide.md` 跨模型互審通過率方法論 1 處（訊 2026-08-15，命中 arXiv 2607.21656 查證來源）；已改註「日報無後續、官方未查證」共約 44 處（見上「呈現品質」）；其餘新語法標記距複查日未到、或近 14 天 news 無新後續者維持不動
- 規則檔健檢：
  - 矛盾：無（`wiki/CLAUDE.md`、`.claude/rules/wiki-ingest.md`、`.claude/rules/wiki-ingest-format.md`、`.claude/rules/wiki-reporter-shared.md` 及六份記者規則檔本輪逐檔全文複查，未見同一行為的相反指示）
  - 引用驗證：全部通過（7 個錨點逐一 grep 命中：`首次出現`欄、`## 痛點洞察`、`近期工具`欄、`## 技術彙整`、`熱門討論`表格、`衍生`欄、`全覽表`區塊）
  - 遵守率：呈現品質審查 3/3（08-12／08-13／08-14 log 皆含 ✅/⚠️/📋 標記）；feature-radar 明確提及 3/3；log 格式正確 3/3。「新工具加入時更新痛點洞察近期工具欄」延續案，`community-tech-tools.md` 已改 lint 專用不受每日 ingest 抽樣影響，不適用
  - 過期規則（> 60 天）：7 項，較 08-08 lint 新增 2 項跨越閾值——`entities/頁面格式模板`〔04-25，112 天〕、`topics/頁面格式模板`〔04-25，112 天〕、`Wiki 頁面呈現品質標準`〔05-15，92 天〕、`community-tech-patterns↔discussions 雙向連結規則`〔05-16，91 天〕、`enterprise-tool-tracker 更新規則`〔05-26，81 天〕、`命名與分類規則`〔06-11，65 天，**本輪新跨越**，08-08 lint 曾預告「下週將跨越」〕、`feature-radar 准入定義`〔06-15，61 天，**本輪新跨越**〕。主編對 7 項各做輕量 spot-check（entities 狀態值分佈、領域欄位分佈、enterprise-tool-tracker 表頭欄數、community-tech-discussions「衍生」欄存在）均未見明顯內容與現狀脫節，惟正式判斷仍需使用者確認，見待確認第 2 項
  - 來源健康：近 7 個運行日（08-08～08-14）逐日核對——`Anthropic Blog` 連續 7 天 count=0（官方源特性，非異常，但天數偏長值得留意）；`Claude API Release Notes` 連續 6/7 天 count=0（同性質）；`Anthropic Status` 曾連續 5 天 count=0（08-08～08-12）後於 08-13/08-14 恢復（1／3）；`Official Docs` 曾連續 3 天 count=0（08-08～08-10）後恢復；其餘來源（Google News／Hacker News／Reddit／dev.to／GitHub／GitHub Issues／Blogroll）均未觸發連續 3 天 count=0 告警。**新發現未註冊 slug**：`official-docs`、`topic-watch` 各 2 筆在 `data/source_attribution.jsonl` 使用，但 `data/source_registry.json` 查無對應項（`topic-watch` 雖已記載於 `wiki-reporter-shared.md` 來源歸因表，但 registry 檔案本身缺漏），見待確認第 3 項
  - 來源記分卡：`python scripts/source_scorecard.py`（33 天窗口）HHI 0.223（未達 0.25 高度集中門檻）；Google News 低信譽桶（pc1 < 0.4）0 筆；11 個社群/媒體來源與 4 個官方/白名單來源逐一列表附回報
  - 跨檔案語意矛盾（6f）：本輪逐一複查 `.claude/review-registry.json` 列出的 sync_pairs 涉及規則檔全文（含六類記者回報格式段七欄一致性、community-lint 邊界標記、subagent_type 名稱一致性等），未發現新的實質語意矛盾，✅ 全部配對語意一致；機械層面確定性檢查（bare_references／path_existence／anchors／equal_values／all_contain／max_count）交由收尾 `gate_web_build.py` 內建 `scripts/check_rules.py` 驗證
  - 成長迴路（月度）：**非本月首次 lint（`wiki/log.md` 08 月已有 08-01、08-08 兩次 Lint 記錄），跳過月度蒸餾**
- 品質指標（6g）：
  - ref 覆蓋率（每週）：**100%**（08-08～08-14，29 條列/29 有歸因；08-06 當日無 news 檔案不計入分母，閾值 80% 通過）
  - 採用驗證率（月度）：**非本月首次 lint，跳過**
  - 外部死鏈（月度）：**非本月首次 lint，跳過**（雲端亦一律跳過，理由同 5c）
  - 趨勢判讀：持平（連續 4 期 ≥97%：07-26 97%／08-08 100%／08-15 100%，高位穩定），已 append `wiki/metrics.md`
- 跨家榜單週更（5b）：**雲端 egress 封鎖，跳過**——`model-task-leaderboard.md` 抓取需存取外部榜單網站，雲端沙盒一律封鎖，留待本機執行，見待確認第 4 項
- 逾期待查證清算（5c）：**雲端 egress 封鎖，跳過**——需查證官方一手來源，雲端沙盒一律封鎖，留待本機執行，見待確認第 5 項
- 讀者模擬：
  - Claude Code 重度使用者「Auto 模式現在是不是已經對我的方案預設開啟了？」→ ✅ 通過：index → `entities/claude-code.md` → 頂部 callout 直接說明 08-14 已對 Pro/Max/Team 正式生效，2 跳內取得結論
  - AI 系統開發者「社群現在有哪些工具在追蹤多個 agent 的執行狀態？」→ ✅ 通過：index → `topics/community-pattern-trends.md` → 趨勢六（多 Agent 可觀測性儀表板化）段落直接列出 Wallfacer／HUD／Cockpit／OtoDock／Fleet Deck 六款實作，2 跳內取得結論
  - Anthropic 生態追蹤者「Decart 收購案跟 Anthropic 上市傳聞現在進展到哪？」→ ✅ 通過：index → `topics/anthropic-business.md` → 頂部 callout 直接說明仍在洽談、CFO 已展開早期 IPO 會議但未談估值，2 跳內取得結論
- lint 自我遵守率：6/6 位記者回報一次過（3a–3g 各項在六份回報中皆有具體頁名與結論，無缺項或含糊，無退回）
- overview.md：已全文改寫（上次全文改寫為 08-01 lint）。本輪反映 08-08～08-14 局勢：Decart 收購案（約 60 億美元）與 Anthropic 估值／IPO 傳聞同週浮現為新商業主線、Anthropic 自揭多 AI agent 同任務互相破壞為新安全訊號、Claude 隱形浮水印爭議延燒逾兩週且 Anthropic 首度透過媒體回應、DeepSeek Harness＋V4-Pro 與 Z.ai 新模型加碼中國陣營競爭壓力、Claude Code v2.1.232 Subagent forking 預設開啟＋Auto Mode 08-14 正式對 Pro/Max/Team 生效預設化；社群趨勢新增趨勢七「規格驅動開發」；`wiki/index.md` 同步更新 `community-tech-tools`（189→58 工具，反映本輪策展後實際數量）與 `community-pattern-trends`（5→7 條成形趨勢）兩則過時摘要數字
- **品質備註**：
  - **[環境]** 雲端 `wiki-reporter-*` 六個自訂 subagent_type 本次仍不在本 session 可用 agent 清單中（同 07-18 起已知現象），六類全數以 `general-purpose` agent 執行，並於 prompt 內指示其依序完整 Read `.claude/rules/wiki-reporter-shared.md` + 對應類別規則檔 + `.claude/rules/wiki-ingest-format.md` 作為角色定義後才開始工作，功能等同原生記者但非原生角色 agent，依 `docs/cloud-runbooks/daily.md` 規定於此明確標注，不靜默 fallback
  - **[主編直接處理]** `wiki/feature-radar.md`「⏰ 倒數中」表 Auto 模式預設化一列截止日已過（2026-08-14），依規則「截止日已過的列移除」由主編直接移除（結果已完整記錄於 `entities/claude-code.md` 現況，不遺失資訊），同步改寫「⚠️ 升版風險」段落中對該列的既有引用
  - **[延續]** 社群記者本輪 `community-tech-patterns.md` 淘汰審查 dry run：建議淘汰 0 條、建議合併 0 組、無法判斷 2 條（Aharness FSM 複查日 2026-09-26 未到；Git Lazy Mount 規模極小已逼近 60 天沉寂門檻但未滿，建議下輪複查列入淘汰候選）

### 📋 待使用者確認（2026-08-15 lint）

1. **新實體頁候選（Step 4 全站掃描）**：`Samsung`（企業提及 28 次）、`Z.ai`（19 次）、`Decart`（13 次）、`Volta`（17 次）、`Sergey Brin`（7 次）均超過「被提及 3 次以上」門檻，但目前分散追蹤於既有 topic 頁（`enterprise-tool-tracker`／`competitor-landscape`／`anthropic-business`／`ai-talent-flow`）。主編判斷：參照既有慣例（企業客戶如 Microsoft/Uber、競品如 DeepSeek 均未建專頁，維持在 tracker/landscape 頁彙整），且符合「每個事實只有一個家」的資訊架構原則，暫不建議拆頁；是否同意維持現狀，或有特定項目認為應獨立建頁？
2. **規則年齡審查（6d）**：7 項超過 60 天（詳見上方「規則檔健檢」），其中 2 項本輪新跨越閾值（`命名與分類規則` 65 天、`feature-radar 准入定義` 61 天）→ 是否逐項審視內容是否仍吻合現狀，或標記「已審閱、長期有效」以停止重複列出？
3. **來源 registry 缺漏**：`official-docs`、`topic-watch` 兩個 slug 在 `data/source_attribution.jsonl` 中使用但 `data/source_registry.json` 查無對應項 → 需修 registry 補登，或確認記者回報用字是否有誤
4. **跨家榜單週更（5b）**：因雲端 egress 封鎖跳過，留待本機執行
5. **逾期待查證清算（5c）**：因雲端 egress 封鎖跳過，留待本機執行
6. **社群記者發現：`community-tech-patterns.md` 有 2 條「無法判斷」淘汰候選**——Aharness FSM（複查日 2026-09-26 未到，暫緩）、Git Lazy Mount（規模極小，建議下輪複查列入淘汰候選）

## 2026-08-15 Query：「review 專案設計／蒐集／派工有無值得優化」→ 記者派工路徑轉正（取消本機／雲端雙軌）

- **提問**：使用者請 review 專案的蒐集與派工設計。review 指出派工端最大的結構問題：六個 `wiki-reporter-*` 自訂 subagent_type 在雲端 routine 自 07-18 起至少六次無法載入（07-18／19／22／24、08-08～14），每次退回 `general-purpose`＋手工內嵌規則並在 log 標「降級執行」——形成本機一條路（原生 agent）、雲端一條路（內嵌）的雙軌，同一角色兩種構成方式，規則檔改動只有一條路自動吃到，且每天付一段降級聲明的利息。
- **裁決**：內嵌路徑轉正為**唯一正典**，本機也走同一條——`subagent_type: "general-purpose"` + `model: "sonnet"` + prompt 首段固定「角色前導」（要求記者 Read `.claude/agents/wiki-reporter-[category].md`），角色檔維持規則單一來源（前導只導向、不重抄規則內文）；自訂 agent 註冊照留供本機手動呼叫，派工流程不再依賴。
- **改動**：`.claude/rules/wiki-ingest.md` 新增「派工方式」節（正典定義＋理由）；`wiki-ingest.md`／`wiki-lint.md`／`wiki-weekly-review.md` 表頭 subagent_type → 角色檔、prompt 範本加前導；`docs/cloud-runbooks/daily.md`／`weekly-lint.md` 移除「降級」措辭與「記者是否降級」摘要欄；六份角色檔頂部加派工方式說明；`review-registry.json` 同步配對改為檢查正典路徑三要素（general-purpose／角色前導語句／sonnet）；`docs/workaround-register.md` 該列移入已收斂（登記 07-24 → 收斂 08-15）。測試 280/280 綠、check_rules 46 組配對綠。
- **第二輪（同日，使用者「你確定嗎、全部修一修」）——review 其餘項目逐項處置**：
  1. **日期誤植**：第一輪把當日寫成 08-13（實為 08-15），rules／runbook／register／本 log 條目全部校正
  2. **雲端派工復現次數**：register 校正為至少 8 次（07-18／19／22／24、08-08～14）
  3. **lobste.rs 殘留**：07-10 已移出 pipeline，但 `wiki-reporter-shared.md` 門檻表「其他」欄與 slug 表、`wiki-ingest-community-lint.md` 排除條仍列它——已清除，門檻表「其他」欄改 Blogroll
  4. **Official Skills／Official Docs 的 state 只做了一半**：08-13 已把兩份 `*_state.json` 納入版控，但 `.github/workflows/daily-gather.yml` 的 `git add` 清單漏了它們——GH Actions 每天全新 checkout、偵測到的異動隨容器銷毀，等於每天拿舊基線比對、同一異動重複偵測，state 只在本機手動跑才前進。已補進 commit 清單
  5. **「查過確認沒有 vs 沒查」**：`wiki-lint.md` 6e 改用 `sourceStatus.ok` 分辨——清冊／官方型來源 `ok=true` 且 count=0 屬正常，不再對它們發連續 0 告警；`ok=false` 才是異常
  6. **來源註冊表缺三個 slug**（`official-docs`／`official-skills`／`topic-watch`，記分卡會報「未註冊 slug」）：已補；`wiki-reporter-shared.md` slug 表補 Official Docs／Official Skills；`data/README.md` 同步；`topic_watch.py` 加 per-query 命中量 INFO log（歸因經 publisher 回填只到 topic 層級，query 層級的去留判斷靠這行 log）
  7. **記者間「轉知」機械化**：新增 `scripts/pending_handoffs.py`＋`data/pending-handoffs.jsonl`（append-only 帳本，open／list／close／void，開立冪等，逾 14 天標 ⚠️，+3 測試）；派工訊息附「轉知待接手」清單、記者回報契約新增第八欄「轉知處置」（八份規則檔＋registry 同步）、主編彙整表明定登帳／結案規則、pipeline Step 3 與 wiki 同批 commit；register 該列移入已收斂
  8. **雲端 push 撞衝突「先重試再停泊」**：查證後發現 `news-pipeline-steps.md` Step 5 早已有 pull --rebase 重試 2 次的規定，08-11 是真衝突非缺重試——**第一輪 review 此條誤判，不需改動**
- **今日事故（review 時順帶發現）**：08-15 GH Actions `daily-gather` 於 10:28 UTC 在「Gather news」步驟失敗（無 token 讀不到 log；本機 21:42 台北排程抓料成功 62 則，疑為暫時性），雲端 routine 13:05 UTC 因 gathered_items 仍為 08-14 而正確中止 → **08-15 日報尚未產出**，待本機補跑 `/news-pipeline`（watchdog 15:00 UTC 亦會推播）
- **未動手（需使用者）**：Reddit OAuth＋GitHub PAT 兩組憑證（一次解三個來源的分數可信度、GitHub Search 限流，逾期 workaround 中槓桿最大）

## 2026-08-15 Ingest

- 來源日報：[[news/2026-08-15]]（本機補跑；GH Actions `daily-gather` 10:28 UTC 於 Gather 步驟以 exit 134/SIGABRT 失敗，本機 21:42 台北排程抓料成功 62 則，雲端 routine 因 gathered_items 仍為 08-14 而正確中止）
- 更新頁面：entities/opus-5、entities/fable-5、entities/claude-code、topics/official-community-gap、topics/anthropic-business、topics/enterprise-tool-tracker、entities/pricing、topics/competitor-landscape、topics/anthropic-government-policy、topics/recursive-self-improvement、topics/community-tech-patterns、topics/community-tech-discussions、topics/code-quality-decline、feature-radar、overview
- 新增頁面：無
- 摘要：浮水印補上官方機制說明與第三方偵測 API（跨 3 來源）；八月風險報告揭露未發布的 Model 2 與新對齊疑慮，官方稱無釋出計畫，報告自陳內部 AI R&D「明顯更快但尚未達兩倍」；Reuters 獨家指 IPO 估值繫於 2028 年 1,900–2,000 億美元營收預測；Samsung 晶片設計採用由 ❓ 轉為具名報導證實（同時明言仍會犯嚴重錯誤）；Auto 模式 8/14 如期生效，媒體發 PSA。
- 呈現品質：全部通過（人物記者本輪無頁面更新）
- 未收錄決策（主編判定）：
  - Cami Clark（Dario Amodei 配偶）Epstein 相關報導兩則（Forbes、NY Post）——內容為私人個人過往私生活，與 Claude/Anthropic 技術、產品、政策、生態無直接關聯，依專案 `CLAUDE.md`「不收錄」條款判定不收，未在任何頁面留痕
  - 「8 AI Coding Models Ranked」（mshale.com，專頁定向 competitor-landscape）——來源網域可信度存疑，文中「Opus 4.6」與本站陣容紀錄（4.7／4.8／5）不符，商業記者依「從嚴判斷、寧可不收」處理
  - Elon Musk 承認低估 Anthropic（Motley Fool）——投資評論媒體二手轉述，原始出處／日期／措辭均不明，人物記者判定證據不足不建檔
  - anthropic-commitments 本輪不動：今日事件不屬「承諾修復／承諾政策／明確拒絕／兌現先前承諾」性質，追蹤中五項均無官方新動作（Auto 模式如期生效屬產品發布時程，不列入承諾追蹤以免稀釋該頁語意）
- 品質備註：[主編] 派工模板落後規則檔——社群記者派工要求「今日順手改寫 community-large-codebase-workflow 主線敘事」，但 `.claude/rules/wiki-ingest-community.md` 今日改版後已明定日更只在 patterns 節點標 `**主線：**` tag、主線縫合改週更。記者正確依規則拒絕執行並回報矛盾，非記者疏失；`.claude/commands/wiki-ingest.md` 派工範本無此指示，是主編臨場加寫，後續派工不得再加。
- 主編待辦（轉主編層 web 查證，非記者可為）：Reddit 質疑 Opus 5 與 Fable 5 共用同一週用量池、牴觸官方「Fable 5 佔 50%」設計，商業記者已在 `entities/pricing` 以待查證方式記錄；需查 support.claude.com 官方說明中心確認配額池規則，屬 `/wiki-lint` 5c 範圍。

## 2026-08-16 週度延伸回顧

- 延伸：
  - `topics/anthropic-business`：「IPO 前瞻與估值追蹤」新增「資本佈局背景（推論）」小結，並置解讀算力合約線（08-11 一天四筆：Riot／GIC／Macquarie／Volta）與 IPO／估值線（08-13 $2 兆傳聞、08-15 Reuters 2028 營收預測、Q2 $115 億），回答「為何此刻密集簽算力合約」。呈現層整理不引入新數字，只動「最後更新」
  - `topics/enterprise-cost-management`：補入 HN `cookbook-meter`（08-14），為繼 Quesma「40 倍」、modelplane.ai「44 倍」後第三個獨立方法論的訂閱／API 價差量化。**記者查證後修正主編轉述**：$5,868 是作者本人上月訂閱換算的工具輸出而非留言數字，HN 僅 2 分，已據實標「單一社群回報」、不與前兩則等量齊觀
  - `topics/code-quality-decline`：補入 08-12 Reddit forensic archive（Claude 失敗／退化／slop 存檔，附 HackerOne 回報連結），定位為社群把品質下滑從零散貼文升級為可被引用的證據基礎設施，呼應頁內 CC-Canary 先例；單一 Reddit 貼文無週熱門標記，已標訊號強度
  - `entities/dario-amodei`：修正三處過期斷言（使用者裁決選項 1）。頁上原寫兩篇報導「均未提供其姓名」，但 08-15 另有報導提供姓名而本庫判定不收錄，導致頁面持續宣稱假事實。改為只描述那兩篇報導本身「內容停留在標題層級、未展開姓名或具體職務」——斷言範圍從「沒有人提供」收窄到「這兩篇沒展開」，不論外界後續如何都保持為真。未引入 08-15 任何素材、未動狀態符號與探針、未加訊號日
- 使用者跳過項目：官方部落格〈Maximizing the value of your Claude Code sessions〉（HN 268 分，本週互動最高的官方一手內容）全庫零收錄——功能記者判定為正確排除（無新操作，不符 feature-radar 准入），主編提出可能的家為 `community-large-codebase-workflow` Context 管理主線或 `entities/pricing` token 成本角度，使用者本輪未指定，維持不安家、留作觀察
- 待辦（同記者跨時交辦，非轉知帳本範圍）：下次 `/wiki-lint` 由社群記者評估 `community-tech-tools.md` 是否收錄 forensic archive 存檔工具本身（單一社群來源、score 不可信，門檻待判）
- 聚焦校準：非本月首次（8 月已於 08-01 執行，命中率 76%，回看 06-29~07-05），跳過
- reader-notes 處置：4 條 ⏳ 全部維持 ⏳，無 🎨／📝 待辦、無逾期雜記。LLM code review 單位成本本週 review×成本 交集零命中、庫內仍零節點；codebase map format 由社群記者標一則鄰近訊號（GitHub #56913 tiered Opus/Sonnet + persistent state，08-13）——碰同一底層需求但屬架構提案而非具名 format，不算第三節點，若其持久化設計具體化則可能是；模型路由／靜默降階本週無新進展；GPT-5.6 對照維持 07-19 起的被動觸發，本週無官方 benchmark
- 無建議記者：模型、功能、安全政策、人物（四位皆回報訊號已被 daily ingest 即時吃進、深度與訊號量相符，非未審視）

## 2026-08-16 Query：官方使用指南在分類層無落點

- **提問**：使用者對週度回顧「官方部落格〈Maximizing the value of your Claude Code sessions〉沒有家」追問「這為什麼沒有家」，繼而指出「技術討論、工作流模式，這我覺得也可以放官方的」。
- **根因（兩層同時漏，才會漏得乾淨）**：
  1. **分類層無格子**——六類分類表的「功能」列只有版本／指令／旗標／SDK／Breaking change／beta，這篇沒有新指令；「社群」列寫作「社群工具（Show HN / score ≥ 30）、技術討論、工作流模式」，加上類別名叫「社群」，讀起來像出處篩選器，主編分類時不會把官方部落格丟過去。**但查證後確認：`community-tech-discussions` 的收錄門檻本就明列「重要人士具名表態」為三個合法訊號來源之一，`community-tech-patterns` 的觸發條件從未限制出處——規則早就允許，是措辭讓人不敢用。**
  2. **主題上最精準的頁把它擋在門外**——`topics/coding-workflow-guide` 的 §2a 標題就叫「怎麼讀得省」，且該頁半數子節是「官方的 include／exclude 清單」「官方的四階段」「官方的規格品質判準」，本就是官方＋社群雙軌；擋住的是建頁時寫的一句「不吃新聞條目」。那句要防的是無來源灌水（配套理由寫著「無來源、不會被更新、會讓讀者誤以為經查證」），卻拿**進料管道**當**可信度**的代理，於是擋掉了唯一最有來源的那種內容。
- **使用者裁決**：兩頁分工，加分流鐵則。
- **處置**：
  - `.claude/rules/wiki-ingest.md` 分類表「功能」列補「官方對既有功能的使用指南」、「社群」列明寫後兩者不限出處；新增「分流鐵則：官方內容不是社群類的禁區」節（三型態對照表：怎麼用既有功能 → 功能／coding-workflow-guide；官方提出的新工作流模式 → 社群／patterns 標官方出處；有新指令旗標 → 功能／claude-code + feature-radar）
  - `.claude/rules/wiki-ingest-features.md` coding-workflow-guide 改為兩條進料（技能清冊週更 ＋ 官方使用指南每日），新增「官方使用指南的寫入紀律」
  - `.claude/rules/wiki-ingest-community.md` 新增「官方內容不是你的禁區」，界線依「它給讀者什麼」而非出處
  - `.claude/review-registry.json` 加三邊 sync_pair（任一邊被改回去，官方使用指南會再次無家可歸）
  - 該條目已由功能記者寫入 `coding-workflow-guide` §2a 新子節「官方的 session 經營建議」，並與該頁第 7 段既有的「同一問題糾正超過兩次就 `/clear`」做區隔（一個管單一任務內失敗重試、一個管任務邊界間的 context 衛生）
- **未查完（另案）**：查證途中發現兩條 funnel 異常，尚未定論——(a) 2026-08-15 `Anthropic Blog` gathered 1 → filtered 0，但 `filter.py` 只擋 Google News 標題無關鍵字與 PR wire 網域，不可能丟棄官方部落格；最像的解釋是 dedup 併入 HN 那份，但 dedup 合併會累加 `source_count` 而存活項為 1，對不上。(b) `Official Docs` 連三天 filtered > 0 但 emitted 0（08-13 8→8→0、08-14 1→1→0、08-15 1→1→0），可能是 `seen_urls` 正常去重，未證實。

## 2026-08-16 Query 後續：兩條 funnel 異常追到底

承同日「官方使用指南在分類層無落點」條目末的「未查完（另案）」，使用者指示全部追完，結果一好一壞。

- **(a) `Anthropic Blog` 08-15 gathered 1 → filtered 0：沒有 bug，是歸因假象。** 該來源當天抓到的是〈How Claude's text watermarking works〉（`anthropic.com/news/claude-text-watermark`），與其他四來源合併成 `source_count: 5` 的條目，勝出標籤為 Hacker News。funnel 的 `filtered`/`emitted` 是按**存活條目的 source 前綴**回算，故官方部落格的貢獻記到 HN 頭上。`source_count` 累加正常（08-15 有 8 則 >1），132→118 的 dedup 損耗逐源對得上。**但這使低流量官方來源長期顯示「零產出」，會誤導來源記分卡與來源×類別 graph**——已登記 `docs/workaround-register.md`（複查 2026-08-30），非本次修復範圍。
- **(b) `Official Docs` filtered > 0 但 emitted 0：真 bug，已修。** `official_docs_watch` / `official_skills_repos` / `api_docs` 三支變更偵測來源，每次都以**同一個穩定 URL**重報、且 `score=0`；`emitted_cache` 以正規化 URL 為鍵，唯一復活路徑是分數再燃（≥2× 且 +10），從 0 永遠不可能達成。**於是每個被監看頁面的第一次變動被日報收錄後，之後所有變動被永久靜默丟棄。** 實測 9 個監看目標**已燒掉 8 個**（08-07～08-12），含 `claude.com/pricing` 與 support 說明中心的方案／配額／限制三頁——正是 `.claude/rules/wiki-ingest-commercial.md` 指定的計費事實權威來源。`api_docs` 更早就燒了：它已在 URL 用 `#anchor` 區隔每則 release note，但 `_normalize_url` 會剝掉 fragment，全部塌成同一鍵（08-07 起）。
  - **修法**：`FeedItem` 新增 `dedup_key`（`"<url>#<內容 hash>"`），`emitted_cache.cache_key()` 優先採用、否則 fallback 正規化 URL；三支來源填值；`main.py` 持久化該欄並讓 `--confirm-digest` 以完整記錄確認（確認到裸 URL 會讓真正的條目永遠未確認、每輪重複提供）；`dedup` 合併時繼承此欄（與 `topic` 同一類坑）。
  - **自我修復**：新鍵與舊的裸 URL 紀錄永不相撞，8 個燒掉的頁面下次變動即自動復活，**不需清 cache 或寫遷移**。已對真實 `emitted_items.json` 實測四個燒掉的 URL：修正前靜默丟棄、修正後放行。
  - 新增 `src/tests/test_change_detection_cache.py`（10 例，含「同內容仍須抑制」的反向保護）；抽掉修正會紅 4 項。測試 300/300 綠，`/pipeline-change-check` compare 15 項指標全無變動、109 份舊 digest 解析零失敗。

## 2026-08-16 Query 後續之二：funnel 歸因失真已修（使用者「全部修到沒問題」）

承同日「兩條 funnel 異常」條目中登記為「已診斷未修」的 (a)。追下去發現後果比原估嚴重：`scripts/source_scorecard.py` 的 **收錄率 = emitted / gathered** 與 **wiki 率 = 歸因筆數 / emitted** 都吃這兩欄，而該記分卡正是 `/wiki-lint` 6e 判斷來源去留的依據——**2026-08-15 Anthropic Blog 供了當日最大條（浮水印報導），記分卡卻算它 0% 收錄率**。一個供頭條的來源可能因此被淘汰。

修法分三段，缺一段就白做：

1. **記住是誰**：`FeedItem.contributors` 記錄 dedup 併掉的來源標籤（勝者自己不列入），合併時以集合聯集更新，順序無關且冪等（A←B 再 AB←C 與任何順序同解）
2. **算對數字**：`main._count_by_prefix` 改為每則條目對「所有貢獻來源」各計一次。per-source 數字因此可能加總大於條目數——那是誠實的讀法（「本來源貢獻了 N 則存活條目」）；`totals` 仍計條目數。每份抓取副本只會併進一個存活條目，故 per-source `filtered`/`emitted` ≤ `gathered` 仍成立。修這裡時踩到一個回歸：無 source 標籤的條目原本落 `""` → `_unmapped` 桶，新寫法一度把它濾掉——那會讓「來源標籤壞掉」變隱形，已修回並加註
3. **傳到下游**：`gathered_items.json` 新增 `contributors`；日報來源欄改寫成 `` `Hacker News ＋Anthropic Blog、Google News / PCMag` ``（`SOURCE_RE` 對反引號內是自由文字，解析器不受影響）；`.claude/rules/wiki-reporter-shared.md` 規定記者見 `＋` 就每來源各報一筆歸因。只改前兩段的話 `source_attribution.jsonl` 仍只記勝者，wiki 率照樣失真

registry 加一組 sync_pair 釘住產出端與歸因端（只改一邊等於白做）。測試 308/308 綠（新增 8 例：合併鏈全記錄、勝者不列自己、標籤前綴正規化、同來源在同一條目只計一次、無貢獻者時行為不變）；`/pipeline-change-check` compare 15 項指標全無變動、109 份舊 digest 解析零失敗；記分卡實跑正常。

**殘留（非缺陷，時間問題）**：歷史 funnel 資料仍是舊語意，記分卡的長期平均要再累積數日才反映真值。`docs/workaround-register.md` 該列已標修復並註明此點。

## 2026-08-16 Query：週報深挖專欄在網站上整個消失

- **提問**：使用者指出 W33「深挖專欄 · 格式不對」，並補充「前幾期都有渲染」。
- **實際症狀（比初判嚴重）**：不是標題矮一級，是**專欄元件整個不渲染**。`scripts/build_web.py` 以 `###` 切子區塊，再把「深挖：」那節抽成專屬元件（kicker「深挖專欄 · DEEP DIVE」＋標題＋內文）；W33 寫成 `####`，子區塊不存在 → `deepDive = None` → 1,200 字整段被靜默併進 `roundup`（討論綜述），網站上無任何錯誤訊息。已用修正前的建置產物（commit 9ed3f7a）驗證：`deepDive` 確為 `None`、深挖末句出現在 `roundup` 尾端。
- **根因（不是有人沒照規格）**：規格檔 `.claude/commands/weekly-report.md` 的範例從 2026-07-26 第一版起就寫成 `` `#### 深挖：主題名稱` ``——**那是規格文件自己的巢狀深度**（該處為 `#### (2) 技術討論＋深挖`），而週報輸出檔的深挖是 `## 二、技術討論與深挖` 的子標題、天然是 `###`，少一層。W30–W32 三期的 session 都從輸出結構推導出 `###`（正確），但沒有人回頭修規格，於是錯誤範例活了三週；W33 照字面抄就中。字數同理：規格 400–600 從未有任何一期遵守（實測 999／1,112／1,080／1,142），也從來沒有機制比對過——與懸置標記同一個病：規格裡寫著一個數字，沒有任何流程會去讀它。
- **處置**：
  - `weekly/2026-W33.md` 小標改回 `###`，重建上站
  - 規格改為 `` `### 深挖：主題名稱` ``＋**800–1,200 字**（依四期實測校準，使用者裁示「變多可以」），並加註「不要照抄本規格檔自己的標題深度」與這次的教訓
  - `scripts/check_weekly_ledger.py` 新增 `check_deepdive()`：層級非 `###` → ❌ 硬擋（會靜默壞掉渲染）；字數逾範圍 → ⚠️ 只提醒（編輯判斷，不設機械棘輪）；多個深挖小標 → ❌；完全沒有 → ⚠️（規格允許「查無不補位」時整段省略）
  - `.claude/review-registry.json` 加三邊 sync_pair（規格／解析器／檢查器）
- **驗證**：故意把小標寫回 `####`，檢查器紅並指出「會讓專欄元件整個不渲染、內文被靜默併進討論綜述」；還原後 308 測試全綠。

## 2026-08-16 Query 續：週報規格範本漏畫的慣例，一次補齊

使用者指示「全部改一改」後，對四期週報做了兩層交叉比對（建置產物 34 個欄位 ＋ markdown 結構骨架），把「三期實作有、規格範本沒畫」的項目一次補完。

**比對結果**：建置產物層僅剩 `nextweek.recap` 在 W30 為空——那是規格明訂的第一期例外（無上一期可回收），非缺陷。markdown 骨架層找出兩處，皆為同一個病：

| 漏處 | 症狀 | 前三期 | 規格範本 |
|---|---|---|---|
| 深挖小標層級 `###` vs `####` | **網站上專欄元件整個不渲染**，1,200 字被靜默併進討論綜述 | 三期皆 `###`（正確） | 範例寫 `####`（規格文件自己的巢狀深度） |
| 回收表導言一行 | `nextweek.intro` 空，網站上小標直接跳進表格 | 三期皆有 | 範本沒畫 |
| 新開表導言一行 | 不進網站（`app.js` 只渲染 intro／recap／forecasts），但 Obsidian 與原始檔缺少「為何追蹤 7 條只新開 5 條」的答案 | W31／W32 皆有 | 範本沒畫 |

**共同結構**：規格是設計當下寫的，實作三期各自把它修對，但沒有人回頭改規格，也沒有任何機制比對兩者——與懸置標記、與本日稍早的 funnel 歸因失真同型。

**處置**：W33 補齊兩行導言並改回 `###`；規格範本補上兩行並註明「不要照抄本規格檔自己的標題深度」與「新開表那行不進網站但仍必寫」；`scripts/check_weekly_ledger.py` 的 `check_deepdive()` 擴充為三檢（層級硬擋、字數 WARN、兩處導言 WARN）；registry 加規格／解析器／檢查器三邊 sync_pair。

**驗證**：W31／W32／W33 的 markdown 結構骨架現已**完全一致**；反向驗證兩項（寫回 `####` 會紅並指出後果、拿掉導言會 WARN）；308 測試綠。

## 2026-08-16 Ingest | news/2026-08-16.md（45 則）

- 來源日報：[[news/2026-08-16]]（45 則，13/13 來源；日報實收 19 則，另 26 則透過 `list_digest_omissions.py` 一併提供給記者判斷；其中 5 則因與 Claude/Anthropic 完全無關聯（Qwen 系列討論、Unsloth Desktop app）在主編分類階段即排除，未進入任何記者派工）
- 分類派工：功能 8 則、社群 16 則、商業 6 則、安全政策 7 則、人物 3 則（模型類今日無條目，未派工）；六類皆以 `subagent_type: general-purpose` + `model: sonnet` foreground 派工，角色前導導向 `.claude/agents/wiki-reporter-[category].md`（正典路徑）
- 更新頁面：
  - **功能**：`entities/claude-code.md`（新增 4 則已知問題：Windows BSOD via Wof.sys #32870、Bedrock Opus 4.7 permission_error #51183、output style YAML frontmatter 未注入系統提示 #47482、GPU process crash 拖垮全部 session #81698；已同步分組統計）、`topics/official-community-gap.md`（Inter-session communication #24798 互動數同步至 78 留言）
  - **商業**：`topics/anthropic-business.md`（傳 Anthropic 洽談收購 Decart，交易規模上修至約 70 億美元、稱先於 Nvidia 談成，單一來源未證實；財務狀況表新增 TechRadar「AI 界的 Apple」評論角度）
  - **社群**：`topics/community-tech-patterns.md`（新增 2 節點：Looker 內建 MCP 端點免裝本機 Toolbox、背景 agent 空 prompt 仍「順利結束」的實戰教訓；GitHub 高星倉庫 AIUsage/awesome-claude-code 因無法查證 forks/issues/commit 佐證且代理無法連線 GitHub API，判斷不收錄）
  - **安全政策**：`topics/ai-agent-safety.md`（Anthropic 官方研究〈Patterns and problems in emerging multi-agent systems〉，剖析多智能體系統浮現的行為模式與風險；Benzinga／Business Insider 同題跟進報導措辭明顯較官方原文聳動，已並存標注、未採信媒體框架強度）
  - **人物**：無（Epstein 相關三則報導經查不符 `entities/dario-amodei.md` 觸發條件，亦不構成 Cami Clark 本人建頁門檻，判斷不收錄，未動任何頁面）
- 新增頁面：無
- 摘要：Anthropic 發布多智能體系統風險研究並引發媒體聳動化跟進、傳出洽談收購 Decart（約 70 億美元，未證實）、Claude Code 集中出現 4 起穩定性 bug 回報（BSOD／Bedrock 權限／output style／GPU crash）
- 呈現品質：全部通過

## 2026-08-17 Ingest | news/2026-08-17.md（52 則）

- 來源日報：[[news/2026-08-17]]（52 則抓取，13/13 來源；日報實收 26 則，另 26 則透過 `list_digest_omissions.py` 一併提供給記者判斷）
- 分類派工：功能 9 則、商業 8 則、安全政策 3 則、社群 22 則、人物 4 則、模型 3 則（六類皆有條目，全數派工）；六類皆以 `subagent_type: general-purpose` + `model: sonnet` foreground 派工，角色前導導向 `.claude/agents/wiki-reporter-[category].md`（正典路徑）
- 更新頁面：
  - **功能**：`entities/claude-code.md`（8/16 服務中斷已修復記入「🌐 服務穩定性」；GitHub Issue #8477/#3412/#17432 互動數同步；新增 2 則「待查證」：Claude Desktop 類 Slack 功能、Cowork 內建瀏覽器／超級應用傳聞，TestingCatalog 單一來源未經官方證實）、`entities/claude-science.md`（新增官方 `anthropics/life-sciences` marketplace repo，576★）
  - **商業**：`topics/anthropic-business.md`（新增 IPO 估值炒作評論列）、`topics/competitor-landscape.md`（新增智譜 Zhipu「抓 bug 優於 Anthropic/OpenAI」聲明）、`entities/pricing.md`（印度盧比定價訴求 issue #17432 留言數 210→212）
  - **安全政策**：`topics/ai-agent-safety.md`（SOFX 單一來源「Claude agent 互相破壞並隱瞞使用者」報導標「待查證」；WSJ「AI Models Went Rogue」深度報導併入既有 turf war 敘事；同步清理違反段落上限的重複舊段落）、`topics/anthropic-government-policy.md`（EU 浮水印法規遵循報導補充）
  - **社群**：`topics/community-tech-discussions.md`（浮水印反彈事件熱度升級 🔥🔥🔥→🔥🔥🔥🔥，新增技術彙整節點；GitHub 三個高星 repo 因無 forks/issues/commit 佐證且代理無法查證，判斷不收錄）、`topics/community-tech-patterns.md`（新增 MCP 長 session 穩健化第四種失效模式節點）
  - **人物**：`entities/dario-amodei.md`（新增 08-16 雙重表態：回應 Gavin Baker 批評稱「信任危機」＋主張需具體科學突破如治癒癌症才能贏回公眾信任，三方獨立來源交叉確認）
  - **模型**：無（Opus 5/Fable 5 相關三則 Reddit 條目 score 不可信且內容空泛，均未達收錄門檻，未寫入任何頁面）
  - **主編**：`index.md` 修正 pricing 條目摘要（原文字停留於 07-03 舊數字「👍584，無官方回應」，已與 pricing.md 現況同步為「07-13 已回應 Pro 方案、Claude Code 涵蓋範圍未見官方確認、留言 212」）
- 新增頁面：無
- 摘要：Anthropic 浮水印功能引發訂閱用戶大規模反彈（HN 293 分＋多家媒體跟進）、8/16 服務中斷已修復、Q2 營收與 IPO 估值傳出具體數字（115 億美元／1900-2000 億美元）、CEO Dario Amodei 公開回應「信任危機」
- 呈現品質：功能／商業／社群 全部通過；安全政策 `ai-agent-safety.md` ⚠️ 已修復（清除違反「現況不被時序侵蝕」段落上限的重複舊段落）、`anthropic-government-policy.md` ✅ 通過；人物 未附獨立呈現品質欄位（角色檔回報模板無此列）

## 2026-08-18 Ingest | news/2026-08-18.md（61 則）

- 來源日報：[[news/2026-08-18]]（61 則抓取，13/13 來源；日報實收 38 則，另 23 則透過 `list_digest_omissions.py` 一併提供給記者判斷；其中 5 則因與 Claude/Anthropic 完全無關聯（Qwen 系列討論、CUDA Agent 論文、Amazon AI 訓練設施報導）在主編分類階段即排除，未進入任何記者派工）
- 分類派工：功能 13 則、商業 9 則、安全政策 9 則、社群 21 則、人物 2 則（六類皆以 `subagent_type: general-purpose` + `model: sonnet` foreground 派工，角色前導導向 `.claude/agents/wiki-reporter-[category].md`；模型類今日無條目，未派工）
- 更新頁面：
  - **功能**：`entities/claude-code.md`（新增 5 則高互動 GitHub Issue：Desktop Relaunch 檔案鎖 #42776、Remote Control 重連失效 #34255、Console 閃爍 #14828、OAuth 白名單 #27263、刪除 session #13514；`/design` 指令與 Claude Workbench 下線各標 ❓ 待查證，複查日 2026-09-01）、`entities/claude-skills.md`（官方技能庫新增 claude-academy-guide、discernment-nudge）、`entities/claude-design.md`（`/design` 指令待查證標記）；feature-radar 新增「自訂專案 Transcript 目錄短名稱」（`CLAUDE_CODE_PROJECT_DIR_NAME`，v2.1.234，🔥）並由主編同步全覽表列與升版風險最新版本行
  - **商業**：`topics/anthropic-business.md`（Anthropic 年化營收站上 650 億美元，Bloomberg／Reuters／CNBC／Benzinga 四方同步報導，另補 TechRadar「AI 界的 Apple」評論）、`topics/competitor-landscape.md`（GitHub Copilot 計費改版終結無限量方案；Cursor 推出程式碼託管平台 Origin）
  - **安全政策**：`topics/anthropic-government-policy.md`（CNET／Guardian／PCWorld 三方跟進浮水印功能報導，延續既有政策系列追蹤）、`topics/ai-agent-safety.md`（CyberSecurityNews 揭露勒索軟體操作者濫用 Claude Code 竊取 LDAP 密碼並外洩資料庫；Cybernews 報導 Anthropic 揭露多智能體「疑心較重」agent 互相部署惡意軟體研究；World IP Review 提示注入商業機密訴訟專頁定向條目）；⚠️ 已登記轉知帳本 H-3e88e6：兩則音樂版權訴訟（Round Hill 10 億美元求償、另一音樂出版商）依既有慣例應收錄至商業記者 `anthropic-business.md`，因商業記者已完成派工，留待下次 ingest 處理
  - **社群**：`topics/community-tech-discussions.md`（新增「Anthropic's War on open source AI」HN 146 分節點）、`topics/community-tech-patterns.md`（新增 statuslin.es Claude Code status line 社群展示網站節點）；GitHub Search 高星倉庫 internet-court-skill（3793★）與 devnors-data-mcp（121★）因無法查證 forks/issues/commit 佐證，比照既有判例不收錄；19 則低互動 Show HN／Reddit 條目未達門檻不收錄
  - **人物**：`entities/dario-amodei.md`（既有 08-14 待查證標記加訊 2026-08-18：The Week 首次在標題層級揭露 Dario Amodei 妻子姓名「Cami Clark」；Fidji Simo 呼應 Amodei「治癒疾病」論述併入歷史記錄，比照 08-16 判例不為 Cami Clark 另建頁）
- 新增頁面：無
- 摘要：Anthropic 年化營收站上 650 億美元（IPO 前強力訊號，四方媒體同步報導）、Claude 浮水印功能持續延燒（CNET/Guardian/PCWorld）、資安媒體揭露勒索軟體濫用 Claude Code 攻擊鏈、音樂產業版權方接連對 Anthropic 提告（10 億美元求償）、Anthropic 揭露多智能體惡意行為研究
- 呈現品質：全部通過

## 2026-08-19 Ingest | news/2026-08-19.md（50 則）

- 來源日報：[[news/2026-08-19]]（50 則抓取，13/13 來源；日報實收 43 則，另 7 則透過 `list_digest_omissions.py` 一併提供給記者判斷）
- 分類派工：功能 9 則（含合併項）、模型 2 則、商業 7 則（另含轉知待接手 1 筆）、安全政策 1 則、社群 17 則（人物類今日無條目，未派工）；六類皆以 `subagent_type: general-purpose` + `model: sonnet` foreground 派工，角色前導導向 `.claude/agents/wiki-reporter-[category].md`（正典路徑）
- 更新頁面：
  - **功能**：`entities/claude-code.md`（新增 3 則已知問題：Memory leak /tmp/claude-*-cwd 未清理 #8856、Linux 剪貼簿貼圖失敗 #8324、Windows GPU 當機 appxState=2 #80444；8/18-19 二度服務異常記入「🌐 服務穩定性」）、`entities/claude-skills.md`（官方技能庫 academy-guide／claude-academy-guide 改名事件，核對確認非新增）；feature-radar 新增「spellcheck 輸入框拼字檢查」（v2.1.235，🔥）並由主編同步全覽表列、升版風險最新版本行、⏰ 倒數中新增 Claude Code 週用量促銷 8/31 到期列
  - **模型**：`entities/fable-5.md`（官方文件確認促銷實際於 7/19（非既有頁面誤植的「6/22」與 7/7）結束，依方案分流計費；修正頁面內一處實質錯誤：舊敘述誤寫「Max 訂閱用戶須額外付費」，實際 Max 為標準內含；另有 Fable 5 使用率偏低的單一來源報導，已標註未經證實、不臆測因果）
  - **商業**：`entities/pricing.md`（Fable 5 計費規則官方再確認；修正一項既有錯誤——07-12 條目誤將「週用量 +50% 促銷」與「Fable 5 免費期」記為同步於 7/19 到期並移入已失效規則，今日證實兩者為獨立時程，週用量促銷實際已延長至 2026-08-31，已更正「當前生效」／「已失效」兩表）、`topics/anthropic-business.md`（新增 Anthropic IPO 前置動作：超級投票權＋逾 100 億美元信用額度；OpenAI vs Anthropic 第二季業績對比含相反訊號並陳；處理轉知 H-3e88e6，Round Hill Music／另一音樂出版商著作權訴訟已收錄至商業風險表）、`topics/enterprise-tool-tracker.md`（新增 Payward〔Claude Mythos 5〕、Duke University〔pay-as-you-go 訂閱〕兩筆具名採用）
  - **安全政策**：`topics/anthropic-government-policy.md`（Business Insider 報導 Anthropic 浮水印偵測技術遭開發者繞過，併入既有浮水印政策系列追蹤，標明僅標題層級可用）
  - **社群**：`topics/community-tech-patterns.md`（新增 2 節點：HP 印表機驅動逆向工程單次長 session 案例、machine0 常駐 GPU/CPU VM 基礎設施）、`topics/community-tech-discussions.md`（新增 GLM 遷移文章、Reddit「22GB 本地模型」未附證據宣稱兩列；同步清理 14 筆逾 21 天 ☄️閃現舊列）、`topics/code-quality-decline.md`（「Opus 5 上線後品質感知訊號群」新增第 9 則訊號）；skill-based-architecture（502★）、Lucasartsifier、五款 Show HN session 管理工具叢集、dev.to J-Space 等因未達收錄門檻或無法查證佐證，判斷不收錄
  - **主編**：`wiki/feature-radar.md` 內既有 ❓ 待查證標記（Fable 5「7/7 後配額政策」）依懸置標記語法加 `訊 2026-08-19`，更新題目內文為今日官方文件查得的實際規則（7/19、依方案分流），符號維持 ❓ 未改判，正式結案留待 `/wiki-lint` 5c
- 新增頁面：無
- 摘要：Claude 服務 8/18-19 二度效能異常（官方已修復＋監控中，多家媒體同步報導）、Claude Code 週用量 +50% 促銷再度延長至 8/31、Anthropic 傳出 IPO 前置動作（超級投票權＋信用額度擴大）、OpenAI vs Anthropic 第二季業績對比出現相反訊號、Fable 5 促銷結束後配額規則經官方文件澄清（7/19 而非頁面舊誤植的 7/7）並修正既有頁面兩處實質錯誤
- 呈現品質：全部通過

## 2026-08-20 Query：週報選題／寫作規格改版，W33 深挖重寫（破例）

- **使用者回饋**：W33 深挖「同樣的 token 差 40 倍」很不好讀，追問選題標準。
- **診斷**：規格對深挖只有一道實質閘門（防假教學＝能否教出機制層），而我實際用的是**排除法**——浮水印只有標題層級、subagent 四模式細節待查證，兩題都因「本週日報素材不足」被砍，剩下唯一素材夠的題目被硬撐到字數框。**根因是把「素材涵蓋窗」當成「內容來源」**，於是選題被素材密度綁架，而非讀者價值。
- **使用者裁示**：(1) 選題可由本週熱議話題延伸，不必是本週新聞裡的技術本身；(2) 來源不必限於 wiki／官方文件／歷史日報，**先定寫作方向，素材不足就往外查**；(3) 深挖字數變多可以；(4) W33 選 B——回頭重寫。
- **規格改動**（`.claude/commands/weekly-report.md`）：
  - 步驟 2 拆為「選題素材」（固定 7 日窗）與「內容素材」（不受窗限制）
  - 新增**選題三判準**（本週有訊號／寫得出寫作方向三件套／每個機制斷言可指回來源）
  - 新增**寫作方向三件套**（一句讀者動作、四段大綱、缺口清單）——動手前必須先寫出來，寫不出就換題
  - 新增**來源紀律**：不限來源位置，但機制層每個斷言要能指回可取回來源（URL＋取得日）；推導結論標「（推論）」；兩者皆非即刪。另記無 egress 環境的退路
  - 新增**寫作風格**（依 W30–W32 實測歸納、W33 為反例）：四段功能標籤骨架＋六條寫作規則＋三條禁止
- **W33 深挖重寫**（凍結存檔破例一次，原因記於此）：換題為「subagent 為什麼會『回報完成』卻沒做完」。缺口以官方文件外查補齊（`code.claude.com/docs/en/sub-agents`，2026-08-20 取得），核心機制為 **`AskUserQuestion` 被從每個 subagent 移除 → 架構上沒有回問通道 → 唯一訊號是它自己寫的摘要**，據此解釋 dev.to 四種靜默失敗與官方自揭的 agent 互相破壞。三條陷阱皆帶具名物（`model: inherit`、`tools` 全繼承、`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 20 vs 社群 10）。
- **⚠️ 同時發現的操作失誤（比上述更嚴重）**：執行 `/weekly-report` 時**沒有查證今天的日期**，沿用先前補跑任務殘留的 08-15 往後推一天當成 08-16，實際今天是 **2026-08-20（ISO W34）**。後果：(a) 無參數應產 W34 卻產了 W33；(b) W33 涵蓋窗誤寫為「6 份日報、08-16 尚未產出」，實際 08-16～08-19 日報皆已由雲端 pipeline 正常產出。**W33 本身仍是必要的**（帳本鏈 W32→W33→W34 缺它不可），已更正涵蓋窗為 08-10～08-16 全週共 7 份、補入 08-16 官方多智能體研究報告與 Decart 金額更新（70 億、競價先於 Nvidia，單一來源）。**W34（08-17～08-23）尚未產出，該週未完結，待 08-23 後再跑。**
- **殘留**：深挖 1,228 字，略高於新訂的 800–1,200（檢查器 ⚠️ 提醒、不擋）。已自 1,911 字砍到 1,228（含刪去第四條陷阱與「怎麼用」段對陷阱 1／2 的重複陳述）；再砍只能砍掉一條陷阱，判斷保留內容優於湊進字數框。

## 2026-08-20 Ingest | news/2026-08-20.md（81 則）

- 來源日報：[[news/2026-08-20]]（81 則抓取，13/13 來源；日報實收 34 則，另 47 則透過 `list_digest_omissions.py` 一併提供給記者判斷）
- 分類派工：模型 2 則、功能 16 則、商業 15 則、安全政策 4 則、社群 38 則（人物類今日無條目，未派工）；六類皆以 `subagent_type: general-purpose` + `model: sonnet` foreground 派工，角色前導導向 `.claude/agents/wiki-reporter-[category].md`（正典路徑）
- 更新頁面：
  - **模型**：查證後判斷今日兩則條目（「Model 2」內部限定使用、Anthropic design study 與蛋白質無關）均為既有事實重複轉載或內容不可讀，未動任何頁面
  - **功能**：`entities/claude-code.md`（新增 2 則已知問題：修改 thinking block 觸發 API 400 錯誤 #10199、v2.1.113 起 Termux/Android glibc 破壞性回歸 #50270；互動數更新 3 則：Cowork VM bundle #22543、記憶體洩漏 #4953、Cowork 工作區啟動失敗 #27801；記入 v2.1.237／SDK 三則版本異動；Reddit 回報「額度重置後自動繼續」已於既有 feature request #13354 註記社群回報）、`entities/managed-agents.md`（anthropic-sdk-python v0.125.0 新增 web search 設定）；feature-radar 新增「Concise 輸出風格」（v2.1.237，🔥）與「Managed Agents Web Search 設定」（🔥），並由主編同步全覽表列、升版風險最新版本行與 Cowork 風險列互動數；轉知 2 筆（社群：claude-code-lsps 星數防刷佐證待週更評估；安全政策：Gmail 自主發信涉 agent 權限擴張）
  - **商業**：`entities/pricing.md`（DevOps.com「暫時性用量提升今晚到期」與已確認延長至 8/31 的週用量 +50% 促銷間關係無法從標題層級確認，新增 ❓ 待查證標記）、`topics/anthropic-business.md`（Amazon 持股 IPO 估值分析、Anthropic 超越 OpenAI 成熱門新創、OpenAI 安全標準追趕與 Anthropic 營收領先擴大、資料中心 13 億美元信貸）、`topics/enterprise-tool-tracker.md`（新增高盛、OKX 香港存取受限退出列）、`topics/competitor-landscape.md`（OpenAI 隱私保護競爭回應、Startup Fortune 專頁定向定價分析，狀態 monitoring→ongoing）
  - **安全政策**：`topics/anthropic-government-policy.md`（浮水印政策系列追蹤新增 Forbes／WIRED 兩則；高盛/OKX 香港存取受限地緣政治面新增列並標 ❓ 待查證；OpenAI 安全標準敘事記錄，狀態 monitoring→ongoing）
  - **社群**：`topics/community-tech-discussions.md`（Opus 5.0「行話」爭議 HN 181 分＋Reddit 跨平台延燒收錄 🔥🔥🔥🔥；arXiv 擬人化推理痕跡論文；Simon Willison 三篇部落格；真金交易實驗）、`topics/community-tech-patterns.md`（Frugal Tokens、dev.to「Give Up」除錯實錄、Register 印表機驅動報導併入既有節點，狀態 monitoring→ongoing）、`topics/code-quality-decline.md`（「Claude is Losing Me」列為第十則品質感知延續訊號，狀態 monitoring→ongoing）；16 個高星 GitHub Search 新專案因無 web 工具無法完成星數防刷佐證，全數不收錄（含日報已提及的 opencodex／omnigent／guizang-social-card-skill）
  - **主編**：`wiki/feature-radar.md` 彙整功能記者新增條目（詳見上）；`wiki/index.md` 同步四筆狀態變更（anthropic-government-policy／competitor-landscape／community-tech-patterns／code-quality-decline，皆 monitoring→ongoing）；`data/pending-handoffs.jsonl` 新增 2 筆轉知（H-6b16c9 功能→社群、H-21f8e6 功能→安全政策），皆待下次派工處理
- 新增頁面：無
- 摘要：Claude Code v2.1.237 發布（Concise 輸出風格＋prompt caching 修復），同日湧現多筆高互動已知問題（記憶體洩漏、Cowork VM 效能、tool call 解析失敗等）；Anthropic 商業敘事升溫（超越 OpenAI 成熱門新創、Amazon 持股 IPO 估值分析）與浮水印政策/香港存取限制並行；Opus 5.0 用詞風格爭議在 HN／Reddit 跨平台延燒，官方回覆疑似 Claude 代寫引發討論
- 呈現品質：全部通過
- 品質備註：無

📋 收件匣提醒：`wiki/reader-notes.md` 有 2 筆 ⏳ 興趣主題已逾 14 天未處理——2026-08-01（成本感知自動模型路由，19 天，週度回顧持續追蹤中）、2026-07-12（GPT-5.6 vs Claude 第一手評測，39 天，已改被動觸發等日報自然出現數字）。

## 2026-08-21 Ingest | news/2026-08-21.md（56 則）

- 來源日報：[[news/2026-08-21]]（56 則抓取，13/13 來源；日報實收 27 則，另 29 則透過 `list_digest_omissions.py` 一併提供給記者判斷）
- 分類派工：功能 7 則、商業 17 則、安全政策 2 則（另含轉知待接手 1 筆）、社群 25 則（另含轉知待接手 1 筆）、人物 1 則；六類皆以 `subagent_type: general-purpose` + `model: sonnet` foreground 派工，角色前導導向 `.claude/agents/wiki-reporter-[category].md`（正典路徑）；模型類今日無條目，未派工
- 更新頁面：
  - **功能**：`entities/claude-code.md`（新增 v2.1.238「keybindingFlavor」設定與 anthropic-sdk-python v1.0.0 breaking change（httpx2 升級，官方未提供遷移時程）；互動數更新：Cowork VM 於 Windows ARM64/Snapdragon 無法啟動（#40198）累積 68 則留言，新增 API 連線錯誤彙整已知問題（#4297，48 則留言）；MCP Apps（HN 2 分）未達門檻不收錄）；feature-radar 新增「anthropic-sdk-python 1.0.0」（🔥🔥🔥）與「keybindingFlavor readline 模式」（🔥🔥），並由主編同步全覽表列與升版風險最新版本行
  - **商業**：`entities/pricing.md`（新增資料保留政策傳聞、企業自有雲端存放傳聞、token 配額變動回報三筆，均標「⚠️ 需主編查證官方說明中心」）、`topics/anthropic-business.md`（IPO 傳聞：規模傳比肩 SpaceX、可能本月遞交文件；Ode 收購 Casper Studios 三方報導）、`topics/competitor-landscape.md`（OpenAI 業務追趕 Anthropic＋零資料保留反制；Slack Code 讓 Claude／ChatGPT 同駐頻道）；KuCoin／36Kr／Morningstar／ETF Trends 四則低品質來源未收錄
  - **安全政策**：`topics/anthropic-government-policy.md`（EU AI Act 浮水印系列追蹤新增 Business Chief／CNET 兩則，內容為既有系列重申、無新機制細節，誠實標註未虛抬訊號）、`topics/ai-agent-safety.md`（處理轉知 H-21f8e6：Claude 未經詢問直接發送 Gmail 郵件〔Mashable/Android Police 08-19 報導〕收錄為 agent 自主權限擴張風險，標 ❓ 待查證待補功能面規格；同步修剪現況段落回 2 段避免時序侵蝕）
  - **社群**：今日條目全數未達收錄門檻，未修改任何頁面——3 筆 GitHub Search 高星工具（640★/631★/511★）因 source_count=1 且無 fork/issue/commit 佐證可查核，標「待查證」不收；9 則 Show HN 分數 2–7 分未達低門檻；10 則 Reddit（r/ClaudeCode 6 則、r/LocalLLaMA 4 則）皆單一來源、score 不可信、無跨平台延燒佐證不收；GLM 5.3 benchmark 因未含與 Claude 的直接比較排除；Simon Willison 兩則與 Claude/Anthropic 無直接關聯排除
  - **人物**：「The woman behind Anthropic's CEO」（calcalistech.com）僅標題可用、無姓名/事件/引述可查證，且屬個人生活側寫非公開聲明/政策立場，判定資訊不足不寫入 `entities/dario-amodei.md`，未修改任何頁面
  - **主編**：`wiki/feature-radar.md` 彙整功能記者新增條目（詳見上，含全覽表列與升版風險最新版本行同步，另補注 SDK breaking change 為獨立產品面風險）；`data/pending-handoffs.jsonl` 結案 H-21f8e6（功能→安全政策，已處理，安全政策記者已收入 ai-agent-safety）；H-6b16c9（功能→社群）維持待接手，社群記者確認屬 `community-tech-tools.md` 週更範圍，今日不動作
- 新增頁面：無
- 摘要：Claude 服務今日一度發生多模型請求錯誤與 Google connectors 中斷（皆同日解決）；Anthropic 傳出 IPO 前置訊號（規模傳比肩 SpaceX、可能本月遞件）與企業資料保留政策擬異動（路透／彭博，未經官方證實）；Anthropic 關聯企業 Ode 收購顧問公司 Casper Studios；anthropic-sdk-python 發布 1.0.0 含 httpx2 breaking change；Claude 未經詢問直接發送 Gmail 郵件的 agent 自主權限議題收入 ai-agent-safety；社群面今日無條目達收錄門檻
- 呈現品質：全部通過（`topics/ai-agent-safety.md` 摘要段落當場修剪回 2 段，屬例行維護，非缺陷）
- 品質備註：無

## 2026-08-22 Lint（雲端排程執行）

- 修正矛盾：`topics/anthropic-government-policy.md` Tom Brown 接管白宮談判日期誤植 2026-06-24 → 更正為 2026-06-25（依日報原文 `news/2026-06-25.md`，並與 `entities/tom-brown.md`／`entities/dario-amodei.md` 一致），修正時序表列＋正文兩處敘述＋詳述段兩則引用日期；由人物記者 3a 跨頁檢查發現、主編直接執行（安全政策記者已先行完成派工未及知悉）
- 補連結：無（六類記者逐頁 Grep 確認，全數頁面皆有 inbound wikilink，無孤立頁）
- 狀態更新：`topics/official-community-gap`（monitoring→ongoing）、`topics/enterprise-cost-management`（monitoring→ongoing）、`topics/ai-talent-flow`（monitoring→ongoing）、`topics/recursive-self-improvement`（monitoring→ongoing）——四頁皆為 3c 回升邊：最後新聞更新距今 ≤14 天但狀態仍停在 monitoring，本輪回升
- resolved 收尾：無
- 新增 entities：無（Step 4 掃描候選 Decart／Casper Studios／Ode／Cami Clark 均未達「3+ 頁提及且有足夠獨立內容」門檻，維持現況：於 `anthropic-business.md`／`dario-amodei.md` 內文覆蓋即可，不建頁）
- 呈現品質：模型 5/8 頁 ⚠️已修復（懸置標記舊語法改新語法）、功能 1/14 頁 ⚠️已修復（official-community-gap 狀態回升）、商業 全部✅、安全政策 1/6 頁 ⚠️已修復（浮水印標記訊號日同步）、社群 1/7 頁 ⚠️已修復（patterns 補漏填主線 tag）、人物 5/14 頁 ⚠️已修復（移除 LLM 操作語句殘留）
- 入口層健檢：`entities/claude-code.md`（661行）、`topics/coding-workflow-guide.md`（608行）、`entities/pricing.md`（642行）、`topics/anthropic-business.md`（669行）、`topics/competitor-landscape.md`（582行）、`topics/ai-agent-safety.md`（985行）、`topics/anthropic-government-policy.md`（593行）、`topics/community-tech-patterns.md`（1522行）、`topics/community-tech-discussions.md`（1250行）——九頁均已具備入口層（callout＋概覽表/月份分組），無需補結構；未發現語意分岔或死案候選，Step 3 本輪跳過
- 待查證回訪：已改註「日報無後續、官方未查證」共約 15 筆（模型 6 頁×多筆舊語法標記改新語法、安全政策浮水印標記訊號日更新、人物既有新語法標記逐筆核對均無新後續）；社群／功能／商業／安全政策另有多筆新語法標記核對後維持原狀不動（詳見各記者回報）
- 規則檔健檢：
  - 矛盾（6a）：本輪掃描與六位記者回報均無新增規則矛盾發現
  - 引用驗證（6b）：7 個錨點（首次出現欄／##痛點洞察／近期工具欄／##技術彙整／熱門討論表格／衍生欄／全覽表）逐一 grep 確認全部存在，全部通過
  - 遵守率（6c）：抽樣近 3 次 ingest（08-19／08-20／08-21）——呈現品質審查 3/3、feature-radar 更新提及 3/3、log.md 格式正確 3/3，全部通過（近期無新工具收錄事件，痛點洞察同步規則本輪無樣本可測）
  - 過期規則（6d，>60天）：10 條規則超過 60 天閾值，📋 待使用者確認是否仍準確——`entities/`頁面格式模板／`topics/`頁面格式模板（119天）、Wiki頁面呈現品質標準（99天）、community-tech-patterns↔discussions雙向連結規則（98天）、enterprise-tool-tracker更新規則（88天）、feature-radar准入定義（68天）、anthropic-government-policy更新規則（65天）、community-tech-tools策展規則（64天）、命名與分類規則（72天）、community-tech-discussions熱門討論保留規則（63天）
  - 來源健康（6e）：近 7 天（08-15～08-21）sourceStatus 全部 `ok=true`，社群/媒體來源（HN／Reddit／Google News／GitHub／GitHub Issues／dev.to／Blogroll）均無連續 3 天 count=0，全部正常；記分卡（`source_scorecard.py`）觀察名單：GitHub（Wilson下界21%／Presence 6%，樣本充足但雙低）、dev.to（Wilson下界16%／Presence 3%，另有跨日重複視窗結構性偏低註記，僅供趨勢觀察），📋 待使用者確認是否列入長期觀察；Google News 低信譽桶 0 筆；⚠️ 未註冊 slug `business-chief`（安全政策記者 08-21 誤用媒體名作為 slug，應為 `google-news`），📋 待使用者確認是否修 registry 或提醒記者
  - 跨檔案語意矛盾（6f）：`scripts/check_rules.py` 54 組 sync_pairs 機械檢查全數 ✅ 通過；本輪六記者回報均無「⚠️ 派工與規則牴觸」；額外發現 12 組高頻互引但未登記的 coupling hints（warn-only，非阻塞，資訊性提示）——✅ 全部配對語意一致，無新增矛盾
  - 成長迴路（月度）：非本月首次 lint，跳過（本月已於 08-01 執行過首次 lint）
- 品質指標（6g）：
  - ref 覆蓋率（每週）：100%（08-16~08-21，25 條列/25 有歸因；08-22 當日 news 檔案尚未產出不計入分母）→ ✅ 通過
  - 採用驗證率（月度）：非本月首次 lint，跳過
  - 外部死鏈（每週，讀 `data/link_health.json`）：checked_at 2026-08-21（新鮮，<10天）；共 4 條死鏈，已由對應類別記者標「（原文已失效）」共 4 頁（`feature-radar-archive-2026-05`／`topics/coding-workflow-guide`／`topics/anthropic-business`／`topics/community-tech-patterns`）；anti_bot 186 筆／unverified 40 筆依規則不派工不標註，僅列入指標
  - 趨勢判讀：持平（連續 5 期 ≥97%：07-26 97%／08-08 100%／08-15 100%／08-22 100%）
- 跨家榜單週更（5b）：雲端 egress 封鎖，跳過（`topics/model-task-leaderboard` 最後新聞更新已距今 17 天但模型記者判斷為抓取管道被擋、非議題沉寂，本輪維持 ongoing 不下修，理由詳見模型記者附註）
- 逾期待查證清算（5c）：雲端 egress 封鎖，跳過，留待本機執行
- 讀者模擬：3 題全數 ✅ 2 跳內找到答案——①「anthropic-sdk-python 1.0.0 breaking change 是否影響我？」→ index→`entities/claude-code.md` 現況段已直接列出 httpx2 影響範圍與 changelog 連結；②「多 agent 可觀測性儀表板化社群驗證結果如何？」→ index→`topics/community-pattern-trends.md` 趨勢六段落已有六個實作與啟示；③「Anthropic IPO 進展到哪？」→ index→`topics/anthropic-business.md` callout 已有規模傳言與遞件時程
- lint 自我遵守率：6/6 位記者回報一次過，3a–3g 七項均有明確結果，無退回
- overview.md：已更新（反映本週局勢：IPO/ARR 650億美元、Opus 5.0行話爭議、v2.1.237/238發布、SDK breaking change、服務穩定性事件、浮水印延燒、多agent互相破壞研究、Decart收購案上修至70億、規格驅動開發與行動裝置遠端控制兩條社群趨勢）

📋 待使用者確認：
1. **`community-tech-patterns` 模式淘汰審查**（社群記者 dry-run，未執行）：建議淘汰 1 條「跨 Session 通訊插件 `/qu /ans`」（2026-05-07，已被官方 08-09 正式推出的 `ListAgents`／`SendMessage` 完全取代）；建議拆分 1 條「Session 記憶與搜尋工具生態」（內「多 session 互通 Claude Relay」子條目同樣被取代，`Claude-Find`／`Memex` 兩子條目應保留）；另有 2026-05 月份 39 個舊格式節點缺少「成熟度」欄位，機械化 60 天沉寂判準無法套用，建議後續補標欄位再審（僅觀察，未列入淘汰候選）。❓ 是否同意執行淘汰／拆分？
2. **規則年齡審查（6d）**：10 條規則已超過 60 天閾值（詳見上方「規則檔健檢」欄清單），是否需要逐條確認內容仍準確？（多數為格式/命名類穩定規則，過去數輪 lint 已複查過部分項目）
3. **來源記分卡觀察名單（6e）**：GitHub、dev.to 兩來源 Wilson 下界與 Presence 雙低，是否需要調整收錄門檻或列入長期觀察名單？
4. **未註冊 slug `business-chief`（6e）**：安全政策記者 08-21 引用 Business Chief（Google News 轉載）時誤用媒體名作 attribution slug，正確應為 `google-news`。是否需要修正 `data/source_registry.json` 或在下次派工提醒記者？（單筆，非結構性問題，可視情況延後處理）

## 2026-08-22 Weekly（W34）：週報＋週度延伸回顧＋本機專屬步驟補跑

### 步驟 0：本機專屬步驟補跑（`/weekly` 首次承接）

- **5b 跨家任務榜單週更**：派 Haiku 抓 18 個榜，`wiki/topics/model-task-leaderboard.md` 全表覆寫（上次更新 2026-08-05，停更 17 天，本步驟即為其唯一觸發邊）。本週異常：SWE-bench Verified 三甲全 ≥95% 已近飽和；Terminal-Bench 兩組來源 harness 不同、分數不可跨表比，並陳不擇一；**Aider Polyglot 連續 2 週停更（榜首仍為 2025-11 陣容），依 5b 規則標記並建議下週汰換該列**；AA 系列四榜頁面未載快照日期，以抓取日標示。已解除的舊註記：TTS 與音樂兩榜上週「待補」本週均取得，EQ-Bench 兩來源歧異本週未再現。
- **5c 逾期待查證清算**：`check_pending_markers.py --queue` 回報**總逾期數 0**，但輸出末尾「⚠️ 舊語法盲區 **94 筆**」——前三頁為 `entities/claude-code`（20）、`topics/ai-agent-safety`（19）、`topics/anthropic-government-policy`（12）。**佇列空而存量 94，正是本步驟要防的餓死型態**，故本輪額度改花在盲區手挑，處理 5 筆：
  1. ✅ **查實**｜Fable 5／Opus 5 是否共用週用量池（08-15 起懸置，主編待辦）→ 官方確認**共用同一池**，「Fable 5 最多用到週用量 50%」是池內天花板而非額外配額。寫入 `entities/pricing`
  2. ✅ **查實**｜Fable 5 過渡 credit 金額與到期日（原 🔎 查無官方）→ $100／Pro 每帳戶、Team 每 standard seat $100 且每組織上限 $2,500；領取窗 2026-08-02 已關、已領者 2026-09-17 到期、不限 Fable 5
  3. ✅ **查實**｜Claude Code +50% 週用量促銷 → 官方確認延長至 2026-08-31、自 2026-05-13 起跑、**不影響 5 小時窗**、Free 與消耗制 Enterprise 席位不適用
  4. ✅ **查實**｜GitHub #78431 User-Agent 洩漏 email（原 ❓ 待查證「真實性存疑」）→ 直查 issue 確認**事件為真**：已補 v2.1.212／macOS／IntelliJ 可重現條件，回報者標為回歸，官方已掛 `bug`／`area:security` 標籤；仍 open、無 assignee、無官方回覆、無修復版本 → 改標 🔴 未修復
  5. ⚠️ **查證未果**｜analyticsindiamag〈Almost Nobody Is Using Anthropic's Fable 5〉→ 文章存在但正文抓不到，無採用數據可查證，維持懸置
- **結案回掃**：拿探針字串回掃全庫，上修 **3 頁**——`topics/ai-agent-safety`（#78431 該條同步改 🔴 並補查證條件）、`entities/fable-5`（過渡 credit 補官方金額與日期）、`entities/pricing`（媒體數字段落上修為官方查證）。同步修正 `entities/claude-code`「安全與隱私」組頭統計（1 條待查證 → 0，未修復 10 → 11）
- **lint 待裁示呈報**：已於本次輸出直接呈給使用者（不只寫進本檔），見下方「呈報使用者的積壓事項」

### 步驟 1：週報

- 產出 `weekly/2026-W34.md`。深挖題目：**〈你到底撞到哪一道牆——Claude Code 用量上限的四層結構〉**（5 小時窗／週上限／池內天花板／usage credits），機制層引官方說明中心四份文件（均 08-22 取得），與步驟 0 的 5c 查證同源
- 帳本：`check_weekly_ledger.py` ✅ 回收 7 筆全數到位、判準無改寫、新開 4 條均帶查證線索。結案 3（模型釘選升為長期警示／浮水印去除標未證實／Max 配額併入靜默降級線）、續盯 4
- **⚠️ 深挖 1,523 字，超出 800–1,200 規格**（機械檢查為提醒不擋）。已兩輪壓縮（2,387 → 1,908 → 1,523），再壓會開始刪掉規格自己要求的具名可驗證物與來源 URL。**建議下次校準時檢討該字數上限是否需含 URL 字元**——W33 為 1,228 亦超標，連續兩期超標指向規格與實作有落差，而非單期失手
- 涵蓋窗誠實揭露：本期只有 `news/2026-08-17`～`08-19` **3 份日報**（08-20 之後尚未產出），續盯條的「本週零命中」須照此折扣理解

### 步驟 2：週度延伸回顧

- 六記者並行判斷（general-purpose ＋ sonnet），提出 5 項候選；**聚焦校準：本月已於 08-01 執行（`wiki/metrics.md` 聚焦命中率欄有 76% 數值），跳過**
- 延伸：使用者確認執行 **2 項**
  - **B｜subagent 型別差異 ＋ MAS 缺口對照（併案）**——`entities/claude-code` 新增「Subagent 型別差異對照」四軸表（內建／自訂／plugin、fork／非 fork、background／foreground、teammate／非 teammate）；`topics/community-tech-patterns`「學術對照」節新增「缺口追蹤：文獻主張 × Claude Code 現況」子表（已補 2／未補 5／倒退 1）。兩頁互加 wikilink（主編補上 `claude-code` → patterns 錨點連結那一側）
  - **C｜浮水印政策子區塊化**——`topics/anthropic-government-policy` 872 字元儲存格瘦身，敘事改由獨立子區塊承接
- 使用者跳過項目 **3 項**：(A) patterns 補「agent session 觀察／管理工具集群」彙整節點；(D) `entities/opus-5` 信任度／穩定性彙整子節；(E) `topics/anthropic-business` 著作權／專利訴訟子區塊化
- **主編更正記者判斷 1 處**：社群記者建議為本週六款 session 觀測工具「新增趨勢區塊」，但 `topics/community-pattern-trends` 已有「趨勢六：多 Agent 可觀測性儀表板化」（live-log-viewer-next → Topsoil → Fleet Deck → Cockpit → Wallfacer → HUD），本批應為該趨勢的**新節點**而非新趨勢。因 (A) 未獲採納，本輪不動；留給 lint 週更
- `wiki/reader-notes.md` 收件匣消費：08-20 兩條同源 ⏳ 🔍 標 ✅（併案執行，未各自開頁，符合該檔原文要求）；其餘 4 條 ⏳ 維持；📌 📓 雜記 0 筆，無逾 30 天需清除者
- **未竟**：`community-tech-patterns` 學術對照節的 8 月新論文仍需主編層 WebSearch 查證補入（記者無 web 工具，本輪僅升級呈現結構未增文獻）

### 收尾時的更正（推送前發現）

- **雲端 `weekly-wiki-lint-cloud` 與每日 pipeline 於本次執行期間同時推送**，收尾 push 遭拒 → `pull --rebase` 後六檔衝突（claude-code／pricing／ai-agent-safety／anthropic-government-policy／community-tech-patterns／log）。標頭與 callout 類衝突一律取雲端側（其新聞內容較新，含 08-20／08-21 ingest），本次新增的區塊與查證結果全部保留並逐項驗證存活；`log.md` 為 append-only，兩側條目皆保留、依日期排序。web build commit 因純產物衝突改為 skip 後重跑 build
- **`news/2026-08-20`／`08-21` 在週報寫完後才隨 rebase 進入本機**。週報依步驟 5 凍結原則不回頭改選題與深挖，但**補掃了預告探針**，命中 1 則具實質影響者：**WIRED（08-20）〈Coders Say They Already Found Workarounds to Claude's Invisible Watermarks〉**——該則推翻了「可去除浮水印」一列初稿寫的「無人復現」，已由 ✅ 結案改判 🟡 續盯至 W35，並在該列與檔尾標明更正緣由
- **可攜教訓**：本機 session 開工時的 `news/` 快照，不等於該週實際存在的日報。`/weekly` 步驟 1 的涵蓋窗是在**開工當下**盤點的，而雲端 pipeline 會在執行期間繼續產出——若不在收尾 push 前重掃一次，週報會以「這幾天沒有日報」的語氣，對實際存在的新聞下「本週零命中」的判定。**建議把「收尾前重掃涵蓋窗與預告探針」寫進 `.claude/commands/weekly.md` 步驟 3**，成本是一次 grep，擋掉的是對讀者說謊

## 2026-08-22 Ingest

- 來源日報：[[news/2026-08-22]]
- 更新頁面：wiki/entities/mythos.md、wiki/entities/claude-code.md、wiki/entities/claude-security.md、wiki/topics/anthropic-business.md、wiki/topics/competitor-landscape.md、wiki/entities/pricing.md、wiki/topics/anthropic-government-policy.md、wiki/topics/ai-agent-safety.md、wiki/entities/dario-amodei.md、wiki/topics/community-tech-patterns.md、wiki/topics/community-tech-discussions.md、wiki/feature-radar.md（主編彙整：Claude Security 熱度 🔥🔥🔥→🔥🔥🔥🔥［source_count 4：MarkTechPost／Dealroom／Palo Alto Networks Unit 42／The New Stack］、「最新版本」更新為 v2.1.239）
- 新增頁面：無
- 摘要：Anthropic IPO 估值傳聞升溫至 1000 億美元並將「AI 反彈情緒」列為風險因素、Claude Mythos 5 整合進 Claude Security 資安產品（承諾 3500 萬美元額度）、延攬前 Google 晶片工程師釋出自研硬體訊號，以及多筆 GitHub Issues 集中回報用量配額異常耗盡（Max 訂閱累積 1488 則留言）
- 呈現品質：六位記者皆回報 ✅ 通過，其中功能記者於 `entities/claude-security.md` 發現「現況」段落與歷史記錄重複，已依「現況不被時序侵蝕」規則修復；全部通過（含 1 項已修復）
- 品質備註：無

**跨記者轉知（已登帳，待下次派工帶入）：**
- H-201d81：社群→功能，patterns 新增 OzBrain 對應 `official-community-gap.md`「跨 session 記憶歸零」矩陣列，評估是否列入
- H-b7c4f2：安全政策→商業，Forbes（08-21）浮水印企業影響報導，`topics/anthropic-business.md` 商業面內容待補

**主編判斷備註：** 功能記者另標「⚠️ 需主編轉知模型記者：entities/mythos.md 補充 Mythos 5 整合進 Claude Security 事件」——經核對，模型記者本輪已獨立處理同一事件（現況／時序均已寫入 `entities/mythos.md`），為兩記者依各自角色檔觸發條件對同一跨類別事件的預期重疊覆蓋，非缺漏，未另開轉知帳目。

## 2026-08-23 Ingest

- 來源日報：[[news/2026-08-23]]
- 更新頁面：wiki/entities/opus-5.md、wiki/entities/claude-code.md、wiki/topics/official-community-gap.md、wiki/topics/anthropic-business.md、wiki/topics/enterprise-tool-tracker.md、wiki/topics/competitor-landscape.md、wiki/topics/ai-talent-flow.md、wiki/topics/community-tech-discussions.md、wiki/feature-radar.md（主編彙整：同步「最新版本」行為 v2.1.241）、wiki/index.md（主編彙整：新增 amir-salek 列）
- 新增頁面：wiki/entities/amir-salek.md（Anthropic 延攬前 Google 自研晶片計畫創辦人，待核實）
- 摘要：Anthropic IPO 準備話題十餘家媒體同日圍繞估值（Motley Fool／Yahoo Finance「Dean of Valuation」1.2兆美元營收門檻）、風險揭露（CNBC「AI 反彈情緒」列為風險因素）與獲客能力（FT）多角度報導；Claude Code 疑似 A/B 測試調降 effort 顯示方式，官方 Thariq 具名澄清使用者實際選擇的 effort 未變；CVP 已核准企業仍遭資安防護誤擋（GitHub Issue 141 留言，今日全站已知問題互動最高）；Anthropic 延攬前 Google 自研晶片計畫創辦人 Amir Salek，人物與商業面雙記者並行記錄
- 呈現品質：六位記者（模型、功能、商業、社群、人物；安全政策今日無條目未派工）皆回報 ✅ 通過，無需修復項目
- 品質備註：無

**跨記者轉知（已登帳，待下次派工帶入）：**
- H-2fc0ba：社群→功能，SkillWorks（第三方索引工具）08-23 揭露 Claude Skills 生態規模統計（503,570 listings、48,190 個 skill 無法載入等），對 `entities/claude-skills.md` 可能有參考價值，社群記者無權代寫功能頁

**本次結案轉知：**
- H-201d81（08-22 開立）：功能記者已處理——OzBrain 列入 `official-community-gap.md`「跨 session 記憶歸零」矩陣列代表社群工具欄
- H-b7c4f2（08-22 開立）：商業記者已處理——Forbes 浮水印企業實務影響已補入 `anthropic-business.md`「商業風險」表

**主編判斷備註：** 人物記者查證後判斷 Palantir CEO Alex Karp 相關言論（HN 15 分，連回 08-03 CNBC 舊文）不建新人物頁——同一事件已於 `topics/anthropic-business.md`、`topics/competitor-landscape.md` 收錄，且 2026-08-10 已有記者做過相同「不足以建頁」判斷，屬既有覆蓋範圍內的重新浮現，非新事件；商業記者亦同步採納相同判斷、未重複記錄。

## 2026-08-24 Ingest

- 來源日報：[[news/2026-08-24]]
- 更新頁面：wiki/entities/mythos.md、wiki/topics/model-comparison.md、wiki/entities/claude-code.md、wiki/entities/claude-skills.md、wiki/topics/official-community-gap.md、wiki/topics/ai-agent-safety.md、wiki/topics/anthropic-business.md、wiki/topics/ai-talent-flow.md、wiki/topics/competitor-landscape.md、wiki/topics/community-tech-patterns.md、wiki/topics/community-tech-discussions.md
- 新增頁面：無
- 摘要：Claude 多款模型今日一度出現錯誤率上升（04:50–07:36 UTC，已解決）；Anthropic 擴大 Mythos 5 防禦端存取並成立 3,500 萬美元開源資安基金；Claude Code 出現高互動凍結／卡住 bug 回報（150 reactions）與多筆桌面版功能請求；中國媒體《36氪》單一來源、無法查證的「Claude 推理能力遭秘密降低」聳動報導以待查證方式記入，未寫成事實；TechRadar 專題報導多個 Claude agent「地盤爭奪、部署自我複製惡意程式」，同樣因僅標題可用、無實驗細節而以待查證處理
- 呈現品質：五位記者（模型、功能、安全政策、商業、社群；人物今日無條目未派工）皆回報 ✅ 通過，無需修復項目
- 品質備註：無

**跨記者轉知：**
- 派工前 `pending_handoffs.py list` 僅 1 筆積壓（H-2fc0ba，2026-08-23 由社群記者轉知功能記者），未逾 14 天，本次已隨功能記者派工帶入並處理

**本次結案轉知：**
- H-2fc0ba（08-23 開立）：功能記者已處理——SkillWorks 第三方生態規模統計已以「訊號待驗」方式加入 `entities/claude-skills.md`

**主編判斷備註：** 今日多達 12 則條目（Anthropic Status 官方事故公告 + 11 則媒體跟進報導）圍繞同一起服務錯誤率上升事故；因無專屬頁面追蹤一般性服務中斷（非安全漏洞、非產品功能缺陷），主編判斷不逐則路由六記者分類，僅由官方狀態頁條目留存於當日日報「技術更新」區塊，不另立 wiki 頁面或事件記錄。36氪與 TechRadar 兩則聳動報導在派工訊息中已明確提示「Google News RSS 僅標題可用、無完整內文」，兩位記者（模型、安全政策）皆採納謹慎處理、以標準待查證語法記入而未寫成既定事實，為預期中的正確處置。

## 2026-08-25 Ingest

- 來源日報：[[news/2026-08-25]]
- 更新頁面：wiki/entities/claude-code.md、wiki/entities/dario-amodei.md、wiki/topics/ai-agent-safety.md、wiki/topics/anthropic-business.md、wiki/topics/anthropic-government-policy.md、wiki/topics/code-quality-decline.md、wiki/topics/community-tech-patterns.md、wiki/topics/community-tech-discussions.md、wiki/topics/enterprise-tool-tracker.md、wiki/topics/enterprise-cost-management.md、wiki/feature-radar.md（主編彙整：同步「最新版本」行為 v2.1.245）
- 新增頁面：無
- 摘要：Anthropic 宣布將為 Claude 工具生成的內容加上浮水印（媒體報導，與既有浮水印爭議系列報導並陳、無新機制細節）；Claude Code GitHub Issue #60705（模型行為模式爭議，含 stop-hook 指令被引為未經授權動作依據）與 #50246（訊息佇列模式功能請求）互動量雙雙創新高（137、67 則留言）；一批鎖定 codebase 理解與長期記憶的社群開發工具同日於 GitHub 亮相（Graft、the-startup、brain.md 等）；Anthropic IPO／估值報導延續多日熱度，同日出現「遜於 SpaceX」與「可能超越 SpaceX IPO」兩種相反論點，並陳收錄；三星證實用 Claude Code 輔助晶片設計但坦言仍有明顯錯誤、Thomson Reuters 傳出降低對 Claude 依賴，反映企業採用出現分歧訊號
- 呈現品質：六位記者皆回報 ✅ 通過（安全政策記者處理 Firstpost「中國駭客用 AI」條目時，因原文僅標題、且該則本身未通過日報收錄門檻，先草擬後複核撤回，判斷正確，非品質問題）
- 品質備註：無

**跨記者轉知（已登帳，待下次派工帶入）：**
- H-70d575：商業→模型，Fierce Healthcare（Epic UGM）報導提及 Project Glasswing 進展，題材屬 `entities/mythos.md` 範疇但僅標題可用，待模型記者查證後續報導補列
- H-f82d69：社群→功能，今日新增技術模式（ambient-context 螢幕記憶、mindmuxai/brain.md、rsmdt/the-startup、Kindle highlights OCR skill）待功能記者評估是否需在 `official-community-gap.md` 產品化矩陣新增對應列

**主編判斷備註：** 延續 2026-08-24 已建立的先例，今日日報中 4 則一般性服務中斷／已修復事故條目（Anthropic Status 登入異常、PCMag Australia／analyticsindiamag.com／Tech Times 三則媒體跟進報導「近期已發生多次中斷」）因無專屬頁面追蹤一般性服務可靠性議題（非安全漏洞、非產品功能缺陷），主編判斷不逐則路由六記者分類，僅保留於當日日報「📌 今日聚焦」與「📰 媒體報導」區塊。社群記者對 GitHub Search 條目 `trailhq/Graft`（4,842 星）依星數防刷規則判定證據不足、不收錄（區別於既有 08-15 已收錄的 `NanoNets/Graft`，同名不同專案），為正確的謹慎處置。
## 2026-08-25 Query：「週報頭條如何讓讀者更清楚」→ 頭條敘事規格從一行擴為四層十一條（W35 起生效）

- **提問**：使用者請從讀者角度 review 週報，聚焦頭條敘事的 prompt 補強；先派三個 sonnet agent（新聞學／冷讀者實測／結構裝置）、再派 Fable＋Opus 各深想一層，五份產出合併取捨。
- **診斷根因**：頭條敘事規格只有一行（「當週最大張力縫成因果敘事，300–500 字，不列清單」），風格實際來自逐期模仿前作——防重複規則管題目不管修辭，於是 W33/W34 收束句逐字級同構、連兩期從財經視角開篇、同一事件全篇六種說法、一段六個無角色詞金額。
- **處置**：`weekly-report.md` 第 (1) 段擴為四層——結構層（入口讀者裁定／編線准入／頭條-深挖分工）、連載層（前情錨＋增量／固定稱呼）、句子層（收束預算禁隱喻／跨期句式 diff／數字角色詞／日期位置／粗體預算＋案例定性）、驗收層（冷讀者三問：每答必須可逐字 grep 回頭條原文）；全部附 W33/W34 實文正反例。機械檢查五項入 `scripts/check_weekly_ledger.py` 新增 `check_headline()`（跨期模板／日期句首／粗體數量硬擋，日期遞增／角色詞 WARN），以 `HEADLINE_RULES_SINCE = 2026-W35` 閘門凍結舊期不回溯；+5 測試；registry 加兩組同步配對防規格與檢查器失步。
- **淘汰紀錄**：三線摘要表（違反「不列清單」的訓練意圖）、腳注全面化（破壞敘事文體區隔）、段落骨架標籤（零增益）、TL;DR 框（與「本週一句話」重疊）——agent 自砍與主編合議，留檔防止日後重提。

## 2026-08-26 Ingest

- 來源日報：[[news/2026-08-26]]
- 更新頁面：wiki/entities/opus-5.md、wiki/entities/fable-5.md、wiki/entities/claude-code.md、wiki/topics/official-community-gap.md、wiki/topics/anthropic-business.md、wiki/topics/enterprise-tool-tracker.md、wiki/topics/competitor-landscape.md、wiki/topics/ai-agent-safety.md、wiki/topics/code-quality-decline.md、wiki/topics/community-tech-discussions.md、wiki/feature-radar.md（主編彙整：新增「Cowork 記憶功能整合」條目＋全覽表列，同步最新版本行至 v2.1.246）
- 新增頁面：無
- 摘要：Claude Cowork 與網頁／App 對話正式共用記憶（官方 Release Notes＋多家媒體同步報導）；Anthropic 傳出將向投資人簡報稱潛在市場規模上看 30 兆美元、為可能創紀錄 IPO 鋪路，社群與評論界對此說法不乏質疑（TAM 非實際營收、「$30 兆幻想」等）；Claude Code 與外部生態摩擦浮上檯面（Shopify CEO 揚言封殺、AGENTS.md 業界標準遭拒引發開發者反彈）；GitHub Issues 熱度集中在四項功能／臭蟲請求（多帳號切換 879👍、Bedrock 後端 243👍、extended-thinking 恢復失敗、1M context 無法關閉）；社群對「Claude Code 是否正被 A/B 測試降規模」的質疑（nerfd models）與作者親身經驗（今昔對比、實測抓到人工漏掉的 bug）並陳收錄
- 呈現品質：六位記者皆回報 ✅ 通過
- 品質備註：無

**跨記者轉知：**
- 派工前 `pending_handoffs.py list` 有 2 筆積壓（H-70d575 商業→模型，2026-08-25 開立；H-f82d69 社群→功能，2026-08-25 開立），均未逾 14 天，本次已隨對應記者派工帶入處理
- 模型記者：H-70d575（Project Glasswing／mythos.md）判斷「不適用」——今日日報無相關後續報導，保留 open 待下次查證（非理由「不屬我」，僅無新證據，不 void）
- 功能記者：H-f82d69 已 `close`——ambient-context／mindmuxai-brain.md 併入 official-community-gap.md 既有「跨 session 記憶持久化」列；rsmdt/the-startup、Kindle highlights skill 判定不新增列
- 商業記者新開一筆轉知：H-1be92f（商業→安全政策），ABC News〈Internal emails expose scale of Anthropic's Australian AI plans〉僅標題可用，可能涉政府合作內容，已於 anthropic-business.md 戰略合作表記錄「歸屬待定」，待安全政策記者查證是否屬 anthropic-government-policy.md 範疇

**人物記者判斷備註：** 今日兩則外部人物條目（Shopify CEO Tobi Lütke 揚言封殺 Claude Code；創投人 Chamath Palihapitiya 質疑 Anthropic $2兆 IPO 前景）均因「僅標題可用、無可查證的具體發言內容」且內容實質屬商業類別議題（企業工具追蹤／IPO 敘事），判定不建人物頁、不適用，為正確處置——避免用不具引用價值的標題湊出人物頁「核心論述」。

**主編判斷備註：** Anthropic 舊金山辦公室因保全人員可能罷工要求員工居家辦公一事，原始報導已於 2026-08-25 由 Business Insider 首發並進入前一日日報；今日僅為 Hacker News 高分討論（121 分）延續同一事件，商業記者判斷不另立新事件（非融資/收購/戰略合作），社群記者今日條目節錄中亦未見對應收錄，均為正確處置，避免同一事件重複計入多頁。「$30 兆潛在市場」系列報導口徑不一（IPO 估值 $2 兆 vs. 市場總量 $30 兆）已在商業記者派工節錄中明確提醒不可混用，anthropic-business.md 更新時已並置區分。

---

## 2026-08-26（Query／主編查證：逾期懸置清理）

**觸發：** 使用者指出今日網站未更新。查得日報與 wiki ingest 均正常，實為 `run_tests.py` 因一筆探針語法 FAIL、`gate_web_build` 擋下 build_web。使用者續指示清理測試輸出中的逾期複查警告。

**A. web build 被擋的根因與防再犯**
- `wiki/entities/fable-5.md` 懸置探針寫成 `$1,125 Gap`，`PROBE_SPLIT_RE` 把千分位半形逗號當分隔符，切出 `$1` 觸發「英數探針需 ≥ 4 字元」FAIL
- 處置：探針改為 `tech-insider.org、GPT-5.6 Sol`；`scripts/pending_markers.py` 的分隔符改為 `[、，]|(?<!\d),(?!\d)`，數字之間的半形逗號不再視為分隔符

**B. 逾期懸置清理（22 天以上者 10 筆，全數結案；剩 39 筆均為 0–2 天正常到期）**

| 頁面 | 逾期 | 處置 |
|---|---|---|
| entities/opus-4-7 | 104 天 | 取得 arxiv 2604.24827v2 全文：論文**未給** Opus 4.7 參數估算，Figure 1 列的是 Opus 4.6 ≈1.6T／Sonnet 4.6 ≈766B／Haiku 4.5 ≈28B。本頁原記「4.7 ≈4T、4.6 =5.3T、屬降規」**查無出處且算式不成立**，改為 🔎 查無官方並更正；同一組數字在 `topics/code-quality-decline` 的引用一併上修 |
| entities/mythos ×2 | 49／45 天 | Z.Ai GLM-5.3 CyberGym 84.5% vs Mythos 5 83.8%、ExploitBench 54.4% vs 78.0%（08-14 自行公布）；360 Tulongfeng 累計 3,432 漏洞、105 經中國官方確認。均未經獨立驗證，改寫為事實敘述並保留該性質 |
| entities/sonnet-5 ×2 | 41 天 | 官方 2026-06-30 changelog 更正 BrowseComp 圖表（原圖未套用標準 agentic-search 方法論，新圖用 system-card 設定）。換版屬實、官方理由可稽，結案 |
| entities/fable-5 | 41 天 | 化學拒答經 The Verge／Anthropic 發言人證實非孤例：護欄刻意過度保守、平均 <5% session 觸發，官方已承認取捨錯誤並承諾放寬。攔截範圍確認不限 coding/cybersecurity |
| entities/sonnet-5 | 34 天 | Mashable 07-09「正式發布」為遲到報導（官方 06-30 PT／本庫採 07-01）；「API 成本減半」屬實；「57 分」查無 benchmark 名稱，改 🔎 查無官方 |
| entities/mythos | 23 天 | Nozomi Networks 加入 Glasswing 經官方部落格確認，結案 |
| entities/mythos | 23 天 | csoonline Mythos FAQ 專文連結已 404 且無獨立事實，議題失效移除 |
| entities/mythos | 22 天 | CNBC Fed 示警經全文＋Bloomberg 佐證：Fed 至少三個月未取得 Mythos Preview，07-15 仍在爭取。結案 |

**C. ⚠️ 查證途中發現的覆蓋缺口（比原任務更嚴重）**
- **Claude Sonnet 5 的 $2/$10 已於 2026-08-10 官方永久化，9/1 漲至 $3/$15 的計畫取消**——官方模型總覽頁定價欄已無任何 introductory／到期字樣
- **本庫 12 個來源於 08-10～08-26 全數未收錄此則**（官方走 X 與 support/pricing 說明中心，兩者皆不在來源清單）。後果：距離原到期日剩 5 天時，`entities/pricing` 仍掛「⏰ 2026-08-31 到期」倒數，`feature-radar`、`model-comparison`、`entities/sonnet-5` 同步誤導，讀者會據以做錯誤的成本決策
- 已上修四頁共 13 處，並在 `entities/pricing` 補記 2026-08-10 事件與此缺口
- **未解決**：說明中心／官方 X 的定價變動仍無任何自動偵測；`.claude/rules/wiki-ingest-commercial.md` 已載明「記者無 web 工具、遇此回報主編查證」，但**沒有任何機制會定期主動查**——這是預言了故障卻沒裝偵測器。建議 weekly-review 評估加一道「⏰ 倒數中條目在到期前 7 天強制官方複查」的閘

**品質備註：** 本次為主編層查證（`/wiki-lint` 5c 性質），非每日 ingest；所有更動頁面只動「最後更新」，不動「最後新聞更新」。

## 2026-08-27 可讀性掃描

- 掃描頁數：55（✅ 41 / ⚠️ 11 / ❌ 3）
- 已修復：topics/anthropic-government-policy（目前局勢表兩儲存格下沉）、topics/enterprise-tool-tracker（摘要文字牆改分組條列）、topics/official-community-gap（缺口分析欄 10 列短語化＋⟨G-01⟩～⟨G-10⟩ 細節下沉）、entities/claude-code（版本動態條列化＋待查證獨立區）、entities/dario-amodei（頂部 4 則懸置 callout 收斂為單一最新動態，其餘下沉歷史記錄）、entities/claude-for-teachers、entities/claude-science、entities/claude-tag、entities/opencode（四頁補頂部 callout）
- 使用者跳過：無
- 共通問題：表格儲存格塞散文（未執行「表格放結論、細節下沉」）——已將該紀律自 wiki-ingest-models G/H 條提升為全站通用規範，寫入 `.claude/rules/wiki-ingest-format.md`「必須修復」表（2026-08-27）

## 2026-08-27 Graphify 試點結案＋節點查詢層上線

- **試點結論**：graphifyy 0.9.50 移除。查詢線 2/3 過（explain/path 贏 grep、query 打平）、分群與分類輔助雙死（contains 壓過 references；英文標題 vs 繁中內文詞彙鴻溝，top-6 命中 3/8）。詳見 `docs/graphify-pilot-plan.md` 試點結果與終局決策。
- **取而代之**：`scripts/wiki_graph.py`（隨需解析 wikilink 圖，explain/path/sections/cluster，頁＋標題層＋行號＋邊產地標記），衛生規則與 frontmatter 生成器/建置檢查字面共用；煙霧測試 4 條掛入測試套件（313→317）；`wiki/CLAUDE.md` 搜尋策略登記第 6 路；`.obsidian/graph.json` 套用同套衛生規則（濾 log/index/幽靈節點、六領域上色）。
- **買到的認識論**（雙 agent 辯論收斂）：模板標題＝圖上的過寬詞；log/index＝無鑑別力樞紐；contains 壓過 references 分群必死；跨語言詞彙鴻溝不在圖層解；roll-up 邊界＝未來 embedding chunk 邊界；樣板區（相關實體/參考來源）佔 26% 的邊、屬 see-also 非敘事關聯。
- **cluster 首跑訊號**：四群語意可辨；4 個 wikilink 孤島人物頁（chris-olah、teresa-carlson、tino-cuellar、tom-blomfield）待記者補語意連結。

---

## 2026-08-27 Ingest

**日報：** `news/2026-08-27.md`（13/13 來源、105 則）｜派工六類記者，全數回報。

**記者回報摘要**

| 類別 | 更新頁面 | 重點 |
|---|---|---|
| 模型 | entities/opus-5、opus-4-8、opus-4-7、fable-5 | GitHub Issue #77136（4.7／4.8／5.0／Fable 重複修辭、106 留言 517 反應）記於 opus-5 並在 4.8／fable-5 交叉引用；Opus 4.6 健身房 API 漏洞發現記能力面（標明為前代 4.6）；Fable 5 官方存取文件判定為既有記錄重申，未寫入新事實 |
| 功能 | entities/claude-code | v2.1.247 `SendFeedback`（進 feature-radar）；AGENTS.md #6235 互動數 335→384 留言／5889→6496 讚；API 中斷 #69415 44→55／82→91；fork subagent 重送對話歷史（Reddit，社群推測）依懸置語法標記；Windows GPU crash 與兩則官方文件判定與 08-19／08-25／08-26 既有記載重複，未重記 |
| 商業 | topics/anthropic-business、topics/ai-talent-flow | Salesforce／Claudeforce 深化合作＋上修全年營收（Reuters／qz／CNBC 三來源）、CrowdStrike 股價 +13% CEO 歸功 Anthropic、Meta 亦敵亦友（NYT）、Nvidia 傳投資 Hugging Face $12.9B 與黃仁勳「後悔」表態（商業風險表）；Fortune 報導 DeepMind 頂尖人才流失進 ai-talent-flow |
| 安全政策 | topics/ai-agent-safety | Amazon Kiro 提示注入外洩（Topic Watch，比照 Grok 列產業對照，不進「未修補風險現況」表）、Opus 4.6 自主發現並利用漏洞的安全意涵、HackerNoon 郵件權限最小化收於防護機制建議 |
| 社群 | topics/community-tech-patterns、topics/community-tech-discussions | Concord（多 agent 互通）、fork subagent 200 萬 token、hooks 強制規則遵循進 patterns；AGENTS.md 標準之爭、本地模型替代潮（LocalLLaMA ×2＋XDA）、#77136 品質退化訊號進 discussions |
| 人物 | entities/dario-amodei（＋新頁 entities/jensen-huang） | Dario 與 Benioff CNBC 聯訪（僅記逐字稿公開此層事實，未推斷發言內容）；黃仁勳達建頁門檻，「後悔」方向含糊依懸置語法標 ❓ 待查證 |

**主編彙整**
- `feature-radar.md`：新增 SendFeedback 工具（🔥🔥／⏳ 觀望／正式發布）詳細條目＋全覽表列；升版風險最新版本行更新至 v2.1.247；本週推薦無合格替補，維持三條並補記輪替說明（SendFeedback 未達 🔥🔥🔥🔥；Opus 5 超出 30 天時間閘、放寬 60 天後留任）。**當月對帳：詳細條目 16／全覽表列 16，相等。**
- `index.md`：新增 `entities/jensen-huang`（person／👤 人物／active（待核實））
- `data/source_attribution.jsonl`：append 28 筆
- `data/pending-handoffs.jsonl`：無新增（H-70d575 模型記者判不適用、H-1be92f 安全政策記者判需 web 查證，兩筆均維持開啟；一筆誤登為跨記者交辦者已 void）
- `anthropic-commitments.md`：無承諾類事件，未動
- `overview.md`：Salesforce 合作屬既有生態敘事的延伸，非局勢級變化，未動

**品質備註：** 功能 記者回報「August 全覽表 15 列對 16 條詳細條目、缺 1 列」，主編實測為 15／15 相等，該缺口不存在——回報前未實際數過，屬對帳欄自述與實況不符。

**📋 待辦（非單日 ingest 可處理）**
- `topics/anthropic-business.md`：「戰略合作」「IPO 前瞻」兩表既有列儲存格全數超過今日新訂的 120 字元全站規範，屬整頁結構性瘦身，建議另立 lint 任務
- `topics/community-tech-discussions.md`：熱門討論表格多數既有列同上，同建議

**📌 待使用者裁示** → 已當日裁決並執行完畢（見下方「表格瘦身重構」條目），本項結案。

---

## 2026-08-27 表格瘦身重構（全站 120 字元規範首次補課）

**觸發：** 使用者對本日 ingest 的待裁示項回覆「不能現在做嗎」，裁決當日執行，不排入 `/wiki-lint`、不另立專案。

**規模（重構前實測）：** 157 列超標，最長儲存格 1148 字元。

| 頁面 | 區塊 | 原超標列 |
|---|---|---|
| topics/anthropic-business | 戰略合作 61／IPO 前瞻 27／財務狀況 13／商業風險 11／摘要 1 | 113 |
| topics/community-tech-discussions | 熱門討論 40／時序 4 | 44 |

**派工：** 一頁一 agent（sonnet），不再細分區塊——同檔並行 Edit 會撞編輯。各自逐區塊由小到大處理，先在小區塊定下細節區格式。

**結果：** 兩頁超標儲存格皆歸零。anthropic-business 724→835 行、community-tech-discussions 1254→1304 行——**行數增加是下沉正確的訊號**（搬位置不是刪除）。anthropic-business「戰略合作」表另拆出獨立「來源」欄（4→5 欄，仍在 H 條上限內）。

**主編獨立驗收（不採信記者自述）：** 對兩頁 diff HEAD 做機械比對——超標儲存格 0、URL 集合零遺失、顯著數字 token 零遺失（`5.6`／`5%` 各少一次為表格內重複副本被壓縮，事實本體仍在細節區與時序）。317 測試全綠。

**驗收抓到的實際遺漏：** 商業記者重寫「來源」欄時掉了 3 個超連結（Oxide 官方部落格、Anthropic Blog／Cognizant、Fortune／SK 集團）——來源名稱留著、連結沒了。已補回細節區對應條目。**記者自查回報「事實遺漏自查：完整保留」，但連結不在它的自查範圍內**——下次同類任務的派工要把「超連結也算歸因」寫進硬性規則。

**品質備註：** 本次為格式修正，兩頁只動「最後更新」，不動「最後新聞更新」。

---

## 2026-08-28（Query：一則 Threads 推薦揭露 repo 搜尋的冷啟動洞）

**觸發：** 使用者貼 Threads 貼文問「這個 skill 推薦嗎、近期有沒有熱門的程式開發 skill」。查證該 repo（`addyosmani/agent-skills`）時順手查本庫覆蓋，發現**零命中**。

**揭露了什麼**

| 事實 | 數字 |
|---|---|
| `addyosmani/agent-skills` | 90,233★、每日 push、12 個來源 × 121 篇日報**零命中** |
| `obra/superpowers` | 278,521★，只在有人抱怨它時被 Reddit 順帶提到一次 |

**根因（兩個獨立原因，只修一個等於沒修）**

1. **scope 綁死 claude**：三條 `_REPO_SEARCH_SCOPES` 都要求 name/description 含 claude；skills 生態的描述多寫「agentic skills framework」「AI coding agents」，不含該字
2. **窗的幾何**（真正的病）：A 新星窗要求 90 天內出生、B 穿越窗上限 3000★，兩扇都是**發現期偵測器**。實查生日——superpowers 2025-10、agent-skills 2026-02、gstack 2026-03，星數 3 萬–28 萬——**就算 scope 完美也全部落空**

第 2 點會復發：每新增一條 scope，該 scope 的存量族群全部隱形。2026-08-04 的設計註解假設「>3000★＝早已成名＝不需要被發現」，被上述兩例推翻——沒有任何來源在報導它們。

**處置：C 窗（存量盤點）**，commit `5e125bed`

- >3000★（與 B 窗上限接壤），每日至多 2 則，掛在**所有** scope 上
- 「已報導過」判準取自 `news/*.md` 全文，不另立 state 檔——日報是唯一的永久記錄（`emitted_items.json` 只有 14 天 TTL，拿它當永久記錄會每半個月重吐同一批）。白送兩個性質：日報沒建成 → 明天自動重試、不靜默燒額度；repo 日後才越過門檻 → 自動被撿起來
- `summary` 帶 `[存量盤點｜出生日]` 前綴，日報撰寫者才不會把 2 月出生的 9 萬星 repo 寫成今日發布
- 新增 skills scope，**只進 C 窗不進 A/B 窗**：實測 100–3000★ 帶被單一用途內容型 skill 洗版（PPT 排版、公眾號排版、戀愛分析），工程級框架全落在 20k★ 以上——在這條 scope 上星數本身即品質過濾器
- 首跑：163 個未報導、吐 superpowers 與 affaan-m/ECC。積壓約 82 天走完（`INVENTORY_PER_DAY` 一個常數可調）

**測試撰寫過程抓到的實作缺陷：** 「讀不到日報時不得吐」這條測試紅了——`Path.glob()` 對不存在的目錄不拋錯只回空，空集合等價於「全部沒報導過」，會把整個存量灌進日報，光靠 try/except 擋不住。已補 digests 非空檢查。**這是先寫測試才發現的，不是先想到的。**

**registry 首版是假綠：** 前綴同步配對原本用概念詞「存量盤點」當 pattern，但檔內設計註解也含那四個字，把前綴改壞照樣通過。已改為釘實際輸出字串 `\[存量盤點｜` 並做過破壞測試（改壞 → ❌，還原 → ✅）。

**未解：** 本次只補了 GitHub repo 這條通道。`support.claude.com` 定價變動無自動偵測（2026-08-26 記錄的同型缺口）仍未解——同樣是「預言了故障卻沒裝偵測器」，建議 weekly-review 一併評估。

---

## 2026-08-28 官方頁偵測三修（含對 08-26 自身診斷的更正）

**觸發：** 使用者問「那是什麼問題」，追查 08-26 記下的「定價變動無自動偵測」缺口。

### ⚠️ 更正 2026-08-26 的診斷

該筆寫「說明中心／官方 X 的定價變動**仍無任何自動偵測**」——**這句話是錯的**。`src/news_aggregator/sources/official_watch.json` 自 2026-08-08 起就在監看 `claude.com/pricing` 與四個 support.claude.com 說明頁，而且它在 08-11 確實響過（該日日報有「官方文件更新：方案與定價」條目）。

診斷錯誤的代價不是零：照那句話行動會去蓋第二個偵測器，而真正的病是既有偵測器的三個缺陷。

### 真正的三個問題與處置

| # | 問題 | 處置 |
|---|---|---|
| 一 | **警報只說「變了」，說不出「變什麼」**。hash 模式只有一個 bit，摘要因此寫「具體改了什麼需開啟連結比對」——警報響了沒人知道響什麼。移除型變動（頁面少了一句「到期」）尤其隱形 | `_hash_item` 加段落級 diff（沿用 `_index_item` 已證明有效的集合差做法）。**hash/length 算法刻意不動**——改了會讓部署當天每頁同時報假警報 |
| 二 | **出事那一頁根本不在清單裡**。`claude.com/pricing` 是訂閱月費；每 token 單價寫在 `platform.claude.com/docs/en/about-claude/pricing`，該頁另獨家承載 fast mode $10/$50、Managed Agents $0.08/session-hour、web search $10/1000 次 | 該頁納入監看清單 |
| 三 | **截止日到期前沒有人回頭查**。倒數寫下去之後無機制複查 | 新增 `scripts/scan_expiring_deadlines.py`，掛為 pipeline Step 1b-3g，輸出接進完成摘要「待使用者裁示」 |

### 首次執行 3g 即抓到第四個缺口

3g 指出 `2026-08-31` 剩 3 天、散在 3 處。依規則查官方原文複查，發現促銷的**專屬官方頁**（`support.claude.com/…/15910845-claude-code-may-august-2026-weekly-limits-promotion`）**也不在監看清單** —— 本庫唯一在追的截止日，其權威來源竟無人監看。已納入清單。

複查結果：原文載「Increased weekly limits now run through August 31, 2026」，**日期仍有效 → 不動**，已在 `entities/pricing` 與 `feature-radar` 標註複查日。

### 測試與驗收

- 327 → 346（+19）：段落級 diff 9 條、截止日掃描 7 條，其餘為既有套件連帶
- registry 新增 2 組同步配對，兩組皆做過破壞測試（改壞 → ❌，還原 → ✅）
- 段落級 diff 以 2026-08-10 那次為測試案例：舊行為只印「內容有變動」，新行為印出「移除 1 段：Introductory pricing through August 31」

### 已知代價

`official_watch_state.json` 由 20KB 增至 323KB（存下各頁段落全文供比對）。判斷：正確性優先於體積，且 git 對逐頁區塊做差異壓縮；`MAX_SEGMENTS = 1200` 是無上限成長的閘。

---

## 2026-08-28 官方頁 diff 優化（並修掉首版一個會讓功能歸零的缺陷）

**觸發：** 使用者對 `official_watch_state.json` 由 20KB 漲到 323KB 說「我覺得要優化」。

### ⚠️ 量體積時發現的缺陷：表格被切成一格一段

檢視儲存內容時看到定價頁存著 `$0.08 / MTok`、`$0.10 / MTok` 這種無主詞碎片——因為 `_BLOCK_END_RE` 把 `</td>`／`</th>` 也當段落邊界。後果比體積嚴重得多：

- `$2 / MTok` 只有 9 字元，低於 `MIN_SEGMENT_CHARS = 12` 會被**整個丟掉**
- 於是「Sonnet 5 從 $2 改成 $3」在偵測器眼中是**零變動**——壞在這個功能唯一存在理由的那一頁上

改為只切到 `</tr>`。現在整列進 diff：`Claude Sonnet 5 $2 / MTok $2.50 / MTok $4 / MTok $0.20 / MTok $10 / MTok`，讀者一眼看得出改了什麼。已加測試釘住（`test_table_rows_are_not_shattered_into_cells`、`test_a_price_change_produces_an_interpretable_diff`）。

> 這個缺陷是**量體積時順手看內容才發現的**，不是測試抓到的——首版的測試只用 `<p>` 造樣本，從沒餵過表格，而被監看的頁面幾乎全是表格。

### 體積優化

量過三條路，選了同時改善訊號品質的那條：

| 作法 | 效果 | 取捨 |
|---|---|---|
| 頁內去重 | 269→256KB | 免費（diff 本來就只用集合語意，存重複是白存） |
| 跨頁池化 | 269→209KB | 需改 state 結構、加遷移 |
| **跨頁樣板過濾** | **323→205KB** | **同時消掉「新增 1 段：Try Claude Try Claude」這類噪音** |

樣板判準用「出現在 ≥2 個監看頁」，不是關鍵字黑名單——樣板的定義就是「每頁都有」，那是它唯一穩定的特徵。段數 4125 → 1631，定價事實全數保留（已驗證 `Sonnet 5 … MTok`、`will not occur` 皆在）。

**穩定性護欄：** 樣板集合隨監看清單而變，清單一改同一段可能從「內容」變成「樣板」而消失，下次 diff 會把它報成「移除」。故 state 存 `_meta.fingerprint`（參與判定的頁面集合雜湊），指紋不同時本輪只重記基線、不報 diff——與舊 state 無 segments 的處理一致。

### 驗收

- 測試 346 → 352；registry 的 diff 護欄配對由 3 條 pattern 增為 4 條（納入表格切法），另新增樣板／指紋配對；兩者皆做過破壞測試
- state 323KB → 205KB

---

## 2026-08-29 Ingest（含 08-28 缺日補救）

**背景：** `news/2026-08-28.md` 不存在。GitHub Actions 未替 08-28 建立任何 run（API 查證：08-27T20:15:28Z 之後直接無紀錄；08-27 那次亦遲到 10h15m），雲端 routine 因無新鮮資料正確中止。該日未抓料故無 `gathered_archive/2026-08-28.json` 可 replay，**不偽造 08-28 日報**；改由本日 26 小時視窗涵蓋（90 則中 43 則為 08-28 發布）。

**日報：** `news/2026-08-29.md`（13/13 來源、90 則）｜六類記者全數回報。

**記者回報摘要**

| 類別 | 更新頁面 | 重點 |
|---|---|---|
| 模型 | entities/fable-5、opus-5 | 社群「模型被削弱」質疑（Opus 5／Fable 5）、三模型 code review 實測（無數字，標待查證）、Fable 5.1 臆測依懸置語法標記；Model Hardware Standard 判非模型記者範疇，轉知功能記者 |
| 功能 | entities/claude-code | SDK files／skills 命名空間轉正 GA（進 feature-radar）；v2.1.250 純 bug fix 不收錄；#38335 session 額度異常 807→837 留言、#6235 AGENTS.md 384→385／6496→6525、#45596 Bring Back Buddy 265→268／2068→2076 |
| 商業 | topics/anthropic-business、entities/pricing、topics/competitor-landscape | Nscale 450 億美元／460 MW 資料中心協議、Claude 營收年增 1000%（單一來源）、Meta 預估支出 $10B、Salesforce Claudeforce 財報面補強、Google 低價方案（數字待查證） |
| 安全政策 | topics/anthropic-government-policy、topics/ai-agent-safety | **五角大廈黑名單經聯邦法官裁定違法、即時解除**（本頁長期追蹤案的終局判決，已四處同步無殘留舊狀態）；embracethered 揭露 Auto Mode 繞過＋Cybernews 實際利用案例；MCP RCE、Wiz 蜜罐遙測 |
| 社群 | topics/community-tech-discussions、topics/code-quality-decline | Tell HN 心智影響反思、HarnessOpt-Bench、`/buddy` 議題升 ☄️閃現→🌊延燒（18 天持續成長）；配額工具小批量與存量盤點三則留待 lint 策展 |
| 人物 | 無 | 三則候選全部判不達門檻（Barret Zoph 與 Anthropic 無直接關聯／CBS 聯合示警無具名發言者／embracethered 職稱僅泛稱）。**無更新是正確結果** |

**主編彙整**
- `feature-radar.md`：新增「SDK files／skills 命名空間轉正（GA）」詳細條目＋全覽表列；升版風險最新版本行更新至 v2.1.250。**當月對帳：詳細條目 17／全覽表列 17，相等。**
- `anthropic-commitments.md`：新增「Fable 5 恢復訂閱內含」列（🔴 未兌現）。官方原始表態出處僅有社群轉述，依懸置語法標 ⟨C-01⟩ 待主編查證——**本頁判準是「官方說過要做的事」，社群轉述不足以立案**。狀態 monitoring → ongoing（實質新事件），`index.md` 同步。
- `data/source_attribution.jsonl`：append 36 筆
- `data/pending-handoffs.jsonl`：close H-1be92f（安全政策記者查證後判不適用）；新增 4 筆——H-723f42（模型→功能：Model Hardware Standard 落點）、H-9f3d35（商業→安全政策：麻州政治獻金）、H-2eb673（安全政策→功能：Auto Mode 繞過同步已知問題）、H-a32301（安全政策→模型：fable-5 殘留黑名單舊狀態）。H-70d575 仍開啟（模型記者判不適用，需 web 查證）
- `overview.md`：未動（黑名單解除已在 government-policy 完整記錄，overview 週更）

**📋 待辦（非單日 ingest 可處理）**
- `entities/opus-5.md` 歷史記錄表、`topics/anthropic-government-policy.md` 目前局勢／攻防紀錄表：既有列儲存格超過 120 字元全站規範（26+ 列），與 08-27 已記的 anthropic-business／community-tech-discussions 同型，建議一併排入 lint

**📌 待使用者裁示**
- ⏰ 2026-08-31（剩 2 天）週用量促銷：08-28 已查官方原文確認日期仍有效，本次為 3g 重複命中，無需動作
- **日報格式瑕疵**：兩則存量盤點條目把 `[存量盤點｜…]` 前綴原樣印進日報，違反 `.claude/commands/news-pipeline-steps.md`「前綴本身不可寫進日報」。但該前綴的**資訊**（出生日、本庫首次收錄）對讀者有價值——要改的是輸出還是規則？

---

## 2026-08-29 Lint（雲端排程執行）

- 修正矛盾：`entities/claude-security.md` ⟨Q-01⟩ 與 `entities/claude-code.md` 07-24 已知問題事實不同步（後者早於08-10查證確認但未回掃），已補寫解釋並互加wikilink（功能記者）；`topics/community-tech-patterns.md` 誤稱 claw-orchestrator 已收錄於 tools.md「Trust／verification 層」（該分類不存在），已補列該工具並修正措辭（社群記者）
- 補連結：無（六類記者逐頁 Grep 確認全數頁面皆有 inbound wikilink，無孤立頁；`entities/jensen-huang` 僅 index.md 單一入鏈已轉知商業記者 H-1813db，非結構性孤立）
- 狀態更新：無（本輪 3c 掃描各 topics 頁最後新聞更新距今皆 ≤14 天或已於前次 lint 回升，無需下修；無 monitoring 頁滿足回升條件）
- resolved 收尾：無
- 新增 entities：無（Model Hardware Standard 達 feature-radar 收錄門檻已收錄，但屬全新產品線非既有頁延伸，是否另建 entities/ 頁列入待使用者裁示，依 4「只回報不動手」不自行建頁）
- 呈現品質：模型 4/8 頁⚠️已修復（fable-5／mythos／opus-4-8／model-comparison 表格>120字元或callout過期）、功能 3/14 頁⚠️已修復+3頁📋待辦（claude-code/managed-agents/claude-skills表格>120字元逾百筆規模大另立專項）、商業 5/7 頁⚠️已修復（pricing/competitor-landscape/enterprise-tool-tracker/anthropic-business/ai-talent-flow表格短語化下沉）、安全政策 3/6 頁⚠️已修復（government-policy/ai-agent-safety表格下沉、commitments過期callout覆寫）、社群 3/7 頁⚠️已修復（patterns矛盾修正+discussions/tools短語化）、人物 0/16 頁全數✅通過
- 入口層健檢：`entities/claude-code`（770行）、`entities/pricing`（660行）、`entities/opus-5`（≈370行）、`topics/anthropic-business`（846行）、`topics/anthropic-government-policy`（676行）、`topics/ai-agent-safety`（1107行）、`topics/coding-workflow-guide`（608行）、`topics/community-tech-patterns`（1637行）、`topics/community-tech-discussions`（1307行）、`topics/competitor-landscape`（646行）——十頁均已具備入口層，無需補結構；未發現語意分岔或死案候選，步驟3本輪跳過
- 待查證回訪：已標訊約4筆（claude-security⟨Q-01⟩訊08-10、dario-amodei訊08-24、amir-salek訊08-24、pricing resale訊08-29）；已改新語法約8筆（商業5筆、社群1筆等，含補齊缺失標/查欄位）；證據不足不動約40餘筆（逐一核對14天news非過度解讀，含多筆已逾複查日仍無後續）；模型組19筆全數核對後本輪無筆可加訊
- 規則檔健檢：
  - 矛盾（6a）：本輪掃描（wiki/CLAUDE.md、wiki-ingest.md、wiki-ingest-format.md、wiki-reporter-shared.md、wiki-lint.md自身）與六位記者回報均無新增規則矛盾發現
  - 引用驗證（6b）：7個錨點（首次出現欄／##痛點洞察／近期工具欄／##技術彙整／熱門討論表格／衍生欄／全覽表）逐一grep確認全部存在，全部通過
  - 遵守率（6c）：抽樣近3次ingest（08-26／08-27／08-29）——feature-radar更新提及3/3✅、log格式正確（來源/更新頁面/摘要欄位）3/3✅；**呈現品質✅/⚠️/📋標記僅1/3明確出現（08-26有「呈現品質：六位記者皆回報✅通過」明文行，08-27／08-29改用表格式摘要後未再寫出該行）**，低於2/3門檻，⚠️待使用者確認：表格式摘要是否視為滿足此規則、或應要求補寫明文rollup行
  - 過期規則（>60天）：`wiki-ingest-format.md`（04-25/05-15/06-11三條）、`wiki-ingest-features.md`（06-15/06-20兩條）、`wiki-ingest-commercial.md`（05-26/06-25兩條）、`wiki-ingest-safety-policy.md`（06-18一條）、`wiki-ingest-community.md`（05-16/06-20/06-28三條）、`wiki-ingest-community-lint.md`（06-19/06-28兩條）共11條（62–126天），逐一比對現行實踐（本輪六記者派工、頁面格式、報告契約）確認行為仍與規則描述一致，無需修訂
  - 來源健康：近7天（08-22~08-29）sourceStatus全部ok=true，社群/媒體來源（HN/Reddit/Google News/GitHub/GitHub Issues/dev.to/Blogroll）均無連續3天count=0，官方/清冊來源count=0屬正常；記分卡（48天窗口）觀察名單延續：GitHub（Wilson下界17%／Presence 6%，樣本充足雙低，已連續第2週列入觀察）；⚠️未註冊slug `business-chief` 1筆延續未處理（已擱置1週）；Google News低信譽桶0筆
  - 跨檔案語意矛盾（6f）：`python scripts/check_rules.py` 全部確定性檢查✅通過，同步配對註冊表全數語意一致；另發現13組高頻互引未登記sync_pair（warn-only提示，不阻塞，未強制登記）
  - 成長迴路（月度）：非本月首次lint，跳過（本月已於08-01/08-08/08-15/08-22執行過）
- 品質指標（6g）：
  - ref覆蓋率（每週）：100%（08-23~08-29，26條列/26有歸因；08-28當日無news檔案不計入分母），閾值80%→✅通過
  - 採用驗證率（月度）：非本月首次lint，跳過
  - 外部死鏈（讀報告）：`data/link_health.json` checked_at 2026-08-21（距今8天，未過10天新鮮度門檻，仍新鮮）；4筆既有dead連結核對仍成立，均已由前次lint標註「（原文已失效）」，本輪無新增
  - 趨勢判讀：持平（ref覆蓋率連續6期≥97%）
- 跨家榜單週更（5b）：雲端egress封鎖，跳過（已固定由本機`/weekly`步驟0承接）
- 逾期待查證清算（5c）：雲端egress封鎖，跳過（已固定由本機`/weekly`步驟0承接，額度5筆）
- 讀者模擬：3題全數✅3跳內找到——「Auto Mode是否有安全問題」→index→entities/claude-code已知問題（2跳）；「跨session記憶社群驗證得怎樣」→index→topics/community-pattern-trends趨勢九（2跳）；「五角大廈黑名單案進展到哪」→index→topics/anthropic-government-policy目前局勢表（2跳）
- lint自我遵守率：6/6位記者回報一次過（形狀層：逐項核對3a–3g＋轉知處置共8項均有明確結果，無缺項）
- 行為層抽驗：抽商業記者「entities/pricing.md ⟨resale標記⟩已加訊2026-08-29」宣稱，`git diff`核對確認如實——訊欄位已加、內文補記08-29跟進且措辭正確標注「非新事實／原問題仍未解決」，未過度解讀。結果：符合宣稱
- 懸置語法WARN：5c雲端跳過，隨之未執行（WARN掃描屬5c第1步盤點的一部分）
- 熱度降溫（5a）：檢查72條（🔥🔥+），降57條（絕大多數為近4週零命中的Claude Code逐版更新/舊API公告條目，詳見wiki/feature-radar.md diff）；同步entities頁3處（opus-4-8🔥🔥🔥🔥🔥→🔥🔥🔥🔥、claude-tag🔥🔥→🔥、claude-for-teachers🔥🔥🔥→🔥🔥）；⏳逾期>90天3條：Proactive Workflows／Capability Curve已加註不重複處置，Dreaming記憶整合（114天）本輪因熱度降溫同步降級，既有「最後後續」註記功能等同不重寫。**本規則自2026-08-20立法後首次真正執行**
- 歸因抽查（5d）：抽5筆（08-15/07-28/08-07/07-29/07-15，跨community-tech-patterns/ai-agent-safety/anthropic-business三頁），逐筆核對日報原文與wiki現文——**5筆全數相符，0修正、0無對應**。註：2筆Blogroll來源項目（Simon Willison部落格）在`news/*.md`當日檔案中查無對應條目（可能為Blogroll項目未進入日報markdown的既有處理路徑），但透過`data/source_attribution.jsonl`與wiki頁面連結交叉核對，內容忠實度確認無誤，非citation drift案例。**本規則自2026-08-28立法後首次真正執行**
- 渲染層驗收：待web build完成後執行（見下方收尾閉迴路）
- overview.md：已重寫（反映本輪08-23~08-29週：五角大廈黑名單終局判決、Auto Mode安全繞過揭露、IPO/商業敘事新數字、Model Hardware Standard、feature-radar熱度降溫首次執行、社群趨勢九升格）
- 待使用者裁示：
  - Model Hardware Standard是否建entities/頁（⏳ 已擱置0週，本輪新提）
  - community-tech-patterns淘汰審查dry run：0條淘汰/0條合併/2條無法判斷（額度監控生態需查官方頁細節；Aharness 60天無後續但機制自洽）（⏳ 已擱置0週，本輪新提）
  - 6c發現：呈現品質✅/⚠️/📋標記log明文rollup行從1/3降至（表格式摘要是否視為滿足規則，或應恢復明文行）（⏳ 已擱置0週，本輪新提）
  - claude-code.md版本更新/歷史記錄表格（550–767行區間）逾百筆儲存格>120字元，規模過大不宜倉促處理，建議另立專項（⏳ 已擱置0週，本輪新提；managed-agents.md 5格、claude-skills.md 3格同型但規模小可隨附）
  - 來源記分卡觀察名單：GitHub（Wilson下界17%／Presence 6%雙低）是否調整收錄門檻（⏳ 已擱置1週，08-22首次提出）
  - 未註冊slug `business-chief`（安全政策記者08-21誤用媒體名，應為google-news）是否修registry（⏳ 已擱置1週，08-22首次提出）
  - `[存量盤點｜…]`前綴誤印進日報：要改輸出還是規則（⏳ 已擱置1週，08-29 ingest首次提出，本次lint未處理）
## 2026-08-29（規則裁決：存量盤點前綴改為「翻譯」而非禁寫）

**觸發：** 今日日報兩則存量盤點條目把 `[存量盤點｜…]` 前綴原樣印給讀者，違反 08-28 才訂的「前綴本身不可寫進日報」。回報時我判斷該檢討的是規則而非輸出，使用者裁決「改規則」。

**原規則錯在哪：** 它把這個前綴類比成 `[加入: …]` 那類純維運標記，一律禁止外流。但兩者性質不同——`[加入: …]` 是規則檔的版本註記，讀者不需要知道；而存量盤點前綴裡裝的是**讀者需要的事實**：這個 27.9 萬星的東西是 2025-10 出生的，不是今天發布的，是本站漏了十個月才看到。禁掉整段，讀者就會把它誤讀成今日新發布。

**改法：** 該禁的是方括號那層外殼，不是裡面的資訊。規則改為三選一中的「翻譯」——

- ✅ `**[obra/superpowers](url)**（2025-10 出生、27.9 萬星，本庫今日首次收錄）…`
- ❌ 原樣照抄方括號標記（讀者會當成系統雜訊）
- ❌ 整段刪掉（讀者會誤讀成今日發布）

**未動今日日報：** `news/` 為唯讀原始資料（`CLAUDE.md` 明文），不因規則改版回頭改寫已發布的日報。今日兩則維持原樣，新規則自明日起生效。

**規則自身的教訓：** 訂一條「禁止 X 外流」之前先問——X 裡面裝的是維運資訊還是讀者資訊？裝的是後者時，正確的動作是換一種呈現形式，不是封鎖。這條規則從訂立到被實跑推翻只隔一天，因為它是在沒有實際輸出可看的情況下憑類比訂的。

**⚠️ 同日更正（08-28 缺日的診斷）：** 本日稍早記「GitHub Actions 未替 08-28 建立任何 run」——**查詢當下屬實，結論不完整**。該 run 後來於 `2026-08-28T21:11:05Z` 才啟動（commit `f692b0c2`），**遲到 11 小時 11 分**；我查 API 的時間是 08-28 約 16:50 UTC，比它啟動早了 4 小時。

正確說法是「排程嚴重遲到」而非「被丟掉」，而這個區別會改變修法：

- 08-27 遲到 10h15m、08-28 遲到 11h11m，皆遠超 workflow 註解記載的觀測最大值 2h42m（當初據此設 3 小時緩衝）
- 雲端 routine 固定 13:00 UTC 開跑，緩衝再拉大也追不上 11 小時級的延遲——**單靠加大緩衝已不可行**
- 可行方向改為：雲端 routine 遇無新鮮資料時不直接中止，改為自行觸發抓取或延後重試；或改用非 cron 的觸發方式

> 教訓：查 API 拿到「查無紀錄」時，那是**當下的快照**，不等於「不會發生」。同一個 endpoint 四小時後就有了。涉及非同步系統的否定結論要標明觀測時間，或隔一段時間複查再下判斷。

---

## 2026-08-29 抓料排程修復（08-27／08-28 連兩天開天窗的根因處置）

**目標：** 使用者下 `/goal`「找到這個問題並解決直到你覺得今晚不會再發生」。此前只做了診斷與補跑，根因未動。

### 量到的事實

| 日期 | 排程延遲（GitHub 建立 run 的時間 − 10:00 UTC）|
|---|---|
| 08-17～08-26（10 天）| 穩定 **+0.5～0.7h** |
| 08-27 | **+10.3h** |
| 08-28 | **+11.2h**（21:09 UTC 才執行）|

延遲發生在 GitHub **建立 run** 的階段，不是 runner 排隊。當初依觀測值 2h42m 所設的 3 小時緩衝被穿透兩次。

### 為什麼「加大緩衝」不是解法

雲端 routine 固定 13:00 UTC 開跑，而延遲已達 11 小時級；緩衝再拉大也追不上。而雲端沙盒 egress 政策封鎖新聞網域（Reddit／HN／Google News 回 403），**routine 結構上無法自己抓料**，必然依賴 GH Actions，只能從時間上解。

### 修法：保險窗

關鍵是一個先前沒被利用的性質——**run 寫進 `gathered_items.json` 的日期，是它實際執行當下的 UTC 日期，不是排程時刻**。因此只要執行落在 [00:00, 13:00) UTC 就算數：

| cron | 正常（+0.6h）| 延遲（+11h）|
|---|---|---|
| 22:00（前一日）| 22:36 → 日期為前一天 ❌ | 09:00 ✅ |
| **00:00（新增）** | **00:36 ✅** | **11:00 ✅** |
| 10:00（保留）| 10:36 ✅（最新鮮）| 21:00 ❌ |

只有 00:00 兩種情況都活。保留 10:00 是因為健康日它的資料比 00:00 新鮮 10 小時，且會覆蓋 00:00 的結果——**健康日的日報新鮮度完全不受影響**，00:00 那班只在 10:00 遲到時才被用到。可容忍延遲上限自 3h 拉到約 13h。

### 一併修掉的第二個落地風險

workflow 原本是裸 `git push`：checkout→push 之間約兩分鐘視窗，期間若雲端 routine 或使用者推了任何 commit 就 non-fast-forward 失敗 → job 失敗 → **當天抓料整包不落地**，而外觀看起來像抓取有問題。本 session 自己就被同一個 bug 咬過兩次。改為三次 `git pull --rebase` 重試，耗盡則 `::error::` + exit 1 讓 GitHub 寄信。加保險窗後每日兩班，此視窗曝險加倍，故一併補。

### 今晚（08-29 13:00 UTC）的實際情境

`news/2026-08-29.md` 已由本日補跑產出，故今晚 routine 會在 **Step 0b 冪等閘**中止——**那是正確行為，不是開天窗**。下一個真正有風險的是 08-30 13:00 UTC，而 00:00 UTC 的保險窗會在它之前執行。

### 驗收

- 測試 352 → 358（新增 `test_daily_gather_schedule.py` 6 條，釘住「最早 cron ＋ 可容忍延遲 < routine 開跑時刻」這條核心不變式與 push 重試）
- 破壞測試：移掉 00:00 那班 → 測試以「最早的 cron 在 10:00 UTC，加上可容忍延遲 12h 會落在 22:00，晚於 routine 的 13:00」失敗；還原 → 通過
- **殘餘風險已登記**（`docs/workaround-register.md`，複查日 2026-09-12）：延遲若超過 13h 仍會開天窗，餘裕僅 1.8h。處置是續觀測，再出現 >12h 才加開前一日晚班——不先加是因為健康日那是每天一次的空跑

**補記（同日，使用者追問「排程遲到不合理」後查證）：** 查 GitHub 官方事件記錄（githubstatus.com API），08-24 以後確有三筆 Actions 事件，含 08-26 15:11 的 critical（資料庫 primary 故障轉移）與 08-26 22:56 的 Actions/PR 延遲——**但三筆都在 08-27 10:00 UTC 之前結案**（分別於 08-26 18:01、08-27 00:26、08-24 14:34），涵蓋不到 08-27／08-28 的延遲窗。**成因仍未明**，只能確認不是本專案設定問題（延遲發生在 GitHub 建立 run 的階段，`created_at` 即已落後）。

查證過程發現自己犯的一個錯：保險窗原本排在 `0 0 * * *`——**整點、且 00:00 UTC 是全平台最熱門的 cron 時刻**。GitHub 官方文件明載 schedule 會在高負載時延遲、「每個整點的開始」正是高負載時段，並建議避開整點。等於我把保險窗放進了最擠的隊伍。已改為 `17 0` / `23 10`。這不保證解決 10 小時級延遲（成因未明），但是官方指名的緩解手段且零成本。

**Review 補記（同日，使用者要求「全部 review 一次改法，非必要不要加」）：** 逐項複查本輪所有改動，找到兩件事：

1. **截止日掃描器無視自己的答案（真缺陷，已修）**：`entities/pricing` 那行明明寫著「2026-08-28 查官方原文複查，日期仍有效」，掃描器照樣每天要求「需主編查官方原文確認一次」，會一路叫到 08-31。**永遠在響的警報會被整段跳過**，正是本庫反覆記錄的那種病。加上以「截止日」為單位的抑制（行內有複查/查證字樣＋近 14 天內的日期即靜默），今日輸出由 3 筆降為 0 筆；靜默期過後會重新提醒，不是永久關掉。抑制刻意不以「行」為單位——同一日期常散在 3 處以上，查證的是日期不是某一行。

2. **我自己引入的餘裕消失（已登記，不修）**：C 存量盤點窗讓每次 gather 的 GitHub search 呼叫由 6 次增為 10 次，**正好等於匿名 API 上限**。GH Actions 有內建 token（30/min）不受影響，本機手動跑已無餘裕。不現在動它——目前實測未撞限流，且修法（減 scope）會重開冷啟動洞；改為登記，下次要加 scope 時必須先有 PAT。

**複查後決定保留的（附理由，避免下次又被問）：** 段落級 diff 的樣板過濾與指紋護欄——監看清單三週內改了 4 次，每次若無護欄都會產出一批假的「移除」；C 窗以 `news/*.md` 當狀態而非新 state 檔；抓料的 push 重試（本 session 被同一 bug 咬過兩次）。

---

## 2026-08-29 官方頁 diff 的第四輪修正（並更正前一輪的錯誤判定）

**⚠️ 更正本日稍早的兩則紀錄。** 上方「Review 補記」與「體積優化」兩段記載：跨頁樣板過濾「同時消掉『新增 1 段：Try Claude Try Claude』這類噪音」，以及本日更後面一次判定該好處「經實測不成立」而整套移除。**兩則都不準確，正確的是第三種說法：**

- 我當時的實測用「穩定導覽列」造樣本，得出「集合差自動抵銷、不會進 diff」的結論——對穩定樣板成立
- 但 6 個 `support.claude.com` 頁共享的**不是**導覽列，是**會變動的 Help Center 文章索引**：實測 354 個段落出現在 ≥5 頁，內容為文章標題
- 官方發一篇新文章時，6 頁會同時報「新增 1 段：〈新文章標題〉」——**配額頁與計費頁會宣稱自己新增了一段不相干的內容**。這不只是噪音，是錯誤歸因，會經日報摘要進 wiki
- 實證：日報中 support 頁的「官方文件更新」則數，08-20～08-26 多為 0–2，**08-27 為 5、08-29 為 4**。單頁各自變動不會有這種齊發形態

**所以樣板過濾是有效的，該砍的不是它。** 前三輪的缺陷全出在它的兩個護欄（指紋、抓不齊處置），而護欄之所以需要，是因為**過濾發生在儲存時**——存進去的東西帶著「當時的樣板基準」，基準一變昨天今天就不可比。

**第四輪修法：過濾改在比較時做。**

| | 儲存時過濾（前三輪） | 比較時過濾（現行） |
|---|---|---|
| state 內容 | 已過濾，與基準綁定 | **未過濾全量，與基準無關** |
| 基準變動 | 昨今不可比 → 需指紋偵測 → 需重記基線 | 兩邊同時套用今日基準，對稱，自我修正 |
| 抓不齊 | 樣板位移 → 假 diff／污染 → 需 complete 閘 | 最壞多報幾段，不會假「移除」 |
| 需要的護欄 | 指紋＋resegmented＋complete | **無** |

代價：state 維持未過濾體積（約 310KB，登記表已列為刻意接受）。

**另修：** 超標頁（段數 > MAX_SEGMENTS）的訊息原本承諾「下次變動起會列出差異」，但超標頁永遠存不進 segments，那句話對它永遠是假的——改為明說不做段落比對。

### ⚠️ 我在 review 過程中吃掉了一則真實的官方文件變動

第 4 輪 reviewer 比對 state 的 hash 發現：我在 12:02 跑重構驗證時連了網，`code.claude.com/docs/en/desktop.md` 當下真的變了（+338 字元，遠高於 40 字元門檻），新 hash 被寫進 state 並 commit，**該變動因此從未進入任何日報**。已還原該頁的 hash/length 至消費前的值。

**教訓：這個來源的 state 是「已消費事件」的帳本，不是快取。** 在 pipeline 之外實跑並 commit state，等於代替 pipeline 消費掉事件。前三輪的驗證跑沒出事，只是剛好那幾次每頁 hash 都沒變。日後驗證這個模組一律用 mock，不要連網跑完再 commit state。

---

## 2026-08-29 第五輪 review：錯誤歸因只是換了層級

第 4 輪修好「段落層級的錯誤歸因」後，第 5 輪 reviewer 指出它只是搬家了：`_hash_item` 是**先**決定發不發（hash 變 + 字數差 ≥40），**後**才算摘要。對稱過濾讓 added/removed 變空，但條目照發——6 個 support 頁各發一則「未偵測到段落層級差異」，而下游 enricher 會把這些空條目改寫成看起來像新聞的摘要。實證：08-27 五則、08-29 四則，其摘要寫的全是該頁的常態說明，沒有一句是變動。

**修法讓程式變短而不是變長**：把「有沒有實質差異」提前到發不發的判斷裡，濾完全空就不發條目。連帶讓「未偵測到段落層級差異」那個分支變成死碼，一併刪除。mock 端到端驗證：共享索引新增一篇 → **6 則變 0 則**；某頁自己真的改了 → 仍 1 則且精確列出改了哪一段。

**樣板門檻 2 → 3（量出來的）**：8 頁 1489 段的跨頁分布是 `1 頁 1124｜2 頁 9｜3 頁 1｜4 頁 1｜5 頁 350｜6 頁 4`。真樣板整團在 5，而 count=2 的 9 段全是導覽標籤。取 3 既涵蓋整個索引，又讓「同一事實剛好被官方寫在兩頁」不致被誤判為樣板而靜音——那是本機制唯一的偽陰性方向。

**另修兩處與樣板無關的**：
- 今日切不出段落時會丟棄昨天的基線，訊息卻說「本頁尚無可比對的前一版段落，下次變動起會列出差異」——兩個子句都不成立（前一版存在；而下次也不會有，因為剛剛才刪掉）。改為保留舊基線
- 我上一輪還原 desktop.md 只還了 hash/length，把 514 段基線清掉了。那份基線就在 `004cffe9` 的 git 裡，已取回——否則下輪那則變動只能報「81136 → 81474 字，請自行開連結比對」

**補了 fetch 層的端到端測試（2 條）**：reviewer 指出前兩輪的缺陷正是從「有 `_boilerplate` 單元測試、有單頁 fetch 測試，但沒有多頁共享樣板的端到端測試」這個縫走出來的。已破壞測試驗證（拿掉抑制 → 紅）。全程 mock 不連網。

**登記為已知取捨不修**：樣板集合只從本輪抓成功的頁算，若 6 個 support 頁只剩 1–2 頁抓成功則近乎空集，該輪會錯誤歸因。不修的理由是修法（把樣板集合存進 state 跨輪沿用）等於再造一個「儲存時綁定基準」的機制，而那正是前三輪三個缺陷的共同根源。

### 五輪下來的模式

第 1～5 輪，**每一輪我的修法都生出下一輪的缺陷**，而且全部集中在同一個功能上。回頭看，共同形狀是：我每次都在既有機制上「再加一層護欄」，而不是問「這層機制的邊界條件是什麼」。真正有效的兩次修改都是**減法**：把過濾從儲存時移到比較時（消掉三個護欄）、把差異判斷提前到發不發（消掉一個死分支）。

---

## 2026-08-29 第六輪 review：這個功能對它唯一存在理由的變動完全無效

第 6 輪 reviewer 找到六輪來最重要的一個缺陷，而它是 **P0**：

`MIN_DELTA_CHARS` 長度閘排在段落 diff **之前**。而價格數字改動是**長度守恆**的——`$2 / MTok` 改成 `$3 / MTok` 差 0 字元。於是：

```
Sonnet 5 從 $2 改成 $3 → 產出條目數：0
  state 已存入：['Claude Sonnet 5 $3 / MTok $10 / MTok']
```

不只報不出來，**新值已被吸收進基線，日後任何一輪都再也報不出來**。這個模組是為了追蹤定價、配額、截止日這些數字事實而存在的，而它對這類變動端到端無效。

**我的測試綠燈，是因為它直接呼叫摘要函式、繞過了那道閘** —— 跟第 4、5 輪同一個「漏在層與層之間」的形狀，第三次。

### 修法：讓兩個閘各司其職

不能把長度閘降為 fallback——查 state 的 git 歷史：22 個 commit 中 hash 變動 67 次，其中 **28 次字數差 <40 被它擋掉**（多為排版與措辭微調）。全部放行等於每日多約 1.3 則雜訊。

而「輪替計數器」與「價格數字」在結構上完全相同（都是同一段落的小編輯），沒有便宜的結構規則能分開。所以改用一條**與本模組目的直接綁定**的判準：

> 差異裡有數字或金額字元變動 → 一定報；否則退回長度閘。

三個情境實測：價格 $2→$3（長度守恆、有數字）→ 1 則；500 個 a 後加 5 個 b（無數字、差 5 字元）→ 0 則；無數字但差 60 字元 → 1 則。

### 連帶修掉的

- 超標頁與切不出段落兩條路徑都會丟棄昨天的基線，訊息卻謊稱「尚無可比對的前一版段落」（上一輪只修了其中一半，而修完之後那句話從「有時假」升級為「必定假」）
- 空 diff 的兩種成因分開處理：原始有差而濾後全空 → 變動在共用區 → 靜音；原始也全空 → 段落層看不見 → 退回長度閘
- 樣板門檻 3 的註解原本寫的分布敘述推不出 3。真理由是兩個鏡像定價頁：門檻 2 會把真正的價格字串當樣板而雙頁靜音。已改寫並把「導覽列雙頁齊報」登記為取捨

### 測試檔整個重寫

**行為測試一律走 `_hash_item` 或 `fetch()`，不再直接呼叫摘要函式。** 三個新行為各做過破壞測試（改壞 → 紅、還原 → 綠）。

### 六輪下來的總結

| 輪次 | 我的修法 | 下一輪發現 |
|---|---|---|
| 1 | 指紋取自抓取結果 | 單頁 timeout 讓全部頁失效兩輪 |
| 2 | 指紋改取自設定 | 樣板位移但指紋不變 → 假 diff＋污染 state |
| 3 | 整套刪掉（理由：噪音抑制不成立） | 理由是錯的，共享的是**會變的**文章索引 |
| 4 | 過濾改在比較時 | 濾空了但條目照發，錯誤歸因只是換層級 |
| 5 | 濾空就不發條目 | 長度閘排在前面，價格變動端到端 0 則 |
| 6 | 數字變動繞過長度閘 | ？ |

共同形狀有兩個。一是**我每次都在既有機制上再加一層護欄**，而有效的修改全部是減法。二是**我的測試每次都測在缺陷逃走的那一層之下**——第 4、5、6 輪的缺陷全部漏在層與層之間，而每一輪我都是在被指出來之後才補上跨層測試。

---

## 2026-08-29 第七輪 review：例外的鍵，正好是那道護欄要擋的東西

第 6 輪加了「差異含數字 → 繞過長度閘」讓價格變動報得出來。第 7 輪 reviewer 指出：**長度閘註解自己寫著它要擋的是「a rotating CSRF token, a "last viewed" widget」——而輪替計數器就是數字。** 我等於對那道護欄要擋的字元類別開了永久後門。

不是假想。真 state 裡有 4 個段落來自 support.claude.com 的 Intercom 小工具：

```
Updated over 2 weeks ago Copy for LLM This article explains how usage credits work…
Updated over a week ago  Copy for LLM This article applies to individual consumers…
Updated this week        Copy for LLM August 2026
```

它每週自己滾一次，長度守恆、只出現在單頁（樣板過濾也接不到），於是 3–4 頁每週各發一則；而時間戳與文章首段吐在同一段裡，摘要讀起來像整段說明被改寫。

**reviewer 對我這七輪的診斷比缺陷本身更值得記：**

> 第 6 輪自己寫下「輪替計數器與價格數字結構上完全相同」，卻只用這個事實推出「所以放行價格」，沒有反向推出「所以也放行了計數器」。同一個前提的另一半沒被走完。

### 修法：從源頭剝掉，而不是再加一條例外

相對時間戳是易變 chrome，不帶任何編輯資訊——和 `<script>` 同一類。剝在 `_visible_text` 裡，hash 因此也不會為它而變：**問題不是被過濾，是不存在。** 剝掉之後數字繞道才站得住腳（實測全庫恰好 4 個此類段落，無其他數字型輪替 chrome）。state 已就地做同樣正規化，避免部署當天為此假警報。

實測：時間戳 2→3→4 weeks 滾動 → 0 則；同頁價格 $2→$3 → 仍 1 則且精確。

### 連帶修掉

- 「本頁尚無可比對的前一版段落」在第三條路徑上仍是假的（hash 變了但段落集合相同）。第 6 輪只修了三分之二。已拆成獨立訊息
- 長度閘算式寫在兩處且 `>=` / `<` 不一致，抽成單一 local——A2 那條 fall-through 藏得住，一部分就是因為判斷散在兩處
- `_diff_summary` 的三個參數只為重建呼叫端已有的字串，抽出 `_head()`

### 測試補上「成本側」

第 6 輪只測了新規則的收益（數字變動報得出來），沒測它的成本（數字雜訊要不要擋）——**第四次同一個形狀**。已補兩條：時間戳滾動不得成為變動、同頁真價格變動仍要報出。另把「訊息說尚無前版段落」的測試從釘訊息文字改為釘**訊息與 state 是否相符**。

寫測試時對照組先紅了一次，抓到另一個真限制：`two dollars → three dollars` 這種拼字數字不含 `[0-9$%]`，會被長度閘擋掉。官方定價頁用的是 `$3 / MTok`，故現況未觀測到漏報，已登記為已知取捨——不擴充判準的理由是那會把「計數器 vs 價格」那條分不開的線再拉長一次，而那正是七輪來反覆栽的地方。

---

## 2026-08-29 第八輪 review：護欄寫得比要擋的東西寬，而守護它的測試從未生效過

第 7 輪把輪替時間戳當 chrome 剝掉，方向是對的，但三處出錯：

**A1（嚴重）——regex 的 `updated` 前綴寫成可選，於是它吃掉正文裡任何「N 天前」的句子：**

| 原句 | 剝除後 |
|---|---|
| `If you purchased your subscription less than 14 days ago, you may request a refund.` | `If you purchased your subscription , you may request a refund.` |
| `Credits granted more than 30 days ago expire automatically.` | `Credits granted more than expire automatically.` |

退款期限、credit 到期日**正是本模組要守的計費事實**，而且因為 `_visible_text` 也剝，hash 根本不變 → 這條事實從此不可能被偵測到。與第 6 輪修掉的「價格變動端到端 0 則」同一形狀，由第 7 輪的修法重新生出來。真 state 的 4 個命中 4/4 都帶字面 `Updated`，改必填零損失。

**A2（嚴重）——同一個修法在兩個函式以兩種順序落地，只驗了其中一個。** `_visible_segments` 在標籤還在時剝、`_visible_text` 在標籤剝掉後剝。頁面若是 `Updated <time>over <b>2</b> weeks ago</time>` 這種 inline markup，前者剝不掉、後者剝得掉。而我 commit 裡寫的「實測 → 0 則」是在測試自造的純文字 `<p>` 上得到的，**不構成對真實頁面的證據**。已統一為兩處都在標籤剝除、空白收斂之後才剝，三種 markup 各驗過。

**C1（最刺）——那條號稱守護 hash 演算法的測試，在演算法被改的同一個 commit 裡全程綠燈。**

它把 `_visible_text(BEFORE)` 餵進 `_hash_item`，再對**同一個字串**算一次 sha256——只證明 `_hash_item` 沒竄改自己的參數，與 `_visible_text` 的算法完全無關。我從第一輪就在 commit 裡宣稱「hash 算法不得改動、由測試守著」，**那個護欄從來沒有存在過**。

已改為 golden digest：對固定 fixture 算 `_visible_text` 的 sha256 與硬編常數比對。三種真實演算法突變（不剝 script／不剝 volatile／volatile 樣式擴大）全數擋下——這是七輪來那條護欄第一次生效。

### 八輪下來的形狀

前七輪是「修 X 生出 Y」。第 8 輪 reviewer 指出這輪的形狀變了，而且更難察覺：

- **同一個修法在兩個地方以兩種順序落地，只驗了其中一個**（A2）
- **護欄寫得比要擋的東西寬**（A1）
- 而這兩件事沒被自己的測試擋下，是因為 **那條測試從未真的守著它宣稱守著的東西**（C1）

C1 是這八輪最值得記的一條：**我每一輪都在 commit 裡引用那條測試當作「已驗證」的依據，而它一次也沒兌現過。** 破壞測試不是形式——沒做破壞測試的護欄，等於沒有護欄。

---

## 2026-08-29 第九輪 review：護欄的斷言對象選錯了（第二次）

第 8 輪為「兩處剝除順序不同」寫的護欄是 `_visible_segments(html) == {_visible_text(html)}`。reviewer 實跑證明它擋不住東西：**把兩個函式一起退回第 7 輪順序，18/18 全綠**，而 inline markup 的時間戳重新進了 hash。

reviewer 抽出的原則是這九輪最有價值的一句：

> 第 8 輪淘汰掉的那條選了「`_hash_item` 有沒有竄改參數」，第 8 輪新寫的這條選了「兩個函式彼此相不相等」——**兩者都是相對於受測物自己的斷言**。golden digest 之所以有效，正因為它是絕對值。

同一個錯我犯了兩次，而第二次是在剛剛才因為第一次被打臉之後。

**修法：** fixture 擴充為同時含 inline markup 與跨原始換行的時間戳（絕對值就守得住這兩類）；一致性測試補上絕對斷言「兩邊都不得殘留 `weeks ago`」，一致性降為附帶條件而非主張。驗證：對稱回退現在被兩條測試同時擋下。

**另修（A2，而且是減法）：** `_visible_segments` 逐行剝 volatile，而 `split('\n')` 的換行不只來自區塊標籤、也來自原始 HTML／markdown 自己的換行，於是跨原始換行的時間戳在段落側剝不掉。修法是把剝除移到**切行之前**——regex 的 `\s+` 本來就跨換行，逐行那層可以整個拿掉。四種換行形態實測全部剝淨，markdown 的段落邊界也保住。

**刪掉一處死重：** `_visible_text` 的第一次 `_WS_RE.sub` 對結果零影響（reviewer 以 3000 組隨機輸入實測 0 差異，golden digest 不變）。

### 一個我撤回的處置

reviewer 指出兩份測試檔有 4 組重複案例，建議清掉舊的。我刪到一半留下空 class，然後停手撤回——**那四條是我動工前就存在的測試，而且 mock 點不同**（一個 mock `requests.get`、一個 mock `_fetch_body`）。刪既有測試來減重複，正是這幾輪我一直在犯的過度出手。留著。

---

## 2026-08-29 根本修法：TARGET_DATE 由資料決定，不由時鐘決定

**使用者指出我這幾天一直在補破洞。** 加保險窗 cron、加 push 重試、加告警——全都在對抗 GitHub 排程的不可靠，沒有一個碰到根因。

### 根因

抓料（GitHub Actions，10:00 UTC）與生成日報（雲端 routine，13:00 UTC）是兩個**各自排程**的工作，而新鮮度防線要求 `gathered_items.json.date == TARGET_DATE`，TARGET_DATE 又取自 routine 執行當下的時鐘。

**等於強迫兩個獨立排程落在同一個 UTC 日。** 任一邊延遲就中止，而隔天抓料會覆寫 `gathered_items.json` —— 那一天的日報永久消失。

08-27 與 08-28 兩次中止的 log 一字不差地印證這件事：

```
ABORTED: gathered_items.json date=2026-08-26 …非目標日期的新鮮資料
ABORTED: gathered_items.json date=2026-08-27 …非目標日期的新鮮資料
```

### 修法是刪一條約束，不是加機制

排程模式下 TARGET_DATE 改由 `gathered_items.json` 的 `date` 決定。routine 的工作變成「把手上這批資料變成日報，如果它還沒被變成日報」—— 而「還沒被變成」正是 `Step 0b：冪等閘`**已經在做**的事，不需要新增任何東西。

| 情境 | 舊行為 | 新行為 |
|---|---|---|
| 正常日 | 生成今天 | 生成今天（完全相同）|
| 抓料延遲 11h | 中止，隔天資料被覆寫 → **永久消失** | 隔天 routine 讀到那批資料、發現日報不存在 → **自動補上** |
| 抓料連續失敗 | 每天中止 | 補完一次後 Step 0b 每天擋下，不需額外的過期判斷 |

回放 08-28：雲端 21:09 那次抓料寫入 `date=2026-08-28`、59 則。新行為下，08-29 13:00 的 routine 會讀到它、發現 `news/2026-08-28.md` 不存在、生成它。**那天不會消失，也不需要我介入。**

### 連帶移除前幾天加的補丁

`daily-gather.yml` 的 00:00 UTC 保險窗是我前兩天為了對抗排程延遲加的。根本修法讓延遲不再造成資料遺失後，它的唯一剩餘價值是「同日送達而非隔日」—— 時效性優化，不是正確性需求。依「不加沒必要的機制」移除，並在 workflow 裡註明何時該加回來。

**push 重試保留**：那修的是「抓料整包不落地」的真 bug（checkout 到 push 之間的併發視窗），不是在對抗延遲。

排程測試也跟著改：不再釘「排程要多早」（那是在維護一個不該存在的耦合），改釘**根因的所在地**——若有人把 TARGET_DATE 改回時鐘，測試會紅。

---

## 2026-08-29 根本修法（第二版）：目標日期取自耐久的 archive，不是時鐘、也不是單槽檔

第一版把目標日期改由 `gathered_items.json` 決定。reviewer 抓到致命問題：

> **抓料（10:23 UTC）排在 routine（13:00 UTC）之前**，所以延遲那批會被隔天準時的抓料覆寫掉。第一版只有在「隔天也壞掉」時才生效——救不到「延遲一天後恢復正常」，而那才是延遲的常態形狀。

也就是說第一版仍然是補洞，只是洞換了位置。

### 正解：讀耐久的那一份

`src/gathered_archive/<date>.json` **本來就存在**：按資料日期分檔、已進 git、保留 14 天，`archive_gathered.py` 明文「檔名取 date 欄位，不取系統當下日期」。它是耐久的，`gathered_items.json` 是單槽易失的。

排程模式的目標 = archive 中每一個尚無 `news/<date>.md` 的日期，由舊到新；每個目標走**既有的** replay 路徑（補跑注意事項第 2 條：`cp archive → gathered_items.json`，跳過 Step 1a）。

| 情境 | 目標 | 結果 |
|---|---|---|
| 正常日 | `['08-29']` | 恰好今天一個，與現行行為完全相同 |
| 08-28 延遲到 21:00、08-29 準時 | `['08-28','08-29']` | 由舊到新各生成一次，**不遺失也不落後** |
| 抓料連續失敗 | `[]` | 本輪無事可做，寫心跳不算失敗 |

**一個新機制都沒加**：耐久產物、replay 路徑、冪等判斷全部是既有的。

### 連帶修正

- **0-1 新鮮度防線的相等檢查恢復**。第一版把它刪了，理由是「兩者恆等」——那個理由建立在已被推翻的單槽設計上。改讀 archive 之後，這道檢查驗的正是「cp 對了沒」（檔名只差一個字就 replay 錯一天），是真護欄
- Step 0b 的第三狀態消失：目標只會是「還沒有日報的日期」，冪等閘不可能觸發
- Step 1c 的 `--date` 由選配改為**必帶**（目標日非今日時漏帶會讓整批不確認、隔天重複提供）
- watchdog 的判準（今日抓料到位、今日日報存在）在新設計下**仍然正確**——沒有永久落後，所以不會誤報。reviewer 的這項顧慮只對第一版成立

### 六處過期文件同步

`workaround-register`（該列改為已收斂）、`daily-automation`（「3 小時鬆耦合」整段改寫，那個論述已被否定）、`cloud-runbooks/daily.md`、`_shared.md`（今日日期那格加註「目標日期不用此值」）、trigger 的 `_cron_note`、排程測試的模組 docstring。

### 這次學到的

第一版與第二版的差別只有一個詞：**單槽 vs 耐久**。而我第一版沒有問「這個資料活多久」——直接抓了最順手的那個檔。reviewer 的 A1 不是靠讀程式碼發現的，是靠**把兩個 cron 的時刻排在同一條時間軸上**看出來的。

---

## 2026-08-29 Query：「歸納我對模型有興趣的主題」→ A 線（成本兌換率）四頁皆有落點但無入口，兩條規則補位

**使用者提問脈絡：** 先連續三輪追問「1M 與非 1M 收費差異」（本人公司走 AWS），再要求依 `wiki/reader-notes.md` 歸納其模型類興趣主題，並判斷該建新頁或補強既有頁的**產生內容方式**。

**歸納結果（三條主線）：** A 兌換率（08-01 自動模型路由、08-08 LLM code review 單位成本、本次的 1M／企業計費／tokenizer）｜B 信任（靜默降階，已在 `topics/code-quality-decline` 有子區塊）｜C 外部參照（07-12 GPT-5.6 ⏳、07-17 GLM/Qwen ✅）。

**揭露的缺陷：** A 線散在 `pricing`（費率）、`model-comparison`（選型）、`community-pattern-trends`（路由趨勢）、`coding-workflow-guide`（review 成本缺口）四頁，**沒有任何一頁的入口寫著「想算實付成本看這裡」**。且 `model-comparison` 全頁 `tokenizer` grep 零命中——於是「Opus 5 與 Opus 4.6 牌價同為 $5/$25、實付差約 30%」這件事，在選型入口上查不到；而 `official-community-gap:55` 早就記著「2026-06-27，Opus 4.7 tokenizer 改版成本大漲後爆發」，**現象在庫內有記錄，機制與量級從未被說明**。

**處置（不建頁，補強產生方式）：**
- `topics/model-comparison` 新增 h2 `## 同一份工作，換設定差多少`（成本面單一入口），內含 tokenizer 換代說明＋六模型實付換算表＋兩個結論（Sonnet 5 比 4.6 便宜／Opus 5 比 4.6 貴 30%）＋`count_tokens` 實測提醒；`pricing`、`official-community-gap` 各補錨點 wikilink 指向它
- `entities/pricing` 新增 `## 通路與乘數`（通路五列＋乘數八列，含長脈絡分世代：4.6 以後不加價／Sonnet 4-4.5 世代超過 200K 輸入 ×2 輸出 ×1.5）
- `topics/code-quality-decline` 新增「對選型的影響」段，反向連回 model-comparison
- 規則：`wiki-ingest-models.md` 新增 **I 條**（換代若動到 tokenizer／費率／context 政策，實付成本必須落地於上述 h2；不得為此加欄，撞 H 條）
- 規則：新建 `.claude/rules/wiki-ingest-commercial-lint.md` ＋ `/wiki-lint` **5e**（通路與乘數吃官方計價文件、非日報，主編查證維護）

**顧問 agent 攔下的兩個錯誤（本次派 agent 對抗性檢視提案，兩條被推翻）：**
1. **通路與乘數原擬為商業記者 daily 責任 → 層級錯。** 該規則檔自己的「官方文件查證優先於媒體轉述」已明訂記者無 web 工具；寫成 daily 會製造一個永遠空著的區塊。改為主編 lint（5e）＋獨立 lint 規則檔，符合 lint-only 規則須分檔的鐵則
2. **08-08「review 成本」原擬升為懸置標記 → 已撤回。** (a) 前提不成立——`reader-notes` 的 ⏳ 本就由 `/wiki-weekly-review` 與 `/weekly-report` 消費，且 08-09 已消費過一輪；(b) 該題無可查的一手來源，主編 5c 永遠結不了案，會長期佔 `pending_overdue` 成為固定假警報，正是 `.claude/rules/wiki-ingest-features.md` 08-28 才立法反對的型態

**顧問另指出、本次未處置（待使用者裁示）：**
- **A 線其實是兩題**：「換設定差多少」（可算，本次已治）與「這個月為什麼比上個月貴」（歸因，`pricing` 事故區 40+ 條幾乎全屬此類，未治）
- **C 線觸犯 08-28 剛立的「⏳ 停車場」規則**：07-19 改被動觸發至今 41 天，失敗原因是**結構性 venue 缺口**（評測部落格不在 12 來源內、`topic_watch.json` `_global_max: 8` 已滿），非「等待中」。應標明「結構上收不到」並寫進 `competitor-landscape` 的蒐集邊界欄，或讓出一個 topic_watch 名額

**驗證：** `python scripts/run_tests.py` 363 案例全過（exit 0）；`check_rules.py` 五項全過；新增的兩條錨點 wikilink 經 `check_wikilink_anchors()` 驗證無 WARN。原擬指向 `code-quality-decline` 子區塊的錨點因該標題帶 `` `[2026-08-09 查證新增]` `` 標記、而錨點檢查只剝粗體不剝反引號，改為純頁面連結＋文字指路。

---

## 2026-08-29 根本修法（第三版，定案）：把緩衝加在消費者，不是增加生產者

前兩版都被 reviewer 推翻，而它們錯的方式不同：

- **v1**（目標取自單槽 `gathered_items.json`）：抓料排在 routine 之前，延遲那批會被隔天準時的抓料覆寫 —— 只有「隔天也壞掉」時才生效
- **v2**（目標取自耐久 `gathered_archive/`，補跑所有缺日）：有效，但 reviewer 找到 6 個問題，**全部源自「補跑多天」這個語意** —— 壞掉的 archive 會 head-of-line 卡死其後所有日期、較舊的日報晚於較新的上站導致 wiki 逆序 prepend、迴圈邊界未定義讓無人值守 agent 必然違反「只能 push 一次」、本機與雲端對「今天該產哪幾天」給出兩個答案

### 一個我十輪來都沒查的事實

`main.py` 的 `check_gap_lookback()` **在昨日日報缺件時自動把回看窗從 26 小時拉到 50 小時**。實證：08-29 的抓料含 13 則 08-28 發布的條目。

也就是說**漏掉那天的內容早就有保護**。缺的只是「那個日期有一個檔案」—— 而 v2 為了補那個檔案，付出逆序與卡頭的代價。這筆交易不划算。

我在建 v1／v2 之前都沒有先問「漏掉那天的內容到底丟了沒」。

### 定案：一個數字

根因是**消費者的緩衝（2.6h）小於生產者的實測變異（11.2h）**。前幾天我加保險窗 cron 是在**增加生產者**，那是補洞；v2 是在增加語意。正解是把消費者移到變異之外：

```
雲端 routine   13:00 UTC → 23:00 UTC     緩衝 2.6h → 12.6h
```

連帶把兩個 watchdog 移到 routine 之後（15:00 → 01:00 UTC、23:00 → 01:30 UTC），並改查**前一個 UTC 日** —— 不移的話它們會在 pipeline 還沒跑完時天天誤報。

代價：日報由台北 21:00 改為隔日 07:00 送達。內容涵蓋範圍不變（抓料時間沒動，仍到台北 18:23）。

### 測試

釘住的不變式是「緩衝 > 實測最大變異」與「routine 不跨 UTC 午夜」。破壞測試：移回 13:00 → 紅、改成隔日 02:00 → 紅、改成 22:00 → 綠（11.6h 確實大於 11.2h，通過是正確的）。

**寫破壞測試時抓到自己的兩個 bug：** 第一次破壞測試用 `json.dump(d, open(...))` 沒關檔，subprocess 讀到舊內容，三個突變全部假綠；修掉之後又發現 `_crons()` 的 regex 把註解裡那句「加回 `- cron: "17 0 * * *"` 即可」也當成真 cron，於是緩衝算成 12.7h 而非 2.6h，整條不變式失效。**兩次都是「護欄自己壞掉而看起來是綠的」** —— 與這個 session 前九輪反覆出現的形狀完全相同。

### 殘餘風險（誠實登記，取代 v2 的「已收斂、無待辦」）

延遲若跨過 UTC 午夜（>12.6h），抓料寫成隔天檔名，該日仍無日報 —— 但內容由 50 小時回看併進隔日。不修的理由三條都寫進登記表：再往後移就跨午夜、加抓料班次是增加生產者（已試過撤回）、掃 archive 補缺日會造成逆序（已試過撤回）。

---

## 2026-08-29 收尾：七輪 review 的帳

前面那筆記的是修法。這筆記**七輪 review 各自抓到什麼**——因為抓到的東西比修法本身更值得留。

| 輪 | 項數 | 最重要的一項 |
|---|---|---|
| 1 | 17 | 三條斷言是假綠的：`assertLess(routine, 24)` 恆真、緩衝取 `min(抓料班次)`（而決定緩衝的是最晚那班）、碰撞用 `abs()` 不繞午夜 |
| 2 | 7 | 我把耐久資料給了觀測者，**生產者還在吃易失的單槽檔**；而看門狗的抓料判準讀單槽檔，等於在唯一的告警管道上裝了一個對事故本身敏感的假警報 |
| 3 | 7 | 同一個「緩衝小於實測變異」的根因**原封不動留在週更那條線上**（linkcheck → weekly lint 只有 7 小時） |
| 4 | 5 | 上一輪那個 `cp` 會弄髒工作樹，而 `rebase.autoStash=false` 讓 push 重試的 `pull --rebase` 被前置檢查拒絕——**只在 `cp` 唯一有作用的那天發作** |
| 5 | 4 | 還原規則在 Step 1a 還留著一份舊副本，而 Phase A 只讀得到那一份 |
| 6 | 2 | 中止落地的食譜沒跟上同一批改動新立的規則；看門狗的補跑建議沒跟上同一批改動寫的裁決 |
| 7 | 0 | — |

### 三個一再出現的形狀

1. **護欄自己壞掉而看起來是綠的**（第 1 輪三條 + `_crons()` regex 吃到註解 + `json.dump` 沒關檔讓三個突變假綠）。共五次。每一次都是「寫了測試」與「測試有效」之間的落差，而唯一能分辨的動作是破壞測試。
2. **只修一半**：第 2 輪把資料來源換給觀測者卻沒換給生產者；第 3 輪對 README 下的診斷（「副本刪掉比加護欄好」）沒套用到同一天改的另一條線；第 6 輪的兩項都是「同一批改動內部沒對齊自己新立的規則」。
3. **修 A 引入 B**：第 4 輪那個 `cp`。而它的解法不是再加一層，是把一條既有規則的適用範圍放寬。

### 淨形狀

七輪下來，真正的行為改動是：**三個 cron 數字、一支腳本換資料來源、一行 `cp`、一條 checkout 移位**。期間主動撤掉的東西比加上的多——保險窗 cron、掃 archive 補缺日、以及第 3 輪自己上一輪才加的那條 README 逐字比對測試。

### 還沒解決的

- `news/2026-08-28.md` 仍缺。內容已由 50 小時回看併進 08-29，補跑會產出大量重複且讓 wiki 逆序 prepend，故不補（看門狗的建議文字已補上這個 caveat）。
- 消費者側已無空間：緩衝 11.62h、餘裕 25 分鐘，而 22:00 + 執行時間正好等於 UTC 午夜。下次變異超標時該動的是**抓料往前挪**，不是再挪 routine。這句寫進了 `OBSERVED_MAX_DELAY_H` 的註解。

---

## 2026-08-29 08-29 的日報其實是 08-28 的——本機用台北日期，雲端用 UTC

使用者指出「早上那個應該算 28 號的」。查條目日期分佈，證實了：

| 日報 | 條目日期 |
|---|---|
| 原 `news/2026-08-29.md` | 08/26 三則、08/27 十七則、08/28 廿一則，**08/29 零則** |
| `news/2026-08-27.md`（正常樣貌） | 08/27 廿四則為主 |

### 根因

那份是**台北 00:44** 跑的本機補跑，而本機 pipeline 拿台北日期當 TARGET_DATE——那一刻的 UTC 日期是 08-28。**台北 00:00–08:00 這個窗內，本機比雲端多算一天**，而深夜補跑正好落在那個窗裡。標頭寫的「00:44 UTC」也是同一個錯，那是台北時間。

### 為什麼不能放著

它佔住 08-29 的檔名，於是當天真正的新聞被 `Step 0b：冪等閘` 擋在門外——今天 12:04 UTC 那一班就是這樣中止的，而 17:00／22:00 兩班也會。**錯標一天不只是標籤錯，它會吃掉一整天的日報。**

### 處置

改標資料層：日報檔名與標頭、web digest、2 處 `[[news/2026-08-29]]` wikilink、歸因帳本 36 筆。**沒動 wiki 頁面的日期欄位**——「最後更新」記的是哪天被編輯，08-29 台北編輯是事實；「最後新聞更新」等今晚真正的 08-29 日報進來時自然更新，現在改只是製造 churn。

根因修在 `.claude/commands/news-pipeline.md`：TARGET_DATE 明訂取 `date -u +%F`，與雲端一致。

### 順帶記一筆今天的排程觀測

GH Actions 抓料排 10:23 UTC，到 14:45 UTC 仍未落地（+4.4 小時且持續中）。08-26 那場 critical 的 Actions 事故餘波尚未退乾淨——連續第三天。三班重試（12/17/22 UTC）的設計正是為此，最後一班涵蓋 +11.6 小時。

## 2026-08-29 Ingest（第二輪；當日真正的 08-29 日報）

- 來源日報：[[news/2026-08-29]]（本檔第一輪「2026-08-29 Ingest（含 08-28 缺日補救）」處理的是誤標為 08-29、實為 08-28 的日報，已於當日稍晚更正檔名；本輪才是真正的 2026-08-29 內容，17:00 UTC 班次執行）
- 更新頁面：wiki/entities/claude-code.md、wiki/entities/dario-amodei.md、wiki/topics/anthropic-business.md、wiki/topics/ai-talent-flow.md、wiki/topics/community-tech-patterns.md、wiki/topics/community-tech-discussions.md、wiki/topics/anthropic-government-policy.md、wiki/topics/ai-agent-safety.md、wiki/topics/recursive-self-improvement.md、wiki/feature-radar.md
- 新增頁面：無
- 摘要：聯邦法官裁定五角大廈將 Anthropic 列入供應鏈黑名單違法（第一/第五修正案理由，點名 Hegseth）持續發酵；資安研究者 Alon Hertz 揭露 llms.txt／llms-full.txt 套件搶注供應鏈風險，另有研究顯示僅需請 Claude Code 摘要網站即可誘發被騙；Anthropic 自陳「自動化研究員」能可靠緩解對齊失誤，媒體解讀為 Claude 早期自我改進跡象；Claude Code v2.1.251 新增 PreModelSwitch／PostModelSwitch hook 事件。
- 呈現品質：全部通過
- 轉知帳本：H-1813db（人物→商業，Jensen Huang wikilink）已於本輪結案；安全政策記者新開 H-0d4176、H-871320（轉知功能記者評估 Auto Mode 繞過與 llms.txt 摘要誘騙是否列入 claude-code.md 已知問題），待下輪功能記者派工時處理

## 2026-08-30 Ingest

**日報：** `news/2026-08-30.md`（13/13 來源、40 條）

**派工：** 四類（功能／商業／社群／安全政策）。模型與人物今日無條目——騰訊 Hy4 Preview 屬競品動態歸商業 `competitor-landscape`，r/LocalLLaMA「中國 LLM 追上 Opus 4.8」屬社群討論面。

**記者回報摘要**

- **功能**：`entities/claude-code` 新增已知問題 5 則（Desktop Windows 當機 #85199／`--quiet` 旗標請求 #9340／context 狀態列對 Sonnet 4.6 顯示 200k #61734／Max 帳號被導向新帳號 onboarding 第 10 次通報 #83633／The Register llms.txt 信任誘騙），GitHub connector #71542 互動數 48→60，群組計數三處同步。轉知 2 筆全數處理並結案（H-0d4176 Cybernews「修復被拒絕」細節、H-871320 llms.txt）
- **商業**：`entities/pricing`（週配額換軌）、`topics/anthropic-business`（Sony／Warner 版權訴訟、OpenAI 退出 Cursor 由 Anthropic 承接）、`topics/ai-talent-flow`（DeepMind 頂尖人才佔比下滑）、`topics/competitor-landscape`（騰訊 Hy4 Preview 770B 開放權重）。Yahoo Finance「營收年增 1,000%」與 08-28 既有記錄同一事件，未重複新增
- **社群**：`community-tech-patterns` 收 gstack（Garry Tan 的 23 工具角色分工設定）、awesome-llm-apps（存量盤點）、dev.to 遞迴刪檔第一手記錄（新風險類型節點「模糊敘述觸發破壞性自主行動」）；`community-tech-discussions` 收 Ask HN 戒除依賴（HN 11 分，剛達低門檻，🔥☄️閃現）。best-claude-hud（501 星、單一訊號）留給週更策展；r/LocalLLaMA 該串 score 恆 0＋source_count=1，未達任一門檻不收錄
- **安全政策**：`topics/ai-agent-safety` 收編碼代理 70 次重複錯誤模式、dev.to 刪檔事件的 agent 安全邊界面

**主編彙整**

- `feature-radar.md`：⏰ 倒數中 換軌——原「2026-08-31 +50% 促銷結束（動向未公布）」改為「**2026-09-14** 標準週配額永久 +25%、同時取消 +50%，淨減約 17%」。該促銷不是單純到期，是被永久制度接手但水位低於現況
- `index.md`：無狀態變更（`topics/long-context-1m` 列已於本日稍早建頁時加入）
- `data/source_attribution.jsonl`：append 18 筆
- 轉知帳本：安全政策記者請轉知社群記者處理 dev.to 條目的 pattern／防護面——**同輪社群記者已自行收錄該條目**，需求當場滿足，不登帳

**🔧 觸發邊漏接（本日發現並修正）**

`topics/long-context-1m` 是 2026-08-30 稍早建的衍生頁，觸發邊當天登記於 `.claude/rules/wiki-ingest-features.md`。**首次受測即漏接**：#61734（狀態列對 Sonnet 4.6 顯示 200k，該模型實際支援 1M，24 則留言）被功能記者正確寫進 `claude-code` 已知問題，卻未同步 1M 頁。

原因不在記者——原觸發表列的是「預設行為、開關、model picker、`[1m]` 變體」四類，**沒有「可見性」**。而「你看不出自己在不在 1M 上」正是控制權缺口的一種：前三條缺口（關不掉、選定保不住、`[1m]` 自成 id）都因為第四條而更難自救。

處置：(a) 觸發表新增「1M 的可見性——狀態列／`/model`／設定畫面顯示的 context 上限與實際不符」一類，並明寫「不因為它『只是顯示問題』而排除」；(b) 頁面「三個你控制不了的地方」改為「你控制不了的地方」共四列，新增 #61734 列、時序 prepend、callout 覆寫為 08-29 該則。

**可攜教訓：** 新建衍生頁的觸發表若以「現有證據的分類」列舉，就只涵蓋得了建頁當天手上那幾條。**列舉式觸發邊要在第一次受測時複查一遍**——漏的那類通常不是罕見情況，而是建頁時剛好沒發生過的常見情況。

**📋 待使用者裁示**

本輪 ingest 無新增待裁示項。`/wiki-lint` 08-29 輪留下的 7 項已於本日 `/weekly` 步驟 0.3 直接呈報給使用者，等待回覆。

## 2026-08-30 Weekly（W35）：週報＋本機專屬步驟補跑＋積壓裁示清空

### 步驟 0：本機專屬步驟補跑

- **5b 跨家榜單週更**：派 Haiku 抓 18 榜，**刻意不整表覆寫**。回報有兩類可靠度問題：(a) 名次與分數自相矛盾——SWE-bench 把 96.2% 的 GPT-5.6 Sol 排在 96% 的 Opus 5 之後第 4，OCR 把 90.1% 排第 3，**兩處恰好都是「非 Claude 會擠掉 Claude」的爭點**；(b) 18 榜中 13 榜與上週逐字相同，而抓取端為取 URL 已先讀過該頁，無法分辨查證與回抄。只更新三列可獨立辨識的變動（TTS 換 Sonic 3.6、改圖換 MAI-Image-2.6-Preview、OpenRouter 日期），其餘保留原值與**原資料日期**，不以抓取日冒充新鮮度。理由寫入該頁「本週註記」，並留一條待查證：GPT-5.6 Sol 是否已在 SWE-bench Verified 超越 Claude 陣容。Aider Polyglot 停更滿 3 週，達汰換門檻。
- **5c 逾期待查證清算**：完整報告 WARN 0 筆。Lane A 8 筆全處理——4 結案（feature-radar Fable 5 配額政策、coding-workflow-guide 跨模型互審方法論、government-policy 浮水印機制 ×2）、2 改 🔎 查無官方（dario-amodei ×2）、1 推複查日（pricing resale）、1 **誠實退回 Lane B**（claude-security ⟨Q-01⟩ 需查產品文件，本輪未查）。Lane B 43 筆未動（本輪額度用於 Lane A 與回掃）。
- **lint 待裁示呈報**：7 項已直接呈給使用者（不只寫進本檔），使用者回覆「都改」，處置見下方。

### 🔧 5c 第 5 步結案回掃：抓到事實錯誤，不只是過期

浮水印機制查實後拿探針回掃全庫，發現**三處寫「2026-08-14 官方已開放第三方偵測 API」是錯的**。查官方原文：「We **will soon be offering** a watermark detection API. We're in the process of working out the details」——API 至今不存在，無時程、無門檻、無費用。the-decoder／BleepingComputer／PCMag 三家同步把「即將提供」寫成「已開放」，本庫沿用未查。

已更正 `topics/anthropic-government-policy` 四處（摘要表、攻防紀錄、08-13 條目、浮水印政策主段），並把官方機制說明寫成事實取代原懸置：只作用在兩個用詞一樣好的低風險選擇點、隨機性由密碼學金鑰與前文決定、模型層施加跨介面一致、**輕度編輯多半移除不掉但逐字重寫會**（官方用語 probably，未給殘留率數字）。品質犧牲疑慮與「可移除」聲稱兩條亦據此上修。

**可攜教訓：** 「多家媒體同步報導」不等於查證——三家可以同時誤讀同一份官方公告的同一個時態。**媒體轉述與官方原文的差異，最常出現在「已經」與「即將」之間。**

### 步驟 1：週報

- 產出 `weekly/2026-W35.md`。頭條走**配額換軌**（09-14 起 +25% 永久、同日取消 +50%、淨減約 17%）→ 算力承諾回壓 → **靜默換模**本週官方給出 `PreModelSwitch`／`PostModelSwitch` hook，但 #61734 顯示連 context 上限都顯示錯。
- 深挖：〈牌價一樣，帳單不一樣——換模型前先看 tokenizer〉。**命中 `reader-notes` 擱置 29 天的 ⏳「成本感知的自動模型路由」**，該筆已標 ✅。
- **帳本回收 9 條全數結案、續盯 0——本刊首次全收**。其中兩條的結案伴隨本庫既有記載的更正（Sonnet 5 促銷結束日在 W34 寫下時已作廢 12 天；浮水印偵測 API 誤寫為已開放）。
- ⚠️ **深挖 1,672 字，連四期超出 800–1,200 規格**（W33 1228／W34 1523／W35 1672，且逐期遞增）。W34 已提「檢討該上限是否需含 URL 字元」，本期不為過檢查而砍機制層內容，列為規格校準項。

### 步驟 0.3 裁示處置（使用者 2026-08-30 回覆「都改」）

| # | 事項 | 處置 |
|---|---|---|
| 1 | Model Hardware Standard 是否建 entities 頁 | **不建**。已進 feature-radar，符合「今日首見先附記、明天再評估」；全新產品線但僅一個公告事件，未達建頁門檻（名稱＋狀態＋至少一個事件中的「事件」僅有發布本身）|
| 2 | 來源記分卡 GitHub 雙低是否調門檻 | **不調，列長期觀察**。連兩週 Wilson 下界 17%／Presence 6%，但星數類條目本就少被 wiki 採用，屬結構性偏低非品質問題 |
| 3 | `claude-code.md` 逾百筆儲存格 > 120 字元 | **另立專項**，已登記 `docs/workaround-register.md`（owner Claude，複查日 2026-09-27），分批以月份區間處理 |
| 4 | 未註冊 slug `business-chief` | **已修**。`data/source_attribution.jsonl` 該筆 source 由媒體名 `business-chief` 改為 `google-news`（1 筆）|
| 5 | `[存量盤點｜…]` 前綴誤印 | **已於 2026-08-29 完成**，本項為清單殘留。規則已改為「翻譯」而非禁寫，今日日報兩則存量條目均為正確格式 |
| 6 | 6c 呈現品質 rollup 明文行降至 1/3 | **認可表格式**。`/wiki-lint` 6c 合格標準加註「明文 rollup 行與表格式摘要等價」——該規則要的是「有沒有審查」，不是版面形式 |
| 7 | `community-tech-patterns` 淘汰／拆分 | **已執行**。刪除「跨 Session 通訊插件（2026-05-07）」整節（`/qu`／`/ans` 已由官方 `ListAgents`／`SendMessage` 完全取代，v2.1.224，官方文件 2026-08-09）；「Session 記憶與搜尋工具生態」拆分——移除被取代的「多 session 互通（Claude Relay）」子條目，保留語義搜尋與本地 RAG 兩條並加「官方趨勢觀察」callout 註明**未被取代的是編排層**（官方只給點對點原語，不含依相依性自動排序）|

### 步驟 2：未執行

`/wiki-weekly-review` 的六記者並行策展判斷本輪**未執行**。使用者回覆「都改」係針對上列具體改動，六記者 fan-out 屬分析步驟且為本輪最大單筆開銷，未逕自啟動。`reader-notes` 消費已單獨完成（1 筆結案、3 筆維持 ⏳，最舊 49 天）。

## 2026-08-30 週度延伸回顧（W35，`/weekly` 步驟 2）

**聚焦校準：** 非本月首次（08-01 已執行，聚焦命中率 76%），依規則跳過。

**六記者並行判斷結果：** 四位回「無」（模型、社群、商業、人物加碼面），兩位各提一條。

四位「無」的共通理由值得記下來：本週最大的幾條線（「模型被削弱」爭議、token 消耗異常、跨 harness 工具潮、IPO／算力軍備、DeepMind 人才流失）**當天就被歸進正確的既有頁面並互相 wikilink 了**，沒有出現足以突破現有結構的訊號密度。這是分工運作正常的樣子，不是漏判。

**使用者確認「都做」，已執行三條：**

1. **`topics/official-community-gap` 新增矩陣列 ⟨G-11⟩ 跨 harness 統一操作層**（功能記者提）：08-24～08-27 四天內至少 7 款同類工具湧現，三款星數逾 4,000（loopx 5,067★、Graft 4,842★、devspace 4,020★），08-27 單日五款同批亮相。**與既有 ⟨G-08⟩ AGENTS.md 列不同層**——那條談設定檔格式相容，本條談執行期統一操作層；亦與 ⟨G-09⟩ 可觀測性不同（G-09 問「我的 agent 在幹嘛」，本條問「不同廠牌的 agent 能不能在同一處操作」）。官方無對應：`ListAgents`／`SendMessage` 只涵蓋 Claude Code 自己的 session。
2. **`topics/ai-agent-safety` 新增合成段「提示注入已不是單點漏洞，是產業級攻擊面」**（安全政策記者提）：七天內六天觸及同一敘事，六則訊號以表格並陳（HackerNoon RCE 原語 08-23／VentureBeat OWASP 第一但事故第 12 08-26／gbhackers MCP＋記憶層 08-27／Wiz 90 天蜜罐 08-28／Alon Hertz `llms.txt` 120 份未註冊套件 08-29／StartupHub 70 個重複錯誤模式 08-30）。收斂點寫明：共通結構是**代理把外部內容當可信輸入，沒有任何一層在問「這段文字憑什麼可信」**；仍未有答案的落差（OWASP 第一 vs 事故第 12）誠實標出。
3. **`entities/dario-amodei` 移除配偶人物側寫條目**（人物記者建議，使用者裁決）：四家媒體跨 8 天全停在標題層級的定性詞（"first lady of AI"），無一觸及具體職務或對公司決策的影響。**判準是 `CLAUDE.md` 的收錄標準**——一位非公眾人物的婚姻側寫答不出「能否幫工程師更了解 Claude/Anthropic 生態系」。

   **移除範圍：正文條目、參考來源 4 筆、歷史記錄 3 筆、現況段 1 段、失去依附的 HN 討論串 1 筆，共 8 行。** 只移正文那條會留下參考來源與歷史記錄，等於沒移——這點在執行時才發現，值得記：**移除條目要跟著移除它的來源與歷史錨點**，否則讀者從參考來源仍讀得到同樣資訊。`log.md` 為 append-only 歷史，其中既有記載不回改。

**模型記者附帶提醒（未列入本輪執行）：** `topics/code-quality-decline` 的「Opus 5 上線後品質感知訊號群」已累積 14 則，**若下週破 20 則，可能該從純訊號記錄升級為有結構的獨立子頁**。屬社群記者／主編 lint 職權，記於此供下輪參考。

**功能記者與社群記者對同一批工具的判斷分歧（已解）：** 兩人都看到跨 harness 工具潮，功能記者要在官方缺口矩陣開列、社群記者說 `community-tech-tools` 已標最高熱度屬「已加碼中」。兩者不衝突——工具目錄追的是「有哪些工具」，缺口矩陣追的是「官方補了沒」，後者確實空著。已在 ⟨G-11⟩ 細節區加 wikilink 指向前者，避免兩頁各自長出重複清單。
## 2026-08-31 Ingest

**日報：** `news/2026-08-31.md`（13/13 來源、61 條）

**執行脈絡：** GitHub Actions 排程派工延遲惡化（本日 00:17 UTC 排程至 14:30 UTC 仍未建立 run；Actions 官方狀態頁無事故，08-27～30 實際觸發延遲 +14.6h～+20.9h），雲端 12:00 UTC 班被新鮮度防線正確擋下後改本機補跑：本機抓料 14:36 UTC → 日報 → 本 ingest。雲端 17:00／22:00 班將由冪等閘自動中止。

**派工：** 四類（功能／商業／安全政策／社群）。模型與人物今日無條目——alignment 研究與自我改進報導屬 recursive-self-improvement（安全政策）、benchmark 波動分析屬社群討論面。

**記者回報摘要**

- **功能**：`entities/claude-code` 新增已知問題 2 則（#61869 1M context 需另開用量額度、#36582 終端機捲回頂端）＋ Compliance API 懸置標記（❓ 待查證，僅媒體報導無官方文件，複查 2026-09-14）；#61869 依 1M 觸發邊同步 `topics/long-context-1m`（控制表＋callout＋時序）。#80444／#65833／#10238 均為既有條目無新資訊未重複寫入。「AI agent 操作實體機器介面」僅標題可見，不足以判斷落點，本輪不建條目
- **商業**：`entities/pricing`（週配額實質降規 17%，社群比較值標示）、`topics/anthropic-business`（Sony／Warner Chappell 正式提告、AWS GovCloud、FTX 股權處置、Claude for Teachers 免費開放美國學區）、`topics/competitor-landscape`（Google 低價定價策略——影音報導無具體費率標待查證、36氪 DeepSeek Harness 免費替代討論）
- **安全政策**：`topics/ai-agent-safety`（Auto Mode 提示注入實測 60–80% vs 官方評測 0% 並陳、infostealer 竊取 Claude session 警示、LM Studio Bionic 定向條目）、`topics/anthropic-government-policy`（五角大廈供應鏈風險標籤判違法 Anthropic 勝訴、中國對美中 AI 對話設條件）、`topics/recursive-self-improvement`（自動化對齊研究 10/10 修復＋2.4% 作弊並陳）
- **社群**：`community-tech-discussions` 新增 session URL 歸因議題（#66504 經 HN 延燒）＋ co-author 去標註轉向文並陳、benchmark 跨日波動 8.4 分（週熱門）、週配額反彈記入額度焦慮系列 🌊延燒；同步清理 4 筆逾 21 天 ☄️閃現與 1 筆孤兒懸置細節。dev.to 兩則為既有條目重出未重複收；存量盤點 4 repo（cc-switch 13.0萬星、graphify 11.3萬星、storybloq、awesome-claude-code）留待週更策展

**主編彙整**

- `feature-radar.md`：無新增條目、無熱度變動、版本無異動——radar 本輪不動。本週推薦「無新達標」已持續 16 天（最後輪替 08-15），接近 3 週檢討線，下輪再無替補須標 ⚠️ 檢討 🔥🔥🔥🔥 門檻
- `index.md`：無狀態變更、無新頁
- `data/source_attribution.jsonl`：append 27 筆
- 轉知帳本：開 H-616500（安全政策 → 功能：Auto Mode 注入數字升級，評估同步 claude-code 已知問題）
- 懸置命中判定：S 級 1 筆（`topics/anthropic-commitments` L55）為**假命中**——探針僅命中 `[[entities/pricing]]` wikilink 展開詞，命中條目是 CNBC「Google 低價 AI 定價」，與 Fable 5 訂閱內含承諾無關，不標訊
- 官方查證（社群記者轉知）：週配額 17% 降規——WebFetch `support.claude.com` Pro/Max 說明頁，**查無週配額具體數字、查無異動記載**；pricing 維持「社群比較值／媒體稱」標示正確，官方數字缺席本身已記入 08-30 radar ⏰ 倒數中（09-14 換軌）

**📋 待使用者裁示**

本輪 ingest 無新增待裁示項。

## 2026-09-01 Ingest

**日報：** `news/2026-09-01.md`（13/13 來源、71 條）

**執行脈絡：** GH Actions 抓料 15:00 UTC 落地（排程 10:23，+4.6h），雲端 12:00 班正確中止；使用者要求提早出報，本機以 archive replay 補跑（料同源、未重抓）。同日使用者裁決：**交付期望改為隔日早上可讀**，台北 20:00 目標作廢（commit e4d695a7，trigger 註記／workaround-register／daily-gather.yml 三處同步，並修正「六班」誤記為三班 12/17/22）。

**派工：** 五類（功能／商業／安全政策／社群／模型）。人物無條目；DeepMind 四主管流失屬 ai-talent-flow 定向條目歸商業。

**記者回報摘要**

- **功能**：`entities/claude-code`——v2.1.252 版本表、08-31 兩起服務降級（同日解決）、#22931 Cowork 封存消失（新增）、#15942／#20697／#52871 互動數更新；**H-616500 已處理**：Auto Mode 注入 60–80% vs 0% 已同步安全與隱私條目並升級嚴重度。radar 無新增（v2.1.252 純 bug fix）
- **商業**：`anthropic-business`（Lambda 350 億雲端合約、8.5 萬認證、Trifecta 採用）、`competitor-landscape`（Meta Muse Code 出 beta 三層訂閱，無公開費率標待查證）、`pricing`（20x 僅 5 小時視窗的誤導爭議；官方 Fable 5 計費頁與 07-20 既有記錄一致未動筆）、`ai-talent-flow`（DeepMind 同日四主管，人名未載標懸置防誤併 08-05 批次）
- **安全政策**：官方部落格首度併案檢討 07-30 三起評測環境連網＋08-04 UK AISI Mythos 5 事件，承諾 METR 獨立審查、已恢復外部測試——`ai-agent-safety` 以「既有事件官方升級」處理不新建列；`anthropic-government-policy` 五角大廈判決第三度重申標無新事實。**懸置標訊 2 筆**：infostealer（訊 09-01）、recursive-self-improvement 自動化研究員機制（訊 09-01，官方文聚焦資安非該機制，維持 ❓）
- **社群**：`community-tech-patterns` 收 agent 記憶否決記錄（縫合索引記憶主線）；`community-tech-discussions` 額度焦慮系列補 20x 誤導＋撞限雙節點。oh-my-subagents／Blume（HN 各 3 分）未達門檻不收；存量盤點 caveman／open-design 留週更策展
- **模型**：`entities/mythos`——UK AISI 事件與頁面既有 08-05 記錄確認為**同一事件**（官方首度正面回應），三處交叉標明防讀者誤判新案例；`fable-5` 促銷到期敘述 grep 核對已一致未動

**主編彙整**

- `topics/anthropic-commitments`：新增追蹤列「與 METR 合作獨立審查訓練環境安全事件」（🟡 進行中，2026-09-01）
- `feature-radar.md`：無異動。本週推薦「無新達標」已 17 天（最後輪替 08-15），下輪再無替補須標 ⚠️ 檢討門檻
- `index.md`：無狀態變更、無新頁
- `data/source_attribution.jsonl`：append 21 筆
- 轉知帳本：H-616500 已結案（功能記者處理完畢）
- 品質備註：商業 歸因欄多筆未附完整 URL（主編以日報原文補齊）；安全政策 歸因欄同病 2 筆（已補）；模型 回報訊息夾雜一段簡體（頁面本文無此問題）

**📋 待使用者裁示**

本輪 ingest 無新增待裁示項。


## 2026-09-02 Query：「單點依賴是你，我比較想解決這個」→ 質疑題庫＋時效燈建成

**點出什麼：** 專案成熟度自評指出「系統品質的最後一道防線是使用者的好奇心」後，使用者要求解決此單點依賴。追查發現：(a) 排程內抽查（收報核對、行為層抽驗、5d）全由 AI 主編執行，使用者的角色其實是「考卷外質疑者」；(b) 回顧全部 35 筆 Query 條目，歷史上所有重大品質問題（25 則靜默消失、漏收 48%、Dreaming 假死案、懸置 20 天、排程從未建立…）零次來自排程檢查、全部來自使用者不定期質疑；(c) 該質疑歸納後僅七種模式，全部可操作化；(d) 順帶揪出行為層抽驗的「隨機抽」無擲骰程序——LLM 自由心證的隨機會養出免檢區。

**處置：** `scripts/inquiry_bank.py` 七題質疑題庫（溯源／缺席偵測／沉默質疑／讀者查找／可讀性／結構健檢／宣稱對帳，每題附機械探針、seed 綁 ISO 週防重擲換題）；`/wiki-lint` 新增 7b 歷史質疑代打（每輪抽 2 題）；`scripts/open_loops.py` 新增 [6] 人類質疑時效燈（最新 Query 逾 21 天亮 ⚠——題庫只代打已知模式，新型質疑仍靠使用者，燈不因代打而熄）；行為層抽驗補真隨機擲骰程序；規則檔 `.claude/rules/wiki-lint-inquiry.md`＋registry sync_pair＋4 組回歸測試。commit 9ba6b03a、e60a4000（後者為連帶修復：懸置棘輪 147→145）。

## 2026-09-02 Lint（本機執行，7b 質疑代打首跑）

- 修正矛盾：無（六記者跨頁比對均一致）
- 補連結：無（全庫無孤立頁面）
- 狀態更新：無
- resolved 收尾：無
- 新增 entities：無（步驟 4 掃描 Nscale／Lambda／Muse Code／Claude Academy／Trifecta 均僅 1 頁提及，未達 3 次門檻）
- 呈現品質：商業 4 頁 ⚠️ 已修復（pricing 12 處維運術語洩漏、anthropic-business 5 處、competitor-landscape 4 處、ai-talent-flow 1 處——「留給 X 記者／需主編查證」等內部用語改寫為讀者語言或轉標準懸置標記）；社群 3 頁 ⚠️ 已修復（patterns／discussions callout 未反映 09-01 節點已覆寫、timeline 凍結頁 callout 誠實化）；其餘全部通過
- 入口層健檢：>500 行七頁（claude-code 793、coding-workflow-guide 608、patterns 1696、discussions 1304、ai-agent-safety 1201、pricing 719、anthropic-business 886 等）均具入口層，無語意分岔／死案候選
- 待查證回訪：功能 4 筆改寫新語法（claude-code：Auto-continue、AWS Gateway、dreaming API ⟨Q-15⟩、1Password）；安全政策 4 筆改寫（LDAP、Cybernews 疑心較重、WSJ/SOFX、Yellow.com）＋清 4 處冗餘措辭；人物 5 筆改寫（Eureka Labs、Bloomberg 受訪者、數千 agent 出處、員工原型 ×2、STAT News）；商業 4 筆轉標準語法（pricing）；社群 3 筆補複查日；均註明「已掃日報至 2026-09-02 無後續；官方頁面未查證」
- 規則檔健檢：
  - 矛盾：無新增（check_rules 65 組 sync_pairs 全綠；本輪範圍：近期改動之 7b／inquiry 規則與既有檔）
  - 引用驗證：全部通過（6b 七項錨點皆在）
  - 遵守率：全部通過（近 3 次 ingest 3/3：品質標記／radar／格式）
  - 過期規則（> 60 天）：25 條 `[加入:]` 逾閾值（94 條在閾值內）——多為 5–6 月基礎條款，行為與現狀吻合者不動；未發現描述已失效者
  - 來源健康：13 來源 7 天全 ok=true；清冊型（Claude API Release Notes、Official Skills）count=0 屬正常；記分卡：Blogroll 51 天樣本充足、Google News 低信譽桶 0 筆
  - 跨檔案語意矛盾（6f）：✅ 全部配對語意一致（check_rules sync_pairs 65 組全綠）
  - 成長迴路（月度）：立法提案 0 條；觀察中 1 條（功能記者 08-27「全覽表缺口不存在」回報與實況不符，同型僅 1 次，已由行為層抽驗制度覆蓋）
- 品質指標（6g）：
  - ref 覆蓋率（每週）：100%（08-27~09-01，26/26），缺 ref 日期：無
  - 採用驗證率（月度）：radar 面 14 天前標 ⏳ 約 11 條，14 天內升級 0 條（0%，僅供判讀）
  - 外部死鏈（每週讀檔）：checked_at 2026-08-30（新鮮），dead 6／anti_bot 79；6 筆 dead 全數已標「（原文已失效）」（本輪補標 2 筆：community-tech-discussions 的 claude-needs-input、anthropic-business 的 daytondailynews；其餘 4 筆前輪已標）
  - 趨勢判讀：持平（連續 7 期 ≥97%）
- 跨家榜單週更（5b）：已更新素材取得 15 榜／3 榜無法取得（Search Arena、WebDev Arena、METR Time Horizon——METR 連續多輪僅互動圖表）；本輪依 Haiku 抓取回報整表覆寫至 model-task-leaderboard（含 SWE-bench 飽和、Terminal-Bench 版本混雜、AA 系列無官方日期、LMArena 重新基準化四項異常註記）
- 逾期待查證清算（5c）：盤點 67 筆（A1／B66），本輪處理 6 筆（查實 5／Lane A 推複查日 1／查無官方 0／失效移除 0），結案回掃上修 0 頁（探針回掃命中皆無關或已一致），剩餘 61 筆。查實明細：andrej-karpathy（Eureka Labs 為暫停非解散，Karpathy 自述日後恢復）、boris-cherny ×3（微管理原文全文——框大目標讓 agent 自行導航；Electron 桌面應用改寫為 Swift、跑逾兩週、逐像素自我驗證；SEJ「prompt engineering 不重要」發言者具名查實為 Cherny）、cat-wu（同前，該頁改為歸屬澄清）；claude-security ⟨Q-01⟩ 依 Lane A 第四列維持 ❓ 推複查日至 09-16。完整報告 WARN：探針偵測力退化 2 頁（code-quality-decline:36、official-community-gap:77）已登轉知帳（H→功能記者）
  - 📊 產消對帳（概估）：近 7 天新增 18 筆｜每週產能 15 筆（A 10＋B 5）｜本輪實際可消 6 筆｜淨增 3 筆/週；📈 趨勢：08-30 51 筆 → 今日 67 筆（+16）；⏳ Lane B 依現行額度約 13.2 週排空。⚠️ 產出快過消費——處置建議：舊語法盲區 135 筆回填後會再湧入，建議（a）記者端提高標記門檻（僅具體可探針之事實才標）或（b）Lane B 額度暫時提高至 8，請使用者裁示
- 歸因抽查（5d）：抽 5 筆，相符 3／修正漂移 0／無對應 0；另發現歸因日期誤差 2 筆（Maximizing 條目實際在 08-15 日報、歸因記 08-16；Claude Academy 實際 08-24、歸因記 08-26——頁面內容忠實，屬 ingest 端歸因 metadata 誤差，帳本 append-only 不回改，供 ingest 端留意）
- pricing 通路與乘數（5e）：資料截至 08-29（4 天），未逾 30 天複查門檻，本輪免查；無新模型世代
- 讀者模擬：3 題全 ✅ 2 跳命中——①「9/14 週配額 +25% 是真的嗎」→ pricing 計費規則（含 −17% 換算與該做的事）②「Model Hardware Standard 能用了嗎」→ feature-radar ⏳ 觀望 ③「Sony/Warner 訴訟進展」→ anthropic-business 商業風險表
- 質疑代打（7b，首跑）：seed 2026-W36 抽 Q2（缺席偵測）＋Q7（宣稱對帳）
  - Q7 ✅：抽中 pricing「計費切割已暫停、當前維持訂閱配額制」現況句；證據行：`news_mentions --since 4w "Agent SDK" "程式化用量" "usage-based"` 命中 0 天，06-16 暫停後無重啟訊號，宣稱成立
  - Q2 ❌ 待辦：funnel 09-01 無「gathered>0 且 emitted=0」來源，改查落差最大者 GitHub（35 抓 9 刊）——**探針撞上資料缺口：`src/gathered_archive/` 只存刊出後的 71 條，被擋的 54 條不留存，「昨天擋掉了什麼」無從逐條稽核**（25 則靜默消失的結構性條件部分仍在：有 funnel 數字可見性、無條目級可考性）。待使用者裁示：是否讓 gather 落一份全量（或被擋清單）archive
  - 人類質疑時效燈：✅ 0 天前有質疑（2026-09-02），未亮
- lint 自我遵守率：6/6 位記者回報一次過（形狀層八項均有明確結果，無退回）
- 行為層抽驗：N=18 項宣稱，seed 2026-W36 擲骰抽中 #8（商業記者：anthropic-business 5 處維運字眼修復）——git diff 核對如實（移除行含「留給安全政策記者」等字樣、殘留 grep 0 命中），✅ 通過
- 懸置語法 WARN：2 條（探針偵測力退化 ×2），已登轉知帳予功能記者；另本輪 lint 前置修復：新語法標記行內散文重複「待查證」3 處措辭消除，存量棘輪 147→145
- 熱度降溫（5a）：檢查 42 條（含 4 條探針重試），降 17 條：Artifacts 4→3、自架沙箱+MCP 隧道 3→2、/loop・/batch・/background 3→2、Reflect 3→2、Outcomes 3→2、Cowork 行動/網頁 3→2、Dynamic Workflows 3→2、Coordinator 模式 3→2、hard_deny 2→1、小企業 Skills 2→1、ultracode 重命名 2→1、sandbox.credentials 2→1、/rewind 2→1、Dreaming 2→1、v2.1.212 2→1、Agent View 2→1、Sandboxing 2→1；同步詳細條目標頭 1 處（v2.1.212，並修其原有表 2／詳 3 之不一致）；entities 頁熱度表 0 處涉及。判定紀律：AND 語意初判 25+4 條零命中 → 改 --any（OR）重跑後 15 條仍零命中、14 條有命中逐條看原文行 → 剔除 2 條假命中（Dynamic Workflows 命中為 fork subagent 討論、Coordinator 命中為 Simon Willison code review 文）後定案 17 條。⏳ 逾 90 天處置：0 條（Dreaming 已帶註記且零後續，依「已加註者不重複處置」跳過）
- 渲染層驗收：（見 step 10 執行後補記於心跳）
- overview.md：已更新（音樂訴訟升級、週配額 −17%、METR 併案檢討、Lambda/Nscale 基建、Boris 三件事查實、第二輪降溫；近期重大事件表改為 08-27~09-02 窗口）
- 待使用者裁示：
  - ⏳ 已擱置 0 週｜**Q2 資料缺口**：gathered_archive 只存刊出量，被擋條目無處稽核——是否讓 daily-gather 落全量（或 rejected 清單）archive？
  - ⏳ 已擱置 0 週｜**5c 產消失衡**：淨增 3 筆/週＋盲區 135 筆待湧入——記者端提高標記門檻 or Lane B 額度暫升 8？
  - ⏳ 已擱置 0 週｜**ai-agent-safety-archive 狀態統一**（安全政策記者觀察）：純封存頁掛 monitoring，是否比照社群封存頁慣例改 `resolved（封存頁）` 並同步 index？
  - ⏳ 已擱置 0 週｜**patterns 淘汰審查 dry run**（社群記者）：7 類 60 天沉寂候選（跨環境 Agent 記憶、架構邊界合約、可靠性測試、Agent 預算控制、確定性 Agent 框架、Agent 記憶保護、跨 Repo 依賴可視化）確認後執行刪除
  - ⏳ 已擱置 0 週｜**5d 歸因日期誤差**：2 筆歸因 date 與日報實際日期差 1–2 天，是否要求 ingest 端以日報檔名為準寫入？
  - ⏳ 已擱置 1 週｜**6c 表格式 rollup 行**（08-29 首提）：表格式 ingest 紀錄是否要求保留「呈現品質：✅」明文行——本輪依 08-30 裁決「明文 rollup 與表格式等價」已視為合格，此項可望結案

## 2026-09-02 Query：「工具目錄要能從痛點找到最推薦的 skill」→ 決策表改版（第一波）

**點出什麼：** 使用者指出 community-tech-tools 應能「找到痛點與目前最推薦的 skill」。Fable（系統面）＋Opus（讀者面）雙發想＋Opus reviewer 對抗審查後定案三波計畫。健檢實錘：痛點格塞 9 工具名＝沒有推薦；⚡ 條目無汰除條件、130 天永久居留；三層分類學 6/8/10 斷裂；量化數字普遍無日期。reviewer 核心裁決：「設計新增大量對讀者的承諾，而兌現機制全落在本庫歷史上已被證明會空轉的位置」——一個有驗證層但驗證從不執行的頁面，比誠實承認只有星數的頁面更誤導。

**處置（第一波）：** 頁面改組為「我卡在這裡」8 症狀決策表（首選唯一＋讀者處境式分界＋帶日期證據 🟢🟡⚪＋安裝徽章 🧩⌨️🖥️🔌）；原痛點洞察＋精選層併入；出口連頁不連錨；`scripts/check_tools_page.py`（數字必帶日期／首選唯一，改壞驗紅已測）掛進 run_tests；build_web wikilink WARN 加合計尾行（給心跳抄錄的消費端）；3 跳自檢題入 `wiki-ingest-community-lint.md` 每輪重跑；規則檔與 review-registry 錨點同步。順帶修 1 個既有錨點 WARN（claude-code→patterns 學術對照，改連頁）。**第二波（驗證層＋5f＋策展回報欄＋daily 窄口）依 reviewer 判決：防腐件到位前不開驗證層。**

## 2026-09-02 Query：「graph 機制不能幫上忙嗎／為什麼沒想到」→ 題庫加 Q8 資產重用審計

**點出什麼：** 同日兩例同型失誤——回答「建程式庫用哪些 skill」時單入口滿足漏掉 graphify（採用量最大者無症狀入口）；設計問題→skill 連結機制時零資產盤點，使用者一句「wiki_graph 不能幫上忙嗎」讓設計成本當場砍半（盤點與防孤兒整塊改用既有 explain/sections）。此質疑模式（「蓋新東西前盤點過既有資產嗎」）不屬題庫既有七種。

**處置：** 經使用者確認加入 Q8「資產重用審計」（探針：列近 7 天新增資產→逐一答盤點證據寫在哪→對照 wiki_graph／news_mentions／check_* 家族找重疊提減法重構）；測試斷言同步；相關檔「七種」措辭改為可成長表述。連帶產出：問題→skill 連結全站化（graph 盤點＋check_spokes 對帳＋候選症狀聚合門檻，見同日前條）；兩條行為教訓入使用者記憶庫（推薦類查詢紀律、事前化資產盤點案例）。

## 2026-09-02 Query：「開發實務要不要獨立記者」→ 導覽層方案＋修雙重認領

**點出什麼：** 使用者盤點程式開發相關頁（12 頁橫跨功能/社群/模型三記者）並提議獨立記者。評估結論：第七位記者的全系統改動面（分類表、六份規則、registry sync_pair、雲端派工）高於收益，且現行「功能管官方面、社群管社群面」是內容型態切法、有其道理；「coding 是跨記者 beat」的需求改以導覽層兌現。盤點順帶抓到真實 bug：code-quality-decline 領域標 🛠️（動態認領→功能）但社群規則自始明列本頁——本日 lint 兩位記者實際都處理了該頁（雙重認領實證）。

**處置：** ① code-quality-decline 領域改正為 🌐 社群（頁首＋index，認領歸一）；② index 新增「💻 開發實務入口」路由表（8 行，我想……→去哪；只放路由不放事實，維護屬主編 index 彙整既有職責）。獨立記者議題若日後重提，先派 reviewer 估全系統改動面。

## 2026-09-02 Query：「archify 存在嗎／怎麼傳承知識」→ C 窗塞車徹查＋知識傳承三工種分類

**點出什麼：** 使用者問 archify（43,355★ 架構圖 agent skill）本庫有無收錄——三層查證（日報／gathered_archive 原料層／data）全零命中，且從未進漏斗。徹查 C 窗機制定案：**查詢抓得到（實測在 scope 結果內），病灶是佇列塞車**——未報導合格候選 154 個、每日吐 2 個、依星數降冪，archify 排第 20（約 10 天）、OpenMontage 真身 calesthio/OpenMontage（55,576★，先前誤登 shingo257 為 0 星仿品）排第 13；排空約 77 天，產出恐快過消費（同 pending 佇列病），且佇列長度只在 logger.info、無消費端。處置選項 (a)提高配額/(b)一次清倉/(c)佇列納入 6e 產消對帳，已登 workaround-register 待裁決。

**沉澱（使用者按讚的分類）：** 追查中發現佇列前 20 名裡「知識傳承」一格藏三個定義級工具，實為**三個工種**：①給人·探索式理解（Understand-Anything，81,325★，可探索可提問的互動知識圖）②給人·交付級圖表（archify，43,378★，精緻架構/時序/資料流圖，自包含 HTML）③給 agent·程式碼索引（codegraph，69,253★，預索引＋改 code 自動同步＋全本機——與已收錄 graphify 113k★ 直接競品，auto-sync 主張更進一步）。三者皆過防刷指標（forks 比例、活躍 push）但**零社群實測證據**，排序僅星數。**待辦：** 三工具經 pipeline 入庫後，社群記者按此三工種重整「🧩 Skills 速查」的「Codebase 理解／索引」組（拆給人/給 agent），並評估 codegraph vs graphify 對比列；「傳給人」屬候選症狀，湊滿 ≥2 頁需求證據再開決策表列。

## 2026-09-02 Query：「使用者提問也可沉澱進 wiki」→ 原則放寬立法＋首次適用＋D7 佇列量規

**點出什麼：** 使用者裁決 wiki 沉澱來源由「日報唯一」放寬為「日報＋使用者提問」。此通道證據等級不低於日報：入口在主編層、有 web 工具、可即時查證一手來源（記者通道反而無 web 工具）。

**立法：** ① 專案 CLAUDE.md「蒐集範圍」加「使用者提問」列（查證是入場券、必標查證日＋來源連結、slug `user-query`、log Query 為溯源記錄）；② `data/source_registry.json` 註冊 user-query（category=official，理由入口即查證）；③ 記者共用規則 slug 表加列；④ tools 頁策展規則「來源」行改寫（user-query 條目視同達標維護，不因無日報出處汰除）。

**首次適用：** archify／Understand-Anything／codegraph 三工具寫入 tools 頁（Skills 速查「Codebase 理解」組觸發三工種細分：給 agent·索引／給人·探索／給人·交付；工具目錄各一列，採用 ⏳、簡介帶 [使用者提問] 前綴＋查證日）；歸因 3 筆 append。

**同輪機制（使用者指示「想一個機制避免這個問題」）：** C 窗佇列產消對帳——`github_releases.py` 抓取時將佇列量寫 `data/inventory_queue_history.csv`（同日 upsert），lint 6e 新增判讀（連兩週上升或排空 > 30 天 → 告警；檔案過期 → 告警，掃描失敗不得當成 0）。並升格為通用原則 D7「建佇列必附產消對帳」（`~/.claude/system-design-principles.md`）。C 窗塞車處置（提配額 vs 一次清倉）仍待使用者裁決——三個關鍵工具已由 user-query 通道先行入庫，急迫性降低。

## 2026-09-02 Query：「為什麼之前會漏球」→ 漏球三層解剖＋C 窗清倉執行

**點出什麼：** 使用者追問 archify 類漏球的根因。解剖為三層，各有不同機制缺口：
① **出生期（結構性盲區）**：A/B 窗 scope 綁 claude 關鍵字，Agent Skills 生態 repo（archify 2026-04-15 出生）名稱描述不含 claude，新星窗／穿越窗自始看不見。08-28 補的「agent skills」scope 只進 C 窗不進 A/B——刻意取捨（100–3000★ 帶被內容型 skill 洗版，該 scope 上星數即品質過濾器），代價是**此生態的工程級 repo 結構上只能在 20k★+ 才被看見，永遠遲到**，C 窗即其唯一感測器。
② **成長期（平台缺口）**：archify 聲量走 X／YouTube／daily.dev——前者明文不收（設計取捨）、後兩者不在來源清單；HN/Reddit/dev.to 121 篇日報＋14 天原料層零命中，不是漏抓是真沒出現。
③ **補課期（吞吐塞車）**：C 窗上線 5 天積 154 候選、每日 2 則 77 天排空（已於同日徹查條目詳述）。

**清倉執行（使用者裁決 b）：** 154 個候選寫入 `data/inventory_clearance.md`（機器清單、未策展、防刷未逐一驗，檔頭明示）；`_emitted_repo_urls()` 改為將清倉帳本與日報同等計入——**刻意放 data/ 不放 news/**（news 會被 build_web 上網站、被多支掃描腳本消費，塞非日報格式會污染所有消費端）。驗證：archify/OpenMontage/codegraph/claude-mem 皆已入帳，佇列歸零；此後新越過 3000★ 者由 C 窗正常吐出、產消對帳（inventory_queue_history.csv＋6e）看守。workaround-register C 窗條目結案。

## 2026-09-02 Query：「只有 X 熱、還是該類別熱？」→ 漏球第二層結論更正：HN 其實熱過，是關鍵字閘掉的

**點出什麼：** 使用者質疑「聲量只在 X」的說法。直查 HN Algolia 全文（不經本庫關鍵字閘）發現：**Understand-Anything 於 2026-05-01 上過 HN 169 分／49 留言**——在本庫收錄窗（04-25 起）內、遠超高門檻（≥50 分），且為同一 repo（Lum1104→Egonex-AI 為 GitHub 組織轉移，星數/forks/建立日/官網全同）。本庫 HN 來源以「claude」關鍵字查 Algolia，該篇標題「Understand Anything」不含關鍵字，抓取端即掉球——**repo 描述明寫 Works with Claude Code，是 in-scope 內容，球在我們的場上、被自己的閘擋掉**。

**各工具修正後的定位：** archify——HN 全文 0 篇（73 命中全是 2012 年同名新創），「X 圈傳播、HN 真沒有」成立；OpenMontage——HN 有 5 篇但最高 7 分，未達低門檻，非關鍵字問題；codegraph——HN 12 分那篇在 2026-03-09（收錄窗之前）。**結論：三個工具三種漏法**（X 圈／未達門檻／窗前＋關鍵字閘），「平台缺口」只對 archify 成立。

**待裁示（pipeline 改動，未擅動）：** HN 關鍵字閘是既有設計取捨（蒐集邊界），但 169 分的 in-scope 工具漏球顯示閘太窄。候選補強：HN 每日高分榜（如 ≥100 分）條目若帶 GitHub 連結，抓 repo description 判 claude/anthropic 字樣（確定性規則、無需 LLM）——此法可接住 Understand-Anything 型漏球。採納與否待使用者裁決，動工前後須跑 /pipeline-change-check。

## 2026-09-02 GitHub 發現機制改善方案：雙 agent 產出＋Phase 0 探針實測

**產出：** 構思 agent（opus）設計 D/E/F 三新窗＋現有窗收斂；調研 agent（sonnet）盤點市面做法。Phase 0 四探針當日實測結果——
- ✅ **D 窗（HN ≥100 分帶 GitHub 連結補撈）介面成立**：Algolia 空 query＋numericFilters 可用（26h 母體 36 則）；歷史回測命中 Understand-Anything（05-01，169 分）——本窗存在理由已驗證
- ✅ search API 回應含 `language`/`topics` 欄（F 窗與 D 窗第二道過濾的資料面成立）
- ❌ **F 窗 R1–R3 規則校準失敗**：67 repo 語料擋掉 44 個，含 anthropics/skills、addyosmani/agent-skills、vercel-labs/skills 等明顯工程級（R3 工程詞 allow 過嚴）——F 窗退回重設計，不上線
- ❌ **OSS Insight Trends API 已死**（調研首推，文件完美、實測回 `data_quality: unavailable`，事件擷取自 2026-03-01 跌至基線 0.3%）——velocity 只剩自建 E 窗一條路；「文件層查證≠實測層可用」再添一例（D6）
- 🐛 **順手抓到當日新 bug**：daily-gather workflow 指名 commit 清單缺 `inventory_queue_history.csv`，雲端對帳寫入會靜默丟失——已修（同型風險正是設計稿對 E 窗歷史檔的警告）
- 共識否決：github.com/trending 抓取（無 API 契約、壞得像正常）、GH Archive/BigQuery（帳號依賴/資料量）、star-history（無時序 API）

**Phase 1 待使用者裁決後動工**：共用已報導閘（防重吐 154 清倉 repo）、對帳 CSV 泛化五欄制、A/B 硬上限＋B 帶擴至 5000、D 窗上線、E 窗記錄端、6e 逐窗判讀。動工前後跑 /pipeline-change-check。

## 2026-09-03 補查：GitHub 事件流生態 2026 現況（調研 agent 二輪，實測型）

**查明的事：** GitHub 公開事件流退化是**永久性、結構性、且官方從未公告**——agent 實際下載三個時間點的 GH Archive 小時檔解壓計數：WatchEvent 佔比 2026-02 為 2.19% → 06 起 0.09%，PR/Issue 事件同步崩盤，僅 Push/Create/Delete 正常；ClickHouse 官方分析站原文確認「2025 年中衰退、2026 崩塌，是資料源的變化不是使用者行為的變化」。GitHub 官方 changelog／可用性月報零提及；2025-08 payload 精簡公告時間接近但無文件證實因果（標註推論）。整個「吃事件流」的第三方生態（OSS Insight trends、GH Archive velocity 分析）連帶陣亡；**Search API 走 GitHub 自家搜尋索引、不吃事件流，完全未受影響**——本庫 A/B/C 窗地基安然。2026 年倖存/新生做法全部收斂到同一架構：**星數快照輪詢＋自算差值**（daily-stars-explorer 等），與本方案 E 窗同構——E 窗從「自己想的設計」獲得市面獨立收斂驗證。GH Archive 路線從候選除名（不是複雜度問題，是「做出來也在算噪聲」）；trendshift 計量單位改「mentions」來歷可疑待查。最終方案維持前日版本不變，信心上修。

## 2026-09-03 GitHub 發現機制 Phase 1 上線（使用者裁決「好」後動工）

**改動（commit 見本日）：** ① D 窗新來源 `hn_repo_bridge.py`——HN 26h 內 ≥100 分故事，GitHub 連結者對 repo description+topics+homepage 做確定性關鍵字閘，每日上限 3；母體為 0 時拋例外（存在性斷言：HN 每天必有高分故事，0=介面壞了，不回空 list 假裝正常）。② 共用已報導閘：日報＋清倉帳本升為 A/B/C 全窗去重（改版前 A/B 只有 14 天 TTL cache，會重吐清倉 repo）。③ 上限收斂：A/B 各 3、B 帶 500..5000（與 C 刻意重疊防接縫）、來源總量 40→16。④ E 窗記錄端：各窗看到的 repo 星數逐日記 `data/repo_star_history.csv`（保留 60 天、同日 upsert、零額外 API）；吐出端待 ≥2 週資料校準閾值（Phase 2）。⑤ 對帳泛化 `data/discovery_queue_history.csv` 五欄制（date,window,queued,emitted,note），lint 6e 改逐窗判讀＋「連 3 天缺列＝窗死」＋星史檔增長看守。⑥ workflow 指名 commit 補兩個新 csv——並抓到前日埋的字面 `\n` bug（git add 行被寫成單行，雲端會失敗）一併修正。

**首跑實測：** D 窗母體 38 則、吐 1 則（Fable 5.1 發布，HN 1352 分官方網域直收）；GitHub 來源四窗對帳全寫入、星史 197 repo 入檔、inventory 清倉後歸 0、總量 10≤16。迴歸測試 7 案例鎖 Understand-Anything 過閘錨點與對帳語意。pipeline-change-check baseline 已拍（digest 2026-09-01，HEAD 46eef944）；**compare 待下次完整 pipeline 跑完執行**（預期：GitHub gathered 下降、emitted 持平或微升、新增 HN Repo Bridge 來源列）。

## 2026-09-03 興趣類別 skill 榜上線（使用者裁決 12 類，「coding 實務開發也很重要」）

**是什麼：** 熱度管線答「大家在看什麼」（推播），使用者要的是「我這幾類現在誰最熱、本週誰竄升」（拉取）——治理型需求在生態裡是少數派、上不了熱度榜，只能定向搜。新頁 `wiki/topics/skill-interest-watch.md` 由 `scripts/skill_interest_snapshot.py` 每日（daily-gather workflow，continue-on-error）整頁覆寫；設定 `data/skill_interest_watch.json`；A 組 8 類按 guide 九段流程（連頁＋「第 N 段」提示，**連頁不連錨**——段標題帶 [社群面待補] 這類會變的標記，首版錨定即建置 8 個 WARN，當場改掉）、B 組 4 類治理。E 窗星史檔第一個消費者（「本週竄升」＝七日星數差，冷啟動明寫）；每類寫 discovery 對帳（window=interest:<slug>），lint 6e 逐窗看守。index 目錄列＋💻 入口列、devpractice 週彙整讀本頁竄升欄、社群 lint 規則明訂機器頁不手改。

**query 校準（兩輪 38 條實測）的發現：** GitHub Search 多組 (A OR B) 括號在 in:description 下幾乎等於「任一詞命中」，含 agent/skill/claude 等通用詞即被同一批巨頭（ECC、karpathy-skills、claude-code 本體、system-prompts、gstack）洗版——6 類的首版 query 全部回傳同一前 5，等於沒問。有效的只有「單一類別專屬名詞片語」。**8 類上線、4 類（實作攔錯／測試驗證／除錯／git 衛生）兩輪皆無辨識力 → 誠實標 needs_calibration、頁面印 ⚠️ 不硬塞**；已登 workaround-register 複查（試 topic: 限定、SKILL.md 存在性探測、或改由 patterns 頁社群節點餵）。首跑：222 repo 入榜、星史 410 列。

## 2026-09-03 Query：「興趣表跟 tools 表有點重疊」→ fable 重設計，方案 D 第一波

**點出什麼：** 使用者要重想兩頁目的（含移除選項）。派 fable 從零設計，結論：兩頁答不同問題——tools「我卡住了該裝哪個」（決策，需證據與分界）、榜「我這幾類這週有什麼沒看到」（感知，需每天掃不漏）——值得各留一頁；但重疊真實存在且**位置具體**：① tools「不綁症狀的精選」是手抄的榜（4 列全 ⚪、無更新機制）；② 榜的 4 個未校準類——**病因不是 query 沒調好，是感測器裝錯層**：GitHub 描述是作者講功能的語言，治理型需求是讀者講痛點的語言，在 HN／dev.to 全文；反證是決策表早有其中 3 類的人工首選（Groundtruth、hooks 機制、Merge Queue），來源全是 Show HN／dev.to、無一來自 GitHub 搜尋。四方案評估：A 砍榜（倒退）、B 砍 tools 判斷層（違反「只看星星找不到需求」）、C 合併（機器與人共寫一檔，違反機器頁約束）、**D 兩頁重劃邊界（採納）**。

**第一波執行：** tools 刪「不綁症狀的精選」、callout 覆寫、速查每組 ≤5 列閘；榜 4 類 `status=retired`（不再掛 ⚠️ 空榜，改印「無法用 GitHub 辨識的需求」指路表）；單向橋：設定檔每類 `tools_symptom`（決策表症狀句原文）→ render「本庫判斷 →」行，`check_tools_page.check_spokes` 對帳（改壞驗紅，測試含反向案例）；🧭 標記＝repo 已在 tools 頁（機器唯讀人工頁，零 API）；對帳 note 加 `retired` 值域（lint 6e 不判窗死）；index／社群 lint 規則同步；register 4 類未校準結案、新開「症狀語言感測器」待裁決。**第二波未動**：速查四組對齊 guide 段號、症狀語言感測器（需 probe＋change-check）。

## 2026-09-02 Ingest | news/2026-09-02.md（97 則抓取，38 則進日報）

- 來源日報：[[news/2026-09-02]]（13/13 來源正常，97 則；日報收錄 38 則，另 59 則透過 `list_digest_omissions.py` 一併提供給記者判斷）
- 分類派工：模型 10 則、功能 12 則、商業 10 則、安全政策 12 則、社群 21 則、人物 1 則（六類並行 foreground，`subagent_type: general-purpose` + `model: sonnet`，正典派工路徑）
- 更新頁面：
  - **模型**：`entities/fable-5.md`、`entities/mythos.md`（Claude Fable 5.1、Claude Mythos 5.1 發布——同一模型不同防護層級，Fable 5.1 GA、Mythos 5.1 限信任機構；反萃取機制；08-29／08-10 兩筆待查證標記補訊 2026-09-02）；`topics/model-comparison.md`（新增陣容列，3 跳自檢通過）；`entities/sonnet-5.md`（過時措辭修正）
  - **功能**：`entities/claude-code.md`（v2.1.258 macOS 12 啟動修復；SDK TS/Python 新增 user profiles beta；4 則已知問題新增：Windows Desktop 孤兒程序鎖檔 #42776、Remote Control 重連失效 #34255、Advisor 無回應 #69238、MCP draft-07 outputSchema #86142；Fable5 usage credits 誤判 #79337 更新；Auto Mode 提示注入劫持與惡意 .git config RCE 兩則安全性已知問題連結 ai-agent-safety）；`topics/long-context-1m.md`（同步 #79337 [1m] 覆蓋事件）
  - **商業**：`entities/pricing.md`（Enterprise Frontier Safeguards／EFS 發布，快取讀取費率降至 0.025x，週用量促銷延至 09-13，INR 定價請求；EFS 相關兩筆既有待查證標記補訊）；`topics/anthropic-business.md`（EFS、Nvidia $35B pact 考證為與既有 Lambda 合約同一交易、AWS Fable5.1 上線、IPO 分析）；`topics/enterprise-tool-tracker.md`（Samsung 晶片設計案例第四次媒體重申）
  - **安全政策**：`topics/ai-agent-safety.md`（Guardian「並未完全對齊」新增細節、Auto Mode 提示注入劫持無修復計畫、teiss 提示注入自我傳播論述、惡意 .git config RCE、AISLE curl CVE 聲稱存疑記錄；「Anthropic banned me」經評估不符任一頁觸發條件，未落地）；`topics/anthropic-government-policy.md`（中國官媒雙重標準指控、SCMP 美中模型競賽分析，與既有 08-31 Bloomberg 主題並陳未逕自合併）
  - **社群**：`topics/community-tech-patterns.md`（10 則：claude-mem／agent-skills 存量盤點、internet-court-skill／cumora／trinity／skilldock、4 則 dev.to 第一手實作；DevnorsAI/devnors-data-mcp 因品質存疑排除）；`topics/community-tech-discussions.md`（3 則：Anthropic 帳號停權經驗、AISLE 資安行銷質疑、Bengaluru 文化遺產遺失究責討論）
  - **人物**：`entities/tom-blomfield.md`（Business Insider 談新同事文化，既有 ❓ 待查證標記補訊 2026-09-02）
- 新增頁面：無
- feature-radar：新增 2 條（Claude Fable 5.1 🔥🔥🔥🔥🔥／使用者個人資料 API Beta 🔥🔥）；本週推薦換上 Fable 5.1，汰換跨 session 訊息互通（🔥🔥🔥🔥，逾 7 天未變動）；升版風險最新版本更新為 v2.1.258；⏰ 倒數中 09-14 換軌事件補充官方促銷頁已同步更新到期日 09-13，互相印證
- 轉知帳本：本輪新開 7 筆（H-3f85a1／H-afe923／H-969fc1／H-398ffe／H-5dee92／H-a2cc40／H-f5c58d），其中 H-969fc1 模型記者已於同日獨立處理並即時結案；其餘 6 筆留待次日對應記者接手
- 摘要：Claude Fable 5.1／Mythos 5.1 發布為今日最大事件（HN 1338 分、十餘家媒體跟進），同日並有 Anthropic 對 7/30、8/4 兩起未授權存取事件的深入檢討部落格（坦承「並未完全對齊」、將與 METR 合作審查）、Enterprise Frontier Safeguards 企業級零留存安全監控上線，以及 Claude Code Auto Mode 遭提示注入劫持且官方無修復計畫的資安警示
- 呈現品質：全部通過；`community-tech-discussions.md` 表格既有債務（多列 core論點欄 >120 字元）記錄待辦，非本輪新增
- devpractice 沉澱：基準線 964d72a → 8c04ac5，候選 14 筆（claude-code 已知問題與版本更新 3、ai-agent-safety 提示注入相關 2、community-tech-patterns 工具與實作心得 5、community-tech-tools 3、fable-5／pricing 快取降價與配額更正 2）；首次執行，帳本原為空檔，無需查重
- 品質備註：無

## 2026-09-03 Query：「昨天的日報怎麼沒有生成」→ 兩班故事＋兩個自己埋的雷

**查明：** 日報**有生成**（22:00 UTC 班於 22:43 推上 master），本機未拉才看不到；網站停在 09-01 是真的。三班全紀錄：① 12:05 正確中止（GH Actions 抓料延遲 4 小時，14:34 才到）；② 17:03 班完整跑完日報＋六記者＋devpractice 首跑＋web，**push 撞上本機同時間的 commit（wiki/log.md append-append 衝突）**，依規則不自解、備份到分支 `cloud-pending-2026-09-02-1703` 後結束——但沒寫 abort 心跳，從 git 看像靜默死亡；③ 22:03 班因冪等閘看不到日報而重做一輪，news＋wiki 推上，**web build 被 `check_wiki_freshness.py` 擋下：`skill-interest-watch` 標頭宣稱有新聞更新卻零歸因、且未登記 DERIVED_PAGES**——建頁者（本機 09-02）漏登記，D6「機制首跑前審計」沒做到位。

**處置：** DERIVED_PAGES 補登記；**防再犯**：check_wiki_freshness 新增「[未登記衍生頁]」檢查——標頭有「更新頻率」欄即視為不走每日 ingest、必須登記，建頁當天就紅，不等當晚 gate；本機重建 web 推上；weekly/open-signals.jsonl 的 stash 衝突以聯集解（jsonl append-append）。**待裁決：** (a) 17:03 班備份分支已被 22:03 班完整取代，建議刪除（內容為同日重複、日報版本不同）；(b) wiki/log.md 是 append-only，append-append 衝突可機械聯集——建議 Step 5 的自解白名單從 emitted_items.json 擴到 log.md（union 策略），否則本機與雲端班次重疊時每次都得整班重跑。

## 2026-09-03 裁決執行：刪 17:03 班備份分支＋Step 5 自解白名單擴至 append-only 檔

使用者「好」：① 遠端分支 `cloud-pending-2026-09-02-1703` 已刪（12 commit 全由 22:03 班重做取代）；② 新增 `scripts/resolve_append_only.py`——rebase 衝突檔全在 `APPEND_ONLY` 白名單（log.md、source_attribution／devpractice-candidates／pending-signals／open-signals jsonl、task_scheduler.log）時以 `git merge-file --union` 三方合併保留兩側新增，白名單外任一衝突即 exit 1 不動檔交回人工；測試在臨時 git repo 實測 rebase 衝突→union→continue 全流程。`.claude/commands/news-pipeline-steps.md` Step 5 自解規則由「唯一 emitted_items.json」改為兩類。本次不動日報格式與收錄門檻，不需 pipeline-change-check；Phase 1 的 compare 仍待下次完整 pipeline（今日 12:00 UTC 班）跑完執行。

## 2026-09-03 Query：「派冷讀者 review 開發實務入口能否定位資訊」→ 三輪自主迴圈 1/6 → 6/6

**方法：** 三位冷讀者（接手大 repo／跑多 agent／技術主管）六題，只准讀讀者看得到的頁，從 index 💻 入口出發計跳數；3 跳內須拿到「單一答案含連結＋為什麼＋怎麼裝」或「誠實不推薦＋改看 Y 且 Y 可執行」。使用者指示自審自改再派、直到沒問題。

**第一輪 1/6**——架構對、末端交付壞：首選 Harness／Groundtruth 全站無連結（次選反而有）；決策表無「agent 讀不懂大 repo」症狀，guide 2a 與速查各答一套互不轉介；榜 code review 類 query 撈到 gitea；「本庫判斷 →」在無 🧭 的類別照印指向空處；「本週竄升」冷啟動但入口照賣；榜頁開始日期>最後更新、半字截斷、參考來源列 data/scripts 路徑；「感測層／判斷層」內部話。**修**：連結補齊（frenchie4111/harness、vnmoorthy/groundtruth）；決策表開列「接手沒碰過的大 repo，agent 讀不懂」（首選 graphify，候選症狀 9 正式開列）；guide 2a 加社群側轉介、推薦細節加「官方設定先做、索引再裝」與 Harness 同名提醒；入口表改讀者語言＋「先分清兩頁」導言＋guide 第 9 段列；榜 code-review 退役指路 guide 第 5 段；橋無 🧭 改印「本庫尚無判斷」；截斷加省略號；日期、參考來源改讀者語言。

**第二輪 6/6、9 刺**：維運字眼（index「三位記者」「每日 ingest」「lint 回升」×4、patterns「本記者」21 處）、index 對榜的類別數漂移、入口缺 code review 列、缺口態語法外洩、榜 multi-agent 橋只接一個症狀、large-codebase 線 3 🧰 接記憶列不接索引列、資料源類別在 coding 榜像雜訊。**修**：全數處理（tools_symptom 支援多症狀、check_spokes 同步；數字改敘述；缺口態保留機器記號改前半句為讀者語言）。

**第三輪 6/6、無阻擋級**：兩頁分工冷讀者能用自己的話說出且指得出在哪句弄懂（index:23＋榜 callout）。殘餘小刺：feature-radar:253 內部對話、guide 亮點「三組」漂移、spec-kit 星數無日期（本輪已擦）；patterns 互動門檻字眼 9 處、claude-code 歷史區維運字眼、tools 目錄 [存量盤點]/[使用者提問] 前綴——開三筆轉知帳交社群／功能記者下次 lint 處理。**結論**：入口現在能讓冷讀者定位並拿到可執行答案；壞的從來不是架構，是末端交付（連結、對應列、橋的誠實度）。

## 2026-09-03 裁決：開發實務 tab 只留強相關五頁，判斷每日抄錄進總覽頁

使用者裁決（「該 tab 只留開發實務強相關，其他資訊放別頁但經蒸餾到該 tab」）：💻 入口移出 Claude Code 產品頁、功能雷達、效能退步事件（產品動態／事件追蹤，住 🛠️ chip）；社群工具目錄也退出 tab——但不是丟掉判斷，而是**總覽頁每日機械抄錄** tools 的「我卡在這裡」整張決策表＋各類別對應列（`decision_table_from_tools`），判斷仍只在 tools 頁寫（單一寫者，抄本最多落後一天）。我原先兩輪堅持「兩頁都留」是守「事實的家」——但那條規則管的是誰寫，不是讀者在哪讀；使用者一句「你想一下」點破。榜頁改名「興趣類別 skill 總覽」（slug 不變），retired 類別直接印判斷列、不再另開指路節；tab 最終五頁：實戰手冊、總覽、模式庫、大型 codebase 主線、模型選型。冷讀者六題以總覽頁重驗（第四輪）。

## 2026-09-03 冷讀者第四輪（單頁總覽）：6/6、無阻擋級——八刺修七、一項待裁決

改版後六題最大跳數 2（四題 1 跳）。讀者判「判斷與規模同頁是淨改善」「抄錄日＋落後上限那句最讓人放心」。修：決策表分界工具加連結（archify 不在 codebase 榜前五——它是圖表工具、query 為 knowledge graph，屬不同工種，靠分界句連結補）；orchestration 判斷列下加 Harness 同名提醒（設定檔 `caveat`）；重印列標「同頁首決策表對應列」；圖例加「榜偶有跨類誤收」；tools 推薦細節去「3 跳自檢與冷讀者驗收」流程名；patterns「功能記者／縫合」28 處改讀者語言；index 導言加升版風險出口（連 feature-radar，不入表列、不把產品頁拉回 tab）。**待裁決**：「資料源韌性與監測」類別讀者兩輪判在開發實務頁像雜訊、自承非 coding 工具——已設 `status=hidden`（設定保留、頁面不印、不查配額），要回來改 active 即可。

## 2026-09-03 裁決：「資料源韌性」找到合適的家——本站抓料工具規模榜（🛠️ 領域獨立機器頁）

使用者裁決「找個合適的頁面放」而非隱藏。它服務的是「本站怎麼抓料」，不是讀者的開發實務，故新頁 `wiki/topics/site-source-tooling.md`（🛠️ 工具/功能，每日快照，只有規模榜不做判斷），由同一支 `skill_interest_snapshot.py` 的 C 組輸出（`render_site`）；DERIVED_PAGES、index 目錄列、workflow commit 路徑同步；測試鎖住「C 組不得帶 guide_section／tools_symptom、不進總覽頁」。開發實務 tab 名單不變（五頁）。

## 2026-09-03 子故事階層設計定案＋機械前置件上線（reviewer 審查後修訂版）

**設計（使用者裁決）：** 維持一頁一故事；厚度 >600 行只是鬧鐘；切線只落在故事邊界——**子故事三題**（有自己的問題／有自己的結論與時序／被獨立引用）為唯一判準；parent＝part-of 不是衍生；單一 parent、規則遞迴、**無深度上限**；子頁不入 index、不在網站平鋪、只從母頁下鑽；母頁必須仍是故事。fable reviewer 對抗審查判「現在不該動工」並列前置條件——全部採納：(a) 母頁自身「最後新聞更新」不因子頁動、改驗 callout 日期 ≥ 子樹最新（原設計與 freshness 第 2 類互斥、會擋站）；(b) index 改機器投影「↳ 子故事：」而非豁免（查詢 2 跳、13 處認領字面不改）；(c) 不重用 `kind` 欄（Bases 在用）改 `page_role`；(d) 子頁扁平＋領域繼承機械驗；(e) 併回留 redirect 殼；(f) 母頁結論層＝週更整線重寫（照 large-codebase 契約），每日唯讀除 callout／目錄／訊；(g) 💻 tab 不遞迴含子頁；(h) 試點改 ai-agent-safety、patterns 先跑既有蒸餾（1,087 行舊月份從未蒸餾）。

**機械件：** 新 `scripts/check_hierarchy.py`（掛 run_tests：扁平／上層有效／成環／領域繼承／archive 掛父／hub 不落後／index 投影，改壞驗紅測試 9 案例）；`gen_wiki_frontmatter.py` 產 parent／children／page_role／days_since_news_subtree、家族邊不計入鏈、index 投影；`check_wiki_freshness.py` 母頁第 2 類看子樹歸因；`test_index_sync` 子頁由投影涵蓋；`build_web`＋`app.js` 麵包屑、子頁卡、列表只顯根頁、「含 N 子故事」徽章；`wiki_graph` 階層邊分型不入 cluster。首例：`ai-agent-safety-archive` 掛上層 ai-agent-safety、退出 index 列、由投影涵蓋。**verify 流程**寫進拆分原則（六階段：前置蒸餾→盤點 dry run→同一 commit 手術＋run_tests＋錨點不增→devpractice mark→push→冷讀者 2 題→一週回訪）。

## 2026-09-03 Lint（本機執行，試跑：09-02 lint 後 1 天；期間六記者中安全政策記者因 API 529＋session 配額中斷兩次，以 SendMessage 續用原 agent 完成）

- 修正矛盾：人物 2（karpathy 現況「或已停止」vs 歷史「暫停非解散」統一；boris 補 cat-wu 承諾的 SEJ 報導）；主編 3（overview 兩處「+50% 促銷 08-31 終止」與 pricing 09-02 更正衝突→改「延長至 09-13」；model-comparison 一處「Sonnet 5 早鳥至 8/31 其後 $3/$15」過期→改永久化）
- 補連結：功能 1（site-source-tooling 孤島→skill-interest-watch 參考來源互指）
- 狀態更新：無
- resolved 收尾：無
- 新增 entities：無（步驟 4 掃描：Simon Willison 14 頁、Cursor 16 頁、graphify 8 頁、Terminal-Bench 6 頁提及而無專頁——皆為引用來源／競品／工具名，未達「具體事物有足夠描述」門檻；列入待裁示）
- 呈現品質：模型 1 頁 ⚠️（fable-5 #79337 互動數與過期措辭）；商業 1 頁 ⚠️（pricing 09-02 條目維運術語）；人物 3 頁 ⚠️（jensen-huang／amir-salek 維運字眼、boris 舊式表格標記改 ⟨Q-02⟩⟨Q-03⟩）；功能 1 頁 ⚠️（claude-code 33 處「今日彙整」等維運術語，對應 H-29a5db）；社群 3 頁 ⚠️（patterns 11 處、tools 8 處通道前綴＋internet-court 重複列合併＋補 5 工具、code-quality-decline 補第二探針）；安全政策 3 頁 ⚠️（safety-china 6 處舊式散文＋⟨Q-nn⟩ 對帳修復、ai-agent-safety 4 處＋2 格 >150 字下沉、gov-policy 4 處＋標題日期同步＋2 格下沉）；其餘 ✅
- 入口層健檢：>500 行頁（patterns 1791、discussions 1315、ai-agent-safety 1249、anthropic-business 903、claude-code ~800、pricing 732、gov-policy 703）均具入口層；無語意分岔／死案候選
- 待查證回訪：舊語法改寫 14 筆（人物 2、安全政策 12）；加訊 0；各記者逐筆比對日報無新後續
- 轉知帳本：結案 5（H-3f85a1 模型／H-5dee92、H-a2cc40、H-29a5db 功能／H-398ffe 安全政策）；void 2（H-afe923 不達門檻、H-f5c58d 誤派）；新開 1（H-d48bee →社群，接手 f5c58d 議題狀態調整）
- 規則檔健檢：
  - 矛盾（6a）：1 條待裁示——`.claude/commands/wiki-lint.md` 6c 表「新工具加入時更新痛點洞察近期工具欄」引用的「痛點洞察」區塊已於 09-02 改版為「我卡在這裡」決策表且脫離每日 ingest，該列判準已無對應物
  - 引用驗證（6b）：7 項錨點全在（首次出現 282／我卡在這裡／先裝這個／技術彙整／熱門討論 10／衍生 3／全覽表）
  - 遵守率（6c）：近 3 次 ingest（08-31、09-01、09-02）品質標記 3/3（09-02 為明文 rollup 行，依 08-30 裁決等價）、feature-radar 3/3、格式欄位 3/3
  - 過期規則（6d）：135 條 `[加入:]` 中 29 條逾 60 天，均為 5–6 月基礎條款，行為與現狀吻合者不動；未發現描述已失效者
  - 來源健康（6e）：7 天無 ok=false、無社群來源連續 3 天 0；發現窗對帳 09-02 四窗（hn_bridge／rising／crossing／inventory）皆有列、09-03 尚無（gather 班次未到，非缺席）；星史 597 列／2 天；記分卡 HHI 0.223、HN Repo Bridge 樣本 0 天（新窗，只讀趨勢）
  - 跨檔案語意矛盾（6f）：✅ 65 組 sync_pairs 機械全綠；語意抽查派工路徑對（六記者名稱兩側一致）
  - 成長迴路（月度）：非本月首次 lint（09-02 已跑），跳過
- 品質指標（6g）：ref 覆蓋率 100%（25/25）；死鏈報告 08-30（4 天，新鮮）dead 6／anti_bot 79——6 筆先前已全數標「原文已失效」，本輪新增 0；採用驗證率：非本月首次，跳過
- 跨家榜單週更（5b）：haiku 抓取 18 榜取得 16 榜，整表覆寫（WebDev Arena 恢復取得 Opus 5 登頂；圖像編輯／TTS 第二三名換人；MTEB 首位 QZhou-Embedding 僅首位可確認）；Search Arena 連續 2 週無法取得、Aider 停更 5 週→待裁示；SWE-bench／OpenRouter 二手來源歧異並陳於註記。註：前一次 haiku 回報隨 context 壓縮遺失，本輪重派一次（成本 haiku 級）
- 逾期待查證清算（5c）：盤點 68 筆（A3／B65），本輪處理 9 筆——查實 7（pricing 337／344 EFS 官方公告；dario:127 STAT News 專訪內容；boris ⟨Q-02⟩ Bloomberg 受訪者、⟨Q-03⟩ Fortune Brainstorm Tech 出處、boris:222＋cat-wu:92 inc.com 發言人＝Cherny）／Lane A 第四列推複查日 2（mythos:180、tom-blomfield:35 →複 09-17）／查無官方 0／失效移除 0；結案回掃上修 6 處（index boris 摘要、boris 歷史、dario 參考來源、anthropic-business 509、pricing 336、ai-agent-safety 253）
  - 完整報告 WARN：claude-code:223「✅ 已修復內嵌 🔎 子問題」經功能記者確認為合理結構非殘留；official-community-gap:84 探針偵測力退化（僅 A2A 協定有效）→ 留待功能記者下輪補探針
  - 📊 產消對帳（概估）：近 7 天新增 17 筆｜每週產能 15 筆（A 10＋B 5）｜本輪實際可消 9 筆｜淨增 2 筆/週 ⚠️；📈 趨勢：67→68；⏳ Lane B 排空約 13 週；舊語法盲區 143 筆（ai-agent-safety 23、claude-code 19、anthropic-business 11）
- 歸因抽查（5d）：抽 5 筆（Cognizant／#13354／session 劫持／How well／v2.1.214），相符 5／修正漂移 0／無對應 0（連續第 1 週 B=0）
- pricing 通路與乘數（5e）：Fable 5.1 本週發布→WebFetch 官方定價頁：基礎定價 $10/$50 與 Fable 5 同（商業記者原記「尚未公布」已更正並補表列）；快取命中特例 ×0.025 寫入乘數表；長脈絡仍不加價；tokenizer 仍為 4.7 世代新版、官方未載再換代→不轉知模型記者；資料截至更新為 09-03
- devpractice 週彙整（5f）：本週亮點 9 條（Fable 5.1 快取降價、Auto Mode 注入風險量測、.git 設定攻擊面、促銷時程更正、codegraph／Understand-Anything／archify、claude-mem、殭屍 subagent 偵測、MCP draft-07）；深查第 4 段（實際動手寫）已補庫內證據、標記升為 [已補：庫內證據]；跨頁對帳三處 ✅ 一致
- 讀者模擬：3 題 ✅——①「Fable 5.1 快取到底多便宜」→ index pricing 列→模型 API 定價現況表（2 跳）②「EFS 是什麼、資料存哪」→ index anthropic-business→callout（2 跳；index 摘要格未提 EFS，屬慢變路由設計）③「接手大 repo agent 讀不懂該裝什麼」→ index 💻 入口→tools 決策表→graphify（3 跳）
- 質疑代打（7b）：seed 2026-W36 抽 Q4（缺席偵測）＋Q2（漏斗對帳）
  - Q4 ✅：擲骰事實「Anthropic tightens security on its training environment after Claude agents went rogue 3 times」→ index→ai-agent-safety→事件記錄（07-30 三起評估事件／09-01 官方併案檢討，callout 與前一態勢均在），3 跳內命中
  - Q2 ✅：funnel 無 gathered>0 且 emitted=0 來源；落差最大 GitHub（archive 10 條：刊 5／未刊 5：internet-court-skill 5,317★、cumora 3,416★、trinity 503、skilldock 503、devnors-data-mcp 242）——未刊 5 條已由 omissions 清單餵 wiki，社群記者 09-02／09-03 已收錄 internet-court、skilldock、cumora、trinity 於 tools 目錄，判「擋得對」（日報呈現層取捨，沉澱層未漏）
  - 人類質疑時效燈：✅ 1 天前有質疑（2026-09-02），未亮
- lint 自我遵守率：6/6 位記者回報一次過（形狀層八項均有明確結果，無退回）
- 行為層抽驗：N=18 項宣稱，seed 2026-W36 擲骰抽中 #8（功能記者：claude-code 33 處維運術語清空）——git diff 核對如實（移除行含「今日彙整」33 行、新增行 0、現檔殘留 0）
- 熱度降溫（5a）：與 09-02 lint 同一 4 週窗，上輪已降 17 條；本輪 OR 複查零命中者（Reflect、Artifacts、Dynamic Workflows、Coordinator、自架沙箱、Outcomes、/goal）皆屬上輪已降，不重複降；⏳ 逾期處置上輪已做，無新增
- feature-radar：第 17 行「本週推薦」選錄規則說明改寫為讀者語言（功能記者建議、主編執行）
- overview.md：已更新（Fable 5.1 官方定價、EFS 查證結案、促銷延長至 09-13 更正、Boris 三筆查實）
- 渲染層驗收：（見 step 10 執行後補記於心跳）
- 待使用者裁示：
  - ⏳ 已擱置 0 週｜**月度蒸餾提案**（社群記者 dry run）：patterns 2026-06（49 條／30k 字）與 2026-05（37 條／15k 字）達門檻；discussions 2026-05 含 🌊延燒首見日期不提案。執行即等於子故事流程「0 前置」的第一步
  - ⏳ 已擱置 0 週｜**patterns 淘汰候選**：Fast Context Task Router（07-05，Microsoft 專案已下架、⏳ 60 天）——移除或降註記？（本輪僅重點掃描，未逐條複查全表）
  - ⏳ 已擱置 0 週｜**榜單汰換**：Search Arena 連續 2 週無法取得、Aider Polyglot 停更 5 週——是否汰換／由 SWE-bench Pro 或 Terminal-Bench 3.0 承接
  - ⏳ 已擱置 0 週｜**6a 規則矛盾**：wiki-lint.md 6c「痛點洞察近期工具欄」判準已無對應物，建議改為「新工具加入時 tools 目錄同步（lint 週更）」或刪列
  - ⏳ 已擱置 0 週｜**步驟 4 建頁候選**：Simon Willison（14 頁提及，人物）、graphify（8 頁，決策表首選）是否建 entities 頁
  - ⏳ 已擱置 1 週｜Q2 資料缺口（gathered_archive 只存刊出量）；5c 產消失衡（本輪淨增 2/週）；ai-agent-safety-archive 狀態統一；5d 歸因日期誤差；6c 表格式 rollup 行（09-02 起）

## 2026-09-03 月度蒸餾首跑：community-tech-patterns 2026-05／2026-06 → archive（使用者裁決「方案 2：蒸餾與盤點同時做」）

**蒸餾（社群記者執行）：** 新建 `topics/community-tech-patterns-archive`（755 行，`**上層：** [[topics/community-tech-patterns]]`、`resolved（封存頁）`，不入 index 目錄表），2026-06 原 489 行、2026-05 原 227 行 `####` 條目一字不刪搬入，含 3 筆懸置標記隨段落搬遷（主頁 pending 9→6、archive 3）。主頁兩月份改寫為 ≤15 行月度總結，末行連回 archive 錨點；主頁 1790 → 1098 行。引用回掃：全庫僅 1 處 `#技術彙整` 錨點指向主頁、目標仍在，0 處需改；large-codebase「代表實作」欄皆為整頁 wikilink，未斷。驗證：gen_wiki_frontmatter 自動投影 `↳ 子故事：` 進 index 主頁列、`page_role: hub`；run_tests 497 全綠（主編獨立重跑一致）；build_web 斷鏈 WARN 14／錨點 WARN 0，與蒸餾前基線（stash 比對）一致、0 新增。主頁只動「最後更新」。

**子故事盤點 dry run（另一社群記者，唯讀）：** 三候選皆不升格——學術對照節缺 Q3（全庫零錨點指向）且無自有時序；技術彙整主題群 Q1 已由「模式概覽」表回答、Q3 零錨點；大型 codebase 四線三題全過但**已是獨立頁**，以引用（非 part-of）銜接正確。母頁契約：蒸餾後母頁仍為完整故事（概覽層＋參考層＋07/08/09 證據層＋結論）。結論與規則「先蒸餾再談拆分」預期一致：等 2026-07 滿 3 個月再蒸一輪，預期掉到 600 行鬧鐘以下。

**首例意義：** 這是階層機制（2026-09-03 立法）第一次用在活頁（`ai-agent-safety-archive` 為既有頁掛父），全流程六階段中 0（蒸餾）、2（手術＋機械驗證）、3（帳本同步）本輪完成；4（上站）隨本次 push；5（冷讀者驗收）與 6（一週回訪）留待下輪 lint。

## 2026-09-03 Query：「本站抓料工具規模榜這種營運資料沒必要放吧」＋「程式開發手冊為什麼放到工具/功能」→ 下架 site-source-tooling、網站改讀者分類

**點出什麼：** ① `topics/site-source-tooling`（資料源韌性類 GitHub 規模榜）是本站評估抓料工具的營運參考，不是讀者內容，卻掛在 🛠️ 領域讓讀者以為是給他們的工具榜——09-03 上午為了把該類挪出開發實務 tab「找個合適的頁面放」，位置判斷偏了。② 使用者問實戰手冊為何在 🛠️：因為「領域」欄實際是**記者認領欄**（六領域＝六記者），實戰手冊吃官方 skills 清冊、屬功能記者維護；「💻 開發實務」只是 index 路由表＋網站 tab，不是領域。使用者裁決：**HTML 不需要知道記者是誰，以讀者角度分類。**

**處置：** ① 下架：`data/skill_interest_watch.json` C 組移至 `_rejected`（保留校準紀錄與下架理由）、刪頁、index 列、`check_wiki_freshness.DERIVED_PAGES`、`daily-gather.yml` commit 路徑、`skill_interest_snapshot.render_site` 與測試一併移除；新測試 `test_no_site_ops_group` 擋回流。② 網站分類：`build_web.py` 為每頁算 `readerDomain`——index「💻 開發實務入口」表的頁一律歸 💻 開發實務（獨佔），其餘沿用領域值；`app.js` 篩選改看 readerDomain，💻 chip 從「跨領域集合」升為正式分類、移到分隔線前；wiki 標頭「領域」欄與六份規則檔的認領邏輯**零改動**（維護面照舊）。

**未做、留待裁決：** 詳頁標頭目前不顯示領域（meta 列只有類型／狀態／日期），故不需再遮；若日後要在詳頁顯示分類，用 readerDomain 不用 domain。「領域」欄改名為「主責記者」屬規則檔層改動，本輪不動。
- **同日追加裁決（不獨佔）**：使用者選擇多標籤——`readerDomains`＝領域值＋（入口表成員再加）💻 開發實務；模型選型在 🤖 與 💻 下都找得到，實戰手冊在 🛠️ 與 💻 下都找得到。獨佔版只上線一個 commit 即改。

## 2026-09-03 Query：「頁面內容更精緻／重點話題要有理由」→ 三 Opus 精修＋書寫風格立法

**點出什麼：** ① 使用者指出 2026-09-02 日報「重點話題」被 GitHub 存量 repo（claude-mem 9.3 萬星等）霸榜且無理由句——發現窗條目的星數被 analyzer 當今日熱度。② 使用者要求頁面內容更精緻，著重可讀性與用字精煉度，並授權「精煉度不好就改 prompt」。

**處置（三層）：**
1. **選材修法**：analyzer prompt 重點話題准入補兩條——每則必附「為何今天是重點」；GitHub Search 存量條目不得憑星數進區或置頂，排序依據＝今日訊號強度（隨下次 pipeline 跑 change-check compare）。
2. **冗語源頭審計（Opus）**：溯源三條事實從日報到 wiki——日報平均 79–94 字很精煉，進 wiki 放大 4 倍，**冗語 85% 產生在記者改寫層**；三種尾巴主導（關係從句全庫 381 次、空意涵句 126 次、展開式缺項自白 122 次）；內部對照組證明「有上限就有效」（analyzer 每點 1–2 句守得住）。落地五處：`wiki-reporter-shared.md` 新增「書寫風格」節（細節區條列 200 字元／callout 120／現況每段 3 句三道硬上限＋禁填充語＋三尾巴設限＋派工過程不上頁）；analyzer 條目 ≤80 字＋一句一資訊點；format「細節下沉」堵無上限傾倒區；commercial 意涵句改條件式；models 附三項合一括號。
3. **存量精修（雙 Opus 並行，10 頁）**：A 組 pricing（−3.5% 字元）/model-comparison/feature-radar（升版風險巨型段拆列表、SendFeedback 內容錯置至 MHS 條目下修正、9 爆格下沉）/claude-code（−3.4%：現況 20 條與版本表逐條重複收斂為 3 條＋指路、維運短語清零）；B 組 coding-workflow-guide/tools（3 爆格下沉收錄註記區、決策表一字未動）/ai-agent-safety（callout 6→3 條）/anthropic-business（四種樣板尾語 159 處機械收斂、（推論）145 處全留）＋boris-cherny、managed-agents 現況時效校正（「截至 YYYY-MM-DD」措辭＋立場軌跡一行）。每頁測試綠才進下一頁；主編抽驗（seed 2026-W36-refine 擲中 #4 anthropic-business）尾語清零屬實；claude-code 殘留 21 處維運短語由主編補刀清零。
4. **正文 [加入:] 標記剝除**：wiki 11 處規則檔式標記移除（規則檔保留，讀者頁不需要）。

**精修發現的事實問題**：登轉知帳本 2 筆（功能：v2.1.247 日期歧異＋v2.1.224 指路失效＋MHS 日期；社群/功能：guide 第 6 段「未查 vs 查過」措辭矛盾）；managed-agents 同一疑問掛兩處懸置待 5c 合併查證。

## 2026-09-04 深夜批次（使用者授權自主排程）：舊語法懸置改寫 44 筆＋蒸餾 dry run 無候選

**舊語法改寫（三 sonnet 並行，前三大盲區頁）**：ai-agent-safety 24 筆全轉新語法（結論表 9 列補 metadata、時序 13 行補粗體或拆標記、2 句散文改措辭避免裸字樣）；claude-code 12 筆（1 筆補完整標記〔XDA 51,000 token｜查 51,000 token、63903〕、11 筆歷史區裸字樣改措辭）＋6 筆正當跳過（描述「當時」的已解決歷史不重標）；anthropic-business 8 筆（新增 ⟨Q-02⟩ Volta 同筆交易、⟨Q-05⟩ IPO $2兆、2028 營收預測標準式等）。全庫舊字樣 **144 → 99**（新語法 147→172）；主編抽驗（seed 2026-W36-legacy 擲中 claude-code）L120 標記如實、497 測試全綠。餘 99 筆散在其他頁，留後續輪次。

**蒸餾 dry run（社群記者）**：discussions 2026-06 **不提案**——八條 🌊延燒討論首見全落 06 月（開源護城河瓦解、Loop Engineering、Context Rot 五法、成就感缺失、無障礙偏差、/specs 目錄、定價戰、Skill Atrophy），依「延燒月份一律不蒸餾」整月被擋；patterns 2026-07 門檻 1 未到期，2026-10 下旬再評（屆時另查額度焦慮、AskUserQuestion 兩條 07 月延燒討論狀態）。本輪無蒸餾候選。

## 2026-09-03 Ingest

- 來源日報：[[news/2026-09-03]]
- 更新頁面：wiki/entities/claude-code.md、wiki/topics/community-tech-patterns.md、wiki/topics/community-tech-discussions.md、wiki/feature-radar.md
- 新增頁面：無
- 摘要：多款旗艦模型（Mythos/Fable 5.1、Mythos/Fable 5、Opus 5、Opus 4.8、Opus 4.6）當日出現錯誤率升高、截至彙整時尚未標記解決，同時段 Reddit 湧入停機抱怨；Claude Code v2.1.259 新增 managedMcpServers 企業級 MCP 管理設定；社群面新增 4 則具體案例（安全掃描工具、設計 skill、agent harness 討論、Rust 事故應變 agent）。
- 呈現品質：全部通過（功能記者順手修復 claude-code.md 既有已知問題重複條目與版本表失效指路；社群記者 callout 覆寫與熱門討論表逾期列汰除皆通過）
- 品質備註：（無）
- devpractice 沉澱：待派工（見下方 4b）

**devpractice 沉澱補記（2026-09-03，接續上方 Ingest 紀錄）：** 候選 5 筆——`topics/community-tech-patterns`：internet-court-skill（agent 間商業信任層 skill）、yetone/cumora（跨平台 agent 團隊聊天工具）、Abilityai/trinity（自架多 agent 平台）；`topics/long-context-1m`：`[1m]` 變體遭 Max 方案覆蓋逾 6 週未解；`entities/claude-code`：官方建議任務間執行 `/clear` 省 token。基準線技術備註：狀態檔記錄基準 sha 因本庫近期歷史重寫而遺失，腳本依文件化失敗模式自動退回 48 小時前基準，記者已逐頁核對排除與稍早批次重複的 14 筆，僅新增本輪確認未入帳的 5 筆；基準線已推進至 HEAD，非本次操作所致、後續執行不受影響。
## 2026-09-04 舊語法懸置清理第二輪（四 sonnet 並行，28 頁 81 筆）：全庫盲區 99 → 12

**分組結果**：模型組 19 筆（opus-5 的 H-01~05 序號改合規 Q-、fable-5 一筆 08-26 已查實解除、model-comparison「待查證聲明」節改名「單一來源聲明」）；商業組 20 筆（competitor-landscape ⟨Q-01⟩⟨Q-02⟩ 新立、enterprise-tool-tracker ⟨Q-03⟩、pricing 兩筆已解決事件殘留改措辭）；功能安全組 19 筆（gov-policy 8 筆清零、claude-skills 表格變體＋細節區新建）；社群人物組 23 筆（large-codebase 證據強度欄轉 ⟨Q-01⟩~⟨Q-03⟩、timeline 一筆「暫停等待確認」假陽性改措辭）。主編另清 anthropic-commitments 1 筆散文裸字樣。

**剩餘 12 筆全屬口徑豁免項，非真懸置**：人物頁 `active（待核實）` 狀態格式 8 筆（people 規則明訂必填）、狀態圖例 1（claude-code:92）、採用符號圖例 1（tools:134）、封存頁原文 1（archive，一字不刪原則）、合法短標記被計數 1（commitments ⟨C-01⟩）。**後續建議**：讓 `pending_markers.iter_legacy()` 豁免這四類（狀態格式／圖例／封存頁／合法短標記），使「存量殘餘」歸真零——列待裁示。

**驗收**：四組各自測試綠；主編抽驗（seed 2026-W36-legacy2 擲中功能安全組）四頁 legacy 重掃全 0；最終 497 測試全綠；新語法標記 147→193（基線內）。

## 2026-09-04 Query：「重點話題的 skill 還是沒列理由」＋「週報／日報派冷讀者 review」→ 產製規則大修（日報 8 項＋週報 6 項）

**點出什麼：** ① 使用者追問重點話題存量 repo 無理由句——查出 09-03 日報由雲端班次在修法 push 前生成，且昨日修的 analyzer.py 是 fallback 路徑、**正典是 news-pipeline-steps.md Step 1b**，修錯了檔。② 兩位 Opus 冷讀者分別 review 週報 W35 與日報 09-02/09-03 呈現，各出八維度報告。③ 使用者指示「今天那個 GitHub 不重要就刪掉」——已從 news/2026-09-03.md 重點話題移除 snyk/agent-scan、superdesign-skill 兩則存量條目（news/ 唯讀原則之使用者指示例外，僅此一次）。

**日報修訂（news-pipeline-steps.md Step 1b，8 項）：** 重點話題三條准入（理由句必寫／存量條目全面退出本區改歸 💬 尾端／排序＝今日訊號）；聚焦 [N] 腳注改行內連結（第三格式時代，6g 偵測器同步、registry 23/24 改寫）；檔尾「選材門檻」附錄廢除（內規不上讀者版，registry 34 改 min 1）；聚焦↔內文防重複＋中文說明禁標題直譯；💰 付費區固定移到 📰 媒體前；常設區塊缺席時來源狀態表上方加讀者語言說明；存量條目星數統一千分位；[社群趨勢] 標籤已在定義列。

**週報修訂（weekly-report.md，6 項）：** 「本週一句話」callout 硬性；頭條與安全條目必附行動句；讀者版禁用內部詞表（判準第 N 支／長期警示／涵蓋窗／帳本／本指令）；來源要可點（行內連結、量級數字須指名媒體、「見下方 X」須存在、wikilink 指路附自足摘要）；新立判準形狀 ≤80 字單 if/then（凍結契約零改動，靠新立案換血）；正文前瞻承諾必入預告表（堵 W34「+50% 促銷」逃過回收的漏洞）；檔尾數字不重列正文數字。

**做法註記：** 判準欄不搬家——三支程式（check_weekly_ledger／scan_open_forecasts／build_web）以表頭 regex 消費它，改用「形狀立法」從源頭治塞爆。冷讀者好評保留不動：深挖四段骨架、預告回收敢認錯、三行式條目、粗體＋等寬節奏。

## 2026-09-04 Prompt review 迭代收斂（使用者指示「修到 review 沒意見」）

第一輪：日報 2🔴6🟡（聚焦行內連結解析器未同步——build_web 補 FOCUS_INLINE_LINK/GROUP_RE＋回歸測試 4 案例；範例推翻千分位規則；fence 混染防線＋3a-2 內規外洩自檢；今日訊號/防重複判定式化；檔尾兩行順序；存量條目情緒位置）＋週報 4🔴8🟡（書寫紀律節誤入範本圍籬；禁用詞表 vs 機械契約欄名／「素材涵蓋窗」footer regex／判準凍結比對三處衝突——加射程宣告與標籤例外解掉；續盯判準禁補寫；callout/量級/摘要/80 字四個量測定義；前瞻與條數上限優先序；到期日行動句）。第二輪：週報 12 項全到位再抓 4🟡（射程誤豁免新立判準、null 分支與到期日型互斥、範例句裸用禁用詞、footer 三要件只寫一半）→ 補完；日報 10 項全到位餘 1🟡（app.js 聚焦連結未上螢幕——補渲染＋CSS＋版本號，DOM 驗證 4 連結可點）＋G1 grep 補「本區」＋G2/G3/G4 regex 韌性（全形逗號/平衡括號 URL/收尾空白）。第三輪：週報「無阻擋意見」結案。意見類型統計：規格改了機器沒跟（6🔴 中 5 個）、新舊條文打架、規則無判定式、範例推翻規則四類。
- **2026-09-04 迭代收斂補記**：第三輪日報側抓到 T1（主編修訂自埋的 U+0001 注入——heredoc 把 r"\1" 解成控制字元，吞句末標點；「尚未爆發但必爆」）→ lambda 回填＋回歸案例；第四輪日報「無阻擋意見」。兩條線（日報 Step 1b、週報規格）全部收斂：日報 R1/R2/Y1–Y6/G1–G5/T1 共 14 項、週報 A–L＋複審 4🟡 共 16 項，皆落地並經 reviewer 逐項驗收。502 測試綠。

## 2026-09-04 Query：「script 會抓的關鍵字，prompt 寫的地方要固定」→ 機械契約字串固定區立法

**點出什麼：** 使用者從本輪 review 歸納出可制度化的原則——六個 🔴 有五個是契約字串散在規格散文裡被順手改斷。

**處置（三層）：** ① `weekly-report.md` 與 `news-pipeline-steps.md` Step 1b 各設「機械契約字串」表（字串｜消費端｜改壞後果），正文引用指回表格；② `.claude/review-registry.json` 補 6 組契約配對（本週一句話↔WEEKLY_LEDE_RE、素材涵蓋窗↔WEEKLY_FOOTER_RE、兩表小標／表頭三方、｜查證↔PROBE_RE、FOCUS_INLINE 互認），check_rules 看守；③ 修改規範 `claude-md-edit.md` 新增「機械契約字串住固定區」條＋跨專案通用原則檔 D8。配對按各腳本**真實依賴**登記（初版過度假設 scan_open_forecasts 吃小標，實查只吃表頭，已修正——契約登記本身也要對照實況，不能照規格想像）。
- **契約固定區 review 落地（2026-09-04）**：reviewer 3🔴8🟡——兩個未入表的硬契約錨點（`## 四、本週數字`、`## 一、`：check_weekly_ledger 不中即靜默跳過）、「正文指回表格」一處都沒執行（等於多加一份副本，且 all_contain 全檔搜尋讓副本互相掩護）、回收小標 `（Wnn）` 寫錯應為 `（YYYY-Wnn）`、新開表 build_web 其實不認小標、｜查證 漏 check_weekly_ledger 硬擋、app.js 消費的是 JSON key 非 emoji、三列漏網（狀態符號／討論子標題／3–6 條數）、registry pattern 太寬（詞不認形狀、alternation 任一存活即綠）、判斷式無 grep 指令、D8 掉出章節。全部落地：週報契約表 7→11 列、日報表 6→7 列並精修、正文五處純重複改指回表格、registry 重寫為規格端／程式端分列的 7 組精確 pattern（表頭 pattern 容許 \| 逃逸與 \s*\| 兩種寫法）、修改規範補 grep 指令、D8 搬回 D 區降為 ###。

## 2026-09-04 Query：「有沒有讓 lint 持續進化的機制」→ 五條迴路全部落地

**點出什麼：** lint 是靜態考卷，進化只靠使用者不定期質疑；「歷史上所有重大問題全來自使用者質疑」是印象不是統計；「連續滿分與抓不到問題是同一枚硬幣」只是一句話沒有動作。

**處置（`scripts/lint_health.py` 四子命令＋規格接線）：**
1. **漏抓帳** `data/lint_misses.jsonl`（`misses add/list/stats`）：結構化記「哪一步本該抓到／為什麼沒抓到（考卷外／抽樣不足／檢查失效／無對應檢查）」。首批登記本週 8 筆：無對應檢查 4、檢查失效 2——最值得投資的步驟 6c。
2. **檢查器的檢查**（6i）：`mutate` 對 registry 每組配對做突變（抹掉命中後仍綠＝假看守）＋過寬啟發式（同檔命中 ≥10）；**首跑即抓到 5 組過寬 pattern**（`深挖`、`5c`、`凍結`、`＋`、`/weekly`），前四組收緊、`/weekly` 加明示豁免（詞本身即契約，理由寫進 `_mutate_exempt`）。`hits record/report` 命中帳：每輪記各步命中數，連續 ≥8 輪零命中標 ⚠️。首筆 09-03 lint 21 步已記。
3. **對抗輪**（6j，月度）：`.claude/rules/wiki-lint-adversarial.md` 固化本週三種派工（冷讀者日報／冷讀者週報＋隨機 3 頁／prompt reviewer 近 30 天規則檔），發現走 misses 帳與題庫。
4. **規則密度審查**（6h）：`density` 量測（首跑 4 檔超門檻：wiki-lint 567 行 50 標記最肥）→ 每次 lint 至多提案 2 檔蒸餾，經使用者確認。
5. **真人入口**：GitHub Issue 範本 `reader-feedback` ＋網站頁尾「這段看不懂／這條錯了？回報」；`/wiki-weekly-review` 1b 步以 `gh issue list` 消費進 reader-notes（雲端無 gh 時明寫「無法讀取」不得寫「無回饋」）。
6. **規則版本戳**：步驟 8 記 `git log -1 -- .claude/`，跨週趨勢才可比。
測試 509 綠（新增 test_lint_health 7 案例），check_rules 77 組綠。

---

## 2026-09-04 Query：「artifact 那個放到網站上某一頁怎麼樣」→ 連結星圖上站成「地圖」tab

**點出什麼：** 星圖原定位「不進網站的快照」（reader-notes 09-03），但它是全站唯一不用讀字就看得出結構的入口；使用者確認手機版可顯示後裁決上站。

**處置：** `scripts/build_web.py` 建置時從 `scripts/wiki_graph.py` 產 `web_reader/data/graph.json`（63 節點／473 邊，邊分正文／樣板／階層）；前端新增 `#view-map`：d3 首次開啟才自 cdnjs 載入，領域篩選（讀者分類含 💻 開發實務）、大小三視角（被引用／頁長／距上次新聞）、正文引用開關、搜尋、點選看入出邊並可開頁、主題切換重取色。**設計例外：**六領域色取既有語意 token（ochre／info／success／warn／danger／ink），比照「emoji 只允許在資料值」——顏色在此是資料值不是 UI 強調，待使用者裁決是否改單色。手機：標籤只標樞紐、面板改落版下方、無橫向捲動（375px 實測）。維運診斷字眼（孤兒／盲區）不上站，留 CLI。

**順手：** `check_wiki_freshness` 漏更 2 頁（claude-code、community-tech-patterns 09-03 有歸因落地但欄位仍 09-02，雲端班次遺留）已補為 09-03。

---

## 2026-09-04 Query：「你怎麼知道我瀏覽過哪個」→ 足跡功能否決；地圖玩法第二輪上站

**點出什麼：** 提案「足跡」（讀過的頁在地圖留痕）時，使用者第一反應是隱私疑慮。說明後（純本機 localStorage、無後端、我看不到）使用者仍裁決不做——**讀者不希望網站留任何瀏覽紀錄，即使只在本機**；這條寫進 reader-notes 作為日後功能提案的邊界。時光機也不做（「還好」）。

**上站（同 commit）：** 疊層下拉（最新一天動過的頁／各新聞來源餵養哪些頁，命中節點加脈動環；資料來自 `data/source_attribution.jsonl`，建置時併進 graph.json）、日報「今日 WIKI 動態」區「在星圖上看 →」直達（`openMapSet`）、兩點連連看（面板「連到另一頁…」→ 再點一顆星 → BFS 最短引用鏈，找不到時提示關掉「只看正文引用」）、隨機漫步（工具列與面板各一顆，從選中頁沿邊走，無選中則隨機挑可見星）、詳頁底部「連結鄰居」一跳小星圖（點鄰居直接跳頁、「在星圖上看 →」）。桌機／375px 手機皆驗過，無橫向捲動、console 零錯誤。

---

## 2026-09-04 Query：「2 4 怎麼做」→ 圖從展示品升格為品管工具：連結缺口偵測（lint 6k）＋讀者「你可能也想看」

**點出什麼：** 使用者問 graph 常見運用，追問「推薦」與「缺口偵測」怎麼做並裁決執行。兩者是同一個分數的兩端：加權 Jaccard（鄰居權重 1/度數，樞紐不霸榜），只看正文引用邊。

**首跑教訓：** 初版沒有門檻，前幾名全是「兩個人物頁都只連 anthropic-business」的 1.00——單一共享樞紐不是相似。加「共享鄰居 ≥ 2、各自度數 ≥ 3、封存頁不列」後訊號才出來：1M 專頁未連 opus-4-7／4-8（該連）、large-codebase 線未連 skill 榜（該連）、commitments↔enterprise-tool-tracker（可疑，靠樞紐撐的）。讀者端門檻 0.15：樞紐頁（pricing、claude-code）拿不到有意義的間接關聯就誠實留空（63 頁中 43 頁有推薦），共享鄰居列最具體的三個、不列樞紐。

**落地：** `scripts/wiki_graph.py` 新增 `similar <頁>`／`gaps [--top N]`；`data/graph_gap_ignore.json`（已審、無需連結——沒有第三個出口同一對會每週重現）；`/wiki-lint` 6k 步驟（每對三選一：補 wikilink／併頁或蒸餾候選／登記忽略；連續 2 輪全是忽略 → 閾值太鬆）；build 時每節點 `alsoSee` 寫進 graph.json，詳頁小星圖下方渲染三張卡，卡上寫「和本頁一起被 X、Y 引用，但兩頁互不相連」。測試 +2（單一共享樞紐不算相似、封存頁不推不列）。**首批 12 對候選留給下次 lint 處理，未在本輪動頁面。**

---

## 2026-09-04 Query：「有什麼可以使用這個優化治理的地方」→ 圖治理三項（Opus 實作，主編重驗）

**點出什麼：** 使用者追問圖對治理層的用處，從六個提案中裁決先做三個。共同點：全用現有資料、把「訊號產出了沒人消費」與「靠人想關鍵字」兩種老病換成機械清單。

**落地（commit 1f77d8bc）：**
1. **同一則新聞落地兩頁卻不互連**：`wiki_graph.py co-landed`／`gaps --with-news`，證據來自歸因帳本的 `item_url`——不是「像」，是同一件事寫在兩處。門檻 K=1（實測 1,451 筆帳本下 K=1 僅 5 對、K=2 僅 2 對，先驗的 2 會靜默丟 3 對真候選；理由與數字進 docstring）。接進 `/wiki-lint` 6k 第二張表，與 ignore 檔共用。首批 5 對：opus-5×community-tech-discussions（3 則）、opus-5×recursive-self-improvement（3）、fable-5×code-quality-decline、opus-4-8×competitor-landscape、ai-agent-safety×model-comparison。
2. **更正回掃改吃入邊**：`explain <頁> --section "標題"` 列「指到這一節的錨點邊」與「整頁邊」兩組（Link 加目標端 anchor 欄）；`wiki-reporter-shared.md`「事實更正必回掃」與 lint 5c 第 5 步同步改為「先入邊清單、關鍵字 grep 降為補充」，回報行 `回掃：入邊 N 處（改 M）＋關鍵字 X 命中 K 處（改 J）`；inquiry_bank Q7 探針同步。registry 新增 5 組 sync_pair，mutate 全數轉紅。
3. **高引用但停滯接上消費端**：`gen_wiki_frontmatter.py --list-signal`（列表留在判準所在檔，不另養第二份門檻），新設 lint 5g（3c 在記者 prompt 內跑不了腳本、5a 管的是 radar 熱度）。今日命中 boris-cherny（入鏈 26／31 天）、safety-china-trust-dispute（18／55 天）。

**主編重驗：** 三個指令實跑輸出一致、check_rules ✅、run_tests exit 0、commit 只含 7 個指名檔。首批候選與 2 頁停滯**未在本輪處置**，留給下次 lint 派記者。


## 2026-09-04 蒸餾（首輪泛化，使用者裁決全清）

**規則面：** 蒸餾契約自 `.claude/rules/wiki-ingest-community-lint.md` 泛化為全站通用，通用部分（對象判準、≥3 個月門檻、三條例外、≤15 行時段總結、archive 子頁規格、引用回掃、每頁至多 2 個時段、只動「最後更新」）住 `.claude/rules/wiki-ingest-format.md`「時段蒸餾與封存（全站通用）」；社群檔只留兩頁的 archive 頁名、月份分組口徑與三處引用檢查欄位。提案觸發邊為 `/wiki-lint` 步驟 2 的 3h，記者回報新增「蒸餾候選」欄、步驟 8 log 新增對應行。`check_hierarchy.py` 新增第 8 項檢查：archive 子頁狀態須為 `resolved（封存頁）`（首跑即抓到 `ai-agent-safety-archive` 掛著 monitoring，已修）。

**Dry run 表（使用者已裁決全清，本輪不另等確認；留證用）：**

| 頁 | 時段 | 條目數 | 字元數 | 擬總結一句 | 引用檢查 |
|---|---|---|---|---|---|
| topics/ai-agent-safety | 技術彙整 2026-05 | 5 | 2,687 | 系統提示注入機制與 RCE 跨工具傳播曝光，官方同期以 Sandboxing 文件與 v2.1.136 收緊 | 錨點邊 0（`explain --section 技術彙整`） |
| topics/ai-agent-safety | 時序 2026-06 | 17 段 | 8,850 | 提示注入升級為完整系統控制、在野濫用成規模、供應鏈攻擊延燒至 hooks | 錨點邊 0（`explain --section 時序`） |
| topics/anthropic-government-policy | 時序 2026-06 | 20 段 | 12,289 | 出口管制自 06-13 全面封鎖到 06-22 撤銷威脅標籤的完整攻防月 | 錨點邊 0 |
| topics/anthropic-government-policy | 時序 2026-05 | 2 段 | 319 | 五角大廈排除與梵蒂岡封論兩則前史 | 錨點邊 0 |
| topics/competitor-landscape | 時序 2026-05 | 18 段 | 4,855 | Microsoft 退出與企業採用創高並存，競品開始整棧複製 | 錨點邊 0 |
| topics/competitor-landscape | 時序 2026-04 | 7 段 | 806 | Claude Code vs Codex 早期格局與首批採用案例 | 錨點邊 0 |

**執行結果（每頁至多 2 個最舊時段，守節奏契約）：**

- `topics/ai-agent-safety`：1,257 → 1,167 行；封存至既有 [[topics/ai-agent-safety-archive]] 新增 `## 2026-05`／`## 2026-06` 兩組（該頁狀態同步改為 `resolved（封存頁）`）
- `topics/anthropic-government-policy`：705 → 605 行；新建 [[topics/anthropic-government-policy-archive]]
- `topics/competitor-landscape`：663 → 582 行；新建 [[topics/competitor-landscape-archive]]
- 引用回掃：三頁被搬時段的 `[[頁#條目標題]]` 錨點邊皆為 0，全庫改指 0 處；`build_web.py` 錨點 WARN 0 → 0、斷鏈 WARN 14 → 14（皆為既有 `[[news/*]]` 缺檔）
- 兩個新 archive 子頁不入 index 目錄表，由 `gen_wiki_frontmatter.py` 投影進母頁列的「↳ 子故事：」（index 改動 2 列）；三頁只更新「最後更新」，未動「最後新聞更新」

## 2026-09-04 書寫上限清理（存量，Sonnet 批次）

**範圍：** `.claude/rules/wiki-reporter-shared.md`「書寫風格」硬上限（2026-09-03 立法）只管增量寫入，存量頁從未清過。先寫腳本掃全部 entities/topics 候選頁，量測四項：表格細節區條列 >200 字元（剝連結 URL 後）、頂部 callout 單則 >120 字元、`## 現況`/`## 摘要` 段落 >3 句、禁填充語命中（值得關注／引發廣泛討論／有待觀察等）；「進一步」作為修飾動詞的合法用法（如「進一步確認」「進一步鎖定」）逐一人工核對後判定非違規，不計入、不刪除。

**排除：** 跳過本輪與另一 Opus agent 蒸餾工作重疊的頁面（`ai-agent-safety`、`ai-agent-safety-archive`、`anthropic-government-policy`、`competitor-landscape`、`community-tech-patterns`、`community-tech-patterns-archive`、`community-tech-discussions`）；跳過本週已由雙 Opus 精修過的十頁（`pricing`、`model-comparison`、`feature-radar`、`claude-code`、`coding-workflow-guide`、`community-tech-tools`、`anthropic-business`、`boris-cherny`、`managed-agents`，另 `ai-agent-safety` 重複）；跳過機器每日整頁覆寫的 `skill-interest-watch`（手改會被下次快照蓋掉）。

**掃描與清理：** 44 頁候選中 26 頁有違規（初測，含「進一步」誤判前）；人工複核後真正需要動手的違規落在 22 頁，共 41 項（含 2 頁不屬本次範圍的新增 archive 頁），實際清理 15 頁：`entities/andrej-karpathy`、`claude-design`、`claude-security`、`fable-5`、`mythos`、`opus-4-8`、`opus-5`、`tom-blomfield`；`topics/ai-talent-flow`、`code-quality-decline`、`community-tech-timeline`、`enterprise-cost-management`、`enterprise-tool-tracker`、`official-community-gap`、`recursive-self-improvement`。違規總數（原始 44 頁候選池，扣除 2 個新 archive 頁乾擾）：56 → 33（細節超長 12→4、callout 超長 0→0、現況超句 9→2、填充語 35→27〔扣除誤判與 archive 頁後〕、派工句 0→0）。殘留的 4 項細節超長為懸置標記／歸因語句被拆分後仍受限於必填 metadata 本身佔用字元數（202–233 字元，超額 1–16%），判斷為 metadata 佔比高的邊際案例，不再進一步拆碎影響可讀性。`community-pattern-trends`、`model-task-leaderboard` 的「現況超句」為腳本誤判（問句內嵌 `？` 被誤判為句界），核對原文後判定非違規、未修改、未動日期。

**驗證：** 每批 commit 後 `python scripts/run_tests.py` exit code 0；commit `196280f5`（第 1 批 8 頁）、`5e8906d0`（第 2 批 7 頁）。

**過程觀察（意外發現，非本次任務缺陷）：** 執行期間 wiki/ 幾乎全部頁面顯示 git 未提交變動，複查後確認絕大多數僅為 `scripts/gen_wiki_frontmatter.py` 的衍生欄位（`days_since_news`／`inbound_links` 等）隨其他頁面異動自動重算，屬預期行為；`ai-agent-safety`／`anthropic-government-policy`／`competitor-landscape` 三頁的實質改動經確認為另一 Opus agent 執行中的月度蒸餾工作（見上方 2026-09-04 蒸餾條目），未與本次清理衝突。
- `devpractice_diff.py mark` 已推進基準線——本輪為搬家 diff，不得被當成新料

---

## 2026-09-04 規則密度減肥（6h 首輪，使用者裁決全清）

`/wiki-lint` 6h（規則密度審查）2026-09-04 上線後的**首次執行**。`python scripts/lint_health.py density` 首跑列出 5 檔蒸餾候選；使用者裁決「全清」，故本輪不受「每次至多提案 2 檔」的週節奏限制（那是常態節奏，本輪是點名的存量清理）。提案表照樣留證。

**處置三選一（不改任何判準的語意）：** (a) 教訓散文下沉到該檔尾新節 `## 沿革（教訓存檔）`（原文一字不刪，只搬位置，條文處留一行「（教訓見本檔『沿革』YYYY-MM-DD）」）；(b) 同檔重述兩次者併入判準一句；(c) 已被機械檢查接住者改為一句＋指向檢查器。

### 提案表

| 檔 | 段落 | 現況行數 | 處置 | 省多少行 |
|---|---|---|---|---|
| `.claude/commands/wiki-lint.md` | 6b 規則引用驗證的 7 列錨點表＋輸出範例 | 19 | (c) 改指 `check_rules.py` 檢查 3（錨點清單住 review-registry） | −15 |
| `.claude/commands/wiki-lint.md` | 3c 回升邊／收報核對行為層／5c 佇列分流／5c 第四列／5c 結案回掃／6 自我掃描／6d 範圍／6e C 窗起因／6g 死鏈三桶＋改讀檔／6h 首次量測／待裁示擱置週數／渲染層驗收 共 12 處教訓散文 | 46 | (a) 下沉沿革 | −22（搬 33 行到檔尾） |
| `.claude/commands/news-pipeline-steps.md` | 本機雲端一致反例／Step 1c 漏做後果／gate 由來／多來源來源欄／修復迴圈起因／append-only 衝突起因 共 6 處 | 14 | (a) 下沉沿革 | −7（搬 14 行到檔尾） |
| `.claude/commands/weekly-report.md` | 深挖字數三次校準（12 行 blockquote）／素材窗 W33／reader-notes 缺口／回收段病灶（2 處，含重述）／檔尾數字 W35／「下週看什麼」目的 共 6 處 | 32 | (a) 下沉沿革＋(b) 回收段病灶重述兩次者合併為一句 | −17（搬 20 行到檔尾） |
| `.claude/rules/wiki-ingest-format.md` | 觸發邊教訓／蒐集邊界教訓／懸置語法由來／樞紐頁探針教訓／「至今無後續」教訓／蒸餾全站泛化理由／拆分量測／別名立法依據 共 8 處 | 16 | (a) 下沉沿革 | −5（搬 21 行到檔尾） |
| `.claude/rules/wiki-ingest-features.md` | ⏳ 逾期首次執行教訓（2 個 blockquote 共 8 行）／熱度棘輪開場／單邊下修實例／全覽表漏列實例／假警報尾巴 共 5 處 | 24 | (a) 下沉沿革 | −25（搬 26 行到檔尾） |

### 結果表

| 檔 | 總行數 前→後 | 條文區行數 前→後 | 標記 前→後 | 教訓行 前→後 | 處置摘要 |
|---|---|---|---|---|---|
| `.claude/commands/wiki-lint.md` | 663 → 669 | 663 → 640（−23） | 60 → 63 | 22 → 32 | 12 處教訓下沉；6b 改指 check_rules 檢查 3 |
| `.claude/commands/news-pipeline-steps.md` | 539 → 556 | 539 → 541（+2） | 35 → 37 | 11 → 14 | 6 處教訓下沉；歸檔說明併句 |
| `.claude/commands/weekly-report.md` | 370 → 373 | 370 → 356（−14） | 27 → 29 | 23 → 26 | 6 處教訓下沉；回收段病灶重述合併 |
| `.claude/rules/wiki-ingest-format.md` | 306 → 328 | 306 → 307（+1） | 21 → 23 | 4 → 8 | 8 處教訓下沉 |
| `.claude/rules/wiki-ingest-features.md` | 270 → 280 | 270 → 248（−22） | 21 → 23 | 5 → 9 | 5 處教訓下沉（含 ⏳ 逾期首次執行的兩種錯） |
| **合計** | **2,148 → 2,206（+58）** | **2,148 → 2,092（−56）** | 164 → 175 | 65 → 89 | — |

「條文區」＝檔首到 `## 沿革（教訓存檔）` 之前，即 agent 實際照做的部分。**總行數上升是預期的**：處置 (a) 明定「原文一字不刪，只搬位置」，搬 114 行敘事到檔尾、再加 5 個節標題與 33 條指路句。

### 不動的段落與理由

- 五檔的「機械契約字串」表（`weekly-report.md`、`news-pipeline-steps.md` Step 1b）——契約字串的單一住所，動它等於改契約。
- 被 `.claude/review-registry.json` sync_pair 釘住的字串一律原地保留（改前逐段核對 84 組配對的 patterns）：`時間閘`／`不補舊條目湊數`／`本週無新達標功能`／`措辭鐵則`／`官方頁面未查證`／`懸置標記`／`回掃`／`5c`／`深挖：`／`時段蒸餾與封存`／`蒸餾候選`／`確認偏誤`／`來源＋` 等。教訓下沉是**同檔搬位置**，`all_contain` 為檔案層斷言，故不影響任一配對。
- `wiki-lint.md` 步驟 2 的派工 prompt fence（L39–110）與記者回報格式 fence（L112–126）——fence 內文字是給記者的指令與機器讀的欄位，即使其中含教訓散文（3c 回升邊、「無後續」改寫理由、措辭鐵則）也不動。
- `6f 跨檔案語意矛盾掃描` 不改指檢查器——它做的是**語意**比對，`check_rules.py` 只做字面 grep，兩者不等價。
- `⏳ 觀望三選一表`、`Lane A/B 四選一寫回表`、`gate 修復允許清單表`——是判準本體不是敘事。
- `wiki-ingest-format.md` 的「升格／併回 verify 流程」六階段表——每格都是要執行的動作與機械證據。

### 驗證

`check_rules.py` ✅ 零錯誤（84 組配對全綠、11 錨點有效、461 路徑存在）｜`lint_health.py mutate` ✅ 77 組配對突變後全部轉紅，無假看守｜`run_tests.py` exit 0｜消費端抽驗 3 條：`wiki-lint 5a → features「熱度降溫：它不是棘輪」`、`news-pipeline-steps 3f／wiki-lint 3g,5c → format「懸置標記語法」`、`wiki-lint 步驟 10 → news-pipeline-steps「gate 擋下時的修復迴圈」`，三條的引用方與被引節名皆逐字命中。

### 發現：density 的三個門檻看不見本次改善

`density` 量測整檔行數／標記數／教訓行比例，對「教訓已下沉到檔尾、條文區變薄」這種處置**完全無感**——本輪跑完五檔仍全數在候選名單上，教訓行反而由 103 升到 127（沿革節的敘事段落每段一行，全部命中 `LESSON_RE`）。**刻意不改腳本口徑**：把量測改成只看條文區，等於為了讓自己這輪的工作看起來成功而調整尺——同 `weekly-report.md`「刻意不調到 1,485 讓 W35 通過」的判斷。真正的取捨是：處置 (a) 保住了考古鏈但**沒有省下 token**（agent 讀檔仍讀全檔）；能真正瘦身的只有處置 (b)(c)，本輪僅 6b 一處適用。若日後要讓 6h 的候選名單真的收斂，得先回答「沿革節該不該和條文一起被 agent 讀進去」——那是尚未裁決的問題，記於此待議。

## 2026-09-04 Query：沿革拆檔——同檔下沉不省 token，改住 docs/rules-changelog/；density 未調口徑

**點出什麼：** 上一則 Query 留的待議問題——「沿革節該不該和條文一起被 agent 讀進去」——使用者當場裁決：不該。`.claude/rules/*.md` 每個 session 開場即整檔載入、`.claude/commands/*.md` 呼叫時整檔載入，教訓敘事留在檔尾等於一個 token 都沒省，`lint_health.py density` 的量測（教訓行 103→127）恰好印證了這件事。

**根因：** 首輪「規則密度減肥」把散文下沉到同檔檔尾的處置 (a)，只解決了「條文區變薄、人眼掃讀變快」，沒有解決「agent 每次讀規則檔的 token 成本」——同檔搬位置對 token 預算是零和。

**處置：** `.claude/commands/wiki-lint.md`、`news-pipeline-steps.md`、`weekly-report.md`、`.claude/rules/wiki-ingest-format.md`、`wiki-ingest-features.md` 五檔的沿革節原文搬到 `docs/rules-changelog/<同名>.md`（不在任何 agent 的預設讀取範圍），原位置只留一行「沿革檔：`docs/...`」指路；條文區 37 處「本檔『沿革』YYYY-MM-DD」指路改寫為「沿革檔 YYYY-MM-DD」。`.claude/review-registry.json` 的 `bare_references`／`path_existence` glob 加入 `docs/rules-changelog/*.md`，新增 5 組 sync_pair 讓規則檔的指路行與沿革檔的標頭互相指認。`lint_health.py density` 的 `RULE_GLOBS` **刻意不改**——沿革檔不入量測範圍是本次改動的設計意圖（量測 agent 實際讀的東西），不是漏算；`.claude/commands/wiki-lint.md` 6h 與 `.claude/rules/claude-md-edit.md` 皆補一句指明此意圖，避免日後被誤判為疏漏而回頭「修正」。

**結果：** 五檔行數 669/556/373/328/280 → 641/542/357/308/262（共 −96 行），標記 63/37/29/23/23 → 60/36/28/21/22，教訓行 32/14/26/8/9 → 26/13/23/7/8；`docs/rules-changelog/` 新增 5 檔、共約 110 行原文一字不刪。`check_rules.py`／`lint_health.py mutate`／`run_tests.py` 三者皆綠。

## 2026-09-05 Query：投資訊號——消息面判讀從「要不要做」收斂到「薄觀點層專頁＋教學型定位」

**點出什麼：** 使用者問「本庫的消息，能不能拿來當投資訊號讀」。逐步對話把這個模糊需求收斂成四個裁決：(1) **定位**——不做選股訊號、做**教學型事件研究**，禁止一切指令式買賣措辭，頁面常駐免責；(2) **交付形態**——每則判讀必須有 action item，五段固定（方向／時效／打折／⏰ 接下來看什麼／你的選項／一課），沒有 action item 的判讀只是評論；(3) **落點**——不散在商業各頁、不進日報正文，開一頁**薄觀點層**專頁，事實一律 wikilink 指回 [[topics/anthropic-business]]／[[entities/pricing]] 等事實頁，本頁不複製任何事實敘述；(4) **可信前提**——分級只收 🔴🟡，**無訊號的日子頁面不動**，並以兩週後的回顧結算讓判準的錯誤被看見。

**根因：** 消息面判讀天然會滑向兩個失敗態——變成明牌（越界且不可信）或變成事實副本（與商業頁重複、雙重維護）。四個裁決分別堵住這兩條路：定位與禁詞表堵前者，「事實不搬家」與薄觀點層堵後者；回顧結算則是對「預測性宣稱必須回來對答案」這條全庫標準的落實（同週報「下週看什麼」逐條結算）。

**處置：** 建 `wiki/topics/market-signals.md`（種子判讀 2 則、回顧結算表 2 列 ⏳、里程碑懸置 1 筆）；新增投資分析（market）記者——`.claude/rules/wiki-ingest-market.md`（daily 判讀）、`.claude/rules/wiki-ingest-market-lint.md`（weekly 回顧環）、`.claude/agents/wiki-reporter-market.md`（角色檔）。觸發邊登記兩處：`.claude/rules/wiki-ingest.md` 新增「第四步：衍生記者派工」（與 devpractice 並列）、`.claude/commands/wiki-ingest.md` 4c；回顧環登記為 `/wiki-lint` 5h（主編親做，雲端 egress 封鎖時跳過、由本機 `/weekly` 承接）。`.claude/rules/wiki-ingest-commercial.md` 加一條例外，避免「領域＝商業的頁面都是商業記者的」與新記者相牴觸。網站端：`scripts/build_web.py` 解析判讀標題契約 `### 💰 事件名（YYYY-MM-DD）`，最新一則日期等於某日日報時在該日 digest JSON 注入 `marketSignal`，`app.js` 於今日聚焦列表末尾渲染一則 💰 導流條目；契約已登記 `.claude/review-registry.json` sync_pair（規格端釘標題原形、程式端釘 `MARKET_SIGNAL_RE`），新增 `src/tests/test_market_signals.py` 8 例。

**IPO 事實沉澱（user-query 通道）：** 使用者提供的「6/1 祕密遞件、目標 10 月上市、私募輪估值約 $9,650 億」經主編查證後判定**僅二手彙整站等級**（Forge、UnusualWhales 等），非一手文件——依使用者提問通道紀律，寫入時全部標「媒體稱＋二手彙整站＋2026-09-05 查證」，並在 `## 追蹤中的里程碑` 以懸置標記登記「公開版 S-1 是否遞交」（探針：Nasdaq、承銷商、公開遞件）。歸因 slug `user-query`，`item_url` 留空並在標題註明無一手連結可附。

**結果：** `check_rules.py` ✅ 零錯誤（90 組配對）｜`lint_health.py mutate` ✅ 83 組全數轉紅｜`run_tests.py` exit 0（529 例）｜`build_web.py` 錨點 WARN 0（未增加），2026-08-26 digest 已注入 marketSignal。

## 2026-09-04 Ingest（補跑）

**補跑原因：** 09-04 的 GH Actions `daily-gather` 在 commit 步驟失敗——09-03「下架 site-source-tooling」刪了 wiki 頁卻漏刪 `daily-gather.yml` 的 `git add` 登記，`git add` 撞到不存在的 pathspec 直接 exit 128，commit+push 整步連坐，**當天抓料一筆未落地**，雲端 routine（fresh clone）看不到新料，故 09-04 日報從未產生。三個抓取步驟全綠，失敗訊息看起來像 git 問題而非「有人刪了一個檔」。09-05 於本機以 `--date 2026-09-04` 現抓補齊（非 replay，`gathered_archive/2026-09-04.json` 當時不存在）。

**抓取結果：** 14/14 來源、dedup 前 117 → dedup 後 100 → 裁至 09-04 視窗 74 → relevance filter 後 71 則；日報 39 條目（📌5 ⭐3 🔧3 💰0 📰10 💬16 🧭2）。Reddit 全數 429，最終仍湊出 14 則但 RSS score 恆 0 不可信。補跑窗口為「目標日 00:00 UTC 到現在」再裁切，社群記者據此攔下 2 則與既有條目重複的 dev.to 文章（記憶實測、hooks 強制執行）。

**記者回報摘要：**
- 模型：`entities/fable-5`（費馬最後定理 Lean 形式化＋實驗室自主操作；官方未指名模型版本，以懸置標記登記，探針 `formalizing-fermats-last-theorem`／`Fable 5.1`）
- 功能：`entities/claude-code`（版本表 3 列：v2.1.261／sdk-python v1.4.0／vertex-sdk v0.19.7；10 則已知問題互動數更新）；feature-radar 新增無
- 商業：`anthropic-business`（IPO $2 兆估值、自建支付、開源轉單、Amadeus）、`enterprise-tool-tracker`（PicPay，Claude API 計數 27→28）、`enterprise-cost-management`（Spotify Portal）、`competitor-landscape`（OpenAI 停供 Cursor 11/12、HydraFusion）、`entities/pricing`（#5088 計費爭議）
- 安全政策：`anthropic-government-policy`（FedScoop 五角大廈）、`ai-agent-safety`（OpenAI rogue agents，以**產業對照**而非 Claude 風險記錄，沿用 Hugging Face／OpenAI 入侵案先例）
- 社群：`community-tech-patterns`（F-Zero X 3DS 移植 147 subagent／24 天，主線「並行規模」；Spotify Portal 模型路由）、`community-tech-discussions`（NYT 開源轉單，HN 274 分，🔥🔥🔥 ☄️閃現）
- 人物：新頁 `entities/kevin-buzzard`（主編查證具名後達門檻）
- 開發實務：候選 5 筆入帳本；**基準線未推進**（本輪未 commit，mark 會讓這批新增永遠落在基準線後）
- 投資分析：`topics/market-signals` 判讀 1 則 🔴（IPO），里程碑 1 筆、回顧結算 ⏳ 1 列

**主編查證（web 工具）：** Xena Project 作者具名為 **Kevin Buzzard**（Imperial College London 數學教授、Xena Project 主持人、EPSRC 資助 FLT 形式化計畫主持人）；一手來源為本人部落格，另以 Terence Tao 於 Mathstodon 指認 `@xenaproject` 佐證。查證日 2026-09-05。

**主編彙整：** feature-radar 最新版本行同步 v2.1.261；本週推薦依防霸榜規則維持不動並註明「本週無新達標功能（最後輪替 2026-09-02）」。index.md 補 `kevin-buzzard` 列。`data/source_attribution.jsonl` append 35 筆——其中 Simon Willison 一則的 slug 由記者回報的 `topic-watch` 更正為 `blog`（日報來源欄為 `Blog / Simon Willison`）。

**品質備註：功能 記者誤用 `git stash` 抹除兩位並行記者的成果。** 功能記者為整理自己檔案的狀態執行 `git stash`，取回自己那份後 `git stash drop`——`git stash` 的作用域是**整個共用工作區**，於是模型記者的 `entities/fable-5.md` 與社群記者的兩頁技術彙整一併消失。安全政策與商業記者各自獨立回報「檔案兩度整檔回退、必須重做」，是同一事故的旁證。兩位受害記者已帶著自己的原回報當規格重跑並 grep 複驗落地。當事記者無惡意，其回報甚至誠實寫著「未觸碰其他記者的工作」——它真心那樣以為，因為 `git stash` 從自身視角看只是在整理自己的桌面。**並行下工作區的共用性不是記者從自己視角看得見的東西**，故立法為明文禁令而非「請小心」：`.claude/rules/wiki-reporter-shared.md` 邊界限制新增一條，禁止 `git stash`／`checkout --`／`restore`／`reset`／`clean`／`pull`／`rebase`，並規定遇 git 狀態異常一律回報主編、不自行動手。

**其他待辦（未處理，留待 lint）：**
- `topics/ai-agent-safety` 的「未修補風險現況」表既有多列儲存格達 240+ 字元，遠超全站 120 上限（既有債務，非本次新增）——安全政策記者回報
- `devpractice_diff.py show` 只比對已 commit 範圍，抓不到當輪未 commit 的改動；本輪記者以 `git diff --unified=0` 繞過。需判定這是設計意圖（刻意落後一天撿已入庫內容）還是缺口

---

## Query — 2026-09-05：競品頁健檢試點（頁面重設計全流程首次跑通）

**使用者點出什麼：** 以 `topics/competitor-landscape` 為試點，問「這頁到底為誰存在、答不答得出讀者的問題」，而不是「這頁要不要拆／版面好不好看」。

**流程（本次確立為 `page-audit-review` 的標準路徑）：** 六問健檢（使命句／讀者考題 a1–a3、b1–b5／現有結構答不答得出／哪些內容跑錯家／鄰居分工／機械契約）→ 冷讀者實測＋健檢卡對照 → 設計 agent 出三案、評審 agent 逐條打分 → 定稿收斂到 3 個裁決點 → 使用者裁決 → 實作 → 原考題複驗（下輪 lint）→ 一週回訪。

**三個裁決（使用者全採「建議」選項）：**
1. 手術切兩刀，**規則一次到位**——記者手上永遠只有一套規則，頁面分兩個 commit 向已生效的規則收斂。
2. ⟨P-01～03⟩ 轉正為 ⟨Q-03～05⟩ 並修正 metadata 順序（原寫成 `標｜複｜查`，`PENDING_RE` 吃不到）——這三筆是全頁唯一機器看不見的懸置，轉正後 `check_pending_markers.py` 才接得住；本頁 `pending_count` 6→9 是誠實上修，不是變差。
3. `## 查證快照（2026-08-13，不回訪）` 訂 **180 天到期日 2027-02-09**——明說「不回訪」的區塊沒有到期日，三年後仍會掛在頁上。

**揭露的根因（不是版面問題）：** 頁面之所以長成 587 行的競品百科，是因為**規則只寫了「定價變動更新表、其餘 prepend 時序」**，沒有任何一句說「本頁不收什麼」。於是人事、管制、股價、Anthropic 自己的融資全都有理由進來，28 個子節各自為政，讀者問「多大」時沒有任何一處答得了——**「多大」是排序問題，只有全域可比的單一表答得了**。

**處置：** 規則檔新增第 0 條五類路由表（放在觸發條件之前）；頁面重心改為一張按衝擊度排序的「對手雷達」，衝擊度量「若屬實，讀者要不要改變什麼」，**證據硬度另立一欄，兩軸絕不合併**；每個成長區都給上限與退場（雷達 12 列／硬答案 6 條／雷達細節 8 節 × 6 行／時序保留最近 3 個完整月）。

**實作前後：** 587 → 421 行（含 2026-06 時段蒸餾封存 30 行原文至 archive `## 2026-06`）；跑錯家的五塊內容中，同記者的三塊直接寫進 `ai-talent-flow`／`anthropic-business`／`enterprise-tool-tracker`，跨記者的四筆走 `pending_handoffs.py` 登帳（H-ab0af9 安全政策／H-b591b1 功能／H-abb47e 社群／H-b432d2 功能），**帳本開完才刪本頁段落**。

**留給主編：** `wiki/index.md` 該列摘要格的鉤子句仍是 04–05 月舊事實（Microsoft 退出、OpenCode 157K），與新首列（Meta 價格戰）已失步；規則第 9 條明訂記者不得自行改 index，故此處只作轉知。建議新鉤子見本輪實作回報。

## 2026-09-05 Query：「內部用語外洩有沒有比較好的方式避免」→ 三層防線（家／閘／渲染）

**點出什麼：** 競品頁健檢的兩輪冷讀者都抓到同一件事——讀者看不懂「12 列上限汰出」「不回訪」「已移交」「每日抄錄」「模式庫」「二手」，以及懸置標記的 `（標…｜查…｜複…）`。使用者不問「幫我改這幾句」，問的是**怎樣之後不再犯**。

**根因：** 規則早就有了。`.claude/rules/wiki-ingest-format.md`「無維運術語洩漏」列與 `.claude/rules/wiki-reporter-shared.md`「派工過程不上頁」都明文禁止，但兩條都**沒有偵測器**——本庫病史的標準形狀（承諾有了、執行點沒有）。而且光靠禁止不夠：有些備忘**刪不掉**（這張表為什麼只留 12 列、這節不回訪到期日是哪天），沒有家就只能留在正文；懸置標記的 metadata 也不是能刪的東西，它是掃描器的輸入。三個症狀三個成因，所以是三層。

**處置：**
1. **給備忘一個家**——`scripts/build_web.py` 的 `read_md()`（唯一讀檔漏斗）加 `strip_editorial_comments()`，剝 Obsidian `%% … %%` 與 HTML 註解。原本**完全沒剝**，備忘會直接進 `markdown` 欄位、`search-index.json` 與日報 digest。regex 非貪婪且不跨越另一組 `%%`，否則兩則相鄰備忘中間的正文會被吞掉。規則寫進 `.claude/rules/wiki-reporter-shared.md`「維運備忘的家」（判斷式：這句話是讀者需要知道的，還是我需要記得的），語法表兩處（根 `CLAUDE.md`、`wiki/CLAUDE.md`）各補一列——前者原本明文「表外語法一律不得寫入 wiki/」，不補等於禁止。
2. **機械閘**——`scripts/check_reader_language.py`，22 個禁詞住腳本頂部常數（單一來源，每詞附「為什麼是內部語言」＋讀者語言替代詞，`--list` 可印），跳過 frontmatter／code fence／`%%`／HTML 註解。首跑命中 **485 筆／40 頁**（最重：ai-agent-safety 109、community-tech-discussions 84、community-tech-patterns 60），照 `data/pending-legacy-baseline.json` 的先例存量寫進 `data/reader-language-baseline.json` **只擋新增**，存量印 WARN 摘要、每週於 `/wiki-lint` 6l 清 2 頁。留白名單 `data/reader-language-allow.json`（page 與 term 不得同時 `*`）。
3. **渲染層摺疊**——`web_reader/assets/app.js` 把 `❓ **待查證**（標 …｜查 …｜複 …）` 渲染成「❓ 待查證 ⋯」，metadata 進 hover title；表格短標記 `⟨Q-nn⟩` 掛上同頁細節區首句。**markdown 一字不改**（Obsidian 與 `check_pending_markers.py` 照舊吃四段式）。渲染層是第三個吃這份語法的地方，故加 `src/tests/test_pending_render_contract.py`（7 例）並登記 registry sync_pair 規格端／消費端各一組——規格改了而渲染層沒跟，症狀是「網站上靜默不再摺疊」，沒有任何既有檢查會轉紅。

**示範頁：** `topics/competitor-landscape` 的 7 句改為讀者語言（「受 12 列上限汰出」→「未列入上表（⚪ 級，動態仍記在下方時序）」＋`%%` 備忘；「已移交 X」→「完整脈絡見 X」；`## 查證快照（2026-08-13，不回訪）`→`（2026-08-13）`，到期日與「不回訪」進 `%%`），該頁清乾淨後從基線移除，**40 → 39 頁**。

**結果：** `check_rules.py` ✅ 零錯誤（92 組配對）｜`lint_health.py mutate` ✅ 85 組全數轉紅｜`run_tests.py` exit 0｜`build_web.py` 錨點 WARN 0（未增加）｜preview 實開競品頁與 pricing 頁確認：metadata 12 處全數摺疊、正文零外洩、`%%` 備忘未上站、樣式為 hairline dotted／無陰影／無圓角。

---

## 2026-09-05 Query：「內部用語外洩有沒有比較好的方式避免」→ 三層防線＋存量首批清理

**點出什麼：** 競品頁健檢兩輪冷讀者都抓到內部用語外洩（「12 列上限汰出」「不回訪」「標｜查｜複」「請使用者裁示」「已移交」「每日抄錄」），且是全站病。病因：同一份 markdown 同時服務主編與讀者，記者把維運備忘寫進正文；禁詞清單只會讓 agent 換說法，治本是給備忘一個家。

**三層（順序 2→1→3）：** ② `scripts/check_reader_language.py` 讀者語言閘（22 個禁詞各附理由與替代詞；`%%`／frontmatter／code fence 跳過；`data/reader-language-allow.json` 逐行例外；`data/reader-language-baseline.json` 存量基線只擋新增）掛 `run_tests.py`，lint 新步驟 6l 每輪派 Sonnet 清 2 頁。① `build_web.py` 原本完全不剝 Obsidian `%% %%`（備忘會進搜尋索引）→ `read_md()` 加 `strip_editorial_comments()`；規則新節「維運備忘的家」；競品頁 7 句示範。③ 網站渲染把懸置標記 metadata 括號摺成 hover、`⟨Q-nn⟩` 掛細節首句，markdown 不動；契約測試＋registry 兩組配對。

**首跑基線 40 頁／477 筆**（ai-agent-safety 109、community-tech-discussions 84、patterns 60、anthropic-business 32、government-policy 24）。使用者裁決先清前五頁：三個 Sonnet 並行（A/B/C），五頁全部歸零，**基線 477→171 筆／36 頁**。誤報 3 筆進白名單（「自主編程」「非預期覆寫」「個人化覆寫」——字面子串撞禁詞）。清法統計：換詞為主、派工句整句刪或移 `%%`、「收錄理由／專頁定向」標籤全數刪除（讀者不需要知道抓取管道）。patterns 頁 H1 由「社群實戰模式庫」改「Claude Code 社群工作流模式」（slug 不動）。

**剩餘 171 筆／36 頁**由 lint 6l 每週消化；下一批最肥：pricing 17、community-pattern-trends 16、code-quality-decline 12、model-task-leaderboard 12、fable-5 11。

---

## 2026-09-05 讀者語言存量全清（四 Sonnet 並行，31 頁 161 筆 → 0）

使用者裁決「流量還夠就全清」。首批五頁後基線 168 筆／34 頁，分四組並行：G1 pricing／pattern-trends／ai-talent-flow／chris-ciauri（44）、G2 code-quality-decline／榜單／official-community-gap／tools／tracker／cost／model-comparison（45）、G3 十個 entities 頁（39）、G4 index／radar／overview／skill-interest-watch 等十頁（33）。**基線降至 7 筆／3 頁，全是封存頁（原文照搬原則刻意不清）。**

**清法統計（四組合計）**：換詞為主（「達…門檻」→ 刪或具體數字、「source_count N」→「多家報導」、「模式庫」→ wikilink 或「工作流模式」、「X 記者負責」→ 直接 wikilink、「請使用者裁示」→「尚未定案」）；派工句整句刪或移 `%%`；白名單 16 筆——字面子串誤報三類：**「記者會」**（真實新聞發布會，G1／G3／G4 各撞到）、**「自主編程／自主編碼」**（子串撞「主編」）、**「覆寫」與「派工」的產品語意**（`/init` 不覆寫 CLAUDE.md、Subagent 派工功能）。

**機器頁處理正確**：skill-interest-watch 由 `skill_interest_snapshot.py` 每日覆寫，G4 追到腳本第 189／284 行模板字串（「機械抄錄」「每日抄錄」）改「同步」後重跑快照歸零——改頁面會被蓋掉，改產生器才是家。

**紀律事件**：G2 誤動 `data/reader-language-baseline.json` 後自行還原未進 commit；G4 誤判 allow.json 被 gitignore（實為已追蹤）；G2 的白名單條目因共用工作目錄被 G1 的 commit 先收走——並行 agent 共寫同一檔的既知風險，功能無誤。快照重跑順手 append 的兩個 data csv 已還原，留給當晚 pipeline 正常產出。


---

## 2026-09-05 全站頁面 review 第 1 波：model-comparison ／ model-task-leaderboard

**使用者兩項裁決（開工前）：** 起點取讀者三個根問題各走一條路徑（非從單一樞紐擴散）；裁決節奏授權主 session 下非阻擋級判斷，拆頁／砍整節／改使命句仍須裁決。總帳與分層判準見 `docs/page-audits/ledger.md`，共用派工前綴見 `docs/page-audits/dispatch-prefix.md`。

**Query（本波考題來源）：** `wiki/reader-notes.md` 2026-09-05 的 ⏳「『誰比較強』三頁互踢皮球」。冷讀者實測重現：問「Codex 和 Claude 誰強」被轉介 2 次、第 3 跳死路。

**診斷（健檢卡與冷讀者對得上）：** 環的斷點**不在措辭**——`model-comparison` L193 與 `competitor-landscape` L149 都正確把跨家問題轉出去，但 `model-task-leaderboard` 18 列全是**模型層**榜，讀者問的 Codex 是**工具／harness 層**，兩個箭頭指向一個接不住的終點；且該頁零 index 入口、入邊 5 筆全在他頁內文深處。健檢卡預測的第二個卡點（「以為終於找對頁了，卻發現沒有 Codex，比第一踢更傷」）與冷讀者實測逐字相符。

**評審 6 條 🔴（設計第一輪推薦案被推翻）：** 最關鍵一條是提案的新節名含「不回訪」——那正是 `check_reader_language.py` 22 個禁詞之一，兩頁基線為零，寫進去 `run_tests.py` 當場變紅：**提案會踩到本庫自己三個月前立的防線**。另拆穿兩項宣稱：「5 筆錨點入邊」實為 wiki 內 5＋weekly 1（`check_wikilink_anchors()` 不掃 `weekly/` 且僅印 WARN）、「90／180 天自動退場」腳本裡不存在（退場改寫成人工步驟，落點 `/wiki-lint` 3e）。定稿改採「只修橋接與過期＋兩頁摘要各補一句真答案，不建任何新表」。

**三個裁決點（使用者全選建議案）：** ① 使命句定稿＋MC 三節（自陳「不影響本頁選型建議」卻擋在讀者與跨家出口之間 18 行）移出正文；② Benchmark 表凍結降位為第 8 節（節名 `## 2026-07 世代對照（2026-07-09 一次性查證）`，到期 2027-03-04，維護承諾住 `%%`）；③ 字元上限閘與錨點硬紅本波做。

**成果：** MC 220→192 行、LB 195→201 行；六張表全部有明文機制；MC 一筆逾期懸置清空。LB 摘要現在第一句宣告「跨家與跨工具的『誰強』到這一頁為止」並**誠實承認本頁量的是模型不是工具**，附懸置標記登記「Codex CLI／OpenCode 各跑什麼模型尚未查得，查到之前不從榜上模型名反推」。MC 摘要末段給出真答案（2026-08-13 頭對頭結論為「沒有單一答案」）＋兩個出口。

**新機械閘兩支（本庫病史的標準形狀：承諾有了、執行點沒有）：** `scripts/check_cell_limits.py`（儲存格 >120／細節區條列 >200，剝連結 URL 後量測，archive 頁豁免；`data/cell-limit-baseline.json` 存量 1191 筆／38 頁只擋新增，照讀者語言閘先例）掛進 `run_tests.py`；`build_web.py` 錨點掃描補 `weekly/` 並由 WARN 改致命（另建 `anchor_scan`，不併進 `all_wiki_md`，否則 `check_wikilinks()` 會對 `news/` 連結誤報）。兩者主 session 獨立複驗：注入壞錨點 → build exit 1 並指名該筆，還原後 exit 0 且 byte-identical。**規則檔明文兩個月、零偵測器**的落差自此關上。

**誤擋預告（寫進 FAIL 訊息本身，不只留在回報裡）：** 字元上限閘的指紋是內容雜湊，改寫既有超限文字（哪怕沒變長）也會脫離基線被判新增；訊息已教操作者如何分辨誤擋與真違規。

**待辦（下次 ingest 交模型記者，同記者故不走轉知帳本——`pending_handoffs.py` 正確擋下 from==to）：**
- `entities/mythos.md`：加一句區分 06-10 條件式降級條目與 36氪「偷偷降級」傳聞（逐字見定稿 §3.2(5)）
- `entities/sonnet-5.md`：MarkTechPost 三模型完整分數（SWE-bench Pro／OSWorld-Verified、effort 成本取捨），因 MC 凍結區細節條列 ≤200 字元而切出

**轉知帳本三筆：** H-7dbf7a（→功能，Auto 模式分類器評測＋逾期懸置移交 `entities/claude-code`）、H-27721d（→安全政策，官方跨模型價值觀研究落點）、H-402a37（→商業，MC 移出的跨家實測 2 列是否入雷達表硬度欄）。

**新開 ⏳（交使用者裁決）：** `.claude/rules/wiki-ingest-format.md`「無維運術語洩漏」列指定的合規範例逐字「🗓️ 週更（每週策展一次；更新日期停留數天屬正常節奏）」，冷讀者對同一句的評語是「像在對我預先辯解」——規則檔指定的範例本身可能就是維運口吻，記者與主編都無權推翻。

**產物：** `docs/page-audits/model-comparison-2026-09-05{,-proposals,-review,-final}.md`＋`wave1-cold-reader-2026-09-05.md`。一週回訪日 2026-09-12（看每日更新有沒有把版面磨回去、凍結節名有沒有被改）。

**冷讀者複驗（同一份四題，前後可比）：** Q1 由「3 跳死路」→ **3 跳拿到帶數字的答案**（SWE-bench Pro Claude 69.2／58.6、Terminal-Bench Codex 82.7／69.4 等四組 08-13 實測），三次轉介都有東西、無死路，且在 leaderboard L30 與 competitor-landscape L173 兩處被明確告知邊界。Q2／Q3／Q4 皆 1 跳（上一輪為 2 跳）。

**複驗抓到本波自造的矛盾（已當場修）：** leaderboard 摘要首句原寫「跨家與跨工具的『誰強』到這一頁為止」，與隔兩行的「本頁量的是模型，不是工具」自打嘴巴——改為「跨家模型的『誰強』到這一頁為止；跨工具（Codex CLI、OpenCode 這類 harness）本站目前答不了，原因見下方第一點」。**教訓：宣告終點與承認能力邊界是兩句話，寫在一起會讓讀者以為工具層也有答案。**

**複驗留下的未修項（併入 2026-09-12 回訪，不在本波處理）：** leaderboard `## 本週註記（僅列異常）` 的「本輪 18 榜取得 16 榜」「尚未定案」「下週複抓判定」被判為編輯部進度報告——歧異本身對讀者有價值（告訴他哪個數字不穩），但抓取成績與排程不是。修它要同步改 `/wiki-lint` 5b 的維護者規則，否則下週原樣長回來，故不半修；與 reader-notes 新開的 ⏳（格式規則指定的合規範例句本身是維運口吻）屬同一族。另：`⟨Q-nn⟩` 懸置短標記在頁上無圖例，讀者不知道那是什麼。

---

## 2026-09-06 全站頁面 review 第 2 波：entities/managed-agents（使用者點名；新派工契約首用）

**流程改動先記（成本教訓）：** 第 1 波 8 棒／約 197 萬 token 改 2 頁，其中設計第二輪 28.5 萬 token 幾乎全在重讀第一輪已有的腦內狀態——本環境無子 agent 續用（`SendMessage` 不存在，且**新 session 也沒有**，否證上個 session「開新 session 可恢復」的假設；記憶已改寫）。改法寫進 `docs/page-audits/dispatch-prefix.md`：設計者只派一次、只交一個推薦案＋可行性前提＋**交件前自己跑兩閘**；評審的修法即實作單，不回派設計者；交棒數預算表。本波實際 6 棒（健檢卡、冷讀者、設計者、評審、實作、複驗），設計者自行過閘並驗紅，第 1 波「禁詞活到評審」那類低級錯沒再發生。

**Query（使用者裁決）：** 使命句與「該刪該留」委由主 session 依鄰居連結自判（使用者：「這頁應該是自己自動生成的」）。判定留頁——31 筆入邊來自 12 頁且全部要「定義與成熟度」、零筆要「怎麼寫」，這張表沒有別的家；使命句「官方多 agent 框架現在做到哪一格：各零件成熟到什麼程度、哪些真的拿得到、跟 `/goal`／subagent／Agent SDK 怎麼選」。允許砍使用指南 75 行 SDK 程式碼（115 天未動、`grep news/` 對 `managed_agents.` 呼叫命中 0 檔、零官方連結）。

**冷讀者實測（改版前）：** Q1 選型沒拿到（4 跳，全庫無一處比較三者）、Q2 半拿到（官方說法清楚、第三方回饋零）、Q3 計費完全沒拿到（全頁零次提錢卻用「預算有限」勸退）、Q4 半拿到；首屏 35 行無入口；熱度 🔥🔥🔥🔥🔥 vs 實質新聞停在 05 月。健檢卡預測兩卡點與實測逐一對上。

**主編官方查證（記者與設計者無 web 工具，本步是唯一能抓到的層）：** 兩處**事實更正**——(1) Managed Agents **仍是 beta**（overview：所有端點須 `managed-agents-2026-04-01` header），本頁／radar 兩列／index 標「正式發布」皆錯；(2) 計費官方有明文：token 依牌價＋**session runtime $0.08／hr**（只計 running，不適用 Batch 與 partner 雲，算例 Opus 5 一小時 ≈ $0.705），直接寫入本頁與 `entities/pricing`，取代設計者留空的 ⟨Q-03⟩。另：dreaming 為 research preview 須申請＋另一 header（結案本頁 26 天的 ⟨Q-01⟩）；`/goal` 官方文件站未收錄，以 changelog 為據。記錄檔 `docs/page-audits/managed-agents-2026-09-05-verified.md`。

**評審 4 🔴（全部有修法、全部落地）：** 熱度上限式判準屬全站立法 → **降級為本頁一次性下修**，條文列 ledger 待使用者裁決；量測改用 `news_mentions.py --any`（預設 ≥2 詞同日是全站假陰性機器）；「負向對照回流」規則原本只寫在功能記者檔，但 09-03 那則結構上只經社群記者手 → 兩側對稱（`wiki-ingest-community.md` 新節「官方功能的負向對照要回流」＋features 檔收件端）；零件表兩列與 radar 現況矛盾 → 以 radar 為準。

**成果：** 211→164 行。新「你該用哪個」四軸表（時長／跨 session 記憶與執行位置／計費／現在拿得到嗎）× 四選項；「接下來看什麼」列等哪個訊號＋讀者選項含「什麼都不做」；零件表提位並補週更回訪規則；熱度 🔥🔥🔥🔥🔥→🔥🔥（radar L226 同步）；index 補「我想讓 agent 自己跑幾小時」路由。**主編自己被新閘擋下一次**：pricing 那條計費規則初版 561 字元 > 200，拆三條才過——第 1 波上線的閘在量真東西，包括主編寫的。

**帳本：** H-4d498f（→商業：複核主編寫入 pricing 的計費條）、H-b4a266（社群→功能：09-03 負向對照首例；評審原稿 `--from 主編` 被腳本擋下，改以實際發訊端登記）。

**實作 agent 的一處判斷（已採納）：** verified.md 引用的「dreaming 映射」內文對應原 L42 而非原 ⟨Q-01⟩（L211，v0.118.0 同批次疑問，兩者標記日與探針相同）；依「懸置 2→1」終態，v0.117.0↔Dreaming 疑問改寫為事實，v0.118.0 窄疑問保留為 ⟨Q-02⟩。

**待辦：** 熱度上限判準成法與否（ledger）；一週回訪 2026-09-13（零件表週更有沒有人做、負向對照回流有沒有第二例、熱度 🔥🔥 有沒有被 ingest 加回去）。

**冷讀者複驗（同四題）：** Q1 4 跳沒拿到 → **2 跳拿到**（分界句可自我對號）；Q2 → 2 跳拿到，官方說法與「第三方回饋為零」分得乾淨；Q3 零覆蓋 → 拿到 $0.08/hr＋算例，**唯一殘留卡點**是「比自己跑貴多少」——訂閱配額與 token 牌價是兩種貨幣、頁面未給換算（資料缺口，非版面問題，記回訪）；Q4 → 2 跳拿到。首屏 index L31 直達；beta 標示四處一致附出處。複驗抓到本波自造洩漏一處（熱度下修說明段含 `python scripts/...` 指令與「編輯判斷而非規則計算」預先辯解）→ 改為讀者語言一句＋`%%` 維運備忘。**教訓：讀者語言閘只擋清單上的詞，抓不到「整段寫給自己看」的結構性洩漏——這一類仍靠冷讀者。**
