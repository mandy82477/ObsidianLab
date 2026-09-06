# 主編官方查證 — topics/ai-agent-safety（2026-09-06）

記者與 agent 無 web 工具；本檔對照「頁面 vs 官方現況」。逐條附出處。

## 一、四件硬事實（讀者考題的錨）

| 事 | 官方／一手現況 | 對頁面的意義 |
|---|---|---|
| **Auto Mode 提示注入 60–80% vs 官方 0%**（頁面 L120 節） | embracethered（Johann Rehberger）原文：網頁摘要請求即可劫持 Opus 5 Auto Mode 達 RCE，`struct.py` 遮蔽標準庫；**Anthropic 把揭露結案為 informative，定性 Auto Mode 是「best-effort convenience control，不是 security boundary」**（[原文](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/)）。官方 blog 稱 Auto Mode 擋下 89% 危險指令（gbhackers 轉述） | Q1 的答案不是「修了沒」而是**官方立場：Auto Mode 不承諾當安全邊界**；頁面若寫「待官方回應」要改成這句 |
| **Enterprise Frontier Safeguards**（頁面 L112 節） | [官方公告 2026-09-01](https://www.anthropic.com/news/enterprise-frontier-safeguards)：監看「offensive cyber／biological capability 開發、憑證外洩跡象」；資料存客戶自己的 S3／Azure Blob／GCS、客戶金鑰；**今年秋季起分階段推出**，推出前符合資格者對 Fable 5／5.1 先給零資料留存；**免費**（雲端儲存另計）；適用 Claude Code、Enterprise、Claude Platform、Bedrock、Claude Platform on AWS、Google Agent Platform、Foundry | Q3「EFS 擋什麼不擋什麼」：擋兩類濫用＋憑證外洩，**不是提示注入防禦**；頁面日期 09-02 應改 09-01；「零資料留存」是過渡措施非 EFS 本體 |
| **infostealer 劫持 session**（頁面 L129 節、L63 表列） | 多家引官方通知（BleepingComputer、SecurityWeek、Help Net Security 08-31）：Anthropic 08-30 起通知受影響用戶；惡意軟體家族 Vidar、LummaC2、StealC、RedLine、Acreed、AMOS；竊 session cookie 繞過 MFA 消耗付費額度；**官方處置＝強制登出、移除已存付款方式、退款未授權扣款**；**平台未被入侵** | Q4「帳號被劫持是真的嗎、怎麼防」：真的，但是用戶端惡意軟體；防法＝別裝來路不明軟體、被登出後重加付款方式。頁面 L63 若標「待查證」可結案 |
| **Anthropic 官方 postmortem 三大原因**（與本頁無關，供 code-quality-decline 已用） | — | — |

## 二、逾期懸置 21 筆（L66–72、L124–131、L386、L395、L427、L1061–1081）

已查到一手可結案的：
- **L63／L129 infostealer** → ✅ 結案（上表）。
- **L112 EFS** → ✅ 結案（上表），日期 09-01。
- **L120 Auto Mode 60–80%** → ✅ 結案：官方定性「非安全邊界」，非「待官方回應」。

未查（屬媒體轉述型，記者可依日報回訪；主編本輪不逐條 WebFetch）：L66 Gmail 直接發信、L67 勒索軟體用 Claude Code、L68／L121／L126 「疑心較重 agent 互相攻擊」（TechRadar／Cybernews 同一事）、L69／L128 WSJ 失控案例、L71／L131 四實驗室評測指標、L72 弱模型解讀強模型推理、L103／L236 惡意 `.git`、L60／L251 AISLE curl 6 CVE、L114 llms.txt、L115 MCP RCE、L116 Wiz 蜜罐、L118 Opus 4.6 健身房 API。**同一事件在「未修補風險現況」表（L58–72）與「提示注入攻擊面」表（L103–131）各掛一次懸置**，21 筆實為約 12 件——去向表要合併。

## 三、給設計者

1. 本頁最缺的一句是官方立場：**Auto Mode 不是安全邊界**。有了這句，Q1「最該防什麼、官方修了沒」才答得出：官方不會「修」到 0%，讀者的選項是隔離環境＋監看。
2. EFS 與提示注入是兩件事；頁面把 EFS 放在「提示注入攻擊面」節下（L112）是跑錯家。
3. 懸置重複掛在兩張表，是本頁 21 筆逾期的一半來源。

## 四、複驗後補查（UTC 05:2x）

- **「擋下 89% 危險指令」出處**：[Anthropic 官方 blog 2026-08-07](https://claude.com/blog/auto-mode-default-in-claude-code)——「auto mode caught 89% of the same commands」（人類測試者 13.6%）；提示注入由第三方 Trajectory Labs 測 72 個間接注入情境 × 10 次＝720 次，「none … succeeded against Claude Fable 5, Opus 5, or Sonnet 5 running auto mode」；同文明寫「relies on classification systems and therefore does not eliminate risk. For high-stakes changes to production infrastructure, we still recommend reviewing Claude's actions yourself」。→ 結論表 Auto 列「官方擋到哪」格：89% 補此出處與日期；0% 的方法論（瀏覽器整合＋MCP 包 Chrome API）可一句帶過，與 embracethered 60–80%（網頁摘要＋`struct.py` 遮蔽）是**不同攻擊面的兩個數字**，不是互相推翻。
- **EFS 日期跨頁不一**：本頁 09-01（官方）；`topics/anthropic-business` 寫 09-02（該頁 L533 又寫 09-01）→ 屬商業記者頁，走轉知帳本，不在本波直接改。
