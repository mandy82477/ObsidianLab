# 官方功能熱度雷達

追蹤 Anthropic 官方發布的 Claude / Claude Code 功能熱度、試用價值與快速上手方式。
僅收錄官方 changelog、release note 或官方公告來源；社群工具見 [[topics/community-tech-tools]]。
每次 ingest 後由 LLM 維護：新增功能、更新熱度、補充社群回饋。

**最後更新：** 2026-06-15（今日無符合准入定義的新官方功能；Agent SDK 計費切割正式生效但屬計費政策歸 [[entities/pricing]]；Claude Corps 歸 [[topics/anthropic-business]]）

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
| **Claude Code v2.1.175**（`enforceAvailableModels` 企業管控） | 2026-06-12 | 🔥🔥 | ✅ 推薦 | 正式發布（企業管理員可鎖定可用模型白名單並同步限制預設模型，防繞過）|
| **Claude Code v2.1.173**（Fable 5 模型名稱修復） | 2026-06-11 | 🔥 | ✅ 推薦 | 正式發布（`[1m]` 後綴自動移除；誤報沙盒錯誤修正）|
| **Claude Fable 5**（Mythos 架構公開版，$10/$50 per M token） | 2026-06-09 | 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布（6/22 前訂閱包含；之後消費制；護欄 fallback 至 Opus 4.8 < 5% session；護欄政策 6/11 部分修改：LLM 研究限制改為可見；資安研究護欄仍過激）|
| Python SDK v0.109.1（`frontier_llm` refusal 類別） | 2026-06-09 | 🔥 | ✅ 推薦 | 正式發布（Fable 5 安全分類器相關 refusal API 補齊）|
| Claude Code v2.1.170（Fable 5 支援） | 2026-06-09 | 🔥🔥 | ✅ 推薦 | 正式發布（Claude Code terminal 可切換 Fable 5）|
| Claude Code v2.1.169 `--safe-mode` 旗標 | 2026-06-08 | 🔥🔥 | ✅ 推薦 | 正式發布（停用所有客製化設定，MCP/hooks/skills/CLAUDE.md；故障排除利器）|
| Google Colab CLI 整合 Claude Code / Codex | 2026-06-08 | 🔥🔥 | ✅ 推薦 | 正式發布（降低 Colab 使用 AI coding agent 門檻）|
| Python SDK v0.107.1（foundry x-api-key header 修復） | 2026-06-07 | 🔥 | ✅ 推薦 | 正式發布（Bedrock Foundry 使用者應升級）|
| Python SDK v0.106.0（Claude Opus 4.1 標記棄用） | 2026-06-06 | 🔥 | ✅ 推薦 | 正式發布（開發者應遷移至新版模型 ID）|
| Claude Code v2.1.162（`waitingFor` 可見性 + `--tools` Grep/Glob 目錄遍歷） | 2026-06-04 | 🔥🔥 | ✅ 推薦 | 正式發布（agent 監控可見性顯著改善）|
| Claude Code v2.1.161（OTEL metrics 標籤 + claude agents 改善） | 2026-06-03 | 🔥🔥 | ✅ 推薦 | 正式發布（企業可觀測性提升）|
| Claude Code v2.1.160（shell 安全修復 + `workflow`→`ultracode` rename） | 2026-06-02 | 🔥🔥🔥 | ✅ 推薦 | 正式發布（⚠️ Breaking: `workflow` 更名為 `ultracode`）|
| Claude Code v2.1.158（Auto mode on Bedrock/Vertex/Foundry） | 2026-05-30 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| Claude Opus 4.8（SWE-bench Pro 69.2%、1M context、Fast Mode 1/3 費用） | 2026-05-28 | 🔥🔥🔥🔥🔥 | ⚡ 有條件推薦 | 正式發布 |
| Dynamic Workflows（最多 1,000 平行子代理） | 2026-05-28 | 🔥🔥🔥🔥 | ❌ 暫不推薦 | Research Preview（UltraCode 1.7M token bug，無退款）|
| `skipLfs` 選項 + npm 版本通知（v2.1.153） | 2026-05-28 | 🔥 | ⚡ 有條件推薦 | 正式發布 |
| Coordinator 模式 + `/code-review --fix`（v2.1.152） | 2026-05-27 | 🔥🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| 小企業 Skills（31 個官方 Skills） | 2026-05-24 | 🔥🔥🔥 | ✅ 推薦 | 正式發布 |
| `/code-review`（原 `/simplify`，v2.1.146） | 2026-05-21 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| `claude agents --json`（v2.1.145） | 2026-05-20 | 🔥🔥 | ✅ 推薦 | 正式發布 |
| 自架沙箱 + MCP 隧道（完整文件） | 2026-05-22 | 🔥🔥🔥🔥 | ⚡ 有條件推薦 | 公開測試（文件完整）|
| `/resume` 背景 session 擴展（v2.1.144） | 2026-05-19 | 🔥 | ✅ 推薦 | 正式發布 |
| Proactive Workflows | 2026-05-18 | 🔥🔥🔥 | ⏳ 觀望 | 公告（細節待確認）|
| Capability Curve | 2026-05-18 | 🔥🔥 | ⏳ 觀望 | 公告（細節待確認）|
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

## 🆕 最新功能（2026-06）

### Claude Code v2.1.175（`enforceAvailableModels` 企業管控）
**發布：** 2026-06-12（v2.1.175） | **熱度：** 🔥🔥 | **試用價值：** ✅ 推薦 | **狀態：** 正式發布

**是什麼：** 新增 `enforceAvailableModels` 管理設定——啟用後，`availableModels` 白名單同時限制預設模型的解析，避免管理員設定的模型限制被繞過。針對企業管理場景，確保組織控管政策的完整性。

**為何熱：** 解決企業部署 Claude Code 時的治理缺口：管理員設定了模型白名單，但預設模型解析仍可能繞過限制。對有合規需求的金融、醫療、政府機構部署場景尤其重要。

**快速上手：**
```json
// .claude/config.json（企業管理員設定）
{
  "availableModels": ["claude-fable-5-20260609", "claude-opus-4-8-20260528"],
  "enforceAvailableModels": true
}
```

**注意事項：** 僅影響企業管理員設定的 `availableModels` 白名單；個人開發者無需關注此設定。

---

### Claude Fable 5（Mythos 架構公開版）
**發布：** 2026-06-09 | **熱度：** 🔥🔥🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** 正式發布

**是什麼：** Anthropic 首款向大眾開放的 Mythos 級模型。Fable 5 = Mythos 5 模型權重 + 安全分類器護欄，觸發時靜默 fallback 至 Opus 4.8（< 5% session）。定價 $10/$50 per million token，context 1M，max output 128K。6/22 前含括於訂閱方案。

**為何熱：** HN 2,448 分，近 2,000 評論。幾乎所有 benchmark SOTA，任務越長期越複雜優勢越大。首次讓開發者在一般工作流中使用 Mythos 等級推理能力。

**快速上手：**
```bash
# Claude Code terminal 切換 Fable 5
claude --model claude-fable-5-20260609

# 或在 Claude Code 設定中選擇 Fable 5 模型
```

**注意事項：** 前沿 LLM 開發工作（訓練 pipeline、推論研究、ML 加速器設計）會觸發靜默護欄，輸出品質降低且不告知；6/22 後需消費制計費；30 天資料保留政策適用於所有平台。見 [[entities/fable-5]]、[[entities/mythos]]。

---

> 2026-05 功能詳細條目已封存，見 [[feature-radar-archive-2026-05]]

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
