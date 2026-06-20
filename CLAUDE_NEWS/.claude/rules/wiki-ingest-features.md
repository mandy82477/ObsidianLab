# Wiki Ingest — 功能記者指南

分類為「功能」的新聞條目由此記者負責。讀此檔後直接操作，需建立新頁面時另讀 `.claude/rules/wiki-ingest-format.md`。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/entities/claude-code.md` | Claude Code 版本更新、新指令/旗標、Breaking change |
| `wiki/entities/bugcrawl.md` | BugCrawl 漏洞偵測工具動態 |
| `wiki/entities/managed-agents.md` | Managed Agents 框架更新 |
| `wiki/entities/openclaw.md` | OpenClaw 第三方整合政策變化 |
| `wiki/entities/claude-design.md` | Claude Design 工具更新 |
| `wiki/entities/claude-security.md` | Claude Security 資安產品動態 |
| `wiki/topics/official-community-gap.md` | 官方功能 vs 社群痛點缺口變化 |
| `wiki/feature-radar.md` | 新增/更新功能條目（**須回報主編彙整**，不直接寫入） |

---

## feature-radar 准入定義 `[加入: 2026-06-15]`

feature-radar 只收**使用者可實際取用、呼叫、設定或執行的官方產物**。收錄前先問：

> 「使用者拿這個能做什麼**具體操作**？」答不出來 → 不收錄。

✅ **屬於功能（收錄）：** 新模型 / 模型能力（可 `--model` 選用）、新指令 / 旗標 / 設定項、新 API / SDK 變更 / 棄用、影響使用方式的 Breaking change。

❌ **不屬於功能（不收錄，改投對應頁面）：**

| 類型 | 範例 | 改投 |
|------|------|------|
| 研究成果 / 論文（無可用介面）| 化學 NMR 分析 | 對應 entities 或略過 |
| 公益 / CSR / 組織 / 人事 | Claude Corps | `topics/anthropic-business` |
| 定價 / 計費 / 配額政策 | Agent SDK 計費切割 | `entities/pricing` |
| 商業合作 / 融資 | TCS / DXC 合作 | `topics/anthropic-business` |
| 純策略表態（無新功能）| HTML 輸出背書 | `topics/community-tech-discussions` 或略過 |

> 模型本身算功能（可選用）；模型的**定價**歸 `entities/pricing`。

---

## feature-radar 動作表

| 情況 | 動作 |
|------|------|
| 日報出現新的官方功能（先過准入定義）| 準備新條目，**回報主編** |
| 已追蹤功能再次出現（討論、工具跟進）| 熱度 +1 格（上限 🔥🔥🔥🔥🔥），回報主編 |
| 出現多個正面使用案例 | 試用價值升級（⏳→⚡→✅），回報主編 |
| 出現重大 bug 或集中負評 | 試用價值降級，回報主編 |
| 功能從 Preview 升格正式 | 考慮升為 ✅，回報主編 |

**新功能條目格式（回報給主編時附上此格式）：**
```markdown
### 功能名稱
**發布：** YYYY-MM-DD（版本號） | **熱度：** 🔥🔥🔥 | **試用價值：** ⚡ 有條件推薦 | **狀態：** Research Preview

**是什麼：** 一句話描述功能用途。

**為何熱：** 社群反應、討論來源、工具跟進情況。

**快速上手：**
\```
最小可用指令或配置範例
\```

**注意事項：** 已知限制或使用前提。
```

---

## 本週推薦自動更新規則 `[加入: 2026-06-20]`

每次 ingest 後，主編在彙整 `wiki/feature-radar.md` 時一併覆寫 `## ⭐ 本週推薦` section。

**選取邏輯（依序）：**
1. 從全覽表選出熱度 🔥🔥🔥🔥 以上、試用價值 ✅ 或 ⚡ 的條目
2. 依熱度降序，同熱度時 ✅ 優先於 ⚡
3. 取前 3 名

**防霸榜規則：** 若某條目已連續在本週推薦超過 7 天，且今日 ingest 未更新其熱度或試用價值，強制換為下一順位條目。

**格式（固定，覆寫整個 section）：**
```markdown
## ⭐ 本週推薦

- **[功能名稱]**（熱度 🔥🔥🔥🔥🔥）：一句話說明適合誰、能做什麼
- **[功能名稱]**（熱度 🔥🔥🔥🔥）：…
- **[功能名稱]**（熱度 🔥🔥🔥🔥）：…
```

若今日 ingest 無新功能且現有推薦均未超過 7 天，保持原內容不動。

---

## 版本更新收錄判斷

版本號本身不是收錄理由，**必須有至少一項使用者端的具體異動**才進 feature-radar：

| 情況 | 判斷 | 處置 |
|------|------|------|
| 純 bug fix / reliability（無具體功能說明）| ❌ 不收錄 | 記入 `entities/claude-code` 版本表 |
| 內部基礎設施更新 | ❌ 不收錄 | 略過 |
| 單一 bug 的 hotfix（已屬於另一功能的修正）| ❌ 不收錄 | 附記在對應功能條目「注意事項」 |
| 有新指令 / 新旗標 / Breaking change | ✅ 收錄 | 正常建立條目 |
| API 棄用 / 重大 SDK 變更 | ✅ 收錄 | 以「SDK / 棄用」為主題建立條目 |

---

## 回報格式

```
## 功能 記者回報
更新頁面：[list]
feature-radar 新增：[條目標題 or 無]
index.md 狀態變更：[page: 舊狀態 → 新狀態 or 無]
新增頁面：[filepath or 無]
```
