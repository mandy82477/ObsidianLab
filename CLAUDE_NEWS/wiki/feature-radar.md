# 功能熱度雷達

追蹤 Claude / Claude Code 每個新發布功能的社群熱度、試用價值與快速上手方式。
每次 ingest 後由 LLM 維護：新增功能、更新熱度、補充社群回饋。

**最後更新：** 2026-05-16（含 5/16 ingest 更新）

---

## 評分說明

| 指標 | 說明 |
|------|------|
| 🔥 熱度 | 1–5 格，依來源數量、討論量、持續天數、社群工具跟進情況綜合評分 |
| 試用價值 | ✅ 推薦 / ⚡ 有條件推薦 / ⏳ 觀望 / ❌ 暫不推薦 |
| 狀態 | 正式發布 / Research Preview / 公開測試 / 限制存取 |

**熱度計分基準：**
- 🔥 — 單次提及，討論有限
- 🔥🔥 — 2–3 個來源，短期討論
- 🔥🔥🔥 — 多來源 + 持續 2 天以上，或有社群工具跟進
- 🔥🔥🔥🔥 — 廣泛討論 + 社群工具爆發 / 大會主角功能
- 🔥🔥🔥🔥🔥 — 里程碑事件，跨平台持續多日，改變開發者工作流

---

## 📋 功能全覽表（2026-04-25 起）

| 功能 | 發布日期 | 熱度 | 試用價值 | 狀態 |
|------|----------|------|----------|------|
| Plugin 依賴關係強制執行（v2.1.143） | 2026-05-16 | 🔥 | ✅ 推薦 | 正式發布 |
| `claude agents` 細粒度旗標（v2.1.142） | 2026-05-14 | 🔥🔥 | ⚡ 有條件 | 正式發布 |
| `/loop`・`/batch`・`/background` | 2026-05-14 | 🔥🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| `/goal` 指令 | 2026-05-12 | 🔥🔥🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| Agent View | 2026-05-12 | 🔥🔥🔥 | ⚡ 有條件 | Research Preview |
| Managed Agents（全套） | 2026-05-11 | 🔥🔥🔥🔥🔥 | ⚡ 有條件 | 正式發布 |
| macOS Computer Use | 2026-05-03 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| Claude Code Sandboxing | 2026-05-10 | 🔥🔥🔥 | ⚡ 有條件 | 正式發布 |
| 操作安全 + `hard_deny` | 2026-05-09 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| Claude Security（公開 Beta） | 2026-05-06 | 🔥🔥🔥 | ⚡ 有條件推薦 | 公開測試 |
| Claude Connectors 創意工作 | 2026-05-04 | 🔥🔥 | ⚡ 有條件 | 正式發布 |
| MCP `alwaysLoad` | 2026-04-28 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| `worktree.baseRef` 設定 | 2026-05-08 | 🔥 | ⚡ 有條件 | 正式發布 |
| Claude Design | 2026-04-27 | 🔥🔥 | ❌ 暫不推薦 | 初期（問題多）|
| Dreaming 記憶整合 | 2026-05-07 | 🔥🔥🔥🔥 | ⏳ 觀望 | Research Preview |
| Outcomes 規格驗證 | 2026-05-07 | 🔥🔥🔥🔥 | ⚡ 有條件 | 公開測試 |

---

## 🆕 最新功能（2026-05）

### Plugin 依賴關係強制執行 — v2.1.143
**發布：** 2026-05-16（v2.1.143） | **熱度：** 🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** `claude plugin disable` 指令新增依賴關係強制執行機制——當目標 plugin 被其他已啟用 plugin 依賴時，指令將拒絕執行並提示完整的停用鏈建議指令，防止工具鏈因單一 plugin 被停用而損壞。

**快速上手：**
```bash
# 若 plugin-A 被 plugin-B 依賴，嘗試停用時 Claude Code 會提示：
claude plugin disable plugin-A
# → 拒絕執行，提示：先執行 claude plugin disable plugin-B，再執行 claude plugin disable plugin-A

# 按建議的停用鏈逐步執行即可安全停用
```

**注意事項：** 對維護複雜 plugin 組合（3 個以上互相依賴）的用戶尤為重要；升級後應測試現有停用腳本是否需要調整順序。

---

### `claude agents` 細粒度旗標 — v2.1.142
**發布：** 2026-05-14（v2.1.142） | **熱度：** 🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：**
`claude agents` 指令新增 8 個啟動旗標，開發者可直接在指令列指定：
- **`--model`** — 指定子代理使用的模型版本
- **`--add-dir`** — 指定額外工作目錄
- **`--settings`** — 指定設定檔路徑
- **`--mcp-config`** — 指定 MCP 配置路徑
- **`--plugin-dir`** — 指定插件目錄
- **`--permission-mode`** — 指定權限模式
- **`--effort`** — 指定任務努力等級
- **`--dangerously-skip-permissions`** — 跳過權限確認（謹慎使用）

**為何有用：** 過去啟動子代理需依賴設定檔，現可完全透過指令列完成細粒度配置，大幅降低多代理腳本化啟動的設定摩擦；與 Managed Agents 架構配合使用效果最佳。

**快速上手：**
```bash
# 指定模型 + MCP 配置啟動子代理
claude agents --model claude-opus-4-7 --mcp-config ./mcp-config.json

# 限制工作目錄 + 安全模式
claude agents --add-dir ./src --permission-mode cautious
```

**注意事項：** `--dangerously-skip-permissions` 會跳過所有確認提示，只在完全受控的 CI 環境中使用；建議搭配 `--permission-mode` 明確定義邊界。

---

### `/loop`、`/batch`、`/background` 指令 — 完整自主執行套件
**發布：** 2026-05-14（官方文件上線） | **熱度：** 🔥🔥🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：**
與 `/goal` 共同構成官方自主執行指令套件：
- **`/loop`** — 固定循環執行，不設完成條件，持續迴圈直到手動停止
- **`/batch`** — 批次任務，對一組輸入依序執行相同工作流
- **`/background`** — 背景執行，讓 Claude 在後台獨立運行不阻斷終端機

**為何熱：** 官方文件同日上線，與 `/goal` 相互呼應，形成完整自主執行指令集；Claude Code 負責人 Cat Wu 同日接受訪問指出「AI 下一步是主動性（proactivity）」，完全呼應此方向；標誌 Claude Code 產品定位正式從「每輪互動」轉向「設定目標、自主完成」的 agent 開發範式。

**快速上手：**
```
# 固定循環（直到手動 Ctrl+C 停止）
/loop 每隔 5 分鐘讀取 logs/app.log 並報告異常

# 批次任務（對一組檔案執行）
/batch src/components/*.tsx 為每個元件新增 JSDoc 型別定義

# 背景執行
/background 持續監控 build/output.log，偵測到 ERROR 時建立 GitHub issue
```

**注意事項：** `/loop` 不設自動終止條件，建議搭配費用監控工具（Ledger、Tokenyst）設定上限；`/batch` 的進度可透過 Agent View 追蹤；與 6/15 信用池制費用結構同步，自動化工作流的成本評估更為重要。

---

### `/goal` 指令 — Fire-and-Forget 自動化
**發布：** 2026-05-12（v2.1.139） | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：**
設定可驗證的完成條件後，每輪執行結束由一個小型快速模型自動判斷條件是否成立；未達成則自動開始下一輪，直到目標完成為止。適合有明確「終態」的長時間任務。

**為何熱：** Code with Claude 大會官方主角功能（2026-05-12）；Reddit 與 HN 廣泛討論；官方文件再度擴充（2026-05-14），搭配 `/loop`・`/batch`・`/background` 形成完整自主執行套件；持續跨日覆蓋，社群稱之為 Claude Code 進入「非同步工作流時代」的標誌性版本。

**最適合的場景：**
- 大批量重構（TypeScript 型別錯誤全部清零）
- 測試全通過（CI green）
- 模組遷移（某目錄下所有 `.js` 改為 `.ts`）

**快速上手：**
```
# 在 Claude Code 中輸入：
/goal 所有 TypeScript 型別錯誤歸零，執行 tsc --noEmit 零報錯

# 或：
/goal tests/unit/ 所有測試通過，npm test 零失敗

# 或：
/goal src/legacy/ 目錄內所有 require() 改為 ES Module import，且不破壞現有測試
```

**注意事項：** 目標條件必須是可機器驗證的（有指令可跑），不適合純主觀判斷的任務（如「優化程式碼可讀性」）。

---

### Agent View — 多 Session 統一管理面板
**發布：** 2026-05-12（v2.1.139） | **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** Research Preview

**是什麼：**
統一面板管理所有並行 Claude Code 工作階段的即時狀態（執行中 / 等待輸入 / 已完成），解決過去需要手動管理多個終端機視窗的痛點。

**為何熱：** 與 `/goal` 同一版本發布，是 Managed Agents 正式生產化的配套工具；多代理工作流的使用者首次有官方 UI 可用。

**適合：** 同時跑 3 個以上 Claude Code agent 的重度使用者；目前仍為 Research Preview，功能可能變動。

**快速上手：**
```bash
# 啟用 Agent View 面板
claude agents

# 或在現有 session 中執行
# 面板會顯示所有並行 session 的狀態與等待輸入提示
```

**社群反應：** 初步正面，但部分使用者仍偏好 mux0 / Nimbalyst 等社群工具提供的更細緻控制。

**v2.1.140 補充（2026-05-13）：** `subagent_type` 現在支援大小寫不敏感及分隔符號不敏感匹配（`"Code Reviewer"` → `code-reviewer`），進一步降低多代理配置摩擦。

---

### Managed Agents — 官方多代理托管框架
**發布：** 2026-05-11（正式發布，從 Research Preview 升格） | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：**
Anthropic 官方 Agent 框架，提供三項核心能力：
- **Dreaming**：Agent 在任務間隙自動鞏固記憶（仍為 Research Preview）
- **20 路子代理並行**：最高 20 個子代理同時執行
- **Outcomes 規格驗證**：Agent 完成後自我驗證是否符合預設規格

**為何熱：** 跨越 3 週持續覆蓋（4/28 → 5/11 → 5/12）；Code with Claude 大會主題；Reddit 70 天自建 multi-agent 開發者案例廣傳；Python/TypeScript SDK 同步支援。

**適合：** 需要長時間、跨 session、可驗證輸出的 Production-level Agent 工作流；**不適合**快速原型或一次性任務。

**快速上手：**
```python
# Python SDK v0.100.0+
import anthropic

client = anthropic.Anthropic()

# 建立 Managed Agent
agent = client.managed_agents.create(
    name="my-agent",
    model="claude-opus-4-20260501",
    instructions="你是一個專注於 Python 重構的工程師代理"
)

# 設定 Outcome 規格
task = client.managed_agents.tasks.create(
    agent_id=agent.id,
    prompt="重構 src/legacy/ 下所有函數至符合 type hints",
    outcomes=["所有函數有完整 type hints", "mypy 零錯誤"]
)
```

```typescript
// TypeScript SDK v0.95.0+
import Anthropic from '@anthropic-ai/sdk';
const client = new Anthropic();

const task = await client.managedAgents.tasks.create({
  agentId: agent.id,
  prompt: '...',
  outcomes: ['...']
});
```

**社群關鍵洞察：** 自建 multi-agent 開發者指出「任務簡報（brief）的撰寫品質才是系統成敗的核心」，非框架選擇。官方托管 vs 社群自組架構差距仍在社群持續比較中。

**2026-05-13 更新：** Boris Cherny 公開每晚讓**數千個 AI 子代理**執行「深度工作」的工作流（白天設框架 → 夜間數千子代理並行深入研究 → 早上整合），被 Business Insider 主流媒體報導。這是 Managed Agents 20 路並行能力的極端個人應用案例，也驗證了官方工具正在降低大規模子代理配置的摩擦（v2.1.140 的 `subagent_type` 不敏感匹配）。

**相關頁面：** [[entities/managed-agents]]

---

### macOS Computer Use — 全桌面自動化
**發布：** 2026-05-03 | **熱度：** 🔥🔥🔥 | **試用價值：** ✅ 推薦（macOS 用戶） | **狀態：** 正式發布

**是什麼：**
Claude Code / Claude Cowork 可直接控制 macOS 桌面滑鼠與鍵盤，從純程式碼助理升格為全桌面自動化代理，可操作任何 GUI 應用程式。

**快速上手：**
```
# 在 Claude Code 或 Claude Cowork 中直接描述桌面任務：
「打開 Figma，將 designs/ 資料夾中所有 frame 匯出為 PNG」
「在 Terminal 中執行 npm test，截圖結果後附上報告」
```

**注意事項：** 不可逆桌面操作（刪除檔案、送出表單）建議在描述中加上「操作前請先確認」；v2.1.136 的 `hard_deny` 機制可設定禁止操作邊界。

---

### Claude Code Sandboxing — 官方沙箱隔離
**發布：** 2026-05-10（官方文件正式發布） | **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：**
透過 OS 層級原語（primitives）對 bash 工具實施檔案系統與網路隔離。在 session 開始時預先定義操作邊界，讓 Claude Code 在邊界內自由執行並縮小意外破壞的半徑。

**為何熱：** 在 CVE-2026-39861 沙箱逃逸漏洞曝光（2026-05-08）的背景下，官方文件及時補位；安全意識高的團隊高度關注。

**快速上手：**
```json
// .claude/settings.json — 限制 bash 工具只能存取 src/ 和 tests/
{
  "sandbox": {
    "enabled": true,
    "allowedPaths": ["src/", "tests/", "package.json"],
    "networkAccess": false
  }
}
```

**適合：** 在生產環境或多人共用機器上執行 Claude Code；不適合需要廣泛系統存取的任務（如環境設定、安裝依賴）。

---

### v2.1.136 操作安全 + `hard_deny` 機制
**發布：** 2026-05-09 | **熱度：** 🔥🔥🔥 | **試用價值：** ✅ 推薦（所有使用者） | **狀態：** 正式發布

**是什麼：**
系統提示新增「操作安全與如實回報」機制（+525 tokens）：
- 不可逆或對外操作須先獲授權確認
- 刪除前需檢視目標
- 必須如實回報跳過的步驟與未通過的測試
- `hard_deny`：使用者可設定無條件安全邊界（不可被覆蓋）

**為何值得關注：** 所有依賴 Claude 自主授權的現有工作流都可能受影響；`hard_deny` 是目前唯一能在提示詞層面設定強制邊界的機制。

**快速上手：**
```json
// .claude/settings.json — 設定 hard_deny 規則
{
  "rules": [
    {
      "type": "hard_deny",
      "pattern": "rm -rf",
      "reason": "禁止強制刪除操作"
    },
    {
      "type": "hard_deny",
      "pattern": "git push --force",
      "reason": "禁止強制推送"
    }
  ]
}
```

---

## 🔍 熱度追蹤說明（給 LLM）

每次 ingest 後，請執行以下步驟更新此頁：

1. **新增功能**：若日報出現新的 Claude 功能（🔧 技術更新 或官方公告），在「最新功能」區塊新增條目，包含：
   - 發布日期、版本號
   - 初始熱度評分（依單日討論量給 🔥–🔥🔥🔥）
   - 試用價值初評（有足夠資訊才評，否則標「⏳ 觀望」）
   - 快速上手（若日報有具體指令或 API）

2. **更新熱度**：若已追蹤功能在新日報再次出現（社群討論、新工具跟進、問題回報），熱度 +1 格（上限 🔥🔥🔥🔥🔥）

3. **更新試用價值**：
   - 若出現多個正面使用案例 → 升級（⏳→⚡→✅）
   - 若出現重大 bug、負面評價集中 → 降級（✅→⚡→⏳→❌）
   - 若進入正式發布（從 Preview 升格）→ 考慮升為 ✅

4. **更新全覽表**：同步更新底部全覽表的熱度與狀態欄

5. **更新「最後更新」日期**
