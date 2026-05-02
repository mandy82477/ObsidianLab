# Claude Mythos

**類型：** model
**狀態：** 限制存取（非公開）
**首次出現：** 2026-04（限定夥伴 Preview）
**最後更新：** 2026-05-02

---

## 現況

Claude Mythos 是 Anthropic 因安全風險而未對外公開發布的高能力 AI 模型，目前僅向有限合作夥伴提供 Preview 存取。**2026-04-29，白宮正式反對 Anthropic 擴大 Mythos 存取範圍**，AI 模型存取管控首次出現聯邦政府層級的直接干預，是 Mythos 政策走向的重要轉折點。

Anthropic 已透過其安全評估流程確認，Mythos 具備在無需人類專家介入的情況下，**自主發現並武器化軟體漏洞、生成可執行 exploit** 的能力，屬於 AI 安全領域的重大里程碑，也是 Anthropic 決定暫不公開的核心原因。

---

## 政府監管介入（2026-04-29）

### 白宮反對擴大 Mythos 存取（Bloomberg 04/29 / WSJ 04/30）
Bloomberg（04/29）與 WSJ（04/30）先後報導，白宮正式反對 Anthropic 擴大 Mythos 的存取範圍。WSJ 補充細節：Anthropic **自身亦公開聲稱** Mythos 的能力強大到足以破壞系統並危及網路安全，「世界尚未準備好接受它」，同時涉及 Anthropic 與五角大廈之間的政策角力。社群稱此為「AI 授權時代的開端」，是聯邦政府對單一 AI 模型存取管控的首次直接干預。

### Steve Blank：「我們已打開潘朵拉的盒子」
創業教父 Steve Blank 撰文將 Anthropic Mythos 計畫與量子運算對加密安全的衝擊相提並論，指出 Mythos 帶來的網路安全威脅比預期的單一量子衝擊更難應對，因為它已「悄然到位」。文章在 HN 引發廣泛討論。

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

## SWE-bench 評測方法論爭議（2026-04-27，2026-04-28 持續報導）

一篇技術分析（The Philosophical Hacker）指出 Anthropic 在 Mythos 的 SWE-bench 評測報告中存在**循環論證**：以 LLM 判斷解題是否為「記憶」，再以此結果計算成功率，邏輯上無法自洽。同日，南華早報報導相關恐慌情緒已蔓延至中國科技圈。2026-04-28，HN 再次精選同一文章（Philosophical Hacker），顯示此爭議已擴散至更廣泛技術社群。

> ⚠️ **方法論待澄清**：Anthropic 截至 2026-04-28 仍未公開回應此質疑。

---

## Project Glasswing：AI 資安威脅研究

Anthropic 的「Project Glasswing」聚焦 AI 資安威脅，Mizuho 分析師認為此計畫將帶動 CrowdStrike 等資安股上漲，顯示 AI 安全議題（Mythos 能力揭露為背景）正從技術討論延伸至資本市場判斷。

---

## Transparency Hub 爭議

社群發現 Anthropic 未將 Mythos Preview 納入其[透明度中心](https://www.anthropic.com/transparency)，引發對資訊公開承諾一致性的質疑。

---

## OpenAI Cyber 限制存取事件（2026-05-01）

TechCrunch 報導，Sam Altman 在公開批評 Anthropic 限制 Mythos 存取範圍之後，旋即宣布 OpenAI 的 **GPT-5.5 Cyber**（高能力資安模型）同樣採用限制性推出策略，僅開放給通過審核的「關鍵防禦者」。社群廣泛討論此舉的雙重標準意涵：Altman 對 Anthropic 的批評顯得站不住腳，同時也間接驗證了高能力 AI 資安工具在公開部署前確實存在實際安全顧慮。

---

## 參考來源

- [[news/2026-04-25]]
- [[news/2026-04-27]]
- [[news/2026-04-28]]
- [[news/2026-04-29]]
- [[news/2026-04-30]]
- [[news/2026-05-02]]
- [What Anthropic's Mythos Means for the Future of Cybersecurity](https://spectrum.ieee.org/ai-cybersecurity-mythos) — IEEE Spectrum
- [Anthropic's Argument for Mythos SWE-bench improvement contains a fatal error](https://www.philosophicalhacker.com/post/anthropic-error/) — The Philosophical Hacker
