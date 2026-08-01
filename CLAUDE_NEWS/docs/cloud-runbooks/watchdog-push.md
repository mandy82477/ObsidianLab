# 雲端 routine：每日產出看門狗推播

`[建立: 2026-08-01]`

執行前先讀 `docs/cloud-runbooks/_shared.md`（環境覆寫、無人值守原則）。

---

## 這個 routine 在補什麼洞

`.github/workflows/daily-watchdog.yml`（15:00 UTC）其實一直有在抓——2026-07-31 web build 被跳過那次，它就正確地紅燈了。問題出在**告警只走 GitHub 的 workflow 失敗信**：那封信混在其他通知裡，使用者實際上是隔天早上打開 Obsidian 才發現網站停在前一天。

偵測層沒問題，**送達層有問題**。本 routine 只做一件事：在台北時間早上把「昨晚那輪到底成不成」推到手機上，而且**只在壞掉時推**。

> 判斷標準：這則通知會不會讓使用者在早上少開一次 Obsidian 才發現問題？若不會（例如一切正常），就不該推。

---

## 排程

`0 23 * * *`（23:00 UTC = **隔日 07:00 台北**）。

時間點的理由：日更 pipeline 13:00 UTC 開跑、約 30–60 分鐘完成，GH watchdog 15:00 UTC 覆核。23:00 UTC 時當日產出早已定案，而使用者剛起床——這是「知道了還來得及在今天處理」的最早時刻。**不要往前挪到 UTC 下午**，那是台北的半夜，把人吵醒換不到任何可行動性。

檢查對象是**執行當下的 UTC 日期**（即剛跑完的那一輪），不是台北日期。

---

## 步驟

1. `cd` 到 repo 的 `CLAUDE_NEWS` 子目錄。
2. 執行健康檢查（判準的唯一來源，與 GH watchdog 共用同一支腳本）：

   ```
   python3 scripts/daily_health_check.py --format push
   ```

3. **exit code 0（產出齊全）** → **不做任何事**，不推播、不 commit、不寫 log。安靜是這個 routine 的正常狀態；每天報平安會讓人在一週內學會忽略它。直接結束並回報「今日產出齊全，未推播」。

4. **exit code 非 0（有缺件）** → 呼叫 `PushNotification` 工具，`message` 直接用腳本輸出的那一行（**不要改寫、不要加前綴**，它已控制在 200 字元內且開頭就是壞掉的段落），`status` 填 `proactive`。

5. 推播後 append 一行到 `src/logs/task_scheduler.log`：

   ```
   [<星期> YYYY/MM/DD hh:mm:ss.00] Watchdog push SENT - <推播訊息原文>
   ```

   然後 `git add src/logs/task_scheduler.log` → commit → push。**只有推播時才寫 log**（步驟 3 的安靜路徑不寫），理由同上：每天一筆平安記錄會把 log 洗掉可讀性。

6. 回報格式（給使用者看的最終訊息）：一行結論 + 檢查到的缺件項目。

---

## 失效保護

- `scripts/daily_health_check.py` 不存在或執行失敗（非 exit 1，而是崩潰／找不到檔案）→ **推播一則說明看門狗本身壞了**（例如 `每日新聞看門狗異常：daily_health_check.py 無法執行`），並照步驟 5 寫 log。看門狗自己死掉而無聲，比它監控的東西壞掉更危險。
- 不要自行判斷「這個缺件應該不重要」而略過推播。判準在腳本裡，routine 不做二次裁量。
- 不要因為近 7 天有舊缺口就推播——腳本已把舊缺口排除在 exit code 之外，只在訊息末尾附帶提及。
