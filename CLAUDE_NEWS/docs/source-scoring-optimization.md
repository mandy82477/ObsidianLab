# 來源挑選優化機制（Source Scoring & Selection）

**受眾**：想了解本專案來源品質機制的工程師
**建立**：2026-07-16 ｜ **狀態**：Phase 0–1 已上線（監控），Phase 2 待資料累積
**相關檔案**：`data/source_registry.json`、`scripts/source_scorecard.py`、`data/external/domain_pc1.csv`

---

## 1. 問題定義

本專案有 10 個活躍來源，橫跨三種性質：官方源（Anthropic Blog/Status、API Release Notes）、社群平台（HN、Reddit、GitHub Issues、dev.to）、媒體聚合（Google News）。過去的品質挑選停在**條目層**：每個來源一套手工特例門檻（HN ≥30 分、Reddit 看週熱門標記、dev.to 改內容判斷…），每次發現某來源指標失真才補一條規則——被動、越疊越多、永遠是踩坑後才修。

缺的是**來源層的回饋迴路**：沒有任何機制回答「這個來源餵進來的東西，最後有多少真的有用？」

## 2. 核心設計決策（與研究依據）

### 2.1 兩層模型：平台層 vs domain 層

學術文獻的關鍵洞察：聚合器的「來源」其實是兩層——

- **平台層**（HN、Reddit、GitHub）：平台本身沒有「可靠度」，可靠度在貼文/帳號層級。外部評級體系（NewsGuard、MBFC）全部評不了平台，**只能靠自家 funnel + attribution 資料算**。
- **domain 層**（Google News 抓回的 publisher、blogroll 的部落格）：有現成的學術評級資料可查表。

### 2.2 平台層：engagement 當排序訊號可以，當品質分數不行

三篇實證研究劃出了 engagement 訊號的使用邊界：

| 結論 | 出處 | 落地方式 |
|------|------|---------|
| HN 分數與內在品質相關性不錯（在已獲基本注意的文章中） | Stoddard, WWW 2015 ([arXiv 1501.07860](https://arxiv.org/abs/1501.07860)) | HN 保留 `score` 門檻機制 |
| 分數絕對值受 herding 膨脹 ~25%（先行正評放大後續投票） | Muchnik et al., Science 2013 | **序位可信、絕對值不可信**：門檻只在來源內比較，永不跨平台比絕對值 |
| GitHub star 可大規模造假（600 萬可疑 star）且與工程品質無相關 | [arXiv 2412.13459](https://arxiv.org/abs/2412.13459)、[arXiv 1606.04984](https://arxiv.org/abs/1606.04984) | GitHub 標 `untrusted`，改看 issue 討論深度與跨來源共現 |

**跨來源共現（`source_count`）是有理論支撐的一級訊號**：idiap 的圖傳播研究（NAACL 2024）與 MediaRank（KDD 2019）都證明「被多個獨立節點共同報導」可以傳播出可靠度。本專案 dedup 產生的 `source_count > 1` 加權，在文獻裡站得住。

### 2.3 domain 層：直接查表，不要自己算

採用 **Lin et al. (2023, PNAS Nexus)** 的聚合評級（[domain-quality-ratings](https://github.com/hauselin/domain-quality-ratings)）：11,520 個 domain，六套專家評級（NewsGuard、MBFC、Ad Fontes 等）經 imputation + PCA 合成單一 `pc1` 分數（0–1）。選它而非 idiap 的理由：覆蓋最廣、有 peer-review 驗證（六套評級間 Spearman 最高 0.90）、單檔 CSV 零依賴。

- 檔案：`data/external/domain_pc1.csv`（403KB，CC 引用要求見 §6）
- 查表規則：host 全名 → 逐層剝 subdomain → 查無則 **記「未知」不記「低分」**（長尾 domain 缺評級是常態，不可懲罰新興垂直媒體）
- 只用於 Google News（唯一 domain 開放、無互動分數的來源）；平台 domain（reddit.com 等）本就不在表內

### 2.4 小樣本平滑：假票 + Wilson 下界

日流量低的來源（lobste.rs、Anthropic Blog）幾天內的命中率是雜訊。兩個標準解並用：

- **Bayesian 假票平滑**（顯示用主指標）：`rate = (成功 + k·p₀) / (總數 + k)`，先驗 p₀ = 全站基準率，k = 20（收錄率）/ 10（wiki 率）。小樣本被拉向全站平均，大樣本自然掙脫先驗。
- **Wilson score 95% 下界**（排序/汰換參考）：小樣本的下界自動壓低——「2 抓 1 中」的下界只有 ~9%，防止一次好運登頂。公式見 [Evan Miller](https://www.evanmiller.org/how-not-to-sort-by-average-rating.html)。

### 2.5 監控先於自動化（Phase 邊界的理由）

生態掃描的共識：SeanLF（同類專案中設計最完整者）把品質控制放在「入口白名單＋出口透明＋事後儀表板」，**刻意不讓分數自動回饋選稿**；Feedly 是唯一自動閉環，但靠海量用戶行為支撐。本專案資料量（funnel 自 2026-07-11 起）遠不足以支撐自動決策，因此：

- **Phase 1（已上線）＝純監控**：記分卡每週產出，數字不影響 pipeline 任何行為
- **Phase 2（門檻：≥ 60 天資料）＝enforcement**：任何會改變收錄結果的變更（門檻調整、來源汰換、farm 黑名單下放到 fetcher）都必須走 `/pipeline-change-check` 前後對照

## 3. 逐來源機制表

`data/source_registry.json` 是單一真相源，欄位語意：

- **score_reliability**：`trusted`＝互動分數可作門檻訊號 / `untrusted`＝分數失真（造假、恆 0、反指標）/ `none`＝天生無分數
- **curation_mode**：`score`＝來源內分數門檻 / `content`＝逐條內容判斷 / `whitelist`＝策展名單收錄即過

| 來源 | 分數可信度 | 挑選機制 | 為什麼 |
|------|-----------|---------|--------|
| Anthropic Blog / Status / API Release Notes | none | whitelist | 官方一手源，價值在存在本身，無分數可用 |
| Hacker News | trusted | score（來源端 min_score + wiki 端門檻表） | 唯一有實證支持「分數≈品質」的平台（§2.2），但只用序位不用絕對值 |
| GitHub Issues | trusted | score（留言數） | 留言數反映討論深度，難造假 |
| GitHub（releases + repo 搜尋） | **untrusted** | content | star 可造假且與品質無關（§2.2）；releases 部分本質是官方 changelog |
| Reddit | **untrusted** | content ＋「· 週熱門」標記 | 匿名 RSS score 恆 0（非真實低互動）；OAuth 真解上線後可升 trusted（見 workaround 登記表） |
| dev.to | **untrusted** | content | 實測讚數為**反指標**（第一手實作文 2–3 讚、SEO 農場文 5–6 讚，2026-07-10 教訓） |
| Google News | none | content ＋ **domain 信譽先驗**（§2.3） | 無互動分數、publisher 長尾雜，是唯一適用外部評級查表的來源 |
| Blogroll | none | whitelist ＋ probation 生命週期 | 人工策展名單；30 天 probation 期滿看記分卡決定去留（`blogroll.json` status 欄） |
| lobste.rs | trusted | whitelist（收錄即算） | 量少質精；fetcher 存在但目前未註冊（registry 標 `active: false`） |

**設計原則**：某來源再踩到「分數失真」坑時，改 registry 一個欄位值，而不是在規則檔加第 N 條特例。

## 4. 記分卡指標定義

`python scripts/source_scorecard.py`（純標準庫、零 LLM、確定性），每週隨 `/wiki-lint` 6e 執行：

| 指標 | 公式 | 回答的問題 |
|------|------|-----------|
| 收錄率* | smoothed(emitted / gathered) | 這來源的雜訊多不多（過濾成本） |
| Wilson 下界 | wilson_lower(emitted, gathered) | 小樣本修正後，收錄率「至少」多少（汰換排序用） |
| wiki 率* | smoothed(wiki 歸因 / emitted) | 進了日報的條目有多少真正沉澱進知識庫（最強的長期價值訊號） |
| Presence | wiki 歸因占全站比例 | 這來源對最終產出的絕對貢獻（Techmeme 式，保護高產出來源不被比率指標冤枉） |
| HHI | Σ Presence² | 全站是否過度依賴少數來源（> 0.25 高度集中） |
| domain 信譽分佈 | Google News 歸因條目的 pc1 分桶 | 媒體條目的信譽組成（低信譽持續出現→人工覆核） |

**收錄率與 Presence 必須並列看**：收錄率懲罰高產出來源（Google News 抓 158 收 91 的比率必然難看），Presence 補償絕對貢獻——一個看效率、一個看產量，合併會互相抵銷資訊。

**樣本閘門**：< 14 天或 < 30 條抓取的來源標 ⚠️，數字僅供趨勢觀察，不得作為汰換依據。

資料來源與 join：`source_funnel.jsonl`（以註冊名為 key，同日多筆取 gathered 最大者）× `source_attribution.jsonl`（以 slug 為 key），經 registry 的 name↔slug 對照 join；attribution 出現未註冊 slug 時記分卡會列「⚠️ 未註冊 slug」提醒修 registry 或記者回報。

## 5. 首次實測基線（2026-07-16，6 天樣本，僅供示意）

- 全站：抓取 522 → 收錄 317（61%）→ wiki 歸因 133（42%）
- HHI 0.265（高度集中，Google News 一家占 Presence 42%）
- Google News 歸因條目 domain 信譽：高 41 / 中 8 / 低 0 / 未知 7 —— 現行規則過濾後的媒體條目信譽組成健康
- GitHub Issues 的 wiki 率（67%）全站最高：進日報的 issue 幾乎都進了 wiki——功能記者的已知問題追蹤是最穩定的價值管道
- 所有來源皆 ⚠️ 樣本不足：以上讀趨勢，不做決策

## 6. 外部資料維護

`data/external/domain_pc1.csv` 來自 [hauselin/domain-quality-ratings](https://github.com/hauselin/domain-quality-ratings)，引用：Lin, H. et al. (2023). *High level of correspondence across different news domain quality rating sets.* PNAS Nexus, 2(9). [doi:10.1093/pnasnexus/pgad286](https://doi.org/10.1093/pnasnexus/pgad286)。

底層評級多為 2022–2023 快照：老牌媒體分數穩定，2023 後新站查無資料（落「未知」桶，無害）。**每季複查**：未知桶占比若持續 > 30%，重新下載上游或評估補充資料集（idiap [News-Media-Reliability](https://github.com/idiap/News-Media-Reliability)、[Iffy Index](https://iffy.news/index/) 黑名單）。已登記於 `docs/workaround-register.md`。

## 7. Phase 2 路線圖（門檻：≥ 60 天資料，全部需 `/pipeline-change-check`）

| 項目 | 內容 | 前置 |
|------|------|------|
| 汰換迴路 | Wilson 下界 + Presence 雙低且出試用期的來源 → weekly-review 出「建議降級/移除」清單，人工確認 | 60 天資料 |
| EWMA 漂移偵測 | 對日收錄率跑 EWMA（半衰期 30 天），偵測「來源最近變爛」而非累積平均 | 60 天資料 |
| percentile 自動門檻 | 互動門檻對照表改為「該來源近 180 天分數分佈的 P80/P50/P25」，特例條文退役 | 180 天分數分佈累積 |
| farm 黑名單下放 | dev.to 農場帳號黑名單從規則檔文字下放到 fetcher（改變收錄結果，故屬 Phase 2） | pipeline-change-check |
| domain 先驗參與過濾 | pc1 < 0.4 的 Google News 條目降權或標記（目前僅監控分佈） | 低信譽桶有實際出現再議 |
| LLM 質性評分卡（可選） | 每月一次，仿 NewsGuard pass/fail checklist（第一手占比、農場率、可驗證性），派 sonnet 在 session 內執行 | 量化分先跑穩 |
