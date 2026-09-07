# 逐字稿：`wiki/entities/fable-5.md`（第 10 波）

分兩欄：**A 進頁面**（讀者語言，已過兩閘並驗紅）與 **B 進規則檔／帳本**（判準、退場、上限、同步——條文不得出現在頁面正文）。
行號＝檔案原始行號（含 frontmatter 25 行），**以磁碟現行檔為準**（該檔在 git 為 `M`，差異只有 frontmatter 兩行）。⚠️ 疑似注入：無（對象頁、九個鄰居、index、四份規則檔皆無指令式文字）。

---

# A. 進頁面

暫存檔 `wiki/entities/__w10draft.md`（只放要進 wiki 的文字），兩閘量完即刪；交件時該暫存檔已刪除。

## A-1. H1 與標頭（取代 L26–33）

```
# Claude Fable 5 與 5.1

**類型：** model
**狀態：** active（現行世代為 Fable 5.1；Fable 5 為 Legacy，官方載明退役不早於 2027-06-09）
**領域：** 🤖 模型
**別名：** Fable 5, Fable 5.1, Claude Fable 5.1
**首次出現：** 2026-06-09
**最後更新：** <實作日>
**最後新聞更新：** 2026-09-04
```

`**別名：**` 依 `.claude/rules/wiki-ingest-format.md`「別名欄位」放在「領域」之後。H1 與節名改動的射程已實掃：`grep -rn "fable-5#" wiki/ .claude/ scripts/` **零命中**，無人以錨點指進本頁任何一節。

## A-2. 頂部 callout（取代 L35–36）

```
> **最新進展**（2026-09-01）
> Fable 5.1 GA 發布並取代 5.0 成為現行旗艦：同價、快取讀取便宜 75%、知識截止晚 5 個月；Fable 5 轉為 Legacy，官方載明退役不早於 2027-06-09。
```

原 callout 的費馬事件不是本頁的事——官方原文寫「a general-purpose internal research model roughly comparable to Claude Fable 5.1」，不是 Fable 5 也不是 5.1（`-verified.md` 第一節第 7 列）。

## A-3. `## 現況` 兩段（取代 L42–48 四段）

```
現行世代是 **Fable 5.1**（2026-09-01 GA）；**Fable 5 仍可呼叫但已列為 Legacy**，官方建議遷移。兩者都是 Mythos 級模型的公開版——與同世代 Mythos 共用模型權重，差別在 Fable 前置了安全分類器，判定高風險時**會通知你**並改由 Opus 4.8 回答。

出口管制已於 2026-06-30 解除、07-01 起全球恢復存取，現在不影響你拿不拿得到；政府那條線之後怎麼走見 [[topics/anthropic-government-policy]]。方案內含什麼、超出怎麼算見 [[entities/pricing]]。
```

**本頁不再寫封鎖天數**（原 L48「歷時 18 天」與 L327 節標「至 06-30」是全庫三個端點組合中的兩個）——天數與起訖的家是 [[topics/anthropic-government-policy]]，本頁只寫對讀者有後果的那半句。

## A-4. `## 你現在拿到的是什麼`（新節，取代 L50–56 指標表）

```
> 資料截至 2026-09-07（官方模型頁與說明中心查證）。一格一個你會問的問題，兩欄是兩代的答案。

| 這一格 | Fable 5（Legacy） | Fable 5.1（現行） | 官方出處（查證日） |
|---|---|---|---|
| 現在誰是預設 | 否 | 是——Claude Code v2.1.257 起 Fable 的預設即 5.1，用 `/model` 確認 | [[feature-radar]] 版本階梯（2026-09-04）|
| 牌價（輸入／輸出，每百萬 token）| $10 ／ $50 | $10 ／ $50（同價）| 官方模型總覽頁（2026-09-07）|
| 快取讀取 | 基礎輸入價 ×0.1（$1）| ×0.025（$0.25）——便宜 75% | 官方定價頁（2026-09-07）|
| 知識截止 | 2026-01 | 2026-06 | 官方模型總覽頁（2026-09-07）|
| 會不會停掉 | Legacy，退役**不早於 2027-06-09**，官方建議遷移 5.1 | 退役不早於 2027-09-01 | 官方模型總覽頁（2026-09-07）|
| 官方推薦拿它做什麼 | 同右（官方已改推 5.1）| 高要求推理與長期 agentic 工作；Opus 5 調高 effort 仍不夠時 | 官方選型文件（2026-09-07）|
| 我的方案能不能用 | Max 與 Team premium：週用量 50% 內免費；Pro 與 standard：走 usage credits | 同左，兩代同一套規則 | 官方說明中心（2026-09-07）→ [[entities/pricing]] |

**表下細節**

- **兩代共用一套方案規則**：官方說明中心寫「Fable 5 and Fable 5.1 are available on all paid plans」，但「拿得到」不等於「方案內含」——Pro 拿得到，是走 usage credits 付費。2026-07-19 到期的那檔免費促銷只適用 Fable 5，5.1 從未納入。
- **Context 與輸出長度兩代相同**：1,000,000 token context、128,000 token 最大輸出。1M 這個旋鈕本身的計費與可見性見 [[topics/long-context-1m]]。
- **5.1 新增反萃取（anti-distillation）機制**，防止他人萃取權重或行為訓練競品（官方 2026-09-01 公告）。
```

七列答掉冷讀者 Q1（第 7 列）與 Q2 的三半（第 1、3、4、5 列）。「會不會停掉」那一列是全站目前零處寫著的官方答案（`-verified.md` V2）。

## A-5. `## 熱度與試用價值`（取代 L60–67）

```
| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥🔥 |
| 試用價值 | ⚡ 有條件推薦（2026-09-07 判定）|
| 最適合 | 跨多天的長期 agentic 工作流、多步驟深推理、安全漏洞分析 |
| 不適合 | 日常短問答（成本過高）；分散式訓練基建、加速器設計這類前沿 LLM 開發（分類器會擋，見下一節）|

> 本表跟著 [[feature-radar]] 全覽表的現行世代那一列走；最新熱度以 [[feature-radar]] 為準。
```

**兩個值都不動**：radar 全覽表 L126（Fable 5.1，現行世代那一列）是 🔥🔥🔥🔥🔥／⚡ 有條件推薦，與本表一致。radar L181 是 Fable 5.0 的舊列，不是本表的對照對象（見 B-4）。本波新增的只有判定日與「不適合」欄的改寫。

## A-6. `## 護欄會怎麼改寫你的請求`（新節，本頁唯一無別家的內容）

```
送進去的請求若被前置安全分類器判為高風險，**你會收到通知**，該次請求改由 Opus 4.8 回答，不是安靜地把品質調低（官方 2026-06-30〈Redeploying Claude Fable 5〉：「Users will be notified if a request to Fable 5 is blocked」）。2026-06-09 發布時的「降級且不告知」已於 06-11 由官方道歉撤回。

| 會踩到的類別 | 具體是什麼 | 誰最容易誤觸 | 你能先做什麼 |
|---|---|---|---|
| 資安（cybersecurity）| 攻擊性資安任務 | **日常 coding 與 debugging 也會較常被誤標**（官方自己寫明的代價）| 看到通知就接受 Opus 4.8 的答案，或把安全審查拆成不觸發的小步驟 |
| 生物與化學 | 高風險生物、化學請求 | 做相關研究的人 | 2026-08-07 官方更新分類器後生物領域誤判約降 85%，再遇到就換問法 |
| 模型萃取（distillation）| 取得權重或行為以訓練競品 | 想拿它的輸出訓練自己模型的人 | 沒有繞法 |
| 窄範圍前沿 LLM 開發 | 分散式訓練基建、ML 加速器設計、非標準晶片的 kernel 開發 | 做這三類工程的人 | 沒有繞法，這類工作改用其他模型 |

**表下細節**

- **5.1 誤觸更少**：官方 2026-09-01 公告把「更少誤判」列為換代理由之一（媒體轉述，2026-09-07 查證）；資安領域是否同步改善，官方仍未逐項說明。
- **分類器刻意調得保守**：官方〈Improving Fable 5 Safeguards〉原文寫 deliberately tuned to be cautious，並稱 Amazon 通報的那項特定技術已擋下逾 99%。被擋的比例，官方在 2026-06-09 發布時稱不到 5% 的 session。
- **這件事對你的產品做了什麼**（政府談判換來的承諾落到你手上長什麼樣）見 [[topics/anthropic-government-policy]]「政府動作對你的產品做了什麼」；那一節也寫出你的選項。
- **機制沿革**：06-09 發布版對前沿 LLM 開發降級且不告知（System Card），06-11 官方道歉改為可見防護；07-02 隨解禁導入 Defense in Depth 分類器，首日即有合法資安審查被誤攔的公開案例。
```

四個觸發類別逐字取自 `-verified.md` 第一節第 4 列（官方 support 專文與〈Improving Fable 5 Safeguards〉）。本節同時處理 H-754509 第 (2) 點：原 L103「觸發時靜默 fallback」改寫，並補上回指政策頁的雙向連結。

## A-7. `## 使用指南`（取代 L89–97）

```
**快速上手（Claude Code）：** 用 `/model` 選 Fable；Claude Code v2.1.257 起預設就是 5.1。要指定特定版本的 model id，見官方模型總覽頁（id 會隨版本更新，本頁不抄）。

**注意事項：**
- 方案內含與 usage credits 的分界見 [[entities/pricing]]；Max 與 Team premium 為標配（週用量 50% 內），Pro 與 standard 走 usage credits。
- 前沿 LLM 開發、攻擊性資安、生物化學、模型萃取四類請求會觸發分類器，見上一節。
- 30 天資料保留政策適用於所有平台（含 AWS Bedrock），資料離開 AWS 安全邊界。
```

原 L91 的 `claude --model claude-fable-5-20260609` 是 5.0 的 id，而 [[entities/claude-code]] L175 已載「`--model` 只接受 family 名、不接受帶日期的完整 id（官方拒修）」——照抄那行讀者跑不動。**5.1 的完整 model id 本波不寫**：`-verified.md` 未取得，猜一個等於把猜測制度化。

## A-8. `## 核心功能`（改兩條，其餘留）

- L101 改寫（這是本波跨頁矛盾的一端）：
```
- **多模型協作數字（社群整理轉載，2026-07-08）**：「Fable 5 orchestrates, cheap models execute」——由 Fable 5 調度、便宜模型執行，宣稱以 46% 成本達到 96% 效能。此數字經 Reddit 整理轉載，**原始官方發布連結未見**，本站列為社群轉載而非官方基準。
```
- L103「安全分類器護欄：觸發時靜默 fallback 至 Opus 4.8」**整條移除**，事實進 A-6（那一節是它的家）。

## A-9. `## 爭議` 13 條 → 10 條（拿現有列跑一遍）

節標下加一行圖例：

```
> 🔴 現在還會遇到｜⚠️ 有爭論、官方無結論｜✅ 官方已處理
```

| 現在這一條 | 去向 |
|---|---|
| L110「靜默降級競爭 LLM 開發（已部分撤回）」 | 併入 A-6「機制沿革」，本節移除（同一事實不在同一頁出現三次）|
| L119 advisor #73365（50 則留言、100 個讚，07-10 快照）| 降為一句：`- 🔴 **Fable 5 advisor 跨全部 session 顯示 unavailable**：完整追蹤與最新互動數見 [[entities/claude-code]] 已知問題（GitHub #73365）`——數字不再抄（本頁 50／100 比家頁 87／176 舊 30 天）|
| L120 Max 誤要求購點 #79337（35→67 留言）| 降為一句：`- 🔴 **Max 方案被要求另購 usage credits 才能跑 Fable 5**：計費面見 [[entities/pricing]]、缺陷追蹤見 [[entities/claude-code]]；1M 變體引發的通用問題見 [[topics/long-context-1m]]`——數字不再抄（本頁 35→67 比家頁 76／26 舊 26 天）|
| L121「太危險」分級質疑 | 留，但刪掉「2026-07-24 日報收錄」「弱訊號」「score 恆 0」三處編輯台語言，改寫成「單一社群貼文，未附測試方法」（冷讀者外洩清單第 5 條）|
| 其餘 9 條 | 一字不動，只依 🔴 → ⚠️ → ✅ 重排 |

## A-10. `## 相關議題`（取代 L160–164，每條補分工句）

```
- [[entities/mythos]] — 同一權重的無護欄版，只開放信任機構；誰拿得到、拿去做什麼
- [[entities/pricing]] — 我的方案內含什麼、超出後怎麼算、一小時大概多少
- [[topics/model-comparison]] — 這份工作該用哪個模型（Fable 5.1 vs Opus 5 vs Sonnet 5）
- [[topics/anthropic-government-policy]] — 政府那條線會不會讓你哪天用不到、或用到被改派的版本
- [[entities/claude-code]] — Claude Code 現在有什麼毛病（Fable 相關的 issue 追蹤在這）
- [[topics/long-context-1m]] — 1M context 這個旋鈕本身的計費與可見性
```

原 L163 [[topics/anthropic-business]] 移除（IPO 與商業策略與本頁使命無關，本頁內文無任何一處指它）；新增的兩條是 A-9 兩句指路的落點。

## A-11. `## 歷史記錄` 的三處改動

1. **09-04 費馬條目（L201–208）改寫並結案**：官方原文為「a general-purpose internal research model roughly comparable to Claude Fable 5.1」。條目首句改成：
```
**費馬最後定理形式化證明（官方 2026-09-07 查證：使用內部研究模型，非 Fable 5 或 5.1）**：
```
   L203 的 ❓ 待查證標記同批移除——它問的正是「哪個模型」，官方已回答（見 B-6 的基線重建）。
2. **新增 `### 2026-06（發布與出口管制期）` 時段總結（10 行）**，取代原 L327–412 的 84 行原文：
```
### 2026-06（發布與出口管制期）

- 2026-06-09 Fable 5 發布：首款向大眾開放的 Mythos 級模型，$10／$50、1M context、128K 輸出，與 Mythos 5 共用權重、差在前置安全分類器。
- 2026-06-10～11 護欄爭議：System Card 揭露對前沿 LLM 開發降級且不告知，官方 06-11 道歉並改為可見防護。
- 2026-06-13 美國政府要求停售，Anthropic 90 分鐘內關閉全球存取（含美國用戶）。
- 2026-06-16 Commerce 部長 Lutnick 致函（Bloomberg 全文刊出）主張護欄無法阻止取得 Mythos 的網路攻擊能力；Anthropic 否認該主張在技術上成立。
- 2026-06-18 Wired 揭露 SK Telecom 的中國關聯是管制的真正起點；Amazon 安全研究員向白宮通報是直接觸發原因。
- 2026-06-22 越獄機制公開：dev.to 揭露「Fix this code」三個字即可繞過控制。
- 2026-06-30 管制解除、07-01 起全球恢復存取，同時導入 Defense in Depth 分類器。
- 雙方立場的完整論點、逐日經過與商業衝擊（DoD 轉單、G7 不豁免、赴華府協商）見下方連結；攻防的家是 [[topics/anthropic-government-policy]]。

原始條目見 [[entities/fable-5-archive#2026-06]]。
```
3. **懸置標記改短標記**（冷讀者外洩清單第 1、2 條）：剩下 5 筆（L220、L238、L246、L248、L255）改為 `❓ 待查證 ⟨Q-nn⟩`，完整標記下沉到 `### 解禁後（2026-07-01 起）` 末新增的「懸置細節」區。**短標記與定義必須成對**——`scripts/pending_markers.py:46-48` 的 `SHORT_RE`（符號＋類別詞＋`⟨Q-nn⟩` 三段相連）與 `:50-52` 的 `QDEF_RE`（定義行須 `- ⟨Q-nn⟩ ` 後緊接 ❓／🔎），由 `scripts/check_pending_markers.py:173` 雙向對帳，格式寫錯即 FAIL。

## A-12. 新頁 `wiki/entities/fable-5-archive.md`（裁決點 1）

```
# Claude Fable 5 — 原始條目封存

**類型：** model
**狀態：** resolved（封存頁）
**領域：** 🤖 模型
**上層：** [[entities/fable-5]]
**首次出現：** 2026-06-09
**最後更新：** <實作日>
**最後新聞更新：** 2026-06-29

> 本頁是 [[entities/fable-5]] 的原始條目封存，現在還成立的答案（哪一代、能不能用、護欄會不會擋你）都在主頁。

## 出口管制：雙方立場（2026-06 定格）
<原 L125–155 一字不動照搬>

## 配額與計費過渡（原訂 7/7，2026-07-19 到期）
<原 L71–85 一字不動照搬>

## 2026-06
<原 L329–412 一字不動照搬，原有的兩個中間分節保留為 h3>
```

`status` 必須逐字是 `resolved（封存頁）`、必須有 `**上層：**`、領域繼承母頁——三者由 `scripts/check_hierarchy.py:123-129` 驗；不補 index 列，跑 `python scripts/gen_wiki_frontmatter.py` 會投影成母頁列的「↳ 子故事：」。母頁 callout 日期 09-01 ≥ archive 的 06-29，`check_hierarchy.py:136-138` 的「hub 不落後」通過。

## A-13. 給主編的文字（index 與 feature-radar，本波不由實作者改）

- **index Entities 表 L76 摘要格**（現為 68 天未動、內容已被推翻的「7/7 前享 50% 配額，7/7 後 usage-based billing」）：
```
Claude Fable 5 與 5.1：現行旗艦是 5.1（09-01 GA），5 轉 Legacy、退役不早於 2027-06-09；兩代同價 $10/$50，護欄擋到什麼、被擋時你會不會知道
```
- **index 💻 開發實務入口新增一列**（冷讀者：前 45 行零列指向本頁）：
```
| 我要不要換到新的旗艦、舊的會不會停掉（Fable 5 vs 5.1、退役日、護欄會不會擋我） | [[entities/fable-5]]「你現在拿到的是什麼」 |
```
- **feature-radar L62**（「Max/Team 動向未明」已被 pricing L74 的 2026-08-08 官方查證推翻）：
```
> Fable 免費期限（原訂 7/19）已到期並移出本表；現在是常態分流：Max 與 Team premium 為標配（週用量 50% 內），Pro 與 standard 走 usage credits，5 與 5.1 同規則，詳見 [[entities/pricing]]。
```
- **feature-radar L181**（Fable 5.0 那列的狀態欄仍寫「7/7 前 50% 配額」）：狀態欄改 `正式發布（Legacy，退役不早於 2027-06-09；現行世代見 Fable 5.1 那一列）`。

---

# B. 進規則檔與帳本

## B-1. `.claude/rules/wiki-ingest-models.md` 負責頁面表（現 :11）

```
| `wiki/entities/fable-5.md` | Fable 5／5.1 世代動態、護欄與分類器行為、Legacy 與退役時程。**出口管制的政策面不在本頁**（家是 [[topics/anthropic-government-policy]]，屬安全政策線），本頁只在現況留一句指路 |
```

## B-2. `.claude/rules/wiki-ingest-models.md` 新增節（接在 J 條之後）

```
## entities/fable-5 的三張表 `[加入: 2026-09-07]`

本頁回答「Fable 這一代模型本身是什麼、護欄會怎麼改寫你送進去的請求，以及它一路走過來的事」。`## 歷史記錄` 是逐則原文，上方三張表是結論。

### fable-5 的 `## 你現在拿到的是什麼`（覆寫式，7 列固定不增減）

四欄固定：`這一格｜Fable 5（Legacy）｜Fable 5.1（現行）｜官方出處（查證日）`。七列固定為：現在誰是預設／牌價／快取讀取／知識截止／會不會停掉／官方推薦拿它做什麼／我的方案能不能用。**判準句（三條全過才留在表上）：** ① 這一格兩代給得出具體值，寫不出值就不佔列；② 值有官方一手出處與查證日，媒體轉述只能寫進表下細節；③ 「我的方案能不能用」一列只寫分界，金額與計費細節指 [[entities/pricing]]，不複製。**列不新增也不移除**——世代換代時整表重判並加一欄新世代；某一代退役當日整欄**移除**，結論降為表下一句。表上方必標「資料截至 YYYY-MM-DD」，距今逾 60 天由主編重查官方模型頁。牌價、快取費率、退役日**由主編查證官方模型總覽頁後填**，記者無 web 工具不得自填。

### fable-5 的 `## 護欄會怎麼改寫你的請求`（覆寫式，四類固定）

四欄固定：`會踩到的類別｜具體是什麼｜誰最容易誤觸｜你能先做什麼`。四列即官方公布的四個觸發類別（cybersecurity／biology and chemistry／distillation／窄範圍 frontier LLM development）。官方改變分類器行為即**覆寫**對應格並更新查證日；官方拿掉某一類即**移除**該列，結論留表下細節。**新增列的唯一入口是官方公布新的觸發類別**——社群回報的誤判案例只能更新「誰最容易誤觸」欄，不得新增列、不得改寫「你能先做什麼」。政策後果（政府談判換來的承諾、你的選項）的家是 [[topics/anthropic-government-policy]]「政府動作對你的產品做了什麼」，本節只寫模型面機制並互指，不複製。

### fable-5 的 `## 熱度與試用價值`：同步對象是 feature-radar 全覽表現行世代那一列

radar 全覽表同時有 Fable 5 與 Fable 5.1 兩列時，本表對照的一律是**現行世代**那一列（2026-09-07 起為 Fable 5.1），不一致時以 radar 為準**覆寫**本表並更新判定日；舊世代那一列的熱度不同步過來。

### fable-5 的 `## 爭議`（上限 10 條）

**判準句（兩條全過才留）：** ① 它是對這個模型本身的爭議，不是 Claude Code 的缺陷或計費事故——後兩者的家是 [[entities/claude-code]] 與 [[entities/pricing]]，本節只留一句指路且**不抄互動數字**（抄了必然比家頁舊）；② 寫得出它現在還成不成立。狀態三值 🔴 現在還會遇到／⚠️ 有爭論、官方無結論／✅ 官方已處理，圖例一行固定放節標下、不重寫。排序 🔴 → ⚠️ → ✅。官方給出結果後改標 ✅，再滿 90 天無新事實即**移除**該條，結論併進對應的表或節。

### fable-5 的封存

照 `.claude/rules/wiki-ingest-format.md`「時段蒸餾與封存（全站通用）」，archive 子頁為 `entities/fable-5-archive`，對象為 `## 歷史記錄` 的 `#### YYYY-MM-DD` 條目（以月為時段）。**2026-06 一個時段已於 2026-09-07 封存**（同批另有兩處死案歸檔：出口管制雙方立場兩張表、配額與計費過渡整節）；2026-07 於 2026-10 起達門檻。
```

**實測**：把上面三個 h3 餵進 `scripts/table_census.py` 的 `_mechanism()`（`page_slug="entities/fable-5"`），三張表全回「有」，對照組「現況」回「無」。h3 逐字含 slug `fable-5` 是必要條件（`table_census.py:57-68`）。

## B-3. `.claude/rules/wiki-ingest-models.md` C 條末加一句

```
**同一個數字在本記者的多頁出現時，訊號強度以最保守的一方為準** `[加入: 2026-09-07]`：某頁自承「社群整理轉載、原始官方連結未見」，另一頁就不得寫成「官方基準」。發現落差時，先把最保守的說法寫進這個數字自己的家那一頁，其餘頁面於下一次更新該表時同步。
```

## B-4. `.claude/rules/wiki-ingest-features.md`「熱度降溫」的「同步」那一條，末加一句

```
entities 頁的熱度表對照的是 radar 全覽表**現行世代**那一列；同一產品線有新舊兩列時（如 Fable 5 與 Fable 5.1），舊列的熱度不同步到 entities 頁。
```

> 改完 `.claude/rules/*.md` 後照 `.claude/rules/claude-md-edit.md` 跑 `/review-commands` 到零錯誤。

## B-5. 帳本（`scripts/pending_handoffs.py`，不手改檔案）

```
python scripts/pending_handoffs.py close H-754509 --by 模型 --result "本頁四處已處理：L48 與 L327 節標隨 2026-06 封存與現況改寫消失、L303 端點改為 06-30 解除／07-01 恢復、L103 靜默 fallback 依官方原文改寫並補回指政策頁。跨頁殘留分兩路：mythos／opus-4-8 屬同一維護者的其他頁，列 09-14 回訪；tom-brown 另開帳本"
python scripts/pending_handoffs.py open --from 模型 --to 人物 --page entities/tom-brown --note "L42／L67「封鎖期共 18-19 天」的端點口徑：家是 topics/anthropic-government-policy（06-30 解除、07-01 恢復），請改為指路或照該頁口徑改寫"
python scripts/pending_handoffs.py open --from 模型 --to 社群 --page topics/community-tech-patterns --note "「46% 成本達 96% 效能」在 patterns L892-896 與 community-pattern-trends L162／L171 寫成官方基準，但該數字的家 entities/fable-5 自承是 Reddit 整理轉載、原始官方發布連結未見（2026-09-07 定為社群轉載）。請把兩頁的來源等級改成社群轉載"
```

## B-6. 兩支腳本的存量檔（實作者同批處理，不然閘會紅）

- **`data/reader-language-allow.json` 加一筆**（**已實測**：不加則 archive 頁新增 2 筆 FAIL，加了之後歸零）：
```json
{"page": "entities/fable-5-archive", "term": "記者", "line_contains": "記者會", "reason": "「首爾記者會」指真實新聞發布會，非編輯部角色詞（隨 2026-06 條目自 entities/fable-5 搬入，原頁已有同型例外）"}
```
- **懸置標記基線**：費馬那筆結案後全庫由 142 降為 141，同批跑
```
python scripts/check_pending_markers.py --rebuild-count --reason "entities/fable-5 費馬歸屬經官方一手查證結案（內部研究模型，非 Fable 5／5.1）"
```
  若 A-11 第 3 點的 5 筆短標記化先落地（每筆各多一個標記），總數會回到 146、不會觸發 FAIL；**但仍要跑 rebuild**，否則基線與實況永久對不上。
