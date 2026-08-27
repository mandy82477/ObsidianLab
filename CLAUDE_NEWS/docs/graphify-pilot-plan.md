# Graphify 試點計畫（ELI5 版）

**建立：** 2026-08-27 ｜ **狀態：** 規劃中，待執行 ｜ **負責：** Claude session（本地手動執行）

---

## 一、這是什麼？（像五歲小孩一樣解釋）

想像 wiki 是一座有 **55 本書** 的小圖書館。

現在你想找「哪些書講到成本」，做法是**一本一本翻**（grep 關鍵字）。翻得到，但很慢，而且每翻一本都要花力氣（token）。更麻煩的是：有些書之間有看不見的關係——A 書提到 B 書、B 書提到 C 書——用翻的永遠看不出這條鏈。

**Graphify 做的事：幫圖書館畫一張地圖。**

它把每本書變成地圖上的一個點，把書裡的 `[[wikilink]]`（「詳見某某頁」）變成點跟點之間的線。畫完之後：

- 想知道「哪些書跟成本有關」→ **看地圖**，不用翻書
- 想知道「pricing 這本書跟社群模式那本書有什麼關係」→ 地圖幫你**找出中間經過哪幾本書**
- 想知道「這座圖書館的書自然分成幾群」→ 地圖自動**圈出朋友圈**（社群偵測）

最棒的是：畫地圖**不需要 LLM API**。它用確定性解析（tree-sitter）讀 Markdown，完全本地跑、完全免費——符合本專案「沒有 `ANTHROPIC_API_KEY` 也要能動」的鐵則。

---

## 二、為什麼要做？

| 現在的痛 | 地圖能不能治 |
|---|---|
| **查詢**：記者/主編找「哪些頁引用 X」要全庫 grep，大頁還要分段讀，費 token | ✅ 能治。圖查詢一次到位，這是試點主目標 |
| **分類**：日報條目分六類全靠主編 LLM 判斷，分得對不對沒有第二意見 | ⚠️ 只能治一半。**誠實說**：新新聞剛進來時還沒有任何 wikilink，地圖上根本沒有它，所以 Graphify **不能**幫忙分類新條目。它能做的是**事後健檢**——看已寫好的 wiki 頁自然聚成的「朋友圈」跟我們的六領域分類（🤖模型/🛠️功能/💼商業/🏛️政策/🌐社群/👤人物）合不合。合＝分類標準健康；某頁被圈進意外的群＝分類或 wikilink 有缺漏的訊號 |

> 信任層驗證已完成（2026-08-27）：repo 活躍（Apache-2.0/MIT 雙授權）、PyPI 官方套件為 `graphifyy`（刻意雙 y，README 自己警告仿冒套件）、最新版 0.9.50（2026-08-25），repo 與套件互相指認一致。

---

## 三、試點四步驟（預計 1 小時內）

### Step 0：安裝（5 分鐘）

```bash
uv tool install graphifyy
graphify --version
```

- 套件名是 **`graphifyy`（雙 y）**，指令是 `graphify`。裝到單 y 的就是仿冒品，馬上移除
- Windows 環境；若 `uv` 不在，先 `pip install uv`

### Step 1：對 wiki 建圖（10 分鐘）

```bash
cd C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
graphify wiki/ --output data/graph/
```

產物三件套：`graph.json`（可查詢）、`graph.html`（互動地圖）、`GRAPH_REPORT.md`（重點摘要）。

**硬規則：**
- 產物一律放 `data/graph/`，並加進 `.gitignore`——**絕不**混進 `wiki/`（wiki 只放知識頁）
- 只餵 `wiki/`，不餵 `news/`（日報 800+ 檔會把圖淹掉，且日報是唯讀原料不是知識層）

### Step 2：三道真題驗收（20 分鐘）

拿記者/主編**實際會問的問題**考它，每題同時用舊方法（grep）做一次，比較答案品質與 token 成本：

| # | 考題 | 舊方法 | 過關標準 |
|---|---|---|---|
| 1 | `graphify query "成本相關的頁面有哪些"` | grep「成本/token/計費」再逐頁確認 | 找齊 pricing、enterprise-cost-management、official-community-gap 成本列等，無重大遺漏 |
| 2 | `graphify path entities/pricing topics/community-tech-patterns` | 人腦想＋grep 驗證 | 給出合理的中介頁鏈（例如經過 official-community-gap） |
| 3 | `graphify explain feature-radar` | 讀 index.md ＋ grep 反向連結 | 正確列出主要引用方（各 entities 頁、model-comparison 等） |

### Step 3：分類健檢（15 分鐘）

看 `GRAPH_REPORT.md` 的社群偵測（Leiden 演算法，不用 LLM）結果：

1. 它圈出的「朋友圈」數量與成員，跟 `wiki/index.md` 的六領域對照
2. 逐一記下「被圈錯群」的頁——每一個都是訊號：要嘛該頁 wikilink 太少（孤島），要嘛它的領域標錯了
3. 結果寫進本文件末尾的「試點結果」節

---

## 四、怎麼算成功？

三項全過才算「值得留下」：

1. **查得到**：三道真題至少 2 題答案品質 ≥ grep，且不需要人工二次過濾
2. **省得多**：單次查詢的 token 成本明顯低於 grep + 分段讀大頁（估計：grep 路徑常要讀數百行，圖查詢應在數十行內）
3. **圈得準**：Leiden 朋友圈跟六領域大致吻合（允許少數例外，例外本身要有解釋價值）

## 五、成功之後 / 失敗之後

**成功 →** 三件事，各自登記後才算閉環：
1. 把 `graphify` 的 MCP server（`python -m graphify.serve data/graph/graph.json`）評估接給記者當查詢工具（另立計畫，不在本試點內）
2. `wiki/CLAUDE.md` 搜尋策略加一條「圖查詢」路徑（改規則檔 → 跑 `/review-commands`）
3. 決定圖的重建節奏（wiki 每天在變，圖會過期）：先手動、觀察一週再決定要不要掛進 pipeline

**失敗 →** `uv tool uninstall graphifyy`、刪 `data/graph/`、在 `wiki/log.md` append 一筆試點結論（含失敗原因），不留殘骸。

## 六、風險與邊界（先想好才動手）

| 風險 | 對策 |
|---|---|
| 圖會過期（wiki 天天變） | 試點期手動重建；只有證明價值後才考慮自動化 |
| 產物污染 repo | `data/graph/` + `.gitignore`，第一步就做 |
| 誤以為它能分類新新聞 | 本文件第二節已明寫：不能。分類仍是主編 LLM 的工作 |
| 工具本身跑不動（Windows 相容性） | Step 0 裝不起來或 Step 1 建不出圖 → 直接走「失敗之後」流程，不硬修 |
| 供應鏈風險 | 已做信任層驗證；只裝官方雙 y 套件；本地執行不出網 |

## 七、成本

- **金錢：** $0（本地、開源、零 API）
- **時間：** 約 1 小時（四步驟合計）
- **Token：** 只有驗收比對時的少量讀取；建圖本身零 LLM

---

## 試點結果（執行後回填）

_（待執行）_
