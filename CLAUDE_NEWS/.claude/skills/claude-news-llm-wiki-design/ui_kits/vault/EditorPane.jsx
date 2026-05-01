// EditorPane.jsx — center reading view (Obsidian "live preview")
function EditorPane({ file }) {
  if (file === "wiki/entities/claude-code.md") {
    return (
      <article className="editor">
        <h1>Claude Code</h1>
        <Frontmatter rows={[
          ["類型", "product"],
          ["狀態", <span style={{color:"var(--success)"}}>active</span>],
          ["首次出現", "2025（正式推出）"],
          ["最後更新", "2026-04-27"],
        ]} />
        <hr />
        <h2>現況</h2>
        <p>Claude Code 是 Anthropic 的 AI 編碼 CLI 工具，支援 agentic 工作流程、MCP Server 整合、Hooks 機制與 Agent Teams。目前為最受開發者關注的 AI 編碼工具之一。近期接連出現效能退步事件（已承認工程疏失）、HERMES.md 靜默計費 bug、API 金鑰外洩漏洞，安全性與可靠性受到集中審視。</p>

        <h2>核心功能</h2>
        <ul>
          <li><b>CLAUDE.md</b> — 專案級別的 AI 指令設定</li>
          <li><b>Hooks</b> — 在特定事件前後注入自定義邏輯</li>
          <li><b>Skills</b> — 可複用的任務封裝單元</li>
          <li><b>Agent Teams</b> — 多 agent 協作</li>
          <li><b>MCP Servers</b> — 外部工具整合</li>
        </ul>

        <Callout kind="danger" title="HERMES.md 計費路由 bug">
          <p>git commit 歷史中含大寫字串 <code>HERMES.md</code> 會觸發靜默切換至 API 額外計費，完全繞過 Max 方案配額。Anthropic 已確認為 bug 但拒絕退款，已知損失達 $200。見 <Wikilink to="entities/pricing">entities/pricing</Wikilink></p>
        </Callout>

        <Callout kind="warning" title="Stop Hooks 被忽略">
          <p>Claude 4.7 開始無視自訂 stop hooks，影響依賴 hooks 的自動化工作流程，屬行為退步（regression）。回報日：2026-04-24。</p>
        </Callout>

        <h2>版本歷史</h2>
        <table className="md-table">
          <thead><tr><th>日期</th><th>事件</th></tr></thead>
          <tbody>
            <tr><td><code>2026-04-27</code></td><td>API 金鑰外洩漏洞被媒體報導</td></tr>
            <tr><td><code>2026-04-27</code></td><td>版本從 2.1.120 回滾至 2.1.119，疑似靜默撤版</td></tr>
            <tr><td><code>2026-04-26</code></td><td>HERMES.md 計費路由 bug 曝光</td></tr>
            <tr><td><code>2026-04-24</code></td><td>Anthropic 正式承認效能退步源於工程疏失</td></tr>
          </tbody>
        </table>

        <h2>相關議題</h2>
        <ul>
          <li><Wikilink to="topics/code-quality-decline" /></li>
          <li><Wikilink to="topics/competitor-landscape" /></li>
        </ul>

        <h2>參考來源</h2>
        <ul>
          <li><Wikilink to="news/2026-04-25" /></li>
          <li><Wikilink to="news/2026-04-26" /></li>
          <li><Wikilink to="news/2026-04-27" /></li>
        </ul>
      </article>
    );
  }

  if (file === "news/2026-04-30.md") {
    return (
      <article className="editor">
        <h1>每日新聞摘要</h1>
        <div className="digest-meta">
          <div><span className="k">日期</span><span className="v"><code>2026-04-30</code></span></div>
          <div><span className="k">來源</span><span className="v">5/5</span></div>
          <div><span className="k">文章</span><span className="v">52</span></div>
          <div><span className="k">產生於</span><span className="v">2026-05-01 03:07 UTC</span></div>
        </div>
        <hr />
        <h2>⭐ 重點話題</h2>

        <div className="digest-item digest-item--star">
          <h3>⭐ <a href="#">Claude Code refuses requests if commits mention "OpenClaw"</a></h3>
          <p>Claude Code 被發現存在異常行為：若 Git 提交訊息中含有特定 JSON 格式的 "OpenClaw" 字串，工具會直接拒絕請求，或立即將帳單的 Extra Usage 衝至 100%。Anthropic 至今未公開說明，是近期最嚴重的帳單透明度信任事件。</p>
          <SourceLine source="Hacker News" time="04/30 14:36 UTC" />
        </div>

        <div className="digest-item digest-item--star">
          <h3>⭐ <a href="#">White House Opposes Anthropic's Plan to Expand Mythos Access</a></h3>
          <p>白宮公開反對 Anthropic 擴大旗下最強大 Mythos 模型的存取範圍。社群稱之為「AI 授權時代的開端」，與 Anthropic 和五角大廈之間的政策角力密切相關。</p>
          <SourceLine source="Hacker News" time="04/30 09:55 UTC" />
        </div>

        <h2>🔧 技術更新</h2>
        <div className="digest-item">
          <h3><a href="#">anthropic-sdk-typescript v0.92.0</a></h3>
          <p>主要改善 Managed API 相關功能，是持續強化 Claude Managed Agents 基礎設施的一環。</p>
          <SourceLine source="GitHub / anthropics/anthropic-sdk-typescript" time="04/30 19:40 UTC" />
        </div>

        <h2>💬 技術熱度討論</h2>
        <div className="digest-item">
          <h3><a href="#">Show HN: Nimbalyst — open-source visual workspace for ClaudeCode</a></h3>
          <p>多 Agent 視覺化工作台，支援 Claude Code、Codex、Opencode，核心功能是讓使用者與 AI Agent 同步協作相同檔案，並透過 WYSIWYG diff 介面逐一審核各 Agent 的修改。</p>
          <SourceLine source="Hacker News" time="04/30 13:36 UTC" sentiment={{ label: "😊 正面", tone: "positive" }} />
        </div>
        <div className="digest-item">
          <h3><a href="#">Opus 4.7 is a genuine regression and I'm tired of pretending</a></h3>
          <p>一位重度 Max 20x 訂戶直言 Opus 4.7 嚴重退步，主要問題是過度「後設化」——每個回覆都像在撰寫論文，無法直接回答問題。</p>
          <SourceLine source="Reddit / r/ClaudeAI" time="04/30 17:37 UTC" sentiment={{ label: "😤 負面", tone: "negative" }} />
        </div>

        <h2>📌 今日聚焦</h2>
        <ul className="focus-list">
          <li><span className="focus-tag focus-tag--major">[重大事件]</span> Claude Code "OpenClaw" 事件暴露 AI 工具的信任危機</li>
          <li><span className="focus-tag focus-tag--major">[重大事件]</span> 白宮介入 Mythos 模型存取管控</li>
          <li><span className="focus-tag focus-tag--track">[持續追蹤]</span> Anthropic 估值逼近 $9,000 億美元</li>
          <li><span className="focus-tag focus-tag--tool">[新工具]</span> Claude Security 公開測試版上線</li>
          <li><span className="focus-tag focus-tag--trend">[社群趨勢]</span> 帳單透明度問題多點同步爆發</li>
        </ul>
      </article>
    );
  }

  if (file === "wiki/index.md") {
    return (
      <article className="editor">
        <h1>Wiki 目錄</h1>
        <p>LLM 查詢此 wiki 時，<b>先讀這個檔案</b>找相關頁面，再讀具體頁面取得詳細資訊。</p>
        <p style={{color:"var(--fg-3)", fontSize: 14}}><b>最後更新：</b> 2026-04-27 · <b>頁面數：</b> 13</p>
        <h2>Entities</h2>
        <table className="md-table">
          <thead><tr><th>頁面</th><th>類型</th><th>狀態</th><th>摘要</th></tr></thead>
          <tbody>
            <tr><td><Wikilink to="entities/claude-code">entities/claude-code</Wikilink></td><td>product</td><td><span style={{color:"var(--success)"}}>active</span></td><td>Claude Code CLI 主頁</td></tr>
            <tr><td><Wikilink to="entities/opus-4-7">entities/opus-4-7</Wikilink></td><td>model</td><td><span style={{color:"var(--warn)"}}>active（爭議）</span></td><td>Opus 4.7 發布細節、思考深度爭議</td></tr>
            <tr><td><Wikilink to="entities/mythos">entities/mythos</Wikilink></td><td>model</td><td><span style={{color:"var(--danger)"}}>限制存取</span></td><td>高能力安全模型</td></tr>
            <tr><td><Wikilink to="entities/pricing">entities/pricing</Wikilink></td><td>policy</td><td>持續調整</td><td>訂閱方案、近期政策變動</td></tr>
          </tbody>
        </table>
        <h2>Topics</h2>
        <table className="md-table">
          <thead><tr><th>頁面</th><th>狀態</th><th>摘要</th></tr></thead>
          <tbody>
            <tr><td><Wikilink to="topics/code-quality-decline">topics/code-quality-decline</Wikilink></td><td><span style={{color:"var(--warn)"}}>monitoring</span></td><td>Claude Code 效能退步事件</td></tr>
            <tr><td><Wikilink to="topics/google-investment">topics/google-investment</Wikilink></td><td><span style={{color:"var(--success)"}}>resolved</span></td><td>Google 投資 400 億美元</td></tr>
            <tr><td><Wikilink to="topics/competitor-landscape">topics/competitor-landscape</Wikilink></td><td>ongoing</td><td>Google 祕密開發競品</td></tr>
          </tbody>
        </table>
      </article>
    );
  }

  return <article className="editor"><h1>{file}</h1><p style={{color:"var(--fg-3)"}}>(file content elided in this kit)</p></article>;
}

window.EditorPane = EditorPane;
