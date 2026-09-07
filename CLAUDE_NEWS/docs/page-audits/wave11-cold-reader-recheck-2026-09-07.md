# Wave 11 冷讀者複驗：Opus 5 vs Fable 5.1（2026-09-07）

## 身分與規則

帶六人團隊的 tech lead，公司用 Team 方案＋API，今天要決定團隊 Claude Code 預設模型設 Opus 5 還是 Fable 5.1，並確認舊的 Opus 4.8 要不要淘汰。15 分鐘。
唯一入口 `wiki/index.md`，只沿 `[[連結]]` 走；不猜檔名、不 Glob、不全庫 grep、不讀 `docs/`／`.claude/`／`scripts/`／`news/`。行號含最上方 frontmatter。

## 路徑清單（開過的頁面＝跳數）

1. `wiki/index.md`（入口）
2. `wiki/entities/opus-5.md` ← index L36
3. `wiki/topics/model-comparison.md` ← index L35／opus-5 L124
4. `wiki/entities/fable-5.md` ← index L36／opus-5 L119
5. `wiki/entities/opus-4-8.md` ← opus-5 L120
6. `wiki/entities/pricing.md` ← opus-5 L123
7. `wiki/feature-radar.md` ← opus-5 L130
8. `wiki/entities/managed-agents.md` ← opus-5 L126
9. `wiki/entities/claude-code.md` ← opus-5 L127

---

## Q1 Opus 5 是我方案的預設嗎、多少錢 — ✅ 拿到（3 跳）

`entities/opus-5` L54「是——但只是『預設的 Opus』；Claude Code 的整體預設仍是 Sonnet」，L60 分出 Max・Team premium・Enterprise 隨用隨付＝預設，Pro・Team standard＝可用。牌價 L55「$5 ／ $25」。
Team 的兩種席位差別要再跳 `entities/pricing` L64–65（standard $20／premium $100 每席）。
半扣分：L60 的 Team standard 一格寫「依 pricing『同 Pro』推得」，讀者拿到的是推得值不是官方值。

## Q2 Opus 5 跟 4.8 差在哪、4.8 還能用多久 — ✅ 拿到（2 跳）

`entities/opus-5` L52–60 七列兩代對照一次答完：同價、知識截止 2026-01 vs 2026-05、4.8「Legacy，退役**不早於 2027-05-28**」、升上去會壞的兩件（thinking 預設開啟；只有 effort `high` 以下關得掉）。
`entities/opus-4-8` L44 同一句 Legacy 與退役日，附「2026-09-07 查證」但**無連結**。
卡住的原句：`opus-4-8` L44「**2026-07-25**：取代 Opus 4.8 成為次旗艦」——在 Opus 4.8 自己的頁面上，主詞不見了，讀起來像 4.8 取代了自己。

## Q3 官方「逼近 Fable 5、價格一半」，社群怎麼說；何時該用 Fable 5.1 — ✅ 拿到（3 跳）

`entities/opus-5` L86「分數由 Anthropic 自行提交、未見第三方複跑」、L104「官方那四個數字全部由 Anthropic 自己提交、沒有人複跑過；社群到今天也沒有一則量化實測能印證或推翻它」。這是全站最誠實的一段。
何時換 Fable 5.1：opus-5 L59「大多數工作先從 Opus 5 起手；調高 effort 仍不夠時才換 Fable 5.1」＋`topics/model-comparison` L50/L61 的分界（跨多天 vs 數小時）。
但 `topics/model-comparison` L74 情境表把「依據」寫成「官方稱評測逼近 Fable 5」，**沒有帶上「無第三方複跑」那句**——決策層比證據層寬鬆。

## Q4 用 Opus 5 跑長時間 agent 任務的已知問題 — ⚠️ 半拿到（4 跳）

拿到的：opus-5 L58 thinking 預設開啟、L36「官方是否已標記解除，本站截至 2026-09-07 未見更新」（09-03 錯誤率事件）、L178／L180 兩筆待查證；`entities/managed-agents` L73 beta＋L82 官方算例 $0.705／小時；`entities/claude-code` L93「進程增長至 120GB+ 遭 OOM killed……Linux 上長時間執行的 session」。
沒拿到的：沒有任何一節把「Opus 5 ＋ 跑好幾小時」合起來回答。L93 是 Claude Code 的毛病、L73 是框架成熟度，跟模型無關；opus-5 頁自己一句長跑注意事項都沒有。四跳之後我仍要自己拼。

## Q5 三頁我該讀哪頁、分得出差別嗎 — ⚠️ 半拿到（4 跳）

分工寫得出來：opus-5 L44「這份工作該用哪個模型見 model-comparison」；model-comparison L42「本頁只回答我這份工作該用哪個」。讀完三頁能說出差別。
分不出的是兩張表：`entities/opus-5` L48–60 與 `entities/fable-5` L47–59 同名同結構同導言（「一格一個……兩欄是兩代的答案」），連熱度表都同值（🔥🔥🔥🔥🔥／⚡／2026-09-07 判定）。截圖給我看我認不出是哪一頁。

---

## 特別提問 1：入口首屏

前 45 行只有 **L36** 一條路提到 Opus 5，而且藏在全表最長那格的**句尾**：「我要不要換到新旗艦、舊的會不會停掉……→ [[entities/fable-5]]『你現在拿到的是什麼』；Opus 這一代見 [[entities/opus-5]] 同名節」。主詞是 Fable，Opus 5 是補述。實體表那一列在 L54，已在首屏外。
L35「寫 code 該用哪個模型 → [[topics/model-comparison]]」也是首屏的路。
**它會不會把我送到一張答不了問題的表？** 會。model-comparison L48 快速選型表四欄（模型｜定位｜定價·Context｜最適合），沒有任何一格回答「團隊預設該設哪個」；L51 只寫「次旗艦（Max 預設／Pro 最強）」。我要的「設成全隊預設」這個動作，全站沒有一頁作答。

## 特別提問 2：幾頁在講 Opus 5／打架的行號／哪個是「現在」

**七頁在講 Opus 5**：opus-5、model-comparison、fable-5、opus-4-8、pricing、feature-radar、managed-agents。
分不出差別的兩頁：`entities/opus-5` 與 `entities/fable-5`（見 Q5）。

同一事件兩處寫得不一樣：

| 事實 | A | B |
|---|---|---|
| 定價兩說是否已解 | `feature-radar` L572「兩說法方向不完全一致……待觀察」（還停在發布首日） | `entities/opus-5` L191／`entities/pricing` L125「2026-08-08 官方查證確認兩說皆成立」 |
| 資安任務該用誰 | `feature-radar` L572「仍建議用 Mythos 5」 | `topics/model-comparison` L66「Mythos 一般使用者取不到，不可作為淘汰基準；公開陣容資安首選 Fable 5.1」 |
| Pro 最強可用模型 | `entities/pricing` L83「Opus 5 為 Pro 方案最強可用模型」 | 同頁 L61 Pro 可用 Fable 5（走 usage credits）——同一頁自打 |
| Fast Mode 費率 | `entities/opus-4-8` L46／L71「降至前代的 1/3」 | `entities/opus-5` L67「基礎價兩倍（$10／$50）」——兩個基準，讀者無從相減 |
| 發布日 | `entities/opus-5` L42「官方 2026-07-24（本站 07-25 收錄）」 | `feature-radar` L147／`model-comparison` L187 單寫 2026-07-25，未註明 |

**看得出哪個是「現在」嗎？看不出。** 每頁頂部同時有「最後更新」與「最後新聞更新」兩個日期（opus-5 L32／L33 為 09-07 與 09-03），沒有一句話說哪個代表現況；feature-radar L5 只有一個「最後更新 2026-09-06」，但它 L572 的內容是 07-25 的。頁頂日期新，不保證內文是新的——這正是我被騙到的地方。

## 特別提問 3：每頁總評（百科 or 雷達）

| 頁 | 判定 | 依據 |
|---|---|---|
| `entities/opus-5` | **雷達**（上半）＋百科（下半） | L48 兩代對照與 L104「所以呢」是雷達；L154–193 四十行歷史記錄是百科 |
| `entities/fable-5` | 雷達 | L47 對照表、L84 護欄表都寫「你能先做什麼」 |
| `topics/model-comparison` | 雷達 | L46 選型表＋L112 換算表直接可用 |
| `entities/opus-4-8` | **百科** | L103–121 十九條社群評價按時間堆疊，沒有一句「所以我現在該不該淘汰它」 |
| `entities/pricing` | 雷達 | L42「09-14 是下一個會動到你帳單的日子」 |
| `feature-radar` | 雷達（前半）／百科（後半） | L12、L22 是雷達；L565 之後的舊條目已腐爛 |
| `entities/managed-agents` | 雷達 | L69 選型表、L111「你的選項」 |

## 特別提問 4：內部用語外洩（10 條）

1. `entities/opus-5` L178「⟨Q-01⟩ ❓ **待查證**（標 2026-08-29｜查 1w0uyu7、code review｜複 2026-09-12）」——標／查／複三個單字，我不知道是什麼欄位；`1w0uyu7` 是給機器比對的字串。
2. `entities/opus-5` L156「❓ ⟨Q-01⟩ 這類記號代表『這一則我們還沒查到答案』」——需要一句話解釋的記號，本身就是內部記號。
3. `entities/opus-5` L102「（Artificial Analysis，2026-08-10 一次性查證）」——「一次性查證」是維護節奏詞。
4. `entities/opus-5` L44「本站 07-25 收錄」——「收錄」是編輯部動作。
5. `entities/fable-5` L76「本表跟著 [[feature-radar]] 全覽表的現行世代那一列走」——在講兩張內部表怎麼同步。
6. `entities/managed-agents` L67「以下分界只填本庫查得到出處的欄位，查不到的留 `—` 或標為待查證，不以通用工程常識補」——整句是寫給撰稿者的守則。
7. `entities/managed-agents` L60「近四週（08-09～09-06）只被提到兩天」——「被提到」＝被本站報導過，讀者會誤讀成業界沒人在用。
8. `entities/pricing` L56「非曾規劃但已暫停的 programmatic 信用池金額」——一句話裡兩個未定義名詞。
9. `feature-radar` L26「[[entities/claude-code#版本更新]] 記的是本站報導過的新功能（來源日報）」——「日報」是內部產物名。
10. `entities/opus-5` L167 表格日期欄「2026-07-30・08-07・08-13・08-20」擠成一格＋L98「五則『變差了』型貼文」——「型」的分類法是編輯分類，不是讀者語言。

## 特別提問 5：「這是在騙我／數字哪來的／撐不起」

- **撐得起的**：`entities/opus-5` L86／L104 明說四個官方數字沒人複跑過；L165「SitePoint……三項皆與官方不符，不採信」；L180「$19 Gap……僅標題可用，不採信為事實」；`entities/pricing` L70「時分為多家媒體轉述，官方說明中心原文本站尚未取得」。這幾句讓我更信這個站。
- **「這些數字是誰量的」那一節：更信官方數字嗎？** 不更信官方，但更信這一頁——它把四個數字全標成「官方自己提交」（L86），我因此知道該打幾折。這是全站最有價值的一節。
- **撐不起的**：
  - `entities/opus-4-8` L69 定價欄「與 Opus 4.7 相同」——沒有數字、沒有日期、沒有出處，我得跳兩頁才知道是 $5／$25。
  - `entities/opus-4-8` L29／L44 「Legacy、退役不早於 2027-05-28」只寫「官方模型總覽頁（2026-09-07 查證）」，**全頁沒有一個可點的官方連結**（L147–150 三條參考來源都不是模型總覽頁）。同一句在 `entities/opus-5` L57 也只有出處名。「退役」是我今天要拿去說服團隊的那個字，它現在點不開。
  - `entities/opus-4-8` L54 熱度 🔥🔥🔥🔥 沒有判定日（opus-5 L76、fable-5 L72 都有）——一個沒有日期的熱度值等於沒有值。
  - `feature-radar` L16「Max／Team premium／API 的預設 Opus」與 L572「發布首日……待觀察」同頁並存，後者已過期 44 天。
  - `entities/opus-5` L98「其中兩則原文已不可取得」——我無法自行核對的證據，被當成「五則」的一部分計數。

## 特別提問 6：最想改的三件

1. **`entities/opus-5` 與 `entities/fable-5` 的同名表加一句身分句**（各在 L50／L49 的導言處寫明「這一頁是 Opus 這一代」），並讓兩頁的熱度表不再逐字相同。現在兩頁長得像同一頁的兩份影本。
2. **`feature-radar` L565–572 的 Opus 5 舊條目就地重寫或撤掉**：同一頁 L16 已經是 09-07 的說法，L572 還停在 07-25 的「待觀察」，而頁頂只有一個「最後更新 2026-09-06」讓我以為整頁都是新的。
3. **把 `entities/opus-4-8` 從百科改成一句判決**：頁頂補「你現在該不該淘汰它」——退役日（附官方連結）＋一句「新採用一律改 Opus 5」。現在這個答案散在 L29、L44、`model-comparison` L56、`opus-5` L57 四處。

## 特別提問 7：這一頁在回答幾個問題／該不該拆

以 `entities/opus-5` 為準（唯一被我當主頁讀的那頁），它在回答四個問題：

1. 這一代跟上一代差在哪（L48–67）
2. 官方的分數可信嗎、社群反證有多硬（L84–104）
3. 它有什麼規格與能力（L108–113）
4. 上線以來發生過什麼（L154–193，四十行）

**該留一頁。** 前三個問題共用同一個判斷——「我要不要用它」，拆開反而讓讀者在兩頁間對照。要動的是第 4 群：L154–193 佔全頁 20%、且 L167 已經把四則社群貼文壓成一格，它是證據不是結論，該整段搬去封存頁，正文留 L98–102 那幾條已經熬好的結論。
`entities/opus-4-8` 相反：它只該回答一個問題（要不要淘汰），現在卻塞著 L103–121 的十九條社群評價與 L152–162 的傳聞考古，那兩段的問題（「4.8 當初出了什麼事」「Opus 5 傳聞真假」）今天沒有人會單獨問。

**⚠️ 疑似注入：** 無。九頁中未出現指令式文字。
