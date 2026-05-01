// BacklinksPane.jsx — right pane "Linked mentions"
function BacklinksPane({ file }) {
  const data = {
    "wiki/entities/claude-code.md": {
      outline: ["現況", "核心功能", "已知問題", "版本歷史", "競品", "實用工具", "相關議題", "參考來源"],
      backlinks: [
        { from: "wiki/index.md",                 snippet: "Claude Code CLI 主頁：功能、已知問題、社群工具" },
        { from: "wiki/overview.md",              snippet: "Claude Code 近期的效能退步事件嚴重損傷了開發者信任" },
        { from: "wiki/entities/opus-4-7.md",     snippet: "Claude Code 頻繁出現隨機觸發 Usage Policy 拒絕的錯誤" },
        { from: "wiki/entities/pricing.md",      snippet: "HERMES.md 計費路由 bug…完全繞過 Max 方案配額" },
        { from: "news/2026-04-30.md",            snippet: "Show HN: Nimbalyst…支援 Claude Code、Codex、Opencode" },
        { from: "news/2026-04-29.md",            snippet: "What's new in CC 2.1.124 (+166 tokens)" },
      ],
    },
    "news/2026-04-30.md": {
      outline: ["⭐ 重點話題", "🔧 技術更新", "💬 技術熱度討論", "💰 付費方案動態", "📌 今日聚焦"],
      backlinks: [
        { from: "wiki/log.md", snippet: "[2026-04-30] ingest | 每日日報更新" },
      ],
    },
  };
  const d = data[file] || { outline: [], backlinks: [] };
  return (
    <div className="backlinks">
      <div className="backlinks__section">
        <div className="backlinks__head">Outline</div>
        <ul className="outline">
          {d.outline.map((h, i) => <li key={i}>{h}</li>)}
        </ul>
      </div>
      <div className="backlinks__section">
        <div className="backlinks__head">Linked mentions <span className="backlinks__count">{d.backlinks.length}</span></div>
        {d.backlinks.map((b, i) => (
          <div key={i} className="backlink">
            <div className="backlink__from"><code>{b.from}</code></div>
            <div className="backlink__snippet">{b.snippet}</div>
          </div>
        ))}
      </div>
      <div className="backlinks__section">
        <div className="backlinks__head">Tags</div>
        <div className="taglist">
          <span className="tag">#claude-code</span>
          <span className="tag">#regression</span>
          <span className="tag">#billing</span>
        </div>
      </div>
    </div>
  );
}

window.BacklinksPane = BacklinksPane;
