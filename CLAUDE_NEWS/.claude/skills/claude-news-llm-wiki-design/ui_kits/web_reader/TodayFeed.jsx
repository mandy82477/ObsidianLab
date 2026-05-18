// TodayFeed.jsx — applied suggestions 1·2·4·5·8·9
// Content synced to CLAUDE_NEWS/news/2026-05-17.md
function SectionH({ label, en, count }) {
  return (
    <div className="section-h">
      <span className="section-h__label">{label}</span>
      <span className="section-h__en">{en}</span>
      {count != null && <span className="section-h__count">{count} items</span>}
    </div>
  );
}

function SumiMasthead() {
  return (
    <div className="masthead">
      <svg className="masthead__stroke" viewBox="0 0 1100 80" preserveAspectRatio="none">
        <defs>
          <linearGradient id="ink-fade" x1="0" x2="1">
            <stop offset="0"    stopColor="var(--ink-1)" stopOpacity="0"/>
            <stop offset="0.05" stopColor="var(--ink-1)" stopOpacity="0.85"/>
            <stop offset="0.92" stopColor="var(--ink-1)" stopOpacity="0.7"/>
            <stop offset="1"    stopColor="var(--ink-1)" stopOpacity="0"/>
          </linearGradient>
        </defs>
        <path d="M 20 50
                 C 200 38, 400 60, 600 44
                 S 950 56, 1080 42"
              stroke="url(#ink-fade)" strokeWidth="2.2" fill="none" strokeLinecap="round"/>
        <circle cx="1080" cy="42" r="2.5" fill="var(--ochre-9)"/>
      </svg>
    </div>
  );
}

function TodayFeed() {
  return (
    <>
      <SumiMasthead />
      <article className="feed">
        <header className="feed__header">
          <div className="day-monumental">
            <div className="day-monumental__y">2026</div>
            <span className="day-monumental__d">17</span>
            <div className="day-monumental__m">May · Sun</div>
          </div>
          <div className="feed__meta">
            <h1>每日新聞摘要 · Claude Code &amp; Anthropic</h1>
            <div className="feed__metarow">
              <div className="row-prim">
                <span><b>26</b> articles</span>
                <span className="dot">·</span>
                <span className="pulse">fresh</span>
              </div>
              <div className="row-sec">6/6 sources · generated 12:45 utc</div>
            </div>
          </div>
        </header>

        <section id="focus" className="feed__section feed__section--focus">
          <SectionH label="今 日 聚 焦" en="today's focus" count={5} />
          <ul className="focus-list">
            <li><span className="focus-tag focus-tag--trend">trend</span> Claude Skills 的靜默行為引發關注：覆蓋指令、壓縮選項、自行派生 sub-agent，社群對 Skills 透明度疑慮升溫。</li>
            <li><span className="focus-tag focus-tag--track">track</span> Context 管理策略成為本日熱門議題：<code>/clear</code> vs <code>/compact</code> 與官方四種 context 工具的最佳實踐。</li>
            <li><span className="focus-tag focus-tag--trend">trend</span> 以 Claude Code 為核心的持久性 agent 系統分享湧現：語音對話、排程任務、螢幕感知等實作深度快速提升。</li>
            <li><span className="focus-tag focus-tag--major">risk</span> Anthropic 多帳號使用政策出現明確紅線：兩種多帳號架構中已有一種被官方明確禁止，需留意合規邊界。</li>
            <li><span className="focus-tag focus-tag--track">track</span> <code>claude -p</code> 計費變更持續影響社群：開發者分享在政策調整後如何維持自動化工作流程。</li>
          </ul>
        </section>

        <section id="star" className="feed__section">
          <SectionH label="重 點 話 題" en="headlines" count={3} />
          <article className="story story--star">
            <h3><a href="https://news.ycombinator.com/item?id=48160604" target="_blank" rel="noreferrer">Ask HN: Do you still spend time maintaining Claude.md / AGENTS.md files?</a></h3>
            <p>HN 上引發廣泛討論的問題：在實際使用 Coding Agent 的開發者中，仍有多少人持續維護 CLAUDE.md、AGENTS.md 等行為指令檔？討論指出即使指令不超過 100 行，規則仍常常不被遵守，但 Karpathy 等知名開發者依然積極分享自己的設定，社群對 instruction file 實際效益的分歧在此篇清晰呈現。</p>
            <div className="sourceline"><code>Hacker News</code><span>·</span><span>05/16 14:33 UTC</span></div>
          </article>
          <article className="story story--star">
            <h3><a href="https://www.reddit.com/r/ClaudeAI/comments/1tfl6b0/claude_skills_silently_override_my_instructions/" target="_blank" rel="noreferrer">Claude skills silently override my instructions, and the surprising pitfalls</a></h3>
            <p>開發者在使用 Claude Skill 時意外發現，<code>ask_user_input_v0</code> 工具存在最多 3 個問題、每題最多 4 個選項的硬性限制，導致 Claude 在不告知用戶的情況下靜默壓縮問題與選項，這種「不透明代理行為」引發對 Skills 機制設計的系統性質疑。</p>
            <div className="sourceline"><code>r/ClaudeAI</code><span>·</span><span>05/17 01:58 UTC</span></div>
          </article>
          <article className="story story--star">
            <h3><a href="https://www.reddit.com/r/ClaudeAI/comments/1tfnnvv/built_a_longterm_autonomous_agent_system_with/" target="_blank" rel="noreferrer">Built a long-term autonomous agent system with Claude Code</a></h3>
            <p>開發者幾乎完全以 Claude Code 建構了一套持久性 agent 系統，具備語義與情節雙重記憶、德英雙語語音對話、情緒狀態追蹤、螢幕感知、自主排程任務，以及即時 SaaS 生成等功能，代表社群在 agentic 系統工程上已達到相當高的實作複雜度。</p>
            <div className="sourceline"><code>r/ClaudeAI</code><span>·</span><span>05/17 04:05 UTC</span></div>
          </article>
        </section>

        <section id="tech" className="feed__section">
          <SectionH label="技 術 更 新" en="technical updates" count={2} />
          <article className="story">
            <h3><a href="https://www.reddit.com/r/ClaudeAI/comments/1tfjja8/anthropic_shipped_4_context_tools_between_clear/" target="_blank" rel="noreferrer">Anthropic shipped 4 context tools between /clear and /compact</a></h3>
            <p>社群整理了 Anthropic 官方 Best Practices 文件中提及的四種 context 管理工具，超越了一般只知道 <code>/clear</code> 和 <code>/compact</code> 兩種選項的認知，提供更細緻的工作階段管理策略，對大型 codebase 中長時間使用 Claude Code 的開發者具直接參考價值。</p>
            <div className="sourceline"><code>r/ClaudeAI</code><span>·</span><span>05/17 00:24 UTC</span></div>
          </article>
          <article className="story">
            <h3><a href="#" target="_blank" rel="noreferrer">Claude Code Did The Heavy Lifting To Get Adobe Lightroom CC Running On Linux</a></h3>
            <p>Phoronix 報導開發者借助 Claude Code 完成了在 Linux 上運行 Adobe Lightroom CC 的主要移植工作，展現 AI Coding Agent 在複雜跨平台工程任務上的實際能力。</p>
            <div className="sourceline"><code>Google News / Phoronix</code><span>·</span><span>05/17 02:20 UTC</span></div>
          </article>
        </section>

        <section id="discuss" className="feed__section">
          <SectionH label="技 術 熱 度 討 論" en="discussion" count={4} />
          <article className="story">
            <h3><a href="https://www.reddit.com/r/ClaudeAI/comments/1tfnadx/got_tired_of_making_sure_my_laptop_is_open_for/" target="_blank" rel="noreferrer">Got tired of making sure my laptop is open for Dispatch, so gave Claude Chat full SSH access</a></h3>
            <p>開發者透過 <code>list_vms</code> 與 <code>run_command</code> 兩個工具讓 Claude Chat 取得伺服器 SSH 存取權，解決無法隨時開啟筆電執行 Claude Code 的痛點，並表示此方案同樣適用於 ChatGPT。</p>
            <div className="sourceline"><code>r/ClaudeAI</code><span>·</span><span>05/17 03:47 UTC</span><span>·</span><span style={{color:"var(--success)"}}>情緒：😊 正面</span></div>
          </article>
          <article className="story">
            <h3><a href="https://www.reddit.com/r/ClaudeAI/comments/1tfnqmc/claude_code_contextwindow_clear_after_every_task/" target="_blank" rel="noreferrer">Claude Code context-window: /clear after EVERY task in the codebase or are there edge cases?</a></h3>
            <p>開發者在大型 Shopify 主題 codebase（3–8 MB 原始碼）中使用 Claude Code，探討每次任務完成後是否應強制執行 <code>/clear</code>，以及何時保留上下文反而更有效率。</p>
            <div className="sourceline"><code>r/ClaudeAI</code><span>·</span><span>05/17 04:08 UTC</span><span>·</span><span style={{color:"var(--warn)"}}>情緒：🤔 褒貶不一</span></div>
          </article>
          <article className="story">
            <h3><a href="https://dev.to/vineethnkrishnan/i-treated-skills-like-dotfiles-then-they-started-spawning-subagents-5c64" target="_blank" rel="noreferrer">I treated skills like dotfiles. Then they started spawning subagents.</a></h3>
            <p>開發者分享將 Claude Skills 視為個人化配置（類似 dotfiles）進行管理的心得，並記錄了 skills 意外觸發子 agent 派生的實際案例，探討此行為的邊界與控制策略。</p>
            <div className="sourceline"><code>dev.to / #claudecode</code><span>·</span><span>05/17 01:50 UTC</span><span>·</span><span style={{color:"var(--warn)"}}>情緒：🤔 褒貶不一</span></div>
          </article>
          <article className="story">
            <h3><a href="https://www.reddit.com/r/ClaudeAI/comments/1tf4ar0/made_a_tool_that_tells_you_what_your_ai_agent/" target="_blank" rel="noreferrer">Made a tool that tells you what your AI agent actually did to your codebase</a></h3>
            <p>開發者釋出 <code>shipcheck</code>，可讀取 Claude Code 或 Cursor 的 session log，輸出費用分解、檔案修改熱圖與安全掃描，不到一秒完成且完全離線；作者特別指出 Claude 常將 <code>@anthropic-ai/sdk</code> 誤寫為 <code>@anthropic/sdk</code> 的 package hallucination 問題。</p>
            <div className="sourceline"><code>r/ClaudeAI</code><span>·</span><span>05/16 12:14 UTC</span><span>·</span><span style={{color:"var(--success)"}}>情緒：😊 正面</span></div>
          </article>
        </section>

        <section id="pricing" className="feed__section">
          <SectionH label="付 費 方 案 動 態" en="pricing & access" count={2} />
          <article className="story">
            <h3><a href="https://dev.to/vainamoinen/two-multi-account-claude-code-architectures-one-anthropic-accepts-one-they-ban-2om7" target="_blank" rel="noreferrer">Two Multi-Account Claude Code Architectures: One Anthropic Accepts, One They Ban</a></h3>
            <p>文章詳細比較兩種多帳號 Claude Code 使用架構，並明確指出其中一種已被 Anthropic 視為違反使用條款，提醒有規模化使用需求的開發者在帳號管理策略上需注意合規邊界。</p>
            <div className="sourceline"><code>dev.to / #anthropic</code><span>·</span><span>05/16 21:27 UTC</span></div>
          </article>
          <article className="story">
            <h3><a href="https://dev.to/hammermei/how-i-kept-my-ai-family-alive-after-anthropics-claude-p-billing-change-k1i" target="_blank" rel="noreferrer">How I kept my AI family alive after Anthropic's claude -p billing change</a></h3>
            <p>以 AI agent 第一人稱視角撰寫的文章，記錄 Anthropic 調整 <code>claude -p</code>（pipe 模式）計費規則後，如何重新設計工作流程以維持自動化 AI 對話系統的持續運作。</p>
            <div className="sourceline"><code>dev.to / #claudecode</code><span>·</span><span>05/16 22:23 UTC</span></div>
          </article>
        </section>

        <aside className="source-ribbon">
          <span className="source-ribbon__label">SOURCES</span>
          <span className="source-ribbon__item"><span className="src-name">anthropic blog</span><span className="src-n src-n--zero">0</span></span>
          <span className="source-ribbon__sep">·</span>
          <span className="source-ribbon__item"><span className="src-name">github</span><span className="src-n src-n--zero">0</span></span>
          <span className="source-ribbon__sep">·</span>
          <span className="source-ribbon__item"><span className="src-name">hn</span><span className="src-n">18</span></span>
          <span className="source-ribbon__sep">·</span>
          <span className="source-ribbon__item"><span className="src-name">reddit</span><span className="src-n">20</span></span>
          <span className="source-ribbon__sep">·</span>
          <span className="source-ribbon__item"><span className="src-name">google news</span><span className="src-n">7</span></span>
          <span className="source-ribbon__sep">·</span>
          <span className="source-ribbon__item"><span className="src-name">dev.to</span><span className="src-n">16</span></span>
        </aside>
      </article>
    </>
  );
}
window.TodayFeed = TodayFeed;
