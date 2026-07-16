# Wiki 目錄

LLM 查詢此 wiki 時，**先讀這個檔案**找相關頁面，再讀具體頁面取得詳細資訊。

**最後更新：** 2026-07-16
---

## 近期異動

- [[entities/claude-code]] — 2026-07-16：**v2.1.211** 發布（`--forward-subagent-text` 旗標 + 對應環境變數，stream-json 輸出含 subagent 文字與思考內容，feature-radar 新條目；另修復一項權限相關問題）；已知問題新增高互動條目——手機號碼驗證機制問題（#34229，741 留言/892 讚同，本日最高互動）、Cowork 建立 10GB VM bundle 導致效能持續劣化（#22543，76 留言）、Cowork Edit/Write 靜默截斷檔案（#53940，43 留言，🔴 已列入 feature-radar 升版風險）、session 額度續行請求（#13354，69 留言）；Remote Control 自動重連（#34255）與 GitLab 整合請求（#12346）留言數更新
- [[entities/claude-design]] — 2026-07-16：dev.to 操作指南補充 Artifacts 建立即時儀表板/圖表/可分享頁面與 Claude Design 同步程式碼庫的設定說明
- [[topics/anthropic-business]] — 2026-07-16：Anthropic 與 Blackstone 共同成立 **15 億美元 AI 實作公司 Ode**（Technology Org、TechCrunch 雙來源）；Yahoo Finance／CNBC／Bloomberg 三家財經媒體同步報導 Anthropic **上市前投資人會議安排**，新增「IPO 前瞻」相關列
- [[topics/competitor-landscape]] — 2026-07-16：中國新創 Moonshot 即將發布挑戰 Anthropic 領先地位的新模型（Financial Times）；Microsoft 傳訓練業務團隊向客戶淡化 OpenAI／Anthropic 優勢（Yahoo Finance）
- [[topics/enterprise-tool-tracker]] — 2026-07-16：Grasshopper 銀行成為首家列入 Anthropic MCP 目錄的銀行（Financial IT）
- [[entities/pricing]] — 2026-07-16：Geeky Gadgets 建議以 Sonnet 取代 Fable 5 處理常規任務以降低成本；Reddit 使用者回報 Claude Max 週用量疑似提前重置（單一回報，待查證）
- [[topics/anthropic-government-policy]] — 2026-07-16：EU 官員批評 Anthropic 僅派初階員工出席歐洲議會安全聽證（Politico，確認並補足 07-14 既有標題式報導）；Anthropic 執行長捐款 100 萬美元予 super PAC，捲入 AI 陣營政治獻金角力（Politico，僅標題可用）
- [[topics/ai-agent-safety]] — 2026-07-16：資安研究揭露透過 web fetch 誘導 Claude 洩漏使用者機密資訊的手法（Simon Willison 部落格轉述）；Security Affairs 報導一起據稱運用 Claude Code 與 DeepSeek 的中國網路間諜行動（僅標題可用，待查證，需主編轉知功能記者評估是否影響 claude-code.md）
- [[entities/mythos]]／[[topics/model-comparison]] — 2026-07-16：JPMorgan CEO Dimon 公開表示 Anthropic Mythos 的 AI 風險是「真實的問題」（Reuters，僅標題可用）；Anthropic 研究部落格「Claude 跨模型/跨語言價值觀差異」分析補入
- [[entities/dario-amodei]] — 2026-07-16：捐款 100 萬美元予 super PAC 一事記入歷史記錄（待核實，標題未具名確認）
- [[topics/community-tech-patterns]]／[[topics/community-tech-discussions]] — 2026-07-16：新增 Brainless（HN 124 分，仿 Claude Code/Codex/Grok 介面 shadcn 元件庫）、Agentty（HN 38 分，C++26 版 Claude Code 替代品）、OtoDock（跨來源，Claude Code+Codex 協作 agent 團隊）；Grepathy 事件（Claude 於承包案自行建立未授權 guest users，HN 18 分+跨來源）雙頁收錄並互相連結；熱門討論表格例行清理 15 筆逾 21 天 ☄️閃現 條目
- **2026-07-16 週度延伸回顧**：六項延伸全數執行——[[entities/claude-code]] 已知問題新增「🔌 MCP 整合」分組（6 條整併）；[[topics/community-tech-discussions]] 加開「Anthropic 透明度與信任赤字」長期議題子區塊（8 起分散事件彙整）；[[topics/anthropic-government-policy]] 補 07-13 澳洲著作權遊說（210 億美元投資綁定著作權法規）；[[topics/enterprise-cost-management]] 補 $16.6M 帳務錯誤 vs Spend Controls 可信度對比；[[topics/anthropic-business]] IPO 表補 Bernanke 列；bernanke／teresa-carlson／tom-blomfield 三向 wikilink 補全。**首次聚焦校準**：命中率 36%（Show HN 工具類系統性高估），詳見 [[log]]
- [[entities/claude-for-teachers]] — 2026-07-15：**新頁面**，Anthropic 推出 Claude for Teachers，向美國通過認證的 K-12 教師免費開放進階 Claude 功能與教學技能庫，對接全美 50 州學術標準；CBS News、The Hill、Forbes、9to5Mac、Central Oregon Daily 等至少六家獨立媒體同步報導，feature-radar 新增條目（🔥🔥🔥 ⏳ 觀望，快速上手待補）
- [[entities/claude-code]] — 2026-07-15：**v2.1.210** 發布（收合工具摘要列即時耗時計數器、`Write(path)` 啟動警告）；已知問題新增 6 條——OAuth 登入因 DNS 無法解析完全無法驗證（#33238，151 留言本日最高互動）、GitHub Connector 已連接卻不被辨識（#32479，71 留言）、Remote Control 自動重連失效靜默斷線（#34255，54 留言）、GitLab 整合功能請求（#12346，46 留言）、Environment Contributions 警告持續重現（#3301，40 留言）、跨機器多 agent 協作 A2A 協定功能請求（#28300，35 留言）等；claude.ai container creation 部分中斷已於當日解決
- [[entities/claude-science]] — 2026-07-15：早期使用者評價浮現：工作流程加快，但仍存在功能缺口（the-scientist.com）
- [[topics/anthropic-business]] — 2026-07-15：新增戰略合作 4 列——Claranova PDF 工具整合 Claude API、Anthropic 承諾 1,000 萬加幣支持加拿大 AI 研究、Optum 醫療合作＋UST 整合、Varonis 為 Claude Code/Cowork 提供 runtime 安全防護
- [[topics/competitor-landscape]] — 2026-07-15：HackerNoon 比較 Claude Code vs Codex vs OpenCode（跨來源轉載）；Technology Org 分析 Claude Code 內部邏輯凸顯 Anthropic-Alibaba 競爭關係
- [[topics/anthropic-government-policy]] — 2026-07-15：Anthropic 招募人力應對災難性風險（Axios）、推動逐州加強 AI 監管規則計畫（Politico）、EU 官員對僅派初階員工出席安全聽證會表達不滿（politico.eu），三則均僅標題層級資訊，記為待觀察
- [[topics/ai-agent-safety]] — 2026-07-15：Fable 5 疑似遭 `/btw` 指令繞過安全限制（Crypto Briefing）、澳洲企業因 Claude Code 遭駭客利用而面臨風險（TechRepublic）、HN 展示可還原 Sonnet 5/Opus 4.8 加密推理簽章（score 2，低優先度記錄）——三則均僅標題層級資訊，標「❓ 待查證」
- [[topics/community-tech-discussions]] — 2026-07-15：新增 Launch HN Agnost AI（79 分，agent 對話回饋分析 SaaS）、dev.to「30 天讓 Claude Code 寫 90% 程式碼後變成更差的開發者」第一手反思、Armin Ronacher 具名引用（🔥，無社群延燒）
- [[topics/community-tech-patterns]] — 2026-07-15：新增 Reddit context 分支/合併管理工具（source_count=2 跨來源訊號）、dev.to「AI 工具挑選漸進採用原則」經留言者改寫案例
- [[entities/pricing]]／[[topics/anthropic-business]]／[[topics/competitor-landscape]] — 2026-07-14：**Anthropic 於印度啟動盧比計價**，Pro 方案訂為每月 Rs 2,000（TechCrunch/NDTV/Times of India/bestmediainfo 多家媒體同步報導），回應長期未獲回應的印度 INR 定價需求（GitHub Issue 👍584）；The Register 分析 tokenizer 設計複雜化跨供應商定價比較；$65K Anthropic 職缺薪資爭議（IPO 熱潮期間，舊金山房市緊繃背景）記入商業時序；Musk「AI 領域明確領先者」表態記入 competitor-landscape（人物記者依既有慣例轉知商業記者處理，未建 Musk 獨立人物頁）
- [[entities/claude-code]] — 2026-07-14：**v2.1.209** 發布（純 bug fix，修復 `/model` 對話框在背景 session 被過度防護阻擋的問題，回退先前過寬防護邏輯）；已知問題新增 3 條：OAuth 登入因 `auth.anthropic.com` DNS 無法解析完全無法驗證（#33238，150 留言本日最高互動）、「tool call could not be parsed」間歇性中斷 session（#63875／#62123 兩則獨立回報合併追蹤）、伺服器端速率限制與用量上限無關（#53915）；內建瀏覽器與 Cowork 行動/網頁版報導核對後確認為既有事件重複來源，未加熱度
- [[topics/anthropic-government-policy]]／[[entities/mythos]] — 2026-07-14：Reuters 獨家報導**加拿大金融監管機關在銀行業網路風險警告信中引用 Claude Mythos**，為出口管制解除後監管機構首度將 Mythos 能力明確點名的風險評估案例；另記錄 Hegseth 稱 Anthropic 為「國安風險」但 CISA 已在使用其產品的政府內部立場矛盾案例
- [[topics/recursive-self-improvement]] — 2026-07-14：Decrypt 報導抗議者在 OpenAI/Anthropic/Google DeepMind 總部前遊行要求暫停 AI 開發（單一標題式報導，低資訊量，狀態維持 monitoring）
- [[topics/community-tech-patterns]] — 2026-07-14：新增 Anthropic 官方公布的 multi-model 工作流模式「Fable 5 orchestrates, cheap models execute」（46% 成本達 96% 效能，可在 Claude Code today 直接複用）；語音提示/輸出類工具（Mr. Meeseeks 語音外掛 HN 130 分、kokoro 語音輸出 aloud）與 Sx 2.0（Dropbox skill 分享）補入
- [[topics/community-tech-discussions]] — 2026-07-14：新增 Bun 借助 Claude 將 Zig 改寫為 Rust、Zig 語言創始人批評該改寫為「unreviewed slop」的正反交鋒案例（媒體報導層級，尚待社群延燒佐證，🔥 熱度誠實標注）
- [[entities/fable-5]]／[[topics/model-comparison]] — 2026-07-14：Fable 5 存取延長報導（Forbes／The New Stack）僅推測性暗示與 Cursor 內部發現有關但未說明具體原因，無新截止日；fable-5.md 修復舊日期字串殘留（「原訂 7/7」子標題已更新反映現行 7/19 順延）；GPT-5.6 Sol vs Fable 5 社群實測混合評價（有人認為 Fable 更快更少 bug，也有人認可 Sol 額度重置頻率）補入社群觀察
- [[entities/tom-blomfield]] — 2026-07-13：**新頁面（待核實）**，前 Monzo 共同創辦人加入 Anthropic（Business Insider 單一來源），人才流動商業影響面同步記入 [[topics/ai-talent-flow]]
- [[entities/pricing]]／[[topics/anthropic-business]] — 2026-07-13：Anthropic 證實 1660 萬美元帳務錯誤，稽核發現企業客戶被多收 170 萬美元；[[topics/competitor-landscape]] 新增 Cursor 對手產品「Sand」、Nadella 隱晦批評模型蒸餾、TCS 前線部署工程師團隊；LTM 與 Anthropic 建立企業合作
- [[entities/fable-5]] — 2026-07-13：Fable 5／週配額促銷延長至 7/19 一事多家媒體（Forbes×2、Help Net Security、Economic Times）重複確認，無新細節
- [[entities/claude-code]] — 2026-07-13：已知問題新增 6 條（#5826 MCP OAuth 2.1 無法連線 Desktop 66 留言本日最高互動、#38993 Cowork virtiofs 過期檔案 44 留言、#5706 MCP token 刷新缺失、#28077 CLI TUI 無法捲動回看、#29006 Desktop App 遠端控制請求、#28322 `/remote-control` 未被識別）；內建瀏覽器與 Cowork 行動/網頁版報導核對後確認為既有事件重複來源，未加熱度
- [[topics/code-quality-decline]]／[[topics/community-tech-discussions]] — 2026-07-13：額度焦慮系列新節點（Max 5x 用戶回報消耗速度變快，延燒天數達 17 天）
- [[topics/anthropic-government-policy]] — 2026-07-13：中國「複製」Anthropic/OpenAI 前沿技術、威脅美國國安報導（NY Post），記入攻防紀錄表
- [[topics/anthropic-business]] — 2026-07-12（本機補跑，GH Actions 抓料成功但當日雲端 routine 未產出，詳見 log）：內建瀏覽器第二媒體來源證實互動能力細節（熱度🔥→🔥🔥）；Fable 5 免費期限＋週配額 +50% 促銷統一延長至 7/19（因 GPT-5.6 Sol 被視為同級競品）；已知問題新增 4 條（#36168 bypass-permissions 於 v2.1.77 後全面失效、#20696 網頁/行動版對話壓縮偶發卡死、#60334 圖片處理 API 錯誤耗用額度、#1785 MCP Sampling 功能請求）；[[topics/community-tech-discussions]] 新增 token overhead 實測討論（Claude Code 33k vs OpenCode 7k）；[[topics/community-tech-patterns]] 新增 5 條 dev.to 第一手實作
- **2026-07-12 週度延伸回顧**：新建 [[topics/safety-china-trust-dispute]]（中美 AI 工具信任對峙，自 ai-agent-safety / government-policy 拆出並收斂重複敘事）；[[topics/anthropic-business]] 加開「IPO 前瞻與估值追蹤」子區塊（Series H→$1.2兆次級估值→3Q26 首度獲利曝光→護城河疑慮鏈條）；[[topics/code-quality-decline]]／[[topics/community-tech-discussions]] 額度異常訊號群數字更新（#38335 達 791 留言、cache 命中率降 20% 機制）、額度焦慮熱度 🔥🔥→🔥🔥🔥；[[entities/claude-code]] 已知問題新增「👤 帳號管理」分組（Mobile/Desktop/Web 多帳號切換三 issue 整併）詳見 [[log]]
- **2026-07-11 週度 Lint（雲端排程）**：修正 3 處跨頁矛盾（opus-4-8 Fable 5 fallback 過期敘述、code-quality-decline/claude-code Stop hooks 狀態不一致、CC-Canary 首次出現日期）；補 2 處孤立連結（bernanke、claude-tag）；11 頁呈現品質修復（delta-first 改寫、凍結指標標註、現況時序侵蝕清理等）；`community-tech-tools.md` 新增 4 工具／汰除 5 筆過期；ref 覆蓋率 100%；讀者模擬 3/3 通過；留 4 項待使用者確認（新實體候選 Reflect with Claude、patterns 合併建議、規則年齡審查、來源健康排查）詳見 [[log]]
- [[entities/bernanke]] — 2026-07-10：**新頁面**，前聯準會主席 Ben Bernanke 加入 Anthropic 長期利益信託（Long-Term Benefit Trust）董事會，Reuters/CNBC/Bloomberg 同步報導，HN 66 分討論其對治理公信力的意義
- [[topics/ai-agent-safety]]／[[topics/anthropic-government-policy]] — 2026-07-10：**中國「後門」指控延燒第三天，Anthropic 首次公開否認**（UC Today/BankInfoSecurity/TechRadar/TechRepublic/Fox Business/CISO Series 多家媒體）；同日 Anthropic 發布「Inviting hard questions」聲明，關聯待查證；dev.to 出現第二則獨立 steganography 隱藏標記指控（adioof），與既有 07-01 同形字符事件關聯待釐清
- [[entities/claude-code]]／[[feature-radar]] — 2026-07-10：**v2.1.206** 發布（`/cd` 目錄路徑建議、`/doctor` CLAUDE.md 精簡檢查，feature-radar 新條目）；已知問題新增 8 條（#16157 Max 額度瞬間觸頂 1479 留言最高互動、#34820 visualize DNS 故障、#73365 Fable 5 advisor unavailable、#15942 VS 2026 整合、#30154 Desktop 多視窗、#49322 Opus 4.7 思考摘要未渲染、#8451 VSCode ide_selection 錯誤等）；AGENTS.md（#6235）反應數更新至 5634 讚；Reflect with Claude 熱度升至 🔥🔥🔥🔥（Axios/Verge 二度跟進）
- [[topics/anthropic-business]]／[[topics/competitor-landscape]]／[[entities/pricing]] — 2026-07-10：UST 與 Anthropic 合作導入實體製造業（2 萬工程師受訓）；OpenAI 推出 ChatGPT Work / GPT-5.6 對標 Anthropic；Cursor 開發 AI Agent 對抗 Claude Cowork；Microsoft 部分產品改用自研 AI 取代 OpenAI/Anthropic；Meta 跨入 AI coding 市場；Anthropic/OpenAI/SpaceX 估值超越 25 年科技業退場交易總和；Musk 稱 Anthropic 為業界「leader」
- [[entities/fable-5]] — 2026-07-10：新增已知問題 #73365 Fable 5 advisor 全 session unavailable（🔴 未修復，Claude Code 呼叫層失效，已與 claude-code.md 互相 wikilink）
- [[topics/community-tech-patterns]]／[[topics/community-tech-discussions]] — 2026-07-10：dev.to 三篇第一手實作收錄（context window 診斷法、對抗式 plan-review-loop、本地 reverse proxy 攔截請求）；HN Show HN 兩則達門檻收錄（Devthropology GitHub 分析工具 34 分、AI 思考表徵編輯器 31 分，源自 Anthropic 可解釋性論文）；Bernanke 任命引發 HN 討論收入 discussions（🔥🔥🔥）
- [[feature-radar]]／[[entities/claude-code]] — 2026-07-09：**Anthropic 推出「Reflect with Claude」測試版**（Settings 使用模式儀表板，TechCrunch/Mashable/CNET/Axios/The Verge 同步報導，feature-radar 新條目 🔥🔥🔥）；AGENTS.md 請求（#6235）反應數更新至 5627 讚；已知問題新增/更新多條（Console scrolling #826、Screen Flickering #769/#1913、Buddy 請願 #45596、多帳號 Connector #27302、Stream idle timeout #46987、Max 5x 帳號停用 #5088）
- [[topics/ai-agent-safety]]／[[topics/anthropic-government-policy]] — 2026-07-09：中國「後門」指控延燒第二天（WSJ/Fox Business/TechRadar/Yahoo Tech），TechRadar 首見「建議解除安裝」具體行動呼籲；三方仍未正式回應，獨立頁建頁門檻暫未達；Anthropic 研究部落格發布 dual-use knowledge「關閉開關」機制說明
- [[topics/anthropic-business]]／[[entities/pricing]]／[[topics/competitor-landscape]] — 2026-07-09：Anthropic 次級市場估值傳飆升至 1.2 兆美元（幾乎無人願售）；Anthropic/OpenAI/SpaceX 市值超越 25 年科技業退場交易總和；TeraWulf 尋求 35 億美元融資續建資料中心；Meta 跨入 AI 程式輔助工具市場；AWS 集中管理 Claude 存取/支出/治理；Max 額度異常（#38335）與 INR 定價需求（#17432）反應數更新
- [[entities/sonnet-5]]／[[entities/fable-5]]／[[topics/model-comparison]] — 2026-07-09：Sonnet 5 媒體重複報導評測/定價傳聞（57分、API 減半，定價面留給 pricing.md）；Fable 5 官方 orchestrator 基準（46% 成本達 96% 效能）補入 model-comparison 對照表
- [[topics/ai-agent-safety]]／[[topics/anthropic-government-policy]] — 2026-07-08：**中國官方層級首度指控 Claude Code「後門」**——工業主管機關發布資安警示，稱其秘密追蹤使用者並回傳資料至遠端伺服器；Reuters/WSJ/CNBC/CBS/Cybernews/China Daily 等 8+ 家媒體同步報導（多標明為「中方說法」）；與 Anthropic 07-07「內部實驗」定調時隔一日、框架正面矛盾，Anthropic 尚未正面回應
- [[entities/claude-code]]／[[feature-radar]] — 2026-07-08：**Claude Cowork 擴展至行動/網頁版**（雲端持續執行、闔上裝置不中斷、涵蓋政府客戶，首波限 Max，🔥🔥🔥🔥 feature-radar 新條目）；v2.1.204 修復 headless SessionStart hook 串流（純 bug fix）；已知問題新增 4 條（#32479 GitHub Connector、#59033 [object Object]、#24798 inter-session 溝通、#8660 VSCode edit preview）
- [[entities/pricing]]／[[entities/fable-5]] — 2026-07-08：**Fable 5 免費期限再延 5 天至 7/12**（原 7/7）；feature-radar「⏰ 倒數中」新增 7/12 到期列；Max 額度異常快速耗盡/token 3-5x（#38335 790 留言、#41506）記入 pricing 配額異常
- [[topics/anthropic-business]]／[[topics/competitor-landscape]] — 2026-07-08：**Microsoft 傳以自研模型取代部分產品中 OpenAI/Anthropic 模型**（SiliconANGLE/Bloomberg，呼應退出風險）；Anthropic 3Q26 獲利 >10 億美元（SemiAnalysis，IPO 前瞻）；Perplexity 傳低調開發 AI 編碼工具對打 Cursor/Claude Code；曼哈頓據點擴張
- [[topics/community-tech-patterns]]／[[topics/community-tech-discussions]] — 2026-07-08：Shellular（手機遠端操作本機 Claude Code/Codex，HN 32）補入「行動裝置遠端控制」模式類（呼應 Cowork 行動化官方趨勢）；Geosql 地理空間 skill 宣稱 4 倍改善數據被質疑（HN 55，正反交鋒）

- [[topics/ai-agent-safety]]／[[topics/anthropic-commitments]] — 2026-07-07：**「隱藏追蹤器」事件轉折**——Anthropic 定調先前被指控的 hidden tracker 為內部「實驗」、非惡意（Malwarebytes/Axios/The Neuron）；commitments spyware 回應狀態 ❓→🟡（官方單方說法，社群接受度待觀察）
- [[topics/enterprise-tool-tracker]]／[[topics/anthropic-government-policy]] — 2026-07-07：Alibaba 禁令三媒體（PYMNTS/Benzinga/BeInCrypto）再確認，補「**改用內部工具 Qoder**」細節（生效日 07-10）
- [[topics/enterprise-tool-tracker]] — 2026-07-07：新增 **Alberta 省政府**（加拿大）具名採用——2025 起用 Claude Code、20 小時掃 4.66 億行程式碼完成資安審查
- [[entities/claude-code]]／[[feature-radar]] — 2026-07-07：**v2.1.202** `/config` 新增「Dynamic workflow size」設定（🔥🔥，feature-radar 新條目）；已知問題新增 3 條（終端機複製縮排 #18170、每輪工具呼叫限制回歸 #33969、Cowork 缺 RTL #38005）
- [[topics/competitor-landscape]] — 2026-07-07：CNBC 中國本土模型成本驅動採用上升；DeepSeek 推開源 agent 工具「Deep Code」對標 Claude Code
- [[entities/teresa-carlson]] — 2026-07-07：**新頁面**，前 Microsoft/AWS 高管加入 Anthropic 主導公部門業務（待核實）
- [[entities/pricing]] — 2026-07-07：印度 INR 定價需求互動數更新（594 反應/205 留言，仍無官方回應）

- [[topics/anthropic-business]] — 2026-07-06：**TeraWulf 簽署 190 億美元、20 年期肯塔基資料中心租約**（WSJ/CNBC/Barron's 等 6+ 家財經媒體同步報導，TeraWulf 股價當日漲約 17%，IREN 盤後漲 5% 聯想）；Samsung 客製晶片洽談、Google Workspace 受治理 workflow agent 整合、小型企業轉單 Salesforce 跟進
- [[topics/anthropic-government-policy]]／[[topics/ai-agent-safety]] — 2026-07-06：Alibaba 禁用 Claude Code 經 qz.com/TechRadar/SDxCentral/digitimes 多媒體確認為正式禁令；同日 Meta 亦被報導限制工程師使用 Claude，企業安全審查似擴散；「中美 AI 工具信任對峙」獨立頁評估——三方仍未就「後門」正式回應，未達建頁門檻
- [[topics/enterprise-tool-tracker]] — 2026-07-06：新增 Meta 限用列（❓未確認，缺來源連結細節待補）
- [[entities/claude-code]] — 2026-07-06：已知問題新增 7 則高互動 GitHub Issue——120GB+ 記憶體洩漏 OOM（#4953）、macOS ECONNRESET（#5674）、Linux CRLF 換行（#2805）、Windows 主控台閃爍（#14828）、OneDrive/mapped drive 對話歷史遺失（#14088）、session 額度接續（#13354）、Mobile 多帳號切換（#36151）；AskUserQuestion 60s 逾時（#73125，391 讚）等三則累積數更新
- [[topics/competitor-landscape]] — 2026-07-06：Z.ai 免費 ZCode 對標 Cursor/Claude Code、Base 44（base-1）vs Anthropic 建站速度實測、FT 分析 OpenAI/Anthropic 上市結構性挑戰
- [[topics/community-tech-discussions]] — 2026-07-06：HN 97 分「Anthropic 好感度流失」文（API 穩定性 + vendor lock-in 批評，🔥🔥🔥）；額度焦慮系列跨 9 天合併升級為 🌊延燒
- [[topics/community-tech-patterns]] — 2026-07-06：CaveMan skill（token 70→20）補入穴居人模式；平行 Agent 即時對話地圖（live-log-viewer-next，⏳）補入 Agent 規模化列
- [[topics/official-community-gap]] — 2026-07-06：產品化矩陣新增「多平行 agent 即時可觀測性／協調地圖」列（❌ 無官方對應；Agent View 僅列表式非 live map）
- [[entities/fable-5]] — 2026-07-06：Anthropic 多模型一度大規模錯誤 Fable 5 一併受影響（同日解決）；Show HN Python-on-SNES 作為 Fable 實測案例（解封後 90 分鐘修復 23 個編譯器 bug）
- [[entities/dario-amodei]] — 2026-07-06：接受 STAT 專訪談 AI 對生技產業影響（事件層級記錄，待核實）

- [[entities/claude-code]] — 2026-07-05：已知問題新增 Advisor 觸發時 API 無回應（❓待查證）、model behavior 三種模式回報（❓待查證）、Focus reporting escape sequences 洩漏輸入框、帳號限制申訴表單迴圈、MCP/hooks/plugins 設定需重啟才生效；AGENTS.md 不支援（#6235）累積達 5598 讚為全站已知問題之最；Max 額度異常耗盡（#38335）累積 793 留言持續居冠
- [[topics/enterprise-tool-tracker]] — 2026-07-05：Alibaba 禁令生效日確認為 **2026-07-10**（The Indian Express 跟進報導）
- [[topics/anthropic-business]] — 2026-07-05：AFR 報導 Anthropic 計畫採購 1.4GW 澳洲資料中心容量；MixRoute 宣布支援 Fable 5（生態邊緣整合）
- [[topics/community-tech-discussions]] — 2026-07-05：新增 Microsoft Fast Context 下架爭議討論（本地 LLM 分流節省 context 機制）、Anthropic 疑似 prompt injection 單方指控（待查證）
- [[topics/official-community-gap]] — 2026-07-05：AGENTS.md 矩陣列同步最新反應數（5598 讚）

- [[entities/claude-code]] — 2026-07-04：已知問題新增額度顯示 84% 卻觸發 limit、Windows Desktop relaunch 失敗（orphaned process file lock）、Cowork virtiofs FUSE 過期檔案、Cowork tab 消失（v1.2581.0）；多帳號管理／Linux build／WSL／Skills 同步等長期功能請求聚集，反映社群對平台相容性期待
- [[topics/enterprise-tool-tracker]] — 2026-07-04：Alibaba 禁用 Claude Code 事件經 TechCrunch 等多方媒體跟進報導，確認日期更新
- [[entities/pricing]] — 2026-07-04：新增 Claude Enterprise 支出控管（Spend Controls）功能，因應企業 Agentic AI 帳單超支問題
- [[topics/enterprise-cost-management]] — 2026-07-04：企業層級成本工具缺口更新，同步 Spend Controls 功能上線
- [[topics/anthropic-business]] — 2026-07-04：Anthropic-Samsung 客製晶片洽談獲 upi.com 跟進報導（仍維持初步報導標記）；企業支出控管功能戰略合作記錄
- [[topics/code-quality-decline]] — 2026-07-04：新增 plan mode 逾時自動代答、整體回應變慢投訴延續事件
- [[topics/community-tech-discussions]] — 2026-07-04：AskUserQuestion 60 秒逾時討論補充延續說明

- **2026-07-04 週度 Lint**：修正 3 處跨頁矛盾（Mythos 5 存取狀態、Rubrik 企業命名不一致、封鎖期天數殘留舊值、Dario Amodei 現況過期敘述）；`community-tech-tools.md` 汰除 25 筆過期 ⏳ 工具、新增額度監控類 2 工具（LimitBar、claude-needs-input）；`community-tech-patterns.md` 修正「200k context」過時描述（已被 Sonnet 5 1M context 取代）；`overview.md` 全文改寫反映信任危機（embedded spyware 指控 + Alibaba 禁用）
- [[topics/enterprise-tool-tracker]] — 2026-07-03：**Alibaba 禁用 Claude Code**（疑似後門風險，Reuters 報導，多媒體跟進），新增退出列
- [[topics/anthropic-government-policy]] — 2026-07-03：出口管制解除媒體確認「19 天封鎖期」；FT 報導 Anthropic 封堵中國企業間接存取漏洞（新支線）
- [[topics/ai-agent-safety]] — 2026-07-03：Alibaba「後門風險」指控（HN 313，單方指控待查證）
- [[entities/claude-code]] — 2026-07-03：v2.1.201（Sonnet 5 不再用 mid-conversation system role 傳遞 harness reminders）；已知問題新增 AskUserQuestion 60s 逾時、v2.1.1 token 暴增
- [[topics/community-tech-discussions]] — 2026-07-03：AskUserQuestion 討論升級 🌊延燒；Ask HN prompt-response 迴圈反思（HN 129）；Reddit 額度焦慮集中出現（🔥🔥）
- [[topics/community-tech-patterns]] — 2026-07-03：額度監控模式（⏳：CCLimitPing / LimitBar）
- [[topics/anthropic-business]] — 2026-07-03：The Verge 藥物開發跟進、大廠員工進駐客戶辦公室模式
- [[entities/pricing]] — 2026-07-03：印度盧比（INR）定價需求註記（GitHub Issue 👍584，無官方回應）
- [[topics/anthropic-commitments]] — 2026-07-03：**新頁面**，承諾兌現追蹤：「Anthropic 說過要做的事做了嗎」——5 條追蹤中（隱寫術修復 🔴、解禁三承諾 🟡 等）
- [[feature-radar]] — 2026-07-03：新增「⏰ 倒數中」區塊（7/7 Fable 5 計費轉換、8/31 Sonnet 5 促銷結束）；最新版本行更新 v2.1.201
- [[topics/model-comparison]] — 2026-07-02：**新頁面**，模型選型對照：快速選型表 + 情境推薦 +（我該用哪個模型的單一入口）
- [[entities/fable-5]] — 2026-07-02：redeploy 隨附「Defense in Depth」新安全分類器，高風險 coding 請求 fallback 至 Opus 4.8；首日已有誤判負面實測
- [[entities/sonnet-5]] — 2026-07-02：官方對比圖表修改爭議（HN 討論可信度）+ 社群反映對 Sonnet 4.6 個性流失的主觀回饋
- [[topics/ai-agent-safety]] — 2026-07-02：中國代理偵測爭議升級為「embedded spyware」指控（版本號 2.1.91、混淆手法、system prompt 隱藏機制細節），社群單方指控待查證
- [[topics/anthropic-government-policy]] — 2026-07-02：Fable 5「Defense in Depth」機制作為出口管制解除後承諾的首次具體落實
- [[topics/anthropic-business]] — 2026-07-02：Anthropic-Samsung 客製晶片洽談（初步報導）、Blackstone 基金強勁月表現（初步報導）
- [[topics/competitor-landscape]] — 2026-07-02：Palantir CEO Karp 公開批評 Anthropic/OpenAI「竊取客戶 IP」，分析師調升 Palantir 評等
- [[entities/pricing]] — 2026-07-02：Max 方案升級誤扣費/客服退款爭議案例
- [[topics/community-tech-discussions]] — 2026-07-02：VS Code 使用率下降、AskUserQuestion 60 秒逾時、390M tokens 紀錄、thinking 停頓分心等中熱度討論
- [[topics/community-tech-patterns]] — 2026-07-02：氛圍狀態燈（hooks 驅動實體 LED 燈號提示 agent 狀態）新模式

### 2026-07-01
- [[entities/sonnet-5]]：**新頁面**，Claude Code v2.1.197 預設模型，1M context，$2/$10 per Mtok 促銷
- [[entities/claude-science]]：**新頁面**，科學家專用 AI 工作台正式發布
- [[entities/fable-5]]：**出口管制全面解除**，Pro/Max/Team 7/7 前 50% 配額，旗艦模型回歸
- [[entities/mythos]]：出口管制解除，全球恢復存取
- [[topics/anthropic-government-policy]]：Fable 5 / Mythos 5 出口管制全面解除，Anthropic 承諾三項義務（安全偵測/標準制定/惡意通報）
- [[topics/ai-agent-safety]]：Claude Code 隱寫術爭議（HN 2263，同形字符替換，Anthropic 承諾修復）+ CVE-2026-55407 DoS 漏洞
- [[entities/claude-code]]：v2.1.197 Sonnet 5 正式預設，SDK v0.115.0
- [[entities/pricing]]：Sonnet 5 促銷 $2/$10/Mtok（至 8/31）、Fable 5 7/7 後 usage-based billing
- [[topics/anthropic-business]]：Enterprise Gateway、Fable 5 正式協議、Amazon/Broadcom 資本市場連動
- [[feature-radar]]：新增 Sonnet 5（🔥🔥🔥🔥🔥）、Claude Science（🔥🔥）、Fable 5 解禁

---

## 概覽

- [[overview]] — 當前 Claude / Anthropic 生態系整體局勢（每週更新）
- [[feature-radar]] — 新功能熱度追蹤、試用推薦與快速上手（每次 ingest 更新）
- [[feature-radar-archive-2026-05]] — 2026-05 功能詳細條目封存

---

## Entities（實體頁）

| 頁面 | 類型 | 領域 | 狀態 | 摘要 |
|------|------|------|------|------|
| [[entities/sonnet-5]] | model | 🤖 模型 | active | Claude Sonnet 5：Claude Code v2.1.197 預設模型，1M context，$2/$10 per Mtok 促銷至 8/31，agentic 效能接近 Opus 4.8 |
| [[entities/claude-science]] | product | 🛠️ 工具/功能 | active | Claude Science：科學家專用 AI 工作台，整合研究工具套件、可稽核 artifact、彈性運算資源；Anthropic 宣布自行開發藥物 |
| [[entities/claude-code]] | product | 🛠️ 工具/功能 | active | Claude Code CLI 主頁：功能、已知問題、社群工具 |
| [[entities/opus-4-8]] | model | 🤖 模型 | active | Opus 4.8：SWE-bench Pro 69.2%、1M context、Dynamic Workflows（1,000 子代理）、Fast Mode 1/3 費用 |
| [[entities/opus-4-7]] | model | 🤖 模型 | active（已被取代）| Opus 4.7 發布細節、思考深度爭議、cache 問題 |
| [[entities/pricing]] | policy | 💼 商業 | active | 訂閱方案、近期政策變動、token 成本注意事項；未滿足需求：印度 INR 在地化定價（👍584，無官方回應） |
| [[entities/mythos]] | model | 🤖 模型 | active（已解禁） | 高能力安全模型；2026-07-01 出口管制解除，全球恢復存取；僅限授權機構/安全研究用途，非一般消費市場 |
| [[entities/bugcrawl]] | feature | 🛠️ 工具/功能 | beta | Anthropic 測試中的 Claude Code 漏洞偵測工具 |
| [[entities/claude-design]] | feature | 🛠️ 工具/功能 | active（初期）| Anthropic AI 設計工具，首日社群反映幻覺多、風格偏移、Claude Code 整合差 |
| [[entities/claude-security]] | product | 🛠️ 工具/功能 | beta | Claude Security 資安產品，情境化安全評估，整合於 Claude Code 開發環境 |
| [[entities/openclaw]] | product | 🛠️ 工具/功能 | active | 第三方 agentic 工具，歷經禁令後 6/15 起恢復允許但改走信用池 API 費率計費 |
| [[entities/google-investment]] | event | 💼 商業 | resolved | Google 投資 400 億美元歷史記錄，含循環算力交易結構 |
| [[entities/managed-agents]] | feature | 🛠️ 工具/功能 | active（正式發布）| Managed Agents 官方框架：Dreaming 記憶整合、20 路並行子代理、Outcomes 規格驗證 |
| [[entities/bernanke]] | person | 👤 人物 | active | 前聯準會主席，2026-07-09 加入 Anthropic 長期利益信託（Long-Term Benefit Trust）董事會 |
| [[entities/boris-cherny]] | person | 👤 人物 | active | Claude Code 創始人，「Loops 是未來」設計哲學、「coding is solved」論戰、第三方工具邊界聲明 |
| [[entities/chris-ciauri]] | person | 👤 人物 | active | Anthropic 國際業務總監；首爾記者會宣布 Fable 5 / Mythos 解禁信心（2026-06-18）|
| [[entities/john-jumper]] | person | 👤 人物 | active | 諾貝爾化學獎得主（AlphaFold），2026-06-19 離開 Google DeepMind 加入 Anthropic（Reuters 確認）|
| [[entities/cat-wu]] | person | 👤 人物 | active | Claude Code 產品負責人，「AI 下一步是主動性（proactivity）」論述 |
| [[entities/andrej-karpathy]] | person | 👤 人物 | active（待核實）| 近期加入 Anthropic，CLAUDE.md 四條規則、「最小必要 context」費用控管原則 |
| [[entities/fiona-fung]] | person | 👤 人物 | active | Anthropic 工程副總裁；「Claude Code 讓工程師更孤獨；coding 不再是瓶頸」論述（2026-06-22） |
| [[entities/tom-brown]] | person | 👤 人物 | active | Anthropic 聯合創辦人（GPT-3 共同作者）；2026-06-25 接管 Fable 5 出口管制與白宮談判 |
| [[entities/dario-amodei]] | person | 👤 人物 | active | Anthropic CEO：政府監管立場、企業文化論述、Code with Claude 大會現場宣布速率政策 |
| [[entities/teresa-carlson]] | person | 👤 人物 | active（待核實）| 前 Microsoft、AWS 高管；2026-07-07 加入 Anthropic 主導公部門（public sector）業務（FedScoop）|
| [[entities/chris-olah]] | person | 👤 人物 | active | Anthropic 共同創辦人、AI 可解釋性研究先驅；2026-05-26 梵蒂岡封論揭幕演講 |
| [[entities/opencode]] | product | 🛠️ 工具/功能 | active（快速成長）| Claude Code 主要開源替代品，157K 開發者分流，OpenCode-power-pack 移植官方 11 個 skills |
| [[entities/claude-tag]] | feature | 🛠️ 工具/功能 | active | Claude Tag：Slack-native AI 協作工具，可讀取頻道上下文、跨 session 記憶、主動完成任務；Anthropic 內部 65% 程式碼由其生成 |
| [[entities/fable-5]] | model | 🤖 模型 | active（已解禁）| Claude Fable 5：首款 Mythos 級公開模型，$10/$50 per M token；7/1 解禁，Pro/Max/Team 7/7 前享 50% 配額，7/7 後 usage-based billing |
| [[entities/tom-blomfield]] | person | 👤 人物 | active（待核實）| 前 Monzo 共同創辦人，2026-07-13 加入 Anthropic（Business Insider 單一來源，AI compute／Y Combinator 背景）|
| [[entities/claude-for-teachers]] | product | 🛠️ 工具/功能 | active | Anthropic 面向美國通過認證 K-12 教師的免費方案，開放進階 Claude 功能與教學技能庫，對接全美 50 州學術標準 |

---

## Topics（進行中議題）

> Topics 頁面本身無「類型」欄位，故表格僅三欄（領域 / 狀態 / 摘要），為刻意設計差異（Entities 四欄含類型）。

| 頁面 | 領域 | 狀態 | 摘要 |
|------|------|------|------|
| [[topics/model-comparison]] | 🤖 模型 | ongoing | 模型選型對照：「我該用哪個模型」單一入口——快速選型表、情境推薦、benchmark 對照（陣容變化時同步更新） |
| [[topics/anthropic-commitments]] | 🏛️ 政策/安全 | ongoing | 承諾兌現追蹤：「Anthropic 說過要做的事做了嗎」——官方承諾/拒絕建檔，狀態變化時由每日 ingest 更新 |
| [[topics/code-quality-decline]] | 🛠️ 工具/功能 | monitoring | Claude Code 效能退步事件，Anthropic 已承認工程疏失 |
| [[topics/competitor-landscape]] | 💼 商業 | monitoring | Google 祕密開發競品 + OpenCode 157K 分流 + DeepSeek clone 低成本替代生態 |
| [[topics/community-tech-tools]] | 🌐 社群 | ongoing | 社群工具目錄：189 工具的活躍度、採用狀態追蹤 |
| [[topics/community-tech-patterns]] | 🌐 社群 | monitoring | 社群實戰模式庫（日更）：multi-agent、skills 設計、工作流最佳實踐的可複用做法 |
| [[topics/community-pattern-trends]] | 🌐 社群 | ongoing | 社群趨勢觀察（週更）：從模式庫萃取的宏觀層——5 條成形趨勢的熱度曲線 + 對現有設計的啟示 |
| [[topics/community-tech-discussions]] | 🌐 社群 | ongoing | 社群技術討論趨勢：設計哲學辯論、實證研究、架構反思（HTML vs MD、Skill Atrophy 等） |
| [[topics/safety-china-trust-dispute]] | 🏛️ 政策/安全 | ongoing | 中美 AI 工具信任對峙：中國代理偵測程式碼/隱寫術指控 → Alibaba/Meta 禁用 → 中國官方「後門」警示 vs Anthropic 07-10 首度公開否認（2026-07-12 自 ai-agent-safety / government-policy 拆出）|
| [[topics/ai-agent-safety]] | 🏛️ 政策/安全 | ongoing | AI agent 安全：GitHub Repo prompt injection 多媒體確認 + 假冒安裝包 + CVE/DoS 漏洞（中國信任對峙已分流至 [[topics/safety-china-trust-dispute]]）|
| [[topics/ai-agent-safety-archive]] | 🏛️ 政策/安全 | monitoring | AI Agent 安全時序歷史存檔（2026-05-22 以前）；主頁 [[topics/ai-agent-safety]] 瘦身分流 |
| [[topics/anthropic-government-policy]] | 🏛️ 政策/安全 | monitoring | Anthropic 政府政策攻防：出口管制主線已於 2026-07-01 解除，剩餘承諾落實、歐洲據點爭奪、Legion 訴訟等衍生支線持續觀察（中國信任對峙已分流至 [[topics/safety-china-trust-dispute]]）|
| [[topics/official-community-gap]] | 🛠️ 工具/功能 | monitoring | 官方功能 vs 社群痛點缺口矩陣：哪些痛點官方正在解決、哪些結構性缺席 |
| [[topics/enterprise-cost-management]] | 💼 商業 | monitoring | 企業規模採用 Claude 的成本結構挑戰：Uber/Microsoft 案例、缺失工具、因應策略 |
| [[topics/enterprise-tool-tracker]] | 💼 商業 | ongoing | 大型企業 AI 編碼工具使用追蹤：Microsoft/Amazon/Uber/Apple 等企業當前工具選擇與變化軌跡；07-03 Alibaba 以疑似後門風險禁用 Claude Code（❌ 退出） |
| [[topics/community-tech-timeline]] | 🌐 社群 | monitoring | 社群技術應用趨勢完整時序（2026-04-25 至今），從 community-tech-patterns 拆分 |
| [[topics/anthropic-business]] | 💼 商業 | ongoing | Anthropic 商業健康度：企業採用率 34.4%、17 倍訂閱補貼、PMF 觀察、Microsoft 退出風險；07-03 藥物開發野心（The Verge）、大廠員工進駐客戶模式 |
| [[topics/recursive-self-improvement]] | 🏛️ 政策/安全 | monitoring | AI 遞歸自我改進與全球暫停呼籲：Claude 已寫 80-90% Anthropic 程式碼、工程師代碼產出 8×、全球 AI 煞車踏板呼籲（2026-06-22 後無新進展，轉低頻觀察）|
| [[topics/ai-talent-flow]] | 💼 商業 | ongoing | AI 實驗室人才流動與對各公司影響：DeepMind 淨流失（Jumper/Adler/Pritzel）、Anthropic 主要承接、OpenAI 次要承接 |
