# Anthropic 訂閱方案與計費政策

**類型：** policy
**狀態：** active（持續調整中）
**最後更新：** 2026-04-30

---

## 現行方案（2026-04）

| 方案 | 月費 | Claude Code 模型存取 |
|------|------|----------------------|
| Free | $0 | 基本限制 |
| Pro | $20 | 含 Sonnet；Opus 需另購額外用量 |
| Max | 更高 | 更高用量上限 |
| API | 按量計費 | 全模型，依 token 計費 |

> **注意**：以上為社群整理的近似資訊，確切定價請以官方頁面為準。

---

## 近期政策變動

### 2026-04-30：ANTHROPIC_API_KEY 雲端環境計費陷阱
使用者警告：若在雲端環境設置 `ANTHROPIC_API_KEY` 環境變數，Claude Code 無法正常運作，且**所有 Code 呼叫將自動改走 API 計費通道**，造成大量意外費用；官方文件存在誤導，過去已有多起「Extra Usage 異常暴增」與此相關。**立即檢查**：雲端環境（CI/CD、Docker、K8s）若有此環境變數應立即移除或改用 Secrets Manager 管理。

### 2026-04-30：Pro 訂閱到期 Extra Usage 餘額消失
使用者 Claude Pro 訂閱到期後，預付的 **$40 Extra Usage 餘額隨之歸零**消失，Anthropic 文件未明確說明訂閱終止後的餘額處置規則，UI 中也不存在退款流程。

### 2026-04-30：長 context 快取隱性成本
使用者分析本機 JSONL 日誌發現，Claude Code 用量暴增源自超大 prompt cache（**約 475k tokens**）的反覆重建；以公開 API 定價估算，單次快取重建成本相當可觀。長 context 工作流使用者應定期監控 JSONL 日誌，警惕快取失效觸發的非預期費用。

### 2026-04-29：Anthropic 洽談 $900B 估值新一輪融資
Bloomberg 與 CNBC 同日報導，Anthropic 正與投資人洽談以超過 **$9,000 億美元**估值進行新一輪融資，估值超越 OpenAI，是目前 AI 新創史上最高估值之一。

### 2026-04-29：Claude Code Token 費用預估翻倍
Business Insider 報導，Anthropic 低調將工程師使用 Claude Code 的**預期 Token 費用估算值調高一倍**（靜默修訂，無官方公告）。企業在規劃 AI 工具採購預算時需重新評估實際成本，大規模部署情境下的費用控管壓力加劇。

### 2026-04-29：Max 方案 API 錯誤與支援失靈
Max 方案用戶在 GitHub issue 投訴 Claude Code 出現內部 API 錯誤，且 Anthropic 支援 AI 持續建議排查 VPN 問題而無法識別實際故障，引發對高價訂閱服務可靠性與支援品質的強烈質疑。

### 2026-04-28：Anthropic 估值突破 $1 兆美元（鏈上數據）
鏈上 pre-IPO 交易數據顯示 Anthropic 隱含估值已達 **$1 兆美元**；機構市場估值約 $800–900B。分析師提醒此為特定投機性市場情緒，不代表正式融資估值，但趨勢方向具參考性。

### 2026-04-28：Opus 「圍牆內圍牆」付費事件（已修正）
Anthropic 在**未事先公告**的情況下，要求 Pro 用戶（$20/月）在 Claude Code 中使用 Opus 須另購「Extra Usage」，引發強烈社群反彈。事後 Anthropic 澄清 **Pro 用戶仍可存取 Opus**，事件得以平息，但溝通方式已造成信任損失。此為近一個月內第二次 Opus 存取政策變動（見 2026-04-24 條目）。

### 2026-04-28：20x 方案使用量計量異常
部分升級至 20x 計畫的用戶回報週末起使用量計量出現**異常跳動**，未執行密集任務一小時內即達 70%，數值隨後又無故下降，疑為計量 bug 或後端流量計算異常，目前無官方說明。

### 2026-04-28：Auto Compact 失效導致 session 鎖死
用戶遭遇 context window 滿載後 Auto Compact 未自動觸發，手動 `/compact` 亦失效，即使重購額外用量並重啟工具仍無法解決。此問題使已付費用量在技術層面無法使用。

### 2026-04-27：Max 方案配額多工場景不足
同時使用 Claude Code 與視覺功能的用戶回報早上 **8:30 即觸及當日用量上限**，反映 Max 方案在 Code + vision 多工場景下的配額設計存在實際痛點。

### 2026-04-27：Google 400 億投資對定價的指標意義
Google 確認對 Anthropic 追加 400 億美元投資，分析師指出 Anthropic 具備更充裕資本空間維持現有定價或推進企業方案擴張，對長期訂閱定價策略具有指標意義。見 [[topics/google-investment]]

### 2026-04-25：HERMES.md 靜默計費 bug
git commit 歷史中出現大寫字串「HERMES.md」，會觸發 Claude Code 靜默切換至 API 額外計費模式，完全繞過 Max 方案配額，已知造成用戶單日損失 **$200**。Anthropic 支援確認為 bug，但**拒絕退款**。

**立即行動**：`git log --all | grep -i HERMES` 檢查 commit 歷史。
來源：[GitHub Issue #53262](https://github.com/anthropics/claude-code/issues/53262)、[[news/2026-04-26]]

### 2026-04-25：Token 配額快速耗盡（$20 方案）
$20 Pro 方案用戶反映 Claude Code 在 **2 小時內耗盡每日配額**；使用 career-ops 等大型工具最快 30 分鐘見底。社群分享節省 token 的實務技巧（分層模型策略：以 Sonnet 為主力，需要時才讓 Sonnet「諮詢」Opus，聲稱節省約 60% 用量）。

### 2026-04-25：Anthropic 限制 OpenClaw 等第三方 agentic 工具配額
The Verge 報導 Anthropic 嚴格限制 OpenClaw 等第三方 agent 工具的使用配額。Claude Code 負責人 Boris Cherny 公開表示：「訂閱方案的設計並非為這類第三方使用模式而生。」預示 agentic 工具的付費門檻將持續提高。

### 2026-04-24：Opus 額外用量需 Pro 起
Anthropic 更新政策，使用 Claude Code 存取 Opus 模型的**額外用量**現在須先訂閱 Pro 以上方案才能開通。官方說明了三種切換模型的方式：
1. `/model` 指令
2. `--model` CLI 旗標
3. 環境變數設定

**影響**：原本以低階方案搭配額外用量的用戶受到顯著影響。

### 2026-04-24：降級後用量不重置
一名用戶回報在 Anthropic 發布重置用量承諾的六天前降級帳號，導致被排除在重置範圍外。Anthropic 拒絕為其重置，引發補償政策時間邊界的爭議。

---

## 宏觀趨勢

The Verge（2026-04-24）報導，AI 商業化壓力下，Anthropic 等實驗室開始大幅限制第三方工具用量。Claude Code 負責人 Boris Cherny 公開表示：

> 「訂閱方案的設計並非為這類第三方使用模式而生。」

此言論被視為付費門檻將持續提高的明確信號。

---

## Token 成本注意事項

- 多個 MCP Server 併用時，每條訊息可能消耗 **20,000+ tokens**（見 [[entities/claude-code]]）
- 切換至 Opus 4.7 會清除整個 prompt cache，導致額外 token 成本

---

## 相關議題

- [[topics/code-quality-decline]]（用戶因品質下滑要求退款或降級）

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-26]]
- [[news/2026-04-27]]
- [[news/2026-04-28]]
- [[news/2026-04-29]]
- [[news/2026-04-30]]
- [官方說明文件](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
