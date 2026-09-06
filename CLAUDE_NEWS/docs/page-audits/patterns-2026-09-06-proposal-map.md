# 逐行號去向表：`wiki/topics/community-tech-patterns.md`（第 8 波）

行號＝檔案原始行號（含 frontmatter 24 行）。逐字稿見 `-draft.md` 的 A／B 欄。**一行不憑空消失**：凡「砍」皆註明事實搬到哪裡。

**第二輪更正（🔴-3）：** 缺口追蹤、誰負責拆分、目前結論三段的行號上一輪錯 1–6 行，我逐段複核屬實。**這三段改以列首文字定位，行號只作參考**——同一波內前面的編輯會把後面的行推移，行號本來就不該當實作座標。

| 行號 | 現在是什麼 | 去向 | 落點 |
|---|---|---|---|
| L1–24 | frontmatter | 留（機器產生） | `gen_wiki_frontmatter.py` 重跑後 `pending_count` 6→7、`last_updated` 改今日 |
| L26–32 | H1 ＋ 標頭六欄 | 留，只改「最後更新」為 2026-09-06；**不動「最後新聞更新」**（本波是結構重整，非新聞） | — |
| L33–37 | 頂部 callout（2 則，2026-09-05） | **留，只改 L35 一個詞**：「存量盤點新收錄」→「本庫首次收錄」 | draft A-1c（🟡-9 選 (a)）。其餘九處「存量盤點」（L172／L173／L210／L219／L320／L328／L329／L338 等）**本波不動，列回訪** |
| L40–50 | `## 摘要` 5 段 | **改**（整節替換） | draft A-1。首句改成 delta；L44 三頁分工句拆成「哪一頁答什麼」；trends 入口補「哪個方向在加溫」 |
| L48 | 官方 context engineering 指引段（42 天，寫在摘要像新聞） | **下沉，不是刪除**——五欄逐字稿見 draft **A-1b**（主線填 `Context 管理`） | 移進 `### 2026-07` 分組最上方。**它會在 2026-10 隨該月被搬進 archive**，B-1 §8 已加保護句 |
| L52 | `## 模式概覽` 節名 | 留（`wiki_graph explain --section "模式概覽"` 回錨點邊無，改名零風險但無必要） | — |
| L53–55 | 表頭 4 欄 | **改為 5 欄**（＋「最後動態」），25→**21 列** | draft A-2；錨點一律全頁式 `[[topics/community-tech-patterns#YYYY-MM]]`（🟡-7） |
| L56–59 | ✅ 4 列 | **留＋補日期與錨點**，順序 Multi-agent／Skills 設計／CLAUDE.md／Hooks（前兩者同為 09-02，同日維持原相對順序） | 09-02／**09-02**（Skills 由 09-05 更正，09-05 那則的關係行寫的是「Skill 生態多元化」不是「Skills 設計」）／08-04／08-02 |
| L60–64、L66 | ⚡ 6 列 | **留＋補日期與錨點**，順序 Plugin·MCP／模型使用策略／記憶與知識管理／Context 管理／Token 成本／多代理 PR Review | 09-05／09-04／09-02／08-27／08-19／08-04 |
| **L62** | ⚡ 記憶與知識管理 | **留，並吸收 L71** | 代表技巧併入 Core Memory Packet；這是 `wiki/log.md` L2858／L3014／L3325／L3509 四次提案的落地 |
| **L65** | ⏳ Agent 版本控制（夾在 ⚡ 之間＝排序壞掉） | **改位**：移到 ⏳ 區，最後動態 2026-07-31 | 排序壞掉是本列造成的，移位即修好 |
| L67–70、L72–74、L76、L79–80 | ⏳ **11 列** | **留＋補日期與錨點**，依最後動態降序排 | 08-27→07-12 |
| **L71** | ⏳ 跨環境 Agent 記憶（本頁零節點，唯一出處在 archive 2026-05-12） | **併入 L62** | 代表技巧 Core Memory Packet 與 L62 完全重疊——四次提案的同一組 |
| **L75** | ⏳ 確定性 Agent 框架 | **移出表，降表下一段** | **評審重算新增的一列**：關係行從未逐字寫出這個類別名，頁內算不出最後動態；我上一輪給的 07-15 來自 L857 一則 `**核心模式：**` 行，不在定義射程內 |
| **L77／L78** | ⏳ Agent 記憶保護、跨 Repo 依賴可視化 | **移出表，降表下一段** | 頁內算不出最後動態（我上一輪給的 2026-06-30 來自 **archive**，不在定義射程內）。表下那段標題因此是「四類已經算不出最近的動靜」不是「兩類已超過 60 天」 |
| L82 | 成熟度圖例 | **留，一字不動**（全頁唯一做對的符號說明） | — |
| L84–90 | 「類別細節」7 條 | **留**；被移出的兩類若在此有條目一併帶走（實測：無） | — |
| L93–96 | 「查證備註」（arXiv 交叉審查） | **留，一字不動**（冷讀者評為全站最扎實處） | — |
| L98 | `## 學術對照` 節名 | 留 | — |
| L99 | 導言（三種機制） | **改**：改寫成官方三層階梯（subagent → agent teams 實驗性 → cross-session），加「資料截至 2026-09-06」 | draft A-4；依 `-verified.md` 第一、二節 |
| L101–108 | 對照表 5 欄 × 3 列 | **改為 5 欄 × 4 列**：新增「官方狀態」欄（取代 MAS 綜述術語欄，該欄值下沉補充段）、新增 Cross-session 一列；Agent Teams 標「實驗性，預設關閉」 | verified：需 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`、文件 as of v2.1.178 |
| L110 | `### 誰負責拆分` 節名 | 留 | — |
| **L114–119**（實測；上一輪誤寫 L111–125） | 拆分來源表 3 欄 × 4 列 | **改為 4 欄 × 5 列**：新增「官方怎麼說（2026-09-06 查證）」欄；新增「模型自動委派」列；「peer 之間協商湧現」列**更正**為「lead 拆分後隊友自領」 | verified 第一節逐字（Claude automatically delegates…）、第二節逐字（The lead breaks work into tasks…；自領 claim 用 file locking） |
| **L121**（實測；上一輪誤寫 L127） | 「核心經驗（文獻）」四條 | **留，加日期**「文獻怎麼說（截至 2026-07-22）」並壓成一段 | draft A-4 |
| L128–137 | 參考論文列 9 筆 | **留，一字不動**（連結全部可點，冷讀者確認） | 補新論文屬主編查證，本波未查到，不硬填 |
| **新增** | — | **新增「社群這邊實際跑出來的三則」** | L186（147 subagent／24 天）、L375（fork 重送 200 萬 token）、L507（Opus 腦＋Sonnet 手），各附月份錨點——健檢卡 Q3 的核心缺陷 |
| L139 | `### 缺口追蹤` 節名 | 留 | — |
| **L141**（實測；上一輪誤寫 L140） | 導言（含「狀態判定為盤點結論（推論）」） | **改**：加「資料截至 2026-09-06（官方文件查證）」、狀態三值說明；「盤點結論（推論）」改寫成讀者語言 | 冷讀者外洩第 7 條 |
| **L143–151**（實測；上一輪誤寫 L141–152） | 缺口表 7 列，狀態 ✅／❌ | **改**：狀態符號 → 文字三值（已補／部分補上／未補），解 ✅ 撞名 | draft A-5 |
| **列首「強 planner ＞ 強 executor（PEAR）」那一列（實測 L147；上一輪誤寫 L148——L148 是動態粒度，照舊稿會翻錯列）** | 「分模型 ❌ 未補」 | **翻為「已補（2026-09-06 查證）」** | verified：subagent 定義有 `model` 欄、呼叫時可另行指定、`CLAUDE_CODE_SUBAGENT_MODEL`、teams 文件建議隊友用 Sonnet。**這是冷讀者抓到的頁內自相矛盾**（L148 vs L60 官方基準 46%／96%） |
| 列首「通訊原語」「Orchestrator→worker context 交接」兩列（實測 L145／L146） | 兩列 ✅ | **留為「已補」＋補查證日與條件** | verified：cross-session v2.1.224+（Windows 2.1.234+）、fork 繼承整段對話 |
| 列首「動態粒度（ADaPT／Coarse-to-Fine）」那一列（實測 **L148**） | 動態粒度 ❌ | **留為「未補」＋補查證日** | verified 未見動態粒度，誠實寫「截至查證日未見」 |
| 列首「Mixed-initiative 共享計畫」「Coordination／conflict resolution」「Trust／verification 層」三列（實測 L149–151） | 三列 ❌ | **留為「未補」**（無查證日，因無官方文件可查） | — |
| L153–156 | 「細節」兩條（含 Anthropic 08-17 自家研究反證） | **留**，並把「協調＝迴避不是解決」那句**升進 A-3 結論層第 2 條** | 健檢卡第 5 節第 3 點：全頁最好的判準埋在第 153 行 |
| L157 | ⚠️ 一項倒退 | **留**，加 ⟨Q-07⟩ 懸置（49 天未回訪，官方未查到） | draft A-5 |
| L159–161 | 「與官方缺口矩陣互見」 | **改**：補一句分工——那頁是官方視角、這裡是文獻視角 | 健檢卡第 11 節 |
| L163 | `## 技術彙整` 節名 | 留；**節名下加一行 ⟨Q-nn⟩ 圖例** | draft A-7 |
| L165／L294／L692／L1059／L1071 | 月份分組標題 | **留，一字不動**（是概覽表新錨點的目標，改名即斷鏈） | `build_web.py` 的 `check_wikilink_anchors()` 會驗 |
| L167–1058 | 115 則節點 | **留，除下列三類** | 證據底不動 |
| L263／L272／L281／L290／L301／L310 | 「可信度註記」6 行含收錄門檻 | **改寫**（去掉「收錄標準」「以內容本身判斷收錄，不看讚數」） | draft A-6。本頁 12 筆存量指紋歸零 |
| L676／L713／L724／L734／L752 | 5 筆完整懸置標記裸露在條列 | **改為短標記 `🔎 查無官方 ⟨Q-nn⟩`**（符號＋類別詞＋短標記三段缺一不可，🔴-1），完整式下沉該月份組末「懸置細節」 | draft A-7 |
| **L755** | 第 6 筆標記，與 L752 同節點同事實（探針同為 ip_reminder、JSONL） | **刪除（去重）** | 事實不消失——L752 的 ⟨Q-05⟩ 是它的家。刪後淨值 141−1＋2＝**142，閘不會擋**（`fingerprints` 裡 `ip_reminder、jsonl` 重複兩次）；仍須同批 `--rebuild-count --reason` 清掉重複指紋 |
| L1059–1070 | `### 2026-06` 蒸餾總結 ＋ archive 指針 | **留，一字不動**（指針已核：`archive#2026-06` 在 archive L39） | — |
| L1071–1083 | `### 2026-05` 蒸餾總結 ＋ archive 指針 | **留，一字不動**（`archive#2026-05` 在 archive L529） | — |
| L1085 | `## 目前結論` 節名 | **改名** `## 現在收斂到哪、哪些還在試` | 全庫 `grep "community-tech-patterns#"` 零命中，改名零斷鏈 |
| **列首「社群工具生態活躍」那一條（實測 L1087；上一輪誤寫 L1088）** | 「70+ 款工具持續追蹤」 | **砍數字**，改寫成 wikilink 指 tools 頁 | 三個數字互不一致；**本頁不是工具數的家**。tools 與 index 的不一致走轉知帳本 |
| **列首「Multi-agent 協作是最熱門的探索方向」那一條（實測 L1088；上一輪誤寫 L1089）** | 「官方量化 15 倍 token」（孤兒數字） | **改寫＋登記懸置 ⟨Q-06⟩** | 庫內唯一出處是停滯 107 天的 `community-tech-timeline` L109，無一手。不刪不虛報 |
| **L1092** | 「6/15 計費政策後爆發」（政策已 2026-06-16 暫停） | **改寫** | 「2026-06 計費切割風波（該政策已於 2026-06-16 暫停）之後」 |
| 列首「Skills 正在從」「CLAUDE.md 最佳實踐」「Hooks 機制正從」三條（實測 L1089／L1090／L1091） | 其餘三條結論 | **改寫**：各補一個月份錨點與「接下來看什麼」 | draft A-3 |
| L1096 | 「概念辯論見 discussions」引言 | **留** | — |
| L1098–1108 | `## 相關實體` 9 條 | **留**，只改 timeline 那一條（見「整頁去向」） | — |
| L1110–1135 | `## 參考來源` 日報連結 | **留，一字不動** | — |

## 跨頁與跨維護者

| 對象 | 動作 | 走哪條路 |
|---|---|---|
| `wiki/index.md` L37 前新增一列、L38 描述、L98 鉤子 | **主編執行**（記者不得改 index） | draft A-8 |
| `wiki/index.md` L100「pattern-trends 7 條」vs 該頁實有九條（`community-pattern-trends.md` L52–299） | **不由我改**（主 session 已定） | 主編 |
| `community-tech-discussions`「本週熱點」含 2026-06 條目 | **不由我改**（第 9 波） | — |
| `community-pattern-trends`、`community-large-codebase-workflow`、`community-tech-tools` | 同維護者，本波只准改入口句／互指句 | **本案未改它們任何一行**——入口句寫在本頁 A-1 |
| `topics/official-community-gap`（功能記者） | 補一句與本頁缺口追蹤的分工 | `python scripts/pending_handoffs.py open --from 社群 --to 功能 --page topics/official-community-gap --note "補一句分工：該頁是官方視角、patterns 缺口追蹤是文獻視角"` |
| 工具數三處不一致（本頁移除自己那個後仍剩 tools 目錄實列 vs index L98 的 91） | 定一個值 | `python scripts/pending_handoffs.py open --from 社群 --to 社群 --page topics/community-tech-tools --note "工具數：目錄實列數與 index L98 的 91 不一致，定一個值並請主編同步 index"` |
| `community-tech-patterns-archive` L35 callout 寫著規則檔路徑（維運術語外洩） | 記回訪清單，本波不動 | archive 是證據層，原文照搬原則 |

## 整頁去向（`community-tech-timeline` 併入 `community-tech-patterns-archive`）——**使用者已裁「併」，本表即定稿**

不再保留「不併」版。逐字殼與搬家體例見 draft **A-9**。

### 該頁自己

| 該頁的節 | 定稿去向 |
|---|---|
| 標頭六欄 | 轉址殼：`**狀態：** resolved（**已併回**）`、`**領域：** 🌐 社群`、`**上層：** [[topics/community-tech-patterns-archive]]`、最後更新 2026-09-06、最後新聞更新維持 2026-05-22。`page_role=redirect` 由 `gen_wiki_frontmatter.py:244-248` 依 head60 裡的「已併回」三字生成，不手填 |
| callout ＋ 摘要（L31–45） | 換成單句識別字，全文見 draft A-9-1。**「已併回」必須在前 60 行內**（`gen_wiki_frontmatter.py:167／244`、`check_hierarchy.py:55` 都只讀 head60） |
| `## 時序`／`### 2026-05`／`### 2026-04` 三個包裝標題 | **丟棄**（只有這三行）。逐字稿寫「只丟包裝」，**不寫「一字不刪」**——那句話對包裝標題不成立（🔴-5） |
| `### 2026-04` 之下的 `####` 條目 | **原文照搬**進 archive 新開的 `## 2026-04`，其下先放一行 `### 時序流水帳（併自原社群時序頁，2026-04-25～04-30）` |
| `### 2026-05` 之下的 `####` 條目 | **原文照搬**進 archive 既有 `## 2026-05` **末尾**，其上先放一行 `### 時序流水帳（併自原社群時序頁，2026-05-01～05-22）` |
| 該頁「15 倍 token」轉述 | 隨條目搬進 archive |
| 懸置標記 | **0 筆**（評審複核）——本波併頁**無保命條款風險**，前四波每波都中的那條本次不適用 |

### archive 目的地要動的兩處

| 處 | 動作 |
|---|---|
| `community-tech-patterns-archive.md:35` callout | **改寫**（🟡-19）：去掉規則檔路徑與「月度蒸餾機制」，改成也涵蓋新併入的流水帳。逐字見 draft A-9-3。我上一輪判它「證據層、原文照搬、列回訪」——併頁後這句本來就要改，順手一併改掉 |
| archive 標頭 | `**最後更新**` 改 2026-09-06；**`**最後新聞更新**` 維持 2026-06-30 不動**（併進來最新條目 05-22 更舊，且搬位置不是新聞） |

### 全庫 7 處引用（🔴-4；我上一輪寫「三個入邊」是錯的，逐處複核如下）

| # | 位置 | 現在寫什麼 | 改成 | 誰改 |
|---|---|---|---|---|
| 1 | `wiki/index.md:109` | 目錄列（monitoring） | **整列刪除**（redirect 不入 index，`gen_wiki_frontmatter.py:88` 的 `redirect_slugs` 與 `test_index_sync.py:74-82` 已排除） | 主編 |
| 2 | `wiki/topics/community-tech-patterns.md:1107`（**不是 L1106**） | 相關實體「2026-04-25 至今完整時序記錄，從本頁拆分」 | `- [[topics/community-tech-patterns-archive]]（2026-04-25～05-22 的社群時序流水帳，已併入該頁）` | 社群記者 |
| 3 | `wiki/topics/community-pattern-trends.md:45` | 分工句「何時首次出現的歷史流水帳見 [[topics/community-tech-timeline]]」 | 同句改指 `[[topics/community-tech-patterns-archive]]` | 社群記者（同維護者，屬入口句層級） |
| 4 | `wiki/topics/community-pattern-trends.md:322` | 相關實體「（4–5 月歷史流水帳，演進起點考據）」 | 同上改指 archive | 社群記者 |
| 5 | `.claude/rules/wiki-ingest-community.md:13` | 負責頁面表列 timeline | **刪列**——留著等於每天把時序類條目路由到一個轉址殼 | 主編 |
| 6 | `.claude/rules/wiki-ingest-community.md:105` | 「不再歸檔至 timeline（timeline 維持趨勢時序頁角色，**不兼任封存箱**）」 | 「不再歸檔至獨立時序頁；封存一律走 [[topics/community-tech-patterns-archive]]（原 `community-tech-timeline` 已於 2026-09-06 併入該頁）」——這句併頁後直接與現狀相反 | 主編 |
| 7 | `.claude/agents/wiki-reporter-community.md:26` ＋ `.claude/rules/wiki-ingest-format.md:294` | 兩處「典型大型頁面」清單含 timeline | 從清單移除（轉殼後約 12 行，不再是大型頁面）。format 檔那半句是刪一個檔名、不動任何條文 | 主編 |
| — | ⟨Q-06⟩ 懸置細節內文（draft A-3） | 「本庫僅 [[topics/community-tech-timeline]] 轉述過」 | 改指 `[[topics/community-tech-patterns-archive]]`（🟡-18；探針字串 `multi-agent token、15 倍` 非 wikilink，不受影響） | 社群記者 |

**收工判準：** `grep -rn "community-tech-timeline" wiki/ .claude/ scripts/ | grep -v log.md` 只剩 timeline 自己那一檔。

**併的理由（已成裁決，記錄備查）：** 同一批 2026-05 的料被封存兩次（timeline 整頁 vs `patterns-archive` 的 `## 2026-05`），而兩個封存頁待遇相反——合規的 archive 不佔 index 列，凍結 107 天的 timeline 反而佔著。
