# .claude/reporter-rules/

wiki 記者 subagent 與 ingest／lint 主編**明文 Read** 的規則檔。**沒有自動載入**——放在這裡就不會佔用每個 session 的開場預算，要用的人自己讀。

誰讀哪一份：

- **六類記者＋衍生記者**：由 `.claude/agents/` 下各自的角色檔（`wiki-reporter-models.md` 等）「開始前必讀」清單指名（共用規則 `wiki-reporter-shared.md`、自己那份 `wiki-ingest-<類別>.md`、建頁時的 `wiki-ingest-format.md`）
- **主編**：由 `.claude/commands/wiki-ingest.md`、`wiki-lint.md`、`wiki-backfill.md` 等 command 內文指名（`wiki-ingest.md` 為主編指南，`*-lint.md` 為週更專用，`wiki-lint-inquiry.md`／`wiki-lint-adversarial.md` 為 lint 特定步驟）

與 `.claude/rules/` 的分工：`.claude/rules/` 放**主 session 自己會用到**、由 `paths:` frontmatter 觸發載入的規則（目前為 `claude-md-edit.md`、`web-reader-design.md`、`collection-scope.md`）；本資料夾的檔案一律不帶 `paths:`。

改動這裡的檔案後照樣跑 `/review-commands`——`scripts/check_rules.py` 與 `.claude/review-registry.json` 的 glob 已涵蓋本資料夾。
