---
description: 完整每日 pipeline：抓新聞 → wiki ingest → 推送 wiki → 建置 web reader → 推送。
argument-hint: [YYYY-MM-DD]
---

# News Pipeline

執行完整每日自動化流程。若提供日期參數（`$ARGUMENTS`），以補跑模式執行該日期；否則以今天為目標。

## 設定

```
REPO_ROOT = C:\Users\Mandy\CLAUDE_OBSIDIAN\ObsidianLab\CLAUDE_NEWS
PYTHON    = C:\Users\Mandy\AppData\Local\Programs\Python\Python313\python.exe
```

若有提供 `$ARGUMENTS`，目標日期為 `$ARGUMENTS`；否則取系統今天日期（YYYY-MM-DD）。

---

## Step 1：新聞聚合器

用 Bash 執行：

```
cd REPO_ROOT\src
PYTHON -m news_aggregator.main [--date TARGET_DATE]
```

- 若有 `$ARGUMENTS`，加上 `--date $ARGUMENTS`
- 成功後應看到 `news/TARGET_DATE.md` 被寫出並 git push
- 若失敗（exit code 非 0），停止並回報錯誤，不繼續後續步驟

---

## Step 2：Wiki Ingest

執行完整 wiki ingest 流程（直接在本 session 執行，不呼叫 `claude -p`）：

1. 讀取 `news/TARGET_DATE.md`
2. 讀取 `wiki/index.md` + `wiki/log.md`，確認未重複 ingest
3. 比對日報內容，找受影響的既有頁面
4. 更新相關 entities/ 和 topics/ 頁面
5. 判斷是否需建立新頁面（entities/ 或 topics/）
6. 更新 `wiki/feature-radar.md`
7. Append 至 `wiki/log.md`
8. 更新 `wiki/index.md`
9. 執行呈現品質審查（見 CLAUDE.md）
10. 輸出 Step 9 核對清單

- Step 2 失敗時記錄但繼續 Step 4（web build 不依賴 wiki）

---

## Step 3：推送 Wiki 變更

用 Bash 執行：

```
git -C REPO_ROOT add wiki/
git -C REPO_ROOT commit -m "wiki: auto-ingest TARGET_DATE"
git -C REPO_ROOT push
```

- 若 wiki 無任何變更，跳過 commit，繼續 Step 4

---

## Step 4：建置 Web Reader

用 Bash 執行：

```
PYTHON REPO_ROOT\scripts\build_web.py
```

- 成功後繼續；若失敗，回報錯誤並跳過推送

---

## Step 5：推送 Web 變更

用 Bash 執行：

```
git -C REPO_ROOT add web_reader/
git -C REPO_ROOT commit -m "web: rebuild TARGET_DATE"
git -C REPO_ROOT push
```

---

## 完成摘要

完成後輸出：

| 步驟 | 結果 |
|------|------|
| Step 1 新聞聚合 | ✅ / ❌ |
| Step 2 Wiki Ingest | ✅ / ❌ |
| Step 3 Wiki 推送 | ✅ / ⏭️ 無變更 / ❌ |
| Step 4 Web 建置 | ✅ / ❌ |
| Step 5 Web 推送 | ✅ / ❌ |
| 目標日期 | TARGET_DATE |

## 注意事項

- 所有 Bash 指令使用絕對路徑，不依賴 PATH 環境變數
- Step 1 失敗時停止整個 pipeline
- Step 2（wiki ingest）失敗時記錄並繼續 Step 4
- Step 4 失敗時跳過 Step 5
- 繁體中文輸出
