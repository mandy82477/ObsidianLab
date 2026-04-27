# Claude Mythos

**類型：** model
**狀態：** 限制存取（非公開）
**首次出現：** 2026-04（限定夥伴 Preview）
**最後更新：** 2026-04-27

---

## 現況

Claude Mythos 是 Anthropic 因安全風險而未對外公開發布的高能力 AI 模型，目前僅向有限合作夥伴提供 Preview 存取。

Anthropic 已透過其安全評估流程確認，Mythos 具備在無需人類專家介入的情況下，**自主發現並武器化軟體漏洞、生成可執行 exploit** 的能力，屬於 AI 安全領域的重大里程碑，也是 Anthropic 決定暫不公開的核心原因。

---

## 能力驗證

### 七週發現 2,000+ 軟體漏洞（2026-04-25 報導）
Mythos AI 模型在七週測試期內發現逾 **2,000 個未知軟體漏洞**，大量涉及加密貨幣基礎設施。Fox News、CoinDesk、Crypto Briefing 等多家媒體同步報導，顯示其漏洞發現能力已引發業界與加密社群的高度關注。

---

## 安全事件

### 駭客入侵事件（2026-04-24 回報）
據多家媒體（KRON4 等）報導，Mythos 遭駭客存取，引發外界對高風險模型保管機制的廣泛疑慮。目前尚不清楚存取範圍及 Anthropic 的具體回應措施。

> ⚠️ **待確認**：此事件細節尚待官方聲明，建議持續追蹤。

---

## 資安意義

IEEE Spectrum 深入分析指出，Mythos 代表 AI 在網路安全攻防上的雙重性：
- **防禦端**：可大幅加速漏洞發現與修補速度
- **攻擊端**：若落入惡意行為者手中，可自動化生成高品質 exploit

這也是為何 Anthropic 選擇限制存取，而非走標準的公開發布路線。

### 安全部署要求（2026-04-27，IEEE Spectrum 後續報導）
IEEE Spectrum 進一步報導，Mythos Preview 的高度自主程式設計能力對軟體供應鏈安全帶來新挑戰，需要配套新的安全管控措施（程式碼隔離、執行沙盒、權限最小化）才能安全部署。這意味著 Mythos 的商業化路徑將比普通模型複雜得多。

---

## SWE-bench 評測方法論爭議（2026-04-27）

一篇技術分析（The Philosophical Hacker）指出 Anthropic 在 Mythos 的 SWE-bench 評測報告中存在**循環論證**：以 LLM 判斷解題是否為「記憶」，再以此結果計算成功率，邏輯上無法自洽。同日，南華早報報導相關恐慌情緒已蔓延至中國科技圈，使 Mythos 的評測可靠性問題成為跨地區焦點。

> ⚠️ **方法論待澄清**：Anthropic 尚未公開回應此質疑。

---

## Project Glasswing：AI 資安威脅研究

Anthropic 的「Project Glasswing」聚焦 AI 資安威脅，Mizuho 分析師認為此計畫將帶動 CrowdStrike 等資安股上漲，顯示 AI 安全議題（Mythos 能力揭露為背景）正從技術討論延伸至資本市場判斷。

---

## Transparency Hub 爭議

社群發現 Anthropic 未將 Mythos Preview 納入其[透明度中心](https://www.anthropic.com/transparency)，引發對資訊公開承諾一致性的質疑。

---

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-27]]
- [What Anthropic's Mythos Means for the Future of Cybersecurity](https://spectrum.ieee.org/ai-cybersecurity-mythos) — IEEE Spectrum
- [Anthropic's Argument for Mythos SWE-bench improvement contains a fatal error](https://www.philosophicalhacker.com/post/anthropic-error/) — The Philosophical Hacker
