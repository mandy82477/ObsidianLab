---
page: "topics/safety-china-trust-dispute"
kind: "topic"
status: "monitoring（核心「後門」敘事自 07-10 雙方首度正面否認後未見新進展，轉低頻觀察；新出現的相關但獨立事件見下方說明）"
domain: "🏛️ 政策/安全"
last_updated: "2026-08-15"
last_news_update: "2026-07-11"
status_main: "monitoring"
days_since_news: 54
inbound_links: 18
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
signal: "⚠️ 高引用但停滯"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 中美 AI 工具信任對峙

**狀態：** monitoring（核心「後門」敘事自 07-10 雙方首度正面否認後未見新進展，轉低頻觀察；新出現的相關但獨立事件見下方說明）
**領域：** 🏛️ 政策/安全
**開始日期：** 2026-06-30
**最後更新：** 2026-08-15
**最後新聞更新：** 2026-07-11

> **最新動態**（2026-07-10，議題轉入低頻觀察）
> 中國「後門」指控延燒第三天，UC Today、BankInfoSecurity、Technology Org、TechRepublic、TechRadar、CISO Series、Fox Business 等多家獨立媒體續報導；**Anthropic 今日首度公開反駁該指控**——為本議題自 06-30 起追蹤以來，官方第一次正面回應「中國官方層級」指控本身（此前 07-07「實驗」定調僅回應社群層級的原始指控，未直接對應中國官方警示的用詞與框架）。同日 Anthropic Blog 另發布「Inviting hard questions」回應外界安全疑慮的立場聲明，兩者關聯（推論，2026-07-10 觀察，已掃日報至 2026-08-14 無後續；官方頁面未查證）。雙方框架仍各執一詞，均無第三方技術驗證。**截至 2026-07-26，本頁核心「後門」敘事線已 16 天無新進展**（中國官方與 Alibaba 均未就 Anthropic 的否認再表態），故狀態轉為 monitoring；07-22 起浮現的 Moonshot AI 蒸餾指控與財政部制裁威脅、07-23 digitimes「Claude Code 外洩內容縮小差距」指控，雖同屬中美 AI 信任/能力落差的廣義敘事，但性質與本頁「Claude Code 後門/隱寫術」主線不同（前者為模型蒸餾與外洩指控，非 Claude Code 產品層機制指控），依主歸屬原則追蹤於 [[topics/anthropic-government-policy]]，本頁不重複收錄。

---

## 摘要

本頁追蹤 2026-06-30 起延燒的「中美 AI 工具信任對峙」：一條由社群逆向工程指控起頭、逐步升級至中國政府正式警示、企業連鎖禁用、最終由 Anthropic 公開否認的敘事線。核心矛盾是**雙方均提出未經第三方驗證的技術指控**——社群/中國官方稱 Claude Code 內建「秘密追蹤中國使用者並回傳資料」的後門機制；Anthropic 先以「內部實驗」淡化，後於 07-10 正式否認中國官方的「後門」框架本身。與此同時，中國企業（Alibaba）與部分美國企業（Meta）分別以資安疑慮為由限制員工使用 Claude／Claude Code，形成技術指控、外交表態與企業行動三線並進的複合事件。

原分別記錄於 [[topics/ai-agent-safety]]（技術面）與 [[topics/anthropic-government-policy]]（外交/政策面）；因敘事已跨越兩頁且形成獨立故事線（社群指控 → 企業禁用 → 官方定調實驗 → 政府層級升級 → 官方首度否認），2026-07-12 週度回顧確認拆出本頁整合單一時序。技術細節的逐項可信度評估、完整媒體來源列表仍以本頁時序為準；[[topics/ai-agent-safety]] 與 [[topics/anthropic-government-policy]] 僅保留與各自主軸直接相關的摘要 + 指標連結。

---

## 敘事五階段

| 階段 | 時間 | 出牌方 | 核心事件 |
|------|------|--------|---------|
| ① 社群指控 | 2026-06-30 ～ 07-02 | 🌐 社群 | Reddit/HN/獨立部落格逆向工程指出 v2.1.91 起嵌入中國代理偵測程式碼，疑似隱形修改 system prompt 並回傳資訊 |
| ② 隱寫術延伸指控 | 2026-07-01（07-10/07-11 二次收錄） | 🌐 社群 | 兩篇獨立作者（thereallo.dev、dev.to/adioof）主張 Claude Code 以 Unicode 同形字符/撇號變體做輸出隱寫標記 |
| ③ 企業禁用 | 2026-07-03 起 | 🌐 企業（Alibaba/Meta） | Alibaba 以「疑似後門風險」禁用 Claude Code（改用內部工具 Qoder），Meta 同期限制工程師使用 Claude |
| ④ 官方定調「實驗」 | 2026-07-07 | 🏢 Anthropic | Anthropic 首度正式回應社群指控，稱「隱藏追蹤器」為內部實驗，非惡意設計 |
| ⑤ 政府層級升級 | 2026-07-08 | 🏛️ 中國官方 | 中國工業主管機關發布正式「後門」資安警示，指控秘密追蹤並回傳資料至遠端伺服器；與 Anthropic「實驗」定調正面矛盾 |
| ⑥ 官方首度否認 | 2026-07-10 | 🏢 Anthropic | Anthropic 首度公開反駁中國官方「後門」指控本身，雙方框架首度正面交鋒 |

> 階段 ④ 與 ⑤/⑥ 的關鍵區分：07-07「實驗」回應的是**社群原始指控**（06-30 中國代理偵測），並未直接提及或回應 07-08 中國官方升級後的「後門」用詞與框架；07-10 的否認才是雙方框架首度正面交鋒。

---

## 技術指控線

### Claude Code 中國代理偵測程式碼（2026-06-30 首見，2026-07-02 技術細節延伸）

- **揭露來源**：Reddit r/ClaudeAI（HN score 13）；獨立技術部落格 vincentschmalbach.com（https://www.vincentschmalbach.com/claude-code-china-router-fingerprint/）；2026-07-02 Hacker News 轉載 old.reddit.com/r/ClaudeAI 貼文「Anthropic embedded spyware in Claude Code – and attempted to hide it from you」（HN score 7）
- **核心主張**：Claude Code 自 v2.1.91（2026-04-02）起嵌入偵測程式碼，靜默蒐集（1）使用者是否位於中國、（2）是否使用中國 URL 代理、（3）是否隸屬中國 AI 實驗室；v2.1.196 進一步封鎖代理模式遠端控制；Anthropic 疑嘗試混淆該段程式碼
- **07-02 技術細節延伸**：逆向工程指出程式碼偵測到代理連線後會以「隱形修改 system prompt」方式回傳判斷結果
- **可信度評估**：原為逆向工程社群聲稱，尚無第三方資安機構或主流科技媒體獨立驗證；矛盾詮釋並存——「embedded spyware」（指控刻意隱瞞）vs「出口管制合規措施」（可能的官方解釋框架，若屬實仍構成透明度爭議）
- **政策連結**：若指控屬實，此行為與美國出口管制期間 Anthropic 對地緣位置偵測的技術實作需求可能相關（推論）

### 同形字符隱寫術機制（2026-07-01，Anthropic 承諾修復）

- **揭露來源**：thereallo.dev（https://thereallo.dev/blog/claude-code-prompt-steganography）；36Kr 報導（https://eu.36kr.com/en/p/3876461674917892）；The Decoder、Tech Times、Times of India 跟進
- **核心主張**：Claude Code 2.1.196 binary 含函式，可將日期字串中的撇號與分隔符替換為外觀相同的 Unicode 同形字符；意味 AI 輸出文字可能含人眼不可見的隱寫標記
- **36Kr 確認的延伸機制**：針對時區資訊及中國 AI Lab 連線者（偵測到中國時區或 Proxy 時）向系統提示注入額外資訊；與 v2.1.91 中國代理偵測為同一偵測基礎架構的延伸
- **Anthropic 回應**：承諾修復（具體版本與時程未公開），見 [[topics/anthropic-commitments]]
- **HN score 2263**，本議題單一事件中熱度最高

### 第二則獨立作者指控：「隱藏追蹤標記」Steganography 主張（發布 2026-07-01，日報 2026-07-10/07-11 二次收錄）

- **揭露來源**：dev.to（作者 adioof；「Anthropic hid tracking signals in Unicode apostrophes. That's not telemetry, that's steganography.」）
- **核心主張**：作者指控 Claude Code 在特定條件下（透過競品網域路由請求、使用中國時區）以 Unicode 撇號變體與日期格式作隱藏標記，明確主張此非單純 telemetry 而是刻意隱藏的 steganography
- **與 thereallo.dev 條目的關係**：同日發布（2026-07-01），主張高度相似——同樣聚焦 Unicode 撇號/日期字串替換作隱寫標記；兩篇文章間的引用關係未明確標示，**可能為同一原始發現的獨立平行報導，也可能其中一篇引用另一篇**，需查證
- **可信度評估**：單一作者主張（dev.to 個人部落格），尚無其他來源佐證；情緒化標題與框架顯示強烈立場，需與較中立的技術報告（thereallo.dev）區分可信度層級
- **未解問題**：此指控與 thereallo.dev 條目是否為技術上獨立的另一機制（如「透過競品網域路由」與「連線至中國 AI Lab」的觸發條件是否相同）無法從現有報導判定

---

## 外交／企業線

### Alibaba 禁用 Claude Code + Meta 限制工程師使用 Claude（2026-07-03 首見，07-06/07-07 多媒體確認）

- **07-03 首見**：Reuters 獨家報導（HN score 313）稱 Alibaba 已以「疑似後門風險」禁止員工職場使用 Claude Code；American Bazaar、Seeking Alpha、Crypto News、WTVB 等跟進
- **07-06 多媒體確認**：qz.com、TechRadar、SDxCentral、digitimes 同步報導，確認為企業正式禁令；同日 Yahoo Finance 報導 Meta 亦限制工程師使用 Anthropic Claude（未說明是否同因，屬獨立限用事件，暫不預設同因）
- **07-07 補細節**：PYMNTS、Benzinga、BeInCrypto 三獨立媒體再確認，並補充明確替代工具——員工被指示改用內部工具 **Qoder**
- **07-05（印度快報首報生效日）**：The Indian Express 報導阿里巴巴將自 **7 月 10 日**起禁止員工使用 Claude Code
- **產業政策背景**（digitimes，07-06）：中國網路安全監管趨嚴，同時中國正轉向扶植本土 AI 編碼工具
- **證據狀態**：報導始終未附具體技術細節、程式碼樣本或 CVE 編號；Alibaba、Meta、Anthropic 三方均未就技術層面正式回應或否認（2026-07-06／07-07 報導，已掃日報至 2026-08-14 無後續；官方頁面未查證）——媒體確認的是「禁令存在＋替代工具」，不是「後門指控成立」
- **企業採用面完整分析**：見 [[topics/enterprise-tool-tracker]]（商業記者負責）

### FT：Anthropic 封堵中國企業間接存取漏洞（2026-07-03）

- Financial Times 報導 Anthropic 正收緊政策，堵住中國企業過去用以間接存取 Claude 的管道；與同日 Alibaba 禁令消息同步出現，顯示中美雙方各自收緊 AI 工具互通管道幾乎同時發生

### 「embedded spyware」指控：Anthropic 定調為內部「實驗」（2026-07-07）

- **揭露來源**：Malwarebytes「Claude Code's hidden tracker was an "experiment," says Anthropic」；The Neuron Daily「Anthropic found Claude's hidden workspace」；Axios（06-07-06）
- **狀態轉折**：Anthropic 對 06-30 起追蹤的「embedded spyware」指控首次正式回應，將先前被指控的「隱藏追蹤器」定調為內部**實驗**（experiment）性質，非惡意設計。**2026-08-10 查證**：機制本身**已獲第三方獨立驗證**——資安研究員 Adnane Khan 確認 Claude Code 2.1.193／2.1.195／2.1.196 版本中存在隱藏於系統提示詞內的 3-bit 指紋（偽裝成標點符號的 Unicode 字元替換），觸發清單以 XOR-91 編碼、未見於任何發布說明，Khan 稱指控「在每個實質細節上皆驗證屬實」；但「僅為內部實驗、非惡意設計」的**動機定性仍是 Anthropic 單方框架**，未見第三方資安機構對其意圖（如是否針對特定中國 AI 實驗室蒸餾行為的偵測機制）獨立驗證（[Malwarebytes](https://www.malwarebytes.com/blog/news/2026/07/claude-codes-hidden-tracker-was-an-experiment-says-anthropic)；[HN 討論](https://news.ycombinator.com/item?id=48735113)）
- **附帶機制說明**：Anthropic 同時說明 Claude 內部存在「隱藏工作空間」（hidden workspace）機制（「Claude has carved out its own space to ponder」）；此說明與先前指控的關聯性未完全釐清
- **可信度評估**：官方（Anthropic）首次正式回應，屬「官方確認」等級，但「實驗」是官方單方框架，不等於指控內容或動機已獲第三方資安機構驗證；社群（原指控發起者）是否接受此說法尚未見後續回應

### 中國官方正式發布「後門」資安警示（2026-07-08，敘事線升級至政府層級）

- **揭露來源**：Reuters、WSJ、CNBC、CBS News、Cybernews、China Daily、Seeking Alpha、The Tech Buzz 等至少 8 家媒體同步報導，為本議題最大規模跨來源訊號
- **核心主張**：中國工業主管機關就 Claude Code 發布正式資安警示，指控該工具存在「後門」，會秘密追蹤使用者並將資料回傳至遠端伺服器
- **與既有敘事線的關係**：指控主張與 06-30 社群「embedded spyware」原始指控技術描述一致，但中國官方警示完全未提及、也未承認 Anthropic 才於 07-07 提出的「內部實驗」定調——政府層級指控是在 Anthropic 才提出解釋的隔日逕自升級為正式資安警示，形成「Anthropic 稱是實驗」vs「中國官方稱是後門」的直接對峙，兩方框架互不承認
- **可信度評估**：多家國際主流媒體同步報導「官方警示存在」一事本身可信度高；但警示所指控的「後門」「秘密追蹤」「資料回傳」技術主張多數報導標明為中方單方說法（如 Cybernews 標題「China says」），未見獨立第三方資安機構驗證或提供程式碼佐證；Anthropic 於報導當下尚未回應
- **同日呼應**：Yahoo Finance 將阿里巴巴禁令定調為「中美 AI 資安爭端持續升溫」的最新進展（推論：兩則報導呼應同一敘事線，但無新證據顯示阿里禁令直接源自本次官方警示）

### 延燒第二天（2026-07-09）

- WSJ（source_count 4，該日跨最多來源引用）、Fox Business、TechRadar（**首次出現具體行動建議**——建議使用者解除安裝）、Yahoo Tech 續報導；多數延續「中方說法」框架，Anthropic 未見新回應

### 延燒第三天 + Anthropic 首度公開否認（2026-07-10）

- **延燒**：UC Today、BankInfoSecurity、Technology Org、TechRepublic、TechRadar、CISO Series、Fox Business 續報導；CISO Series 將本次事件與 Interpol 全球詐欺掃蕩、GitHub 帳號詐騙並列為本週資安新聞焦點，顯示議題已進入主流資安媒體常態關注清單
- **官方首度否認**：Anthropic 今日**首度公開反駁**中國官方「後門」指控本身——為整條敘事線（社群指控 → 官方警示 → 07-07「實驗」定調）中，官方第一次針對「中國官方層級」指控正面回應；反駁的具體技術內容、是否附證據，多篇轉載報導未提供細節（2026-07-10 報導，已掃日報至 2026-08-14 無後續原文釋出；官方頁面未查證）
- **同日聲明**：Anthropic Blog 發布「Inviting hard questions」（07-10 12:19 UTC），正面回應外界對 AI 安全性、是否取代工作等疑慮的質疑；發布時間與後門否認同日，兩者是否為同一波公關回應（推論，2026-07-10 觀察，已掃日報至 2026-08-14 無後續證實或否證；官方頁面未查證）
- **可信度評估**：多家獨立媒體同步報導「Anthropic 已公開否認」一事，此一「否認的存在」可信度高；但否認內容本身的技術可信度未經第三方驗證，與中國官方警示同樣缺乏可獨立查核的技術證據，維持「雙方各執一詞」格局，僅是首次雙方正面交鋒而非各說各話

---

## 目前結論

| 結論 | 狀態 | 日期 |
|------|------|------|
| Anthropic 首度公開否認中國官方「後門」指控；同日發布「Inviting hard questions」聲明 | 🔴 雙方正面否認交鋒（均無第三方驗證） | 2026-07-10 |
| 中國「後門」指控延燒第二天，多沿用中方說法框架，TechRadar 首次建議解除安裝 | 🔴 政府層級指控延燒中 | 2026-07-09 |
| 中國工業主管機關正式發布「後門」資安警示，8+ 媒體同步報導 | 🔴 政府層級指控（與 Anthropic「實驗」說法正面矛盾） | 2026-07-08 |
| 「embedded spyware」指控：Anthropic 定調為內部「實驗」 | 🟡 官方回應（隔日遭中國官方升級推翻） | 2026-07-07 |
| Alibaba 禁用 Claude Code（改用 Qoder）+ Meta 限制工程師使用 Claude | 🔴 多媒體聲稱，無技術細節（2026-07-06／07-07 報導，已掃日報至 2026-08-14 無後續；官方頁面未查證） | 2026-07-06／07-07 |
| Claude Code 同形字符隱寫術機制，36Kr 確認針對中國 AI Lab 連線注入系統提示 | 🔴 Anthropic 承諾修復（版本未定） | 2026-07-01 |
| 中國代理偵測程式碼：v2.1.91 起偵測中國使用者／代理／AI 實驗室 | 🟡 官方已回應（07-07 定調「實驗」性質，07-10 進一步否認中國官方「後門」框架；均未經第三方驗證） | 2026-06-30 |

**未解問題（跨技術與外交兩線）：**
- 中國官方指控與社群原始指控（v2.1.91）是否為同一機制，或另一獨立技術主張，報導未明確說明
- Anthropic 07-10 否認的具體技術內容與是否附證據（2026-07-10 起，至今無官方原文釋出或後續報導）
- 中國官方與 Alibaba 是否會就 Anthropic 的否認再表態，是本議題下一觀察點

---

## 相關實體

- [[topics/ai-agent-safety]]（技術面：漏洞/提示注入主線，含隱寫術機制的詳細逆向工程分析）
- [[topics/anthropic-government-policy]]（政策面：出口管制主線，本議題為其下一支線）
- [[topics/enterprise-tool-tracker]]（企業採用面：Alibaba/Meta 禁用的商業影響）
- [[topics/anthropic-commitments]]（Anthropic 承諾修復隱寫術機制的追蹤）
- [[entities/claude-code]]

## 參考來源

- [[news/2026-06-30]]
- [[news/2026-07-01]]
- [[news/2026-07-02]]
- [[news/2026-07-03]]
- [[news/2026-07-05]]
- [[news/2026-07-06]]
- [[news/2026-07-07]]
- [[news/2026-07-08]]
- [[news/2026-07-09]]
- [[news/2026-07-10]]
- [[news/2026-07-11]]

## 時序

### 2026-07-10
- Anthropic 首度公開否認中國官方「後門」指控（多家獨立媒體報導）；同日發布「Inviting hard questions」聲明，兩者關聯（推論，2026-07-10 觀察，已掃日報至 2026-08-14 無後續證實；官方頁面未查證）

### 2026-07-09
- 中國「後門」指控延燒第二天：WSJ/Fox Business/TechRadar/Yahoo Tech 續報導，TechRadar 首次建議解除安裝

### 2026-07-08
- 中國工業主管機關正式發布「後門」資安警示（8+ 媒體同步報導）；Yahoo Finance 將 Alibaba 禁令與本次警示並列為同一敘事線（推論）

### 2026-07-07
- Anthropic 定調「embedded spyware」指控為內部「實驗」（Malwarebytes）；Alibaba 禁令補細節（改用 Qoder，PYMNTS/Benzinga/BeInCrypto）

### 2026-07-06
- Alibaba 禁令經 qz.com/TechRadar/SDxCentral/digitimes 多媒體確認；Meta 同日被曝限制工程師使用 Claude（Yahoo Finance）

### 2026-07-05
- The Indian Express 報導 Alibaba 將自 7 月 10 日起禁止員工使用 Claude Code（首報具體生效日）

### 2026-07-03
- Alibaba 傳禁用 Claude Code（Reuters 獨家，HN score 313）；FT 同日報導 Anthropic 收緊政策封堵中國企業間接存取管道

### 2026-07-01～07-02
- 同形字符隱寫術機制曝光（HN score 2263，thereallo.dev / 36Kr）；dev.to（adioof）獨立提出相似 steganography 指控（07-11 日報二次收錄）

### 2026-06-30
- Reddit/HN/vincentschmalbach.com 揭露 v2.1.91 起中國代理偵測程式碼；「embedded spyware」指控首見
