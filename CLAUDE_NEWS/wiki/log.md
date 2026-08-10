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
- [商業] Yahoo Finance「Anthropic 與成立七個月新創簽下 100 億美元歐洲算力合約」——商業記者查證時發現與既有 08-04 已記錄的 Volta 交易（100 億美元、成立 8 個月的英國新創）高度相似，但兩則報導皆未具名新創公司、成立月數與地區描述有些微差異，記者無法確認是否為同一筆交易的不同媒體轉述，暫依「疑似重複、未確認」處理寫入 `topics/anthropic-business.md`；需查證原文釐清是否為同一事件
