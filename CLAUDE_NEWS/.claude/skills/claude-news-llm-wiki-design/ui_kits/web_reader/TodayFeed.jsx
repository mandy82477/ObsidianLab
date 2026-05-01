// TodayFeed.jsx
function TodayFeed() {
  return (
    <article className="feed">
      <header className="feed__header">
        <div className="day-badge">
          <div className="day-badge__y">2026</div>
          <div className="day-badge__d">30</div>
          <div className="day-badge__m">Apr · Wed</div>
        </div>
        <div className="feed__meta">
          <h1>每日新聞摘要 · Claude Code &amp; Anthropic</h1>
          <div className="feed__metarow">
            <span><b>5/5</b> sources</span>
            <span><b>52</b> articles</span>
            <span>generated <b>2026-05-01 03:07 UTC</b></span>
            <span className="pulse">● fresh</span>
          </div>
        </div>
      </header>

      <section id="star" className="feed__section feed__section--star">
        <h2>⭐ 重點話題</h2>
        <article className="story story--star">
          <h3><a href="#">Claude Code refuses requests if commits mention "OpenClaw"</a></h3>
          <p>Claude Code 被發現存在異常行為：若 Git 提交訊息中含有特定 JSON 格式的 "OpenClaw" 字串，工具會直接拒絕請求，或立即將帳單的 Extra Usage 衝至 100%；也有使用者僅在文件內容中提及 OpenClaw 便觸發異常回應。Anthropic 至今未公開說明，是近期最嚴重的帳單透明度信任事件，在 HN 引發近千則討論。</p>
          <div className="sourceline"><code>Hacker News</code><span>·</span><span>04/30 14:36 UTC</span></div>
        </article>
        <article className="story story--star">
          <h3><a href="#">White House Opposes Anthropic's Plan to Expand Mythos Access</a></h3>
          <p>白宮公開反對 Anthropic 擴大旗下最強大 Mythos 模型的存取範圍。社群稱之為「AI 授權時代的開端」，並與 Anthropic 和五角大廈之間的政策角力密切相關。</p>
          <div className="sourceline"><code>Hacker News</code><span>·</span><span>04/30 09:55 UTC</span></div>
        </article>
        <article className="story story--star">
          <h3><a href="#">Anthropic Could Raise $50B at a $900B Valuation</a></h3>
          <p>TechCrunch 報導 Anthropic 已收到多個主動出擊的融資要約，規模約 $500 億美元、估值區間 $8,500 億–$9,000 億；Google 另被報導押注高達 $400 億。</p>
          <div className="sourceline"><code>Hacker News</code><span>·</span><span>04/30 00:39 UTC</span></div>
        </article>
      </section>

      <section id="tech" className="feed__section">
        <h2>🔧 技術更新</h2>
        <article className="story">
          <h3><a href="#">anthropic-sdk-typescript v0.92.0</a></h3>
          <p>主要改善 Managed API 相關功能，是持續強化 Claude Managed Agents 基礎設施的一環。</p>
          <div className="sourceline"><code>GitHub / anthropics</code><span>·</span><span>04/30 19:40 UTC</span></div>
        </article>
        <article className="story">
          <h3><a href="#">CC 2.1.124 (+166 tokens) and 2.1.126 (-87 tokens) system prompt</a></h3>
          <p>2.1.124 新增「File modification detected」預算超出提醒機制（增 166 tokens），2.1.126 則精簡核心身份指令（減 87 tokens）。</p>
          <div className="sourceline"><code>r/ClaudeAI</code><span>·</span><span>04/30 18:34 UTC</span></div>
        </article>
      </section>

      <section id="discuss" className="feed__section">
        <h2>💬 技術熱度討論</h2>
        <article className="story">
          <h3><a href="#">Show HN: Nimbalyst — visual workspace for Claude Code, Codex, OpenCode</a></h3>
          <p>多 Agent 視覺化工作台，核心功能是讓使用者與 AI Agent 同步協作相同檔案，並透過 WYSIWYG diff 介面逐一審核各 Agent 的修改。</p>
          <div className="sourceline"><code>Hacker News</code><span>·</span><span>04/30 13:36 UTC</span><span>·</span><span style={{color:"var(--sentiment-positive)"}}>情緒：😊 正面</span></div>
        </article>
        <article className="story">
          <h3><a href="#">Opus 4.7 is a genuine regression and I'm tired of pretending</a></h3>
          <p>一位重度 Max 20x 訂戶直言 Opus 4.7 嚴重退步，主要問題是過度「後設化」——每個回覆都像在撰寫論文。</p>
          <div className="sourceline"><code>r/ClaudeAI</code><span>·</span><span>04/30 17:37 UTC</span><span>·</span><span style={{color:"var(--sentiment-negative)"}}>情緒：😤 負面</span></div>
        </article>
      </section>

      <section id="pricing" className="feed__section">
        <h2>💰 付費方案動態</h2>
        <article className="story">
          <h3><a href="#">Claude Code dies with ANTHROPIC_API_KEY in cloud environment</a></h3>
          <p>使用者警告：若在雲端環境設置 <code>ANTHROPIC_API_KEY</code>，所有 Code 呼叫將改走 API 計費通道，造成大量意外費用。</p>
          <div className="sourceline"><code>Hacker News</code><span>·</span><span>04/30 19:11 UTC</span></div>
        </article>
      </section>

      <section id="focus" className="feed__section feed__section--focus">
        <h2>📌 今日聚焦</h2>
        <ul className="focus-list">
          <li><span className="focus-tag focus-tag--major">[重大事件]</span> Claude Code "OpenClaw" 事件暴露 AI 工具的信任危機。</li>
          <li><span className="focus-tag focus-tag--major">[重大事件]</span> 白宮介入 Mythos 模型存取管控。</li>
          <li><span className="focus-tag focus-tag--track">[持續追蹤]</span> Anthropic 估值逼近 $9,000 億美元。</li>
          <li><span className="focus-tag focus-tag--tool">[新工具]</span> Claude Security 公開測試版上線。</li>
          <li><span className="focus-tag focus-tag--trend">[社群趨勢]</span> 帳單透明度問題多點同步爆發。</li>
        </ul>
      </section>

      <aside className="sourcetable">
        <div className="sourcetable__title">來源狀態 · Source status</div>
        <div className="sourcetable__rows">
          <div><span>Anthropic Blog</span><b>✅</b><span>0</span></div>
          <div><span>GitHub</span><b>✅</b><span>3</span></div>
          <div><span>Hacker News</span><b>✅</b><span>37</span></div>
          <div><span>Reddit</span><b>✅</b><span>20</span></div>
          <div><span>Google News</span><b>✅</b><span>24</span></div>
        </div>
      </aside>
    </article>
  );
}
window.TodayFeed = TodayFeed;
