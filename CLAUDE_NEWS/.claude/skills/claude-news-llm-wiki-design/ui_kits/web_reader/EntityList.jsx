// EntityList.jsx — wiki index
function EntityList() {
  const rows = [
    { name: "claude-code", type: "product", state: "active", stateColor: "success", summary: "Claude Code CLI 主頁：功能、已知問題、社群工具", updated: "2026-04-27" },
    { name: "opus-4-7", type: "model", state: "active（爭議）", stateColor: "warn", summary: "Opus 4.7 發布細節、思考深度爭議、cache 問題", updated: "2026-04-27" },
    { name: "mythos", type: "model", state: "限制存取", stateColor: "danger", summary: "高能力安全模型，七週發現 2,000+ 漏洞", updated: "2026-04-27" },
    { name: "pricing", type: "policy", state: "持續調整", stateColor: "warn", summary: "訂閱方案、近期政策變動、token 成本", updated: "2026-04-27" },
    { name: "bugcrawl", type: "feature", state: "測試中", stateColor: "info", summary: "Anthropic 測試中的漏洞偵測工具", updated: "2026-04-26" },
    { name: "claude-design", type: "feature", state: "active（初期）", stateColor: "info", summary: "Anthropic AI 設計工具，首日評價偏負面", updated: "2026-04-27" },
    { name: "project-deal", type: "feature", state: "實驗中", stateColor: "info", summary: "Anthropic Claude 代理人自主交易談判實驗", updated: "2026-04-27" },
  ];
  const topics = [
    { name: "code-quality-decline", state: "monitoring", stateColor: "warn", summary: "Claude Code 效能退步事件" },
    { name: "google-investment", state: "resolved", stateColor: "success", summary: "Google 投資 400 億美元" },
    { name: "competitor-landscape", state: "ongoing", stateColor: "info", summary: "Google 祕密開發競品" },
    { name: "community-tech-patterns", state: "ongoing", stateColor: "info", summary: "社群技術應用趨勢追蹤" },
  ];
  return (
    <div className="wikipage">
      <div className="wikipage__head">
        <h1>Wiki</h1>
        <p className="text-secondary">LLM-curated knowledge graph of the Claude / Anthropic ecosystem. <b>13</b> pages · last updated 2026-04-27.</p>
      </div>
      <h2>Entities</h2>
      <div className="entitytable">
        {rows.map((r,i)=>(
          <a key={i} href="#" className="entityrow">
            <div className="entityrow__name"><span className="wikilink-glyph">[[</span><span>entities/{r.name}</span><span className="wikilink-glyph">]]</span></div>
            <div className="entityrow__type">{r.type}</div>
            <div className="entityrow__state"><span className={"pill pill--"+r.stateColor}>● {r.state}</span></div>
            <div className="entityrow__summary">{r.summary}</div>
            <div className="entityrow__updated">{r.updated}</div>
          </a>
        ))}
      </div>
      <h2 style={{marginTop: 32}}>Topics</h2>
      <div className="entitytable entitytable--topics">
        {topics.map((r,i)=>(
          <a key={i} href="#" className="entityrow">
            <div className="entityrow__name"><span className="wikilink-glyph">[[</span><span>topics/{r.name}</span><span className="wikilink-glyph">]]</span></div>
            <div className="entityrow__state"><span className={"pill pill--"+r.stateColor}>● {r.state}</span></div>
            <div className="entityrow__summary">{r.summary}</div>
          </a>
        ))}
      </div>
    </div>
  );
}
window.EntityList = EntityList;
