---
page: "topics/model-task-leaderboard"
kind: "topic"
status: "ongoing"
domain: "🤖 模型"
last_updated: "2026-09-03"
last_news_update: "2026-08-05"
update_freq: "🗓️ 週更（每週抓取一次外部榜單快照；更新日期停留數天屬正常節奏）"
status_main: "ongoing"
days_since_news: 31
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 31
inbound_links: 5
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 任務 × 跨家模型領先者週快照

**狀態：** ongoing
**領域：** 🤖 模型
**更新頻率：** 🗓️ 週更（每週抓取一次外部榜單快照；更新日期停留數天屬正常節奏）
**開始日期：** 2026-08-05
**最後更新：** 2026-09-03
**最後新聞更新：** 2026-08-05

> **本週快照重點**（2026-09-03）
> 18 榜取得 16 榜，整表覆寫：WebDev Arena 恢復取得（Opus 5 登頂）、圖像編輯與 TTS 第二／三名換人、MTEB 首位換為 QZhou-Embedding（僅首位可確認）。Search Arena **連續 2 週無法取得**，列入汰換候選；SWE-bench 與 OpenRouter 兩榜的二手來源彼此歧異，本頁保留兩說並註明，不擇一。

---

## 摘要

回答「**做某類任務，目前哪家模型最強？**」——按任務類型列出各活榜單的本週領先者快照，涵蓋跨家模型（OpenAI、Google、開源等）與非文字生成（畫圖、影片、語音）。每列標資料日期；即時精確數字請點榜單連結（活榜單永遠最新，本頁只是每週速讀），各榜怎麼算分見下方評比方式索引。Claude 家內選型見 [[topics/model-comparison]]。

## 本週快照

| 你想做的任務 | 本週前三名 | 資料日期 | 榜單 |
|---|---|---|---|
| [寫 code（agent 解 issue）](#eval-swebench) | Claude Opus 5 > DeepSeek V4 Pro > Kimi K3（97／96.4／93.4%；二手來源歧異，見註記） | 09-03（二手） | [SWE-bench](https://www.swebench.com/) |
| [寫 code（Aider 實戰）](#eval-aider) | gpt-5 (high) > gpt-5 (medium) > o3-pro（⚠️ 榜停更，連續 5 週） | 2025-08-23 | [Aider Polyglot](https://aider.chat/docs/leaderboards/) |
| [寫文案、聊天、翻譯](#eval-lmarena) | Claude Fable 5 > Claude Opus 4.8 > GPT-5.5 Pro（二手來源彼此不一致，見註記） | 08 月（二手） | [LMArena](https://lmarena.ai/) |
| [查資料（AI 搜尋）](#eval-search) | Claude Opus 4-6 Search > GPT-5.5 Search > Fable 5（連續 2 週無法取得，考慮汰換；沿用） | 07-21 | [Search Arena](https://arena.ai/leaderboard) |
| [做網頁／前端](#eval-webdev) | Claude Opus 5（1691）> Kimi K3（1674）> Grok 4.6（1630） | 08 月（二手） | [WebDev Arena](https://arena.ai/leaderboard) |
| [畫圖（文生圖）](#eval-image) | GPT Image 2 > MAI-Image-2.6-Preview > Reve 2.1 | 未載（09-03 抓取） | [AA 圖像榜](https://artificialanalysis.ai/image/leaderboard/text-to-image) |
| [改圖（圖像編輯）](#eval-imageedit) | MAI-Image-2.6-Preview > GPT Image 2 > Nano Banana 2 | 08 月 | [AA 編輯榜](https://artificialanalysis.ai/image/leaderboard/editing) |
| [生成影片](#eval-video) | Wan 3.0 > Gemini Omni Flash > MiniMax H3 Max（前三 Elo 差距 ≤3，實質並列） | 08 月 | [AA 影片榜](https://artificialanalysis.ai/video/leaderboard/text-to-video) |
| [語音合成（TTS）](#eval-tts) | Sonic 3.6 > Inworld Realtime TTS-2 > Qwen-Audio-3.0-TTS-Plus | 08 月 | [AA TTS 榜](https://artificialanalysis.ai/text-to-speech/leaderboard) |
| [語音轉文字（逐字稿）](#eval-stt) | Fun-Realtime-ASR > Scribe v2 > MAI-Transcribe-1.5 | 未載（09-03 抓取） | [AA STT 榜](https://artificialanalysis.ai/speech-to-text) |
| [電腦操作 agent](#eval-terminal) | Claude Opus 5（42.7%）> GPT-5.6 Sol > Fable 5（TB 3.0；2.1 版排名相反，見註記） | 08-28（二手） | [Terminal-Bench](https://www.tbench.ai/) |
| [文件解析／OCR](#eval-docparse) | MiniMax M3（0.916）> Qwen3.7-Plus > Qwen3.6 Plus | 09-03 | [OmniDocBench](https://llm-stats.com/benchmarks/omnidocbench-1.5) |
| [音樂生成](#eval-music) | Suno V5.5 > Mureka V9 > Mureka V8 | 未載（09-03 抓取） | [AA Music Arena](https://artificialanalysis.ai/music/leaderboard/vocals) |
| [Embedding（自建 RAG）](#eval-mteb) | QZhou-Embedding（75.97；僅首位可確認，二手） | 未載（09-03 二手） | [MTEB](https://huggingface.co/spaces/mteb/leaderboard) |
| [聊天陪伴／情商](#eval-eqbench) | Claude Fable 5 > Kimi K3 > GPT-5.5 | 07-20 | [EQ-Bench](https://eqbench.com/) |
| [放多長的任務給 agent](#eval-metr) | Claude Opus 4.6（14.5 小時@50%）> GPT-5.2（6.6h）> Opus 4.5（4.8h）（⚠️ 現役陣容未入測） | 2026-05（二手） | [METR](https://metr.org/) |
| [讀文件不胡說（幻覺率低）](#eval-vectara) | finix_s1_32b > gpt-5.4-nano > gemini-2.5-flash-lite | 05-11 | [Vectara 幻覺榜](https://github.com/vectara/hallucination-leaderboard) |
| [大家實際在用什麼](#eval-openrouter) | Hermes Agent > DeepSeek V4 Flash > 騰訊 Hy3（09-02 直接抓取；09-03 二手稱 GPT-5.6 Luna 居首，歧異見註記） | 09-02 | [OpenRouter](https://openrouter.ai/rankings) |

## 本週註記（僅列異常）

- **本輪 18 榜取得 16 榜（2026-09-03）**：Search Arena 連續 2 週無法取得（JS 渲染、無二手報導），**已達汰換候選門檻，請使用者裁示**；MTEB 僅能確認首位。
- **SWE-bench 二手來源歧異**：09-02 二手（morphllm）前三為 Opus 5 > Mythos 5 > Fable 5；09-03 二手（llm-stats）為 Opus 5 97% > DeepSeek V4 Pro 96.4% > Kimi K3 93.4%。兩者僅首位一致，可能一為 Verified 一為 Pro，本頁列最新者並保留兩說；榜已飽和（前三差距小於評測雜訊）。
- **OpenRouter 二手與直接抓取歧異**：09-02 直接抓取首位 Hermes Agent（35.7 兆 token）；09-03 二手稱 GPT-5.6 Luna 居首、無具體數字。本頁維持直接抓取結果，下週複抓判定。
- **LMArena 二手來源彼此不一致**：一說 Fable 5 居首、一說 Opus 4.8 居首；整表 07-01 重新基準化後前期排名不可追溯。
- **Terminal-Bench 2.1 與 3.0 排名相反，不可跨版比較**：3.0 Claude Opus 5 42.7% 領先；通用版／2.1 為 GPT-5.6 Sol 65.9%、Fable 5 62.9%。本頁快照列 3.0 並註明版次。
- **Aider Polyglot 停更（連續 5 週）**：直接抓取最新資料日期 2025-08-23。**已達汰換門檻，續請使用者裁示**（改由 SWE-bench Pro 或 Terminal-Bench 3.0 承接「寫 code 實戰」語意）。
- **METR 數據更新但仍不含現役陣容**：二手來源給出 2026-05-08 資料（Opus 4.6 14.5h、GPT-5.2 6.6h、Opus 4.5 4.8h），較先前記錄的 2026-02 新；官方仍附「≥16 小時量測不可信」免責，Opus 5／Fable 5 未入測，數字僅供尺度感。
- **Vectara 幻覺率兩說**：直接抓取 finix_s1_32b 1.8%、二手稱 0.6%，疑為資料集版本差異；本頁採直接抓取。
- **AA 系列多榜未載官方資料日期**：文生圖、STT、音樂等榜為直接抓取但頁面無快照日期，本頁以抓取日標示。

## 評比方式索引（每榜比什麼、分數怎麼來）

查快照表看到「誰贏」後，這裡回答「贏在什麼題目上」。各榜按計分機制分四組。

### 盲測投票組——人類投票，分數是相對的

同一題丟給兩個**匿名**模型，人類看產出投票誰好。多數榜實際用 Bradley-Terry 統計模型（棋類 Elo 的嚴謹版，不會過度加權近期比賽）把幾萬場勝負摺算成分數，再換算成 Elo 風格數字呈現。分數是相對的，**只在同一個榜內可比**。

- <a id="eval-lmarena"></a>**寫文案、聊天（LMArena）**
  - **題目**：真實使用者當下輸入的任何問題——寫 email、潤稿、翻譯、解 bug、閒聊都有，不設題庫。
  - **規模**：累積 680 萬+ 盲測票、360+ 模型，全球最大人類偏好榜。
  - **算分**：兩匿名模型同題作答、投票；Bradley-Terry 摺算成 Elo 風格分數。有 style control（把「寫得長、排版漂亮」的討喜因素統計拆離）與位置／組織偏差修正。
  - **盲點**：仍偏好長回答；測「討喜」不測「正確」。07-12 重新基準化＝Fable 5 解禁後只計 07-01 之後的票。
- <a id="eval-search"></a>**查資料（Search Arena）**
  - **題目**：要上網查的真實需求——「這兩台吸塵器哪台值得買」「這則新聞是真的嗎」「某產業最新市況」這類。
  - **規模**：已公開 2.4 萬筆對話資料。
  - **算分**：盲測投票，比查得準不準、引用對不對；Bradley-Terry。
  - **盲點**：投票者偏好部落格與程式碼來源、引 Wikipedia 反而不討喜——測「使用者滿意」不等於「來源權威」。
- <a id="eval-webdev"></a>**做網頁（WebDev Arena）**
  - **題目**：自由輸入的網頁需求——「做個 landing page」「做個小遊戲」「仿一個 Spotify 介面」；分布約網站設計 15%、遊戲 12%、仿製既有網站 12%。
  - **規模**：累積 8 萬+ 票。
  - **算分**：兩模型各生出**可實際互動**的網頁，試用後投票（可投「兩個都爛」）；Bradley-Terry。
  - **盲點**：「都爛」佔 26%——前端生成整體還不成熟，榜首也只是矮子裡的將軍。
- <a id="eval-image"></a>**畫圖（AA 圖像榜）**
  - **題目**：約 900 條策劃 prompt，按「用途 × 能力」二軸設計——行銷海報、商品圖、遊戲美術、UI 畫面，分別考文字渲染、人體結構、多物件佈局、推理等能力（如「一張含指定標語的活動海報」這類題）。
  - **規模**：累積 4.5 萬+ 票；每月汰換辨別度低的題目防過擬合。
  - **算分**：同題兩張匿名圖並排盲投；Bradley-Terry → Elo。
  - **盲點**：測描述還原度＋大眾審美——榜首是「最多人覺得好」，不等於適合你的風格。
- <a id="eval-imageedit"></a>**改圖（AA 編輯榜）**
  - **題目**：原圖＋修改指令——「移除背景」「改成水彩風」「把紅衣換成藍衣」這類。
  - **規模**：票數未公開。
  - **算分**：同一張原圖同一指令，兩個編輯結果盲投；Elo。
  - **盲點**：與文生圖是獨立的榜、排名不同——「生得好」與「改得好」是兩種能力，選工具分開查。
- <a id="eval-video"></a>**生成影片（AA 影片榜）**
  - **題目**：策劃 prompt 隨機抽題；生成參數統一（1080p、24fps、10 秒、固定 seed）排除設定差異。
  - **規模**：票數未公開；榜每小時更新。另有圖生影片、影片編輯子榜（各分含音訊／無音訊）。
  - **算分**：兩段匿名影片並排盲投（動作合理性、畫面品質）；Bradley-Terry。
  - **盲點**：用預設參數測——各家在最佳化設定下的表現可能不同。
- <a id="eval-tts"></a>**語音合成（AA TTS 榜）**
  - **題目**：約 500 字元的實境情境文本——客服應答、數位助理回覆、知識講解、娛樂旁白。
  - **規模**：每日 4 次隨機時段測試；票數未公開。
  - **算分**：8 個標準聲音＋各家自有聲音分開盲聽投票（防「喜歡某個音色」污染合成品質評估）；Elo。
  - **盲點**：終究是主觀自然度；你的語言／口音場景不一定在題庫內。
- <a id="eval-music"></a>**音樂生成（AA Music Arena）**
  - **題目**：分流派的策劃 prompt——Pop、Hip-Hop、EDM、古典、爵士，另收審核後的使用者投稿題。
  - **規模**：票數未公開；分純樂器與含人聲兩榜，另有流派別排名。
  - **算分**：所有音檔先統一響度到 -16 LUFS 再盲聽投票（防「比較大聲聽起來比較好」）；Bradley-Terry。
  - **盲點**：流派偏好仍會影響投票；≥10 秒片段測不出整曲結構力。

### 任務通過率組——固定題庫，過就得分（%）

有客觀對錯，靠測試或驗收腳本判定，不靠人類感覺。要留意題庫版本——同名 benchmark 的不同子集分數不能互比。

- <a id="eval-swebench"></a>**寫 code（SWE-bench）**
  - **題目**：真實 GitHub 專案的 bug 單／需求單——像「某 API 在特定輸入下回傳錯誤結果」這種真實 issue，附整個 repo 要模型寫出修復 patch。
  - **規模**：**Verified** 500 題（工程師人工確認可解、多數單檔案可解決）；**Pro** 1,865 題、跨 41 個活躍 repo（需跨檔案修改、更長 context）。
  - **算分**：patch 跑該專案的 unit tests 全過才算解決；**Pass@1 一次定生死，無重試**。
  - **盲點**：Verified 頂級模型已 9 成以上接近飽和、Pro 頂級也僅兩三成——看到「SWE-bench XX%」先問是哪個子集。
- <a id="eval-aider"></a>**寫 code（Aider Polyglot）**
  - **題目**：Exercism 程式練習題——實作資料結構、演算法、小工具這類，特挑「連頂級模型都常錯」的難題。
  - **規模**：225 題，C++/Go/Java/JS/Python/Rust 六語言。
  - **算分**：允許兩次嘗試（第一次失敗拿到測試錯誤訊息再改）；必須用結構化編輯格式實際改檔，通過 hidden tests 算對；每題成本一併記錄（同題 o3-pro $146 vs gpt-5 $29 就是這樣量出來的）。
  - **盲點**：疑似停更（見本週註記）；題型偏演算法練習，離真實專案開發有距離。
- <a id="eval-terminal"></a>**電腦操作（Terminal-Bench）**
  - **題目**：真實終端機任務——「編譯這個專案並修好錯誤」「從 log 抽出統計數字」「架好某服務」，跨系統管理、資安、資料科學、模型訓練。
  - **規模**：89 題。
  - **算分**：agent 在沙盒自主操作到完成，驗收腳本檢查產出檔案或執行結果。
  - **盲點**：2.1 版修復 28 題評估問題（依賴失效、資源不足、題意與測試不符），2.0 與 2.1 分數不能直接比。
- <a id="eval-docparse"></a>**文件解析（OmniDocBench）**
  - **題目**：真實 PDF 頁面轉結構化文字——論文、財報、新聞、教科書、手寫筆記都有。
  - **規模**：1,651 頁，10 類文件 × 5 種版型 × 5 種語言。
  - **算分**：分項計分——文字用編輯距離、表格用 TEDS（樹結構比對）、公式用 CDM、閱讀順序用序列比對；綜合分＝（文字＋表格＋公式）三項平均，0–1。
  - **盲點**：綜合分會掩蓋分項強弱——只在乎表格擷取就直接看表格分項。
- <a id="eval-mteb"></a>**Embedding（MTEB）**
  - **題目**：embedding 的各種用法——給查詢找出對的文件（檢索）、判斷兩句話多相似、文本分類與聚類等 8 大類任務。
  - **規模**：英文版 58 個資料集；多語版 500+ 資料集、250+ 語言。
  - **算分**：各任務用各自標準指標（檢索 nDCG@10、分類 accuracy、相似度 Spearman）再彙總排名。
  - **盲點**：彙總方式不同會改變模型排序；v1 與 v2 分數不可互比。

### 錯誤率組——越低越好

- <a id="eval-stt"></a>**語音轉文字（AA STT 榜）**
  - **題目**：三種真實音檔——語音助理對話（50%）、多口音議會錄音（25%）、滿是術語的財報電話會議（25%）。
  - **規模**：共約 8 小時音檔。
  - **算分**：**WER 字錯率＝（替換＋插入＋刪除的詞數）÷ 參考逐字稿總詞數**；另量批次速度（音檔時長 ÷ 處理時間）與串流延遲（首字／定稿時間）。
  - **盲點**：只測這三類英語情境——你的場景（如中文會議逐字稿）不在題庫內。
- <a id="eval-vectara"></a>**幻覺率（Vectara）**
  - **題目**：跨領域文章（法律、醫療、金融…，取自 BBC、CNN、Wikipedia 等，50–24,000 字），要求模型「只根據原文摘要、不得外加知識」。
  - **規模**：7,700+ 篇；題庫刻意不公開（防針對性過擬合）。
  - **算分**：幻覺偵測模型 HHEM 逐篇檢查摘要有無原文沒講的內容；幻覺率＝有幻覺的摘要數 ÷ 總數。
  - **盲點**：測「忠於原文」不是知識全面正確性；小模型可能贏過主流旗艦——選「讀文件／摘要」用途時看此榜比能力榜實用。

### 特殊機制組——不是傳統分數

- <a id="eval-eqbench"></a>**情商（EQ-Bench）**
  - **題目**：120 個各有雷點的虛擬人物——有人重溫暖、有人厭惡虛偽，含刻意刁難場景與權力關係；模型要跟每個人物進行 16 輪對話、建立信任並實際幫上忙。
  - **規模**：120 人物 × 16 輪。
  - **算分**：不同家族的 LLM 分飾人物與評審（防自家互相加分），按六維度打 0–10：建立關係、真誠、感知對方、滿足需求、情緒理解、情緒管理。
  - **盲點**：LLM 評審仍可能有系統性偏好；高情商分數與「討好」難完全切割。
- <a id="eval-metr"></a>**agent 自主時長（METR）**
  - **題目**：HCAST／RE-Bench／SWAA 的真實工程任務——從幾分鐘的小修到數十小時的 ML 實驗（軟體、ML、資安）。
  - **規模**：每題先由人類專家實測耗時；模型每題跑約 8 次取成功率。
  - **算分**：把「人類耗時 vs 模型成功率」擬合成曲線，取**成功率恰好 50% 的交點時長**——單位是分鐘／小時，不是分數；這條「每 7 個月翻倍」的曲線是 AGI 進度討論的核心圖表。
  - **盲點**：量測更新慢（本輪停在 2026-01）；任務偏工程域，不代表其他領域的自主力。
- <a id="eval-openrouter"></a>**實際用量（OpenRouter）**
  - **題目**：沒有題目——這是真實 API 流量統計，不是評測。
  - **規模**：百萬級使用者經 OpenRouter 路由的全部請求。
  - **算分**：token 用量（輸入＋輸出）排名，可切日／週／月窗口；另有「趨勢」排序（近期增量 vs 過去平均）。
  - **盲點**：只計該平台流量、深受價格與延遲影響——測的是**採用**，不是品質；跟能力榜對照著看才有意思。

> 讀榜提醒：所有榜都測不到「跟你的實際工作流合不合」，最終仍以自己的任務實測為準。

## 相關實體

- Claude 家內選型：[[topics/model-comparison]]
- 各模型深度資訊：[[entities/fable-5]] · [[entities/opus-5]] · [[entities/sonnet-5]]
- 競品動態：[[topics/competitor-landscape]]
